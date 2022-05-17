class Mamifero:
    def __init__(self,especie, esperanza_vida, cantidad_mamas):
        
        self.cantidad_mamas = cantidad_mamas
        self.esperanza_vida = esperanza_vida
        self.especie = especie
    def __str__(self) :
        
        if self.cantidad_mamas == 1 :
            return f"Soy {self.especie}, por lo tanto soy  {type(self).__qualname__} vivo al rededor de  {self.esperanza_vida} años y tengo {self.cantidad_mamas} glandula mamaria"
        else: 
            return f"Soy {self.especie}, entonces soy {type(self).__qualname__} vivo al rededor de  {self.esperanza_vida} años y tengo {self.cantidad_mamas} glandulas mamarias"
    def nacer(self):
        return f"{self.especie} Ha tenido una cria"
    
    def mamar(self):
        return f"{self.especie} Esta amamantando"
    
    
class AnimalMarino:
    habitat = "Acuático"
    def __init__(self, especie, branqueas) :
        
        self.branqueas = branqueas
        self.especie = especie
        
    def __str__(self) :
        return f"Soy {self.especie}, por ende soy {type(self).__name__} y {self.habitat}"
        
        
    def nadar(self):
        return f"{self.especie} esta nadando"

class Cetaceo(Mamifero,AnimalMarino): 
    
    def __init__(self, especie, esperanza_vida, peso) :
        Mamifero.__init__(self, especie, esperanza_vida, cantidad_mamas=1) 
        self.habitat = AnimalMarino.habitat                             
        self.peso = peso

    def __str__(self) :
        
        return f"{Mamifero.__str__(self)}, tambien soy {self.habitat} por lo tanto soy {AnimalMarino.__name__}"
    
delfin = Cetaceo("delfin", 50, 3000)
print(delfin.cantidad_mamas)  
print(delfin)
print(delfin.nacer()) 
print(delfin.nadar())

cachalote= AnimalMarino(" cachalote",True)
print( cachalote)

perro = Mamifero("perro",20,6)
print(perro)