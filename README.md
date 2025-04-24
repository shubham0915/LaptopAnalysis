# Budget Laptop Market Analysis Using EDA and Visualization

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## Project Overview

This project, part of the INT375 course at Lovely Professional University, analyzes laptop listings from Flipkart to uncover pricing trends, hardware preferences, and consumer insights in the budget and mid-range market (≤₹1,00,000). Using **web scraping**, **exploratory data analysis (EDA)**, and **data visualization**, the project leverages Python to process the `flipkart_laptop12.csv` dataset, extracted from Flipkart’s website. Six objectives guide the analysis, revealing key market dynamics through visualizations like histograms, box plots, and pie charts. Conducted under the guidance of **Baljinder Kaur**, this project showcases skills in data extraction, cleaning, and visualization, with potential for future predictive modeling.

## Dataset

The `flipkart_laptop12.csv` dataset contains laptop listings scraped from Flipkart, including:
- **Product**: Laptop model name (e.g., ASUS Vivobook 15).
- **Description**: Specifications (e.g., Intel Core i5, 8 GB RAM, 512 GB SSD).
- **Price**: Price in INR (e.g., ₹34,999).
- **Rating**: Customer rating (0–5 scale).
- **Review**: Combined ratings and reviews (e.g., “1,234 Ratings & 567 Reviews”).
- **Offer**: Discount percentage (e.g., “20% off”).

**Source**: Data was extracted using a Python web scraping script with `requests` and `BeautifulSoup`, targeting Flipkart’s laptop search results. Ethical scraping practices (e.g., request delays, rotating user agents) were followed to minimize server impact.

## Objectives

The project addresses six objectives to analyze the laptop market:
1. **Price Distribution**: Identify dominant price segments.
2. **Rating by Processor**: Assess customer satisfaction across processor types (e.g., Intel Core, AMD Ryzen).
3. **Discount by RAM**: Explore discount trends for different RAM capacities.
4. **Top Reviewed Laptops**: Identify popular models based on review counts.
5. **Price vs. Rating**: Examine the relationship between price and customer ratings.
6. **Storage Distribution**: Analyze prevalent storage configurations.

## Methodology

### 1. Web Scraping
- **Tools**: `requests` for HTTP requests, `BeautifulSoup` for HTML parsing.
- **Process**: Scraped Flipkart’s laptop listings, extracting product details across multiple pages. Used delays (e.g., 45 seconds) and rotating user agents to ensure ethical data collection.
- **Output**: Saved data to `flipkart_laptop12.csv`.

### 2. Data Preprocessing
- **Cleaning**:
  - Removed currency symbols (₹) and commas from `Price`, converted to float.
  - Extracted discount percentages from `Offer`.
  - Split `Review` into `Ratings` and `Reviews` counts.
  - Parsed `Description` using regex to extract `Processor`, `RAM`, and `Storage`.
  - Imputed missing `Rating` with mean, set missing `Ratings`/`Reviews` to 0.
- **Outlier Removal**: Eliminated outliers in numerical columns (`Price`, `Rating`, `Offer`, `RAM`, `Storage`) using z-scores (|z| > 3).
- **Final Columns**: `Product`, `Price`, `Rating`, `Offer`, `Ratings`, `Reviews`, `Processor`, `RAM`, `Storage`.

### 3. EDA and Visualization
- **Libraries**: `pandas` for data manipulation, `numpy` for numerical operations, `seaborn` and `matplotlib` for visualizations.
- **Analyses**:
  - **Price Distribution**: Histogram with KDE.
  - **Rating by Processor**: Box plot.
  - **Discount by RAM**: Bar plot.
  - **Top Reviewed Laptops**: Horizontal bar plot.
  - **Price vs. Rating**: Scatter plot with regression line.
  - **Storage Distribution**: Pie chart.

## Key Findings

- **Price Distribution**: Most laptops are priced ₹20,000–₹60,000, peaking at ~₹40,000, indicating a strong mid-range market.
- **Rating by Processor**: Ratings (~4.2–4.4) are similar across Intel Core, AMD Ryzen, and Celeron, suggesting uniform satisfaction.
- **Discount by RAM**: 8GB RAM laptops receive the highest discounts (~20–25%), reflecting aggressive mid-range promotions.
- **Top Reviewed Laptops**: ASUS Vivobook and Lenovo Ideapad lead with thousands of reviews, indicating high consumer trust.
- **Price vs. Rating**: Weak correlation (r ≈ 0.1–0.2); budget laptops (~₹30,000) match premium ones in ratings (~4.5).
- **Storage Distribution**: 512GB SSDs dominate (~50–60%), followed by 256GB and 1TB, aligning with modern storage needs.

## Visualizations

Below are sample visualizations (screenshots to be added):
1. **Price Distribution**: Histogram showing right-skewed prices with a peak at ₹40,000.
2. **Rating by Processor**: Box plot comparing ratings across processors.
3. **Discount by RAM**: Bar plot highlighting 8GB RAM discounts.
4. **Top Reviewed Laptops**: Horizontal bar plot of top 10 models by reviews.
5. **Price vs. Rating**: Scatter plot with a flat regression line.
6. **Storage Distribution**: Pie chart showing 512GB dominance.

## Prerequisites

To run the project, ensure the following:
- **Python**: Version 3.8 or higher.
- **Libraries**:
  ```bash
  pip install pandas numpy matplotlib seaborn requests beautifulsoup4
