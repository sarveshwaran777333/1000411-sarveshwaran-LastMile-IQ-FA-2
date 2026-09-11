# 1000411-sarveshwaran-LastMile-IQ-FA-2

# 🚚 LastMile IQ

## Smart Last-Mile Delivery Analytics Dashboard

LastMile IQ is an interactive data analytics dashboard designed to analyze last-mile delivery performance.

The system uses **Python, Pandas, Plotly, and Streamlit** to process delivery data and present meaningful insights through interactive visualizations, statistical analysis, filters, and downloadable datasets.

The dashboard helps users understand how factors such as **weather, traffic, vehicle type, delivery area, product category, and agent characteristics** are associated with delivery time.

---

## 📌 Project Overview

Last-mile delivery is the final stage of the delivery process, where an order is transported from a local facility or store to the customer.

Delivery performance can be affected by several factors, including traffic conditions, weather, vehicle type, delivery area, and the characteristics of delivery agents.

LastMile IQ analyzes these factors using an interactive dashboard.

The system provides:

- Total number of deliveries
- Average delivery time
- Late delivery rate
- Average agent rating
- Average delivery time by weather and traffic
- Average delivery time by vehicle
- Agent age vs delivery time analysis
- Area-based delivery time analysis
- Delivery-time distribution by category
- Statistical analysis
- Interactive filters
- Raw dataset viewing
- Filtered dataset download
- Graph explanations through `?` help buttons
- Customizable dashboard background colour

---

## 🎯 Project Objective

The main objective of LastMile IQ is to develop an interactive data analytics dashboard that can be used to investigate patterns in last-mile delivery performance.

The project focuses on:

1. Cleaning and preparing the delivery dataset.
2. Filtering delivery records interactively.
3. Calculating statistical measures such as mean and standard deviation.
4. Identifying deliveries that exceed the late-delivery threshold.
5. Comparing delivery times across different conditions.
6. Visualizing relationships between delivery variables.
7. Providing an easy-to-use dashboard for data exploration.
8. Allowing users to download filtered data for further analysis.

---

## 📊 Dataset

The application uses the following dataset:


Last mile Delivery Data.csv

The dataset contains delivery-related information such as:

Order ID
Agent Age
Agent Rating
Store Latitude
Store Longitude
Drop Latitude
Drop Longitude
Order Date
Order Time
Pickup Time
Weather
Traffic
Vehicle
Area
Delivery Time
Category

The dataset contains 43,739 delivery records and 16 columns.

Missing Data

The dataset contains some missing values, including:

Agent Rating
Weather

The application handles missing values during data preprocessing.

Numerical values are converted to appropriate numeric formats, while missing categorical values are represented as "Unknown".

Missing agent ratings are replaced using the median agent rating.

🧹 Data Processing

Before analysis, the dataset goes through a preprocessing stage.

The application:

Loads the CSV dataset using Pandas.
Converts numerical columns into numeric data types.
Removes records where required delivery-time or agent-age values are unavailable.
Handles missing agent ratings using the median.
Handles missing categorical values using "Unknown".
Calculates the overall mean delivery time.
Calculates the standard deviation.
Creates the late-delivery threshold.
Creates agent age groups for visualization.
Applies the selected dashboard filters.
📐 Statistical Analysis

LastMile IQ uses statistical calculations to identify unusually long delivery times.

Mean Delivery Time

The mean represents the average delivery time of the dataset.

Mean = Σx / n

Where:

x represents an individual delivery time.
n represents the total number of deliveries.
Standard Deviation

Standard deviation measures how spread out delivery times are around the mean.

The application uses the standard deviation to define the late-delivery threshold.

Late Delivery Rule

A delivery is classified as late when:

Delivery Time > Mean Delivery Time + Standard Deviation

Mathematically:

Late Delivery if Delivery Time > x̄ + σ

Where:

x̄ = Mean Delivery Time
σ = Standard Deviation

This rule is applied to the dataset to identify deliveries with unusually high delivery times.

📊 Dashboard Visualizations

LastMile IQ contains five compulsory visualizations.

01 · Delay Analyzer

The Delay Analyzer shows the average Delivery Time under different Weather and Traffic conditions.

The visualization uses a grouped bar chart.

