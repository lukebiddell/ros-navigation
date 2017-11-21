#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class RobotVoiceOperation:
    #define the constructor of the class
    def  __init__(self):
        #initialize the ROS node with a name voice_op
        rospy.init_node('voice_op')

        # Publish the String message to the audio_conntrol topic
        self.movement_pub= rospy.Publisher('audio_control', String, queue_size=5)

        # Subscribe to the /recognizer/output topic to receive voice commands.
        rospy.Subscriber('/recognizer/output', String, self.voice_command_callback)

        #create a Rate object to sleep the process at 5 Hz
        rate = rospy.Rate(5)

        # Initialize the movement command message we will publish.
        self.movement_str = '0'



        # A mapping from keywords or phrases to commands
        #we consider the following simple commands, which you can extend on your own
        self.commands =        ['forward',
                                'slight-left',
                                'slight-right',
                                'stop',
                                'rotate-left',
                                'rotate-right',
                                'backward',
                                'voice control',
                                'twitch control',
                                ]
        rospy.loginfo("Ready to receive voice commands")
        # We have to keep publishing the movement_str message if we want the robot to keep moving.
        while not rospy.is_shutdown():
            self.movement_pub.publish(self.movement_str)
            rate.sleep()


    def voice_command_callback(self, msg):
        # Get the motion command from the recognized phrase
        command = msg.data
        if (command in self.commands):
            if command == 'forward':
                self.movement_str = '1'
            elif command == 'slight-left':
                self.movement_str = '2'
            elif command == 'slight-right':
                self.movement_str = '3'
            elif command == 'stop':
                self.movement_str = '4'
            elif command == 'rotate-left':
                self.movement_str = '5'
            elif command == 'rotate-right':
                self.movement_str = '6'
            elif command == 'backward':
                self.movement_str = '7'
            elif command == 'voice-control':
                #TODO
            elif command == 'twitch-control':
                #TODO

        else: #command not found
            print 'command not found: '+command
            self.movement_str = '0'
        print ("command: " + command)



if __name__=="__main__":
    try:
      RobotVoiceOperation()
      rospy.spin()
    except rospy.ROSInterruptException:
      rospy.loginfo("Voice navigation terminated.")
