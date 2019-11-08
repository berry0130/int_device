#!/usr/bin/env python
from PIL import Image
import cherrypy
import rospy
from geometry_msgs.msg import PoseStamped
from launcher import Launcher
import threading
config = {
    'global' : {
        'server.socket_host' : '192.168.3.3',
        'server.socket_port' : 8080
    }
}
class HelloWorld(object):

    def __init__(self):
        self.laucher = Launcher()

    @cherrypy.expose
    def index(self):

        # <input type="button" value="goalA" onclick="location.href='192.168.3.3:8080/goalA_to'">
        # ERIC https://github.com/VirtuosoEric/robot_web_service/blob/pn60/home.html
        
        f = open("t.html", "r")
        return f

    @cherrypy.expose
    def start(self):
        # t = threading.Thread(target=launch_nav)
        # t.daemon = True
        # t.start()
        self.laucher.roslauncher()
        f = open("strat.html", "r")
        return f

    @cherrypy.expose
    def kill(self):
        self.laucher.kill_roslaunch()
        return 'kill roscore'


    @cherrypy.expose
    def goalA_to(self):
        # rospy.init_node('berry_goal', anonymous=True)
        pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)          
        goal = PoseStamped()
        goal.header.frame_id = "map"
        # goal.header.stamp = rospy.Time.now()
        goal.pose.position.x = 3
        goal.pose.position.y = 0
        goal.pose.position.z = 0
        goal.pose.orientation.w = 1.0
        pub.publish(goal)
        return 'goal to!'
    @cherrypy.expose
    def goalA_leave(self):
        pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)          
        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.header.stamp = rospy.Time.now()
        goal.pose.position.x = 0
        goal.pose.position.y = 0
        goal.pose.position.z = 0
        goal.pose.orientation.w = 1.0
        pub.publish(goal)
        return 'goal leave!'
    @cherrypy.expose
    def goalB_to(self):
        # f = open("latop.html", "r")
        return 'Hello!'
    @cherrypy.expose
    def goalB_leave(self):
        # f = open("latop.html", "r")
        return 'Hello!'
    @cherrypy.expose
    def goalC_to(self):
        # f = open("latop.html", "r")
        return 'Hello!'
# def launch_nav():
#     laucher = Launcher()
#     laucher.roslauncher()
def startCherry():
    cherrypy.quickstart(HelloWorld(), '/',config)
if __name__ == '__main__':
    # laucher = Launcher()
    # laucher.launch_roscore()
    t = threading.Thread(target=startCherry)
    t.daemon = True
    t.start()
    # cherrypy.quickstart(HelloWorld(), '/',config)
    rospy.init_node('berry_goal', anonymous=True)
    rospy.spin()