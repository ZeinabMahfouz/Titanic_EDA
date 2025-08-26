import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load data
df = pd.read_csv("Titanic_Train.csv")

# ---------------------------
# Feature engineering
# ---------------------------

# Extract Title from Name (only for Age imputation)
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
rare_titles = df['Title'].value_counts()[df['Title'].value_counts() < 10].index
df['Title'] = df['Title'].replace(rare_titles, 'Rare')
df['Title'] = df['Title'].replace({'Mlle': 'Miss', 'Ms': 'Miss', 'Mme': 'Mrs'})

# Fill missing Age using Title median
df['Age'] = df['Age'].fillna(df.groupby('Title')['Age'].transform('median'))

# Create Age bins
df['AgeGroup'] = pd.cut(
    df['Age'], 
    bins=[0,12,18,35,60,80],
    labels=['Child','Teen','Young Adult','Adult','Senior']
)

# Create Family Size feature
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1  # +1 for the person themselves
df['FamilySizeGroup'] = pd.cut(
    df['FamilySize'],
    bins=[0, 1, 4, 11],
    labels=['Alone', 'Small Family (2-4)', 'Large Family (5+)'],
    right=False
)

# Create more readable labels
df['Gender'] = df['Sex'].map({'male': 'Male', 'female': 'Female'})
df['Class'] = df['Pclass'].map({1: '1st Class', 2: '2nd Class', 3: '3rd Class'})
df['Port'] = df['Embarked'].map({'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'})
df['Survival_Status'] = df['Survived'].map({0: 'Did Not Survive', 1: 'Survived'})

# Fill missing embarkation with most common
df['Port'] = df['Port'].fillna('Southampton')

# ---------------------------
# Streamlit UI
# ---------------------------

st.set_page_config(page_title="Titanic Explorer", page_icon="🚢", layout="wide")

st.title("🚢 Titanic Survival Explorer")
st.markdown("Explore survival patterns by family size, gender, class, and embarkation port")

# ---------------------------
# Sidebar Filters
# ---------------------------

st.sidebar.header("🔍 Filters")

# Family Size Filter
family_sizes = df['FamilySizeGroup'].dropna().unique()
selected_family = st.sidebar.multiselect(
    "👨‍👩‍👧‍👦 Family Size", 
    options=sorted(family_sizes),
    help="Filter by family size groups"
)

# Gender Filter
genders = df['Gender'].dropna().unique()
selected_gender = st.sidebar.multiselect(
    "👤 Gender", 
    options=sorted(genders),
    help="Filter by passenger gender"
)

# Class Filter
classes = df['Class'].dropna().unique()
selected_class = st.sidebar.multiselect(
    "🎫 Passenger Class", 
    options=sorted(classes),
    help="Filter by ticket class"
)

# Embarkation Port Filter
ports = df['Port'].dropna().unique()
selected_port = st.sidebar.multiselect(
    "⚓ Embarkation Port", 
    options=sorted(ports),
    help="Filter by port of embarkation"
)

# Age Group Filter (additional)
age_groups = df['AgeGroup'].dropna().unique()
selected_age = st.sidebar.multiselect(
    "🎂 Age Group", 
    options=list(age_groups),
    help="Filter by age group"
)

# Apply filters
filtered_df = df.copy()

if selected_family:
    filtered_df = filtered_df[filtered_df['FamilySizeGroup'].isin(selected_family)]
if selected_gender:
    filtered_df = filtered_df[filtered_df['Gender'].isin(selected_gender)]
if selected_class:
    filtered_df = filtered_df[filtered_df['Class'].isin(selected_class)]
if selected_port:
    filtered_df = filtered_df[filtered_df['Port'].isin(selected_port)]
if selected_age:
    filtered_df = filtered_df[filtered_df['AgeGroup'].isin(selected_age)]

# ---------------------------
# Main Dashboard
# ---------------------------

# Display current filter status
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Current Selection")
st.sidebar.info(f"Showing **{len(filtered_df)}** of **{len(df)}** passengers")

# Feature selection for detailed analysis
feature_options = {
    "Family Size": "FamilySizeGroup",
    "Gender": "Gender", 
    "Class": "Class",
    "Embarkation Port": "Port",
    "Age Group": "AgeGroup"
}

selected_feature = st.selectbox(
    "Select Feature for Detailed Analysis", 
    options=list(feature_options.keys()),
    help="Choose which feature to analyze in detail"
)

