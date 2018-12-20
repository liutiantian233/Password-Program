# Password Program

The substitution cipher is a cipher that has been in use for many hundreds of years. It basically consists of substituting every plaintext character for a different ciphertext character. The cipher alphabet may be shifted or reversed or scrambled. In this project, we will **combine** two types of substitution cyphers: a simple substitution cipher followed by an affine cipher.

-------------------

## Encoding
 
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

Thus, the string ‘green’ becomes the string ‘nrggl’. You will use that cyphertext ‘nrggl’ as the starting point (“plaintext”) for the next stage, the affine cipher.

-------------------

## Decoding

**Affine cipher**: The key for the Affine cipher consists of two numbers, a and b. It takes in a plain-text string, and translates it into a new string based on an encryption/decryption functions that rotate the alphabet of size m: 
- 1 The encryption function is y = (a * x + b) mod m
- 2 The decryption function is the inverse operation
- 3 Do the encryption backwards (mathematically decryption is x = a<sup>-1</sup> * (y − b) mod m where a<sup>-1</sup> satisfies the equation 1 = a * a<sup>-1</sup> mod m, but in this case thinking mathematically will make programming much more difficult).

**To encrypt** consider our plaintext ‘green’ and its cyphertext ‘nrggl’ now using our affine key (a=5, b=8). After scrambling the alphabet using the keyword “michigan” and encrypting the plaintext "green” to “nrggl”, we will encrypt "nrggl" using the table mentioned above for the numeric values of each letter, from our key a is 5 and b is 8, and finally m is 26 since there are 26 characters in the alphabet being used. The first step is to write the numeric values of each letter using the scrambled alphabet. Then, take each value of x, and solve the first part of the equation, (5x + 8). After finding the value of (5x + 8) for each character, take the remainder when dividing the result of (5x + 8) by 26. The final step in encrypting the message is to look up each numeric value in the table for the corresponding letters. In this example, the encrypted text would be “kpccv”. The table below shows the completed table for encrypting a message in the Affine cipher.

![image](https://github.com/liutiantian233/Password-Program/blob/master/encrypt.png)
