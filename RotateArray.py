import sys
 
# total arguments
print("Hello");
n = len(sys.argv)
rr = sys.argv
print("test ::",rr)
inArr = {1,2,-99,-4,5}
inputArr = list(inArr)
numbToRotate = int(input("Enter the number "))

def rightArr(Arr, y):
    for i in range(0, y):
        a = list([0] * len(Arr))
        a[0] = Arr[len(Arr) - 1]
        for x in range(1,len(Arr)):
            a[x] = Arr[x-1]
        Arr = a
        print(a)
        # for z in a: TEST
        #     print(z)
rightArr(inputArr, numbToRotate)