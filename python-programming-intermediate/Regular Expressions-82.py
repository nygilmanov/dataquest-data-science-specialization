## 1. Introduction ##

strings = ["data science", "big data", "metadata"]
regex = "data"

## 2. Wildcards in Regular Expressions ##

strings = ["bat", "robotics", "megabyte"]
regex = "b.t"

## 3. Searching the Beginnings And Endings Of Strings ##

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"

## 5. Reading and Printing the Data Set ##

import csv
f=open("askreddit_2015.csv","r")
csvreader=csv.reader(f)
posts_with_header=list(csvreader)
posts=posts_with_header[1:]

for item in posts:
    print(item)


## 6. Counting Simple Matches in the Data Set with re() ##

import re

of_reddit_count = 0

for item in posts:
    if re.search("of Reddit", item[0]) is not None:
        of_reddit_count=of_reddit_count+1
        
    
    



## 7. Using Square Brackets to Match Multiple Characters ##

import re

of_reddit_count_old = 0
for row in posts:
    if re.search("of Reddit", row[0]) is not None:
        of_reddit_count_old += 1
print(of_reddit_count_old)
        
of_reddit_count = 0
for row in posts:
    if re.search("of [Rr]eddit", row[0]) is not None:
        of_reddit_count += 1
        
print(of_reddit_count)

## 8. Escaping Special Characters ##

import re

serious_count = 0

for item in posts:
    if re.search("\[Serious\]",item[0]) is not None:
        serious_count=serious_count+1

print(serious_count)       


## 9. Combining Escaped Characters and Multiple Matches ##

import re

serious_count_old = 0
for row in posts:
    if re.search("\[Serious\]", row[0]) is not None:
        serious_count_old += 1
print(serious_count_old)
        
serious_count = 0

for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count += 1
print(serious_count)
        

## 10. Adding More Complexity to Your Regular Expression ##

import re

serious_count_old = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count_old += 1
        
        
print(serious_count_old)
        
serious_count = 0
for row in posts:
    if re.search("[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_count += 1
        
print(serious_count)
        
        
        

## 11. Combining Multiple Regular Expressions ##

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



## 12. Using Regular Expressions to Substitute Strings ##

import re

for row in posts:
    row[0]=re.sub("[\[\(][Ss]erious[\]\)]","[Serious]",row[0]) 
        



## 13. Matching Years with Regular Expressions ##

import re

year_strings = []

for string in strings:
    if re.search("[1-2][0-9][0-9][0-9]",string) is not None:
        year_strings.append(string)
        

## 14. Repeating Characters in Regular Expressions ##

import re

year_strings = []

for string in strings:
    if re.search("[1-2][0-9]{3}",string) is not None:
        year_strings.append(string)
        
print(year_strings)   
        

## 15. Challenge: Extracting all Years ##

import re

years=re.findall("[1-2][0-9]{3}",years_string) 

years


