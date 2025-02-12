import pandas as pd


def impute_column(df: pd.DataFrame, column_name: str, impute_mode: str) -> pd.DataFrame:
    """
    Impute missing values in a specified column of a DataFrame using the specified imputation mode.
    
    Arguments:
    df (pd.DataFrame): The DataFrame containing the column to be imputed.
    column_name (str): The name of the column in which to impute missing values.
    impute_mode (str): The imputation mode to use. Must be either 'mean', 'median' or 'value'.
    
    Returns:
    pd.DataFrame: The DataFrame with the imputed column.
    """

    # Check that the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f'{column_name} is not present in df')

    # Check that the column is numeric
    if not pd.api.types.is_numeric_dtype(df[column_name]):
        raise TypeError(f'{column_name} is not numeric')

    # Check that the impute_mode is valid
    if impute_mode not in ['mean', 'median']:
        raise ValueError(f'{impute_mode} is not a valid impute_mode')
 
    if impute_mode == 'mean':
        # Impute missing values with the mean of the column
        df[column_name].fillna(df[column_name].mean(), inplace=True)
    
    if impute_mode == 'median':
        # Impute missing values with the median of the column
        df[column_name].fillna(df[column_name].median(), inplace=True)

    return df

def remove_columns(df: pd.DataFrame, columns_to_remove: list[str]) -> pd.DataFrame:
    """
    Remove specified columns from a DataFrame.
    
    Arguments:
    df (pd.DataFrame): The DataFrame from which to remove columns.
    columns_to_remove ([str]): A list of column names to remove.
    
    Returns:
    pd.DataFrame: The DataFrame with the specified columns removed.
    """
    
    # Check that the columns exist in the DataFrame
    missing_columns = [column for column in columns_to_remove if column not in df.columns]
    if missing_columns:
        raise ValueError(f'The following columns are not present in df: {missing_columns}')
    
    # Drop the specified columns
    df.drop(columns=columns_to_remove, inplace=True)
    
    return df

def standard_scale_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Standardise a column using Z-score scaling so that it has a mean of 0 and a standard
    deviation of 1.
    
    Arguments:
    df (pd.DataFrame): The DataFrame containing the column.
    column_name (str): The column to standardise.

    Returns:
    pd.DataFrame: DataFrame with standardised column.
    """

    # Check that the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f'{column_name} is not present in df')

    # Scale the column using Z-score scaling
    mean = df[column_name].mean()
    std = df[column_name].std()
    df[column_name] = (df[column_name] - mean) / std

    return df

def min_max_scale_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Normalize a column using Min-Max Scaling so that it ranges from 0 to 1.
    
    Arguments:
    df (pd.DataFrame): The DataFrame containing the column.
    column_name (str): The column to normalize.

    Returns:
    pd.DataFrame: DataFrame with normalized column.
    """
    
    # Check that the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f'{column_name} is not present in df')

    # Scale the column using Min-Max Scaling so that it ranges from 0 to 1
    min_val = df[column_name].min()
    max_val = df[column_name].max()
    df[column_name] = (df[column_name] - min_val) / (max_val - min_val)

    return df

def one_hot_encode_column(df: pd.DataFrame, column_to_encode: str) -> pd.DataFrame:
    """
    Perform one-hot encoding on a specified categorical column.
    
    Arguments:
    df (pd.DataFrame): The DataFrame containing the categorical column.
    column_to_encode (str): The name of the categorical column to encode.

    Returns:
    pd.DataFrame: DataFrame with the one-hot encoded column.
    """

    # Check that the column exists in the DataFrame
    if column_to_encode not in df.columns:
        raise ValueError(f'{column_to_encode} is not present in df')
    
    df = pd.get_dummies(df, columns=[column_to_encode])

    return df

def cast_column(df: pd.DataFrame, column_name: str, data_type: type) -> pd.DataFrame:
    """
    Cast a column to a specified data type.
    
    Arguments:
    df (pd.DataFrame): The DataFrame containing the column.
    column_name (str): The name of the column to cast.
    data_type (type): The target data type (e.g., int, float, str, bool).
    
    Returns:
    pd.DataFrame: DataFrame with the column cast to the specified type.
    """
    assert column_name in df.columns, f'{column_name} not in df'
    
    try:
        df[column_name] = df[column_name].astype(data_type)
    except ValueError as e:
        raise ValueError(f"Cannot cast {column_name} to {data_type}: {e}")
    
    return df

def rename_columns(df: pd.DataFrame, rename_dict: dict[str, str]) -> pd.DataFrame:
    """
    Rename multiple columns in a DataFrame.

    Arguments:
    df (pd.DataFrame): The DataFrame with columns to rename.
    rename_dict (dict): Dictionary mapping old column names to new column names.

    Returns:
    pd.DataFrame: DataFrame with renamed columns.
    """

    df = df.rename(columns=rename_dict)

    return df

def reorder_columns(df: pd.DataFrame, new_order: list[str]) -> pd.DataFrame:
    """
    Reorder the columns of a DataFrame.

    Arguments:
    df (pd.DataFrame): The DataFrame to modify.
    new_order (list[str]): List of column names in the desired order.

    Returns:
    pd.DataFrame: DataFrame with columns reordered.
    """

    assert set(new_order) == set(df.columns), "new_order must contain all and only the columns of df"

    df = df[new_order]
    
    return df
