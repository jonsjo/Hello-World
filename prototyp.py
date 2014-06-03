# Title: Prototyp till P-Uppgift.
# Författare: Jonas Sjösvärd
# Datum: 2012-03-04
#
# Programet simulerar en tennis match om tre set.
# Användare väljer ut två spelare från en lista.
# Listan läses in från en fil.
# Slumpen får avgöra vem som vinner.
# När matchen är färdigspelad skall listan updateras.
# Spelare presenteras i vinst ordning.

import random

RESULTATRUBRIK = "Nr Namn       Vunna  Spelade  %Vunna\n"

# En klass som beskriver tennis spelare
# namn    : spelares namn
# vinster : antal vinster
# spelade : antal spelade matcher
class TennnisSpelare:
   # Konstructor, skapar spelare med data
   def __init__(self,namn,vinster,spelade,vinstproc):
      self.namn     = namn
      self.vinster  = vinster
      self.spelade  = spelade
      self.vinstproc = vinstproc

   # skriver ut spelar data
   def __str__(self):
      return (self.namn + self.vinster + self.spelade + self.vinstproc)

   # updaterar spelar data
   def uppdateraTennisSpelare(self,vinst):
      self.spelade+=1
      if vinst==True:
         self.vinster+=1
      self.vinstproc=self.vinster/self.spelade

# En klass som håller en lista med spelar
# object av klassen TennsisSpelare inlästa
# från text fil.
# spelare : lista med TennisSpelare objekt
class SpelarLista:
   # Konstructor
   def __init__(self,txtfil):
      self.lista = list()
      #self.lasInSpelareFranFil(txtfil)
      self.skapaSpelarLista(txtfil)
      
   # Las in spelare från fil och lägg i spelarlista    
   def skapaSpelarLista(self,text):
      index = 0
      while index < len(text):
         self.lista.append(TennnisSpelare(str(text[index]),
                        int(text[index+2]),
                        int(text[index+3]),
                        float(text[index+1])))
         index+=4
      
   # Skriv ut lista med spelare
   def skrivLista(self):
      self.sorteraSpelarLista()
      i=1
      res_txt = ""
      for l in self.lista:
         txt =""
         txt+= l.namn 
         txt+=str(l.vinster) + "\t"
         txt+=str(l.spelade) + "\t"
         txt+=str(round(l.vinstproc,2)) + "\t"
         txt = txt.replace("\n","\t")
         txt = str(i) + " " + txt
         res_txt += txt + "\n"
         i+=1
      return res_txt

   # Skriv ut lista med spelare
   def skrivListaText(self):
      self.sorteraSpelarLista()
      i=1
      res_txt = ""
      for l in self.lista:
         txt =""
         txt+= l.namn + "\t"
         txt+=str(l.vinster) + "\t"
         txt+=str(l.spelade) + "\t"
         txt+=str(round(l.vinstproc,2)) + "\t"
         txt = txt.replace("\n","\t")
         txt = str(i) + " " + txt
         res_txt += txt + "\n"
         i+=1
      return res_txt

   

   # Las in spelare från fil och lägg i spelarlista    
   def lasInSpelareFranFil(self,txtfil):
      self.file = open(txtfil, 'r', encoding='iso-8859-1')
      self.text = []
      for line in self.file:
         self.text.append(line)         
      self.file.close()
   
   # Spela match med två spelare
   def spelaMatch(self,spelare1,spelare2):
      temp = [spelare1,spelare2]
      res  = random.choice(temp)
      if (res==spelare1):
         vinnare   = self.lista[spelare1-1]
         forlorare = self.lista[spelare2-1]
      else:
         forlorare = self.lista[spelare1-1]
         vinnare   = self.lista[spelare2-1]  
      return vinnare, forlorare
      
   # Sortera spelarlista
   def sorteraSpelarLista(self):
      self.lista.sort(key = lambda x:x.vinstproc)
      self.lista.reverse()

   # Antal spelare i lista
   def antalSpelare(self):
      return len(self.lista)

   # Resultat av spelad match
   def resultSpeladMatch(self,vinst,forlust):
      txtResInfo  = ""
      txtResInfo  = (self.lista[vinst-1].namn + " mot " + \
                     self.lista[forlust-1].namn).replace("\n","") + "\n"
      txtResInfo += (self.lista[vinst-1].namn + " vann!!!").replace("\n","")
      return txtResInfo

   # Returnerar inmatade spelare
   def txtSpelare(self,spelare_1,spelare_2):
      txtResInfo  = ""
      txtResInfo  = (self.lista[spelare_1-1].namn + " mot " + \
                     self.lista[spelare_2-1].namn).replace("\n","") + "\n"     
      return txtResInfo

# Spela tennis match med två spelare
def spelaTennisMatch(spelare1,spelare2):
   temp = [spelare1,spelare2]
   res  = random.choice(temp)
   if (res==spelare1):
      vinnare   = spelare1
      forlorare = spelare2
   else:
      forlorare = spelare1
      vinnare   = spelare2
   return vinnare, forlorare

# Las in spelare från fil och lägg i spelarlista    
def lasInTextFranFil(txtfil):
   text = []
   res  = False
   try:
      file = open(txtfil, 'r', encoding='iso-8859-1')   
      for line in file:
         text.append(line)         
      file.close()
      res = True
   except:
      text = []
      
   return res, text

# Kollar att värden är rimliga
# Retunerar true för rimliga värden,
# annars false
def rimligaVarden(text):
   res = False
   index = 0
   while index < len(text):
      try:
         res = (text[index]).replace(' ','').replace('\n','').isalpha()
         if int(text[index+2]) < 0:
            res = False
         if int(text[index+3]) < 0:
            res = False
         if float(text[index+1]) < 0.0 or 1.0 < float(text[index+1]):
            res = False
         index+=4
      except:
         res = False
         break
   return res
      
         
# Om module exeveras enskilt, ej anropas
# Exeveras rader efter if sats
if __name__ == '__main__':
   
# Huvuprogram med meny, kommando basserat.
# Spelar lista samt inmatning av två spelare
# eller avslut av program skall vara möjlig.

# Spelar lista skapas

   #kontroll av att fil finns
   resfil, txt = lasInTextFranFil('spelare.txt')

   #kontroll av rimliga värden
   resvarden = rimligaVarden(txt)
   
   if resfil and resvarden:
       spelarlista = SpelarLista(txt)

   while resfil and resvarden:
      print("*************  Tennis  *************")
      print(RESULTATRUBRIK)
      print(spelarlista.skrivLista())
      print("**  Välj två spelare med deras    **")
      print("**  nummer för att spela match.   **")
      print("Ej giltigt val avslutar programmet:")

      try:
         spelare1 = int(input("Mata in första spelarens nummer :"))         
         if not(0 < spelare1 <= spelarlista.antalSpelare()):
            raise
         spelare2 = int(input("Mata in andra spelarens nummer  :"))
         if not(0 < spelare2 <= spelarlista.antalSpelare()):
            raise
         if (spelare1==spelare2):
            raise         
         vinst, forlust = spelaTennisMatch(spelare1,spelare2)
         print(spelarlista.resultSpeladMatch(vinst,forlust))
         print()
         spelarlista.lista[vinst-1].uppdateraTennisSpelare(True)
         spelarlista.lista[forlust-1].uppdateraTennisSpelare(False)
      except:
         print("Program avslutat !!")
         break
   else:
      if not(resfil):
         print("Text fil kunde ej hittas eller öppnas!")
      elif not(resvarden):
         print("Text fil innehåller ej rimliga värden!")
      print("Program avbrytes!")
         
         
