import sys 
sys.path.append('..')

from src.vector import Vector
from src.constants import Constants



class Hitbox():
    def __init__(self, x, y, width, height):
        """Center rectangle"""
        self.x = x + width/2
        self.y = y + height/2
        self.half_width = width/2.0
        self.half_height = height/2.0
        self.collision_directions = {'x':None, 'y':None} # Holds coordinates of safe position

    def clone(self):
        return Hitbox(self.x - self.half_width, self.y - self.half_height, self.half_width, self.half_height)

    """For use of object class only. Converts objects coordinates to hitbox coordinates"""
    def move_to(self, x, y):
        self.x = x + self.half_width
        self.y = y + self.half_height

    def pos(self):
        return Vector(self.x, self.y)

    def reset_collisions(self):
        self.collision_directions = {'x':None, 'y':None}

    def bottom_collide(self, other):
        self.collision_directions['y'] = other.y + other.half_height
        self.y = self.collision_directions['y'] + self.half_height

    def top_collide(self, other):
        self.collision_directions['y'] = other.y - other.half_height - self.half_height * 2
        self.y = self.collision_directions['y'] + self.half_height

    def left_collide(self, other):
        self.collision_directions['x'] = other.x + other.half_width
        self.x = self.collision_directions['x'] + self.half_width

    def right_collide(self, other):
        self.collision_directions['x'] = other.x - other.half_width - self.half_width * 2
        self.x = self.collision_directions['x'] + self.half_width

    def collision(self, other, velocity):
        if self.intersects(other):
            #Intersected
            print(self)
            print(other)
            angle = velocity.angle_x_axis()
            top_point = Vector(self.x - velocity.x, self.y - velocity.y + self.half_height)
            right_point = Vector(self.x - velocity.x + self.half_width, self.y - velocity.y)
            bottom_point = Vector(self.x - velocity.x, self.y - velocity.y - self.half_height)
            left_point = Vector(self.x - velocity.x - self.half_width, self.y - velocity.y)
            print(angle)
            if angle < 180 and angle > 90:
                #top left
                if left_point.distance(other.pos()) < top_point.distance(other.pos()):
                    #left side
                    self.left_collide(other)
                else:
                    #top side
                    self.top_collide(other)

            if angle < 90 and angle > 0:
                #top right
                if top_point.distance(other.pos()) < right_point.distance(other.pos()):
                    #top side
                    self.top_collide(other)
                else:
                    #right side
                    self.right_collide(other)

            if angle < 0 and angle > -90:
                #bottom right
                if right_point.distance(other.pos()) < bottom_point.distance(other.pos()):
                    #right side
                    self.right_collide(other)
                else:
                    #bottom side
                    self.bottom_collide(other)

            if angle < -90 and angle > -180:
                #bottom left
                if bottom_point.distance(other.pos()) < left_point.distance(other.pos()):
                    #bottom side
                    self.bottom_collide(other)
                else:
                    #left side
                    self.left_collide(other)

            if angle == 0:
                #right side
                self.right_collide(other)

            if angle == 90:
                #top side
                self.top_collide(other)

            if angle == -90:
                #bottom side
                self.bottom_collide(other)

            if angle == 180 or angle == -180:
                #left side
                self.left_collide(other)

            if (self.collision_directions['x'] is not None):
                self.move_to(self.collision_directions['x'] - self.half_width, self.y - self.half_height)
            if (self.collision_directions['y'] is not None):
                self.move_to(self.x - self.half_width, self.collision_directions['y'] - self.half_height)
            print(self.collision_directions)

    '''
    def collision(self, other, velocity):
        if self.intersects(other):
            #Intersected
            if (velocity.x == 0 and velocity.y == 0):
                if (self.x < other.x ):
                    self.collision_directions['x'] = self.x - self.half_width - 1
                else:
                    self.collision_directions['x'] = self.x - self.half_width + 1
                if (self.y < other.x):
                    self.collision_directions['y'] = self.y - self.half_height + 1
                else:
                    self.collision_directions['y'] = self.y - self.half_height + 1
                self.move_to(self.collision_directions['x'], self.collision_directions['y'])
            else:
                self.collision_directions['x'] = int(self.x - self.half_width - velocity.x)
                self.collision_directions['y'] = int(self.y - self.half_height - velocity.y)
                self.move_to(self.collision_directions['x'], self.collision_directions['y'])


    def collision(self, other, velocity):
        if abs(self.y - other.y) < self.half_height + other.half_height and abs(self.x - other.x) < self.half_width + other.half_width:
            #Intersected
            if (velocity.y == 0):
                k = 0
            else:
                k = velocity.x / velocity.y

            if self.y - self.half_height > other.y + other.half_height:
                # Is above
                self.collision_directions['y'] = other.y + other.half_height
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
        if abs(self.y - other.y) + 1 <= self.half_height + other.half_height and abs(self.x - other.x) + 1 <= self.half_width + other.half_width:
            return True
        else:
            return False

    def __str__(self):
        return "Hitbox(" + str(self.x) + ";" + str(self.y) + " - " + str(self.half_width) + ";" + str(self.half_height) + ")"