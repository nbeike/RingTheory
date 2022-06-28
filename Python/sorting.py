from math import inf
import random

def insertionSort(l: list):
    for x in range(len(list)):
        for y in reversed(range(x)):
            if(l[y+1]<l[y]):
                l[y+1], l[y]=l[y], l[y+1]
            else:
                break    

def selectionSort(l: list):
    for x in range(len(l)-1):
        smallest=x
        for y in range(x, len(l)):
            if l[smallest]>l[y]:
                smallest=y
        l[smallest], l[x]=l[x], l[smallest]

def bubbleSort(l: list):
    for x in range(len(l)):
        for y in range(x,len(l)):
            if l[x]>l[y]:
                l[x], l[y]=l[y], l[x]

def mergeSort(A: list):
    
    if len(A)>1:
        
        mid=len(A)//2
        
        L=A[:mid]
        R=A[mid:]
        
        mergeSort(L)
        mergeSort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
    
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
    
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

def binarySearch(A: list, x):
    mid=len(A)//2
    # if mid>=1:
    if x==A[mid]:
            print(x, "=", A[mid])
            return True
    elif x<A[mid] and mid>0:
            print(x, "<", A[mid])
            return binarySearch(A[:mid], x)
    elif x>A[mid] and mid>0: 
            print(x, ">", A[mid])
            return binarySearch(A[mid:],x)
    else:
        return False

    if len(A)==1:
        return (0,0,A[0])
    else:
        mid=len(A)//2
        ll,lh,ls=maxSubArrayDC(A[:mid])
        rl,rh,rs=maxSubArrayDC(A[mid:])
        cl,ch,cs=maxCrossingSubArray(A)
    if ls>=rs and ls>=cs:
        return (ll,lh,ls)
    elif rs>=ls and rs>=cs:
        return (rl,rh,rs)
    else:
        return (cl,ch,cs)

def maxSubArray(A: list):  #Kadane
    bs=float(-inf)
    bl=br=0
    cs=0
    for x in range(len(A)):
        cr=x
        if cs<=0:
            cl=cr
            cs=A[x]
        else:
            cs+=A[x]
        if cs>bs:
            bs=cs
            bl=cl
            br=cr
    return bl, br, bs   

def code():
    A=[]
    for x in range(10):
       A.append(random.randint(-2,2))
    print(A)
    A.pop(0)
    print(A)
    A.pop(1)
    print(A)
    # bubbleSort(list)
    # print(list)
    # if binarySearch(list,50)==True:
    #     print("50 is in the list")
    # else:
    #     print("50 is not in the list")

code()

