import os
import time
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime


def generate_daily_graph(output_dir="data/results/daily"):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(f"{output_dir}/daily-{datetime.today().strftime('%d-%m-%Y')}.csv")
    labels = list(df.columns)
    sizes = df.loc[0, :].values.flatten().tolist()

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)

    fig.savefig(f"{output_dir}/{datetime.today().strftime('%d-%m-%Y')}.png")


if __name__ == "__main__":
    generate_daily_graph()
