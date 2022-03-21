m = 37
mod = []

with open("message.txt", "r") as f:
	nums = f.read().split(" ")
	for num in nums[:-1]:
		mod.append(int(num) % m)

final = ""

for i in mod:
	if i <= 25:
		final += chr(i + 65)
	elif i <= 35:
		final += str(i - 26)
	else:
		final += "_"

print("picoCTF{" + final + "}")