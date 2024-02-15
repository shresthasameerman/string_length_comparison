str1=input("enter the 1st string:")
str2=input("enter the 2nd string:")
if len(str1)>len(str2):
    print("the 1st string entered has the maximum length")
elif len(str1)<len(str2):
    print("the 2nd string entered has the maximum length")
else:
    print("both string has equal length")
