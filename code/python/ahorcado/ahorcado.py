import random 


IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


list_sentences = 'profesor inglés orígenes humildes historia rechazos hecho acrecentar misterio convirtiéndose personajes reconocidos internamente occidente solamente éxito empresarial carisma irreverencia llevado orquestar algunos episodios mediáticos región años recientes cuando decidió encarnar convención anual descrito cierto detalle mencionado elogiosamente algunos artistas viajeros tuvieron oportunidad verlo palacio alcanzó auténtica reputación internacional hasta cuando apertura copiado contemplado público amplio entonces ofrecido diversas interpretaciones sintetizadas grandes corrientes realista cronológicamente primera defendida ponía acento fidelidad momento pintor anticipaba realismo fotografía valorando Édouard medios técnicos empleados publicación artículo dedicado librería inventario biblioteca poseía abrió camino nuevas interpretaciones carácter histórico empírico basadas reconocimiento intereses literarios científicos pintor presencia biblioteca pintor libros estimuló búsqueda variados significados ocultos contenidos simbólicos meninas última corriente interpretativa carácter filosófico nació posestructuralismo descartó iconografía significación prescindió datos históricos explicar estructura conocimiento espectador partícipe dinámico representación viaje deriva buque utilizado exploración calvario duró días barco equipo grupo formaba parte expedición imperial transantártica organizada comandada viaje deriva inició cuando durante vendaval buque rompió amarres estaba anclado estrecho aprisionado témpano hielo comenzó deriva impidió maniobrar siendo arrastrado aguas abiertas océano siempre encastrado témpano accidente dejó hombres expedición varados tierra escasos suministros principales encontraban barco'


def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print(hidden_word)


def sentence(list_o):
    sentence = random.choice(list_o)
    return list(sentence)


def organization(list_sentences):
    list_organized = list_sentences.lower().split(' ')
    return list_organized


def machine(list_sentences):
    tries = 0
    
    list_organized= organization(list_sentences)
    random_sentence = sentence(list_organized)
    #print(random_sentence)
    
    hidden_word = ['-']*len(random_sentence)
    
    while tries < 8 :

        display_board(hidden_word,tries)
        
        try:
            word = input(f'Escoge una letra 🤔 ')
            assert(len(word) == 1 ),'Solo puedes ingresar una letra a la vez'
        
        except AssertionError:
            print('\nSolo puedes ingresar una letra a la vez\n')
        
        box = []
        
        for i in range(len(random_sentence)) :
            if word == random_sentence[i]:
                box.append(i)
        
        if len(box) == 0:
            tries += 1

            if tries == 6:
                display_board(hidden_word,tries)
                lost_output = ''.join(random_sentence)
                print(f'Perdiste carnal. La palabra era {lost_output} 😔😔 ')
                break  

        else:
            for i in box:
                hidden_word[i] = word
            box  = [] 
            
        try:
            hidden_word.index('-')
        
        except ValueError:
            lost_output = ''.join(random_sentence)
            display_board(hidden_word,tries)
            print(f'Ganaste!! La palabra era {lost_output}')
            break


if __name__ == '__main__':
    
    print(f'\nBIENVENIDO AL JUEGO DEL AHORCADO\n')
    machine(list_sentences)
















        # display_board(hidden_word,tries)
        # if word == random_sentence[count_word]:
        #     display_board(hidden_word,tries,count_word + 1,random_sentence)
        #     count_word += 1
        #     word = input(f'Acertaste intenta la siguiente letra ')
            
        
        # elif word != random_sentence[count_word]:
        #     display_board(hidden_word,tries - 1,count_word,random_sentence)
        #     word = input(f'Intenta otra vez ')
        #     tries -= 1 
        
        # if count_word == (len(random_sentence) - 1):
        #     display_board(hidden_word,tries,count_word + 1,random_sentence)
        #     print('Ganaste ' + '*' * 10)
        #     break
