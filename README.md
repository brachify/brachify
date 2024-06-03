# brachify

## License
brachify is licensed under the terms of the GNU 3.0 license, as noted in the LICENSE file. 

## User Info
### Download exe zip at:
https://github.com/nsmela/brachify/releases

### Tutorial info can be found:
#TODO

## Developer Info
### Getting Started programatically
- Download Python 
- Download VS Code or your favorite IDE
- download git
brachify uses the pythonocc library. Easiest setup is to use [Anaconda3](https://www.anaconda.com/download) as your python interpreter. Some modules take significant time to install using conda install. For those which seem to take time, try to use pip install instead (pip is included in conda)

- Open Anaconda prompt with Administrator rights
- optional: create and activate a virtual environment
- install pyside 6 ```conda install PySide6``` 
- install pythonocc using ```conda install conda-forge::pythonocc-core```
- ```conda install matplotlib```
- ```conda install reportlab```
- ```conda install pydicom```
- download code (clone git repository to your local machiene)
- run launch.py to use the application

To build .exe make sure your working directory is the brachify directory then run the following command in the command line:

```pyinstaller --noconsole --noconfirm --icon "./resources/brachify_splash-ico.ico" --name "brachify" --splash ".\src\windows\splashscreen\brachify_splash.png" --hidden-import "pydicom.encoders.gdcm" --hidden-import "OCC" --hidden-import "pydicom.encoders.pylibjpeg" --paths=src "./src/launch.py"```

This command may take a few minutes to compile depending on your machine. After it has compiled it will make 2 folders: `dist` and `build`. To run the application from the executable file, run `brachify.exe` located in `dist\brachify`.

