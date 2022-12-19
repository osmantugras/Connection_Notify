import Foundation
import objc
import AppKit
import sys
import os
from colorama import Fore, Back, Style
python = sys.executable

NSUserNotification = objc.lookUpClass('NSUserNotification')
NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')

def notify(title, subtitle, info_text, delay=0, sound=False, userInfo={}):
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setSubtitle_(subtitle)
    notification.setInformativeText_(info_text)
    notification.setUserInfo_(userInfo)
    if sound:
        notification.setSoundName_("NSUserNotificationDefaultSoundName")
    notification.setDeliveryDate_(Foundation.NSDate.dateWithTimeInterval_sinceDate_(delay, Foundation.NSDate.date()))
    NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)

def wait_connection():
    hostname = "google.com" #example
    response = os.system("ping  -c 3 " + hostname)
    while response != 0 :
      response = os.system("ping  -c 3 " + hostname)
    else:
      notify("Netowk Connection", "Network Connection", "Network Connection is UP", sound=True)
      sys.stdout.write("Notification sent...\n")


hostname = "google.com" #example
response = os.system("ping  -c 3 " + hostname)
while response == 0 :
  response = os.system("ping  -c 3 " + hostname)
else:
 notify("Netowk Connection", "Network Connection", "Network Connection is Down", sound=True)
 sys.stdout.write("Notification sent...\n")
 wait_connection()
 
      
      
os.execl(python, python, * sys.argv)