Simple notifier for Mac OS X. It grabs data from pebble endpoint on nightscout site and show it as notification on desktop vie notify() command.

There is no installer at the omment but there is also good news - it's ultra simple. You've got two files: "com.nightscout.notifier.plist" and "nsnotifier.py". To install this "software" all You have to is:


Edit __nsnotifier.py__ top variables:

```
ns_url = "http://ns.rajewski.pl/"
min = 80
max = 160
```

and then do:


```
cp com.nightscout.notifier.plist ~/Library/LaunchAgents/
sudo cp nsnotifier.py /usr/local/bin/

```

To load for the first time __notifier__ do:

```
$ launchctl load ~/Library/LaunchAgents/com.nightscout.notifier.plist
$ launchctl start com.nightscout.notifier
```

Some helpful commands:

```
$ launchctl load ~/Library/LaunchAgents/com.nightscout.notifier.plist 
$ launchctl start com.nightscout.notifier 
$ launchctl stop com.nightscout.notifier
$ launchctl unload ~/Library/LaunchAgents/com.nightscout.notifier.plist 
$ launchctl list | grep night
```

![](https://github.com/mazek/nsnotifier/blob/master/notification-screenshot.png)

