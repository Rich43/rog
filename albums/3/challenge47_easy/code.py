''' Your task today is to implement one of the oldest ciphers known, the so-called Caesar cipher (or Caesar shift, as it is sometimes called). It works like this: for every letter you want to encrypt, you shift it some number of places down the alphabet to get the letter in the cipher.

So, for instance, in a Caesar cipher with a shift of 3, "A" becomes "D", "B" becomes "E", "C" becomes "F", and so on. At the end of the alphabet it wraps around, so "W" becomes "Z", "X" becomes "A", "Y" becomes "B" and "Z" becomes "C". If you encrypt "Hello" with a shift of 3, you get "Khoor".

One interesting thing about this cipher is that you can use the same algorithm to decode a cipher as you can to encode it: if you wish to decrypt some text that has been Caesar-shifted 6 places, you simply shift it another 20 places to get back the original text. For example, if you encrypt "Daily programmer" with a shift of 6 you get "Jgore vxumxgsskx", and if you encrypt "Jgore vxumxgsskx" with a shift of 20 you get "Daily programmer".

Implement the cipher and encrypt a bit of text of your choice!

Bonus: Using your program, become a code-cracker and decrypt this cipher (posted in honor of Mayday):
'''

def encode(letter):
    ''' str -> str '''
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    indx = alph.index(letter)
    shift = (indx - 7) % 26
    result = alph[shift]
    return result

if __name__ == '__main__':

    message = "Spzalu - zayhunl dvtlu sfpun pu wvukz kpzaypibapun zdvykz pz uv ihzpz mvy h\
    zfzalt vm nvclyutlua.  Zbwyltl leljbapcl wvdly klypclz myvt h thukhal myvt aol\
    thzzlz, uva myvt zvtl mhyjpjhs hxbhapj jlyltvuf. Fvb jhu'a lewlja av dplsk\
    zbwyltl leljbapcl wvdly qbza 'jhbzl zvtl dhalyf ahya aoyld h zdvyk ha fvb! P\
    tlhu, pm P dlua hyvbuk zhfpu' P dhz hu ltwlylyvy qbza iljhbzl zvtl tvpzalulk\
    ipua ohk sviilk h zjptpahy ha tl aolf'k wba tl hdhf!... Ho, huk uvd dl zll aol\
    cpvslujl puolylua pu aol zfzalt! Jvtl zll aol cpvslujl puolylua pu aol zfzalt!\
    Olsw! Olsw! P't ilpun ylwylzzlk!"

    out = ''
    for letter in message:
        if letter.isalpha():
            out += encode(letter)
        else:
            out += letter
    print(out)