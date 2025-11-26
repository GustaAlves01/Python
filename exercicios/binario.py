
def Sort(n):
    arr = [1,2,3,4,5,6,7,8]
    max=7
    min=0
    while min<=max:
        mid=(max+min)//2
        if arr[mid]>n:
            max=mid-1
        elif arr[mid]<n:
            min=mid+1
        else:
            break
    print(mid)

Sort(1)