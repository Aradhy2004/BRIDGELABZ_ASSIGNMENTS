user_name = input("Enter your name: ")
if len(user_name) >=3:
    message = "Hello <<userName>>, how are you?"
    message = message.replace("<<userName>>" , user_name)
    print(message)
else:
    print(" Name should have atleast 3 character")

