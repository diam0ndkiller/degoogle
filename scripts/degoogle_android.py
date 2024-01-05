#!/bin/python3

from install_fdroid_apps import *
from uninstall_google_apps import *

POSTINSTALL_FIXES = '''
\x1b[91mAfter installation, please change these settings:
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
	install_fdroid_apps()
	uninstall_google_apps()
	print(POSTINSTALL_FIXES)


if __name__ == "__main__":
	degoogle_android()
