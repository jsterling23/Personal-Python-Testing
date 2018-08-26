# As we learn NumPy, we'll be analyzing taxi trip data released by the city of New York. The city releases data on taxis and for-hire vehicles on the Taxi and Limousine Commission (TLC) Website. There is data on over 1.3 trillion individual trips, reaching back as far as 2009 and is regularly updated.

# New York City Taxis

# We'll be working with a subset of this data: Yellow taxi trips to and from New York City airports between January and June 2016. In our dataset, each row represents a unique taxi trip. Below is information about selected columns from the data set:

# pickup_year - The year of the trip.
# pickup_month - The month of the trip (January is 1, December is 12).
# pickup_day - The day of the month of the trip.
# pickup_location_code - The airport or borough where the the trip started, as one of eight categories:
# 0 - Bronx.
# 1 - Brooklyn.
# 2 - JFK Airport.
# 3 - LaGuardia Airport.
# 4 - Manhattan.
# 5 - Newark Airport.
# 6 - Queens.
# 7 - Staten Island.
# dropoff_location_code - The airport or borough where the the trip finished, using the same eight category codes as pickup_location_code.
# trip_distance - The distance of the trip in miles.
# trip_length - The length of the trip in seconds.
# fare_amount - The base fare of the trip, in dollars.
# total_amount - The total amount charged to the passenger, including all fees, tolls and tips.
# You can find information on all columns in the dataset data dictionary.

# We have randomly sampled approximately 90,000 trips for our analysis, representing one 50th of the trips for the six month period. Our data is stored in a CSV file called nyc_taxis.csv. Here are the first 10 rows of the data set:

# pickup_year	pickup_month	pickup_day	pickup_dayofweek	pickup_time	pickup_location_code	dropoff_location_code	trip_distance	trip_length	fare_amount	fees_amount	tolls_amount	tip_amount	total_amount	payment_type
# 2016	1	1	5	0	2	4	21.00	2037	52.0	0.8	5.54	11.65	69.99	1
# 2016	1	1	5	0	2	1	16.29	1520	45.0	1.3	0.00	8.00	54.30	1
# 2016	1	1	5	0	2	6	12.70	1462	36.5	1.3	0.00	0.00	37.80	2
# 2016	1	1	5	0	2	6	8.70	1210	26.0	1.3	0.00	5.46	32.76	1
# 2016	1	1	5	0	2	6	5.56	759	17.5	1.3	0.00	0.00	18.80	2
# 2016	1	1	5	0	4	2	21.45	2004	52.0	0.8	0.00	52.80	105.60	1
# 2016	1	1	5	0	2	6	8.45	927	24.5	1.3	0.00	6.45	32.25	1
# 2016	1	1	5	0	2	6	7.30	731	21.5	1.3	0.00	0.00	22.80	2
# 2016	1	1	5	0	2	5	36.30	2562	109.5	0.8	11.08	10.00	131.38	1
# 2016	1	1	5	0	6	2	12.46	1351	36.0	1.3	0.00	0.00	37.30	2
# This, however, is how the first few lines of raw data in our CSV look like (we are showing only the first four columns from the file to make the format easier to understand:


# pickup_year,pickup_month,pickup_day,pickup_dayofweek
# 2016,1,1,5
# 2016,1,1,5
# 2016,1,1,5
# 2016,1,1,5
# To start working with this CSV data in NumPy, we'll first need to start by importing the NumPy library into our Python environment. For this, we use a simple import statement:


# import numpy as np
# We used the as syntax in our import statement. This allows us to access the NumPy library using another name. When working with NumPy, the convention is to import the library as np for brevity.

# Next, we'll use Python's built-in csv module to import our CSV as a 'list of lists'.

# The last step is to convert our list of lists into a NumPy n-dimensional array, or ndarray. We're going to explain ndarrays in more detail in the next screen, but for now you can think of it as NumPy's version of a list of lists format. To convert from the list type to ndarray, we use the numpy.array() constructor. Here's an example of how it works:


# # our list of lists is stored as data_list
# data_ndarray = np.array(data_list)
# We used the syntax np.array() instead of numpy.array() because of our import numpy as np code. When we introduce a new syntax, we'll always use the full name to describe it, and you'll need to substitute in the shorthand as appropriate.

# Let's convert our taxi CSV into a NumPy ndarray!

import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)
    


# start writing your code below this comment
taxi = np.array(converted_taxi_list)


