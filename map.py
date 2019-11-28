import rospy,tf
from geometry_msgs.msg import PoseWithCovarianceStamped
from PIL import Image
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt 
import threading

def draw():
    im = Image.open("1121.pgm")    
    width , height = im.size
    x=position[0]
    y=position[1]
    plt.imshow(im,cmap ='gray',origin='lower')
    print x,y
    plt.scatter(100*x+86,(-100*y+86), c = 'y',marker = 'o')
    # plt.scatter(x,y, c = 'y',marker = 'o')
    plt.imshow(im,cmap ='gray')
    plt.savefig("./static/show.jpg")
    plt.clf()
    print "haha"
    
            
if __name__ == '__main__':
    rospy.init_node('map', anonymous=True)
    position = (0,0,0)
    listener = tf.TransformListener()
    r = rospy.Rate(10)
    thread=threading.Thread(target=draw)
    thread.start()
    while not rospy.is_shutdown():
        try:
            # listener.waitForTransform("/map", "/base_link", rospy.Time(0), rospy.Duration(1))
            position, quaternion = listener.lookupTransform("/map", "/base_link", rospy.Time(0))
        except Exception as e:
            print e
        r.sleep()