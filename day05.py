def bubble_sort(lst):
    lst_length=len(lst)-1
    for i in range(lst_length):
        for j in range(lst_length):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=[2,7,1,9]
print(bubble_sort(lst))
