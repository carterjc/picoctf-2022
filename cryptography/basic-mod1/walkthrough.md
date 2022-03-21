# basic-mod1

This challenge is pretty straightforward presupposing an understanding of the modulo operation (or at least how to use it).

I believe the easiest solution is to write a script, though this problem is very feasible to complete manually.

My solution script, `solve.py`, is attached, but I'll walk through it quickly.

The first line, `m = 37`, defines a globally accessible variable m (denoting modulus) to 37 as per the instructions. Similarly, `mod = []` aims to store the numbers after the modulo operation has been applied.

```python
with open("message.txt", "r") as f:
    nums = f.read().split(" ")
    for num in nums[:-1]:
        mod.append(int(num) % m)
```

The above block is the first main portion of the program. It opens `message.txt`, the provided message file with the integers, and separates each number into an array called `nums`. The array is then iterated over, with each value modulo 37 being stored in our `mod` array.

The `final` variable will store our flag.

Since the mod has been applied, we need only to iterate over each number and map it to its corresponding value. We take advantage of the decimal representation for ASCII characters to do this easily.

Running this program results in the following flag: `picoCTF{R0UND_N_R0UND_C0A86577}`
