# We will have a look at the practical use cases and implementation of try, except
# raise and finally

# we will create a variable to store file data using open()

# 1st Iteration
# try: # Use try block for a line of code where we know this will throw an error
#     file = open("orders.text")
# except:
#     print("Panic alert!")

try:  # Use try block for a line of code where we know this will throw an error
    file = open("orders.text")
except FileNotFoundError as errmsg: # Aliasing the erro
    print("Alert something went wrong" + str(errmsg))
# if we still wanted the users to see the actual exception together with customised message
    raise # raise will send back the actual exception i.e. FileNotFoundError

finally: # finally will execute regardles of the above conditions
    print("Hope you had a good Customer experience")