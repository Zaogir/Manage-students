```python
from institut import *
    
carregarDadesAlumne = input("Vols carregara les dades desde un archiu (Si/No): ")
if carregarDadesAlumne == "Si":
    format = input("Quin format vols carregar les dades (json/bin): ")
    carregarArchius(format)

while True:
    print("1. Nou alumne")
    print("2. Nova materia")
    print("3. Afegir alumne a materia")
    print("4. Desmatricula el alumne")
    print("5. Mostrar les notes de un alumne")
    print("6. Posar la nota del alumne")
    print("7. Mostrar les notes de una materia")
    print("8. Eliminar una materia")
    print("9. Eliminar un alumne")
    print("10. Guardar el estat de la base de dades")
    print("11. Sortir")

    opcio = input("Escull una opció: ")

    if opcio == "1":
        alumne = nouAlumne()
        afegirAlumne(alumne)
    elif opcio == "2":
        materia = novaMateria()
        afegirMateria(materia)
    elif opcio == "3":
        codiAlumne = input("Codi del Alumne que vols matricular: ")
        codiMateria = input("Codi de la Materia on el vols matricular: ")
        matriculaAlumne(codiAlumne,codiMateria)
    elif opcio == "4":
        codiAlumne = input("Codi del Alumne que vols desmatricular: ")
        codiMateria = input("Codi de la Materia on el vols desmatricular: ")
        desmatriculaAlumne(codiAlumne,codiMateria)
    elif opcio == "5":
        codiAlumne = input("Codi del Alumne que vols comprovar les seves notes: ")
        mostrarNotesAlumne(codiAlumne)
    elif opcio == "6":
        codiAlumne = input("Codi del Alumne que li vols posar nota: ")
        codiMateria = input("Codi de la Materia on el vols posar la nota: ")
        nota = int(input("Quina nota tindra el alumne: "))
        posarNota(codiAlumne,codiMateria,nota)
    elif opcio == "7":
        codiMateria = input("Codi de la Materia on vols mirar les notes: ")
        mostrarNotesMateria(codiMateria)
    elif opcio == "8":
        codiMateria = input("Codi de la Materia que vols eliminar: ")
        eliminarMateria(codiMateria)
    elif opcio == "9":
        codiAlumne = input("Codi del Alumne que vols eliminar: ")
        eliminarAlumne(codiAlumne)
    elif opcio == "10":
        format = input("Quin format vols guardar les dades que tens (json/bin): ")
        creaArchius(format)
    elif opcio == "11":
        break
    else:
        print("La opcio que has posat no es valida.")
```
