'''
Created on Mar 12, 2012

@author: Julie
'''

from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.gui.OnscreenImage import OnscreenImage

class guiUpdate(): 
    def __init__(self, value):

        self.value = value;
        self.screenText = OnscreenText(text='Time: ', pos=(0.8, 0.95), scale=0.05, fg=(1, 1, 1, 1))
        self.timeValue = OnscreenText(text='  ', pos=(1.0, 0.95), scale=0.05, fg=(1, 1, 1, 1))
        self.resources = OnscreenText(text='Minerals: ', pos=(0.3, -0.67), scale=0.05, fg=(1, 1, 1, 1))
        self.resourceValue = OnscreenText(text='  ', pos=(0.6, -0.67), scale=0.05, fg=(1, 1, 1, 1))
       # tex = loader.loadTexture("/models/gui/gravsymbol.png")
        self.image = OnscreenImage(image=("./models/gui/gravsymbol.png"), scale = 0.03, pos=(0.2, 0, -0.75))
        self.image.setTransparency(True)
        self.ge = OnscreenText(text='               : ', pos=(0.4, -0.75), scale=0.05, fg=(1, 1, 1, 1))
        self.geAmount = OnscreenText(text=' ', pos=(0.6, -0.75), scale=0.05, fg=(1, 1, 1, 1))
        
    def update(self, event):
        if (event == "updateTime"):          
            from gameEngine.gameEngine import player
            if(player.selected_star != None):
                self.refreshTime() 
                self.value = player.selected_star.lifetime
                self.printTime()
        if (event == "updateMinerals"):
            self.refreshResources()
            from gameEngine.gameEngine import player
            self.value = player.minerals
            self.printResources()
        if (event == "updateGE"):
            self.refreshGE()
            from gameEngine.gameEngine import player
            self.value = player.ge_amount
            self.printGE()
        if (event == "updateUnits"):
            self.refreshUnits
        if (event == "updateConstructions"):
            self.updateConstructions
            
    def start(self):
        self.printTime()
        self.printResources()
        self.printGE()
        
    def refreshTime(self):
        self.timeValue.remove()

    def printTime(self):
        self.timeValue = OnscreenText(text=str(self.value), pos=(1.0, 0.95), scale=0.05, fg=(1, 1, 1, 1))
        
    def refreshResources(self):
        self.resourceValue.remove();  
        
    def printResources(self):      
        self.resourceValue = OnscreenText(text=str(self.value), pos=(0.6, -0.67), scale=0.05, fg=(1, 1, 1, 1))
        
    def refreshGE(self):
        self.geAmount.remove()
        
    def printGE(self):
        self.geAmount = OnscreenText(text=str(self.value), pos=(0.6, -0.75), scale=0.05, fg=(1, 1, 1, 1))
        
    def refreshUnits(self):
        pass
    
    def updateConstructions(self):
        pass