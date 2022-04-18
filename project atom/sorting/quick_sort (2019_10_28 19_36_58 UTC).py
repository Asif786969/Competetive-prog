def partition(a,si,ei):
    pivot=a[si]
    c=0
    for i in range(si,ei+1):
        if(a[i]<pivot):
            c+=1
    a[si+c],a[si]=a[si],a[si+c]
    pivot_index=si+c
    i=si
    j=ei
    while(i<j):
        if(a[i]<pivot):
            i+=1
        elif(a[j]>=pivot):
            j-=1
        else:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
    return pivot_index


def quickSort(a,si,ei):
    if si>=ei:
        return
    pivot_index=partition(a,si,ei)
    quickSort(a,si,pivot_index-1)
    quickSort(a,pivot_index+1,ei)
arr=[1,2,3,6,4,1,0,9]
quickSort(arr,0,len(arr)-1)
print(*arr)
