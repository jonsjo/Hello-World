# Title: Prototypwin till P-Uppgift.
# Författare: Jonas Sjösvärd
# Datum: 2012-03-04
#
# Programet simulerar en tennis match om tre set.
# Användare väljer ut två spelare från en lista.
# Listan läses in från en fil.
# Slumpen får avgöra vem som vinner.
# När matchen är färdigspelad skall listan updateras.
# Spelare presenteras i vinst ordning.

# En klass som beskriver tennis spelare
# namn    : spelares namn
# vinster : antal vinster
# spelade : antal spelade matcher

from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from prototyp import *
from gamefunc import *

# Huvuprogram GUI basserat:
# 
# Spelar lista visas inmatning av två spelare kan göras,
# där efter sker spel av match.
# Hjäp och info fås via dialog ruta
# Avslut av program genom att sänga fönster.


#visar hjälp text vid anrop
def spelaHjalpInfo():
   hjalptext = "Spela Match:\n" + \
               "Tryck på knapp och två spelare skall där efter väljas.\n" + \
               "Två korrekta val måste göras, hälptext fås i respektive dialog.\n" + \
               "Meddelade ruta med resultat fås efter att match har spelats.\n" + \
               "Resultat lista updateras efter att resultat bekräftats.\n\n" + \
               "Hjälp & info:\n" + \
               "Tryck på knapp denna text du läser fås som användar hjälp.\n\n" + \
               "Avslut:\n" + \
               "Sker genom att trycka i kryssruta, övre hörnet.\n" + \
               "Kan ej ske under inmatning eller bekräftelse.\n"
               
   messagebox.showinfo(message=hjalptext, title='Hjälp & info', icon='info')     

def spelaXtra():
   print("spelaXtra ",dummy.get())
   dummy.set(dummy.get()+1)
   
#match spelas vid anrop      
def spelaMatch():
   #spelare 1
   spelarval1 = []
   spelarval1 = (range(1,(spelarlista.antalSpelare()+1)))
   spelare1 = 0
   #val av spelare 1
   while not(spelare1 in spelarval1):
      spelare1 = simpledialog.askinteger("Spelare 1","Välj spelare mellan 1 och " + \
                                         str(spelarlista.antalSpelare()) + " :")
   #spelare 2   
   spelarval2 = []
   valbar = ""
   for i in range(1,(spelarlista.antalSpelare()+1)):
      if not(spelare1 == i):
         valbar += str(i) + ", "
         spelarval2.append(i)
         
   spelare2 = 0
   #val av spelare 2
   while not(spelare2 in spelarval2):
      spelare2 = simpledialog.askinteger("Spelare 2","Välj bland spelare " + valbar + " :")     

   #spel börjar
   t.delete('1.0', END)
   g = Game()
   g.resGlobals()
   gameEnd = FALSE
   setTXT=""
   #när spel är slut lämnas loopen
   while not gameEnd:           
      gameTXT, gameRES, gameSet, gameEnd = g.gameOver()
      print( gameTXT)
      t.insert(END,gameTXT)
      t.insert(END,'\n')
      setTXT = ""
      setTXT = spelarlista.txtSpelare(spelare1,spelare2) + "       " +  str(gameTXT) + "\n"
      print(setTXT)
      if 'Serv & Set'==valRes.get():
         messagebox.showinfo("Spela boll :     ", setTXT)
     
      if gameSet:
          print("Set :",gameRES)
          setTXT = ""
          setTXT = spelarlista.txtSpelare(spelare1,spelare2) +  "           " + str(gameRES) + "\n"
          print(setTXT)
          if 'Serv & Set'==valRes.get() or 'Set'==valRes.get():
             messagebox.showinfo("Set ",setTXT )                 
          t.insert(END,"Set "+str(gameRES))
          t.insert(END,'\n')
          gameSet=FALSE 

   #vinnare sorteras
   if gameRES[0]>gameRES[1]:
      vinst   = spelare1
      forlust = spelare2
   else:
      vinst   = spelare2
      forlust = spelare1      

   #resultat skrivs till textarea
   t.insert(END,spelarlista.resultSpeladMatch(vinst,forlust))
   t.insert(END,'\n')

   #dialog visas med vinnare
   messagebox.showinfo("Resultat:", spelarlista.resultSpeladMatch(vinst,forlust))                          
   spelarlista.lista[vinst-1].uppdateraTennisSpelare(True)
   spelarlista.lista[forlust-1].uppdateraTennisSpelare(False)
   t.insert('1.0',RESULTATRUBRIK + spelarlista.skrivListaText() + '\n')

#skapa root widget, fönsterhantag        
root = Tk()

#sätt titel på fönster
root.title("Spela Tennis !!!")




#läs in text från fil
res, txt = lasInTextFranFil('spelare.txt')

#kolar att rimliga värden fås
resvarden = rimligaVarden(txt)

# Spelar lista skapas
spelarlista = SpelarLista(txt)

#hjälp fönster kopplas till knapp 
bHjalpInfo = Button(root,text="Hjälp & info",command=spelaHjalpInfo)
bHjalpInfo.pack(side=TOP, expand=YES)

#text area skapas och kopplas till
#root widget med skrollist
t = Text(root,width=45,height=spelarlista.antalSpelare()+10)
scroll = Scrollbar(root, command=t.yview)
scroll.pack(side=RIGHT, fill=Y)
t.configure(yscrollcommand=scroll.set)
t.pack(side=TOP, expand=YES, fill=BOTH)
t.delete('1.0', END)

#kontroll av att fil finns
if not(res):
   t.insert('1.0',"Fil kunde ej läsas!\nAvsluta genom att trycka i kryssruta,\növre hörnet!")
#kontroll av rimliga värden   
elif not (resvarden):
   t.insert('1.0',"Värden inlästa från fil ej rimliga!\nAvsluta genom att trycka i kryssruta,\növre hörnet!")
else:
#kontroll av in fil och giltiga värden ok   
   t.insert('1.0',RESULTATRUBRIK + spelarlista.skrivListaText())
#   servRes = IntVar()
#   Checkbutton(root,text="Serv & Set",variable=servRes).pack(expand=YES, side=LEFT)
#   setRes  = IntVar()
#   Checkbutton(root,text="Endast Set",variable=setRes).pack(expand=YES, side=LEFT)
   valRes = StringVar()
   valen = ['Serv & Set','Set','Ingen']
   for val in valen:
      Radiobutton(root,text=val,value=val,variable=valRes).pack(expand=YES, side=LEFT)
   valRes.set('Ingen')
   bSpelaMatcth = Button(root,text="Spela match",command=spelaMatch)
   bSpelaMatcth.pack(side=BOTTOM, expand=YES)

   
#programlopp   
root.mainloop()
