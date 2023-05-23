import pandas as pd
import matplotlib.pyplot as plt


def generate_service_rating_graph(input_dir="data/tmp", output_dir="data/results/daily"):
    fig = plt.figure()
    df = pd.read_csv(f"{input_dir}/service-rating.csv")
    labels = df.columns
    values = df.iloc[0]
    fig.set_figwidth(12)
    fig.set_figheight(8)
    ax = plt.bar(labels, values, width=0.7)
    fig.savefig(f"{output_dir}/rating.png")

    fig = plt.figure()
    df = pd.read_csv(f"{input_dir}/service-published.csv")
    labels = df.columns
    values = df.iloc[0]
    fig.set_figwidth(12)
    fig.set_figheight(8)
    ax = plt.bar(labels, values, width=0.7)
    fig.savefig(f"{output_dir}/published-rating.png")


if __name__ == "__main__":
    generate_service_rating_graph()
