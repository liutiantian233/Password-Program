# Password Program

The substitution cipher is a cipher that has been in use for many hundreds of years. It basically consists of substituting every plaintext character for a different ciphertext character. The cipher alphabet may be shifted or reversed or scrambled. In this project, we will **combine** two types of substitution cyphers: a simple substitution cipher followed by an affine cipher.

## Encoding and Decoding
 
**Simple substitution cipher**: the cipher alphabet is created by first writing out a keyword, removing repeated letters in it, then writing all the remaining letters in the alphabet in the usual order. Consider the following example. Consider the alphabet being a single string consisting of the lower-case English letters as below (shown with each letter’s associated index, e.g. m’s index is 12):

![image](https://github.com/liutiantian233/Password-Program/blob/master/index.png)

Then, using this system, the keyword "michigan" gives us the following alphabet mapping:

![image](https://github.com/liutiantian233/Password-Program/blob/master/michigan.png)

Note how “michigan” starts the mapping, how the second “i” is skipped, and how the remaining letters continue in alphabetical order without the characters of “michigan”.

Using the example above, the word “green” is translated as follows:
- the ‘g’ is found at index 6 in the alphabet. The letter in the rotated alphabet is ‘n’.
- the ‘r’ is found at index 17, the rotated letter is ‘r’.
- the ‘e’ is found at index 4, the rotated letter is ‘g’.
- the ‘e’ is found at index 4, the rotated letter is ‘g’.
- the ‘n’ is found at index 13, the rotated letter is ‘l’.

-------------------
