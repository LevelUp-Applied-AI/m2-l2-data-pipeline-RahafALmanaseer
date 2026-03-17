"""
Lab 2 — Data Pipeline: Retail Sales Analysis
Module 2 — Programming for AI & Data Science

Complete each function below. Remove the TODO: comments and pass statements
as you implement each function. Do not change the function signatures.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ─── Configuration ────────────────────────────────────────────────────────────

DATA_PATH = 'data/sales_records.csv'
OUTPUT_DIR = 'output'


# ─── Pipeline Functions ───────────────────────────────────────────────────────

def load_data(filepath):
    """Load sales records from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Raw sales records DataFrame.
    """
    # TODO: Load the CSV using pd.read_csv(filepath)
    # TODO: Print a progress message: f"Loaded {len(df)} records from {filepath}"
    # TODO: Return the DataFrame
    
    """Load sales records from CSV. Returns a DataFrame."""
    
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records from {filepath}")
    
    return df


def clean_data(df):
    """Handle missing values and fix data types.

    - Fill missing 'quantity' values with the column median.
    - Fill missing 'unit_price' values with the column median.
    - Parse the 'date' column to datetime (use errors='coerce' to handle malformatted dates).
    - Print a progress message showing the record count after cleaning.

    Args:
        df (pd.DataFrame): Raw DataFrame from load_data().

    Returns:
        pd.DataFrame: Cleaned DataFrame (do not modify the input in place).
    """
    # TODO: Start with df = df.copy() — never modify the input DataFrame in place
    # TODO: Fill missing 'quantity' with df['quantity'].median()
    # TODO: Fill missing 'unit_price' with df['unit_price'].median()
    # TODO: Parse 'date' column: pd.to_datetime(df['date'], errors='coerce')
    # TODO: Print progress and return cleaned DataFrame
    
    """
    Clean the input DataFrame by handling missing values and fixing data types.

    Steps:
    1. Work on a copy of the input to avoid modifying it in place.
    2. Fill missing 'quantity' and 'unit_price' values with the median of each column.
       - If the entire column is missing, fill with 0 as a fallback.
    3. Convert 'date' column to datetime (invalid dates become NaT).
    4. Print a progress message showing the number of records after cleaning.
    
    Args:
        df (pd.DataFrame): Raw DataFrame from load_data().
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Step 1: Work on a copy
    df = df.copy()
    
    # Step 2: Handle missing 'quantity'
    if df['quantity'].isna().all():
        df['quantity'] = 0
    else:
        df['quantity'] = df['quantity'].fillna(df['quantity'].median())
    
    # Step 2: Handle missing 'unit_price'
    if df['unit_price'].isna().all():
        df['unit_price'] = 0
    else:
        df['unit_price'] = df['unit_price'].fillna(df['unit_price'].median())
    
    # Step 3: Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # Step 4: Print progress
    print(f"Cleaned data: {len(df)} records")
    
    return df


def add_features(df):
    """Compute derived columns.

    - Add 'revenue' column: quantity * unit_price.
    - Add 'day_of_week' column: day name from the date column.

    Args:
        df (pd.DataFrame): Cleaned DataFrame from clean_data().

    Returns:
        pd.DataFrame: DataFrame with new columns added.
    """
    # TODO: Start with df = df.copy()
    # TODO: df['revenue'] = df['quantity'] * df['unit_price']
    # TODO: df['day_of_week'] = df['date'].dt.day_name()
    #        (requires 'date' to be datetime type — must call after clean_data)
    # TODO: Return the enriched DataFrame
    
def add_features(df):
    """Add revenue and day_of_week columns. Returns an enriched DataFrame."""
    
    # 1. Copy input DataFrame
    df_enriched = df.copy()
    
    # 2. Add revenue column
    df_enriched['revenue'] = df_enriched['quantity'] * df_enriched['unit_price']
    
    # 3. Add day_of_week column (requires 'date' to be datetime)
    df_enriched['day_of_week'] = df_enriched['date'].dt.day_name()
    
    # 4. Return enriched DataFrame
    return df_enriched

def generate_summary(df):
    """Compute summary statistics.

    Args:
        df (pd.DataFrame): Enriched DataFrame from add_features().

    Returns:
        dict: Summary with keys:
            - 'total_revenue': total revenue (sum)
            - 'avg_order_value': average order value (mean)
            - 'top_category': product category with highest total revenue
            - 'record_count': number of records in df
    """
    # TODO: Compute top category: df.groupby('product_category')['revenue'].sum().idxmax()
    # TODO: Return a dict with the four keys above
    def generate_summary(df):

       """Compute summary statistics. Returns a dict."""
    
    # Total revenue
    total_revenue = df['revenue'].sum()
    
    # Average order value
    avg_order_value = df['revenue'].mean()
    
    # Top category by total revenue
    top_category = df.groupby('product_category')['revenue'].sum().idxmax()
    
    # Record count
    record_count = len(df)
    
    # Return as dictionary
    summary = {
        'total_revenue': total_revenue,
        'avg_order_value': avg_order_value,
        'top_category': top_category,
        'record_count': record_count
    }
    
    return summary


