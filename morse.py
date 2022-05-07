from tones import SINE_WAVE
from tones.mixer import Mixer
from tones.tone import Samples
import os

def code(code):

    a = Mixer(44100, 0.5)
    a.create_track(0,SINE_WAVE,0.0,0.0)

    alpha = {
        'a' : ('dit','dah'),
        'b' : ('dah','dit','dit','dit'),
        'c' : ('dah','dit','dah','dit'),
        'd' : ('dah','dit','dit'),
        'e' : ('dit'),
        'f' : ('dit','dit','dah','dit'),
        'g' : ('dah','dah','dit'),
        'h' : ('dit','dit','dit','dit'),
        'i' : ('dit','dit'),
        'j' : ('dit','dah','dah','dah'),
        'k' : ('dah','dit','dah'),
        'l' : ('dit','dah','dit','dit'),
        'm' : ('dah','dah'),
        'n' : ('dah','dit'),
        'o' : ('dah','dah','dah'),
        'p' : ('dit','dah','dah','dit'),
        'q' : ('dah','dah','dit','dah'),
        'r' : ('dit','dah','dit'),
        's' : ('dit','dit','dit'),
        't' : ('dah'),
        'u' : ('dit','dit','dah'),
        'v' : ('dit','dit','dit','dah'),
        'w' : ('dit','dah','dah'),
        'x' : ('dah','dit','dit','dah'),
        'y' : ('dah','dit','dah','dah'),
        'z' : ('dah','dah','dit','dit'),
        '1' : ('dit','dah','dah','dah','dah'),
        '2' : ('dit','dit','dah','dah','dah'),
        '3' : ('dit','dit','dit','dah','dah'),
        '4' : ('dit','dit','dit','dit','dah'),
        '5' : ('dit','dit','dit','dit','dit'),
        '6' : ('dah','dit','dit','dit','dit'),
        '7' : ('dah','dah','dit','dit','dit'),
        '8' : ('dah','dah','dah','dit','dit'),
        '9' : ('dah','dah','dah','dah','dit'),
        '0' : ('dah','dah','dah','dah','dah'),
        ' ' : (' ')
    }

    def response(code):
        for i in code:
            if i not in alpha:
                continue
            for j in alpha[i]:
                if j == 'dah':
                    a.add_tone(0,641.0,0.5)
                    a.add_tone(0,0.0,0.025)
                elif j == 'dit':
                    a.add_tone(0,641.0,0.12)
                    a.add_tone(0,0.0,0.025)
                elif j == ' ':
                    a.add_silence(0,0.35)               
        return

    a.create_track(response(code))
    a.write_wav('/home/dae/Documents/Projects/Morse/morse.wav')
    os.system("lame /home/dae/Documents/Projects/Morse/morse.wav /home/dae/Documents/Projects/Morse/morse.mp3")
    os.system("rm /home/dae/Documents/Projects/Morse/morse.wav")

if __name__ == '__main__':
    code = input("What do you want me to do? ").lower()
    code(code)