
class Lamp:
    _Lamp = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self):
        self.is_tuned_on = False 

    def turn_on(self):
        self.is_tuned_on = True
        self._image_display()
    
    def turn_off(self):
        self.is_tuned_on = False 
        self._image_display()

    def _image_display(self):
        if self.is_tuned_on == True:
            print(self._Lamp[0])
        else :
            print(self._Lamp[1])

def run():
    lamp = Lamp()

    while True:
        res = input('Welcome to Lampara \n [e] to turn on the lamp \n [a] to turn off the lamp \n [s] to exit \n ').lower()

        if res == 'e':
            lamp.turn_on()
        elif res == 'a':
            lamp.turn_off()
        else :
            print('Adiós papu ')

if __name__ == '__main__':
    run()
