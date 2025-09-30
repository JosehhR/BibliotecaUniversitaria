# Simulador de Operaciones Basicas de Una Biblioteca Universitaria

## 🎯Objetivo
Implemente un simulador de operaciones básicas de una biblioteca universitaria, diseñando e implementando las clases y conceptos vistos en clase (encapsulamiento, instanciación, atributos, objetos, etc.) que considere pertinentes.
## ✅Requerimientos
<img width="563" height="196" alt="Diseño sin título" src="https://github.com/user-attachments/assets/09e6aeb5-699d-4000-852f-9ac08e6aa420" />  

## Clases Utilizadas

### Clase Libreria 📚
````python
class Library:
    def __init__(self):
        self._catalogo = []
        self._usuarios = []
        pass

    def addUser(self, n, e, c):
        u=User(n,e,c)
        self._usuarios.append(u)

    def addBook(self, t, cat):
        b=Book(t, cat)
        self._catalogo.append(b)

    def seeUsers(self):
        return tuple(self._usuarios)

    def seeBooks(self):
        return tuple(self._catalogo)
````
La clase libreria posee dos atributos los cuales son:  
**1._catalogo:** un atributo destinado a guardar objetos de clase **Libro** 
**2._usuarios:** un atributo destinado a guardar objetos de clase **Usuario** 
y por otro lado, posee 4 metodos para administar estos atributos:
**1.addUser:** que recibe 3 variables, **n** para el nombre del usuario, **e** para la edad del usuario, y **c** para la carrera de este. Usando estos tres, crea un objeto de clase **Usuario** y lo agrega a **_usuarios**
**2.addBook:** que recibe 2 variables, **t** para el titulo de este y **cat** para la categoria del libro. Usando estos tres, crea un objeto de clase **Libro** y lo agrega a **_catalogo**
**3.seeUsers:** que regresa una tupla del atributo **_usuarios**
**4.seeBooks** que regresa una tupla del atributo **_libros**
