# Py2MBScript
This Project aims to replace the old Module System with a pure Python alternative.  
Which means, that with this you can use if, for and other python things and also related objects.  
The goal is to make all related objects actually related in code, so that you can see the relation.  
Also there should be objects for related code patterns to simplify their implementation.  
  
For example the presentation module holds buttons, labels, etc. and, in the old module system  
there are several lines and different, sometimes confusing codes to implement these.  

For now this is only a test and kind of prove of concept trial.  
In the "modules" folder you can write the python versions of the otherwise MBScript versions of the thing.  
  
Later on, once you run:

```bash
python -B main.py
```  
your python code will be translated into good ol' MBScript style of code (if all goes well for now).  

Then you can simply run the build bat or python3 version of it (yes Python3) and done.  

(Before you run it, please check module_info.py and correct the path to your output folder!)  


## Important Info
This is early access and many things might change over time.  
It is also worth noting, that this module system is completely empty.  
Which means, that besides the current test and minimal support codes all is up to you!  
You could write a complete new game with this, but maybe not a good one at the current state.  
If you want to add upon the native module system, you might want to check out something else for now.  
Or you could add the native codes yourself, if you want and help me translate it.  
Otherwise it might take ages for me to translate all code into python(-like)-code.


## Quick Start
### How it works  
* First you write your code inside "modules" folder
* Then you run "main.py"
* After that your python code is translated into MBScript  
* You can find the output in the "build_system" folder (old module_system style)
* Now check module_info.py in there for the correct path
* And run the build script (Linux/Windows) [build_module_py3.sh / build_module.bat]  

### Hint
If you want to directly compile the MBScript code when you run "main.py", simply run the following code:  
```bash
python -B main.py --build
```
or
```bash
python -B main.py -b
```

### Linux only
Or run the following:
```bash
./build.sh
```

You can also directly build and run.  
```bash
python -B main.py --build-and-run
```
As the title says, this only works for Linux at the current state.


#### IDE
Now there is an IDE in the making, currently also just for Linux.  
It integrates openBRF as 3D View.  
  
**WARNING: Please dont use the openBRF window unless you know what you are doing!!!**
  
To start the IDE run the following:
```bash
./run_ide.sh
```


## Documentation
Here I will tell you what might be different or going on in Py2MBScript, so you know how to use it.

### Global Variables
These kind of variables are marked with '$' at the beginning of MBScript and are global as the name says.
In Py2MBScript these are also possible to use in direct python code, but currently are not fully supported.  

To mark a variable as global you add an underscore as prefix. (e.g. "_tax_code" > "$tax_code").  
This will be transformed into the MBScript global variable with dollar sign later on.
  
In later stages there might be a track of the global variables and more advanced usage possible.  
For now they act inside Python like local variables, but in MBScript as global.  

#### Example:
(Python Code)
```python
def game_event_party_encounter(_g_encountered_party, _g_encountered_party_2):
    _g_encountered_party_faction = store_faction_of_party(_g_encountered_party)
    _g_encountered_party_relation = store_relation(_g_encountered_party_faction, "fac_player_faction")
```
(MBScript)
```python
("game_event_party_encounter", [
(store_script_param, "$g_encountered_party", 1),
(store_script_param, "$g_encountered_party_2", 2),
(store_faction_of_party, "$g_encountered_party_faction", "$g_encountered_party"),
(store_relation,"$g_encountered_party_relation","$g_encountered_party_faction","fac_player_faction"),
]),
```


### Local Variables & Script Parameters
Local variables work like typical local python variables.
When in MBScript you would have to put them as the first argument of a function to store something, here 
you can simply put them like you might be used to from python functions.  
  
#### Example:
```python
# ...
 
def myScript():
    versionx = get_operation_set_version()
    #...
    
# ...
```

You can also use local variables as function parameters and they will automatically be transformed internally.

