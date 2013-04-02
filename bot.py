"""
A bot the post quotes from The Fast and the Furious franchise.

reddit's API rules
https://github.com/reddit/reddit/wiki/API

#reddit api
https://praw.readthedocs.org/en/latest/

#subs api
https://github.com/byroot/pysrt
"""
import os
import random

#python reddit API
import praw

#SRT subtitle API
from pysrt import SubRipFile

#get our sekrit credentials and things
from Secret import bot_name, bot_pass, bot_useragent

#the directory where all .srt's are kept
SUBTITLES_DIR  =  'Subtitles/'
SRT_EXT        =  '.srt'


#a function to get a random subtitle line from an open srt
def GetRandomSubLine(srt):
   return srt[random.randint(0, len(srt) - 1)].text


#the object which holds the open subtitles
subs = None

#get first subtitles from dir
for files in os.listdir(SUBTITLES_DIR):
   if files.endswith(SRT_EXT):
      print files
      subs = SubRipFile.open(SUBTITLES_DIR + files)

print 'subs len = ' + str(len(subs))
print 'line 0 = ' + str(subs[0].text)

#connect to reddit
rdt = praw.Reddit(user_agent=bot_useragent)

#login
res = rdt.login(bot_name, bot_pass)

#res == None is good I think. Not sure if returns error
print 'reddit login res = ' + str(res)

#the flag to keep us running or die
Run = True

while Run:
   #search for relevant posts on reddit
   print GetRandomSubLine(subs)

