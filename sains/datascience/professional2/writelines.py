file = open("hello.txt", "w")
file.writelines(["hello under", "kamu siap nikah?"])
file.close()
file.writeline("menulis dalam 1 baris")
file.writeline("masuk")

buka = open("hello.txt", "r")
for i in buka :
    print(i)
    