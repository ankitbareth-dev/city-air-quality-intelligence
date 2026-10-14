import pandas as pd

def view_all_records() -> None:
    print()

    file_path = "data/air_quality.csv"

    data = pd.read_csv(file_path)

    print(data)