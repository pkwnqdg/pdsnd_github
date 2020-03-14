#Bikeshare Project Created March 1, 2020
#by Ted Jordan
import time
import pandas as pd
#import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

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
    print("Which City?  ")
    city = input().lower()
    while city not in {"chicago", "new york city", "washington"}:
        city = input ("Please choose from: chicago, new york city, or washington. Which City? ")


    # TO DO: get user input for month (all, january, february, ... , june)
    print("Which Month?  ")
    month = input().lower()
    while month not in {'january', 'february', 'march', 'april', 'may', 'june', 'all'}:
        month = input ("Please choose from: january, february, march, april, may, june, or all.  ")



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("What Day of the Week?  ")
    day = input().title()
    while day not in {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'all', 'All'}:
        day = input ("Please choose from: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all.  ")




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

    # convert the Start and End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
#        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    popular_month = months[popular_month-1]
    print('Most Popular Month:',popular_month)


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_dow = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week: ', popular_dow)


    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hr = df['hour'].mode()[0]
    print('Most Popular Hour:  ',popular_hr)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The Most Common Start Station is: ',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The Most Common End Station is: ',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    pop_SS_ES = df['Start Station'] + ' Station and '+ df['End Station'] + ' Station'
    pop_SS_ES = pop_SS_ES.mode()[0]
    print('The Most Popular Start and End Stations Combos are:\n ',pop_SS_ES)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['tripduration'] = df['End Time'] - df['Start Time']
    df['duration']= df['tripduration'].cumsum()
    print('The Total Travel Time Over the Specified Period is: ',df['duration'].iloc[-1])
    df['Trip Duration'] = df['Trip Duration'].cumsum()
    print('The Total Travel Time Over the Specified Period is: ',df['Trip Duration'].iloc[-1], ' seconds')
    # TO DO: display mean travel time
    df['tripduration'] = df['End Time'] - df['Start Time']
    df['mean']= df['tripduration'].mean()
    print('The Mean Travel Time Over the Specified Period is: ',df['mean'].iloc[-1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df['User Type'] = df['User Type'].fillna('Empty')
    print(df['User Type'].value_counts())
    print('\n')


    # TO DO: Display counts of gender

    #for col in list(df) determine if Gender is found:
    if ('Gender' in list(df)):
        print('Gender was found')
        df['Gender'] = df['Gender'].fillna('Empty')
        print(df['Gender'].value_counts())
    else:
        print('Gender not in the file')






    # TO DO: Display earliest, most recent, and most common year of birth

    if ('Birth Year' in list(df)):
        print('Birth Year Was Found.')
        df['Birth Year'] = pd.to_numeric(df['Birth Year'],errors='ignore')
        birthyear = df['Birth Year'].mode()[0]
        print('The Most Common Year of Birth is: ',int(birthyear))

        earliest = df['Birth Year'].min()
        print('The Earliest Birth Year is: ',int(earliest))

        most_recent = df['Birth Year'].max()
        print('The Most recent Birth Year is: ',int(most_recent))


    else:
        print('No Birth Year Was Found.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw(df):
    index1=0
    index2=5
    while True:
       raw_data = input('Would you like to see 5 rows of raw data?\nPlease select yes or no.').lower()
       if raw_data == 'yes':
           print(df.iloc[index1:index2])
           index1 += 5
           index2 += 5
           continue
       else:
           break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw(df)





        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
