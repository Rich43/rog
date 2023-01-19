'''
Let's try something different this week. Our output is going to be sound instead of text/graphics
Formal Inputs & Outputs

No real input for this challenge. But this is research/getting familiar with the sound framework
of your language, for the next 2 challenges.

You create an applition that produces Do–Re–Mi–Fa–Sol–La–Si of the Solfège.
Notes/Hints

Here you find some more info about music notes, especialy the part about frequencies.
Bonus

Be able to output Chords

'''

import winsound


def solfege():
    Do = 261
    Re = 294
    Mi = 327
    Fa = 348
    Sol = 392
    La = 436
    Si = 490
    s = [Do, Re, Mi, Fa, Sol, La, Si]
    return s

duration = 300
if __name__ == '__main__':
    scale = solfege()
    for note in scale:
        winsound.Beep(note, duration)