feature_column = feature_options[selected_feature]

# ---------------------------
# Visualizations
# ---------------------------

col1, col2 = st.columns(2)

with col1:
    # Main survival chart
    st.subheader(f"Survival by {selected_feature}")
    
    if len(filtered_df) > 0:
        fig1 = px.histogram(
            filtered_df,
            x=feature_column,
            color="Survival_Status",
            barmode="group",
            text_auto=True,
            title=f"Survival Count by {selected_feature}",
            color_discrete_map={"Survived": "#2E8B57", "Did Not Survive": "#DC143C"}
        )
        fig1.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.warning("No data matches the current filters")

with col2:
    # Survival rate chart
    st.subheader("Survival Rates")
    
    if len(filtered_df) > 0:
        survival_rates = (
            filtered_df.groupby(feature_column)['Survived']
            .agg(['mean', 'count'])
            .reset_index()
        )
        survival_rates['Survival_Rate'] = (survival_rates['mean'] * 100).round(1)
        
        fig2 = px.bar(
            survival_rates,
            x=feature_column,
            y='Survival_Rate',
            text='Survival_Rate',
            title=f"Survival Rate by {selected_feature}",
            color='Survival_Rate',
            color_continuous_scale='RdYlGn'
        )
        fig2.update_traces(texttemplate='%{text}%', textposition='outside')
        fig2.update_layout(xaxis_tickangle=-45, yaxis_title="Survival Rate (%)")
        st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# Summary Statistics
# ---------------------------

st.subheader("📈 Summary Statistics")

col3, col4, col5 = st.columns(3)

if len(filtered_df) > 0:
    overall_survival_rate = (filtered_df['Survived'].mean() * 100).round(1)
    total_passengers = len(filtered_df)
    survivors = filtered_df['Survived'].sum()
    
    with col3:
        st.metric("Overall Survival Rate", f"{overall_survival_rate}%")
    
    with col4:
        st.metric("Total Passengers", total_passengers)
    
    with col5:
        st.metric("Survivors", f"{survivors} of {total_passengers}")

# ---------------------------
# Detailed Data Table
# ---------------------------

st.subheader("📋 Detailed Breakdown")

if len(filtered_df) > 0:
    # Create comprehensive summary table
    summary_stats = (
        filtered_df.groupby(feature_column)
        .agg({
            'Survived': ['count', 'sum', 'mean'],
            'Age': 'mean',
            'Fare': 'mean'
        })
        .round(2)
    )
    
    # Flatten column names
    summary_stats.columns = [
        'Total_Passengers', 'Survivors', 'Survival_Rate', 
        'Avg_Age', 'Avg_Fare'
    ]
    summary_stats['Survival_Rate'] = (summary_stats['Survival_Rate'] * 100).round(1)
    summary_stats = summary_stats.reset_index()
    
    # Rename columns for display
    display_columns = {
        feature_column: selected_feature,
        'Total_Passengers': 'Total',
        'Survivors': 'Survived',
        'Survival_Rate': 'Survival Rate (%)',
        'Avg_Age': 'Avg Age',
        'Avg_Fare': 'Avg Fare (£)'
    }
    summary_stats = summary_stats.rename(columns=display_columns)
    
    st.dataframe(summary_stats, use_container_width=True)

# ---------------------------
# Cross-Analysis Section
# ---------------------------

st.subheader("🔍 Cross-Feature Analysis")

# Allow users to compare two features
col_a, col_b = st.columns(2)

with col_a:
    feature_x = st.selectbox("X-axis Feature", list(feature_options.keys()), key="x_feature")

with col_b:
    feature_y = st.selectbox("Y-axis Feature", list(feature_options.keys()), key="y_feature", index=1)

if feature_x != feature_y and len(filtered_df) > 0:
    # Create heatmap showing survival rates
    cross_table = pd.crosstab(
        filtered_df[feature_options[feature_y]], 
        filtered_df[feature_options[feature_x]], 
        filtered_df['Survived'], 
        aggfunc='mean'
    ) * 100
    
    fig_heatmap = px.imshow(
        cross_table,
        text_auto='.1f',
        aspect="auto",
        title=f"Survival Rate (%) by {feature_y} vs {feature_x}",
        color_continuous_scale='RdYlGn'
    )
    fig_heatmap.update_layout(
        xaxis_title=feature_x,
        yaxis_title=feature_y
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)