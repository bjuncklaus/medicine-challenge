# medicine-challenge
Write a python script that reads in a file containing patient data, and outputs the average age of patients in the file. The file is in CSV (comma-separated values) format, with one patient per line. Each line contains the patient's name, age, and diagnosis, in that order, separated by commas.

## Challenge 1
To solve this challenge, you will need to use basic python programming skills such as file input/output, string manipulation, and basic data types.

The CSV file is named `patient_data.csv` and you cannot use any libraries to solve this challenge, only native python code is allowed. Your output should be a number indicating the average age of all patients in the file. For example, if the CSV file contained only the following data:

| Name         | Age | Diagnosis      |
| ------------ | --- | -------------- |
| John Smith   | 35  | Flu            |
| Jane Doe     | 41  | Cold           |
| Mike Thompson| 29  | Allergy        |
| Sarah Johnson| 38  | Flu            |

The output of your python script should be: `33.25` because, in the example, there are four patients with ages 35, 41, 29, and 38, respectively. The sum of these ages is 133, and the average age is therefore 133 / 4 = `33.25`.

## Challenge 2
Now calculate and output the average age of all patients grouped by `Diagnosis`. For example, using the same data in the previous challenge, the output should be something similar to this:
```
Average age for Flu diagnosis: 36.5
Average age for Cold diagnosis: 41.0
Average age for Allergy diagnosis: 29.0
```