# ******************************************************************************************************************************************



# Just like we saw in the previous screen, selections of rows ndarray's look like they behave very similarly to lists of lists. In reality, what we're seeing is a shortcut of sorts. For any two-dimensional array, the full syntax for selecting data is:


# ndarray[row,column]
# ​
# # or if you want to select all
# # columns for a given set of rows
# ndarray[row]
# Where row defines the location along the row axis and column defines the location along the column axis. Both row and column can be one of the following:

# An integer, indicating a specific location, eg ndarray[3,0].
# A slice, indicating a range of locations, eg ndarray[0:5,6:].
# A colon, indicating every location, eg ndarray[:,2].
# A list of values, indicating specific locations, eg ndarray[[0,1,3,4],0].
# A boolean array, indicating specific locations - we'll look at this method in detail in the second mission of this course.
# Or any combination of the above.
# This is how we select a single item from a 2D ndarray:

# ******************************************************************************************************************************************




# Let's continue by learning how to select one or more columns of data:

# Selecting columns from a 2D ndarray

# With a list of lists, we need to use a for loop to extract specific column(s) and append them back to a new list. With ndarray's, the process is much simpler. We again use single brackets with comma separated row and column locations, but we use a colon (:) for the row locations. This colon acts as a wildcard, and gives us all items in that dimension, or in other words all rows.

# If we wanted to select a partial 1D slice of a row or column, we can combine a single value for one dimension with a slice for the other dimension:

# Selecting partial 1D slices from a 2D ndarray

# Lastly, if we wanted to select a 2D slice, we can use slices for both dimensions:

# Selecting a 2D slice from a 2D ndarray

# Let's practice everything we've learned so far to perform some more complex selections using NumPy

# Instructions

# From the taxi ndarray:
# Select every row for the columns at indexes 1, 4, and 7 and assign them to columns_1_4_7.
# Select the columns at indexes 5 to 8 inclusive for the row at index 99 and assign them to row_99_columns_5_to_8.
# Select the rows at indexes 100 to 200 inclusive for the column at index 14 and assign them to rows_100_to_200_column_14.


# cols = [1,4,7]
# columns_1_4_7 = taxi[:,cols]

# row_99_columns_5_to_8 = taxi[99,5:9]

# rows_100_to_200_column_14 = taxi[100:201,14]

# ******************************************************************************************************************************************


# Earlier, we created trip_mph, a 1D ndarray of the average mile-per-hour speed of each trip in our dataset, based off the trip_length and trip_distance columns. We might like to explore this data further, for instance working out what the maximum and minimum values are for that ndarray.

# We could use the built-in Python functions min() and max() to make these calculations, however these will perform calculations without taking advantage of vectorization. Instead we can use NumPy's ndarray methods we can use to calculate statistics.

# To calculate the minimum value of an 1D ndarray, we use the vectorized ndarray.min() method, like so:


# >>> mph_min = trip_mph.min()
# ​
# >>> mph_min
# ​
#     0.0
# The minimum value in our trip_mph ndarray is 0.0, for a trip that didn't travel any distance at all.

# Before we look at other array methods Let's take a moment to clarify the difference between methods and functions. Functions act as stand alone segments of code that usually take an input, perform some processing, and return some output. When we're working with Python lists, we can use the len() function to calculate the length of a list, but if we're working with Python strings, we can also use len(). In this case, it calculates the numbers of characters (or length) of the string.


# >>> my_list = [21,14,91]
# ​
# >>> len(my_list)
# ​
#     3
# ​
# >>> my_string = 'Dataquest'
# ​
# >>> len(my_string)
# ​
#     9
# In contrast, methods are special functions that belong to a specific type of object. Python lists have a list.append() method that we can use to add an item to the end of a list. If we try to use that method on a string, we will get an error:


# >>> my_list.append(21)
# ​
# >>> my_string.append(' is the best!')'
# ​
#     Traceback (most recent call last):
#       File "stdin", line 1, in module
#     AttributeError: 'str' object has no attribute 'append'
# When you're learning NumPy, this can get confusing, because sometimes there are operations that are implemented as both methods and functions, but sometimes there are not. Let's look at some examples:

