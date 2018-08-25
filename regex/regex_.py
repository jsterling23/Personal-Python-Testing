# Data scientists often need to parse strings to extract important information. Suppose we have manually-entered data that includes dates, and need to extract the years from those dates. The dates may look something like this:


# - "Jan 17, 2012"
# - "9/22/2005"
# - "Spring 2007"
# - "New Year's Eve 1999"
# All of these strings contain the information we need, but in very different formats. If we try to split the strings, what character would we split them on? In the resulting lists, which element would contain the year? We can handle a problem like this with regular expressions.

# A regular expression (regex) is a sequence of characters that describes a search pattern. We can use regular expressions to search for and extract data.

# In practice, we say that strings match a regular expression if the pattern exists anywhere within those strings (as substrings). The simplest example of a regular expression is an ordinary sequence of characters that we specify. We say that any string containing that sequence of characters, adjacent and in the same exact order, matches the regular expression. Here are a few examples:

# visit site for diagram:
# https://www.dataquest.io/m/82/regular-expressions

# This is the simplest form of a regex. We'll soon see that regular expressions can also contain special characters that denote particular patterns.


# *******************************************************************************************************



# We've seen that we can use regular expressions to find strings containing a simple pattern, but they can match much more complex patterns.

# There are a number of special characters we can use with regular expressions to change the way a pattern is interpreted. In Python, we use the re module to work with regular expressions. The module's documentation provides a list of these special characters.

# For instance, we use the special character "." to indicate that any character can be put in its place. Here are a few examples of how you might use this placeholder:

# visit site for diagram:
# https://www.dataquest.io/m/82/regular-expressions/2/wildcards-in-regular-expressions


# *******************************************************************************************************




# Let's use the csv module to read and print our data file, "askreddit_2015.csv". Recall that we can use the csv module by performing the following steps:

# Import csv.
# Open the file that contains our CSV data in 'r' mode.
# Call the csv.reader() function with the file object as input.
# Convert the result to a list.
# Instructions

# Use the csv module to read our data set and assign it to posts_with_header.
# Use list slicing to exclude the first row, which represents the column names. Assign this sliced data set to posts.
# Use a for loop and string slicing to print the first 10 rows. See if you notice any patterns in this sample of the data set.



# assuming you have a dataset that matches. Couldn't find the exact one worked with here. Dude deleted his account.

import csv

