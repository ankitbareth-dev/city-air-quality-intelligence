def main():
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
        except ValueError: 
            print()
            print("Error : Enter a valid choice")
            continue
        match choice:
            case 1:
                print("1")
            case 2:
                print("2")
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

