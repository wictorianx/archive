import os
import pickle
action = []
app = []
apps = []
locations = []
syntax = "TASKKILL /F /IM "
path = "app locations.pkl"
def Synchronize(apps, locations):
	if os.path.getsize("app locations.pkl") > 0:
		fh = open("app locations.pkl", "rb+")
		apps = pickle.load(fh)
		locations = pickle.load(fh)
		return (apps, locations)
	else:
		return(False)
def registAppsAndLocations(apps, locations):
	apps.append(app[len(app)-1])
	locations.append(input("type location"))
	fh = open("app locations.pkl", "wb")
	pickle.dump(apps,fh)
	pickle.dump(locations,fh)
def CloseApp(app):
	if "." in app:
		os.system(syntax+app)
	elif app == "os":
		os.system("shutdown /s /t 1")
	else:
		os.system(syntax+(app+".exe"))
def OpenApp(app):
	os.startfile(locations[apps.index(app)])
def Execute(action, app):
	if "c" in action and "l" in action and "o" in action and "s" in action and "e" in action:
		CloseApp(app)
	elif "o" in action and "p" in action and "e" in action and "n" in action:
		OpenApp(app)
	elif "r" in action and "e" in action and "g" in action and "i" in action and "s" in action and "t" in action:
		registAppsAndLocations(apps, locations)
f = open("app locations.pkl", "w+")
f.close()


if Synchronize(apps, locations) != False :
	fakeApps, fakeLocations = Synchronize(apps, locations)
	apps.append(fakeApps)
	locations.append(fakeLocations)
while(True):
	try:
		CloseApp("AdobeGCClient.exe")
	except: print("Adobe was not opened") 
	fakeAction = input("Type Action\n")
	fakeApp = input("Type App \n")
	if "r" in fakeAction and "e" in fakeAction and "g" in fakeAction and "i" in fakeAction and "s" in fakeAction and "t" in fakeAction:
		if input("COMMIT? \n") == "COMMIT":
			action.append(fakeAction)
			app.append(fakeApp)
	else:
		action.append(fakeAction)
		app.append(fakeApp)
	print(action)
	print(app)
	Execute(action[len(action)-1], app[len(app)-1])


