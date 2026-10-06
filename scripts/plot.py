# %%
import pandas as pd
import numpy as np
import seaborn as sns

data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=["a", "b"]
)

# %%
sns.scatterplot(data=data, x="a", y="b")
