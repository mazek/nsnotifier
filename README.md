Simple notifier for Mac OS X. It grabs data from pebble endpoint on nightscout site and show it as notification on desktop vie notify() command.


$ launchctl load ~/Library/LaunchAgents/com.nightscout.notifier.plist 
$ launchctl start com.nightscout.notifier.plist 
$ launchctl stop com.nightscout.notifier.plist 
$ launchctl unload ~/Library/LaunchAgents/com.nightscout.notifier.plist 
$ launchctl list | grep night


