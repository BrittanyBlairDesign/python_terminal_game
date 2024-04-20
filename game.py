import sys
import components as c
import vectors as v

movement_test = c.Movement(v.Vector2(0,0), v.Vector2(-1, 0))
movement_test.Move()
movement_test.SetDirection("rights")
movement_test.MoveRandom()