#### Example:
```python
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

#### FYI
The above scripts are currently translated into the following MBScript code that will run later on:
```python
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
```python
# ...
 
# Module Scripts
# ScriptConverter().createCode()
 
# ...
```


### Conditional Code [if/else]
In Python we use **if**, **elif** (else if) and **else**.  

#### Example1:
(Python Code)
```python
if agent_id == 0:
    print("Server agent found!")
else:
    print("Not server agent.")
```
(MBScript)
```python
(try_begin),
    (eq, ":agent_id", 0),
    (display_message, "@Server_agent_found!"),
(else_try),
    (display_message, "@Not server agent."),    
(try_end),
```

#### Example2:
(Python Code)
```python
if not is_edit_mode_enabled() and multiplayer_is_server() == False or agent_id >= 0:
    print("Player Code! >", agent_id)
    if True: # always true example
        print("Success!")
else:
    pass
    # server code
```
(MBScript)
```python
(try_begin),
    (neg|is_edit_mode_enabled),
    (this_or_next|neg|multiplayer_is_server),
    (ge,":agent_id",0),
    (assign, reg1, ":agent_id"),
    (display_message, "@Player Code! > {reg1}"),
    (try_begin),
        (eq,1,1),
        (display_message, "@Success!"),
    (try_end),
(else_try),
(try_end),
```

As you can see in Example2, there are multiple ways to express a condition now and boolean support.  
You can either negate with **not** *or* **compare to False**.  
It is also possible, for the sake of debugging and code activation, to make a condition always **True** or **False**.  

Multiple conditions will be checked in the given order.  
As the name says *this_or_next* checks the first condition and if that is not true, it checks the next.  
The checking order is the same, but it is "this or next".  
For multiple OR in a row, it will make as many *this_or_next* as given conditions.  

#### Important
Sometimes it is possible that at the current state, an *if* is not closed correctly after conversion into MBScript.  
When this happens, you can simply add the following line where the *if* should end in Python:
```python
#end
```
It is not so much important what stands after the '#', but this makes it easier to read and remember.  


### For Loops
In Python we all have used for loops quite a lot, I am sure.  
In MBScript there are a few differences tho and special for loops.  

#### Example1:
(Python Code)
```python
for x in range(1, 10):
    print(x)
```
(MBScript)
```python
(try_for_range, ":x", 1, 10),
    (assign, reg0, ":x"),
    (display_message, "@{reg0}"),
(try_end),
```

#### Example2:
(Python Code)
```python
for x in range(0, 10, -1):
    print(x)
```
(MBScript)
```python
(try_for_range_backwards, ":x", 10, 0),
    (assign, reg0, ":x"),
    (display_message, "@{reg0}"),
(try_end),
```


### Special For Loops
In MBScript there are a few special for loops:
* try_for_parties
* try_for_agents
* try_for_prop_instances
* try_for_players

For the Python code I chose to implement them as following:
```python
for partyx in __all_parties__:
    print(partyx)
for playerx in __all_players__:
    print(playerx)
for propix in __all_prop_instances__:
    print(propix)
for agentx in __all_agents__:
    print(agentx)
```
(MBScript)
```python
(try_for_parties, ":partyx"),
    (assign, reg0, ":partyx"),
    (display_message, "@{reg0}"),
(try_end),
(try_for_players, ":playerx"),
    (assign, reg0, ":playerx"),
    (display_message, "@{reg0}"),
(try_end),
(try_for_prop_instances, ":propix"),
    (assign, reg0, ":propix"),
    (display_message, "@{reg0}"),
(try_end),
(try_for_agents, ":agentx"),
    (assign, reg0, ":agentx"),
    (display_message, "@{reg0}"),
(try_end),
```

### break
In Python for loops you sometimes might want to break out of it.  
Now it is possible to do the same here.  

