
import components as c
import vectors as v
import unittest as ut

class Test_Vector(ut.TestCase):
    def test_print(self):
        self.assertEqual(str(v.Vector2(5,8)),"(5,8)")
    
    def test_addition(self):
        vector1 = v.Vector2(5,4)
        vector2 = v.Vector2(3,9)
        answer = v.Vector2(7,13)

        self.assertEqual(vector1 + vector2, answer)

    def test_Subtraction(self):
        vector1 = v.Vector2(5,4)
        vector2 = v.Vector2(3,9)
        answer = v.Vector2(2,-5)
        self.assertEqual(vector1 - vector2, answer)
    
    def test_Equal(self):
        vector1 = v.Vector2(0.0)
        vector2  = v.Vector2(5,8)
        answer = v.Vector2(5,8)
        vector1 = vector2
        self.assertEqual(vector1, answer )

class Test_Movement(ut.TestCase):
    def test_print(self):
        self.assertEqual(str(c.Movement(v.Vector2(2,3), v.Vector2(0,1))), "Location : (2,3)\nDirection : (0,1)")

    def test_getters(self):
        t_mover = c.Movement(v.Vector2(1,4), v.Vector2(0,-1))
        directions = ["down","right","left"]
        directionV = t_mover.GetDirection()
        locationV = t_mover.GetLocation()
        print(locationV)
        directionsV = t_mover.GetPossibleDirections(v.Vector2(10,10))
        print(directionsV)
        self.assertEqual(directionV, v.Vector2(0,-1))
        self.assertEqual(locationV, v.Vector2(1,4))
        self.assertEqual(directionsV, directions)

        t_mover = c.Movement(v.Vector2(0,0))
        t_mover.SetDirection("up")
        self.assertEqual(t_mover.direction, v.Vector2(-1,0))

        t_mover.SetLocation(v.Vector2(3.9))
        self.assertEqual(t_mover.location, v.Vector2(3,9))

    def test_move(self):
        t_mover = c.Movement(v.Vector2(0,0), v.Vector2(-1,0))
        t_mover.Move(v.Vector2(10,10))
        self.assertEqual(t_mover.location, v.Vector2(-1,0))
        t_mover.SetDirection('right')
        t_mover.Move(v.Vector2(10,10))
        self.assertEqual(t_mover.GetLocation,v.Vector2(-1,-1))

class Test_Stat(ut.TestCase):
    def test_getters(self):
        stat = c.Stat(5, 0)
        self.assertEqual(stat.GetValue(), 5)
        self.assertEqual(stat.GetMax(), 5)
        self.assertEqual(stat.GetMin(), 0)

    def test_Setters(self):
        stat = c.Stat(3)
        stat.Decrease(1)
        self.assertEqual(stat.GetValue(), 2)
        stat.Increase(3)
        self.assertEqual(stat.GetValue(), 3)
        stat.Decrease(2)
        stat.Reset()
        self.assertEqual(stat.GetValue(), 3)

if __name__ == '__main__':
    ut.main()  