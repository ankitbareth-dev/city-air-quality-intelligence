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
              
def analyze_air_quality_by_city(data: pd.DataFrame) -> None:
    cities = data["city"].drop_duplicates().reset_index(drop=True)
    for index, city in enumerate(cities, start=1):
        print(f"{index}. {city}")
    print()


    while True:
        try:
            city_index = int(input("Select a city: ").strip())
        except ValueError:
            print()
            print("Error: Enter a valid number.")
            continue

        if 1 <= city_index and city_index <= len(cities):
            selected_city = cities[city_index - 1]
            city_data = data[data["city"] == selected_city]
            print("\nAverage air quality measurements:")
            print()
            averages = city_data[["pm25", "pm10", "temperature", "humidity"]].mean()
            for column, value in averages.items():
                print(f"{column}: {value}")
            break    
        else:
            print("Error: Select a city from the list.")
            print()