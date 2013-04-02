"""
A bot the post quotes from The Fast and the Furious franchise.

reddit's API rules
https://github.com/reddit/reddit/wiki/API

https://praw.readthedocs.org/en/latest/
"""

#python reddit API
import praw

#get our sekrit credentials and things
from Secret import bot_name, bot_pass, bot_useragent

#connect to reddit
rdt = praw.Reddit(user_agent=bot_useragent)

#login
res = rdt.login(bot_name, bot_pass)

#res == None is good I think. Not sure if returns error
print 'login res = ' + str(res)

