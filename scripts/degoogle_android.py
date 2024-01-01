#!/bin/python3

from install_fdroid_apps import *
from uninstall_google_apps import *
import time

PREINSTALL_DISCLAIMER = '''
\x1b[93mDISCLAIMER
This script REMOVES system applications and other tools you may need.

In general, after running, you won't have any Google-ACCOUNT specific software left on your phone. But because the Android operating system is partially built by Google, you will have a lot of their stuff left. If you DON'T want that, please try other operating systems.

Please first check if you have a supported device for some Android custom ROMS, because they have a better experience in general than changing your current operating system. Look for:
- /e/os
- LineageOS
- CalyxOS
- GrapheneOS

If you want to continue using some Google services, like syncing your photos or contacts, please PAY ATTENTION and READ DESCRIPTIONS when entering the uninstaller section.

DO READ the descriptions of MARKED (!!!) apps when uninstalling.

ONCE UNINSTALLED, MOST OF THE APPS AREN'T VERY EASY TO RE-INSTALL!
\x1b[0m'''

POSTINSTALL_FIXES = '''
\x1b[94mAfter installation, please change these settings:
- "Settings/Apps/Default apps":
  - set "Phone app" to "Dialer"
  - set "Home app" to "Launcher"

Open the FlorisBoard app and follow the steps to enable the keyboard.

Open the Aurora Store, initialize it and login anonymously.
From Aurora, install:
- "HERE WeGo" [Navigation replacement for Google Maps]
- "Shizuku" [Needed for uninstalling other apps with Canta]

Open the all orange apps in your app drawer and in their "Settings/Appearance" change the app icon color to make your apps a bit more colorful.

\x1b[92mCongrats, you are now de-googled to your liking!\x1b[0m'''

def degoogle_android():
	print(PREINSTALL_DISCLAIMER)
	print("Waiting 10 seconds to read...")
	time.sleep(10)
	confirm = input("\x1b[91mDID YOU READ THE DISCLAIMER AND ACCEPT ANY POSSIBLE BROKEN FUNCTIONS AFTER UNINSTALL? (Yes/No): \x1b[0m")
	if confirm.lower() != "yes": return
	install_fdroid_apps()
	uninstall_google_apps()
	print(POSTINSTALL_FIXES)


if __name__ == "__main__":
	degoogle_android()
