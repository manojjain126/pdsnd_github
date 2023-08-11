import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze the data.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter the city (Chicago , New York City or Washington) : ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid City !! . Enter a valid input from given cities.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "Enter the month (January, Februaray , March , April , May , June) or 'All' for all months : "
        ).lower()
        months = ["january", "february", "march", "april", "may", "june", "all"]
        if month in months:
            break
        else:
            print("Invalid Month !! . Enter a valid input from given months.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            "Enter the day (Monday, Tuesday , Wednesday , Thursday , Friday , Saturday) or 'All' for all days : "
        ).lower()
        days = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
            "all",
        ]
        if day in days:
            break
        else:
            print("Invalid Day !! Enter a valid input from given days.")

    print("-" * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df['Month'] = df["Start Time"].dt.month_name()
    df['weekday'] = df["Start Time"].dt.day_name()

    # Month Filter
    if month != "all":
        df = df[df['Month'] == month]

    # Day Filter
    if day != "all":
        df = df[df['weekday'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # TO DO: display the most common month
    most_common_months = df["Start Time"].dt.month.mode()
    most_common_month = ", ".join(
        [calendar.month_name[month] for month in most_common_months]
    )

    print(" Most Common Month is: ", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df["Start Time"].dt.day_name().mode()[0]
    print(" Most Common Day is: ", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df["Start Time"].dt.hour.mode()[0]
    print(" Most Common Hour is: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df["Start Station"].mode()[0]
    print("Most Common Used Start Station is : ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]
    print("Most Common Used End Station is : ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_station_combination = (
        df["Start Station"] + " to" + df["End Station"]
    ).mode()[0]
    print(
        "Most Frequent Station Combination of Start and End Station Trip is : ",
        most_frequent_station_combination,
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total Travel Time (Seconds) : ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("MEan Travel Time (Seconds) : ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = None
    user_type_count = df["User Type"].value_counts()
    print("\nCounts of User Types:")
    for user_type, count in user_type_count.items():
        print(user_type + ":" + str(count))


    # TO DO: Display counts of gender
    gender_count = None
    if "Gender" in df.columns:
        gender_count = df["Gender"].value_counts()
        print("\nCounts of Gender:")
        for gender, count in gender_count.items():
            print(gender + ":" + str(count))

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year_stats = None
    if "Birth Year" in df.columns:
        earliest_birth_year = int(df["Birth Year"].min())
        most_recent_birth_year = int(df["Birth Year"].max())
        most_common_birth_year = int(df["Birth Year"].mode()[0])
        birth_year_stats = f"Earliest birth year: {earliest_birth_year} \n"\
                           f"Most recent birth year: {most_recent_birth_year} \n"\
                           f"Most common birth year: {most_common_birth_year}"
        print("\nUser Stats:", birth_year_stats)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

def raw_data(df):
    """Displays Raw data until user inputs."""

    start_time = time.time()

    # TO DO: display Raw Data
    raw_data_input = input("\nWould you like to see 5 lines of raw data ? Enter yes or no.\n").lower()
    row = 0
    while raw_data_input =='yes':
        print(df.iloc[row: row+5])
        row +=5
        raw_data_input = input("\nWould you like to see 5 lines of raw data ? Enter yes or no.\n").lower()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

def test_load_data():
    # Test the condition
    result = load_data('washington', 'all', 'monday').shape[0] == load_data('washington', 'all', 'all').shape[0]

    # Print the result of the test
    if result:
        print("The number of rows are same.")
    else:
        print("The number of rows are different.")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
#        test_load_data()
        raw_data(df)

        restart = input("\nWould you like to restart? Enter yes or no : \n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
