```python
import json
import pickle
from os.path import exists



#Variables Globals
#alumnes és un diccionari que tindrà com a Key el codi de l'alumne, i com a Value al propi alumne
alumnes={}
#materies és un diccionari que tindrà com a Key el codi de la materia i com a value la pròpia matèria
materies={}


#Classes
class Alumne:
    def __init__(self,Codi:str,Nom:str,Cognom:str,DataNaixement:str,Materies:dict):
        self.Codi=Codi
        self.Nom=Nom
        self.Cognom=Cognom
        self.DataNaixement=DataNaixement
        #self.Materies és un diccionari que tindrà com a Key el codi de MAtèria, i com a value la nota que ha tret l'alumnes de la matèria
        self.Materies = Materies
class Materia:
    def __init__(self,Codi:str,Nom:str,Alumnes:list):
        self.Codi=Codi
        self.Nom=Nom
        #self.Alumnes és una llista que contindrà els alumnes que estan matriculats de cada matèria. Han de ser els alumnes(Clss Alumne), no els codis d'alumnes
        self.Alumnes=Alumnes


def object_to_json(obj):
    dades = json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True,indent=4)
    return dades


def nouAlumne():
    #Ha de demanar les dades d'un alumne, crea-lo i retornar una variable de la classe Alumne
    codi = input("Codi: ")
    nom = input("Nom: ")
    cognom = input("Cognom: ")
    datanaixement = input("Data Naixement: ")
    materies={}
    alu =  Alumne(codi,nom,cognom,datanaixement,materies)
    return alu

def novaMateria():
    #Ídem anterior però amb materia
    codi = input("Codi de la materia: ")
    nom = input("Nom de la materia: ")
    alumnes=[]
    mater = Materia(codi,nom,alumnes)
    return mater

def afegirAlumne(a:Alumne):
    #Afegirà l'alumne a al diccionari alumnes
    if a.Codi not in alumnes:
        alumnes[a.Codi]=a
    else:
        print("\nEl alumne ja esta dintre\n")

def afegirMateria(m:Materia):
    #Afegirà la materia m al diccionaru materies
    if m.Codi not in materies:
        materies[m.Codi]=m
    else:
        print("\nLa materia ja esta dintre\n")


def eliminarAlumne(codiAlumne:str):
    #Elimina del diccionary alumnes, l'alumne que té com a codi codiAlumne
    #Ha de eliminar-lo també de totes les materies que estigui matriculat7
    if codiAlumne in alumnes:
        a = alumnes[codiAlumne]
        for codiMateria in a.Materies:
            if codiMateria in materies:
                m = materies[codiMateria]
                for alumne in m.Alumnes:
                    if alumne['Codi'] == codiAlumne:
                        m.Alumnes.remove(alumne)
        del alumnes[codiAlumne]
        print(f"\nL'alumne {codiAlumne} s'ha eliminat correctament.\n")
    else:
        print(f"\nL'alumne {codiAlumne} no existeix.\n")


def eliminarMateria(codiMateria:str):
    #Eliminar la materia amb codiMateria del diccionari materies,
    #i també del diccionari a.materies de tots els alumnes que estaven matriculats d'aquella matèria
    if codiMateria in materies:
        m = materies[codiMateria]
        for alumne in m.Alumnes:
                a = alumnes[alumne['Codi']]
                a.Materies.pop(codiMateria)
        del materies[codiMateria]
        print(f"\nLa materia {codiMateria} s'ha eliminat correctament.\n")
    else:
        print("\nLa materia no existeix.\n")


def matriculaAlumne(codiAlumne:str,codiMateria:str):
    #agafarà l'alumne a, que té com a codi codiAlumne del dicc alumnes
    #agafarà la materia m, que té com a codi codiMateria del dicc materies
    #afegirà el coidiMateria a alumne a, per tant, l'afegirà al diccionai a.Materies, amb value buit, el value serà la nota
    #afegirà l'alumne a la materia m, l'afegirà a la llista m.Alumnes
    #Tot l'anterior sempre comprovant que existeixen l'alumne i la materia
    if codiAlumne in alumnes and codiMateria in materies:
        a = alumnes[codiAlumne]
        m = materies[codiMateria]
        a.Materies[codiMateria] = None
        m.Alumnes.append(a)
        print(f"\nL'alumne {codiAlumne} se a matriculat correctament.\n")
    else:
        print("\nRevisa bé les dades, pot ser que alguna dada no estigui correcte.\n")

def desmatriculaAlumne(codiAlumne:str,codiMateria:str):
    #Ha de fer el contrari que el métode anterior
    if codiAlumne in alumnes and codiMateria in materies:
        a = alumnes[codiAlumne]
        m = materies[codiMateria]
        del a.Materies[codiMateria]
        for alumne in m.Alumnes:
                    if alumne['Codi'] == codiAlumne:
                        m.Alumnes.remove(alumne)
        print(f"\nL'alumne {codiAlumne} se a desmatriculat correctament.\n")
    else:
        print("\nRevisa bé les dades, pot ser que alguna dada no estigui correcte\n")

def estaMatriculat(codiAlumne:str,codiMateria:str):
    #retornarà True si l'alumne ja està matriculat de la materia i false sinó està matriculat
    if codiAlumne in alumnes and codiMateria in materies:
        a = alumnes[codiAlumne]
        if codiMateria in a.Materies:
            return True
        else:
            return False

#Obtenim el alumne.       
def obtenirAlumne(codiAlumne,codiMateria):
    m = materies[codiMateria]
    for alumne in m.Alumnes:
        if alumne['Codi'] == codiAlumne:
            return alumne
    return None

def posarNota(codiAlumne:str,codiMateria:str,nota:int):
    #Servirà per posar nota a l'alumne a
    #Comprovarà que l'alumne està matriculat de la materia, i després li possarà nota
    # a[codiMateria]=nota
    a = alumnes[codiAlumne]
    if estaMatriculat(codiAlumne,codiMateria):
        a.Materies[codiMateria] = nota
        alumne = obtenirAlumne(codiAlumne,codiMateria)
        if alumne is not None:
            alumne['Materies'][codiMateria] = nota
        print(f"\nSe a posat la nota a l'alumne {codiAlumne} en la materia {codiMateria} correctament.\n")
    else:
        print(f"\nL'alumne {codiAlumne} no esta matriculat en {codiMateria}\n")

            

def mostrarNotesMateria(codiMateria:str):
    #Li passarem el codi d'una Matèria i ens mostrarà per pantalla un llistat amb les següents columnes:
    #Nom Materia    CodiAlumne  NomAlumne Nota
    #Si l'alumne no té nota, mostrarà 2 guionets --
    if codiMateria in materies:
        m = materies[codiMateria]
        print(f"{'Nom Materia':20}{'Codi Alumne':20}{'Nom Alumne':20}{'Nota':4}")
        print("-"*64)
        for alumne in m.Alumnes:
            print(f"{m.Nom:20}{alumne['Codi']:20}{alumne['Nom']:20}{alumne['Materies'][codiMateria] if alumne['Materies'][codiMateria] is not None else '--':4}")
    else:
        print("\nLa materia no existeix\n")

def mostrarNotesAlumne(codiAlumne:str):
    #Li passarem el codi d'un alumne i ens mostrarà per pantalla un llistat amb les següents columnes:
    #Nom Materia  Nota
    #Si l'alumne no té nota, mostrarà 2 guionets --
    if codiAlumne in alumnes:
        a = alumnes[codiAlumne]
        print(f"{'Nom Materia':20}{'Nota':5}")
        print("-"*25)
        for materia in a.Materies:
            print(f"{materies[materia].Nom:20}{a.Materies[materia] if a.Materies[materia] is not None else '--':5}")   
    else:
        print("\nEl alumne no existeix\n")


def creaArchius(format:str):
    dadesJasonAlumne = {x:object_to_json(alumnes[x]) for x in alumnes}
    dadesJasonMateria = {x:object_to_json(materies[x]) for x in materies}
    if format == "json":
        with open("./alumnes.json","w") as alumnesJson:
            json.dump(dadesJasonAlumne,alumnesJson)
        with open("./materies.json","w") as materiesJson:
            json.dump(dadesJasonMateria,materiesJson)
        print("\nL'archiu de Json se ha creat correctament.\n")
    elif format == "bin":
        with open("./alumnes.pkl","wb") as alumnesBinari:
            pickle.dump(alumnes,alumnesBinari)
        with open("./materies.pkl","wb") as materiesBinari:
            pickle.dump(materies,materiesBinari,-1)
            print("\nL'archiu Binari se ha creat correctament.\n")
    else:
        print("Format no valid. Nomes pot ser 'json' o 'bin'.")

def carregarArchius(format:str):
    if format == "json":
        if exists('./alumnes.json') and exists('./materies.json'):
            with open("./alumnes.json","r") as alumnesJson, open("./materies.json","r") as materiesJson:
                dadesAlumne = json.load(alumnesJson)
                dadesMateria = json.load(materiesJson)
                for codiM, dadesM in dadesMateria.items():
                    materiaJson = json.loads(dadesM)
                    codi = materiaJson["Codi"]
                    nom = materiaJson["Nom"]
                    alumne = materiaJson["Alumnes"]
                    materies[codiM] = Materia(codi, nom, alumne)
                for codiA, dadesA in dadesAlumne.items():
                    alumneJson = json.loads(dadesA)
                    codi = alumneJson["Codi"]
                    nom = alumneJson["Nom"]
                    cognom = alumneJson["Cognom"]
                    dataNaixement = alumneJson["DataNaixement"]
                    materia = alumneJson["Materies"]
                    alumnes[codiA] = Alumne(codi, nom, cognom, dataNaixement, materia)               
                print("\nL'archiu de json se ha exportat correctament al programa\n")   
        else:
            print("\nNo existeix cap json per carregar les dades\n")
        
    if format == "bin":
        if exists('./alumnes.pkl') and exists('./materies.pkl'):
            with open("./alumnes.pkl","rb") as alumnesBinari, open("./materies.pkl","rb") as materiesBinari:
                dadesAlumne = pickle.load(alumnesBinari)
                dadesMateria = pickle.load(materiesBinari)
                for codiM, dadesM in dadesMateria.items():
                    materies[codiM] = dadesM
                for codiA, dadesA in dadesAlumne.items():
                    alumnes[codiA] = dadesA
                print("\nL'archiu binari se ha exportat correctament al programa\n")   
        else:
            print("\nNo existeix cap arxiu binari per a carregar les dades\n")
```
