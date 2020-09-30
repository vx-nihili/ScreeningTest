## Screening Test for Research: Autograding/Seat Assignment
This is the repository for the screening test, specifically for the project of Autograding and Seat Assignment projects.

This particular project takes two arguments from the terminal, a command and a csv file, and outputs the names (FirstName LastName) that fit the requested data. The possible commands are as follows:

|      **Command**                                         |               **Description**             |
| -------------------------------------------------------- | ----------------------------------------- |
| `-name <pattern>`  | This command finds any student names that contains the pattern and outputs the students' full names. This is<br> case insensitive and looks at both the first and last names. |
| `-email <pattern>` | This command searches for emails that contain the pattern and outputs the students' corresponding names.                                              |
| `-gpa <gpa>[+-]`   | This command finds students that have a higher (if '+') or lower (if '-') than the inputted gpa number and outputs<br> the full name of the students. |
