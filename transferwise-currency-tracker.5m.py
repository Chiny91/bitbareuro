#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <bitbar.title>Currency Tracker Transferwise</bitbar.title>
# <bitbar.version>1.0</bitbar.version>
# <bitbar.author>Andrew Keating</bitbar.author>
# <bitbar.author.github>andrewzk</bitbar.author.github>
# <bitbar.desc>Keep an eye on Transferwise currency exchange rates</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.image>http://andrewzk.github.io/gh-pages/transferwise.png</bitbar.image>

# Downloaded 14/5/17 and hacked that very day

import urllib2
import json

import os
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
# Exactly how the notification is presented is controlled by the “Notifications” preferences in System Preferences

TRANSFERWISE_KEY = "dad99d7d8e52c2c8aaf9fda788d8acdc"

# Variables to be set
currency_from = 'GBP'
currency_to = 'EUR'
watch_level = 1.185

url = "https://transferwise.com/api/v1/payment/calculate?amount=1" \
      "&amountCurrency=source&hasDiscount=false&isFixedRate=false" \
      "&isGuaranteedFixedTarget=false" \
      "&sourceCurrency={}&targetCurrency={}".format(currency_from, currency_to)

req = urllib2.Request(url)
req.add_header('X-Authorization-key', TRANSFERWISE_KEY)

result = json.loads(urllib2.urlopen(req).read())['transferwiseRate']

if result > watch_level:
    print '\033[31m', "{}: {:.4f}".format(currency_to, result)
    notify_text = str(currency_to) + " hit watch level of " + str(watch_level)
    notify("Transferwise", notify_text)
else:
    print "{}: {:.4f}".format(currency_to, result)
print "---"
print "From: {}".format(currency_from)
print 'Go to Transferwise | href="https://transferwise.com"'