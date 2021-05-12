def SoundEx():  #requests an input for a decibel level (dB), and returns a common noise for comparison.
    dB = int(input("Type in the decible level"))
    if dB == 130:
    	print (dB,"decibles is the same volume as a jackhammer.")
    if dB > 130:
        print (dB,"is", (dB - 130), "decibles louder than a jackhammer.")
    if dB == 106:
    	print (dB, "decibles is the same volume as a gas lawnmower.")
    if 106 < dB < 130:
    	print (dB, "decibles has a volume between the volume of a gas lawnmower and the volume of a jackhammer.")
    if dB == 70:
    	print (dB, "decibles is the same volume as an alarm clock.")
    if 70 < dB < 106:
    	print (dB, "decibles has a volume between the volume of an alarm clock and the volume of a gas lawnmower")
    if dB == 40:
    	print (dB, "decibles is the same volume as a quiet room.")
    if 40 < dB < 70:
    	print (dB, "decibles has a volume between the volume of a quiet room and the volume of an alarm clock")
    if dB < 40:
        print (dB, "is", (40 - dB), "decibles quieter than a quietroom.")
        
SoundEx()         
