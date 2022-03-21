# credstuff

The first step to solving this challenge is untar-ing the archive which contains our usernames and passwords files. Run `tar -xvf leak.tar` to extract the files to the `leak/` subdirectory.

The hint seems to nudge us in the direction of the `passwords.txt` file, so let's go there first. The most obvious thing to check is if it possesses the flag itself. CTRL-F-ing for `picoCTF{` turns up blank, but while doing so you might note the presence of the word pico alone. Navigating to this line (the only line with the phrase), we see the following text: `pICo7rYpiCoU51N6PicOr0t13`. The end of this string indicates a `rot13` encoding, so let's run `passwords.txt` through CyberChef.

We can drag the file to the input panel of the web application and then search rot13 in the operations panel and drag it to the recipe section. CTRL-F-ing for `picoCTF{` after the decoding reveals the following flag: `picoCTF{C7r1F_54V35_71M3}`