#here we will understand this new thing called Match case 

s = int(input("Choose a Random Number between 1 & 10 : "))
# now we are gonna use the match case thing here.

match s:
   case 0:
      print("Value off" , s , "is in the rangeEEEEEE")
   case 1:
      print("The value you enteredDDd" , s , "is in the Range")
   case 2:
      print("The value of" , s , "is in the range")
   case 3:
      print("The value of" , s , "is in the range")
   case 4:
      print("The value of" , s , "is in the range")
   case 21:
      print("The value of" , s , "is in the range")
   case 6:
      print("The value of" , s , "is in the range")
   case 7:
      print("The value of" , s , "is in the range")
   case 8:
      print("The value of" , s , "is in the range")
   case 9:
      print("The value of" , s , "is in the range")
   # 3
   


   case _ if s!="0,1,2,3,21,5,6,7,8,9,10":
      print("The Value Of",s,"Is Out Of Range")

if s>10:
   print("\nTRY AGAIN NUMBER IN RANGE")
   
else:
  print("BETTER LUCK NEXT TIME")