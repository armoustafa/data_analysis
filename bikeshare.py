import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data from Chicago, New York or Washington?').lower().title()
    while city not in ['Chicago', 'New York', 'Washington']:
        city = input('That seems wrong would you try again? (Chicago, New York, Washington)').lower().title()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Would you like to filter the data based on which month? (all, january, february, ... , june)').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may','june'] :
        month = input('That seems wrong would you try again? (all, january, february, march, april, may, june)').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Would you like to filter the data based on which day? (all, monday, tuesday, ... sunday)').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('That seems wrong would you try again? (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)').lower()

    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day of week is {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most popular start hour is {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most popular start station is {}'.format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print('The most popular end station is {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    start, end = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent trip starts from {} and ends in {}'.format(start, end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Average travel time is {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('There are two types of users\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('Our users are \n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Our users youngest was born in {} and their oldest was born in {} while our most common year of birth is {}'.format(int(df['Birth Year'].max()),int(df['Birth Year'].min()),int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'Washington':
            user_stats(df)
        view_display = input("\nWould you like to view 5 rows of the data? Enter yes or no?")
        start_loc = 0
        while (view_display =="yes" ):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you want to see the next five row too?").lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
