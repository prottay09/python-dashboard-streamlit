# %%
import polars as pl
df = pl.read_excel("data/population_data.xlsx", read_options={"skip_rows":4}, has_header=False)
df  = (
    df
    .rename({
        'column_1': 'states',
        'column_2': 'total_population',
        'column_3': 'age(18+)',
        'column_4': 'age(18+) in %'
    })
    .drop_nulls()
    .with_columns(
        states = pl.when(
            pl.col("states").str.starts_with(".")
            ).then(pl.col("states").str.slice(1)).otherwise(pl.col("states"))

    )
    .filter(pl.col("states")!="United States")
)

# get unique states
unique_states = df.select("states").unique().to_series().to_list()

sorted_data = df.select("states", "total_population").sort("total_population", descending=True)