It allows users to compare delivery times across combinations of:

Weather
Traffic

A taller bar represents a higher average delivery time.

Purpose

This visualization helps identify weather and traffic conditions that are associated with longer delivery times.

02 · Vehicle Comparison

The Vehicle Comparison visualization shows the average Delivery Time for each Vehicle type.

The visualization uses a bar chart.

Purpose

This helps compare the delivery performance associated with different vehicle types.

A higher bar indicates a higher average delivery time.

03 · Agent Performance

The Agent Performance visualization uses a scatter plot to show the relationship between:

Agent Age
        vs
Delivery Time

The agents are divided into three age groups:

<25
25–40
40+

Each point represents a delivery.

The visualization also allows additional delivery information to be inspected through hover information.

Purpose

This visualization helps investigate whether delivery time shows any visible relationship with agent age.

04 · Area Heatmap

The Area Heatmap displays average delivery time across different:

Areas
Traffic conditions

The heatmap uses colour intensity to represent average delivery time.

Purpose

This visualization makes it easier to compare delivery performance across different areas while considering traffic conditions.

05 · Category Visualizer

The Category Visualizer uses a horizontal boxplot to show the distribution of delivery times across different categories.

The boxplot displays:

Median
Middle portion of the data
Wider spread
Potential variation in delivery times
Purpose

This visualization helps compare the distribution and spread of delivery times between different order categories.

🔎 Interactive Filters

The dashboard provides interactive filters through the sidebar.

Users can filter the dataset using:

Weather
Traffic
Vehicle
Category
Area

The selected filters are applied to the dashboard dynamically.

When filters are changed:

KPI values update.
Graphs update.
Statistical information updates.
The displayed raw dataset updates.
The downloadable dataset updates.

This allows users to explore specific subsets of the delivery data.

📈 Key Performance Indicators

The dashboard displays four main KPIs.

Total Deliveries

Shows the number of delivery records currently included after applying the selected filters.

Average Delivery Time

Shows the mean delivery time of the currently filtered records.

Late Delivery Rate

Shows the percentage of filtered deliveries classified as late using the late-delivery rule.

Late Delivery Rate =
(Late Deliveries / Total Deliveries) × 100
Average Agent Rating

Shows the average rating of delivery agents within the currently filtered dataset.

📋 Raw Dataset

The Raw Dataset section allows users to inspect the delivery records directly inside the application.

The application displays:

Number of filtered records
Complete filtered dataset
Download option

Users can download the currently filtered dataset as a CSV file.

The output file is:

LastMile_IQ_Filtered_Dataset.csv

This allows the user to continue working with the selected data offline.

❓ Graph Explanations

Each major visualization contains a ? help button.

The help button explains:

What the graph represents.
Which variables are being compared.
How the graph should be interpreted.
What the user should look for.

This makes the dashboard easier to understand for users who may not be familiar with data visualization.

🎨 Dashboard Customization

LastMile IQ includes a dashboard appearance section.

Users can select a custom background colour using a colour picker.

The application dynamically adjusts:

Text colour
Sidebar appearance
Cards
Buttons
Tabs
Graph backgrounds
Graph text

The interface is designed to maintain readability for both light and dark backgrounds.

The active dashboard tab also changes colour based on the selected background.

🛠️ Technologies Used
Programming Language

Python 3.13

Data Processing

Pandas

Pandas is used for:

Loading the dataset
Cleaning data
Filtering records
Grouping data
Calculating statistics
Data Visualization

Plotly

Plotly is used to create:

Bar charts
Scatter plots
Heatmaps
Boxplots
Web Application

Streamlit

Streamlit is used to build the interactive dashboard and provide:

Sidebar filters
Tabs
KPI cards
Interactive graphs
Dataset viewing
CSV download
Dashboard customization
📦 Project Structure
LastMile IQ/
│
├── app.py
│
├── Last mile Delivery Data.csv
│
├── requirements.txt
│
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/sarveshwaran777333/1000411-sarveshwaran-LastMile-IQ.git

Move into the project folder:

cd 1000411-sarveshwaran-LastMile-IQ

Install the required packages:

pip install -r requirements.txt
📦 Requirements

The project requires the following Python libraries:

streamlit
pandas
plotly

