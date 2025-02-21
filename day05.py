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
print(bubble_sort(lst))
lst_=[1,2,3,4]
print(bubble_sort(lst_))