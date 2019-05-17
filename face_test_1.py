class Apple:
    def __init__(self,weight,smell,color,volume):
        self.weight = weight
        self.smell = smell
        self.color = color
        self.volume = volume

Apple = Apple("190g","sweet","red","1 cubic")
print(Apple.weight,Apple.smell,Apple.color,Apple.volume)
