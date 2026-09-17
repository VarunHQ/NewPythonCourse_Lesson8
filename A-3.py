#input no greater than 1
n = int(input("Enter the value of n: "))

#printthe numbers n to 1
print("The numbers from {0} to {1} are: " .format(n,1))
#loop to print the numbers
for i in range(n, 0, -1):
    print(i)