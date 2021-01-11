

#Welcome to mathematician.py
#Developers are Working on the file to improve the file more.
#View the terms of uses befor you start using this Module on your work.

#-----------------------------------------------------------------------

#The code starts here-



#To add nmbers, make list of the numbers and call the function add({list name}).

def add(nums):
    add = sum(nums)
    print(add)



#To minus two nmbers, make list of the numbers and call the function mns({list name})

def mns(nums):
    all = (nums.index(nums[-1]))+1
    left = all-2
    while (left>0):
        nums.pop()
        left = left-1
    a = nums[0]
    b = nums[1]
    sub = a-b
    print(sub)




#To multiply nmbers, make list of the numbers and call the function into({list name})

def into(nums):
    into = 1
    for j in nums:
        into = into * j
    print(into)





#To devide two nmbers, make list of the numbers and call the function mns({list name})

def dev(nums):
    all = (nums.index(nums[-1]))+1
    left = all-2
    while (left>0):
        nums.pop()
        left = left-1
    a = nums[0]
    b = nums[1]
    dev = a/b
    print(dev)




#To get a squre root of a number, call the function sqrt({number or number variable})
def sqrt(num):
    sqrt = num**0.5
    print(sqrt)




#To get the squre value of a number, call the function sqr({number or number variable})
def sqr(num):
    sqr = num*num
    print(sqr)



#To get the power value of a number, make a list including the number and the power and then call the function sqr({list})

def pow(nums):
    all = (nums.index(nums[-1]))+1
    left = all-2
    while (left>0):
        nums.pop()
        left = left-1
    a = nums[0]
    b = nums[1]
    pow = a/b
    print(pow)


#Work in progress.
