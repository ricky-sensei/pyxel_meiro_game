
import pyxel
pyxel.init(128, 128)
pyxel.load("meiro.pyxres")

player = {
    "position_x":16,
    "position_y":16,
}

move = {
    "LEFT":0,
    "RIGHT":0,
    "UP":0,
    "DOWN":0,
}

def update():
    if list(move.values()) == [0, 0, 0, 0]:
        if pyxel.btn(pyxel.KEY_LEFT):
            print("left pressed")
            move["LEFT"] = 16
            
        elif pyxel.btn(pyxel.KEY_RIGHT):
            print("right pressed")
            move["RIGHT"] = 16
            
        elif pyxel.btn(pyxel.KEY_UP):
            print("up pressed")
            move["UP"] = 16
            
        elif pyxel.btn(pyxel.KEY_DOWN):
            print("down pressed")
            move["DOWN"] = 16
    
    elif move["LEFT"] > 0:
        player["position_x"] = player["position_x"] - 1
        move["LEFT"] = move["LEFT"] - 1
    elif move["RIGHT"] > 0:
        player["position_x"] = player["position_x"] + 1
        move["RIGHT"] = move["RIGHT"] - 1
    elif move["UP"] > 0:
        player["position_y"] = player["position_y"] - 1
        move["UP"] = move["UP"] - 1
    elif move["DOWN"] > 0:
        player["position_y"] = player["position_y"] + 1
        move["DOWN"] = move["DOWN"] - 1
    else:
        pass



    

    

def draw():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 0, 0, 128, 128, 0)
    pyxel.blt(player["position_x"], player["position_y"], 0, 0, 0, 16, 16, 0)

pyxel.run(update, draw)
