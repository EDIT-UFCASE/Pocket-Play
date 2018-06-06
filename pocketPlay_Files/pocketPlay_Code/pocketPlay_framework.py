#This is the framework for pocketPlay

#initialization happens here
import os


#Reads audio input and chooses job accordingly
def readJobIntent():
    audioIn = str(snips.intent.firstTerm)  #This will be the audio input variable

    #Different Job slots
    if (audioIn == "firefighter"):
        firefighter()

    else if (audioIn == "doctor"):
        doctor()

    else if (audioIn == "vet"):
        vet()

    else if (audioIn == "astronaut"):
        astronaut()    

    else:
        print "Unavailable job intent"  ##Output "I didn't understand or unavailable job" audio
        


def firefighter():

    #Audio Out Test
    os.system("aplay ./firefighter_firealarm.wav") #INPUT FILE LOCATION AFTER RUN COMMAND
    
    ##Play "What job role do you want to be" audio
    
    audioIn = False

    
    #Different job roles
    if (audioIn == "truck"):
        pass
    if (audioIn == "fire"):
        pass
    if (audioIn == "station"):
        pass
    else:
        pass#Return to readJobIntent(Home)



def doctor():

    os.system("aplay ./doctor_cardiogram-beats.wav") #INPUT FILE LOCATION AFTER RUN COMMAND
    
    ##Play "What job role do you want to be" audio
    
    audioIn = False

    
    #Different job roles
    if (audioIn == "surgery"):
        pass
    if (audioIn == "heal"):
        pass
    if (audioIn == "ambulance"):
        pass
    else:
        pass#Return to readJobIntent(Home)


        
def vet():

    os.system("aplay ./vet_dogbark.wav") #INPUT FILE LOCATION AFTER RUN COMMAND
    
    ##Play "What job role do you want to be" audio
    
    audioIn = False

    
    #Different job roles
    if (audioIn == "dog"):
        pass
    if (audioIn == "cat"):
        pass        
    if (audioIn == "fish"):
        pass
    else:
        pass#Return to readJobIntent(Home)

def astronaut():

    os.system("aplay ./astronaut_blaster.wav") #INPUT FILE LOCATION AFTER RUN COMMAND
    
    ##Play "What job role do you want to be" audio
    
    audioIn = False

    
    #Different job roles
    if (audioIn == "dog"):
        pass
    if (audioIn == "cat"):
        pass        
    if (audioIn == "fish"):
        pass
    else:
        pass#Return to readJobIntent(Home)

readJobIntent()
