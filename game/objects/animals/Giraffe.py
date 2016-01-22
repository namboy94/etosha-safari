from objects.animals.GenericAnimal import GenericAnimal

class Giraffe(GenericAnimal):

    def __init__(self, screen, xPos=-1, yPos=-1, xSize=-1, ySize=-1):
        if xSize + ySize < -1:
            xSize = 462
            ySize = 592
        if xPos + yPos < -1:
            xPos, yPos = screen.get_size()
            yPos = yPos - ySize - 10

        super(Giraffe, self).__init__("../resources/sprites/animals/giraffe.png", screen, xPos, yPos, xSize, ySize)

    @staticmethod
    def search():
        return GenericAnimal.searcher(100)

    """
    Method that defines the points this animal gives when photographed.
    """
    def getPoints(self):
        return 500