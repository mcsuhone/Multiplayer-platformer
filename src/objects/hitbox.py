import sys 
sys.path.append('..')

from src.vector import Vector
from src.constants import Constants



class Hitbox():
    def __init__(self, x, y, width, height):
        """Center rectangle"""
        self.x = x + width/2
        self.y = y + height/2
        self.half_width = width/2
        self.half_height = height/2
        self.collision_directions = {'x':None, 'y':None} # Holds coordinates of safe position

    def clone(self):
        return Hitbox(self.x - self.half_width, self.y - self.half_height, self.half_width, self.half_height)

    """For use of object class only. Converts objects coordinates to hitbox coordinates"""
    def move_to(self, x, y):
        self.x = x + self.half_width
        self.y = y + self.half_height

    def reset_collisions(self):
        self.collision_directions = {'x':None, 'y':None}
                
    def basic_collision(self, other, velocity):
        orig_x = self.x
        orig_y = self.y

        # Checks if object is moving into collision with other
        self.x += velocity.x
        self.y += velocity.y

        self.x = orig_x
        self.y = orig_y

    def collision(self, other, velocity):
        if abs(self.y - other.y) < self.half_height + other.half_height and abs(self.x - other.x) < self.half_width + other.half_width:
            #Intersected
            velocity.x -= abs()
            velocity.y -= abs()
            #Eri tapaukset

            if velocity.y < 0:
                # Bottom side
                self.collision_directions['y'] = self.y - self.half_height - velocity.y
                self.collision_directions['x'] = self.x - self.half_width - velocity.x
                self.move_to(self.collision_directions['x'], self.collision_directions['y'])
            elif velocity.y > 0:
                # Top side
                self.collision_directions['y'] = self.y - self.half_height - velocity.y
                self.collision_directions['x'] = self.x - self.half_width - velocity.x
                self.move_to(self.collision_directions['x'], self.collision_directions['y'])
            else:
                if velocity.x < 0:
                    # Left side
                    self.collision_directions['x'] = self.x - self.half_width - velocity.x
                    self.x = self.collision_directions['x'] + self.half_width
                elif velocity.x > 0:
                    # Right side
                    self.collision_directions['x'] = self.x - self.half_width - velocity.x
                    self.x = self.collision_directions['x'] + self.half_width

    '''
    def collision(self, other, velocity):
        if abs(self.y - other.y) < self.half_height + other.half_height and abs(self.x - other.x) < self.half_width + other.half_width:
            #Intersected
            if (velocity.y == 0):
                k = 0
            else:
                k = velocity.x / velocity.y

            if velocity.y < 0:
                # Bottom side
                self.collision_directions['bottom'] = other.y + other.half_height
                dy = self.collision_directions['bottom'] - self.y
                self.collision_directions['x'] = (self.x - self.half_width) + (dy * k)
                self.move_to(self.collision_directions['x'], self.collision_directions['bottom'])
            elif velocity.y > 0:
                # Top side
                self.collision_directions['top'] = other.y - other.half_height*2 - self.half_height*2
                dy = self.y - self.collision_directions['top']
                self.collision_directions['x'] = (self.x - self.half_width) - (dy * k)
                self.move_to(self.collision_directions['x'], self.collision_directions['top'])
            else:
                if velocity.x < 0:
                    # Left side
                    self.collision_directions['x'] = other.x + other.half_width
                    self.x = self.collision_directions['x'] + self.half_width
                elif velocity.x > 0:
                    # Right side
                    self.collision_directions['x'] = other.x - other.half_width - self.half_width*2
                    self.x = self.collision_directions['x'] + self.half_width
    '''
    def intersects(self, other):
        if abs(self.y - other.y) < self.half_height + other.half_height and abs(self.x - other.x) < self.half_width + other.half_width:
            return True
        else:
            return False

    def __str__(self):
        return "Hitbox(" + str(self.x) + ":" + str(self.y) + " - " + str(self.half_width) + ":" + str(self.half_height) + ")"