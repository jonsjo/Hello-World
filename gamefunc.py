# Title: Game klass till Prototypwin, P-Uppgift.
# Författare: Jonas Sjösvärd
# Datum: 2012-03-04
from random import *
from tkinter import *

# En klass som simulerar en poäng räkning
# för en tennis match där resultat returneras
# i form av text.
class Game:

    #initering
    def __init__(self):
        self.RES=[0,0]
        self.resSpelare1 = "   0  "
        self.resSpelare2 = "   0  "
        self.i=0
        self.a=0
        self.spelare1=0
        self.spelare2=0
        print("__init__")

    #reset vid ny körning
    def resGlobals(self):
        self.__init__()

    #vinnare tilldelas text som skall visas senare, gameTXT
    def updateStatus(self,res,winner,looser):
        if res == "   0  ":
            res = "  15  "
        elif res == "  15  ":
            res = "  30  "
        elif res == "  15  ":
            res = "  30  "
        elif res == "  30  ":
            res = "  40  "
        elif res == "  40  ":
            if winner > (looser + 1):
                res = " Game "
            else:    
                res = "Fördel"
        elif res == "Fördel":
            res = " Game "
        elif res ==" Lika ":
            res = "Fördel"
        return res

    #bygger upp resultat i form av text 
    def gameTXTSet(self):            
        if self.spelare1==self.spelare2 and self.spelare1>3:
            self.resSpelare1=" Lika "
            self.resSpelare2=" Lika "            
            gameTXT = self.resSpelare1+self.resSpelare2    
        elif self.spelare1==self.spelare2 and self.spelare1<4:            
            gameTXT = self.resSpelare1+" Lika "
        elif self.resSpelare1==" Lika " and not(self.resSpelare2==" Lika "):            
            gameTXT = "      "+self.resSpelare2
        elif not(self.resSpelare1==" Lika ") and self.resSpelare2==" Lika ":           
            gameTXT = self.resSpelare1+"      "
        elif self.resSpelare2=="Fördel":        
            gameTXT = "      "+self.resSpelare2
        elif self.resSpelare1=="Fördel":           
            gameTXT = self.resSpelare1+"      "
        elif self.resSpelare2==" Game ":            
            gameTXT = "      "+self.resSpelare2
        elif self.resSpelare1==" Game ":    
            gameTXT = self.resSpelare1+"      "
        else:          
            gameTXT = self.resSpelare1+self.resSpelare2
        return gameTXT      

    #kontroll av    
    def gameSetCheck(self):
        gameSet = FALSE
        if self.spelare1 == 4 and self.spelare2 < 3:
            gameSet = TRUE      
        if self.spelare2 == 4 and self.spelare1 < 3:
            gameSet = TRUE
        if self.spelare1>3:
            if (self.spelare2+2)==self.spelare1:
                gameSet = TRUE
        if self.spelare2>3:
            if (self.spelare1+2)==self.spelare2:
                gameSet = TRUE
        #om game färdigspelat räkna upp resultat och nollställ
        if gameSet:
            if self.spelare1>self.spelare2:
                self.RES[0]+=1
            else:
                self.RES[1]+=1
            self.resSpelare1 = "   0  "
            self.resSpelare2 = "   0  "
            self.spelare1=0
            self.spelare2=0
        return gameSet    

    def gameEndCheck(self):
        gameEndRes=FALSE
        if ((self.RES[1]>=6)or(self.RES[0]>=6)):
            if ((self.RES[1]>=6)or(self.RES[0]>=6)):
                if ((self.RES[0]-self.RES[1])>1):
                    gameEndRes=TRUE
                if ((self.RES[1]-self.RES[0])>1):
                    gameEndRes=TRUE
        return gameEndRes            

    #generar resultat för ett game.
    #returnerar reultattext, resultat, set och slut
    def gameOver(self):
        gameEnd = FALSE
        gameSet = FALSE
        gameTXT = ""

        #slumpar fram vem som skall vinna
        res = randrange(0,2)

        #räkna resultat
        if res == 0:
            self.spelare1+=1
            self.resSpelare1 = self.updateStatus(self.resSpelare1,
                                                 self.spelare1,
                                                 self.spelare2)
        else:
            self.spelare2+=1
            self.resSpelare2 = self.updateStatus(self.resSpelare2,
                                                 self.spelare2,
                                                 self.spelare1)
        
        #skapa resultat i text
        gameTXT = self.gameTXTSet()        

        #kolla om Set är färdigspelat   
        gameSet = self.gameSetCheck()    

        #kolla antalet set, minst 6 eller fler och en diff på minst 2
        #mellan vinnare och fölorare
        gameEnd = self.gameEndCheck()

        #tilldela resultat siffror, game
        gameRES = self.RES
                
        return gameTXT, gameRES, gameSet, gameEnd


    def __del__(self):
        print("*__del__*")


# Om module exeveras enskilt, ej anropas
# Exeveras rader efter if sats
if __name__ == '__main__':
   
    def nyFunk():
        g = Game()
        g.resGlobals()
        gameEnd = FALSE
        while not gameEnd:
            gameTXT, gameRES, gameSet, gameEnd = g.gameOver()
            print( gameTXT)            
            if gameSet:
                print("Set ",gameRES)
               
        
    root=Tk()
    
    button = Button(root,text='Ny funk',command=nyFunk)
    button.pack(padx=40,side=TOP)

    root.mainloop()
