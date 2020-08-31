import os
# this is a sample test file1
ax = str(10)
print(" value of x :" + ax)

# x = int(input("x value: "))
# y = int(input("y value: "))


def function1(x,y):
    if x == 10:
        print("x is 10")
    elif y == 20:
        print("y is 20")
    else:
        print("x is neither 10 nor 20 ")
    return x
function1(1,0)

print("completed the if loop")

f = open("file4.txt", "r")
print(f.readline())
print(f.readline())
# f.write("\n line 7")
f.close()
os.remove("file4.txt")