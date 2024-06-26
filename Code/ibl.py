# from util import Image, drawImages

class IBL:
    def __init__(self, container_width, container_height):
        self.container_width = container_width
        self.container_height = container_height
        self.placed_images = []

    def higestBarrier(self, image):
        barrier = None
        max_y = 0

        for placed in self.placed_images:
            pl = placed.x
            pr = placed.x + placed.width
            pt = placed.y + placed.height
            il = image.x
            ir = image.x + image.width

            if pl < il and pr > il  or pl >= il and pl < ir:
               if not barrier or pt > max_y: 
                    barrier = placed
                    max_y = pt
                    
        return barrier
    
    def rightmostBarrier(self, image, new_bound_x):
        barrier = None
        max_x = 0

        for placed in self.placed_images:
            if placed.x >= new_bound_x:
                continue 

            pb = placed.y
            pt = placed.y + placed.height
            pr = placed.x + placed.width
            ib = image.y
            it = image.y + image.height

            if pb < ib and pt > ib  or pb >= ib and pb < it:
               if not barrier or pr > max_x: 
                    barrier = placed
                    max_x = pr
                    
        return barrier

    def shift_to_buttom(self, image, x0, y0):
        image.x = x0
        image.y = y0
        barrier = self.higestBarrier(image)

        if barrier :
            barrier_top = barrier.y + barrier.height
            if image.y < barrier_top:
                # print('Nema vise prostora')
                return -1

            image.y = barrier_top
        else:
            image.y = 0

        # Vrati sledecu sirunu 
        if barrier:
            return barrier.x
        return 0

    def shift_to_left(self, image, x1):
        barrier = self.rightmostBarrier(image, image.x + image.width)

        if barrier :
            barrier_right = barrier.x + barrier.width
            if image.x < barrier_right:
                #print('Nema vise prostora')
                return -1
            image.x = max(barrier_right, x1)
        else:
            image.x = max(0, x1)
        

    def find_position(self, image):
        x0 = self.container_width - image.width
        y0 = self.container_height * 10

        
        new_width = self.shift_to_buttom(image, x0, y0)
        x1 = new_width - image.width
        ind = self.shift_to_left(image, x1)

        if new_width == -1 or ind  == -1: 
           return False

        xi = x0
        yi = y0

        while xi > image.x:
            xi = image.x
            yi = image.y
            new_width = self.shift_to_buttom(image, xi, yi)
            x1 = new_width - image.width
            ind = self.shift_to_left(image, x1)
            if new_width == -1 or ind  == -1: 
                break
            

        return True

    def update_bounds(self, image):
        x_border = image.x + image.width
        y_border = image.y + image.height

        if x_border > self.bound_width:
            self.bound_width = x_border

        if y_border > self.bound_height:
            self.bound_height = y_border

    def get_bounds(self):
        return self.bound_width, self.bound_height

    def place_images(self, images):
        self.placed_images.clear()
        self.bound_width = 0
        self.bound_height = 0
        for image in images:
            success = self.find_position(image)
            if not success:
                self.bound_height = self.container_height
                self.bound_width = self.container_width
                return []
            self.placed_images.append(image)
            self.update_bounds(image)
            # drawImages(self.placed_images, 300, 200, 300, 200)

        return self.placed_images


# images = [Image(101, 41), Image(41, 101), Image(21, 31), Image(41, 41), Image(31, 41), Image(21, 21),
#           Image(102, 42), Image(42, 102), Image(22, 32), Image(42, 42), Image(32, 42), Image(22, 22),
#           Image(101, 41), Image(41, 101), Image(21, 31), Image(41, 41), Image(31, 41), Image(21, 21)]
# ibl = IBL(300, 200)

# placed = ibl.place_images(images)

# bx, by = ibl.get_bounds()

# drawImages(placed, 300, 200, bx, by)
