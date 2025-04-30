import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('flipkart_laptops12.csv')


print("First few rows of the dataset:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nChecking for missing values...")
print(df.isnull().sum())
print("\nChecking for duplicates:", df.duplicated().sum())
print("\nSummarizing the data:")
print(df.describe())
print("\nColumns in the dataset:")
print(df.columns.tolist())



# Cleaning
df_clean = df.copy()


df_clean['Price'] = df_clean['Price'].replace({'₹': '', ',': ''}, regex=True).astype(float)

df_clean['Offer'] = df_clean['Offer'].replace({'% off': ''}, regex=True).astype(float)


df_clean['Ratings'] = df_clean['Review'].str.split('&').str[0].str.replace(',', '', regex=False).str.extract(r'(\d+)').astype(float)
df_clean['Reviews'] = df_clean['Review'].str.split('&').str[1].str.replace(',', '', regex=False).str.extract(r'(\d+)').astype(float)


df_clean['Rating'] = df_clean['Rating'].fillna(df_clean['Rating'].mean())
df_clean['Ratings'] = df_clean['Ratings'].fillna(0)
df_clean['Reviews'] = df_clean['Reviews'].fillna(0)

# Extract features from Description

df_clean['Description'] = df_clean['Description'].astype(str)

df_clean['Processor'] = df_clean['Description'].str.extract(r'(Intel Core|AMD Ryzen|MediaTek|Celeron|Athlon|Pentium)')



df_clean['RAM'] = df_clean['Description'].str.extract(r'(\d+\s*GB)')[0].str.replace(' GB', '', regex=False)
df_clean['RAM'] = pd.to_numeric(df_clean['RAM'], errors='coerce')


df_clean['Storage'] = df_clean['Description'].str.extract(r'(\d+\s*(GB|TB))')[0]
df_clean['Storage'] = df_clean['Storage'].str.replace(' GB', '').str.replace(' TB', '000').str.extract(r'(\d+)')[0]
df_clean['Storage'] = pd.to_numeric(df_clean['Storage'], errors='coerce')


df_clean.dropna(subset=['Price', 'Offer', 'Processor', 'RAM', 'Storage'], inplace=True)

# Outlier detection
numeric_cols = ['Price', 'Rating', 'Offer', 'RAM', 'Storage']
z_scores = (df_clean[numeric_cols] - df_clean[numeric_cols].mean()) / df_clean[numeric_cols].std()
outliers = (np.abs(z_scores) > 3).any(axis=1)
print(f"\nNumber of outliers found: {outliers.sum()}")
df_clean = df_clean[~outliers]

# Keep relevant columns
key_columns = ['Product', 'Price', 'Rating', 'Offer', 'Ratings', 'Reviews', 'Processor', 'RAM', 'Storage']
df_clean = df_clean[key_columns]
print("\nCleaned dataset head:")
print(df_clean.head())




# Objective 1: Price Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df_clean['Price'], kde=True, bins=30, color='skyblue')
plt.title('Distribution of Laptop Prices')
plt.xlabel('Price (₹)')
plt.ylabel('Frequency')
plt.axvline(df_clean['Price'].mean(), color='red', linestyle='--', label='Mean Price')
plt.legend()
plt.tight_layout()
plt.show()

# Objective 2: Rating by Processor
plt.figure(figsize=(10, 6))
sns.boxplot(x='Processor', y='Rating', data=df_clean, palette='Set2')
plt.title('Rating Distribution by Processor Type')
plt.xlabel('Processor')
plt.ylabel('Rating')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Objective 3: Discount by RAM
plt.figure(figsize=(10, 6))
sns.barplot(x='RAM', y='Offer', data=df_clean, palette='Blues_d')
plt.title('Average Discount by RAM Capacity')
plt.xlabel('RAM (GB)')
plt.ylabel('Discount (% off)')
plt.tight_layout()
plt.show()

# Objective 4: Top 10 by Reviews
top_reviews = df_clean.nlargest(10, 'Reviews')[['Product', 'Reviews']]
plt.figure(figsize=(10, 6))
sns.barplot(x='Reviews', y='Product', data=top_reviews, palette='Greens_d')
plt.title('Top 10 Laptops by Number of Reviews')
plt.xlabel('Number of Reviews')
plt.ylabel('Product')
plt.tight_layout()
plt.show()


# Objective 5: Price vs. Rating

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Price', y='Rating', data=df_clean, alpha=0.6, color='purple')
sns.regplot(x='Price', y='Rating', data=df_clean, scatter=False, color='black')
plt.title('Price vs. Rating of Laptops')
plt.xlabel('Price (₹)')
plt.ylabel('Rating')
plt.tight_layout()
plt.show()

# Objective 6: Storage Distribution
storage_counts = df_clean['Storage'].value_counts().head(5)
plt.figure(figsize=(8, 8))
plt.pie(storage_counts, labels=storage_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Distribution of Storage Capacities')
plt.tight_layout()
plt.show()

print("\nCleaned dataset info:")
print(df_clean.info())
