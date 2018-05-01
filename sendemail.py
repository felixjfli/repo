import tensorflow as tf
from tensorflow.python.ops import rnn_cell
'''
lstm_hidden_size = 3
batch_size =100
loss =0.0
num_steps= 3000

lstm = tf.rnncell.BasicLSTMCell(lstm_hidden_size)
state = lstm.zero_state(batch_size=batch_size,dtype=tf.float32)

for i in range(num_steps):
    if i>0:
        tf.get_variable_scope().reuse_variables()
        lstm_output,state = lstm(current_input,state)
        final_output = fully_connected(lstm_output)
        loss += calc_loss(final_output,expected_output)
'''

import configparser
from time import sleep
#import WeChat
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


import urllib2


class checkurl(object):
    def __init__(self,file):
        self.file=file
        self.cfg=configparser.ConfigParser()

    def cfg_load(self):
        self.cfg.read(self.file)
        self.allurl=self.cfg.items('yuming')
        self.reload=self.cfg.get('time','reload')
        self.sender=self.cfg.get('mailto','sender')
        self.receiver = self.cfg.get('mailto', 'receiver')
        self.retrytimes=self.cfg.get('retry','times')

        self.passwd=self.cfg.get('mailto','passwd')

    def sendmessage(self,errinfo):
        #wechat.send('@all',errinfo)
        message = MIMEMultipart()
        message['From'] = Header("beibei", 'utf-8')
        message['To'] = Header("beibeisina", 'utf-8')
        subject = 'Python SMTP mail test'

        message['Subject'] = Header(subject, 'utf-8')
        message.attach(MIMEText(errinfo, 'plain', 'utf-8'))
        #for key,values in self.mailto:
        try:
            smtp = smtplib.SMTP_SSL('smtp.qq.com',port=465)
            smtp.login(self.sender, self.passwd)
            smtp.sendmail( self.sender, self.receiver,message.as_string())
            smtp.quit()
            print('success')
        except smtplib.SMTPException:
            print "Error: cannot send email"




    def cfg_dump(self):
        while True:
            for k,v in self.allurl:
                checknum=0
                #try times

                while checknum < int(self.retrytimes):
                    print (v, ' checknum', checknum, 'retrytimes', int(self.retrytimes))
                    try:
                        strHtml = urllib2.urlopen(v).read()
                        print(strHtml[0:20])
                        break
                    except:
                        errinfo=v+' is error'
                        print(errinfo+'please wait ,try',checknum+1,'times...')
                        sleep(1)
                        if checknum == int(self.retrytimes)-1:
                            print('still cannot connect , send email...')
                            self.sendmessage(errinfo)

                    checknum=checknum+1
            print('-----------------------------------')
            nextcheck=0
            while nextcheck < int(self.reload):
                print('before next check',int(self.reload)-nextcheck,'minutes')
                sleep(60)
                nextcheck=nextcheck+1

if __name__ =='__main__':
    #mail=Mail.sendmail()
    #wechat=WeChat.WeChat()
    check=checkurl('yuming.ini')
    check.cfg_load()
    check.cfg_dump()
