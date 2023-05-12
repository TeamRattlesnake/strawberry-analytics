import os
import matplotlib.pyplot as plt

from datetime import datetime, date, timedelta


def generate_daily_graph(input_dir="data/tmp", output_dir="data/results/monthly"):
    os.makedirs(output_dir, exist_ok=True)
    X = []
    Y = []
    with open(f"{input_dir}/monthly-{datetime.today().strftime('%d-%m-%Y')}", 'r') as f:
        for line in f:
            x, y = line.strip().split(';')
            cur_date = date.today() - timedelta(days=(30-int(x)))
            X.append(cur_date.strftime("%d.%m"))
            Y.append(int(y))

    fig, ax = plt.subplots()
    ax.bar(X, Y, color='maroon', width=0.4)

    fig.savefig(f"{output_dir}/{datetime.today().strftime('%d-%m-%Y')}.png")


if __name__ == "__main__":
    generate_daily_graph()
