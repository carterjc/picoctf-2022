m = 41
inv = []

with open("message.txt", "r") as f:
    nums = f.read().split(" ")
    for num in nums[:-1]:
        inv.append(pow(int(num) % m, m-2, m))

final = ""

for i in inv:
    if i <= 26:
        final += chr(i + 64)
    elif i <= 36:
        final += str(i - 27)
    else:
        final += "_"

print("picoCTF{" + final + "}")