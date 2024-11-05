# Clustering Countries for Development Aid

## Project Overview
This project utilizes unsupervised learning techniques to categorize countries based on critical socio-economic and health metrics. The analysis is part of an initiative for HELP International, an NGO dedicated to combating poverty and providing essential support in underprivileged regions.

## Dataset
The dataset used for this analysis was sourced from [Kaggle](https://www.kaggle.com/), providing a comprehensive view of the socio-economic and health landscape across different countries.

### Key Features of the Dataset
- **country**: Name of the country
- **child_mort**: Death of children under 5 years of age per 1000 live births
- **exports**: Exports of goods and services per capita as a percentage of GDP per capita
- **health**: Total health spending per capita as a percentage of GDP
- **imports**: Imports of goods and services per capita as a percentage of GDP per capita
- **income**: Net income per person
- **inflation**: Annual growth rate of total GDP
- **life_expec**: Average lifespan of a newborn child given current mortality patterns
- **total_fer**: Number of children each woman would bear if current age-fertility rates remain unchanged
- **gdpp**: GDP per capita, calculated as total GDP divided by the total population

## Objective
To identify countries in the direst need of aid by analyzing various socio-economic and health factors that determine overall development.

## Methodology
1. **Data Preprocessing**: Log transformations were applied to certain features to manage skewness.
2. **Dimensionality Reduction**: PCA was utilized to reduce the dataset while retaining 95% of the variance.
3. **Clustering**: KMeans clustering was employed to identify patterns within the data. The optimal number of clusters was determined, and clustering quality was evaluated using silhouette scores and the Davies-Bouldin index.
4. **Results**: Identified 19 countries that are in dire need of aid namely: 'Angola', 'Benin', 'Burkina Faso', 'Cameroon', 'Central African Republic', 'Chad', 'Congo Dem. Rep.', "Cote d'Ivoire", 'Equatorial Guinea', 'Guinea', 'Guinea-Bissau', 'Haiti', 'Lesotho', 'Mali', 'Mauritania', 'Mozambique', 'Niger', 'Nigeria', 'Sierra Leone'

## Results
The clustering results provide a clear direction for the CEO of HELP International to allocate resources strategically and effectively, significantly enhancing the impact of their humanitarian efforts.

## Acknowledgments
- HELP International for their commitment to humanitarian efforts.
- Kaggle for providing the dataset.
