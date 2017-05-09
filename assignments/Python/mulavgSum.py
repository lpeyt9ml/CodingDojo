#Multiples: Find Odd Numbers and Multipes of 5
#for x in range(0, 101):
    #if (x % 2 == 0):
        #print x
for x in range(0, 1000):
    if x % 2 != 0: #if number doesn't haven't remainder of 0 meaning it is od
        print x

print(range(0,1000,5)) #start, end, define multipe


#Fnd the Sum of a List
a = [1, 2, 5, 10, 255, 3]
print sum(a)


#Find the Aveeage of a List
a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a) #The sum of the list divided by the length of the list
