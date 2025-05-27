"""
It is a custom Python module for data process.
"""
import os
from typing import Union

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def load_data(
        path: str,
        columns: list,
        keyword: str = None,
        rename_columns: list = None,
):
    """
    Load and concat data from a specified folder.

    Parameters:
        - path: str, a folder path for the data files.
        - columns: list(str), column name list.
        - keyword: str, a keyword within filenames for load specified files.
        - rename_columns: list(str), rename columns.
    Returns:
        - data: pandas DataFrame.
    """
    # Capture exceptions in file reading, such as incorrect reading path
    try:
        files = os.listdir(path)
    except IOError as e:
        print(f'[Error] failed to read files from path: {os.path.abspath(path)}, message: {e}')
        return None
    df = None
    file_path = None
    # Capture exceptions in file reading, such as file format error
    try:
        for f in files:
            if not f.endswith('.csv') or (keyword and keyword not in f):
                continue
            file_path = path + f
            data = pd.read_csv(file_path, low_memory=False, usecols=columns)
            if df is None:
                df = data
            else:
                df = pd.concat([df, data])
    except Exception as e:
        print(f'[Error] fail to read file: {os.path.abspath(file_path)}, message: {e}')
        return None
    if rename_columns:
        df.columns = rename_columns
    return df


def trim_and_fill_dataframe(
        data: pd.DataFrame,
        value: object,
):
    """
    Trim the beginning and ending rows with missing values
    and fill other missing values with a specified value.

    Parameters:
        - data: pd.DataFrame.
        - value: number or string, the default value.
    Returns:
        - new_data: pandas DataFrame.
    """
    data_drop_na = data.dropna()
    data = data[(data.index >= data_drop_na.index.min())
                & (data.index <= data_drop_na.index.max())]
    return data.fillna(value)


def set_full_time_index(
        data: pd.DataFrame,
        time_col: str,
        freq: str,
):
    """
    Set full time index for a DataFrame.

    Parameters:
        - data: pd.DataFrame.
        - time_col: string, the name of the time column.
        - freq: string, the frequency of the data, eg: 15min.
    Returns:
        - new_data: pandas DataFrame, new data with time index.
    """
    _data = data.set_index(time_col)
    _data = _data[~_data.index.duplicated(keep='last')]
    start_time = _data.index.min()
    end_time = _data.index.max()
    full_time_index = pd.date_range(start=start_time, end=end_time, freq=freq)
    return _data.reindex(full_time_index)


def average_fill(
        data: pd.DataFrame,
):
    """
    Replace missing values by the average of the forward and backward values for a DataFrame.

    Parameters:
        - data: pd.DataFrame.
    Returns:
        - new_data: pandas DataFrame.
    """
    # Replace missing values with the forward value
    data_f = data.ffill().infer_objects(copy=False)
    # Replace missing values with the backward value
    data_b = data.bfill().infer_objects(copy=False)
    # Replace missing values with the average of the forward and backward values
    return (data_f + data_b) / 2


def reduce_dimension(
        data: pd.DataFrame,
        n_components: int,
        column_names: [str] = None,
):
    """
    Reduce dimensions by PCA for a DataFrame.

    Parameters:
        - data: pd.DataFrame.
        - n_components: int, number of PCA components (dimensions).
        - columns_names: [str], the name of columns.
    Returns:
        - new_data: pandas DataFrame.
    """
    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Initialize PCA and fit it to the data
    pca_model = PCA(n_components=n_components)
    pca_result = pca_model.fit_transform(scaled_data)

    # Return a new dataframe with the PCA results
    return pd.DataFrame(data=pca_result, columns=column_names)


def prepare_data_for_regression(
        data: pd.DataFrame,
):
    """
    Prepare data for regression by extracting week_of_year, day_of_week and hour attributes.

    Parameters:
        - data: pd.DataFrame.
    Returns:
        - new_data: pandas DataFrame, new data with week_of_year, day_of_week and hour columns.
    """
    new_data = data
    new_data['week_of_year'] = data.index.day_of_year // 7
    # Extract the day of the week (0=Monday, 6=Sunday)
    new_data['day_of_week'] = data.index.dayofweek
    new_data['hour'] = data.index.hour
    return new_data


def extract_values(data: pd.DataFrame,
                   source_col: str,
                   cols: [str],
                   saved_cols: [str],
                   validated_col: str = None,
                   validated_code: str = '1',
                   convert_cols_to_int: [str] = None):
    """
    Extract values from multi-values in a string within pd.DataFrame.

    Parameters:
        - data: pd.DataFrame.
        - source_col: str, the name of the target column.
        - cols: list(str), new column names.
        - saved_cols: list(str), the remaining columns.
        - validated_col: str, the name of the validated column.
        - validated_code: str, the code for valid.
        - convert_cols_to_int: list(str), a name list of columns, which are needed to be converted to int.
    Returns:
        - new_data: pandas DataFrame, new data .
    """
    expend_data = data[source_col].str.split(',', expand=True)
    expend_data.columns = cols
    data = pd.concat([data, expend_data], axis=1)
    if validated_col:
        for col in saved_cols:
            data.loc[:, col] = np.where(data[validated_col] == validated_code, data[col], np.nan)
    for col in saved_cols:
        data.loc[:, col] = data[col].bfill()
        data.loc[:, col] = data[col].ffill()
    if convert_cols_to_int:
        for col in convert_cols_to_int:
            data.loc[:, col] = data[col].astype(int)
    return data.drop(columns=[c for c in cols if c not in saved_cols])


