# #let's discover various strings of python today.

# string1 = " ShIVVVesH "
# # print(string1.upper())
# # print(string1.lower())

# print(string1.lower())
# print(string1.upper())

string2 = " ShIVEEEEsHHH "
print(string2.strip("-"))

# string3 = "Hello Shivesh !!!"
print(string2.rstrip("-"))

# string4 = "Hello Shiveshhh"
# # print(string4.replace("Hello" , "Hi"))
# print(string4.replace("Shiveshhh" , "shivesh25"))

string5 = "Namaste Sirji"
# print(','.join(string5))
# print (string5.split(",."))
print (string5.split())

string6 = "JAI SHRI RAM"
print(string6.capitalize())

string7 = "SHIVESH RICHHARIYA"
# print(string7.center(89 , ":"))
print(string7.center(38 , ","))

# string8 = "shibusokoksjsdbjsdhubsnslifnlnclsnssnfirls"
# print(string8.count("s"))
from collections import Counter

string8 = "shibusokoksjsdbjsdhubsnslifnlnclsnssnfirls"
letter_counts = Counter(string8)

print(letter_counts)
print(len(string8))


# print(string8.count("l"))