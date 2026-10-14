import pandas as pd

def load_data() -> pd.DataFrame:

    file_path = "data/air_quality.csv"

    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame()

def view_all_records(data: pd.DataFrame) -> None:
    print()
    print(data)
              
def analyze_air_quality_by_city(city: str) -> None:
    pass

