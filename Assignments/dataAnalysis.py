"""
Author: Akingbayi Ojo
Purpose: To create a data analysis program of life expectancy
Creativity: The user can search by country, year, or both
"""

def process_year_search(file, input_year):
    # Initialize variables for the specified year
    input_total_life = 0
    input_min_life = float("inf")
    input_max_life = -1
    input_min_country = ""
    input_max_country = ""
    life_count = 0

    # Initialize overall max/min life expectancy variables
    overall_max_life = -1
    overall_min_life = float("inf")
    overall_max_year = -1
    overall_min_year = -1
    overall_max_country = ""
    overall_min_country = ""

    for line in file:
        if not line.startswith("Entity"):
            line = line.strip()
            entity, code, year, life_expectancy = line.split(",")
            year = int(year)
            life_expectancy = float(life_expectancy)

            # Update overall max/min life expectancy across all years
            if life_expectancy > overall_max_life:
                overall_max_life = life_expectancy
                overall_max_country = entity
                overall_max_year = year

            if life_expectancy < overall_min_life:
                overall_min_life = life_expectancy
                overall_min_country = entity
                overall_min_year = year

            # Update stats for the year the user is interested in
            if year == input_year:
                input_total_life += life_expectancy
                life_count += 1

                if life_expectancy < input_min_life:
                    input_min_life = life_expectancy
                    input_min_country = entity

                if life_expectancy > input_max_life:
                    input_max_life = life_expectancy
                    input_max_country = entity

    # Calculate the average life expectancy for the input year
    if life_count > 0:
        average_life = input_total_life / life_count
    else:
        average_life = None

    # Output overall statistics
    print(f"\nThe overall max life expectancy is: {overall_max_life:.2f} from {overall_max_country} in {overall_max_year}")
    print(f"The overall min life expectancy is: {overall_min_life:.2f} from {overall_min_country} in {overall_min_year}")

    # Output statistics for the input year
    if average_life:
        print(f"\nFor the year {input_year}:")
        print(f"The average life expectancy across all countries was {average_life:.2f}")
        print(f"The max life expectancy was in {input_max_country} with {input_max_life:.2f}")
        print(f"The min life expectancy was in {input_min_country} with {input_min_life:.2f}")
    else:
        print(f"\nNo data found for the year {input_year}.")

def process_country_search(file, input_country):
    country_data = []

    for line in file:
        if not line.startswith("Entity"):
            line = line.strip()
            entity, code, year, life_expectancy = line.split(",")
            life_expectancy = float(life_expectancy)

            # Match the input country
            if entity.lower() == input_country.lower():
                country_data.append((year, life_expectancy))

    if country_data:
        # Sort by year for output clarity
        country_data.sort()

        print(f"\nLife expectancy data for {input_country}:")
        for year, life_expectancy in country_data:
            print(f"{year}: {life_expectancy:.2f}")
    else:
        print(f"\nNo data found for the country: {input_country}")

def main():
    file_path = "Python/Assignments/life-expectancy.csv"

    try:
        with open(file_path) as file:
            # Ask the user for search type: year or country
            search_type = input("Do you want to search by 'year', 'country', or 'both'? ").strip().lower()

            if search_type == 'year':
                try:
                    input_year = int(input("Enter a year of interest: "))
                    process_year_search(file, input_year)
                except ValueError:
                    print("Invalid input. Please enter a valid numeric year.")
            elif search_type == 'country':
                input_country = input("Enter the country of interest: ").strip().title()
                process_country_search(file, input_country)
            elif search_type == 'both':
                try:
                    input_year = int(input("Enter a year of interest: "))
                    input_country = input("Enter the country of interest: ").strip().title()

                    with open(file_path) as file:  # Re-open file for both searches
                        process_year_search(file, input_year)

                    with open(file_path) as file:  # Re-open file for country search
                        process_country_search(file, input_country)
                except ValueError:
                    print("Invalid input. Please enter a valid numeric year.")
            else:
                print("Invalid option. Please choose 'year', 'country', or 'both'.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()

if __name__ == "__main__":
    main()
