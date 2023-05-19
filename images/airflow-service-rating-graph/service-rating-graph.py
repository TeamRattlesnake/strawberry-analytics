import pandas as pd
import matplotlib.pyplot as plt


def generate_service_rating_graph(input_dir="data/tmp", output_dir="data/results/daily"):
    fig = plt.figure()
    df = pd.read_csv(f"{output_dir}/service-rating.csv")
    ax = df.plot.bar(x="method", y="rating", rot=0)
    fig.savefig(f"{output_dir}/rating.png")


if __name__ == "__main__":
    generate_service_rating_graph()
