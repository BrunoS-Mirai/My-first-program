print ("CALCULATOR");
print ("Choose the desired option");
print ("[1] Addition");
print ("[2] Subtraction");
print ("[3] Multiplication");
print ("[4] Division");

option = int (input());

number1 = int (input ("Digite o primeiro número "));
number2 = int (input ("Digite o segundo número "));

if option == 1:
    print (f"Resultado: {number1 + number2}");
elif option == 2:
    print (f"Resultado: {number1 - number2}");
elif option == 3:
    print (f"Resultado: {number1 * number2}");
elif option == 4: 
    print (f"Resultado: {number1 / number2}");