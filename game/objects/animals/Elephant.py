from objects.animals.GenericAnimal import GenericAnimal

class Elephant(GenericAnimal):

    def __init__(self, screen, xPos=-1, yPos=-1, xSize=-1, ySize=-1):
        if xSize + ySize < -1:
            xSize = 640
            ySize = 494
        if xPos + yPos < -1:
            xPos, yPos = screen.get_size()
            yPos = yPos - ySize - 10

        super(Elephant, self).__init__("../resources/sprites/animals/elephant.png", screen, xPos, yPos, xSize, ySize)

    @staticmethod
    def search():
        return GenericAnimal.searcher(30)

    """
    Method that defines the points this animal gives when photographed.
    """
    def getPoints(self):
        return 2500