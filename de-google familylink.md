*diamonddev presents:*
# De-Google Part 2: FamilyLink -> TimeLimit
When having kids with phones, you probably have them restricted using Google's FamilyLink. But if you read this guide, you are probably more interested in FOSS software, which Google's apps are not. So here is the solution:
#### TimeLimit.io
[TimeLimit](https://timelimit.io) is a FOOS app available in F-Droid to limit app usage times on android. It is capable of setting different limits for custom app categories and is controllable from either the phone itself or another phone via the Connected Mode.
#### Setup
To setup TimeLimit, you have two options:
##### Local Mode
Setting up TimeLimit in Local Mode is pretty straight-forward. You get the app from F-Droid on you child's phone and follow the setup instructions for the Local Mode. You will setup a parent password and end up with two users, one for the parent and one for the child.
##### Connected Mode
In this mode, you can manage the apps on your child's phone from your own phone like in FamilyLink. For that, **first** install TimeLimit on your own phone and setup using the *Connected Mode - Parent e-mail addressl*. You will enter your E-Mail and  create a user in the next steps. Confirm your E-Mail and set a password and username. These are only used in the app to authenticate you're a parent. Once setup on your own phone, you can get TimeLimit on your child's phone and setup in *Connected Mode - Code from another TimeLimit installation*. Now scan the QR-Code or enter the pairing code shown on your device when pressing **Add device** in TimeLimit. Go through the password creation steps and you're done.
#### 2. Setup TimeLimit
TimeLimit is all about categories. Every app that isn't in a category gets blocked by default and you can set rules for every single category.
I would suggest a four-category setup:
##### Emergency
In this category you add all the emergency messenger / phone apps that need to always be available for you child. You don't add any rules.
##### Allowed Apps
This category will contain all normal apps you want to put a limit for. In the *Add Apps* panel, uncheck the *Show apps in other categories* box and select all to add. That will result in all non-system non-emergency apps to be added to this category. In this category, you will add the rules for phone usage, e.g. daily 1 hour or block (set to 0 hours 0 minutes) between certain times.
##### System
By default, all apps are blocked, so also all system services are blocked. This includes a lot of essential, normally hidden apps. You are going to want to allow all of them by default. So again in *Add Apps* uncheck the other categories box and then check the *Show System Apps* box. Now select all and add. This will add all system apps and services to this category. You don't set any rules for this category either.
##### Operator
This last category contains administrative apps. You should put all the app stores (F-Droid, Aurora, Play Store) there. That will remove them from the Allowed Apps category. You should also add the system app "Package Installer" to that category, responsible of installing APK-Files. If you have Canta and / or Shizuku installed from the first part, put them here too.
The one Rule for this category will be 0 hours 0 minutes (blocked) for all days of the week.
#### 3. Using TimeLimit
TimeLimit will now block apps with their time limit used up or blocked from access by the child. If you want to install another app, you can press the toggle for the Operator category and *disable limits* for today or 10 minutes. When you're done, just hit the toggle again and the limits are back on.
#### 4. Cons
TimeLimit is only able to limit apps. If you want to limit internet access, you should consider a VPN (virtual private network). The other method is staying on Google Chrome with Play Services and blocking pages through the Google Account and FamilyLink, although that kind of destroys the reason of this mod.