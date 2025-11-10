
import pyxel
pyxel.init(128, 128)
pyxel.load("meiro.pyxres")

player = {
    "position_x":16,
    "position_y":16,
}

move = {
    "left":0,
    "right":0,
    "up":0,
    "down":0,
}

def btn_pressed():
    if move.values == [0, 0, 0, 0]:
        for key_code in pyxel.pyxel.input_keys:
            if key_code == pyxel.KEY_LEFT:
                move["left"] = 16
            if key_code == pyxel.KEY_RIGHT:
                move["right"] = 16
            if key_code == pyxel.KEY_UP:
                move["up"] = 16
            if key_code == pyxel.KEY_DOWN:
                move["down"] = 16




    






def update():
    btn_pressed()
    minusone()


    

def draw():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 0, 0, 128, 128, 0)
    pyxel.blt(player["position_x"], player["position_y"], 0, 0, 0, 16, 16, 0)

pyxel.run(update, draw)
