


import unittest

from game_functions import projectile

class TestProjectile(unittest.TestCase):
    def setUp(self):

        self.obj_player = projectile(10,15,5,10,1)
    def test_store_values(self):
        x,y = 100,150
        radius = 5
        color = 10
        f = 1
        obj_player = projectile(x,y,radius,color,f)
        ##for value in data:
        #    self.assertIn(data,self.my_data)
        #self.assertIn(obj_player.x,self.my_data[0])
        #self.assertIn(y,self.obj_player.y)
        #self.assertIn(obj_player.w,self.my_data[2])
        #self.assertIn(obj_player.h,self.my_data[3])
        

if __name__=='__main__':
    unittest.main()