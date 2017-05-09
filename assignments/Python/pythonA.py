#Find and replace
str = "It's thanksgiving day. It's my birthday,too!"
print str.find('day') #the first instance of day has the 18th position so output should be 18

list = str.split() #splitting string into a list since lists are mutable
replacedWord = "day."

for count in range(0, len(list)): #len is length of list;
    if list[count] == replacedWord: #when reach the word day in loop/count is Returns the count of number of items passed as an argument
        list.insert(count, "month.") #insert the word month/ .insert is o insert an item at the defined index
        break #once if statement met exit loop
list.remove(replacedWord) #remove the word day

newStr = (' ').join(list) #join the list together
print newStr

#Min and Max: https://docs.python.org/2/library/functions.html#max
x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)

#First and Last Values from a list
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0], x[-1]


#Create A New List
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
sortedList = sorted(x)
print sortedList

firstHalf = sortedList[0 : (len(sortedList) / 2)]
print firstHalf

secondHalf = sortedList[(len(sortedList) / 2) : len(sortedList)]
print secondHalf

secondHalf.insert(0, firstHalf) #Assigning this to variable and printing variable prints 'None' :S
print secondHalf #[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]

# Excellent! Keep it up!
