import subprocess
import os,sys,time
import signal

class Launcher:

    def __init__(self):
        self.current_path = os.getcwd()

    def launch_roscore(self):
        subprocess.Popen(['bash ' + self.current_path + '/start_roscore.bash'],shell=True)

    def kill_roscore(self):
        subprocess.call(['pkill', '-f', 'roscore'])

    def roslauncher(self):
        subprocess.Popen(['bash ' + self.current_path + '/start_roslauch.bash'],shell=True)

    def kill_roslaunch(self):
        subprocess.call(['pkill', '-f', 'HyphaROS_MiniBot_Nav.launch'])


if __name__ == "__main__":
    laucher = Launcher()
    # laucher.roslauncher()
    # time.sleep(5)
    # laucher.kill_roslaunch()