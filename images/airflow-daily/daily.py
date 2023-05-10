import os
import pandas as pd

from datetime import datetime
from database import Database
from config import *


SIZE = 100
NAME_OF_GENERATED_DATA = "generated_data.csv"


def generate_daily_analytics(output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)
    db = Database(user, password, database, port, host)
    a = db.get_all()
    methods = {}
    yesterday = datetime.date.today() - datetime.timedelta(1)
    unix_time = yesterday.strftime("%s")
    for item in a:
        if int(item.date) >= int(unix_time):
            methods[item.method] = methods.get(item.method, 0) + 1
    df = pd.DataFrame(methods)
    df.to_csv(f"{output_dir}/daily-{datetime.today().strftime('%d-%m-%Y')}.csv")


if __name__ == "__main__":
    generate_daily_analytics()
