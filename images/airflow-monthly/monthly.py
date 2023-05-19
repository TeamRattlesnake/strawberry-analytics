import os
import time

from datetime import datetime
from database import Database
from config import *


def generate_monthly_analytics(output_dir="data/tmp"):
    os.makedirs(output_dir, exist_ok=True)
    db = Database(user, password, database, port, host)
    a = db.get_all()
    month_ago = time.time() - 60 * 60 * 24 * 30
    days = [[i, 0] for i in range(1, 31)]

    for item in a:
        if int(item.date) < month_ago:
            continue
        days[(int(item.date)-int(month_ago)) // (60 * 60 * 24)][1] += 1

    with open(f"{output_dir}/monthly-{datetime.today().strftime('%d-%m-%Y')}", 'w') as f:
        for day in days:
            f.write(f"{day[0]};{day[1]}\n")


if __name__ == "__main__":
    generate_monthly_analytics()
