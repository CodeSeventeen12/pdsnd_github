import time
import pandas as pd
CITY_DATA = { 'chicago': pd.read_csv('chicago.csv'),
              'new york city': pd.read_csv('new_york_city.csv'),
              'washington': pd.read_csv('washington.csv')
              }
########################## FUNCTION 1 ###########################
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try :
            city = input('Which city would you like to explore? Chicago, New York City, or Washington? \n').lower()
            if city in list(CITY_DATA.keys()):
                print('\nYou are exploring {} .......... '.format(city))
                break
            else:
                print('\nPlease enter a valid city name .\nConsider typing one of these chicago,new york city or washington.')
        except Exception as e:
            print('Exception occurred {}'.format(e))
            print('\nPlease enter a valid city name .\nConsider typing one of these chicago,new york city or washington.\n')

    # get user input for month (all, january, february, ... , june)
    while True:
        try :
            month = input("\nPlease enter a month from ['january', 'february', 'march', 'april', 'may', 'june'] or all. \n").lower()
            if month in ['january', 'february', 'march', 'april', 'may', 'june','all']:
                print('\nData will be filtered by {} ............'.format(month))
                break
            else:
                print("\nPlease enter a valid month.\nConsider one of the following  ['january', 'february', 'march', 'april', 'may', 'june'] or all.")
        except Exception as e :
            print('{} occurred.'.format(e))
            print("\nPlease enter a valid month.\nConsider one of the following  ['january', 'february', 'march', 'april', 'may', 'june'] or all.\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try :
            day = input('\nPlease Enter the day you would like to see data for [Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday] or all. \n').lower()
            if day in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
                print("\nData is being filtered for {} .".format(day))
                break
            else:
                print("\nPlease enter a valid day.\nConsider one of the following [Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday] or all.\n")
        except Exception as e :
            print('{} occurred.'.format(e))
            print("\nPlease enter a valid day.\nConsider one of the following [Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday] or all.\n")


    print('-'*40)
    return city, month, day

######################## FUNCTION 2 #############################

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
    df = pd.DataFrame(CITY_DATA.get(city))
    # Converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracting month and day of week from Start Time column to create new columns
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

######################## FUNCTION 3 ##########################

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time() # For displaying time taken

    # display the most common month
    common_month = df['month'].mode()
    print('Most popular month : ',common_month)
    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()
    print('Most popular day of week : ',common_day_of_week)
    # display the most common start hour
    # creating an hour column
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()
    print('Most popular hour : ',common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

######################### FUNCTION 4 #########################

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print('Most popular Start Station : ',popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print('Most popular End Station : ',popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Start_And_End_Station'] = df['Start Station'] + ' , ' + df['End Station']
    popular_start_and_end_station = df['Start_And_End_Station'].mode()
    print('Most Frequent trips are between : ',popular_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

########################### FUNCTION 5 #############################

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time in seconds : ',df['Trip Duration'].sum())
    print('Total travel time in minutes : ',int(df['Trip Duration'].sum()/60))

    # display mean travel time
    print('Average travel time in seconds : ',df['Trip Duration'].mean())
    print('Average travel time in minutes : ', int(df['Trip Duration'].mean()/60))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

############################ FUNCTION 6 ################################

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Types : \n')
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:
        print('\nGender information : ')
        print('\n',df['Gender'].value_counts())
    else:
        print(" \nGender information not available. ")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nBirth date information : ')
        print('\nEarliest year of birth : ',df['Birth Year'].min())
        print('Most recent year of birth : ',df['Birth Year'].max())
        print('Common year of birth : ',df['Birth Year'].mode())
        from datetime import date
        today = date.today()
        # creating an age column
        df['age'] = today.year - df['Birth Year']
        print('Most Common age of bike users : ',df['age'].mode())

    else:
        print("\nBirth Year information not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

############################### FUNCTION 7 ############################

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        print('Data for 5 bike users  .')
        for a in range(5):
            print('\n')
            print(df.iloc[a])

        # Displaying data for 5 more users
        b = 5
        c = 10
        while True:
                word = input("\nPlease enter 'Y' if you would like to see data of 5 more bike users else N: \n ").lower()
                if word == "y":
                    for a in range(b, c):
                        print('\n')
                        print(df.iloc[a])
                    b = c
                    c = c + 5

                elif word == "n":
                    print("Finished.")
                    break

                else :
                    print('Please enter y or n .')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
