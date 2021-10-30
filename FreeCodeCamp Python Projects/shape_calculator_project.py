class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def __repr__(self):
        return  f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self,setwidth):
        self.setwidth=setwidth
        self.width =self.setwidth
        return  self.width
    def set_height(self,setheight):
        self.setheight=setheight
        self.height=self.setheight
        return self.height
    def get_area(self):
        return (self.width * self.height)
    def get_perimeter(self):
        return  ((2 * self.width) + (2 * self.height))
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        i = self.height
        s=''
        if self.width > 50 or self.height >50:
            return "Too big for picture."
        else:
            while i >0:
                z='*'*self.width+'\n'
                s=s+z
                i-=1
            return s
    def get_amount_inside(self,name):
        self.name=name
        return self.get_area()//self.name.get_area()


class Square(Rectangle):
    def __init__(self,lenght):
        self.lenght = lenght
        self.side = self.lenght
        super().__init__(width=lenght,height=lenght)
    def get_area(self):
        return Rectangle.get_area(self)
    def set_width(self,setwidth):
        self.wit=setwidth
        super().set_width(self.wit)
        return self.set_side(setwidth)
    def set_height(self,setheight):
        self.set=setheight
        super().set_height(setheight=self.set)
        return self.set_side(setheight)
    def set_side(self,side):
        super().__init__(width=side,height=side)
        self.side= side
        self.lenght =self.side

        return self.side
    def get_diagonal(self):
        return super().get_diagonal()
    def __repr__(self):
        return f"Square(side={self.side})"
