# morse-code

For the low-level morse code challenges, Audacity is **the** best method to solve (in my opinion and experience). It so happens that this challenge can also be solved automatically, but I'll briefly cover that at the end.

Opening the file in Audacity reveals a lot of rectanges of varying lengths. These are our morse code representations, the longer box representing a dash (`-`) and the shorter one representing a dot (`.`). The long breaks are underscores, as per the challenge description. Use a morse code translator (online works very well) and work through the file. This will give you the flag.

Additionally, you can run the .wav through a tool like [this Adapative Audio Decoder for morse code](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) which returns the following string `WH47 H47H 90D W20U9H7`. Replace the spaces with underscores and wrap it in the pico flag syntax for a submittable flag: `picoCTF{WH47_H47H_90D_W20U9H7}`
