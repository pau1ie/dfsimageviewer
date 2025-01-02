# dfsimageviewer
View BBC Micro dfs disc images.

Written in pyqt5. The program is still incomplete. To run, install
pyqt5 and invoke the app using:

```
python3 dfsapp.py 
```

Then open a disc image using the File menu. Click Display on a file to look at the contents.
The .ui files are created by qt designer. The corresponding .py files are generated
by pyuic5 as follows:

```
$ pyuic5 filename.ui -o filename.py
```
