import copy
def bubble_sort(lst):
    lst_length=len(lst)-1
    for i in range(lst_length):
        no_swap=True
        for j in range(lst_length-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                no_swap = False
                print(j,end=' ')
        if no_swap:
            return lst
    return lst
lst=[2,7,1,9]
print("bubble_sort예시")
print(bubble_sort(lst))
lst_=[1,2,3,4]
print("bubble_sort예시")
print(bubble_sort(lst_))

def insertion_sort(lst):
    for i in range(1,len(lst)):
        value=lst[i]
        while i>0 and lst[i-1]>value:
            lst[i]=lst[i-1]
            i=i-1
        lst[i]=value
    return lst

def quick_sort(lst):
    n=len(lst)
    if n<=1: return 1
    pivot=lst[n//2]
    left,right=list(),list()

    for i in lst:
        if i<pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)

    return quick_sort(left)+[pivot]+quick_sort(right)

lst=[2,7,1,9]
print("insertion_sort예시")
print(insertion_sort(lst))
lst_=[1,2,3,4]
print("insertion_sort예시")
print(insertion_sort(lst_))
lst__=lst_.copy()
print("quick_sort예시")
print(lst__)