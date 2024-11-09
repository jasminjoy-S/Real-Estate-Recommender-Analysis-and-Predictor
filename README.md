A Real Estate Application which leverages data science techniques to provide insights, predictions and recommendation.

Deployed : https://real-estate-app-cwq4.onrender.com/

- Data Gathering and cleaning :
The data for this project has been gathered through web scraping. Data of 256 communities and 3000 flats was gathered, cleaned and pre-processed. To prepare the dataset for analysis, a meticulous data cleaning process was undertaken, handling missing values and ensuring consistency. The data was then merged, bringing together information on villa and flats into a unified dataset.

- Feature Engineering :
New features such as additional room indicators, age of possession, furnish details, luxury score etc were introduced to provide a more detailed representation of the properties

- Exploratory Data Analysis (EDA) :
Univariate and multivariate analyses were conducted to uncover patterns and relationships within the data. The use of Pandas Profiling facilitated a deeper understanding of data distribution and structure.

- Feature Selection :
Multiple feature selection techniques were employed to identify the most impactful variables for modeling. These included correlation analysis, random forest, LASSO, permutation importance and recursive feature elimination.

- Model Selection & Productionalization :
In this phase, an exhaustive comparison of various regression models was conducted to determine the most effective model for predicting property prices. The process involved implementing a detailed price prediction pipeline that incorporated encoding methods ensuring robustness and accuracy of the chosen model. The selected model was then deployed using Streamlit, creating an intuitive and user-friendly web interface for end users.

- Building the Analytics Module :
An analytics module was developed to visually represent key insights about the real estate data. Geographical maps, word clouds for amenities, scatter plots, pie charts, and box plots were employed to offer users a comprehensive understanding of the market. 

- Building the Recommender System :
In the process of building the recommender system, three distinct recommendation models were developed, each focusing on different aspects of the real estate dataset - i.e top facilities, price details and location advantages.
