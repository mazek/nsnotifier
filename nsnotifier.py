#!/usr/bin/python

import json, urllib2, os
from time import strftime, gmtime, localtime

ns_url = "http://ns.rajewski.pl/"
min = 80
max = 100

def notify(title, subtitle, message):
   t = '-title {!r}'.format(title)
   s = '-subtitle {!r}'.format(subtitle)
   m = '-message {!r}'.format(message)
   snd = '-sound \'default\''
   url = '-open %s' % ns_url
   group = '-group 666000666'
   
   appIcon = '-appIcon http://www.nightscout.info/wp-content/uploads/2014/07/Nightscout.png'

   os.system('/usr/local/bin/terminal-notifier {}'.format(' '.join([m, t, s, snd, url, appIcon, group])))


j = urllib2.urlopen('%s/pebble' % ns_url)

data = json.load(j)

cur_time = data['status'][0]['now']
read_time = data['bgs'][0]['datetime']

if cur_time - read_time > 1800000:
   lost_time = strftime("%d %b %Y %H:%M",localtime(read_time/1000))
   notify(title    = 'Nightscout read.',
          subtitle = '',
          message  = 'I\'ve lost parakeet signal at: %s' % (lost_time))

else:
   bwpo = data['bgs'][0]['sgv']
   bgdelta = data['bgs'][0]['bgdelta']

   if bgdelta > 0:
      bgdelta_s = "+%s" % bgdelta
   else:
      bgdelta_s = "%s" % bgdelta

   if bwpo < min or bwpo > max:
      notify(title    = 'Nightscout read.',
             subtitle = '',
             message  = 'Sugar: %s, change: %s' % (bwpo, bgdelta_s))


