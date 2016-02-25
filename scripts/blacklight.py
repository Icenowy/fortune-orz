#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import html
import urllib.request

XML_URL = 'https://github.com/PaperAirplane-Dev-Team/BlackLight/raw/geng/blacklight-base/src/main/res/values-zh-rCN/splashes.xml'

with urllib.request.urlopen(XML_URL) as f:
    src = f.read().decode('utf-8')

src = src.split('<string-array name="splashes">')[1].split('</string-array>')[0]
seen = set()
with open('blacklight', 'w', encoding='utf-8') as f:
    for item in src.split('</item>'):
        s = item.strip()
        if s.startswith('<item>'):
            s = html.unescape(s[6:].replace('\\n', '\n').replace('\\"', '"').replace("\\'", "'"))
            if s not in seen:
                f.write(s + '\n')
                f.write('%\n')
                seen.add(s)
