# Py2MBScript
This Project aims to replace the old Module System with a pure Python alternative.  
Which means, that with this you can use if, for and other python things and also related objects.  
The goal is to make all related objects actually related in code, so that you can see the relation.  
Also there should be objects for related code patterns to simplify their implementation.  
  
For example the presentation module holds buttons, labels, etc. and, in the old module system  
there are several lines and different, sometimes confusing codes to implement these.  

For now this is only a test and kind of prove of concept trial.  
In the "test_cases" folder you can write the python versions of the otherwise MBScript versions of the thing.  
(Later or also currently some will be in the "modules" folder, just check it out.)  
  
Later on, once you run:

```
python -B main.py
```  
your python code will be translated into good ol' MBScript style of code (if all goes well for now).  

Then you can simply run the build bat or python3 version of it (yes Python3) and done.  

(Before you run it, please check module_info.py and correct the path to your output folder!)  


## Info  
The Animations Module is currently not active!   
The reason for this is, that otherwise it would only have test values for now.   
And without actual correct values the Mod won't even start in a correct way.  
  
If you still want to activate it, you can uncomment the line in **main.py**:

```
    # AnimationConverter().createCode()
```
  
### Important
This is early access and many things might change over time.  
It is also worth noting, that this module system is completely empty.  
Which means, that besides that current test and minimal support codes all is up to you!  
You could write a complete new game with this, but maybe not a good one at the current state.  
If you want to add upon the native module system, you might want to check out something else for now.  
Or you could add the native codes yourself, if you want and help me translate it.  
Otherwise it might take ages for me to translate all code into python(-like)-code.


## How it works  
* First you write your code (inside "test_cases" or "modules" folder)
* Then you run "main.py"
* After that your python code is translated into MBScript  
* You can find the output in the "build_system" folder (old module_system style)
* Now check module_info.py in there for the correct path
* And run the build script (Linux/Windows) [build_module_py3.sh / build_module.bat]


## Quick Start
If you want to directly compile the MBScript code when you run "main.py", simply run the following code:  
```
python -B main.py --build
```

### Global Variables
These kind of variables are marked with '$' at the beginning of MBScript and are global as the name says.
In Py2MBScript these are also possible to use in direct python code, but currently are not fully supported.  

To mark a variable as global you add an underscore as prefix. (e.g. "_tax_code" > "$tax_code").  
This will be transformed into the MBScript global variable with dollar sign later on.
  
In later stages there might be a track of the global variables and more advanced usage possible.  
For now the act inside Python like local variables, but in MBScript as global.  

### Local Variables & Script Parameters
Local variables work like typical local python variables.
When in MBScript you would have to put them as the first argument of a function to store something, here 
you can simply put them like you might be used to from python functions.  
  
Example:
```
# ...
 
def myScript():
    versionx = get_operation_set_version()
    #...
    
# ...
```

You can also use local variables as function parameters and they will automatically be transformed internally.

Example:
```
# ...
 
def version_handling(game_version):
    if game_version == 1530:
        print("Version 1.5.3 detected! - Success")
    else:
        print("Version", game_version, "detected! - Failure")
  
  
def myScript():
    versionx = get_operation_set_version()
    version_handling(versionx)
    
# ...  
```

In the upper example you can also see that *print* is used, just like you know it from Python3.  
Ofcourse the example scripts are kinda useless right now, but give you an idea of what might be possible.  
At least I hope so. :)  


You can use if, try/catch, for and also create small lists with for loops to make your life easier.  
Some of this is not fully working at the moment, but might already make things better readable for you.  

### FYI
The above scripts are currently translated into the following MBScript code that will run later on:
```
# ...
 
("version_handling", [
(store_script_param, ":game_version", 1),
(try_begin),
    (eq,":game_version",1530),
    (display_message, "@Version 1.5.3 detected! - Success"),
(else_try),
    (assign, reg1, ":game_version"),
    (display_message, "@Version {reg1} detected! - Failure"),
(try_end),
]),
  
("myScript", [
(get_operation_set_version, ":versionx"),
(call_script, "script_version_handling", ":versionx"),
]),
 
# ...
```

After you coded your stuff in Python and generated the MBScript Code, 
you maybe want to add some code from another old school written Module System.  
You can do that inside the build_system folder, since it is the actual MS.  
But be warned, as soon as you execute **main.py** again, all will be overwritten!  
  
So make sure, to comment out the modules inside **main.py** you dont want to be changed.  
  
Here you can see how to comment out the scripts section:
```
# ...
 
# Module Scripts
# ScriptConverter().createCode()
 
# ...
```