with open('askreddit_2015.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    posts_with_header = list(data)
    posts = posts_with_header[1:]
    for post in posts[:10]:
        print(post)
    


# *******************************************************************************************************




# We mentioned the re module earlier, and now we'll begin to use it in our code. One useful function the module provides is re.search.

# With re.search(regex, string), we can check whether string is a match for regex. If it is, the expression will return a match object. If it isn't, it will return None. For now, we won't worry about returning the actual matches - we'll just compare the result to None to see whether we have a match or not.


# if re.search("needle", "haystack") is not None:
#     print("We found it!")
# else:
#     print("Not a match")
# The code above will print Not a match, because "haystack" is not a match for the regex "needle".

# You may have noticed that many of the posts in our AskReddit database are directed towards particular groups of people, using phrases like "Soldiers of Reddit". These types of posts are common, and always follow a similar format. We can use regular expressions to count how many of them are in the top 1,000.

# Let's do this in our next exercise. We've already read the data set into the variable posts.

# Instructions

# Count the number of posts in our data set that match the regex "of Reddit". Assign the count to of_reddit_count.


# ---------WHAT I ORIGINALLY WROTE-------------
import re

of_reddit_count = 0

for post in posts:
    if re.search("of Reddit", str(post)):
        of_reddit_count += 1

Note: works but the "solution" was different and I think I know why it is better. It only checks relevant data instead of the entire post data.

# -------------------Solution------------------
import re

of_reddit_count_old = 0
for row in posts:
    if re.search("of Reddit", row[0]) is not None:
        of_reddit_count_old += 1



# *******************************************************************************************************


# If you look at the data set closely, you may notice that some posts use "of Reddit", and others use "of reddit". While both versions have the same format, the capitalization of "Reddit" is different. We can account for this inconsistency with square brackets. We use square brackets in a regex to indicate that any character within them can fill the space.

# For example, the regex "[bcr]at" would match the substrings "bat", "cat", and "rat", but nothing else. We indicate that the first character in the regex can be either "b", "c" or "r".

# Instructions

# Use square bracket notation to make the code account for both capitalizations of "Reddit", and count how many posts contain "of Reddit" or "of reddit" in the title.

# Assign the resulting count to of_reddit_count.


import re

of_reddit_count_old = 0
for row in posts:
    if re.search("of Reddit", row[0]) is not None:
        of_reddit_count_old += 1


of_reddit_count = 0
for row in posts:
    if re.search("of [Rr]eddit", row[0]) is not None:
        of_reddit_count += 1
        



# *******************************************************************************************************



# Our data set contains a lot of posts that use the [Serious] tag. AskReddit members use this tag to indicate that they're not looking for humorous responses, and that their question should be taken seriously. We'd like to search through our data set to see how many posts have this tag, but the regex "[Serious]" doesn't do what we need. Since square brackets serve a special function within regular expressions, "[Serious]" will match any string that contains "S", "e", "r", etc.

# To deal with this sort of problem, we need to escape special characters. In regular expressions, escaping a character means indicating that you don't want the character to do anything special, and that the interpreter should treat it just like any other character. We use the backslash ("\") to escape characters in a regex.

# Suppose we wanted to match all of the strings that end with a period. If we used ".$", it would match all strings that contain any character, because "." has that special meaning. Instead, we need to escape the "." with a backslash, so our regex becomes "\.$".

# Instructions

# Escape the square bracket characters to count the number of posts in our data set that contain the "[Serious]" tag.

# Assign the count to serious_count.



# *******************************************************************************************************

# Some people tag serious posts as "[Serious]", and others as "[serious]". We should account for both capitalizations.

# Instructions

# Refine the code to count how many posts have either "[Serious]" or "[serious]" in the title.
# Assign the count to serious_count.


import re

serious_count_old = 0
for row in posts:
    if re.search("\[Serious\]", row[0]) is not None:
        serious_count_old += 1
        
serious_count = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count += 1



    
# *******************************************************************************************************


# On the previous screen, you saw that we can use square brackets as both special notation and escaped characters, all in the same regex. We'll be using more brackets to refine our search.

# In our data set, some users have tagged their posts with "(Serious)" or "(serious)", including the parentheses. Therefore, we should account for both square brackets and parentheses. We can do this by using square bracket notation, and escaping the "[", "]", "(", and ")" characters with the backslash.

# Instructions

# Refine the code so that it counts how many posts have the serious tag enclosed in either square brackets or parentheses.
# Assign the count to serious_count.



# --------------me--------------------
import re

serious_count_old = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count_old += 1
        
serious_count = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count += 1
    elif re.search("\([Ss]erious\)", row[0]) is not None:
        serious_count += 1


# ----------solution---------------------
# >> I did try something like this but I didn't get the escaped chars right. Looking this over it makes sense. Cool. I like regex.

serious_count = 0
for row in posts:
    if re.search("[\[\(][Ss]erious[\)\]]", row[0]) is not None:
        serious_count += 1


# *******************************************************************************************************



# We should consider a post serious only if the tag occurs at the beginning or end of the title. To match titles with the tag at the beginning, we can use the "^" character in a regex. To match titles with the tag at the end, we can use "$". These characters produce two different regular expressions, and we'd like to identify all titles that match either of them.

# To combine regular expressions, we use the "|" character. For example, "cat|dog" would match "catfish" and "hotdog", because both of these strings match either "cat" or "dog". Similarly, we can combine our regular expressions for the serious tags with the "|" operator to match all titles that either begin or end with the tag.

# Instructions

# Use the "^" character to count how many posts include the serious tag at the beginning of the title. Assign this count to serious_start_count.

# Use the "$" character to count how many posts include the serious tag at the end of the title. Assign this count to serious_end_count.

# Use the "|" character to count how many posts include the serious tag at either the beginning or end of the title. Assign this count to serious_count_final.



# ----------This is how they did it....----------------
import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0
for row in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_start_count += 1
    if re.search("[\[\(][Ss]erious[\]\)]$", row[0]) is not None:
        serious_end_count += 1
    if re.search("^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$", row[0]) is not None:
        serious_count_final += 1

# ------------I like mine a LOT better----------------------
# ------------Am I thinking like a python dev??-------------
# ------------I don't know, but it is cleaner---------------

import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0

regex_start = "^[\[\(][Ss]erious[\)\]]"
regex_end = "[\[\(][Ss]erious[\)\]]$"
both_regex = "{}|{}".format(regex_start, regex_end)

for row in posts:
    if re.search(regex_start, row[0]) is not None:
        serious_start_count += 1
    if re.search(regex_end, row[0]) is not None:
        serious_end_count += 1
    if re.search(both_regex, row[0]) is not None:
        serious_count_final += 1


# *******************************************************************************************************


# We've looked at one way we can account for inconsistencies in data; now let's examine another approach. The re module provides a sub() function that takes the following parameters (in order):

# pattern: The regex to match
# repl: The string that should replace the substring matches
# string: The string containing the pattern we want to search
# If we were to call re.sub("yo", "hello", "yo world") and assign it to a variable:

# if a match is found, the function will replace the "yo" in "yo world" with "hello" and return the result "hello world".
# if a match isn't found, the function simply returns the original string.
# Let's use re.sub() to convert all serious tags to the format "[Serious]".

# Instructions

# Replace "[serious]", "(Serious)", and "(serious)" with "[Serious]" for all of the titles in posts.
# You should only need to use one call to sub(), and one regex.
# Recall that the repl argument is an ordinary string. It's not a regex, so you don't need to escape characters like "[".


# ---------I didnt get it right away... But here it is----------------
import re

regex = "[\[\(][Ss]erious[\)\]]"

for row in posts:
    row[0] = re.sub(regex, '[Serious]', row[0])
        


# *******************************************************************************************************


# Let's return to the example from the beginning of our mission. Suppose we need to extract years from strings. An intuitive way to do this would be to match any string that contains four consecutive integers. We can indicate that we're looking for integers in a pattern by using square brackets ("[" and "]"), along with a dash ("-"). For example, "[0-9]" will match any character that falls between 0 and 9 (all of which will be one-digit integers). Similarly, "[a-z]" would match any lowercase letter. We can also specify smaller ranges like "[3-5]" or "[d-g]".

# Since we want to match four consecutive integers, our regex could be "[0-9][0-9][0-9][0-9]". This would work, but let's also add the condition that we only want to match years after year 999 and before year 3000 (any other four-digit numbers in a string are probably not years).

# Instructions

# We've loaded a number of strings into the strings variable for you.
# Loop through strings and use re.search() to determine whether each string contains a year between 1000 and 2999.
# Store every string that contains a year in year_strings. The .append() function will help here.


# -----------What I wrote -----------------
import re

year_strings = []
regex = "[1-2][0-9][0-9][0-9]"

for row in strings:
    if re.search(regex, row):
        year_strings.append(row)
    else:
        print('No bueno')


# *******************************************************************************************************


# On the previous screen, we used the regex "[1-2][0-9][0-9][0-9]", which looks a bit repetitive. Luckily, there's a better way to do it!

# We can use curly brackets ("{" and "}") to indicate that a pattern should repeat. To match any four-digit number, for example, we could repeat the pattern "[0-9]" four times by writing "[0-9]{4}".

# Instructions

# We've loaded a number of strings into the strings variable for you.
# Loop through strings and use re.search() to determine whether each string contains a year between 1000 and 2999. Use a regex that takes advantage of curly brackets.
# Store every string that contains a year in year_strings. The .append() function will help here.


# that was easy..........
import re

year_strings = []
regex = "[1-2][0-9]{3}"

for row in strings:
    if re.search(regex, row):
        year_strings.append(row)



# *******************************************************************************************************


# Finally, let's extract years from a string. The re module contains a findall() function that returns a list of substrings matching the regex. re.findall("[a-z]", "abc123") would return ["a", "b", "c"], because those are the substrings that match the regex.

# Instructions

# Use re.findall() to generate a list of all years between 1000 and 2999 in the string years_string.

# Assign the result to years.

import re
years = re.findall("[1-2][0-9]{3}", years_string)


*******************************************************************************************************


# Regular Expressions: Takeaways
# by Dataquest Labs, Inc. - All rights reserved © 2018
# Syntax
# To start using regex, use the re module.
# WILDCARDS
# To indicate that any character can be put in its place:

# strings = ["bat", "robotics", "megabyte"]
# regex = "b.t"

# BEGINNINGS AND ENDINGS OF STRINGS
# To match all strings that start with "a", use "^a" .
# To match all strings that end with "a", use "a$".
# COUNTING MATCHES WITHIN THE DATASET
# To check whether "needle" is a match for "haystack".

# Input:
# if re.search("needle", "haystack") is not None:
#     print("We found it!")
# else:
#     print("Not a match")

# Output:
# Not a match

# MATCHING MULTIPLE CHARACTERS
# To match multiple characters, specify the characters between "[ ]":

# `"[bcr]at"`

# This expression would match "bat", "cat", and "rat".

# ESCAPING SPECIAL CHARACTERS
# To escape a character use "\":

# for row in posts:
#     if re.search("\[Serious\]", row[0]) is not None:
#         serious_count += 1

# COMBINING REGEX CHARACTERS
# Checking if our code has either "[Serious]" or "[serious]":

# serious_count = 0
# for row in posts:
#     if re.search("\[[Ss]erious\]", row[0]) is not None:
#         serious_count += 1

# To match either one character or another, use "|":

# ADDITIONAL REGEX
# To substitute strings, use sub():

# re.sub("yo", "hello", "yo world")

# To match years, use:

# "[1-2][0-9][0-9][0-9]"

# To repeat characters, use "{ }". To repeat the pattern "[0-9]" four times:

# `"[0-9]{4}"`

# Concepts
# A regular expression (regex) is a sequence of characters that describes a search pattern. We can use regular expressions to search for and extract data.

# In regular expressions, escaping a character means indicating that you don't want the character to do anything special

# The re module provides a sub() function that takes the following parameters (in order):
# pattern: The regex to match
# repl: The string that should replace the substring matches
# string: The string containing the pattern we want to search
# Resources

# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/library/re.html#re.search

