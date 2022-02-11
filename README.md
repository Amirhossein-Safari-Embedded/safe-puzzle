# The safe-puzzle

---------
In this example code, we are going to solve the following safe puzzle.

Suppose that the password is three digits with available information as follow:

682: One of the digits is correct with the right location.  
614: One of the digits is correct but not in the right location.  
206: Two of the digits is correct but not in the right location.  
738: All the digits are incorrect.  
380: One of the digits is correct but not in the right location.  

What is the desired password?

To solve this puzzle, a python program is written and the answer can be obtained by running this python program.  
Also to test the implemented function, the "pytest" module is used.

# How to install "pytest"
`pip install pytest`

# How to use "pytest"
Suppose that you have the "my_func.py" file and have implemented a function entitled "my_func" in it. Our goal is to test the function with some input and respective  
outputs. To do that using the "pytest" module, you need to define a function with a name starting with "test_" and use the "assert" statement  
to evaluate the results. After all, you only need to run the following command:  
  
`pytest my_func.py`  
  
The aforementioned command runs every function that has a name starting with "test_" and report the results.  
It is preferred that to implement tests in separated files. To pytest recognise the test files, you should entitle the files starting with "test_" or ending
with "_test". As it is mentioned before the test function names should start with the "test_" keyword.  
After all, you just need to run the following command. This command finds every python file with names starting with "test_" or ending with "_test". Then run every function with names starting with "test_" within these python files.  
  
`pytest`



