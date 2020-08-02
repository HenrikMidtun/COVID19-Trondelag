'''
    Lage en enkel QT applikasjon som viser
        Trondheim
        #Antall smittede
        #Døde
        #Sist oppdatert
    #Horisontalt løpende liste med data fra andre steder i trøndelag
'''
from view import App
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display, use -> 0.0')
    os.environ.__setitem__('DISPLAY',':0.0')

app = App()
