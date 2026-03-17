"""
Lab 2 — Learner Test File

Write your own pytest tests here. You must implement at least 3 test functions:
  - test_load_data_returns_dataframe
  - test_clean_data_no_nulls
  - test_add_features_creates_revenue

The autograder will run your tests as part of the CI check.
"""

import pandas as pd
import numpy as np
import pytest
from pipeline import load_data, clean_data, add_features


# ─── Test 1 ───────────────────────────────────────────────────────────────────

def test_load_data_returns_dataframe():
    """load_data should return a DataFrame with expected columns and rows."""
    # TODO: Call load_data('data/sales_records.csv')
    # TODO: Assert the result is a pd.DataFrame
    # TODO: Assert len(df) > 0
    # TODO: Assert all expected columns are present:
    #        'date', 'store_id', 'product_category', 'quantity', 'unit_price', 'payment_method'
    
def test_load_data_returns_dataframe():
    """load_data should return a DataFrame with expected columns and rows."""
    
    # Call load_data
    df = load_data('data/sales_records.csv')
    
    # Assert the result is a DataFrame
    assert isinstance(df, pd.DataFrame)
    
    # Assert there are rows
    assert len(df) > 0
    
    # Expected columns
    expected_columns = [
        'date',
        'store_id',
        'product_category',
        'quantity',
        'unit_price',
        'payment_method'
    ]
    
    # Check all columns exist
    for col in expected_columns:
        assert col in df.columns


# ─── Test 2 ───────────────────────────────────────────────────────────────────

def test_clean_data_no_nulls():
    """After clean_data, quantity and unit_price should have no NaN values."""
    # TODO: Load the data, then call clean_data
    # TODO: Assert cleaned['quantity'].isna().sum() == 0
    # TODO: Assert cleaned['unit_price'].isna().sum() == 0
    

def test_clean_data_no_nulls():
    """After clean_data, quantity and unit_price have no NaN values."""
    
    # Load and clean the data
    df = load_data('data/sales_records.csv')
    cleaned = clean_data(df)
    
    # Assert no NaN values
    assert cleaned['quantity'].isna().sum() == 0
    assert cleaned['unit_price'].isna().sum() == 0

# ─── Test 3 ───────────────────────────────────────────────────────────────────

def test_add_features_creates_revenue():
    """add_features should add a 'revenue' column equal to quantity * unit_price."""
    # TODO: Load and clean the data, then call add_features
    # TODO: Assert 'revenue' in df.columns
    # TODO: Assert the revenue values equal quantity * unit_price
    #        Use pd.testing.assert_series_equal for float comparison
    

def test_add_features_creates_revenue():
    """add_features creates a 'revenue' column equal to quantity * unit_price."""
    
    # Load, clean, and add features
    df = load_data('data/sales_records.csv')
    cleaned = clean_data(df)
    featured = add_features(cleaned)
    
    # Assert 'revenue' column exists
    assert 'revenue' in featured.columns
    
    # Expected revenue
    expected_revenue = featured['quantity'] * featured['unit_price']
    
    # Assert values are equal
    import pandas as pd
    pd.testing.assert_series_equal(
        featured['revenue'],
        expected_revenue,
        check_names=False
    )
