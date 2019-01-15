import turtle as t

# class

class MagicBrush:
    t.color('red')
    def draw_square(self):        
        for i in range(4):
            t.forward(100)
            t.right(90)

    def draw_triangle(self):
        for i in range(3):
            t.forward(100)
            t.right(120)
    
    def go(self):
        t.forward(200)
    
    def turn(self):
        t.right(90)

    def draw_circle(self):
        for i in range(72):
            t.forward(14)
            t.right(5)

m1 = MagicBrush()
m2 = MagicBrush()

m1.draw_circle()

# brad = t.Turtle()
# brad.shape('turtle')
# brad.speed(2)
# brad.forward(100)

# m1.go()
# m2.turn()
# m1.turn()
# m1.go()
# m2.go()

t.mainloop()
