# 🌍 **Clustering Countries for Development Aid**  

## **1. Introduction**  
Economic and health disparities significantly impact global development, requiring targeted aid distribution. This project leverages **unsupervised learning** to **identify countries in dire need of development aid**, helping NGOs like **HELP International** allocate resources efficiently.  

✅ **Applies KMeans clustering** to group countries based on socio-economic indicators.  
✅ **Uses PCA for dimensionality reduction**, ensuring efficient data analysis.  
✅ **Provides actionable insights** for targeted humanitarian assistance.  

This project offers a **data-driven approach** to **prioritizing international aid efforts** effectively.  

---

## **2. Background**  
HELP International, a global NGO, seeks to **identify countries most in need** of economic and health-related aid. Key challenges include:  

🔹 **Unequal Resource Distribution** – Aid must be **strategically allocated** to maximize impact.  
🔹 **Complex Socio-Economic Indicators** – Multiple **factors affect country development**, requiring advanced analytics.  
🔹 **Data-Driven Decision Making** – Clustering helps **categorize countries based on similar needs**.  

This project addresses these challenges by:  

✅ **Applying clustering techniques** to group similar countries.  
✅ **Reducing dimensionality using PCA** for meaningful pattern identification.  
✅ **Identifying high-risk countries** requiring urgent aid intervention.  

---

## **3. Data Collection and Processing**  
### **📂 Dataset**  
The dataset, sourced from **[Kaggle](https://www.kaggle.com/)**, provides **socio-economic and health metrics** across various countries.  

| Feature | Description |
|---------|------------|
| `country` | Name of the country |
| `child_mort` | Death rate of children under 5 years per 1,000 live births |
| `exports` | Exports of goods and services as a percentage of GDP per capita |
| `health` | Total health spending per capita as a percentage of GDP |
| `imports` | Imports of goods and services as a percentage of GDP per capita |
| `income` | Net income per person |
| `inflation` | Annual GDP growth rate |
| `life_expec` | Average lifespan of a newborn based on mortality patterns |
| `total_fer` | Number of children per woman |
| `gdpp` | GDP per capita |

### **🛠️ Data Preprocessing Steps**  
✅ **Applied log transformation** to normalize skewed features.  
✅ **Checked for missing values** and handled inconsistencies.  
✅ **Standardized numerical variables** for optimal model performance.  

---

## **4. Exploratory Data Analysis (EDA)**  
📊 **Correlation Heatmap**  
- **Analyzed relationships between economic indicators and development needs.**  

📈 **GDP & Child Mortality Trends**  
- **Identified inverse relationships between GDP per capita and child mortality rates.**  

📉 **Impact of Healthcare on Life Expectancy**  
- **Visualized how health spending correlates with increased life expectancy.**  

---

## **5. Model Development**  
### **📌 Machine Learning Techniques Used**  
- **Principal Component Analysis (PCA)** – **Reduced dimensionality** while preserving 95% variance.  
- **KMeans Clustering** – **Segmented countries** into distinct groups based on development indicators.  

### **🛠 Model Training Process**  
✅ **Applied PCA to reduce feature complexity.**  
✅ **Determined optimal clusters using Elbow Method & Silhouette Score.**  
✅ **Trained KMeans to categorize countries based on similar socio-economic traits.**  

---

## **6. Model Evaluation & Results**  
📊 **Performance Metrics:**  
✅ **Silhouette Score** – Measures cluster cohesion and separation.  
✅ **Davies-Bouldin Index** – Evaluates cluster compactness and separation.  

📉 **Key Findings:**  
- **Identified 19 countries in dire need of aid**, including:  
  **Angola, Benin, Burkina Faso, Cameroon, Central African Republic, Chad, DR Congo, Côte d'Ivoire, Guinea, Haiti, Lesotho, Mali, Mozambique, Niger, Nigeria, Sierra Leone, and more.**  
- **Countries with high child mortality and low GDP per capita were prioritized for aid allocation.**  

---

## **7. Visualizing the Results**  
📊 **Cluster Visualization**  
- **Scatter plots & bar charts** illustrated country groupings based on economic indicators.  

📈 **Heatmaps & PCA Explained Variance**  
- **Visualized the importance of each socio-economic feature in clustering.**  

📉 **Top Countries Needing Aid**  
- **Tables & reports showcased the most vulnerable nations for targeted intervention.**  

---

## **8. Future Work**  
+ 🔹 Incorporate **additional socio-political factors** like conflict levels and corruption indexes.  
+ 🔹 Use **hierarchical clustering** for deeper insights into development patterns.  
+ 🔹 Develop an **interactive dashboard** for real-time country analysis.  
+ 🔹 Apply **time-series forecasting** to predict economic changes over time.  

---

## **9. Technologies Used**  
+ 🔹 Programming: Python  
+ 🔹 Machine Learning: Scikit-learn, KMeans Clustering, PCA  
+ 🔹 Data Processing: Pandas, NumPy  
+ 🔹 Data Visualization: Seaborn, Matplotlib  
+ 🔹 Model Evaluation: Silhouette Score, Davies-Bouldin Index  

---

## **10. Connect With Me**  
💼 **LinkedIn:** [Uvietobore Joshua Adjugah](https://www.linkedin.com/in/uvietobore-joshua-adjugah-2b548621a)  
📧 **Email:** uviejosh@gmail.com  

🚀 **Star this repo if you find it useful!** ⭐  