These dependencies are also provided in:

requirements.txt
▶️ Running the Application

Run the Streamlit application using:

streamlit run app.py

The application will open in a web browser.

After opening the dashboard:

Use the sidebar filters.
Explore the five visualizations.
Click the ? button beside a graph for an explanation.
Open the Mathematical Analysis tab.
Open the Raw Dataset tab.
Download the filtered dataset if required.
Change the background colour using the dashboard appearance settings.
🔬 Testing

The dashboard can be tested using different filter combinations.

Examples include:

Different weather conditions
Different traffic conditions
Different vehicle types
Different delivery areas
Different categories
Multiple filters at the same time

Testing should verify that:

KPI values update correctly.
Graphs respond to filters.
Statistical values update correctly.
The late-delivery calculation works correctly.
The raw dataset matches the selected filters.
The download option exports the filtered records.
Graph text remains readable.
Light and dark backgrounds remain usable.
Empty filter results are handled correctly.
⚠️ Limitations

LastMile IQ has several limitations.

Dataset Dependency

The quality of the analysis depends on the quality and completeness of the dataset.

Correlation Does Not Prove Causation

The visualizations show patterns and relationships in the data. They do not prove that one factor directly causes changes in delivery time.

Missing Information

Some potentially important factors may not be included in the dataset, such as:

Exact road conditions
Distance travelled
Number of delivery stops
Vehicle condition
Real-time traffic changes
Static Dataset

The dashboard analyzes the provided dataset and does not automatically receive live delivery information.

Late Delivery Definition

The late-delivery classification is based on:

Mean + Standard Deviation

This is a statistical rule chosen for the project and may not represent the official definition used by a real delivery company.

🚀 Future Improvements

Possible future improvements include:

Adding real-time delivery data.
Adding GPS-based route analysis.
Adding delivery-distance calculations.
Adding date and time filters.
Adding predictive delivery-time models.
Adding machine-learning-based delay prediction.
Adding interactive geographic maps.
Adding route optimization.
Adding real-time traffic information.
Adding weather API integration.
Adding delivery-time forecasting.
Adding automated reports.
Adding more advanced statistical analysis.
Adding user authentication.
Improving dashboard performance for larger datasets.
📚 Research and Learning

This project demonstrates the application of several data analytics concepts:

Data Cleaning
Data Preprocessing
Descriptive Statistics
Mean
Standard Deviation
Data Filtering
Grouped Data Analysis
Data Visualization
Scatter Plot Analysis
Boxplot Analysis
Heatmap Analysis
Interactive Dashboards
CSV Data Processing
Data Export
Statistical Thresholds

The project demonstrates how raw delivery data can be transformed into an interactive analytical dashboard that helps users identify patterns and investigate delivery performance.

🌐 Deployment

The application is designed to run using Streamlit.

The project can be hosted using a Streamlit-compatible deployment platform with the following files:

app.py
Last mile Delivery Data.csv
requirements.txt

GitHub Repository:

https://github.com/sarveshwaran777333/1000411-sarveshwaran-LastMile-IQ

👨‍💻 Project Information

Project: LastMile IQ

Title: Smart Last-Mile Delivery Analytics Dashboard

Course: Data Analytics

Programming Language: Python

Data Processing: Pandas

Visualization: Plotly

Application Framework: Streamlit

Dataset: Last mile Delivery Data.csv

📌 Conclusion

LastMile IQ demonstrates how Python-based data analytics can be used to analyze last-mile delivery performance.

By combining data preprocessing, statistical analysis, interactive filtering, and data visualization, the dashboard provides a simple way to explore relationships between delivery time and factors such as weather, traffic, vehicle type, area, category, and agent age.

The five visualizations provide different perspectives on delivery performance, while the mathematical analysis uses mean and standard deviation to identify unusually long delivery times.

The interactive filtering system allows users to investigate specific parts of the dataset, and the Raw Dataset section provides the ability to view and download filtered records for further offline analysis.

Overall, LastMile IQ demonstrates how raw delivery data can be transformed into a useful and interactive data analytics solution using Python, Pandas, Plotly, and Streamlit.


**Important:** Save it exactly as **`README.md`** in the same GitHub repository as `app.py`, `requirements.txt`, and `Last mile Del