if __name__ == '__main__':
    traffic_path = 'data/traffic/'
    weather_path = 'data/weather/'
    _traffic_columns = ['Report Date', 'Time Interval', 'Total Volume']
    _traffic_rename_columns = ['date', 'interval', 'total']
    _traffic1 = load_data(traffic_path, keyword='19078', columns=_traffic_columns,
                          rename_columns=_traffic_rename_columns)
    _traffic2 = load_data(traffic_path, keyword='19124', columns=_traffic_columns,
                          rename_columns=_traffic_rename_columns)
    _traffic1.date = (pd.to_datetime(_traffic1.date, format='%d/%m/%Y %H:%M:%S')
                      + pd.to_timedelta(_traffic1.interval * 15, unit='m'))
    _traffic1 = set_full_time_index(_traffic1, time_col='date', freq='15T')
    _traffic1 = _traffic1.drop(columns='interval')
    _traffic2.date = (pd.to_datetime(_traffic2.date, format='%d/%m/%Y %H:%M:%S')
                      + pd.to_timedelta(_traffic2.interval * 15, unit='m'))
    _traffic2.set_index(_traffic2.date, inplace=True)
    _traffic2 = _traffic2.drop(columns='interval')
    _traffic = trim_and_fill_dataframe(_traffic1, 0)
    _traffic = _traffic.resample('h').sum()
    _weather = load_data(weather_path, columns=['DATE', 'REPORT_TYPE', 'WND', 'CIG', 'VIS', 'TMP', 'DEW', 'SLP'],
                         rename_columns=['date', 'report_type', 'wnd', 'cig', 'vis', 'tmp', 'dew', 'slp'])
    _weather = extract_values(_weather, source_col='wnd',
                              cols=['wnd_angle', 'wnd_qc', 'wnd_tq', 'wnd_speed', 'wnd_speed_qc'],
                              saved_cols=['wnd_speed'], validated_col='wnd_speed_qc', convert_cols_to_int=['wnd_speed'])
    _weather = extract_values(_weather, source_col='cig', cols=['cig_height', 'cig_qc', 'cig_dc', 'cig_cavok'],
                              saved_cols=['cig_height'], validated_col='cig_qc', convert_cols_to_int=['cig_height'])
    _weather = extract_values(_weather, source_col='vis', cols=['vis_dist', 'vis_qc', 'vis_vc', 'vis_vqc'],
                              saved_cols=['vis_dist'], validated_col='vis_qc', convert_cols_to_int=['vis_dist'])
    _weather = extract_values(_weather, source_col='tmp', cols=['tmp_cs', 'tmp_qc'],
                              saved_cols=['tmp_cs'], validated_col='tmp_qc', convert_cols_to_int=['tmp_cs'])
    _weather = extract_values(_weather, source_col='dew', cols=['dew_tmp', 'dew_qc'],
                              saved_cols=['dew_tmp'], validated_col='dew_qc', convert_cols_to_int=['dew_tmp'])
    _weather = extract_values(_weather, source_col='slp', cols=['slp_val', 'slp_qc'],
                              saved_cols=['slp_val'], validated_col='slp_qc', convert_cols_to_int=['slp_val'])
    weather_multivalued_columns = ['wnd', 'cig', 'vis', 'tmp', 'dew', 'slp']
    _weather = _weather.drop(columns=weather_multivalued_columns)
    _weather = _weather[_weather.report_type == 'FM-12']
    _weather = _weather.drop(columns='report_type')
    # Convert date format
    _weather.date = pd.to_datetime(_weather.date)
    # Set date as index
    _weather = set_full_time_index(_weather, time_col='date', freq='h')
    # Replace missing values with the average of the forward and backward values
    _weather = average_fill(_weather)
    _weather = _weather[(_weather.index >= _traffic.index.min())
                        & (_weather.index <= _traffic.index.max())]
    _rg_weather = prepare_data_for_regression(_weather)
    test_weeks = 2
    train_size = len(_traffic) - 24 * 7 * test_weeks
    rg_weather_train, rg_weather_test = _rg_weather[:train_size], _rg_weather[train_size:]
    _traffic_train, _traffic_test = _traffic[:train_size], _traffic[train_size:]
    linear_model = LinearRegression()
    linear_model.fit(_rg_weather, _traffic.total)
    linear_forecast = linear_model.predict(rg_weather_test).astype(int)
