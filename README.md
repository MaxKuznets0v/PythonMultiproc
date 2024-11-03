# PythonMultiproc

### Description

This is a test task, which implements a multiprocessing communication between two programs (Program A and Program B).
**Program A** - Pseudo-Random Number Generator. 
**Program B** - Controller, which calls different commands for Program A.
Each program works in its own process, all their interactions happen exclusively via *stdout*/*stdin*.

### Commands

- *Greetings*: called by code word "Hi". Program A answers back with "Hi".
- *Get Random integer*: called by code word "GetRandom". Program A generates random integer within set range.
- *Termination*: called by code word "Shutdown". Program A gracefully terminates.
- Any other commands are fully ignored by Program A.

### Settings

All configurations are flexible and can be configured using `config.ini`. That includes possible commands and their naming, responses and generator preset (min and max value for generation range and number of generating samples by Program B).

### Program behaviour

Program B acts as an entry point and follows workflow below:

1. Sends Greetings to Program A, then verifies that it replies with "Hi".
2. Generates 100 (by default) random integers, retrieving them from Program A.
3. Shutdowns Program A execution with corresponding command. 
4. Sorts obtained list of numbers, prints them out to console.
5. Calculates median and average value of the list. Prints results.

In order to run task, update `config.ini` file with necessary data and call:

```commandline
python program_b.py
```
