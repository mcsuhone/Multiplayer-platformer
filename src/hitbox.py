



class Hitbox():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collision_directions = {'left':False, 'right':False, 'top':False, 'bottom':False}

    def reset_collisions(self):
        self.collision_directions = {'left':False, 'right':False, 'top':False, 'bottom':False}

    def intersects(self, hitbox):

        if (hitbox.x + hitbox.width > self.x and hitbox.x + hitbox.width < self.x + self.width) and (hitbox.y + hitbox.height > self.y and hitbox.y + hitbox.height < self.y + self.height):
            if abs((self.x + self.width) - hitbox.x) > abs((self.y + self.height) - hitbox.y):
                self.collision_directions['right'] = True
            else:
                self.collision_directions['bottom'] = True
        # Check if colliding from bottom right corner
        if (self.x + self.width > hitbox.x and self.x + self.width < hitbox.x + hitbox.width) and (self.y + self.height > hitbox.y and self.y + self.height < hitbox.y + hitbox.height):
            if abs((self.x + self.width) - hitbox.x) > abs((self.y + self.height) - hitbox.y):
                self.collision_directions['right'] = True
            else:
                self.collision_directions['bottom'] = True
        #Check from other obj side
        if (hitbox.x + hitbox.width > self.x and hitbox.x + hitbox.width < self.x + self.width) and (hitbox.y + hitbox.height > self.y and hitbox.y + hitbox.height < self.y + self.height):
            if abs((self.x + self.width) - hitbox.x) > abs((self.y + self.height) - hitbox.y):
                self.collision_directions['right'] = True
            else:
                self.collision_directions['bottom'] = True
        # Check if colliding from top right corner
        if (self.x + self.width > hitbox.x and self.x + self.width < hitbox.x + hitbox.width) and (self.y > hitbox.y and self.y < hitbox.y + hitbox.height):
            if abs((self.x + self.width) - hitbox.x) > abs(self.y - hitbox.y):
                self.collision_directions['right'] = True
            else:
                self.collision_directions['top'] = True
        #Check from other obj side
        if (hitbox.x + hitbox.width > self.x and hitbox.x + hitbox.width < self.x + self.width) and (hitbox.y > self.y and hitbox.y < self.y + self.height):
            if abs((self.x + self.width) - hitbox.x) > abs(self.y - hitbox.y):
                self.collision_directions['right'] = True
            else:
                self.collision_directions['top'] = True

        # Check if colliding from top left corner
        if (self.x > hitbox.x and self.x < hitbox.x + hitbox.width) and (self.y > hitbox.y and self.y < hitbox.y + hitbox.height):
            if abs(self.x - hitbox.x) > abs(self.y - hitbox.y):
                self.collision_directions['left'] = True
            else:
                self.collision_directions['top'] = True
        #Check from other obj side
        if (hitbox.x > self.x and hitbox.x < self.x + self.width) and (hitbox.y > self.y and hitbox.y < self.y + self.height):
            if abs(self.x - hitbox.x) > abs(self.y - hitbox.y):
                self.collision_directions['left'] = True
            else:
                self.collision_directions['top'] = True

        # Check if colliding from bottom left corner
        if (self.x > hitbox.x and self.x < hitbox.x + hitbox.width) and (self.y + self.height > hitbox.y and self.y + self.height < hitbox.y + hitbox.height):
            if abs(self.x - hitbox.x) > abs((self.y + self.width) - hitbox.y):
                self.collision_directions['left'] = True
            else:
                self.collision_directions['bottom'] = True
                
        #Check from other obj side
        if (hitbox.x > self.x and hitbox.x < self.x + self.width) and (hitbox.y + hitbox.height > self.y and hitbox.y + hitbox.height < self.y + self.height):
            if abs(self.x - hitbox.x) > abs((self.y + self.width) - hitbox.y):
                self.collision_directions['left'] = True
            else:
                self.collision_directions['bottom'] = True

    def __str__(self):
        return "Hitbox(" + str(self.x) + ":" + str(self.y) + "-" + str(self.width) + ":" + str(self.height) + ")"