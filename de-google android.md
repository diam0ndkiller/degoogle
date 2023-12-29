*diamonddev presents:*
# How to de-Google your android phone in (pretty) simple steps
## 1. Get F-Droid
[F-Droid](https://f-droid.org) is an alternative android app store. In F-Droid, there are only FOSS (Free Open Source Software) applications available, so everyone can see what the app actually does and how much it tracks you. The first step for you to take is to try alternatives to default apps.
**From now on, whenever you need an app, search F-Droid first!**
This is also required for the next steps.
## 2. Find alternatives to Google's default apps
By default, Google packs a ton of apps with your phone. Most of them you actually need, but Google's ones aren't exactly private. So some alternatives must be found. For almost all basic phone needs, there is an app in F-Droid.
**I would suggest the [Simple Mobile Tools](https://simplemobiletools.com) library for most of them. They include for example a Gallery, Calendar and even SMS and Phone apps.**
They are all available in F-Droid and completely FOSS.
As a replacement for Chrome you can use any browser you like. You can use Firefox or Brave, both on Google Play (look below how to get access to that) or the DuckDuckGo browser on F-Droid.
## 3. Install Aurora
The [Aurora Store]() is by definition another alternative app store, but actually it is an interface for you to download ALL free apps from Google Play anonymously and without the Play Store.
**Whenever you don't find an app you need in F-Droid, look on Aurora to get it from Google Play.**
This often applies to company specific apps.
## 4. Remove Google's default apps
Once you have an alternative app for your need, you are going to want to uninstall the Google app. Most phones block the removal of these system apps however. To still do it, you have three options:
### 4.1. Deactivate apps
In Android, you have the ability to **deactivate apps which you can't uninstall**. That will leave the app on your device, but stop it from running and showing icons.
**This is the easiest option to just have it out of the way.**
Just go to *Settings - Apps - All apps - [your app]* and press deactivate.
### 4.2. Uninstall using Shizuku and Canta
For devices running at least Android version 9.0 you can use the [Canta](https://f-droid.org/en/packages/org.samo_lego.canta) from F-Droid. This app uses [Shizuku](https://shizuku.rikka.app/download/) for permissions to uninstall system apps.
**This is a far more complex but still graphical way to uninstall system apps.**
You are going to setup debugging for Shizuku to work. For that, you need developer options. Go to *Settings - Device* and press the build number option at the bottom 8 times. Then go to *Settings - System - Developer options* and enable **Wireless Debuging**. Then follow the instructions in the Shizuku app to pair and start the service. When you're done, you can start Canta and get to uninstalling apps.
### 4.3. Uninstalling via adb
If you like the terminal more than graphical apps, you can use adb (the Android Debug Bridge) to connect to your phone from a PC via your USB-Cable. For that, go to *Settings - System - Developer options* and enable **USB-Debugging*. On your system, [install the ADB tools](https://www.xda-developers.com/install-adb-windows-macos-linux/) and open a terminal / cmd window.
**This is a more complex approach, so you would want to have some knowledge with the terminal or cmd first.**
Run `adb shell` to open the shell on your phone.
Now, search your apps in *Settings - Apps - All apps* on your phone and scroll to the bottom of the page to see the id (e.g. `com.google.android.phone`).
In the adb shell, run `pm uninstall -k --user 0 [app id]` and your app is gone forever!
## 5. Remove Google Play
At this point, you should have all your default apps replaced with FOSS alternatives from F-Droid and whenever you need a proprietary app, you get it from the Aurora Store. Now you can choose:
### 5.1. You're done
Congrats, you found alternatives for most of your uses. Whenever you do actually need a Google specific app or a paid app, you can get it from the Play Store, which you still have installed, but most of the time you are away from Google. In that case you should double-check your permissions for the Google apps. E.g. you're using the Gboard (Google's Keyboard app): Block it's internet usage in *Settings - Apps - All apps - Gboard* and remove all other non-logical permissions for your app (Why should my keyboard app now my location?)
### 5.2. Remove Google Play Store
If you are confident you can make it without, you can now uninstall the Google Play Store. Do it through your preferred method like all the other apps.
**NOW, YOU CAN'T INSTALL PAID APPS ANYMORE.**
### 5.3. Remove Google Play Services
If you want to block ALL possible Google impact, you can uninstall the Google Play Services. They are responsible for connecting apps to the Google Servers.
**BUT CAUTION: Also some non-Google apps from Aurora use the Play Services for some functions e.g. integrated maps. Double-Check your apps still work by first deactivating Google Play.**
You can also constantly have it deactivated if you only need an app which requires it rarely.
