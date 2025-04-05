#take input for the student that he can attend or not
medical_cause=input("did you have a medical medical_cause Y or N")
#take input of the attendence
atten=int(input("enter the attendence of the student"))
#checking the user input predicting output accordinglly
if medical_cause=="Y":
    print("student can attend the class")
elif atten>=75:
    print("student can attend the class")
else:
    print("student can not attend the class")
#end of the program