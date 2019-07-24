# Log Recorder
A basic program which allows you to write into a designated text file with timestamps.

### Instructions

Run `make install` to install the program.

You need to edit directory and filename in `dict_strings` beforehand for the program to work for your needs. Using absolute path is recommended. Or you can set the path on command line with options `-p` and `-f`.

`path_dir`: directory path (`.` for the current directory)  
`name_filename`: filename

Default file path is `Other/myLogs.txt` for my own use.


```
Usage: logrecorder [OPTIONS]
	
Options:
  -p, --path PATH	Set & save destination directory to the config file.
  -f, --file FILENAME	Set & save target filename to the config file.
			  Creating the config file will override path values of in-program dictionary (dict_strings: path_dir, name_filename).
  -d, --del		Delete the configuration file & folder.
  -g, --gui		Launch the program in GUI instead of CLI.
			  When combining with path options, GUI must come last.
  -v, --version		Show version information and exit.
  -h, --help		Show this message and exit.
```

### CLI

![](https://raw.githubusercontent.com/kittenparry/log-recorder/master/extras/screenshot_cli.png)

### GUI

![](https://raw.githubusercontent.com/kittenparry/log-recorder/master/extras/screenshot_linux.png)

![](https://raw.githubusercontent.com/kittenparry/log-recorder/master/extras/screenshot_windows.png)
