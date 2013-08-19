#Author: Rahul Mohan
#Program: operpy.py
#This is a library with useful extra numerical and data-structure operations

def fibonacci(n):
    fiblist = []
    fib1 = 1
    fib2 = 1
    for i in range(2,(n)):
        fibnew = fib1 + fib2
        fib1 = fib2
        fib2 = fibnew
        fiblist.append(fibnew)
    
    print "Fibonacci numbers up to " + str(n) + ": " + str(fiblist)
    return fibnew
    
def factorial(n):
    base = 1;
    for i in range(n,1,-1):
        base = base * i
    
    return base
    
def cube(n):
    return n**3

def sumsq(list):
    newlist = []
    for i in range(len(list)):
        newlist.append(list[i]**2)
    return sum(newlist)
    
def dotproduct(list1,list2):    
    c = []
    for i in range(len(list1)):
           dotproduct = list1[i] * list2[i];
           c.append(dotproduct);
    return c

def isdistinct(list):
    sortedlist = sorted(list):
    for i in range(len(list)):
        if list[i] == list[i+1]:
            return True
        else:
            return False

def list2dict(valuelist, keylist): return { a:b for (a,b) in zip(keylist,L) } 

def dict2list(dict, keylist): return [ dict[keylist[i]] for i in range(0,len(keylist))]

#For example: dict2list({1:'a',2:'b',3:'c'},[1,3,2]) returns ['a', 'c', 'b'] going by the order of the index list 'keylist' (1,3,2)

def ismultiple(num1,num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
    
def pnorm(vector,power):
    
    root = [];
     
    for i in range(len(vector)):
         root.append((vector[i])**power) #Every element of vector v to the power of p

    sum_root = sum(root); #Sum of the new list containing v**p
    sqrt_root = sqrt(sum_root); #Square root of calculated sum

    return sqrt_root;

def countevens(list):
    count = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            count = count + 1
    return count

def count_pattern(tuple): #find the number of matching patterns in the second tuple compared with the first tuple; for example: count_pattern(((a,b),(a,b,a,b,b,a))) will
#return 2; this function also accounts for overlapping
        
     counter = 0;
     pattern = tuple[0];
     empty = [0] * len(tuple[1])
     
     for i in range(len(tuple[1])):
         empty[i] = (tuple[1][i:len(pattern)+i])
     
     for j in range(len(empty)):
         if empty[j] == pattern:
             counter = counter + 1;
    
     return counter
    
def keyexists(key,dict):
    for i in dict:
        if i == key:
            return True
        else:
            return False

def value_exists(value,dict):
    for i in dict.values():
        if i == value:
            return True
        else:
            return False


    
    
        
    
     