import numpy as np
import pandas as pd
import scikit_posthocs as sp
import stats_test as st

df = pd.read_csv("analyze.csv", header = 0)
st.stats_test(df, val_col = "time", group_col = "pos")
df_result_time = sp.posthoc_dscf(df, val_col = "time", group_col = "pos")
print(df_result_time)
# st.stats_test(df, val_col = "accuracy", group_col = "type")
# df_result_accuracy = sp.posthoc_dscf(df, val_col = "accuracy", group_col = "type")
# print(df_result_accuracy)