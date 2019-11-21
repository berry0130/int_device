import rospy,tf
from geometry_msgs.msg import PoseWithCovarianceStamped
from PIL import Image
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt 
# from tf import TransformListener

class mapdrawing:
    def __init__(self):
        # self.tf = TransformListener()
        self.listener = tf.TransformListener()
        # rospy.Subscriber('/', PoseWithCovarianceStamped, self.position)
    def position(self):
        print "a"
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            try:
                (position, quaternion) = self.listener.lookupTransform("/map", "/base_link", rospy.Time(0))
                print position[0], position[1]
                return position[0]*100,position[1]*100
            except:
                print 'tf not ready'
            r.sleep()

        # if (self.listener.frameExists("/base_link") and self.listener.frameExists("/map")):
        #     print "b"
        #     t = self. listener.getLatestCommonTime("/map", "/base_link")
        #     position, quaternion = self.lisenter.lookupTransform("/map", "/base_link", rospy.Time(0))
        #     print position, quaternion
        #     r.sleep()
        # print "c"
        # self.pos_x = data.pose.pose.position.x
        # print self.pos_x
        # self.pos_y = data.pose.pose.position.y

    def draw(self,x,y):
        im = Image.open("base.pgm")    
        width , height = im.size

        plt.imshow(im,cmap ='gray',origin='lower')
        plt.scatter(x+86,(-y+86), c = 'y',marker = 'o')
        plt.imshow(im,cmap ='gray')
       
        plt.savefig('result.png')
        print "haha"
        # plt.show()
        # im = Image.open("1107.pgm")    
        # im.show()
        # width , height = im.size    
        # for i in range(width):
        #     for j in range(height):
        #         pixel=im.getpixel((i,j))
        #         if (pixel>220) :
        #             print im.getpixel((i,j))
            
if __name__ == '__main__':
    rospy.init_node('map', anonymous=True)
    do=mapdrawing()
    x,y=do.position()

    print x,y
    do.draw(4,4)
 