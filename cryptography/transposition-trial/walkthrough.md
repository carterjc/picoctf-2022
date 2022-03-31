# transposition-trial

In my opinion, the hint really gives this to you on a silver platter. That being said, only a quick analysis would probably lead you to a similar conclusion. From a quick visual analysis, we can see the letters were divided into blocks of three and then the first letter was moved to the end. For example, `The` turns into `heT`. I wrote a quick python script to solve this challenge--it's not the cleanest code, but it works!

```python
with open("message.txt", "r") as f:
        t = f.read()
        blocks = [t[i:i+3] for i in range(0, len(t), 3)]
        t2 = ""
        for block in blocks:
                t2 += block[-1] + block[:2]
        print(t2)
```

We can see that I first open up the plaintext file and read its input. Then I divide the string I just instantiated into the `t` variable into blocks of three characters. `t2` is my final text string, so when I iterate over every block I first append the last character and then the first two. The resulting flag is: `picoCTF{7R4N5P051N6_15_3XP3N51V3_5C82A0E0}`.