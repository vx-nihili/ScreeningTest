# Screening Test for Research: Autograding/Seat Assignment
This is the repository for the screening test, specifically for the project of Autograding and Seat Assignment projects.

## Overview
This particular program takes two arguments from the terminal, a command and a csv file, and prints the names (FirstName LastName) that fit the requested data. The possible commands are as follows:

|      **Command**                                         |               **Description**             |
| -------------------------------------------------------- | ----------------------------------------- |
| `"-name <pattern>"`  | This command finds any student names that contains the pattern and prints the<br> students' full names. This is case insensitive and looks at both the first and last names. |
| `"-email <pattern>"` | This command searches for emails that contain the pattern and prints the students' <br>corresponding names. This search is also case insensitive.    |
| `"-gpa <gpa>[+-]"`   | This command finds students that have a higher (if '+') or lower (if '-') gpa than<br> the inputted gpa number and prints the full name of the students. |

No dependencies, other than python itself, are needed to run the code. Enter the following in the terminal to clone the repository so the code can be run locally.
```
git clone https://github.com/vx-nihili/ScreeningTest.git
cd ScreeningTest
```

## Demo
To get an idea of how this program will work, [testFile.csv](https://github.com/vx-nihili/ScreeningTest/blob/master/testFile.csv) has been included with 10,000 randomly generated names, emails, and gpa scores. Once the repository has been cloned, enter the following code to try the program. Note that any command following the directions above can be used with this file, this is simply an example.
```
python ClassRosterSearch.py "-name johnson" testFile.csv
```
The following names should be printed:
```
Ryker Johnson
Harry Johnson
Raphael Johnson
Pablo Johnson
Ricardo Johnson
Sarah Johnson
Lilianna Johnson
Libby Johnson
Siena Johnson
Javon Johnson
Ainsley Johnson
```
While this particular csv test file does not have headers, the program will work with any csv file, regardless if file contains headers or not, as long as the csv file is formatted correctly (i.e. FirstName, LastName, email, gpa).
