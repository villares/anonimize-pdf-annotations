# Anonimize PDF annotations

A naive Python tool to remove your name from PDF annotations

## Dependencies and how to run this.

I recommend either having Python and a virtual env where you can install these two libraries:

- `pymupdf`  (the main PDF manipulation required)
- `FreeSimpleGUI` (for the GUI panel)

If you have no idea how to set up a Python virtual env I recommend installing [Thonny IDE](https://thonny.org) that gives you an isolated Python env out of the box and installing the libries from it's "Tools > Manage Packages" interface.

## Stand-alone executables (using `pyinstaller`)

- Linux: https://github.com/villares/anonimize-pdf-annotations/releases/download/v0/remove_name_from_annotations_gui

I'd love some help building and testing  `pyinstaller` results for Windows and MacOS!