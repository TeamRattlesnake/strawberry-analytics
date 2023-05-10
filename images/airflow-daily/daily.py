import os
import time
import pandas as pd

from datetime import datetime
from database import Database
from config import *


def generate_daily_analytics(output_dir="data/tmp"):
    os.makedirs(output_dir, exist_ok=True)
    db = Database(user, password, database, port, host)
    a = db.get_all()
    methods = {}
    yesterday = time.time() - 60 * 60 * 24
    for item in a:
        if int(item.date) >= yesterday:
            methods[item.method] = methods.get(item.method, 0) + 1
    df = pd.DataFrame(methods, index=[0])
    df.to_csv(f"{output_dir}/daily-{datetime.today().strftime('%d-%m-%Y')}.csv")


if __name__ == "__main__":
    generate_daily_analytics()