def create_visualizations(df, output_dir=OUTPUT_DIR):
    """Create and save 3 charts as PNG files.

    Charts to create:
    1. Bar chart: total revenue by product category
    2. Line chart: daily revenue trend (aggregate revenue by date)
    3. Horizontal bar chart: average order value by payment method

    Save each chart as a PNG using fig.savefig().
    Do NOT use plt.show() — it blocks execution in pipeline scripts.
    Close each figure with plt.close(fig) after saving.

    Args:
        df (pd.DataFrame): Enriched DataFrame from add_features().
        output_dir (str): Directory to save PNG files (create if needed).
    """
    # TODO: Create the output directory: os.makedirs(output_dir, exist_ok=True)

    # TODO: Chart 1 — Bar chart: total revenue by product category
    #   - Group by 'product_category', sum 'revenue'
    #   - fig, ax = plt.subplots(figsize=(10, 6))
    #   - ax.bar(categories, values) or use ax.barh() for horizontal
    #   - Set title, labels
    #   - fig.savefig(f'{output_dir}/revenue_by_category.png', dpi=150, bbox_inches='tight')
    #   - plt.close(fig)

    # TODO: Chart 2 — Line chart: daily revenue trend
    #   - Group by 'date', sum 'revenue' — sort by date
    #   - ax.plot(dates, revenues)
    #   - fig.savefig(f'{output_dir}/daily_revenue_trend.png', ...)
    #   - plt.close(fig)

    # TODO: Chart 3 — Horizontal bar chart: avg order value by payment method
    #   - Group by 'payment_method', mean 'revenue'
    #   - ax.barh(methods, avg_values)
    #   - fig.savefig(f'{output_dir}/avg_order_by_payment.png', ...)
    #   - plt.close(fig)

    def create_visualizations(df, output_dir='output'):

      """Create and save 3 charts to output_dir."""
    
    import os
    import matplotlib.pyplot as plt
    
    # 1. Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # 2. Chart 1: Total revenue by product category
    category_revenue = df.groupby('product_category')['revenue'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    category_revenue.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title('Total Revenue by Product Category')
    ax.set_ylabel('Revenue')
    ax.set_xlabel('Product Category')
    fig.savefig(os.path.join(output_dir, 'revenue_by_category.png'))
    plt.close(fig)
    
    # 3. Chart 2: Daily revenue trend
    daily_revenue = df.groupby('date')['revenue'].sum()
    fig, ax = plt.subplots()
    daily_revenue.plot(kind='line', ax=ax, color='green')
    ax.set_title('Daily Revenue Trend')
    ax.set_ylabel('Revenue')
    ax.set_xlabel('Date')
    fig.savefig(os.path.join(output_dir, 'daily_revenue_trend.png'))
    plt.close(fig)
    
    # 4. Chart 3: Average order value by payment method
    avg_order_by_payment = df.groupby('payment_method')['revenue'].mean().sort_values()
    fig, ax = plt.subplots()
    avg_order_by_payment.plot(kind='barh', ax=ax, color='orange')
    ax.set_title('Average Order Value by Payment Method')
    ax.set_xlabel('Average Revenue')
    ax.set_ylabel('Payment Method')
    fig.savefig(os.path.join(output_dir, 'avg_order_by_payment.png'))
    plt.close(fig)


def main():
    """Run the full data pipeline end-to-end."""
    # TODO: Call load_data(DATA_PATH)
    # TODO: Call clean_data(df)
    # TODO: Call add_features(df)
    # TODO: Call generate_summary(df) and print the results
    # TODO: Call create_visualizations(df)
    # TODO: Print "Pipeline complete."
def main():
    """Run the full pipeline end-to-end."""
    
    # Load data
    df = load_data(DATA_PATH)
    
    # Clean data
    df_clean = clean_data(df)
    
    # Add features
    df_enriched = add_features(df_clean)
    
    # Generate summary statistics
    summary = generate_summary(df_enriched)
    
    # Print summary
    print("Summary Statistics:")
    for key, value in summary.items():
        print(f"{key}: {value}")
    
    # Create visualizations
    create_visualizations(df_enriched)
    
    # Completion message
    print("Pipeline complete.")

# Guard to run main only if script is executed directly
if __name__ == "__main__":
    main()



    main()
