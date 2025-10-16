#Autor: Jose Luis Ramirez
#Este codigo presenta un simulador de biblioteca universitaria, la finalidad de el es la realizacion del parcial de POO

class Library:
    def __init__(self):
        self._catalogo = []
        self._users = []
        pass

    def addUser(self, n, e, c):
        u=User(n,e,c)
        self._users.append(u)

    def regUser(self):
        print("-------------------------------------------------------------")
        n=(input("Ingrese su nombre: "))
        e=int(input("Ingrese su edad: "))
        c=(input("Ingrese su carrera: "))
        self.addUser(n,e,c)
        print("-------------------------------------------------------------")
        print(f"Usuario {n} registrado con exito!")
        print("-------------------------------------------------------------")

    def addBook(self, t, cat):
        b=Book(t, cat)
        self._catalogo.append(b)

    def regBook(self):
        print("-------------------------------------------------------------")
        t=(input("Ingrese el titulo del libro: "))
        opc=0
        while(opc<1 or opc>3):
            print("Seleccione la categoria:\n1. Calculo\n2. Literatura\n3. Ciencia")
            opc=int(input())
            match(opc):
                case 1:
                    c="Calculo"
                case 2:
                    c="Literatura"
                case 3:
                    c="Ciencia"
        self.addBook(t,c)
        print("-------------------------------------------------------------")
        print (f"El libro {t} ha sido registrado con exito!")
        print("-------------------------------------------------------------")

    def getUsers(self):
        return tuple(self._users)

    def showUsers(self):
        usuarios=self.getUsers()
        print("-------------------------------------------------------------")
        if(len(usuarios)==0):
            print("Aun no hay usuarios registrados!")
            print("-------------------------------------------------------------")
        else:
            for n in range(len(usuarios)):
                obj=usuarios[n]
                print(f"{n+1}\nNombre: {obj.nombre}\nEdad: {obj.edad}\nCarrera: {obj.carrera}")
                print("-------------------------------------------------------------")

    def getBooks(self):
        return tuple(self._catalogo)
    
    def showBooks(self):
        libros=self.getBooks()
        print("-------------------------------------------------------------")
        if(len(libros)==0):
            print("Aun no hay libros registrados!")
            print("-------------------------------------------------------------")
        else:
            opc=0
            cat=""
            while(opc<1 or opc>4):
                print("Que categoria de libros quiere ver?:\n1. Calculo\n2. Literatura\n3. Ciencia\n4. Todos")
                print("-------------------------------------------------------------")
                opc=int(input())
                print("-------------------------------------------------------------")
                match(opc):
                    case 1:
                        cat="Calculo"
                    case 2:
                        cat="Literatura"
                    case 3:
                        cat="Ciencia"
                    case 4:
                        cat=False
            if(cat==False):
                for n in range(len(libros)):
                    obj=libros[n]
                    print(f"{n+1}\nTitulo: {obj.titulo}\nCategoria: {obj.categoria}")
                    print("-------------------------------------------------------------")
            else:
                librosN=[]
                for n in range(len(libros)):
                    obj=libros[n]
                    if(libros[n].categoria==cat):
                        librosN.append(libros[n])
                if(len(librosN)==0):
                    print("Aun no hay libros registrados con esa categoria!")
                    print("-------------------------------------------------------------")
                else:
                    for n in range(len(librosN)):
                        obj=librosN[n]
                        print(f"{n+1}\nTitulo: {obj.titulo}\nCategoria: {obj.categoria}")
                        print("-------------------------------------------------------------")

    def showMenu(self):
        opc=0
        print("-------------------------------------------------------------")
        print("Bienvenido a la biblioteca universitaria!")
        print("-------------------------------------------------------------")
        while(opc<1 or opc>5):
            print("Seleccione una opcion: \n1.Registrar un Usuario\n2.Registrar un libro\n3.Ver usuarios\n4.Ver libros\n5.Salir")
            print("-------------------------------------------------------------")
            opc=int(input())
            match(opc):
                case 1:
                    self.regUser()
                    opc=0
                case 2:
                    self.regBook()
                    opc=0
                case 3:
                    self.showUsers()
                    opc=0
                case 4:
                    self.showBooks()
                    opc=0
                case 5:
                    return
        
class Book:
    def __init__(self, titulo, categoria):
        self._titulo=titulo
        self._categoria=categoria
        pass

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, v):
        if(type(v)==str):
            self._titulo=v
        else:
            raise TypeError("La propiedad titulo debe ser de tipo string")
        
    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, v):
        if(type(v)==str):
            self._categoria=v
        else:
            raise TypeError("La propiedad categoria debe ser de tipo string")

class User:
    def __init__(self, nombre, edad, carrera):
        self._edad=edad
        self._carrera=carrera
        self._nombre=nombre
        pass

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, v):
        if(type(v)==str):
            self._nombre=v
        else:
            raise TypeError("La propiedad nombre debe ser de tipo string")
        
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, v):
        if(type(v)==int):
            self._edad=v
        else:
            raise TypeError("La propiedad edad debe ser de tipo entero")
        
    @property
    def carrera(self):
        return self._carrera
    @carrera.setter
    def carrera(self, v):
        if(type(v)==str):
            self._=v
        else:
            raise TypeError("La propiedad nombre debe ser de tipo string")

def main():
    lib=Library()
    lib.showMenu()

if __name__ == "__main__":
    main()