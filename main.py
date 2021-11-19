import avatar
from avatar import Avatar
import core
from creep import Creep



def setup():
        print("Setup START---------")
        core.fps = 60
        core.WINDOW_SIZE = [800, 600]


        core.memory("avatar",Avatar())

        core.memory("listcreep", [])
        core.memory("nbrcreep", 100)
        for c in range(0, core.memory("nbrcreep")):
            core.memory("listcreep").append(Creep(800,600))





        print("Setup END-----------")

def run():
    core.cleanScreen()
    for creep in core.memory("listcreep"):
        creep.show(core.screen)
    core.memory("avatar").show(core.screen)




    core.printMemory()



core.main(setup, run)




