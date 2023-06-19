print ("1. Add")

print ("2. Subtract")

print ("3. Multiply")

print ("4. Divide")

print ("Enter choose operation above : ")


operation = input()


n1 = input ("Enter n1 : " )

n2 = input ("Enter n2 : " )


if operation == "1":

   sum = int(n1) + int(n2)

   print ("The sum is ", sum)


elif operation == "2":

   difference = int(n1) - int(n2)

   print ("The difference is ", difference)


elif operation == "3":

   product = int(n1) * int(n2)

   print ("The product is ", product)


elif operation == "4":

   result = int(n1) / int(n2)

   print ("The result is ", result)


else:

   print ("Invalid Number.\nPlease choose the correct operation.")

