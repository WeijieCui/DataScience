"""It is a custom python module to provide functions for visualization"""
from typing import Union

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def plot_target_exog_variables(
        x: pd.DataFrame,
        y: Union[pd.Series, pd.DataFrame],
        title: str,
):
    """
    Visualize target and exogenous variables to the same figure.

    Parameters:
        - x: pd.DataFrame, exogenous variables.
        - y: pd.Serial | pd.DataFrame, the target variable.
        - title: the title of the figure.
    """
    # normalize the data to the same range for better visualization
    scaler = MinMaxScaler()
    norm_x = scaler.fit_transform(x)
    norm_x = pd.DataFrame(norm_x, columns=x.columns)
    norm_x.set_index(x.index, inplace=True)
    norm_y = scaler.fit_transform(y)
    norm_y = pd.DataFrame(norm_y, columns=y.columns)
    norm_y.set_index(y.index, inplace=True)

    # plot a figure
    plt.figure(figsize=(12, 6))
    plt.plot(norm_x, label=norm_x.columns, linewidth=1, linestyle='--')
    plt.plot(norm_y, label='target', linewidth=2, marker='s')
    plt.legend()
    plt.title(title)


def visualize_results(
        source_data: pd.DataFrame,
        forecast: Union[list, pd.DataFrame],
        labels: Union[str, list],
        title: str,
):
    """
    Visualize results by a plot function of Matplotlib.

    Parameters:
        - source_data: pd.DataFrame, real values.
        - forecast: list(pd.DataFrame) | pd.DataFrame, predictions of one or more models.
        - labels: list(str) | str, one or more labels.
        - title: the title of the figure.
    """
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
              'tab:brown', 'tab:pink', 'tab:cyan']
    plt.figure(figsize=(12, 6))
    plt.plot(source_data, label='real data sample', color='tab:olive')
    if isinstance(forecast, list):
        for idx, prediction in enumerate(forecast):
            plt.plot(prediction.index, prediction,
                     label=labels[idx], color=colors[idx % len(colors)], linestyle='--')
        plt.axvline(forecast[0].index[0], color='tab:gray', linestyle='--', label='train/test ratio')
    else:
        plt.plot(forecast.index, forecast, label=labels, color=colors[0], linestyle='--')
        plt.axvline(forecast.index[0], color='tab:gray', linestyle='--', label='train/test ratio')
    plt.legend()
    plt.title(title)
