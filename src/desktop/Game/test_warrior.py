
import unittest

from warrior import player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        
        data = [100,150,50,50]
        self.obj_player = player(data[0],data[1],
                                data[2],data[3])
        self.my_data = [100,150,50,50]
    def test_store_values(self):
        x,y = 100,150
        w,h = 50,50
        obj_player = player(x,y,w,h)
        data = [100,150,50,50]
        ##for value in data:
        #    self.assertIn(data,self.my_data)
        #self.assertIn(obj_player.x,self.my_data[0])
        #self.assertIn(y,self.obj_player.y)
        #self.assertIn(obj_player.w,self.my_data[2])
        #self.assertIn(obj_player.h,self.my_data[3])
        

if __name__=='__main__':
    unittest.main()