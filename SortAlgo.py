import random

MyArray = []


for i in range(10):
    MyArray.append(random.randint(1,100))
print(MyArray)



def BubbleArray():
    for i in range(len(MyArray)):
        swapped = False
        for j in range(len(MyArray) - i - 1):
            if MyArray[j] > MyArray[j + 1]:
                MyArray[j], MyArray[j + 1] = MyArray[j + 1], MyArray[j]
                swapped = True
        if not swapped:
                break
    return MyArray

print(BubbleArray())


     