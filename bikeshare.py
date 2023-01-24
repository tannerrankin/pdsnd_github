import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }
months_dict = ['January', 'February', 'March', 'April', 'May', 'June']

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input('Please choose city: Chicago, New York City, or Washington?\n').title()
        if city not in ('Chicago', 'New York City', 'Washington'):
            print('Invalid input. Please try again.\n')
            continue
        else:
            break
    
    while True:
        month = input('Please choose month: January, February, March, April, May, June, or All\n').title()
        if month not in ('J','January', 'February', 'March', 'April', 'May', 'June', 'All'):
            print('Invalid input. Please try again.\n')
            continue
        else:
            break
    
    while True:
        day = input('Please choose day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All\n').title()
        if day not in ('M','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'):
            print('Invalid input. Please try again.\n')
            continue
        else:             
            break    
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
  
# converting the Start Time to datetime column
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extracting the month, day and hour of week from Start Time to have new columns    
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    df['hour'] = df['Start Time'].dt.hour

    # filtering by month if applicable    
    if month != 'All':
        month = months_dict.index(month) + 1
        df = df[df['month'] == month]
    
    # filter by day of week if applicable
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
    
    return df
                
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month is ', most_common_month, '.')

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day is ', most_common_day, '.')

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('Most common start hour is ', most_common_hour, '.')            

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].value_counts().max()
    print('The most commonly used start station is ', most_common_start, '.')

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].value_counts().max()
    print('The most commonly used end station is ', most_common_end, '.')

    # TO DO: display most frequent combination of start station and end station trip
    most_freq_trip = df.groupby(['Start Station', 'End Station']).count()
    print('The most frequent combinaiton of start and end stations is ', most_common_start, ' and ', most_common_end, '.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is ', total_travel_time, '.')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is ', mean_travel_time, '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_values = df['User Type'].value_counts()
    print('The user types represented are ', user_type_values, '.')
    
    # TO DO: Display counts of gender - need try statement due to Key Error
    try:
        gender_type_values = df['Gender'].value_counts()
        print('The genders represented are ', gender_type_values, '.')
    except KeyError:
        print('Data unavailable.')
                                
    # TO DO: Display earliest, most recent, and most common year of birth -- need 3 try statements due to KeyError
    
    # For earliest birth year
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest birth year is ', earliest_birth_year)
    except KeyError:
        print('Data unavailable.')
    
    # For most recent birth year
    try:
        recent_birth_year = df['Birth Year'].max()
        print('The most recent birth year is ', recent_birth_year)
    except:
        print('Data unavailable.')
    
    # For most common birth year
    try:
        common_birth_year = df['Birth Year'].mode()
        print('The most common birth year is ', common_birth_year)
    except:
        print('Data unavailable.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data_rows(df):
    data_view = input('Do you want to see five rows of trip data? Enter Yes or No').title()
    begin_location = 0
    while(data_view == 'Yes'):
        print(df.iloc[begin_location:begin_location+5])
        begin_location +=5
        data_view = input('Would you like to continue?').title()
       
       
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data_rows(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()