import os
import pandas as pd

from datetime import datetime
from database import Database
from config import *


def generate_service_rating(output_dir="data/tmp"):
    os.makedirs(output_dir, exist_ok=True)
    db = Database(user, password, database, port, host)
    a = db.get_all()
    methods_rating = {}
    methods_published = {}
    methods_count = {}
    for item in a:
        methods_count[item.method] = methods_count.get(item.method, 0) + 1
        methods_rating[item.method] = methods_rating.get(item.method, 0.0) + item.rating
        methods_published[item.method] = methods_published.get(item.method, 0.0) + item.published
    for key in methods_rating:
        methods_rating[key] /= methods_count[key]
        methods_published[key] /= methods_count[key]
    df = pd.DataFrame(methods_rating, index=[0])
    df.to_csv(f"{output_dir}/service-rating.csv", index=False)
    df = pd.DataFrame(methods_published, index=[0])
    df.to_csv(f"{output_dir}/service-published.csv", index=False)


if __name__ == "__main__":
    generate_service_rating()
