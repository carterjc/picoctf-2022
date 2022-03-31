with open("message.txt", "r") as f:
        t = f.read()
        blocks = [t[i:i+3] for i in range(0, len(t), 3)]
        t2 = ""
        for block in blocks:
                t2 += block[-1] + block[:2]
        print(t2)