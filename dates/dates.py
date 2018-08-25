# There are a few modules in Python's Standard Library that deal with dates and times. One is the time module, which deals primarily with Unix timestamps.

# A Unix timestamp is a floating point value with no explicit mention of day, month, or year. This value represents the number of seconds that have passed since the "epoch", or the first second of the year 1970. So, a timestamp of 0.0 would represent the epoch, and a timestamp of 60.0 would represent one minute after the epoch. We can represent any date after 1970 this way.

# To retrieve the current Unix timestamp, we use the time.time() function.

# Instructions

# Return the current timestamp and assign it to current_time.
# Display current_time using the print() function.

import time

current_time = time.time()
print(current_time)

days = current_time / 86400
years = days / 365
print(years)


# ***************************************************************************************************************


# We can convert a timestamp to a more human-readable form using the time.gmtime() function. This function takes a timestamp as an argument, and returns an instance of the struct_time class. struct_time instances have attributes that represent the current time in other ways.

# Here are some of the attributes:

# tm_year: The year of the timestamp
# tm_mon: The month of the timestamp (1-12)
# tm_mday: The day in the month of the timestamp (1-31)
# tm_hour: The hour of the timestamp (0-23)
# tm_min: The minute of the timestamp (0-59)
# For example, we can retrieve the year value as an integer using the tm_year property:


# current_time = time.time()
# current_struct_time = time.gmtime(current_time)
# current_year = current_struct_time.tm_year
# current_time = time.time()
# current_struct_time = time.gmtime(current_time)
# current_year = current_struct_time.tm_year

current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour
print(current_hour)



# ***************************************************************************************************************


# Note the value for the hour from the last screen. The time module always results in a UTC time. UTC stands for Coordinated Universal Time. This is the accepted time standard within the programming community. It corresponds to the mean solar time at 0° longitude, or Greenwich Mean Time, except that it doesn't follow daylight saving time. While we can convert UTC to other time zones, we'll use UTC in this mission for simplicity.

# The datetime module offers better support for working extensively with dates. For example, it's easier to perform arithmetic on them (such as adding days), and to work with different time zones.

# The datetime module contains a class that's also named datetime that represents points in time. These datetime instances appear similar to struct_time instances.

# To represent a specific point in time, we pass in values into the constructor when creating an instance of the datetime class:


# current_time = time.time()
# current_struct_time = time.gmtime(current_time)
# current_year = current_struct_time.tm_year
# nye_2017 = datetime.datetime(year=2017, month=12, day=31, hour=12, minute=59, second=59)
# We can leave out specific details if we'd like:


# nye_day_2017 = datetime.datetime(year=2017, month=12, day=31)
# We can return the current utc time as a datetime instance using the datetime.utcnow() function.

# Once we have a datetime instance that represents a specific point in time, we can use the following attributes to return more specific properties:

# year: returns the year value as an integer.
# month: returns the month value an integer.
# day: returns the day value as an integer.
# hour: returns the hour value as an integer.
# minute: returns the minute value as an integer.
# second: returns the second value as an integer.
# microsecond: returns the microsecond value as an integer.
# You can read about these attributes in the documentation.

# Instructions

# Import the datetime module.
# Assign the datetime object representation of the current time to a new variable current_datetime.
# Assign the current year to current_year.
# Assign the current month to current_month.


# ***************************************************************************************************************


# We know how to represent dates, but we'd also like to perform arithmetic on them. Since adding a day, week, month, etc. to a date can be tedious to do from scratch, the datetime module provides the timedelta class. We can create an instance of this class that represents a span of time, then add or subtract it from instances of the datetime class.

# When we create instances of the timedelta class, we can specify the following parameters:

# weeks
# days
# hours
# minutes
# seconds
# milliseconds
# microseconds
# Suppose we want to calculate the date for three weeks and two days from now. We would first create an instance of the datetime class that represents today:


# today = datetime.datetime.now()
# Then, we could get an instance of the timedelta class that represents the span of time we're working with:


# diff = datetime.timedelta(weeks = 3, days = 2)
# Finally, we would add these two instances:


# future = today + diff
# We can also subtract a timedelta instance from a datetime instance.


# past = today - diff
# Instructions

# Create an instance of the datetime class that represents the day March 22, 2233. Assign this to a new variable kirks_birthday.
# Create an instance of the timedelta class representing 15 weeks and assign to diff.
# Find the date 15 weeks prior to March 22, 2233 and assign the resulting datetime instance to before_kirk.


import datetime

kirks_birthday = datetime.datetime(year=2233, month=3,day=22)
diff = datetime.timedelta(weeks=15)
before_kirk = kirks_birthday - diff
print(before_kirk)

