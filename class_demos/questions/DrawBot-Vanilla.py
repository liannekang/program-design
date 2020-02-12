import drawBot as db
import vanilla
from vanilla.dialogs import putFile
from random import random


class MyInterface:
    
    def __init__(self):
        
        self.pdf = None
        
        self.w = vanilla.Window((600, 900), "My Interface")
        self.w.drawButton = vanilla.Button((10, 10, 100, 25), "Draw!", callback=self.draw)
        self.w.saveButton = vanilla.Button((120, 10, 100, 25), "Save!", callback=self.save)
        self.w.drawView = db.ui.drawView.DrawView((10, 50, -10, -10))
        
        self.w.open()


    def draw(self, sender):

        db.newDrawing()
        db.newPage(300, 300)
        fill(random(), random(), random())
        db.rect(0, 0, 50, 50)
        
        self.pdf = db.pdfImage()
        self.w.drawView.setPDFDocument(self.pdf)
    
    
    def save(self, sender):
        if self.pdf:
            fileSavePath = putFile(title="Save Image", fileName="Image.pdf")
            if fileSavePath:
                db.saveImage(fileSavePath)
        
MyInterface()
        