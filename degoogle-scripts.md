*diamonddev presents:*
# `degoogle` scripts in this repo
BEFORE YOUR READ: Please read the [general guide](https://github.com/diam0ndkiller/degoogle/blob/main/de-google%20android.md) first.

In this repo there are three scripts made to automatically de-google your phone. They can be found in the scripts folder. To run them, download the repo.

You will need to install **adb** (the Android Debug Bridge), guides to do that are all around the internet. Then you will have to enable *Settings - System - Developer Options - USB Debugging* and connect your phone to your PC with your cable. For the F-Droid installer script you will also need to install [`fdroidcl`](https://github.com/mvdan/fdroidcl) on your system, available on Windows and Linux. Requires Go 1.19 or later.

The three scripts are:
## `degoogle_android.py`
This is a python script to manage the other two scripts and show general information.
## `install_fdroid_apps.py`
This script is responsible of installing open-source apps from F-Droid (and also installing F-Droid itself). It can't break stuff that easily because it is only adding apps.

## `uninstall_google_apps.py`
This is the critical script. It UNINSTALLS most of Google's non-essential software from your phone. You can choose, what apps you want to uninstall. DO READ the descriptions of the apps you want to uninstall in this script.


**DISCLAIMER:**

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
