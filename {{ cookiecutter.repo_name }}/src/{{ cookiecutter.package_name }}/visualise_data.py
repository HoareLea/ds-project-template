import pandas as pd
import plotly.express as px

from utils import hl_colors

def create_scatter_plot(df: pd.DataFrame, x_axis_column: str, y_axis_column: str,
    colour_column: str = None, title: str = None, plot_trendline: bool = False) -> None:
    """
    Generates an interactive scatter plot using Plotly.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data to be plotted.
    x_axis_column (str): Column name for the x-axis.
    y_axis_column (str): Column name for the y-axis.
    colour_column (str, optional): Column name for coloring the points. Defaults to None.
    title (str, optional): Title of the plot. Defaults to None.
    plot_trendline (bool, optional): If True, adds a trendline to the plot. Defaults to False.

    Returns:
    None
    """
    fig = px.scatter(
        df, 
        x=x_axis_column, 
        y=y_axis_column, 
        color=colour_column if colour_column else None,
        title=title if title else f'{x_axis_column} vs {y_axis_column}',
        color_discrete_sequence=hl_colors,
        trendline='ols' if plot_trendline else None,
        trendline_color_override=hl_colors[1] if plot_trendline else None
    )
    fig.show()