#### Example:
(Python Code)
```python
# backwards range
start = 200
end = 100
for x in range(start,end,-1):
    print(x)
    if x == 150:
        break
# forward range
end = 30
for x in range(end):
    print(x)
    if x == 10:
        break
# other try blocks
for p in __all_parties__:
    print("Party:", p)
    if p == "p_test_town":
        break
# while block (experimental)
while True:
    if True:
        break
```
(MBScript)
```python
(assign,":start",200),
(assign,":end",100),
(try_for_range_backwards, ":x", ":end", ":start"),
    (assign, reg0, ":x"),
    (display_message, "@{reg0}"),
    (try_begin),
        (eq,":x",150),
        (assign, ":end", ":start"),
    (try_end),
(try_end),
(assign,":end",30),
(try_for_range, ":x", 0, ":end"),
    (assign, reg0, ":x"),
    (display_message, "@{reg0}"),
    (try_begin),
        (eq,":x",10),
        (assign, ":end", 0),
    (try_end),
(try_end),
(assign, ":__break__", 0),
(try_for_parties, ":p"),
    (eq, ":__break__", 0),
    (assign, reg1, ":p"),
    (display_message, "@Party: {reg1}"),
    (try_begin),
        (eq,":p","p_test_town"),
        (assign, ":__break__", 1),
    (try_end),
(try_end),
(assign,":__while_range_end_0__",1),
(try_for_range,":unused",0,":__while_range_end_0__"),
    (eq,1,1),
    (val_add,":__while_range_end_0__",1),
    (try_begin),
        (eq,1,1),
        (assign, ":__while_range_end_0__", 0),
    (try_end),
(try_end),
```
Technically the break will be translated into other possible commands.  
In the forward and backwards for loop, the end condition will be set equal to the start.  

For the other try loops there will be a trick using a local variable, to skip all the code for the remaining calls. 
So it does not really break, but skip here, while for the ranged for loops it does break out completey.  

#### Warning
Use this feature with caution, since it is not fully tested and implemented yet.  
So always check wether the code was generated properly and works as expected.  


### try/catch
We also have a primitive version of try/catch.  
But it actually is working similar to if/else.  
The main difference is, that it looks more like the actual MBScript code.  
Exceptions are not really handled, since the game does not provide that inside MBScript.  
So don't get confused, it just exists.  

#### Example:
(Python Code)
```python
try:
    is_edit_mode_enabled()
except:
    print("EDIT MODE NOT ACTIVE!")
```
(MBScript)
```python
(try_begin),
    (is_edit_mode_enabled),
(else_try),
    (display_message, "@EDIT MODE NOT ACTIVE!"),
(try_end),
```


### while
This is a tricky one, since the actual logic of MBScript does not really need nor use while like checks.  
Nonetheless I implemented a test *while* loop.  
It works like a while on the outside, but is actually a for range loop on the inside, with conditions.  
Let's check it out.  

#### Example:
(Python Code)
```python
found = False
x = 0
while not found:
    print("Hello World", ">", x)
    x += 1
    if x == 10:
        found = True
```
(MBScript)
```python
(assign,":found",0),
(assign,":x",0),
(assign,":__while_range_end_0__",1),
(try_for_range,":unused",0,":__while_range_end_0__"),
    (neg|eq,":found",1),
    (assign, reg2, ":x"),
    (display_message, "@Hello World > {reg2}"),
    (val_add, ":x", 1),
    (val_add,":__while_range_end_0__",1),
    (try_begin),
        (eq,":x",10),
        (assign,":found",1),
    (try_end),
(try_end),
```
As you see it checks for a boolean 'found' and some counting code below.  
In Python it looks rather simple to exectue and you understand the logic in a way.  
Although this code might be not that useful, especially as a 'while', it shows how it kinda works.  
It uses a try_for_range and always counts the end condtion one up, until the condition is not met anymore.  

#### Warning!!!
Messing with while might crash the game!  
There also is a limit to which it can count up! -> Int32.MaxValue = 2147483647  


### Currently not supported commands
* continue
* return


