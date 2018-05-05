#Euler Problem 20: Factorial digit sum
def factorial(var): 
    ans = 1
    # I created a list of the range for the number. it starts from 0 so I add 1
    mylist = list(range(1,var+1)) 
    #The loop cycles through the list mulitiplying them together
    for i in mylist:
        ans = ans*i
    return (ans)
sol20 = 0
string20 = str(factorial(100))
for i in range(0,len(string20)):
    sol20 = sol20 + int(string20[i])
print("The answer to Euler 20 is ")
print(sol20)
    