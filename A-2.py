#Input a word or sentence 
string = input("Please enter a word/string: ")

string2 = ('')
#loop for printing the given string in reverse order
for i in string:
    string2 = i + string2
print("\n Original String: ", string)
print("The Reversed string: ", string2) 