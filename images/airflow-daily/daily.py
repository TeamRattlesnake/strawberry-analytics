import os


from database import Database
from config import *


SIZE = 100
NAME_OF_GENERATED_DATA = "generated_data.csv"


def generate_daily_analytics(output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)
    db = Database(user, password, database, port, host)
    methods = ['hi']
    print(methods)


if __name__ == "__main__":
    generate_daily_analytics()
