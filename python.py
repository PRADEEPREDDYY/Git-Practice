import os
# this is a sample test file1
ax = str(10)
print(" value of x :" + ax)

# x = int(input("x value: "))
# y = int(input("y value: "))

print("completed the if loop")

f = open("file4.py", "r")
print(f.readline())
print(f.readline())
# f.write("\n line 17")
f.close()

if os.path.exists("file2.txt"):
    os.remove("file2.txt")
    print("file2 deleted")
else:
    print("file2 not present")
# os.remove("file4.txt")
a = str(5)
def fun1():
    a, b =0, 1
    while(a < 10):
        if a == 0:
            print(a)
        a, b =b, (a+b)
        print(a)

fun1()

print("a value " + a)
print("done with while loop")
