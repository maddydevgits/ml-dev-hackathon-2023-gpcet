# Reading List
a=[10,11,13,31,22,121,133]

# checking whether k is palindrome
def palindrome(k):
    dummy=str(k)
    dummy=dummy[::-1]
    if(dummy==str(k)):
        return 1
    else:
        return 0

# iterating through list
count=0
for i in a:
    if palindrome(i):
        count+=1

# print result
print(count)
