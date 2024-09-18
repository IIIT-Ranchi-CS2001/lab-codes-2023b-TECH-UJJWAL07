def selectionsort(Arr,n):
    for k in range(0,n-1):
        min=Arr[k]
        min_index = k
        for j in range(k+1,n):
            if min>Arr[j]:
                min_index=j
    Arr[min_index],Arr[k]=Arr[k],Arr[min_index]

A=[]
n=int(input("eneter number of elements:"))

for i in range(n):
    x=int(input("enter element"+str(i+1)+": "))
    A.append(x)
print(A)
selectionsort(A)
print(A)