### Working with python lists
It is possible to use python like lists to create the same code with them, while not having to write the line each time.  

#### Example:
(Python Code)
```python
bits = [0, 1, 2, 4, 8, 16, 32, 64, 128]
x = 8
if x in bits:
    print(x, "is in the list!")
```
(MBScript)
```python
(assign,":x",8),
(try_begin),
    (this_or_next|eq,":x",0),
    (this_or_next|eq,":x",1),
    (this_or_next|eq,":x",2),
    (this_or_next|eq,":x",4),
    (this_or_next|eq,":x",8),
    (this_or_next|eq,":x",16),
    (this_or_next|eq,":x",32),
    (this_or_next|eq,":x",64),
    (eq,":x",128),
    (assign, reg0, ":x"),
    (display_message, "@{reg0} is in the list!"),
(try_end),
```
As you see, the whole list gets transformed into multiple *this_or_next* and *eq* statements.  


### Working with Triggers
There are triggers in Missions and also for the general game.  
They have condtional code too.  

In Py2MBScript the first **if** will be transformed and the condition directly used.
If there is not secondary condition (another if inside the first one), you have to write *pass* as code.  

#### Example:
(Python Code)
```python
triggyx = Trigger(1,0,0)
 
def condition():
    if key_is_down(0x0f):
        pass
triggyx.conditionBlock = condition
 
def code():
    finish_mission(0)
    change_screen_return()
triggyx.codeBlock = code
```
(MBScript)
```python
(1, 0, 0, [
(key_is_down, 0x0f),
], [
(finish_mission, 0),
(change_screen_return),
]),
```

### Advanced Math
Now it is possible to have some more advanced math logic in one line!  
Use with caution!  
  
(Python Code)
```python
def superMaths(bul, bal, bil):
    x = 1 + 3 * 5 + 2 * 7 + 5 * 2 # 40
    print(x)
    
    y = 1 + 3 + x / 4 * 3 / 3 # 14
    print(y)
    
    z = 1 + 3 + (x + y) * 4 # 220
    print(z)
    
    z2 = (1+3) * (4+8) # 48
    print(z2)
    
    z3 = (3-1) * (8-4) # 8
    print(z3)
    
    z4 = z / (x + y) * z2 # 195,555555556 --> 192 (integer rounding after division!)
    print(z4)
    
    z5 = x - 4 - 5 + z3 # 39
    print(z5)
    
    x2 = (9 + 3 * 2) - (5 * 2) + (3 - 1) # 7
    print(x2)
    
    y2 = (9 + 6 * 2) - (8 / 2) - (3 - 1) # 15
    print(y2)
    
    qq = (bul * bal) / bil + bil # use ( ... ) even tho it should work because it sometimes does not
    print(qq)
```

