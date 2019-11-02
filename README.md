# pygrader
Scripts to check python assignments automatically

# How to use:

0. Create a folder "submissions" and place all assignments to check in this folder.

1. Create a file containing class "unit_test". The class will contain tests to be performed on each assignment. (It is recommended to save this file with name "unit_test_file.py"). 


2. Open the file define_unit_test.py and replace "unit_test_file" in the following line with the file name created in the step 1 (no change will be required if the file name is "unit_test_file.py")

from unit_test_file import unit_test

3. Run following commands:

python check_assignments.py [-all -o outputfile]

-all to check all assignment without interruption. Otherwise it will ask to continue after each assignment
-o outputfile (default is "results.txt")

# Example:

python check_assignments.py -all -o results.txt

python check_assignments.py -o results.txt


# Dependency 
unittest
py_compile
