environment = input("Please enter environment:" )
print(type(environment))
# environment = "PROD"
change_ticket = False
environment = environment.casefold()

if environment == "prod":
    change_ticket = True
    print("Please provide change ticket")
elif environment == "qa":
    print("welocome to qa environment")
else:
    print("please log in through  your credentials")

## python is a case sensitive
# indentation is important in python
# condition must be specified before continue

