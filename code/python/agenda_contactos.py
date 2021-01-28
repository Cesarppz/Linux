import csv


class Contact:
    def __init__(self,name,phone,email):
        self.name  = name 
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._book = []

    def add(self,name,phone,email):
        conatcto = Contact(name,phone,email)
        self._book.append(conatcto)
        self._save()

    def show_all(self):
        for i in self._book:
            self._print_contact(i)
    
    def find(self,name):
        for contact in self._book:
            if name == contact.name:
                self._print_contact(contact)
                break
        else:
            print('\n'+'*' * 10)
            print('Contacto no encontrado ')
            print('\n'+'*' * 10)

    def delete(self,name):
        for indx,contact in enumerate(self._book):
            if name == contact.name:
                self._print_contact(contact)
                print('Se ha eliminado')
                print('*'* 30)
                del self._book[indx]
                self._save()
                break
            else :
                print('No se encuentra el contacto')

    def _save(self):
        with open('agenda.csv','w',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow( ('name','phone','email') ) # EScribo la cabezera 
            
            for contact in self._book:
                writer.writerow( (contact.name,contact.phone,contact.email) )
                    
    
    def _print_contact(self,contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')


def run():    
    contact_book = ContactBook()

    try:
        with open('agenda.csv','r',encoding='utf-8') as f:
            reader = csv.reader(f)
            for idx,row in enumerate(reader):
                if idx == 0:
                    continue
                if row == []:
                    continue
                contact_book.add(row[0],row[1],row[2])
    except FileExistsError as e:
        print(f'No existe el archivo {e}')


    while True:
        command = input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        ''').lower()

        if command == 'a' :
            name  = input('Ingresa el nombre ').lower().strip()
            email = input('Ingresa el email ').lower().strip()
            phone = input('Ingresa el teléfono ').lower().strip()
            contact_book.add(name,phone,email)
        
        elif command == 'l':
            contact_book.show_all()

        elif command == 'ac':
            del_name = input('ingresa el nombre del contacto a actualizar ').lower().strip()
            
            print('\n A continuación ingrese el los nuevos dats del contacto')
            new_name  = input('Ingresa el nombre ').lower().strip()
            new_email = input('Ingresa el email ').lower().strip()
            new_phone = input('Ingresa el teléfono ').lower().strip()
            print('\n')
            contact_book.delete(del_name)
            contact_book.add(new_name,new_phone,new_email)

        elif command == 'e':
            name_b = input('Ingrese el nombre del contacto que quiere elminar ').lower().strip()
            contact_book.delete(name_b)

        elif command == 'b':
            name_b = input('Que nombre estas buscando? ').lower().strip()
            contact_book.find(name_b)

        elif command == 's':
            print('Bye')
            break
        else:
            print('\n'+'-*-' * 5 + 'C O M A N D O   I N V A L I D O ' + '-*-' * 5)

if __name__ == '__main__':
    print('-*-' * 5 + 'B I E N V E N I D O ' + '-*-' * 5)
    run()

