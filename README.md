# Py2MBScript
This Project aims to replace the old Module System with a pure Python alternative.  
Which means, that with this you can use if, for and other python things and also related objects.  
The goal is to make all related objects actually related in code, so that you can see the relation.  
Also there should be objects for related code patterns to simplify their implementation.  
  
For example the presentation module holds buttons, labels, etc. and, in the old module system  
there are several lines and different, sometimes confusing codes to implement these.  

For now this is only a test and kind of prove of concept trial.  
In the "test_cases" folder you can write the python versions of the otherwise MBScript versions of the thing.  
Later on, once you run:

```
python main.py
```  
your python code will be translated into good ol' MBScript style of code (if all goes well for now).  

Then you can simply run the build bat or python3 version of it (yes Python3) and done.  

(Before you run in, please check module_info.py and correct the path to your output folder!)  
    
  
# Info  
The following modules are currently not active:  
* Strings
* Meshes
* Partice System
* Skins
* Animations
* PostFX
* Tableau Materials
* Game Menus
* Skills
  
The reason for this is, that otherwise they would only have test values for now.   
And without actual correct values the Mod won't even start in a correct way.  
  
If you still want to activate them, you can go into main.py and uncomment the three lines below the # Module xyz line.  
In the future these will be activated again, once the code is equal to the necessary code for the Mod to run.  

