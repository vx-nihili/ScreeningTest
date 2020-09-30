## Screening Test for Research: Autograding/Seat Assignment
This is the repository for the screening test, specifically for the project of Autograding and Seat Assignment projects.

This particular project takes two arguments from the terminal, a command and a csv file, and outputs the names (FirstName LastName) that fit the requested data. The possible commands are as follows:

| **Command** | **Description** |
| ----------- | --------------- |
| `-name <pattern>` | Finds any names that contains the pattern and the person's full name. This is case insensitive and looks at both the first and last names. |
| `-email <pattern>` | Finds emails that contains the pattern and outputs their corresponding full name. |
| `-gpa <gpa>[+-]` | Finds students that have a higher (if '+') or lower (if '-') then the inputted gpa number and outputs the full name of the students. |
