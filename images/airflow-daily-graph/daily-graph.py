import os
import time
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime


def generate_daily_graph(input_dir="data/tmp", output_dir="data/results/daily"):
    os.makedirs(output_dir, exist_ok=True)
    try:
        df = pd.read_csv(f"{input_dir}/daily-{datetime.today().strftime('%d-%m-%Y')}.csv")
        labels = list(df.columns)
        sizes = df.loc[0, :].values.flatten().tolist()
    except pd.errors.EmptyDataError:
        pass
    else:
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct="%1.1f%%")

        fig.savefig(f"{output_dir}/{datetime.today().strftime('%d-%m-%Y')}.png")

    df = pd.read_csv(f"{input_dir}/all-daily-{datetime.today().strftime('%d-%m-%Y')}.csv")
    labels = list(df.columns)
    sizes = df.loc[0, :].values.flatten().tolist()

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%")

    fig.savefig(f"{output_dir}/all-pie.png")



if __name__ == "__main__":
    generate_daily_graph()
