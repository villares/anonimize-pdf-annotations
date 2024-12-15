# Anonimize PDF annotations

A naive Python tool to remove your name from PDF annotations

## Dependencies and how to run this

You need a Python 3.9 or more recent virtual environment where you can install these two libraries:

- `pymupdf`  (the main PDF manipulation required)
- `FreeSimpleGUI` (for the GUI panel)

Then run [`remove_name_from_annotations_gui.py`](https://github.com/villares/anonimize-pdf-annotations/blob/main/remove_name_from_annotations_gui.py).

If you have no idea how to set up a Python virtual env, no worries! I recommend installing [Thonny IDE](https://thonny.org) that gives you an isolated Python env out of the box and then you can install the two libraries metioned above from the "Tools > Manage Packages" panel. After that you can use Thonny to run the code.

## Stand-alone executables (using `pyinstaller`)

- Linux: https://github.com/villares/anonimize-pdf-annotations/releases/download/v0/remove_name_from_annotations_gui

I'd love some help building and testing  `pyinstaller` results for Windows and MacOS!
