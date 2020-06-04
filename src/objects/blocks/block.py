import sys
sys.path.append('..')
import pyglet
from src.objects.object import Object



class Block(Object):
    def __init__(self, texture_id, x, y, batch = None):
        super().__init__(texture_id, x, y, batch = batch)
