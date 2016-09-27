#!/bin/bash

LAUNCHCTL="/bin/launchctl"

$LAUNCHCTL stop com.nightscout.notifier
$LAUNCHCTL unload ~/Library/LaunchAgents/com.nightscout.notifier.plist
$LAUNCHCTL load ~/Library/LaunchAgents/com.nightscout.notifier.plist 
$LAUNCHCTL start com.nightscout.notifier


