from objects.animals.GenericAnimal import GenericAnimal

class Cheetah(GenericAnimal):
    
    def __init__(self, screen, xPos=-1, yPos=-1, xSize=-1, ySize=-1):
        if xSize + ySize < -1:
            xSize = 300
            ySize = 137
        if xPos + yPos < -1:
            xPos = screen.get_size()[0]
            yPos = screen.get_size()[1] - ySize - 10

        super(Cheetah, self).__init__("../resources/sprites/animals/cheetah.png", screen, 5, xPos, yPos, xSize, ySize)