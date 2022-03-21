# basic-mod2

Unlike `basic-mod1`, this challenge is difficult to complete by hand due to the nature of modular inverses. So we'll script (again)!

This challenge is *extremely* similar to its earlier namesake, so we'll essentially use our earlier script once again. The solution script, `solve.py` is attached.

The largest difference is the use of a modular difference on line 7 in comparison to a basic modulo operation.

`inv.append(pow(int(num) % m, m-2, m))`

Breaking down the above statement for a modular inverse, we can see that the integers from the `message.txt` file modulo 41 are the first parameter of our function. Second is `m-2`, the power we raise our first parameter to. Lastly, we take the result from the operation between the first two parameters and apply the modulus of 41 again.

The only other difference with our program is the mapping. Instead of starting at 0, we start at 1 and have to adjust our integers accordingly.

After running the `solve.py` program, the following flag is printed: `picoCTF{1NV3R53LY_H4RD_261CB530}`
