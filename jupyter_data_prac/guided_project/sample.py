# In this project, you'll be working with Jupyter notebook, and analyzing data on gun deaths in the US. By the end, you'll have a notebook that you can add to your portfolio or build on top of on your own. If you need help at any point, you can consult our solution notebook here.

# https://github.com/dataquestio/solutions/blob/master/Mission218Solution.ipynb

# The dataset came from FiveThirtyEight, and can be found here. 
# https://github.com/fivethirtyeight/guns-data
#  

# The dataset is stored in the guns.csv file. It contains information on gun deaths in the US from 2012 to 2014. Each row in the dataset represents a single fatality. The columns contain demographic and other information about the victim. Here are the first few rows of the dataset:

# year	month	intent	police	sex	age	race	hispanic	place	education
# 1	2012	1	Suicide	0	M	34.0	Asian/Pacific Islander	100	Home	4.0
# 2	2012	1	Suicide	0	F	21.0	White	100	Street	3.0
# 3	2012	1	Suicide	0	M	60.0	White	100	Other specified	4.0
# 4	2012	2	Suicide	0	M	64.0	White	100	Home	4.0
# 5	2012	2	Suicide	0	M	31.0	White	100	Other specified	2.0
# As you can see above, the first row of the data is a header row, which tells you what kind of data is in each column of the CSV file. Each row contains information about the fatality, and the victim. Here's an explanation of each column:

# -- this is an identifier column, which contains the row number. It's common in CSV files to include a unique identifier for each row, but we can ignore it in this analysis.
# year -- the year in which the fatality occurred.
# month -- the month in which the fatality occurred.
# intent -- the intent of the perpetrator of the crime. This can be Suicide, Accidental, NA, Homicide, or Undetermined.
# police -- whether a police officer was involved with the shooting. Either 0 (false) or 1 (true).
# sex -- the gender of the victim. Either M or F.
# age -- the age of the victim.
# race -- the race of the victim. Either Asian/Pacific Islander, Native American/Native Alaskan, Black, Hispanic, or White.
# hispanic -- a code indicating the Hispanic origin of the victim.
# place -- where the shooting occurred. Has several categories, which you're encouraged to explore on your own.
# education -- educational status of the victim. Can be one of the following:
# 1 -- Less than High School
# 2 -- Graduated from High School or equivalent
# 3 -- Some College
# 4 -- At least graduated from College
# 5 -- Not available
# In this project, we'll explore the dataset, and try to find patterns in the demographics of the victims. Our first step is to read the data in and take a look at it.

# Instructions

# Read the dataset in as a list using the csv module.
# Import the csv module.
# Open the file using the open() function.
# Use the csv.reader() function to load the opened file.
# Call list() on the result to get a list of all the data in the file.
# Assign the result to the variable data.
# Display the first 5 rows of data to verify everything.