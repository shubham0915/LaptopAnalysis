#  Budget Laptop Market Analysis Using EDA and Visualization

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Course](https://img.shields.io/badge/Course-INT375-blue)
![Institution](https://img.shields.io/badge/Institution-LPU-orange) 
https

 
## Project Overview

This project, completed as part of the **INT375 course** at **Lovely Professional University** (January–April 2025), analyzes laptop listings from Flipkart to uncover pricing trends, hardware preferences, and consumer insights in the budget and mid-range market (≤₹1,00,000). Under the guidance of **Baljinder Kaur**, the project leverages **web scraping**, **exploratory data analysis (EDA)**, and **data visualization** using Python to process the `flipkart_laptop12.csv` dataset, scraped from Flipkart’s website. Six objectives drive the analysis, delivering actionable insights through visualizations like histograms, box plots, and pie charts. This work showcases proficiency in data extraction, cleaning, analysis, and visualization, with potential for predictive modeling and interactive tools.

**Key Skills Demonstrated**:

- Web scraping with `requests` and `BeautifulSoup`.
- Data cleaning and preprocessing with `pandas` and `numpy`.
- Statistical analysis and visualization with `seaborn` and `matplotlib`.
- Ethical data collection and market trend analysis.

## Dataset

The `flipkart_laptop12.csv` dataset contains hundreds of laptop listings scraped from Flipkart, covering brands like ASUS, Lenovo, HP, and Dell. Key columns include:

- **Product**: Laptop model name (e.g., ASUS Vivobook 15).
- **Description**: Specifications (e.g., Intel Core i5, 8 GB RAM, 512 GB SSD).
- **Price**: Price in INR (e.g., ₹34,999).
- **Rating**: Customer rating (0–5 scale).
- **Review**: Combined ratings and reviews (e.g., “1,234 Ratings & 567 Reviews”).
- **Offer**: Discount percentage (e.g., “20% off”).

**Source**: Data was extracted using a Python web scraping script with `requests` and `BeautifulSoup`, targeting Flipkart’s laptop search results. Ethical scraping practices, including request delays (e.g., 45 seconds) and rotating user agents, ensured minimal server impact and compliance with Flipkart’s terms of service.

## Objectives

The project addresses six objectives to analyze the laptop market:

1. **Price Distribution**: Identify dominant price segments in the budget and mid-range market.
2. **Rating by Processor**: Assess customer satisfaction across processor types (e.g., Intel Core, AMD Ryzen).
3. **Discount by RAM**: Explore discount trends for different RAM capacities.
4. **Top Reviewed Laptops**: Identify popular models based on review counts.
5. **Price vs. Rating**: Examine the relationship between price and customer ratings.
6. **Storage Distribution**: Analyze prevalent storage configurations.

## Methodology

### 1. Web Scraping

- **Tools**: `requests` for HTTP requests, `BeautifulSoup` for HTML parsing.
- **Process**: Scraped Flipkart’s laptop listings across multiple pages, extracting product details (name, specs, price, ratings, reviews, discounts). Implemented delays and rotating user agents to ensure ethical data collection.
- **Output**: Saved raw data to `flipkart_laptop12.csv`.

### 2. Data Preprocessing

- **Cleaning**:
  - Removed currency symbols (₹) and commas from `Price`, converting to float.
  - Extracted discount percentages from `Offer` (e.g., “20% off” to 20.0).
  - Split `Review` into `Ratings` and `Reviews` counts using string parsing.
  - Parsed `Description` with regex to extract `Processor` (e.g., Intel Core, AMD Ryzen), `RAM` (e.g., 8 GB), and `Storage` (e.g., 512 GB).
  - Imputed missing `Rating` with the mean; set missing `Ratings`/`Reviews` to 0.
- **Outlier Removal**: Eliminated outliers in numerical columns (`Price`, `Rating`, `Offer`, `RAM`, `Storage`) using z-scores (|z| &gt; 3).
- **Final Columns**: `Product`, `Price`, `Rating`, `Offer`, `Ratings`, `Reviews`, `Processor`, `RAM`, `Storage`.

### 3. Exploratory Data Analysis (EDA)

- **Libraries**: `pandas` for data manipulation, `numpy` for numerical operations, `seaborn` and `matplotlib` for visualizations.
- **Analyses**:
  - **Distribution Analysis**: Studied `Price` and `Storage` distributions.
  - **Categorical Analysis**: Examined `Processor` and `RAM` frequencies.
  - **Relationship Analysis**: Explored `Price` vs. `Rating` and `Offer` vs. `RAM`.
  - **Popularity Analysis**: Identified top-reviewed laptops.
- **Visualizations**:
  - Histogram with KDE for price distribution.
  - Box plot for ratings by processor.
  - Bar plot for discounts by RAM.
  - Horizontal bar plot for top reviewed laptops.
  - Scatter plot with regression line for price vs. rating.
  - Pie chart for storage distribution.

## Key Findings

- **Price Distribution**: Right-skewed, with most laptops priced ₹20,000–₹60,000 (peak at \~₹40,000), highlighting a dominant mid-range market.
- **Rating by Processor**: Ratings (\~4.2–4.4) are consistent across Intel Core, AMD Ryzen, and Celeron, with Celeron showing more outliers below 3.5.
- **Discount by RAM**: 8GB RAM laptops receive the highest discounts (\~20–25%), followed by 4GB (\~15%) and 16GB (\~10–20%), reflecting mid-range competition.
- **Top Reviewed Laptops**: ASUS Vivobook and Lenovo Ideapad lead with 5,000–10,000 reviews, indicating strong consumer trust in mid-range models (₹30,000–₹50,000).
- **Price vs. Rating**: Weak correlation (r ≈ 0.1–0.2); budget laptops (\~₹30,000) achieve ratings (\~4.5) comparable to premium models.
- **Storage Distribution**: 512GB SSDs dominate (\~50–60%), followed by 256GB (\~20–25%) and 1TB (\~10–15%), aligning with modern multimedia and software needs.

## Visualizations

Sample visualizations (screenshots in `visualizations/`):

1. **Price Distribution**: Histogram with KDE, peaking at ₹40,000, showing right-skewed prices.
2. **Rating by Processor**: Box plot comparing ratings across processors, with Intel Core at \~4.3 median.
3. **Discount by RAM**: Bar plot highlighting 8GB RAM’s \~20–25% discounts.
4. **Top Reviewed Laptops**: Horizontal bar plot of top 10 models, led by ASUS and Lenovo.
5. **Price vs. Rating**: Scatter plot with flat regression line, showing weak correlation.
6. **Storage Distribution**: Pie chart with 512GB at \~50–60% share.

## Project Report

A detailed project report is available in `docs/project_report.pdf`, covering:

- **Introduction**: Context of the laptop market and project goals.
- **Source of Dataset**: Details on web scraping and data characteristics.
- **EDA Process**: Preprocessing, analysis types, and visualization methods.
- **Analysis Details**: Six in-depth analyses with objectives, methods, results, and visualizations.
- **Conclusion**: Summary of findings and implications.
- **Future Scope**: Plans for predictive modeling, dashboards, and recommendation systems.
- **References**: Sources like Flipkart, Python, and library documentation.

## LinkedIn Post

Shared this project on LinkedIn to engage the data science community:

> 🚀 Thrilled to share my INT375 project at LPU: **Budget Laptop Market Analysis Using EDA and Visualization**! 💻📊\
> Scraped Flipkart’s laptop listings with `requests` and `BeautifulSoup`, analyzed `flipkart_laptop12.csv` with Python, and visualized trends with `seaborn` and `matplotlib`.\
****Findings**: Mid-range laptops (₹20,000–₹60,000) dominate, 8GB RAM gets \~20–25% discounts, and 512GB SSDs lead (\~50–60%). ASUS and Lenovo models shine in reviews!\
> Thanks to **Baljinder Kaur** for guidance. Excited for feedback and ideas on ML or dashboards! 🔗 #DataScience #WebScraping #Python #EDA\
> \[[https://shorturl.at/TAkJx](https://shorturl.at/rXPUc)\]

## Prerequisites

To run the project, ensure:

- **Python**: Version 3.8 or higher.
- **Libraries**:

  ```bash
  pip install pandas numpy matplotlib seaborn requests beautifulsoup4
  ```
- **Dataset**: `flipkart_laptop12.csv` (place in `data/`).
- **Hardware**: Standard laptop/desktop with 4GB+ RAM.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/[your-username]/budget-laptop-market-analysis.git
   cd budget-laptop-market-analysis
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script**:

   - Place `flipkart_laptop12.csv` in `data/`.
   - Execute:

     ```bash
     python scripts/analysis.py
     ```

## Project Structure

```
budget-laptop-market-analysis/
├── data/
│   └── flipkart_laptop12.csv  # Dataset
├── docs/
│   └── project_report.pdf     # Detailed project report
├── notebooks/
│   └── analysis.ipynb         # Jupyter notebook with EDA and visualizations
├── scripts/
│   ├── scraper.py            # Web scraping script (optional)
│   └── analysis.py           # Analysis script
├── visualizations/           # Output folder for plots
├── requirements.txt          # Dependencies
├── LICENSE                   # MIT License
├── CODE_OF_CONDUCT.md        # Contributor guidelines
└── README.md                # Project documentation
```

## Usage

1. **Web Scraping** (Optional):

   - Run `scripts/scraper.py` to collect fresh data from Flipkart.
   - Update the script’s target URL and ensure ethical scraping (requires internet and Flipkart compliance).
   - Output: New `flipkart_laptop12.csv` in `data/`.

2. **EDA and Visualization**:

   - Open `notebooks/analysis.ipynb` in Jupyter Notebook or run `scripts/analysis.py`.
   - The script loads `flipkart_laptop12.csv`, preprocesses data, and generates six visualizations saved to `visualizations/`.

3. **Output**:

   - Visualizations (PNG files) in `visualizations/`.
   - Console output: Dataset info, cleaned data preview, outlier counts.

## Future Work

- **Predictive Modeling**: Use Random Forest or XGBoost for price prediction based on `RAM`, `Storage`, `Processor`.
- **Expanded Scraping**: Scrape Amazon or Croma for price comparisons; include screen size or GPU.
- **Interactive Dashboard**: Build a Plotly Dash app with filters for `Processor`, `RAM`, or price, deployable online.
- **Sentiment Analysis**: Analyze review text (if available) for customer sentiment.
- **Recommendation System**: Develop a tool to recommend laptops by budget and preferences.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request with a clear description.

Adhere to the Code of Conduct and ensure code quality with comments and tests.

## License

This project is licensed under the MIT License. See LICENSE for details.

## Acknowledgements

- **Baljinder Kaur**: Mentor for guidance and support.
- **Lovely Professional University**: For resources and infrastructure.
- **Python Community**: For libraries like `pandas`, `seaborn`, and `BeautifulSoup`.

## Contact

For questions or feedback:

- **Name**: \[SHUBHAM\]
- **Email**: \[shubhamkuya@example.com\]
- **LinkedIn**: \[[https://shorturl.at/TAkJx](https://shorturl.at/rXPUc)\]
- **GitHub**: \[https://github.com/shubham0915\]

---

*Project completed as part of INT375, Lovely Professional University, January–April 2025.*
