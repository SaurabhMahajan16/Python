"""
try:-> something that might cause an exception
except:-> do this if there was an exception
else:-> do this if there were no exceptions
finally:-> do his no matter what happens

"""
try:
    file=open("afile.txt")
    dict={"key":"value"}
    dictValue=dict["thisIsnotTheKey"]
    print(dictValue)
except Exception as e:
    print(e)
    file=open("afile.txt", "w") 
    file.write("something")
#except KeyError as f:
#    print(f)
else:
    content=file.read()
    print(content)
    
finally:
    file.close()
    print("file was closed")
    #raise TypeError("this is the error i made for practise")

height=float(input("enter your height"))
weight=float(input("enter your weight in kg"))

if height>3 or weight>250:
    raise ValueError("Human height is less than 3 and weight is less than 250 kg")

bmi=weight/height**2
print(f"bmi is {bmi}")


"""raise error is which you can create your own exception"""