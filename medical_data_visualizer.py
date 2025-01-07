import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
bmi = (df["weight"] / (df["height"] / 100) ** 2)
df['overweight'] = bmi.map(lambda x: 0 if x < 25 else 1)

# 3
df["cholesterol"] = df["cholesterol"].map(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].map(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5
    value_vars = [
        "active",
        "alco",
        "cholesterol",
        "gluc",
        "overweight",
        "smoke",
    ]

    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=value_vars) # partially correct?


    # 6
    df_cat_counts = df_cat.groupby(["variable", "value"]).value_counts().to_frame().rename(columns={"count":"total"}) # almost - need to split values along cardio being 0 or 1

    # 7
    sns.catplot(df_cat_counts, kind="bar", x="variable", hue="value", y="total", col="cardio")



    # 8
    fig = sns.catplot(df_cat_counts, kind="bar", x="variable", hue="value", y="total", col="cardio")


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    bp_condition = df["ap_lo"] <= df["ap_hi"]
    df_heat = df[bp_condition]

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
