## Screening Test for Research: Autograding/Seat Assignment
This is the repository for the screening test, specifically for the project of Autograding and Seat Assignment projects.

This particular project takes two arguments from the terminal, a command and a csv file, and prints the names (FirstName LastName) that fit the requested data. The possible commands are as follows:

|      **Command**                                         |               **Description**             |
| -------------------------------------------------------- | ----------------------------------------- |
| `-name <pattern>`  | This command finds any student names that contains the pattern and prints the students'<br> full names. This is case insensitive and looks at both the first and last names. |
| `-email <pattern>` | This command searches for emails that contain the pattern and prints the students' <br>corresponding names.                                              |
| `-gpa <gpa>[+-]`   | This command finds students that have a higher (if '+') or lower (if '-') than the inputted <br>gpa number and prints<br> the full name of the students. |
