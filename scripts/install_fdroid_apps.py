#!/bin/python3
import os
import subprocess

def fdroidcl_init():
	print("\x1b[93mSee if your device is found:\x1b[0m")
	os.system("fdroidcl devices")
	print()
	print("\x1b[93mTesting fdroidcl:\x1b[0m")
	os.system("fdroidcl update")
	if os.system("fdroidcl install org.fdroid.fdroid"):
		print("\x1b[91mfdroidcl failed (see above for reason)\x1b[0m")
		return False
	print("\x1b[92mfdroidcl working as expected.\x1b[0m")
	return True

def install_app(app: str):
	return not bool(os.system(f"fdroidcl install {app}"))

def ask_app_install(app: str):
	print("\x1b[36m")
	os.system(f"fdroidcl search {app}")
	res = input(f"\x1b[94mInstall \x1b[96m{app}\x1b[94m (\x1b[92mY\x1b[94m/\x1b[91mn\x1b[94m)?\x1b[0m ")
	if res.lower() == "y": return install_app(app)
	else: return True

FDROID_CORE_APPS = [
	"com.simplemobiletools.calculator",
	"com.simplemobiletools.calendar.pro",
	"com.simplemobiletools.camera",
	"com.simplemobiletools.clock",
	"com.simplemobiletools.contacts.pro",
	"com.simplemobiletools.dialer",
	"com.simplemobiletools.filemanager.pro",
	"com.simplemobiletools.gallery.pro",
	"com.simplemobiletools.launcher",
	"com.simplemobiletools.musicplayer",
	"com.simplemobiletools.notes.pro",
	"com.simplemobiletools.smsmessenger",
	"com.simplemobiletools.voicerecorder",
	"dev.patrickgold.florisboard",
	"com.fsck.k9",
	"org.documentfoundation.libreoffice",
	"com.duckduckgo.mobile.android"
]

FDROID_ADDITIONAL_APPS = [
	"com.zionhuang.music",
	"org.localsend.localsend_app",
	"org.schabi.newpipe",
	"com.github.andreyasadchy.xtra",
	"org.samo_lego.canta",
	"com.aurora.store"
]

def install_fdroid_apps():
	if not fdroidcl_init(): return
	print()
	print("\x1b[94mInstalling core applications...\x1b[0m")
	for i in FDROID_CORE_APPS:
		install_app(i)
	print("\n\x1b[94mChoose which other apps to install:\x1b[0m")
	for i in FDROID_ADDITIONAL_APPS:
		ask_app_install(i)

if __name__ == "__main__":
	install_fdroid_apps()
