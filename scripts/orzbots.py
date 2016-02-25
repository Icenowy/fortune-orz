#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This script collects selected quotes of bot "Orizon" and "Peter Bot"
from a tg-export v2 database.
'''

import re
import sys
import sqlite3

def uniq(seq): # Dave Kirby
    # Order preserving
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]

re_irc = re.compile('^\[\w+\]')

# The database is in tg-export v2 format
db = sqlite3.connect(sys.argv[1])
cur = db.cursor()

# 欧瑞珍 aka. Orizon, orzdigbot
Orizon = '$01000000352b2d0768a508a944a63d60'
# Peter Bot
PeterBot = '$0100000039e5d9062e85b4f94e6d02df'

Groups = (
# 欧瑞珍黑历史
'$050000006e33203c547d7dcf6323cfb4',
# 机器人真噫 ~ 黑历史收集器
'$0200000066bad0010000000000000000'
)

quotes_orizon = []
quotes_peterbot = []

for fwd_src, text in cur.execute('SELECT fwd_src, text FROM messages WHERE dest = ? OR dest = ? ORDER BY fwd_date, date ASC', Groups):
    if fwd_src == Orizon and re_irc.match(text) is None:
        quotes_orizon.append(text)
    elif fwd_src == PeterBot:
        quotes_peterbot.append(text)

with open('orizon', 'w', encoding='utf-8') as f:
    for q in uniq(quotes_orizon):
        f.write(q)
        f.write('\n%\n')

with open('peterbot', 'w', encoding='utf-8') as f:
    for q in uniq(quotes_peterbot):
        f.write(q)
        f.write('\n%\n')