# ***************************************************************************************************************

# Suppose we'd like to output dates in human-readable formats. If we use the print() function to display a datetime object, the output will look something like 2016-01-06 13:51:25.849719. Instead of displaying the full timestamp down to the microsecond, we can use the datetime.strftime() method to specify how we'd like the string output to be formatted.

# The datetime.datetime.strftime() method takes a format string as its input. A format string contains special indicators, usually preceded by percent characters ("%"), that indicate where certain values should go. For example, suppose we stored a timestamp from March 3, 2010 in the object march3. If we want to format it nicely into the string "Mar 03, 2010", we can write the following code:


# march3 = datetime.datetime(year = 2010, month = 3, day = 3)
# pretty_march3 = march3.strftime("%b %d, %Y")
# print(pretty_march3)
# The format string argument in strftime() indicates that we want:

# the abbreviated month name ("%b") followed by a space
# the day of the month ("%d") followed by a comma and space
# the full year ("%Y").
# Thankfully, we don't have to memorize the string arguments and can refer to the documentation for the strftime() method, which provides a useful summary table of the different options.

# Instructions

# Using the datetime.datetime.strftime() method, display mystery_date, a datetime instance we've created for you, in the following format:

# [12-hour time][AM/PM] on [Day of week] [Month full name] [Day of month], [Full year]
# Here's an example in that format:

# "11:00AM on Wednesday March 03, 2010"
# Store this string in the new variable mystery_date_formatted_string and display using the print() function.


# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# Using the datetime.datetime.strftime() method, display mystery_date, a datetime instance we've created for you, in the following format:

# [12-hour time][AM/PM] on [Day of week] [Month full name] [Day of month], [Full year]
# Here's an example in that format:

# "11:00AM on Wednesday March 03, 2010"
# Store this string in the new variable mystery_date_formatted_string and display using the print() function.

import datetime

time_format = "%I:%M%p on %A %B %d, %Y"

mystery_date_formatted_string = mystery_date.strftime(time_format)
print(mystery_date_formatted_string)


# ***************************************************************************************************************

# Just as we can convert a datetime object into a formatted string, we can also do the reverse. The datetime.datetime.strptime() function allows us to convert a string to a datetime instance:

# The date string (e.g. "Mar 03, 2010")
# The format string (e.g. "%b %d, %Y")
# With just these two arguments, strptime() will return a datetime instance for March 3, 2010:


# march3 = datetime.datetime.strptime("Mar 03, 2010", "%b %d, %Y")
# This is useful if we have a date in a string format, and need to convert it to a datetime instance. If we inspect the data and determine the format of every date, we can save ourselves a lot of manual string manipulation by using the datetime.datetime.strptime() function instead. We could even use datetime.strptime() and datetime.strftime() together to convert a date string to a datetime object, and then convert it to a date string of a different format.

# Instructions

# Use the datetime.datetime.strptime() function to return a datetime instance that represents the timestamp associated with the string mystery_date_formatted_string:
# mystery_date_formatted_string has the format: [Time][AM/PM] on [Day of week] [Month full name] [Day of month], [Full year].
# March 3, 2010 at 11:00AM would look like "11:00AM on Wednesday March 03, 2010" in this format.
# Assign the resulting datetime instance in mystery_date_2 and display it using the print() function.


import datetime

print(mystery_date_formatted_string)

time_format = "%I:%M%p on %A %B %d, %Y"
mystery_date_2 = datetime.datetime.strptime(mystery_date_formatted_string,time_format)
print(mystery_date_2)



# ***************************************************************************************************************


# Reddit is a content and community website where users can submit links, text posts, and other types of content to groups of people with similar interests. These groups are called subreddits, and each one specializes in a particular topic. One popular subreddit, AskReddit, is a place where users pose questions to the entire Reddit population. Other users answer those questions in the comments section.

# We'll be working with a data set of the top 1,000 posts on AskReddit from 2015. Reddit user P_S_Laplace created the data set, which contains the following columns:

# Title: The title of the post
# Score: The number of upvotes the post received
# Time: When the post appeared (timestamp)
# Gold: How much Reddit Gold users gave the post
# NumComs: The number of comments the post received

# ***************************************************************************************************************

# In the following code cell, we've read the AskReddit data into the posts variable for you as a list of lists. Each nested list represents an AskReddit post. Here's what the first few rows of the data set looks like:

