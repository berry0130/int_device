import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from PIL import Image
import numpy as np


class mapdrawing:
    def __init__(self):
        rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.position)
    def position(self,data):
        self.pos_x = data.pose.pose.position.x
        # print self.pos_x
        self.pos_y = data.pose.pose.position.y
        rospy.spin()
    def draw(self):
        im = Image.open("1107.pgm")    
        im.show()
        width , height = im.size    
        for i in range(width):
            for j in range(height):
                pixel=im.getpixel((i,j))
                if (pixel>220) :
                    print im.getpixel((i,j))
            
if __name__ == '__main__':
    rospy.init_node('map', anonymous=True)
    do=mapdrawing()
    do.draw()
    
 