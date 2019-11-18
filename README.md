# Log Recorder
A basic program which allows you to write into a designated text file with timestamps.

Run `make install` to install the program.

## HOW TO ❓
* Set path to logs file you want to write into.
* Run with either GUI or through CLI. GUI is default behaviour on Windows. 
```bash
$ ./logrecorder -p /path/to/logs.txt
$ ./logrecorder # cli
# or
$ ./logrecorder --gui
# or
$ ./logrecorder --cli # on Windows
```

### USAGE
```
$ ./logrecorder [-h] [-v] [-i] [-c] [-g] [-p PATH]

Write into a designated text file with timestamps. A diary, log keeping
program if you will.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show version information and exit
  -i, --info            print current path to log file and exit
  -c, --cli             launch the program in cli instead of gui (default
                        behaviour in windows)
  -g, --gui             launch the program in gui instead of cli
  -p PATH, --path PATH  set path to log file in config file
```

## Screenshots

### CLI

![](https://raw.githubusercontent.com/kittenparry/log-recorder/master/extras/screenshot_cli.png)

### GUI

![](https://raw.githubusercontent.com/kittenparry/log-recorder/master/extras/screenshot_linux.png)

![](https://raw.githubusercontent.com/kittenparry/log-recorder/master/extras/screenshot_windows.png)