# Title	Score	Time	Gold	NumComs
# "What's your internet ""white whale"", something you've been searching for years to find with no luck?"	11510	1433213314.0	1	26195
# What's your favorite video that is 10 seconds or less?	8656	1434205517	4	8479
# What are some interesting tests you can take to find out about yourself?	8480	1443409636.0	1	4055
# Here's what the first three lists in posts looks like:


# posts = [
#             ['What\'s your internet "white whale", something you\'ve been searching for years to find with no luck?', '11510', '1433213314.0', '1', '26195'],
#             ["What's your favorite video that is 10 seconds or less?", '8656', '1434205517.0', '4', '8479'],
#             ['What are some interesting tests you can take to find out about yourself?', '8480', '1443409636.0', '1', '4055'],
#             ...
#         ]
# The values in the Time column are formatted as Unix timestamps, not human-readable strings. We can convert each Unix time stamp into datetime object using the datetime.datetime.fromtimestamp() function:


# datetime_object = datetime.datetime.fromtimestamp(1433213314.0)
# We'll convert the Unix timestamp for each row to a datetime object using datetime.datetime.fromtimestamp() and store the result back in the row, replacing the Unix timestamp.

# Instructions

# Loop through posts, and for each row:

# Convert the value in the Time column (index 2 of each row) to a floating point number.
# Convert the floating point number to a datetime instance using datetime.datetime.fromtimestamp().
# Store the resulting datetime instance back in index 2 of the row, overwriting the original Unix timestamp value.


import datetime

for row in posts[0:10]:
    unix_time = float(row[2])
    print(unix_time)
    new_time = datetime.datetime.fromtimestamp(unix_time)
    row[2] = new_time
   
print(posts[0:10])


# ***************************************************************************************************************


# Now that we've converted our posts data set to contain datetime instances, we can count how many of the top 1,000 posts users submitted in the month of March.

# Instructions

# Loop through posts, and for each row:
# Use the datetime.month attribute to check if the datetime instance at index 2 equals 3.
# If so, increment march_count.


march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1

# ***************************************************************************************************************


# Let's write a function that generalizes our counting logic and makes it works for any month.

# Instructions

# Write a function that takes in an integer value representing a month, and returns the number of posts users submitted during that month.

# Use the function to return the number of posts users submitted in February (month value of 2), and assign the count to a new variable feb_count.

# Use the function to return the number of posts users submitted in August (month value of 8), and assign the count to a new variable aug_count.


  
def month_post_count(num):
    count = 0
    if num > 12:
        print("Use a valid month")
        return
    for row in posts:
        if row[2].month == num:
            count += 1
    return count

            
feb_count = month_post_count(2)
aug_count = month_post_count(8)
jun_count = month_post_count(6)


# ***************************************************************************************************************

# Dates in Python: Takeaways
# by Dataquest Labs, Inc. - All rights reserved © 2018
# Syntax
# CONVERTING TIMESTAMPS
# Here are the attributes of the struct_time instance:

# tm_year: The year of the timestamp
# tm_mon: The month of the timestamp (1-12)
# tm_mday: The day in the month of the timestamp (1-31)
# tm_hour: The hour of the timestamp (0-23)
# tm_min: The minute of the timestamp (0-59)
# current_time = time.time()
# current_struct_time = time.gmtime(current_time)
# current_hour = current_struct_time.tm_hour

# DATETIME CLASS
# Here are the attributes for the datetime instance:

# year: returns the year value as an integer.
# month: returns the month value an integer.
# day: returns the day value as an integer.
# hour: returns the hour value as an integer.
# minute: returns the minute value as an integer.
# second: returns the second value as an integer.
# microsecond: returns the microsecond value as an integer.
# current_datetime = datetime.datetime.utcnow()
# current_year = current_datetime.year
# current_month = current_datetime.month

# To use timedelta within datetime:

# diff = datetime.timedelta(weeks = 3, days = 2)
# future = today + diff

# Here are all the parameters for timedelta:

# weeks
# days
# hours
# minutes
# seconds
# milliseconds
# microseconds
# To format the dates, we'll use % character to indicate where values should go:

# march3 = datetime.datetime(year = 2010, month = 3, day = 3)
# pretty_march3 = march3.strftime("%b %d, %Y")
# print(pretty_march3)

# Concepts
# A Unix timestamp is a floating point value with no explicit mention of day, month, or year. This value represents the number of seconds that have passed since the "epoch", or the first second of the year 1970.
# UTC stands for Coordinated Universal Time. This is the accepted time standard within the programming community.
# Resources

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# https://docs.python.org/3/library/datetime.html
# https://docs.python.org/3/library/time.html#time.time
# https://docs.python.org/3/library/time.html
# https://docs.python.org/3/library/
