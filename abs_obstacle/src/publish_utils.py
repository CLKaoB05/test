#!/usr/bin/env python

import rospy
import message_filters
import math
import re
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Header

def get_near_number(number):
  if int(number) is int(round(number,0)):
    return int(number) - 1
  else:
    return int(number) + 1
def publish_final_pos(positions):
    final_pos = ""
    for final in positions:
        final_pos += final
    obstacle_pub = rospy.Publisher('abs_obstacle',String,queue_size = 10)
    rospy.loginfo(final_pos)
    obstacle_pub.publish(final_pos)
class Server:
  def __init__(self):
    self.wamv_x = None
    self.wamv_y = None
    self.wamv_yaw = None
    self.obstacle_num = 0
    self.relative_x = []
    self.relative_y = []
    self.pre = None
    self.abs_x =[]
    self.abs_y =[]
    self.record_obstcle = {}
  def wamv_x_callback(self,msg):
    self.wamv_x = msg.data

  def wamv_y_callback(self,msg):
    self.wamv_y = msg.data

  def wamv_yaw_callback(self,msg):
    self.wamv_yaw = msg.data

  def pre_callback(self,msg):
    self.pre = msg.data
    
    self.compute()

  def compute(self):
    if self.wamv_x is not None and self.wamv_y is not None and self.wamv_yaw is not None and self.pre is not None:
      publish_list = []
      sin = math.sin(math.radians(self.wamv_yaw))
      cos = math.cos(math.radians(self.wamv_yaw))
      #print('wamv_x = ' + str(self.wamv_x) + ' ,wamv_y = ' + str(self.wamv_y) +' ,wamv_yaw = ' + str(self.wamv_yaw))
      obstacleRegex = re.compile(r'\D\d+.\d+')
      obslist = obstacleRegex.findall(str(self.pre))
      print ('obslist length:' + str(len(obslist)))
      for i in range(0,len(obslist),2):
        self.relative_x.append(float(obslist[i]))
        #print('relative_x = ' + obslist[i])
      for j in range(1,len(obslist),2):
        self.relative_y.append(float(obslist[j]))
        #print('relative_y = ' + obslist[j])
      counter = 0
      '''
      for k in range(len(self.relative_y)):
        print('k = ' + str(k))
        a = self.relative_y[k] 
      self.relative_y =[]
      '''
      for k in range(len(self.relative_y)):

        self.abs_x.append( self.wamv_x + self.relative_x[k] * sin - self.relative_y[k] * cos)
        self.abs_y.append( self.wamv_y + self.relative_x[k] * cos + self.relative_y[k] * sin)
        publish_list.append('( ' + str(self.abs_x[k]) + ' , ' + str(self.abs_y[k]) + ')')
        if ((int(self.abs_x[k]),int(self.abs_y[k])) not in self.record_obstcle.keys()):
          self.record_obstcle[int(self.abs_x[k]),int(self.abs_y[k])] = 'unknown: ' + str(self.obstacle_num)
          self.record_obstcle[get_near_number(self.abs_x[k]),get_near_number(self.abs_y[k])] = 'unknown: ' + str(self.obstacle_num)
          self.record_obstcle[get_near_number(self.abs_x[k]),get_near_number(self.abs_y[k])] = 'unknown: ' + str(self.obstacle_num)
          self.record_obstcle[int(self.abs_x[k]),get_near_number(self.abs_y[k])] = 'unknown: ' + str(self.obstacle_num)
          print('NEW OBSTACLE ADDED ' + str(self.obstacle_num))
          print(str([int(self.abs_x[k]),int(self.abs_y[k])]))
          self.obstacle_num = self.obstacle_num + 1
        else:
          print('obstacle position is:'+' ( ' + str(int(self.abs_x[k])) +' , '+str(int(self.abs_y[k])) + ' ) ') 
          #print( 'obstacle is ' + self.record_obstcle[int(self.abs_x[k]),int(self.abs_y[k])])


      #print('total obstacle is:' + str(self.obstacle_num))
        #print(str(k)+' ( ' + str(self.abs_x[k]) +' , '+str(self.abs_y[k]) + ' ) ')
      
      for i in self.record_obstcle.items():
       print(i)


      self.abs_x = []
      self.abs_y = []
      self.relative_x = []
      self.relative_y =[]
      publish_final_pos(publish_list)
   
        
     
