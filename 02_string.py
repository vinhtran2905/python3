text = " Vinh Tran"

print(text)

text1 = 'First name'

print(text1)


str1 = "I don't eat"

print(str1)


str2 = "she said \" what is the my favourite coloe\""

print(str2)

str3 = "new line \n a new line begins"

print(str3)

print('C:\Windows\my document\newfolder')

print('C:\Windows\my document\\newfolder')

print(r'C:\Windows\my document\newfolder')

firstName = "Bucky"

full = firstName + " Rober"

print(full)


print(firstName * 5)


print(''' this will print multiplines
as the format you typed''')


greeting = 'Hello'
name = 'Vinh'
message = '{}, {}.Welcome to python world'.format(greeting,name.upper())
print(message)

#fstring
message = f'{greeting}, {name.upper()}. Welcome to python world'
print(message)

# method of string
print(dir(message))

print(help(str))

print(help(str.lower))