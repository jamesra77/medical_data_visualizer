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
        "cholesterol",
        "gluc",
        "smoke",
        "alco",
        "active",
        "overweight",
    ]
    df_cat = pd.melt(df, value_vars=value_vars)


    # 6
    df_cat = df_cat.groupby("variable")
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

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
