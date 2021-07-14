# PicLib
Photo &amp; Image Manager

- **Eduardo Carvalho**
	     fc55881@alunos.fc.ul.pt
	
	 
	
- **João Milagaia**
       fc55738@alunos.fc.ul.pt
   
   
   
- Complements to Programming.
	     Lecturer: Dr. Thibault Langlois.
	
	 
	
- FCUL - Faculdade de Ciências da Universidade de Lisboa.



STRUCTURE
---------------

- appmodule.py
- bottomrow.py
- buttonsbar.py
- centralpanel.py
- coloredlabel.py
- cpcollection.py
- cpimage.py
- imagebox.py
- imagecollection.py
- main.py
- middlerow.py
- piclib.py
- picturegrid.py
- serializable.py
- squarebutton.py
- tag.py
- tagbutton.py
- tagcollection.py
- tagspanel.py
- toprow.py
- README.md



INTRODUCTION
---------------

> This assignment was made by Eduardo Carvalho and João Milagaia for the Complements to Programming - lectured by Dr. Thibault Langlois.
>
> Below are relevant information about the application, we advise that you read the **Usage Instructions** and **Known Issues**



REQUIREMENTS
---------------

This piece of software requires the Kivy library to be installed for the software to work.

> Instructions can be seen here: https://kivy.org/#home



## Usage Instructions

​	The application has to be started in the terminal, through **main.py** by using run command in any IDE.

> We tested the application in both Spyder and VSCode.

​	At the first run of application, you will be required to input a folder that contains photos and/or images, for example: 

> **C:\Users\YOURUSERNAME\Pictures**\

​	Piclib will then search for all *jpg* files in any subfolder and move it to its own folder, this folder will be created at the root of the **main.py** the images will then be saved in subfolders following the date format to create the folder structure, ./Piclib/**2021/03/01**. 

​	Several *json* files will be created. These contain each image file loaded as well as the collection of possible tags. Every image will have its own *json* file, with its metadata. This process only happens once, as if these files exist, they will be loaded.

```markdown
_Root Folder of the Project_
│   README.md
│   main.py
|	etc...
│
└───Piclib
|	|	mainImgCollection.json
|	|	mainTagCollection.json
|       │
|       └───2021
|		|__etc__
|   		│
|		|	image_name.jpg
|		|	image_name.json
```



Known Issues
---------------

1. PicLib will crash if at Scan folder its input text is empty and the OK button is pressed.
2. The first scan, is likely to take a long time to run (~30 seconds), and PicLib may look like it crashed.
3. Rotating images will sometimes leave a leftover canvas. This is fixed by restarting PicLib - images will stay rotated as intended.
4. Images will lose quality after being rotated.
5. Dates, Tags and any input may be, theoretically infinite in size, which would create problems. However we decided to approach the problem for its functional aspect and not usability. We trust the user of this application will be mindful as to not break things that may go beyond what's expected. **PicLib is not a robust application**



## Deviations from the Requirements

​	The requirements of the project were mostly kept, however we diverged in a few ways.

1. We considered unneeded to create some of the panels as their own, namely the date & tag input, as well as the configuration panel. As such we used Kivy's Popups to achieve the same goal. These allowed us to better *mimic* how everyday applications work and look, and it also felt more natural to have smaller sub-windows for small functionalities. We believe this to be a quality solution.



MANTAINERS
---------------

This program was coded and is maintained by:

```markdown
| Eduardo Carvalho | fc55881@alunos.fc.ul.pt | Master's in Informatics | FCUL |
|------------------|-------------------------|-------------------------|------|
| João Milagaia    | fc55738@alunos.fc.ul.pt | Master's in Informatics | FCUL |
```
