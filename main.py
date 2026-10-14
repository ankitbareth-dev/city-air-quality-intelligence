import utlis as ut

def main() -> None:
    data = ut.load_data()
    if data.empty:
        print("Error: CSV file not found.")
        return
    while True:
        print()
        print("======= CITY AIR QUALITY INTELLIGENCE =======")
        print()
        print("1. View all records")
        print("2. Analyze a city's air quality")
        print("3. Compare cities")
        print("4. Analyze pollution trends")
        print("5. Find unusual pollution readings")
        print("6. Export analysis results")
        print("7. Exit")
        try:
            choice = int(input("Enter your choice (1 to 7): ").strip())
            print()
        except ValueError: 
            print()
            print("Error : Enter a valid choice")
            continue
        match choice:
            case 1:
                ut.view_all_records(data)
            case 2:
                ut.analyze_air_quality_by_city(data)
            case 3:
                print("3")
            case 4:
                print("4")
            case 5:
                print("5")
            case 6:
                print("6")
            case 7:
                break
            case _:
                print()
                print("Error : Please choose between 1 to 7")
main()

