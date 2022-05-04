from pickle import APPEND


def countdown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list
print(countdown(5))    

def print_return(x,y):
    print (x)
    return (y)
i = print_return(3,5)


def first_plus_length(list):
    sum=(list [0])
    x= (sum + len(list))
    return x
print (first_plus_length([1,2,3,4,5]))



def greater_than_second(list):
    x=[]
    if len(list) <= 2:
        return'False'
    for i in range(0,len(list),1):
        if list[i] > list[1]:
            x.append (list[i]) 
    print (len(x))        
    return x
    
    
print (greater_than_second([5,2,3,2,1,4]))
print (greater_than_second([5,2]))


def length_value(x,y):
    z=[]
    for i in range(0,x):
        z.append(y) 
    
    return z
    


print (length_value(4,7))
print (length_value(6,2))