# Calculation	Function Representation	Method Representation
# Calculate the minimum value of trip_mph	np.min(trip_mph)	trip_mph.min()
# Calculate the maximum value of trip_mph	np.max(trip_mph)	trip_mph.max()
# Calculate the mean average value of trip_mph	np.mean(trip_mph)	trip_mph.mean()
# Calculate the median average value of trip_mph	np.median(trip_mph)	There is no ndarray median method
# To remember the right terminology, anything that starts with np (e.g. np.mean()) is a function and anything you express with an object (or variable) name first (eg trip_mph.mean()) is a method. As we discussed in the previous screen, where both exist it's up to you which you use, but it's much more common to see the method approach, and that's the one we'll use moving forward.

# Numpy ndarrays have methods for many different calculations. A few key methods are:

# ndarray.min() to calculate the minimum value
# ndarray.max() to calculate the maximum value
# ndarray.mean() to calculate the mean average value
# ndarray.sum() to calculate the sum of the values
# You can see them a full list of ndarray methods in the NumPy ndarray documentation.

# Let's use the methods we've just learned about to calculate the smallest, largest, and mean average speed from our trip_mph ndarray.

# Instructions

# Use the ndarray.max() method to calculate the maximum value of trip_mph and assign the result to mph_max.
# Use the ndarray.mean() method to calculate the average value of trip_mph and assign the result to mph_mean.


mph_min = trip_mph.min()
mph_max = trip_mph.max()
mph_mean = trip_mph.mean()
print('Min: {} | Max: {} | Average: {}'.format(mph_min,mph_max,mph_mean))

# ******************************************************************************************************************************************


# Earlier in the mission, we produced a ndarray trip_mph of the average speed of each trip. We also observed that the maximum speed was 82,000 mph, which is definitely not an accurate number. To take a closer look at why we might be getting this value, we're going to do the following:

# Add the trip_mph as a column to our taxi ndarray.
# Sort taxi by trip_mph.
# Look at the rows with the highest trip_mph from our sorted ndarray to see what they tell us about these large values.
# To start, let's learn how to add rows and columns to an ndarray. The technique we're going to use involves the numpy.concatenate() function. This function accepts:

# A list of ndarrays as the first, unnamed parameter.
# An integer for the axis parameter, where 0 will add rows and 1 will add columns.
# The numpy.concatenate() function requires that each array have the same shape, excepting the dimension corresponding to axis. Let's look at an example to understand more precisely how that works. We have two arrays, ones and zeros:


# >>> print(ones)
# ​
#     [[ 1  1  1]
#      [ 1  1  1]]
# ​
# >>> print(zeros)
# ​
#     [ 0  0  0]
# Let's try and use numpy.concatenate() to add zeros as a row. Because we are wanting to add a row, we use axis=0


# >>> combined = np.concatenate([ones,zeros],axis=0)
# ​
#     Traceback (most recent call last):
#       File "stdin", line 1, in module
#     ValueError: all the input arrays must have same number of dimensions
# We've got an error because our dimensions don't match - let's look at the shape of each array to see if we can understand why:


# >>> print(ones.shape)
# ​
#     (2, 3)
# ​
# >>> print(zeros.shape)
# ​
#     (3,)
# Because we're using axis=0, our shapes have to match across all dimensions except the first. If we look at these two array's we can see that the second dimension of ones is 3, but zeros doesn't have a second dimension, because it's only a 1D array. This is the source of our error. The table below shows the shapes we need to be able to combine these arrays.

# Object	Current shape	Desired Shape
# ones	(2, 3)	(2, 3)
# zeros	(3,)	(1, 3)
# In order to adjust the shape of zeros, we can use the numpy.expand_dims() function. You might like to follow these steps in the console. We'll start by passing axis=0 because we want to convert our 1D array into a 2D array representing a row:


# >>> zeros_2d = np.expand_dims(zeros,axis=0)
# ​
# >>> print(zeros_2d)
# ​
#     [[ 0  0  0]]
# ​
# >>> print(zeros_2d.shape)
# ​
#     (1, 3)
# Finally, we can use numpy.concatenate() to combine the two arrays:


# >>> combined = np.concatenate([ones,zeros_2d],axis=0)
# ​
# >>> print(combined)
# ​
#     [[ 1  1  1]
#      [ 1  1  1]
#      [ 0  0  0]]
# Adding a column is done the same way, except substituting axis=1 for axis=0 in both functions. The initial code for this screen shows this process.

# Instructions

