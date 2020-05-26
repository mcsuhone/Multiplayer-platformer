import pyglet
from game import Game

window = pyglet.window.Window(800, 600)

def main():
    game = Game(window)

if __name__ == '__main__':
    main()