# substitution0

Transparently, this took me a little bit more time than required (still easy though) because I didn't notice one thing. At the top of the `message.txt` file are 26 uppercase characters - also known as a scrambled alphabet. Thus it is very, very easy to discern the substitution cipher even without a frequency analysis.

A nice online tool for solving this challenge is [https://cryptii.com/pipes/alphabetical-substitution](https://cryptii.com/pipes/alphabetical-substitution) where you can copy the message.txt into the ciphertext field in addition to the alphabet at the top into the ciphertext alphabet field.

Included is also my `solve.py` script which prints the flag right away. It defines the ciphertext and plaintext alphabets right away, just like in the above website. The 'genius' of the script lies within the below two lines.

```python
# zip creates a tuple of tuples, dict creates key-value mappings from it
keyMap = dict(zip(key, alphabet))
# .get(keyname, value) where value is the value to return if the keyname does not exist
unscrambled = ''.join(keyMap.get(c.upper(), c) for c in cipher_text)
```

Instead of manually mapping each ciphertext letter to a plaintext one, we use the python zip function which groups the same indexes of two iterables (strings in our case) into a zip object. That's a lot of word vomit so here's a short example.

```python
a_day = ["Steven", "Alexander", "Joseph", "Miranda", "Marabel"]
b_day = ["Alexa", "Sasha", "Weierstrauss", "John"]

print(list(zip(a_day, b_day)))

# Output
# [('Steven', 'Alexa'), ('Alexander', 'Sasha'), ('Joseph', 'Weierstrauss'), ('Miranda', 'John')]
```

In our program, we then convert the zip object to a dictionary, completing our mapping. The following line iterates over each character in our cipher text and either replaces it with it's mapping or maintains the same character (in case it is an integer, etc).

That's all there is to it!
