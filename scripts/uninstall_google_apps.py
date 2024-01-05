#!/bin/python3
import os
import subprocess
import sys
import time

adb_shell_cmd = "adb shell"

if len(sys.argv) > 1:
	device = sys.argv[1]
	adb_shell_cmd = f"adb -s {device} shell"

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

def check_disclaimer():
	print(PREINSTALL_DISCLAIMER)
	print("Waiting 10 seconds to read...")
	time.sleep(10)
	confirm = input("\x1b[91mDID YOU READ THE DISCLAIMER AND ACCEPT ANY POSSIBLE BROKEN FUNCTIONS AFTER UNINSTALL? (Yes/No): \x1b[0m")
	if confirm.lower() != "yes": return

def adb_init():
	print("\x1b[93mSee if your device is found:\x1b[0m")
	os.system("adb devices")
	print()
	print("\x1b[93mTesting adb:\x1b[0m")
	if os.system(f"{adb_shell_cmd} echo"):
		print("\x1b[91madb failed (see above for reason)\x1b[0m")
		return False
	print("\x1b[92madb working as expected.\x1b[0m")
	return True

def remove_app(app: str):
	return not bool(os.system(f"{adb_shell_cmd} pm uninstall -k --user 0 {app}"))

def ask_app_remove(app: str, description: str):
	print(f"\x1b[96m\n{app}\x1b[36m: {description}\x1b[0m")
	res = input(f"\x1b[91mRemove \x1b[96m{app}\x1b[94m (\x1b[92mY\x1b[94m/\x1b[91mn\x1b[94m)?\x1b[0m ")
	if res.lower() == "y": return remove_app(app)
	else: return True

GOOGLE_REPLACED_APPS = {
	"com.google.android.calendar": "Google's Calendar [replacement NOT synced]",
	"com.google.android.camera": "Google's Camera app",
	"com.android.camera2": "Android's default Camera app",
	"com.google.android.deskclock": "Google's Clock app",
	"com.google.android.contacts": "Google's Contact app [replacement NOT synced]",
	"com.google.android.dialer": "Google's Phone Dialer app",
	"com.google.android.apps.photos": "Google's Photos [replacement NOT synced]",
	"com.google.android.gm": "Gmail app",
	"com.google.android.googlequicksearchbox": "Google Search app",
	"com.google.android.apps.messaging": "Google's SMS app",
	"com.google.android.inputmethod.latin": "Gboard Keyboard",
	"com.google.android.apps.youtube.music": "YouTube Music [replacement NOT synced]",
	"com.google.android.youtube": "YouTube [replacement NOT synced]",
	"com.google.android.apps.wellbeing": "Google Digital Wellbeing",
	"com.android.chrome": "Google Chrome"
}

GOOGLE_UNREPLACED_APPS = {
	"com.google.android.apps.maps": "Google Maps [Replacement in the Aurora Store]",
	"com.google.android.apps.docs": "Google Drive [No ONE logical Replacement]",
	"com.android.vending": "Google Play Store [Only needed for Paid apps]",
	"com.google.android.gms": "!!! Google Play Services [RESPONSIBLE FOR MOST TRACKING, NEEDED FOR SOME APPS TO RUN, also BREAKS SETTINGS SEARCH BAR (idk why)]",
	"com.google.android.gsf": "!!! Google Play Services Framework [NEEDED FOR GMS]",
	"com.google.android.gms.supervision": "Google Parental Control Services [Needed for FamilyLink]",
	"com.google.android.odad": "Google Play Protect [Only uninstall when removing services]",
	"com.google.android.apps.nexuslauncher": "!!! Default Google homescreen [BREAKS SYSTEM GESTURE NAVIGATION]"
}

def uninstall_google_apps():
	if not adb_init(): return
	print()
	print("\x1b[94mThese apps have replacements already installed:\x1b[0m")
	for k, i in GOOGLE_REPLACED_APPS.items():
		ask_app_remove(k, i)
	print("\n\x1b[94mThese apps DON'T have any replacements or not yet installed (DO READ):\x1b[0m")
	for k, i in GOOGLE_UNREPLACED_APPS.items():
		ask_app_remove(k, i)

if __name__ == "__main__":
	uninstall_google_apps()
