""" Practice with parent and child classes """

# Parent class Bicycle and its attributes
class Bicycle:
    brand = ''
    size = ''
    frameMaterial = ''
    speed = ''
    wheelSize = ''

# Child classe and its added attributes
class Road(Bicycle):
    handlebarType = ''
    pedalType = ''

# Child class and its added attributes
class fullSuspension(Bicycle):
    forkSuspension = ''
    frameSuspension = ''
    dropperPost = False
    suspensionType = ''
    
