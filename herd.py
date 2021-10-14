from dinosaur import Dinosaur

class Herd:
    
    def __init__(self):
        self.herd_list = []
        self.create_herd()

    def create_herd(self):
        trex = Dinosaur("Trex", 100, 50)
        triceratops = Dinosaur("Triceratops", 100, 50)
        velociraptor = Dinosaur("Velociraptor", 100, 50)
        self.herd_list.append(trex)
        self.herd_list.append(triceratops)
        self.herd_list.append(velociraptor)