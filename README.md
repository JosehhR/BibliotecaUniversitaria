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

### Clase Libro 📖
```python
class Book:
    def __init__(self, titulo, categoria):
        self._titulo = titulo
        self._categoria = categoria

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, v):
        if isinstance(v, str):
            self._titulo = v
        else:
            raise TypeError("El título debe ser de tipo string")

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, v):
        if isinstance(v, str):
            self._categoria = v
        else:
            raise TypeError("La categoría debe ser de tipo string")
```

### Clase Usuario 👤
```python
class User:
    def __init__(self, nombre, edad, carrera):
        self._nombre = nombre
        self._edad = edad
        self._carrera = carrera

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, v):
        if isinstance(v, str):
            self._nombre = v
        else:
            raise TypeError("La propiedad nombre debe ser de tipo string")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, v):
        if isinstance(v, int):
            self._edad = v
        else:
            raise TypeError("La propiedad edad debe ser de tipo entero")

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, v):
        if isinstance(v, str):
            self._carrera = v
        else:
            raise TypeError("La propiedad carrera debe ser de tipo string")
```

---

## 📌 Casos de Uso

A continuación, algunos ejemplos de cómo podría usarse el simulador:

### 1. Registrar usuarios en la biblioteca
```python
libreria = Library()

libreria.addUser("Ana Gómez", 20, "Ingeniería")
libreria.addUser("Luis Torres", 22, "Derecho")

print("Usuarios registrados:")
for u in libreria.seeUsers():
    print(f"Nombre: {u.nombre}, Edad: {u.edad}, Carrera: {u.carrera}")
```

**Salida esperada:**
```
Usuarios registrados:
Nombre: Ana Gómez, Edad: 20, Carrera: Ingeniería
Nombre: Luis Torres, Edad: 22, Carrera: Derecho
```

---

### 2. Agregar libros al catálogo
```python
libreria.addBook("Cálculo Integral", "Matemáticas")
libreria.addBook("Introducción al Derecho", "Derecho")

print("\nCatálogo de libros:")
for b in libreria.seeBooks():
    print(f"Título: {b.titulo}, Categoría: {b.categoria}")
```

**Salida esperada:**
```
Catálogo de libros:
Título: Cálculo Integral, Categoría: Matemáticas
Título: Introducción al Derecho, Categoría: Derecho
```

---

### 3. Validación de tipos de datos
El uso de **properties** asegura que se ingresen datos correctos:
```python
try:
    libreria.addUser("Pedro", "veinte", "Ingeniería")
except TypeError as e:
    print("Error:", e)
```

**Salida esperada:**
```
Error: La propiedad edad debe ser de tipo entero
```

---

### 4. Visualizar listas completas
```python
print("Usuarios:", libreria.seeUsers())
print("Libros:", libreria.seeBooks())
```

Esto permite ver todas las instancias registradas.

---

✅ Con estos casos de uso se demuestra la creación de objetos, encapsulamiento y manejo básico de operaciones típicas en una biblioteca universitaria.

---

## 🛠️ Tecnologías Usadas
- **Lenguaje:** Python 3.12  
- **Paradigma:** Programación Orientada a Objetos (POO)  
- **Entorno de desarrollo:** VS Code / Terminal de Python  
- **Control de versiones:** Git y GitHub para almacenar y versionar el proyecto  

---

## 💡 Notas para el Futuro
- Evitar mezclar **nombres en inglés y español** en el código. Esto mejora la **legibilidad**, la **consistencia** y facilita la colaboración con otros desarrolladores.  
