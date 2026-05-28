import pandas as pd


def preprocess_data(df):

    # Drop unwanted columns
    drop_columns = [
        'IsPEP',
        'Occupation',
        'DateofBirth',
        'TransactionId',
        'AccountId',
        'ClientId'
    ]

    for col in drop_columns:
        if col in df.columns:
            df.drop(columns=col, inplace=True)

    # Fill Missing Values
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].fillna(
            df['Gender'].mode()[0]
        )

    if 'RiskCategoryId' in df.columns:
        df['RiskCategoryId'] = df['RiskCategoryId'].fillna(
            df['RiskCategoryId'].mode()[0]
        )

    # Convert Date Columns
    date_columns = [
        'TransactionDate',
        'AccountOpenDate'
    ]

    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col])

    # Feature Engineering
    df['transaction_year'] = (
        df['TransactionDate'].dt.year
    )

    df['transaction_month'] = (
        df['TransactionDate'].dt.month
    )

    df['account_open_year'] = (
        df['AccountOpenDate'].dt.year
    )

    df['account_open_month'] = (
        df['AccountOpenDate'].dt.month
    )

    # Drop original date columns
    df.drop(
        columns=[
            'TransactionDate',
            'AccountOpenDate'
        ],
        inplace=True
    )

    return df