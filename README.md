# Anonymize PDF annotations

A naive Python tool to remove your name from PDF annotations

![image](https://github.com/user-attachments/assets/3271d15f-ae29-43a7-8fe1-b9d29d637b38)

## Dependencies and how to run this...

You need a Python 3.9 or more recent virtual environment where you can install these two libraries:

- `pymupdf`  (the main PDF manipulation required)
- `FreeSimpleGUI` (for the GUI panel)

Then run [`remove_name_from_annotations_gui.py`](https://github.com/villares/anonimize-pdf-annotations/blob/main/remove_name_from_annotations_gui.py).

If you have no idea how to set up a Python virtual env, no worries! I recommend installing [Thonny IDE](https://thonny.org) that gives you an isolated Python env out of the box and then you can install the two libraries mentioned above using  "Tools > Open Systen Shell..." and `python -m pip install pymupdf freesimplegui`. After that you can use Thonny to run the code.

## ... or try a stand-alone executable 

Made using `pyinstaller remove_name_from_annotations_gui.py -F`:

- Linux: [...//download/v0.1/remove_name_from_annotations_gui](https://github.com/villares/anonimize-pdf-annotations/releases/download/v0.1/remove_name_from_annotations_gui)
- Windows: [.../download/v0.1/remove_name_from_annotations_gui.exe](https://github.com/villares/anonimize-pdf-annotations/releases/download/v0.1/remove_name_from_annotations_gui.exe)

- If you are on MacOS, it would be great to have someone building it, we could then add it here.

## Acknowledgments

Thank you [@introscopia](https://github.com/introscopia) for the encouragement and he first Windows .exe build!
Rodrigo Ghedin proposed the removal of the output field to simplify the UX, saving the resulting PDF on same folder as the input with a modified name, thank you!
