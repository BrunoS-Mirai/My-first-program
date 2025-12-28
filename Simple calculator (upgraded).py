import re

calculator = input ("Enter the operation ");
#The input() function displays the message "Enter the operation: " to the user
#and waits for them to type something on the keyboard.
#The entered value will be stored in the variable "calculator".
#This variable will contain a string with the mathematical operation that the
#user wants to perform

standard = r"(\d+)\s*([\+\-\*/])\s*(\d+)"
#(\d+): Captures the first number.
#\s*: Ignores spaces before the operator.
#([\+\-\*/]): Captures the mathematical operator (one of: +, -, *, /).
#\s*: Ignores spaces after the operator.
#(\d+): Captures the second number.

match = re.match (standard, calculator);
#The re.match() function is used to try to find a match
# between the string calculator and the pattern defined in the 
# variable "standard".

#re.match() attempts to match the beginning of the string.
#In other words, it checks if the string starts with the pattern that was 
# defined in the regular expression.

#If a match is found, the function returns a match object containing the 
# parts of the string that matched the groups in the regex. 
# Otherwise, it returns None.

#If the user typed something like "3 + 4" or "15 - 7", the match will try to
#identify the numbers and the operator.
#If there is a match, the match object will have the capture groups
#(the two numbers and the operator).
    
if match: 
#match: This is the object that was returned by the function
#re.match(standard, calculator).
    
#The "if match:" statement is used to check if a match has been found.
    num1 = int (match.group(1));
    #"group()" method is used to access the capture groups
    # that the regular expression found during the matching.

    #match.group(1) accesses the first capture group, that is,
    # the first number the user entered in the operation
    operator = match.group(2);
    #match.group(2) accesses the second capture group, which is
    # the mathematical operator.
    num2 = int (match.group(3));
    #access the third capture group, which is the second number of the operation.

    if operator == "+":
        result = num1 + num2;
    elif operator == "-":
        result = num1 - num2;
    elif operator == "*":
        result = num1 * num2;
    elif operator == "/":
        if num2 != 0: 
            result = num1 / num2;
        else: 
            result = "Error: Division by zero.";
    else:
        result = "Invalid operator";
    print (f"result: {result}");
else: 
    print ("Invalid operation. Use the format 10 + 5");

