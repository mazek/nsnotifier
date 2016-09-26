#!/usr/bin/python

import json, urllib2, os

ns_url = "http://ns.rajewski.pl/"
min = 80
max = 160

def notify(title, subtitle, message):
   t = '-title {!r}'.format(title)
   s = '-subtitle {!r}'.format(subtitle)
   m = '-message {!r}'.format(message)

   snd = '-sound \'default\''

   url = '-open %s' % ns_url
   appIcon = '-appIcon http://www.nightscout.info/wp-content/uploads/2014/07/Nightscout.png'
   os.system('/usr/local/bin/terminal-notifier {}'.format(' '.join([m, t, s, snd, url, appIcon])))


j = urllib2.urlopen('%s/pebble' % ns_url)

data = json.load(j)

bwpo = data['bgs'][0]['bwpo']
bgdelta = data['bgs'][0]['bgdelta']

if bgdelta > 0 :
   bgdelta_s = "+%s" % bgdelta

if bwpo < min or bwpo > max:
   notify(title       = 'Nightscount read.',
             subtitle = '',
             message = ' Sugar: %s, change: %s' % (bwpo, bgdelta_s))

