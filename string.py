#Greeting="Greetings to you"
#name-input


greeting = "Greetings to you" #Basic greeting
name = input("Please enter your name: ")

#Capatalization of the first letter
message = "HELLO world"
print(message.capitalize())
print(message.upper())
#Lower case
print(message.lower())
#Capatalization of the first letter of every word 
print(message.title())
#Switches lowercase to uppercase and vice versa
print(message.swapcase())

#Erasing whitespace(triming)
quote=" to be, or not to be, that is the question"
print(quote.strip())
print(quote.lstrip())
print(quote.rstrip())

#Exercises
user_data+" I'm going to "




message ="Mr. Ustrzycki's class is the worst class in the world.best"
message = message.replace("worst", "best")
print(message)
print(message.find("best"))
print(message.rfind("best"))
message_list = message.split("")
print(message_list)
print(message_list[1]) #prints only the second word


quote = "Glory is fleeting, but obscurity is forever"

new_quote = quote.split(" ")

print(new_quote[2])