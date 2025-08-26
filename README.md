# 🚢 Titanic Survival Explorer

An interactive Streamlit dashboard for exploring survival patterns on the RMS Titanic. This application provides comprehensive analysis of passenger survival rates based on family size, gender, class, embarkation port, and age demographics.

![Titanic Explorer Demo](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

## 📊 Features

### 📈 Exploratory Data Analysis (EDA)
- **Comprehensive Data Overview**: Statistical summaries and data quality assessment
- **Distribution Analysis**: Histograms and box plots for numerical features
- **Correlation Analysis**: Heatmaps showing relationships between variables
- **Missing Data Visualization**: Identify and understand data gaps
- **Survival Pattern Discovery**: Initial insights into factors affecting survival

### Interactive Streamlit Dashboard
- **👨‍👩‍👧‍👦 Family Size**: Filter by family size groups (Alone, Small Family, Large Family)
- **👤 Gender**: Analyze survival patterns by gender
- **🎫 Passenger Class**: Compare survival rates across 1st, 2nd, and 3rd class
- **⚓ Embarkation Port**: Explore differences by port of departure (Southampton, Cherbourg, Queenstown)
- **🎂 Age Groups**: Filter by age demographics (Child, Teen, Young Adult, Adult, Senior)

### Advanced Visualizations
- **Survival Distribution Charts**: Side-by-side comparison of passenger counts and survival rates
- **Interactive Heatmaps**: Cross-feature analysis between any two demographic factors
- **Real-time Filtering**: Dynamic updates based on selected criteria
- **Color-coded Results**: Intuitive green/red color scheme for survival status

### Data Analysis Tools
- **Summary Statistics**: Key metrics including overall survival rate and passenger counts
- **Detailed Breakdowns**: Comprehensive tables with survival rates, average age, and fare information
- **Data Export**: Download filtered datasets as CSV files
- **Cross-Feature Analysis**: Compare survival patterns across multiple demographic factors

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/titanic-survival-explorer.git
   cd titanic-survival-explorer
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install individually:
   ```bash
   pip install streamlit pandas plotly jupyter seaborn matplotlib scikit-learn
   ```

3. **Explore the data (Optional but Recommended)**
   ```bash
   jupyter notebook EDA/Titanic_EDA.ipynb
   ```

4. **Run the Streamlit application**
   ```bash
   streamlit run Streamlit_App/Titanic_streamlit.py
   ```

5. **Download the Titanic dataset**
   - Place your `Titanic_Train.csv` file in the `Data/` directory
   - You can download the dataset from [Kaggle's Titanic Competition](https://www.kaggle.com/c/titanic/data)

6. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

## 📁 Project Structure

```
titanic-survival-explorer/
│
├── 📊 EDA/
│   ├── Titanic_EDA.ipynb            # Jupyter notebook with exploratory analysis
│   ├── EDA_Report.html              # HTML export of EDA findings
│   └── visualizations/              # Generated plots and charts
│       ├── correlation_matrix.png
│       ├── survival_by_class.png
│       └── age_distribution.png
│
├── 🚀 Streamlit_App/
│   └── Titanic_streamlit.py         # Main Streamlit application
│
├── 📊 Data/
│   ├── Titanic_Train.csv            # Training dataset
│   ├── Titanic_Test.csv             # Test dataset (if available)
│   └── processed_data.csv           # Cleaned and engineered data
│
├── 📋 Documentation/
│   ├── README.md                    # This file
│   ├── EDA_Summary.md               # Key findings from exploratory analysis
│   └── Data_Dictionary.md           # Detailed feature descriptions
│
├── requirements.txt                 # Python dependencies
└── .gitignore                      # Git ignore file
```

## 🔬 Exploratory Data Analysis (EDA)

The project includes comprehensive exploratory data analysis to understand the dataset before building the interactive dashboard.

### 📊 EDA Highlights

#### Data Quality Assessment
- **Dataset Overview**: 891 passengers with 12 features
- **Missing Data Analysis**: Age (19.9%), Cabin (77.1%), Embarked (0.2%)
- **Data Types**: Mixed numerical and categorical features
- **Outlier Detection**: Fare and Age outlier identification

#### Key Findings
- **Overall Survival Rate**: 38.4% of passengers survived
- **Gender Impact**: Women had 74.2% survival rate vs 18.9% for men
- **Class Influence**: 1st class (62.9%) > 2nd class (47.3%) > 3rd class (24.2%)
- **Family Size Effect**: Small families (2-4 members) had higher survival rates
- **Age Patterns**: Children under 12 had better survival chances

#### Statistical Insights
- **Correlation Analysis**: Strong negative correlation between class and survival
- **Fare Distribution**: Highly skewed with luxury passengers paying significantly more
- **Port Analysis**: Cherbourg passengers had higher survival rates (55.4%)

### 📈 EDA Workflow
1. **Data Loading and Overview**
2. **Missing Data Visualization**
3. **Univariate Analysis** (distributions, counts)
4. **Bivariate Analysis** (survival by features)
5. **Correlation Analysis**
6. **Feature Engineering Insights**
7. **Key Findings Summary**

### 🔍 How to Use the EDA
1. Open `EDA/Titanic_EDA.ipynb` in Jupyter Notebook
2. Run all cells to reproduce the analysis
3. Review the generated visualizations in `EDA/visualizations/`
4. Check `Documentation/EDA_Summary.md` for key takeaways

## 📈 Dataset Information

This application uses the famous Titanic dataset, which includes the following key features:

- **PassengerId**: Unique identifier for each passenger
- **Survived**: Survival status (0 = No, 1 = Yes)
- **Pclass**: Ticket class (1st, 2nd, 3rd)
- **Name**: Passenger name
- **Sex**: Gender
- **Age**: Age in years
- **SibSp**: Number of siblings/spouses aboard
- **Parch**: Number of parents/children aboard
- **Ticket**: Ticket number
- **Fare**: Passenger fare
- **Cabin**: Cabin number
- **Embarked**: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

## 🔧 Features in Detail

### Data Processing
- **Age Imputation**: Missing ages filled using median values by passenger title
- **Family Size Calculation**: Combines SibSp and Parch to create meaningful family size groups
- **Feature Engineering**: Creates readable labels and categories for better analysis

### Interactive Elements
- **Multi-select Filters**: Choose multiple values from any category
- **Dynamic Updates**: All charts and tables update in real-time based on selections
- **Cross-Analysis**: Compare survival rates between any two demographic factors
- **Export Functionality**: Download your filtered analysis results

### Visualizations
- **Grouped Bar Charts**: Compare survivor counts across categories
- **Survival Rate Charts**: Percentage-based analysis with color gradients
- **Heatmaps**: Two-dimensional survival rate comparisons
- **Summary Metrics**: Key statistics displayed prominently

## 💡 Usage Examples

### EDA Workflow
1. **Start with Exploration**: Open the Jupyter notebook to understand data patterns
2. **Review Key Findings**: Check the EDA summary for initial insights
3. **Identify Interesting Patterns**: Note which factors most strongly correlate with survival

### Dashboard Analysis
1. **Overall Survival**: View the app without any filters to see overall patterns
2. **Gender Analysis**: Select only "Female" or "Male" to compare survival rates
3. **Class Comparison**: Filter by different passenger classes to see socioeconomic impacts

### Advanced Exploration
1. **Family Survival**: Use family size filters to explore how traveling alone vs. with family affected survival
2. **Port Analysis**: Compare survival rates by embarkation port
3. **Cross-Feature**: Use the heatmap to see how class and gender together influenced survival

### Research Workflow
1. **Hypothesis Formation**: Use EDA findings to form hypotheses
2. **Interactive Testing**: Use the Streamlit app to test hypotheses interactively
3. **Deep Dive Analysis**: Export filtered data for further statistical analysis

### Data Export
1. Apply your desired filters
2. Click "Download Filtered Data" in the sidebar
3. Use the exported CSV for further analysis in Excel, Python, or R

## 🛠️ Technical Details

### Built With
- **[Streamlit](https://streamlit.io/)** - Interactive web app framework
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[Plotly Express](https://plotly.com/python/plotly-express/)** - Interactive visualizations
- **[Jupyter Notebook](https://jupyter.org/)** - EDA and data exploration
- **[Seaborn](https://seaborn.pydata.org/)** - Statistical data visualization
- **[Matplotlib](https://matplotlib.org/)** - Base plotting library
- **[Python 3.7+](https://www.python.org/)** - Programming language

### Key Libraries
```python
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
```

## 📝 Requirements

Create a `requirements.txt` file with:

```
streamlit>=1.28.0
pandas>=1.5.0
plotly>=5.15.0
jupyter>=1.0.0
seaborn>=0.12.0
matplotlib>=3.6.0
scikit-learn>=1.3.0
numpy>=1.24.0
```

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. **Report Bugs**: Open an issue describing the bug and how to reproduce it
2. **Suggest Features**: Open an issue with your feature request
3. **Submit Pull Requests**: Fork the repo, make changes, and submit a PR

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## 📊 Screenshots

*(Add screenshots of your application here)*

## 🔮 Future Enhancements

### Data Science Extensions
- [ ] Add machine learning model predictions
- [ ] Implement feature importance analysis
- [ ] Include survival probability calculator
- [ ] Add statistical significance tests

### Visualization Improvements
- [ ] Include cabin deck analysis
- [ ] Add more advanced visualizations (3D plots, network graphs)
- [ ] Implement fare analysis by route
- [ ] Add animated time-series visualizations

### Interactive Features
- [ ] Add comparison mode between passenger profiles
- [ ] Implement "what-if" scenario analysis
- [ ] Include passenger story generator
- [ ] Add voice narration of findings

### Technical Enhancements
- [ ] Deploy to cloud platform (Heroku, Streamlit Cloud)
- [ ] Add automated data quality checks
- [ ] Implement caching for better performance
- [ ] Add unit tests and CI/CD pipeline

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset provided by [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)
- Inspiration from the historical tragedy of RMS Titanic
- Built with love using Streamlit and Plotly

## 📞 Contact

Your Name - [@yourusername](https://twitter.com/yourusername) - email@example.com

Project Link: https://github.com/ZeinabMahfouz/Titanic_EDA

---

⭐ **Star this repository if you found it helpful!** ⭐
