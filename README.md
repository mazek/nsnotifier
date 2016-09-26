Simple notifier for Mac OS X. It grabs data from pebble endpoint on nightscout site and show it as notification on desktop vie notify() command.

```
$ launchctl load ~/Library/LaunchAgents/com.nightscout.notifier.plist 
$ launchctl start com.nightscout.notifier 
$ launchctl stop com.nightscout.notifier
$ launchctl unload ~/Library/LaunchAgents/com.nightscout.notifier.plist 
$ launchctl list | grep night
```

![](https://github.com/mazek/nsnotifier/blob/master/notification-screenshot.png)

