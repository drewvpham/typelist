#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The array you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
#
# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the array contains. If it contains only one type, print that type, otherwise, print 'mixed'.
#

l = ['magical unicorns',19,'hello',98,'world', ['sdad'], [2,43,5]]
count=0
total_sum=0
total_string=''
total_list=[]
while count < len(l):

    if type(l[count]) == int:

        total_sum=total_sum + l[count]
        check1=True
    if type(l[count]) == str:
        total_string+=(l[count])
        check2=True
    if type(l[count]) == list:
        total_list.append(l[count])
        check3=True
    count+=1


print total_sum
print total_string
print total_list
