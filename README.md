Galaxy Groups Data Analysis

This project was developed as part of my studies in Python and Data Analytics through JetBrains Academy (Hyperskill).

The goal was to explore the properties of compact groups of galaxies using statistical methods and data analysis techniques. Throughout the project, I worked with astronomical datasets to investigate relationships between galaxy morphology, surface brightness, and the distances separating galaxies within groups.

The project was divided into five stages, each focusing on a different aspect of the analysis.

About the Project

Compact groups of galaxies are relatively small systems in which galaxies are located close to one another. Studying these groups can help researchers understand how galaxies interact and evolve.

In this project, I used Python to analyze data related to galaxy morphology, redshift, intra-group light (IGL), and galaxy positions.

The main objective was to explore possible relationships between these characteristics and apply statistical methods to better understand the data.

Technologies Used

* Python
* Pandas
* NumPy
* SciPy
* Matplotlib
* Astropy

Project Development

1. Data Preparation

I started by working with a dataset containing information about compact groups of galaxies.

The data included redshift values, mean surface brightness, and the presence or absence of low surface brightness (LSB) features.

I used Pandas to load the dataset, remove missing values, and calculate the average surface brightness for groups with and without LSB features.

This stage helped me practice basic data cleaning and descriptive statistics.

2. Analysis of Variance (ANOVA)

The second stage focused on investigating whether the presence of LSB features was associated with differences in intra-group light surface brightness.

I applied three statistical tests:

* Shapiro-Wilk test to evaluate normality.
* Fligner-Killeen test to assess the equality of variances.
* One-way ANOVA to compare the mean surface brightness between groups.

This stage helped me understand the assumptions behind statistical tests and how to interpret their results.

3. Isolated Galaxies and Galaxy Groups

In this stage, I compared isolated galaxies with galaxies belonging to compact groups.

I used the Sérsic index, which describes how light is distributed within a galaxy, to investigate differences between the two samples.

The analysis included:

* Histograms of Sérsic index distributions.
* Calculation of the proportion of galaxies with a Sérsic index greater than 2.
* A two-sample Kolmogorov-Smirnov test to compare the distributions.

This helped me explore how statistical methods can be used to compare different populations.

4. Galaxy Morphology and Intra-group Light

The fourth stage focused on examining relationships between galaxy morphology and intra-group light surface brightness.

I calculated the mean Sérsic index and the mean numerical Hubble stage for each galaxy group.

After combining the datasets, I created scatter plots and applied Shapiro-Wilk normality tests and Pearson correlation tests.

This stage gave me more experience with grouping and merging datasets, data visualization, and correlation analysis.

5. Median Projected Separation

The final stage involved calculating the projected median separation between galaxies within compact groups.

Using equatorial coordinates and redshift data, I estimated the physical distances between galaxy pairs.

The analysis involved:

* Initializing a FlatLambdaCDM cosmological model.
* Calculating angular diameter distances.
* Using SkyCoord to determine angular separations between galaxies.
* Converting angular separations into physical distances.
* Calculating the median projected separation for each group.
* Creating a scatter plot to examine the relationship between galaxy separation and surface brightness.
* Applying Shapiro-Wilk normality tests and Pearson correlation analysis.

This was the most technically challenging stage because it combined data analysis with astronomical calculations using Astropy.

Repository Structure

galaxy-groups-data-analysis/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

The repository contains the Python implementation from the final stage of the project. The previous stages are described above to provide context for the complete learning process.

How to Run

Clone the repository:

git clone https://github.com/maiapedro/galaxy-groups-data-analysis.git

Navigate to the project directory:

cd galaxy-groups-data-analysis

Install the required libraries:

pip install -r requirements.txt

Place the following datasets in the same directory as main.py:

* groups.tsv
* galaxies_coordinates.tsv

Note: These datasets were provided through Hyperskill and are not included in this repository.

Run the program:

python main.py

The program generates a scatter plot showing the relationship between projected median separation and intra-group light surface brightness.

It also calculates the Shapiro-Wilk normality test results and the Pearson correlation p-value.

What I Learned

Working on this project helped me improve my understanding of Python and statistical data analysis.

I gained practical experience with data preprocessing, grouping and merging datasets, statistical hypothesis testing, correlation analysis, and data visualization.

I also had the opportunity to work with Astropy and learn how astronomical coordinates and cosmological models can be used to estimate physical distances.

Although the project focused on astronomy, the analytical techniques I practiced can also be applied to other fields, including business analytics and data science.

Acknowledgments

This project was developed through JetBrains Academy (Hyperskill) as part of my studies in Python and Data Analytics.
