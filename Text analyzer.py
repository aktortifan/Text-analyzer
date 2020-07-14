text = input("Please input your text: ")

#Is the default value if there is no space in the string
co_space = 0

#Making the function for counting upper keys. isupper() will return True if the
#single character is upper key

def upper(x):
    return x.isupper()

#Making the function for counting lower keys. islower() will return True if the
#single character is lower key

def lower(x):
    return x.islower()

#I am using the loop. When the loop met the True value, it would be added by one
for i in text:
    if(i.isspace()):    
        co_space = co_space + 1 

#The function map takes a function and an iterable as arguments, 
#and returns a new iterable with the function applied to each argument.        
res_up = list(map(upper, text))
res_low = list(map(lower, text))


print("The length of the text (with spaces): ", len(text))
print("The length of the text (without spaces): ", len(text)-co_space)
print("The number of spaces): ", co_space)

#sum() will only count the True value
print("The number of uppercases : ", sum(res_up))
print("The number of lowercases : ", sum(res_low))

