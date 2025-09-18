import eurostat, pandas as pd
df = eurostat.get_data_df('hlth_co_disch2')
df.to_csv('hlth_co_disch2.csv', index=False)
