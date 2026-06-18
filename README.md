# *brachify*

## License
*brachify* is licensed under the terms of the GNU 3.0 license, as noted in the LICENSE file. 

## User Info
### Download exe zip at:
https://github.com/brachify/brachify/releases

### Tutorial info can be found at:
[`user_guide/Brachify User Manual.docx`](user_guide/Brachify%20User%20Manual.docx)

## Developer Info
### Getting Started programatically
- Download Python 3.12 (or 3.11)
- Download Visual Studio Code (VS Code)
- download git
- create a conda environment using the instructions in [`virtual_environments_instructions.md`](virtual_environments_instructions.md)
- download code (clone git repository to your local machiene)
- run `launch.py` to use the application
- developer notes can be found in the folder [`notes/`](notes/)

### To build .exe
#### Option 1
Make sure your working directory is the brachify directory then run the following command in the command line:  

```pyinstaller --noconsole --noconfirm --icon "./resources/brachify_splash-ico.ico" --name "brachify" --splash ".\src\windows\splashscreen\brachify_splash.png" --hidden-import "pydicom.encoders.gdcm" --hidden-import "OCC" --hidden-import "pydicom.encoders.pylibjpeg" --paths=src "./src/launch.py" --exclude-module PyQt5```  

After it has compiled it will make two folders in your brachify folder: `dist` and `build`. The executable is `brachify.exe` located in `dist\brachify`.

#### Option 2
Run [`build_executable.py`](build_executable.py). This should produce the same result as [Option 1](#option-1).

After it has compiled it will make two folders in your brachify folder: `dist` and `build`. The executable is `brachify.exe` located in `dist\brachify`.

