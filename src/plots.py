import plotly.express as px
import polars as pl
from src.dataloader import sorted_data, df

def make_bar_plot(input_color_theme, df: pl.DataFrame = sorted_data):
    return px.bar(data_frame=df, x= "total_population", y="states", color_continuous_scale=input_color_theme)

def make_choropleth(input_color_theme, input_df=df):
    choropleth = px.choropleth(input_df, locations="states", color="total_population", locationmode="USA-states",
                               color_continuous_scale=input_color_theme,
                               #range_color=(0, df.select("total_population").max()),
                               scope="usa",
                               labels={'population':'total_population'}
                              )
    choropleth.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350
    )
    return choropleth