(MBScript)
```python
("superMaths", [
(store_script_param, ":bul", 1),
(store_script_param, ":bal", 2),
(store_script_param, ":bil", 3),
(store_mul, ":var___x1", 3, 5),
(store_mul, ":var___x2", 2, 7),
(store_mul, ":var___x3", 5, 2),
(store_add, ":x", 1, ":var___x1"),
(val_add, ":x", ":var___x2"),
(val_add, ":x", ":var___x3"),
(assign, reg0, ":x"),
(display_message, "@{reg0}"),
(store_div, ":var___y1", ":x", 4),
(store_div, ":var___y2", 3, 3),
(store_mul, ":var___x1", ":var___y1", ":var___y2"),
(store_add, ":y", 1, 3),
(val_add, ":y", ":var___x1"),
(assign, reg0, ":y"),
(display_message, "@{reg0}"),
(store_add, ":var___z1", ":x", ":y"),
(store_mul, ":var___x1", ":var___z1", 4),
(store_add, ":z", 1, 3),
(val_add, ":z", ":var___x1"),
(assign, reg0, ":z"),
(display_message, "@{reg0}"),
(store_add, ":var___z1", 1, 3),
(store_add, ":var___z2", 4, 8),
(store_mul, ":var___x1", ":var___z1", ":var___z2"),
(assign,":z2",":var___x1"),
(assign, reg0, ":z2"),
(display_message, "@{reg0}"),
(store_sub, ":var___z1", 3, 1),
(store_sub, ":var___z2", 8, 4),
(store_mul, ":var___x1", ":var___z1", ":var___z2"),
(assign,":z3",":var___x1"),
(assign, reg0, ":z3"),
(display_message, "@{reg0}"),
(store_add, ":var___z1", ":x", ":y"),
(store_div, ":var___y1", ":z", ":var___z1"),
(store_mul, ":var___x1", ":var___y1", ":z2"),
(assign,":z4",":var___x1"),
(assign, reg0, ":z4"),
(display_message, "@{reg0}"),
(store_sub, ":var___a1", ":x", 4),
(val_sub, ":var___a1", 5),
(store_add, ":z5", ":var___a1", ":z3"),
(assign, reg0, ":z5"),
(display_message, "@{reg0}"),
(store_mul, ":var___x1", 3, 2),
(store_add, ":var___z1", 9, ":var___x1"),
(store_mul, ":var___z2", 5, 2),
(store_sub, ":var___z3", 3, 1),
(store_sub, ":var___a1", ":var___z1", ":var___z2"),
(store_add, ":x2", ":var___a1", ":var___z3"),
(assign, reg0, ":x2"),
(display_message, "@{reg0}"),
(store_mul, ":var___x1", 6, 2),
(store_add, ":var___z1", 9, ":var___x1"),
(store_div, ":var___x1", 8, 2),
(assign,":var___z2",":var___x1"),
(store_sub, ":var___z3", 3, 1),
(store_sub, ":y2", ":var___z1", ":var___z2"),
(val_sub, ":y2", ":var___z3"),
(assign, reg0, ":y2"),
(display_message, "@{reg0}"),
(store_mul, ":var___z1", ":bul", ":bal"),
(store_div, ":var___x1", ":var___z1", ":bil"),
(store_add, ":qq", ":var___x1", ":bil"),
(assign, reg0, ":qq"),
(display_message, "@{reg0}"),
]),
```

### Translations

In the folder **translation** you can find all the translation files.  
(**WARNING**: Currently there only is **trans_items.py** for *items*)
  
#### Example:
```python
def createTranslations():
    # ...
    #
    # no_item - INVALID ITEM
    # -------------------------------------------------------------------------
    locale["de"].translate(itm.no_item.id, "UNGÜLTIGER GEGENSTAND")
    locale["de"].translate(itm.no_item.id + "_pl", "UNGÜLTIGER GEGENSTAND")
    locale["cz"].translate(itm.no_item.id, "NEPLATNÁ POLOŽKA")
    locale["cz"].translate(itm.no_item.id + "_pl", "NEPLATNÁ POLOŽKA")
    locale["es"].translate(itm.no_item.id, "OBJETO INVALIDO")
    locale["es"].translate(itm.no_item.id + "_pl", "OBJETOS INVALIDOS")
    locale["fr"].translate(itm.no_item.id, "OBJET INVALIDE")
    locale["fr"].translate(itm.no_item.id + "_pl", "OBJETS INVALIDES")
    locale["hu"].translate(itm.no_item.id, "NEM MEGFELELŐ TÁRGY")
    locale["hu"].translate(itm.no_item.id + "_pl", "NEM MEGFELELŐ TÁRGY")
    locale["pl"].translate(itm.no_item.id, "NIEPRAWIDŁOWY PRZEDMIOT")
    locale["pl"].translate(itm.no_item.id + "_pl", "NIEPRAWIDŁOWY PRZEDMIOT")
    # -------------------------------------------------------------------------
    #
    # ...
```

This will add translations for **no_item**. The "_pl" is for plural translation, in case it is used.  


