#%%
import polars as pl
import pandas as pd

df = pd.DataFrame({
    'household_id': [1, 1, 1, 2, 2, 2],
    'person_id': [1,2,3,4,5,6],
    'female': [True, False, True, False, True, False],
    'income': [10000, 20000, 30000, 40000, 50000, 60000],
})

df = pl.from_pandas(df)

#%%
household_df = (
    df.group_by("household_id")
    .agg(
        pl.col("female")
        .get(pl.col("income").arg_max())
        .alias("highest_earner_female")
    )
    .sort("household_id")
)
# %%