# Expand the dimensions of trip_mph to be a single column in a 2D ndarray, and assign the result to trip_mph_2d.
# Add trip_mph_2d as a new column at the end of taxi, assigning the result back to taxi.
# Use the print() function to display taxi and view the new column.


trip_mph_2d = np.expand_dims(trip_mph,axis=1)
print('trip 2d',trip_mph_2d)
print()

taxi = np.concatenate([taxi,trip_mph_2d], axis=1)
print('taxi',taxi)


# ******************************************************************************************************************************************



# In this mission we learned:

# How vectorization it makes our code faster.
# About n-dimensional arrays, and NumPy's ndarrays.
# How to select specific items, rows, columns, 1D slices, and 2D slices from ndarrays.
# How to use vector math to apply simple calculations to entire ndarrays.
# How to use vectorized methods to perform calculations across either axis of ndarrays.
# How to add extra columns and rows to ndarrays.
# How to sort an ndarray.
# In the next mission, we'll continue to work with the NYC taxi data as we learn about boolean indexing, one of the most powerful tools when working with data in NumPy and pandas.





# Introduction to NumPy: Takeaways
# by Dataquest Labs, Inc. - All rights reserved © 2018
# Syntax
# SELECTING ROWS, COLUMNS, AND ITEMS FROM AN NDARRAY
# Convert a list of lists into a ndarray:

# import numpy as np
# f = open("nyc_taxis.csv", "r")
# taxi_list = list(csv.reader(f))
# taxi = np.array(converted_taxi_list)

# Selecting a row from an ndarray:

# second_row = taxi[1]

# Selecting multiple rows from an ndarray:

# all_but_first_row = taxi[1:]

# Selecting a specific item from an ndarray:

# fifth_row_second_column = taxi[4,1]

# SLICING VALUES FROM AN NDARRAY
# Selecting a single column:

# second_column = taxi[:,1]

# Selecting multiple columns:

# second_third_columns = taxi[:,1:3]
# cols = [1,3,5]
# second_fourth_sixth_columns = taxi[:, cols]

# Selecting a 2D slice:

# twod_slice = taxi[1:4, :3]

# VECTOR MATH
# vector_a + vector_b - Addition
# vector_a - vector_b - Subtraction
# vector_a * vector_b - Multiplication (this is unrelated to the vector multiplication used in linear algebra).
# vector_a / vector_b - Division
# vector_a % vector_b - Modulus (find the remainder when vector_a is divided by vector_b)
# vector_a ** vector_b - Exponent (raise vector_a to the power of vector_b)
# vector_a // vector_b - Floor Division (divide vector_a by vector_b, rounding down to the nearest integer)
# CALCULATING STATISTICS FOR 1D NDARRAYS
# ndarray.min() to calculate the minimum value
# ndarray.max() to calculate the maximum value
# ndarray.mean() to calculate the mean average value
# ndarray.sum() to calculate the sum of the values
# CALCULATING STATISTICS FOR 2D NDARRAYS
# Max value for an entire 2D Ndarray:

# taxi.max()

# Max value for each row in a 2D Ndarray (returns a 1D Ndarray):

# taxi.max(axis=1)

# Max value for each column in a 2D Ndarray (returns a 1D Ndarray):

# taxi.max(axis=0)

# ADDING ROWS AND COLUMNS TO NDARRAYS
# Joining a sequence of arrays:

# np.concatenate([a1, a2], axis=0)

# Expanding the shape of an array:

# np.expand_dims([1, 2], axis=0)

# SORTING
# Sorting a 1D Ndarray:

# np.argsort(taxi[0])

# Sorting a 2D NDarray by a specific column:

# sorted_order = np.argsort(taxi[:,15])
# taxi_sorted = taxi[sorted_order]

# Concepts
# Python is considered a high-level language because we don't have to manually allocate memory or specify how the CPU performs certain operations. A low-level language like C gives us this control and lets us improve specific code performance, but a tradeoff in programmer productivity is made. The NumPy library lets us write code in Python but take advantage of the performance that C offers. One way NumPy makes our code run quickly is vectorization, which takes advantage of Single Instruction Multiple Data (SIMD) to process data more quickly.
# A list in NumPy is called a 1D Ndarray and a list of lists is called a 2D Ndarray. NumPy ndarrays use indices along both rows and columns and is the primary way we select and slice values.
# Resources

https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.math.html#arithmetic-operations

https://docs.scipy.org/doc/numpy-1.14.0/reference/arrays.ndarray.html#calculation

