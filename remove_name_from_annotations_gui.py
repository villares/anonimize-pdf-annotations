from pathlib import Path

import pymupdf  # needs to be installed
import FreeSimpleGUI as sg  # needs to be installed
 
default_output = Path.home() / 'modified.pdf'
L_FONT = ('Courier', 20)
I_FONT = ('Courier', 16)

# Define the GUI layout
layout = [
    [sg.Text('Input file:', font=L_FONT)],
    [sg.InputText(font=I_FONT), sg.FileBrowse(font=I_FONT)],
    [sg.Text('Change names in notes to:', font=L_FONT), sg.InputText(default_text='redacted name', font=I_FONT, size=(18, 1))],
    [sg.Checkbox('Remove author\'s name from main document metadata', font=I_FONT)],
    [sg.Button('Create modified PDF', font=L_FONT),
     sg.Button('CLOSE/EXIT', font=L_FONT)]
]

# Create the GUI window
window = sg.Window('Modify PDF annotations & metadata', layout)

# Run the GUI event loop
while True:
    # Get the next GUI event
    event, values = window.read()
    # Exit the event loop if the window was closed or the Cancel button was clicked
    if event in (None, 'CLOSE/EXIT'):
        break
    elif event == 'Create modified PDF' and values:
        # Get the input and output values from the GUI
        input_file = Path(values[0])
        output_file = input_file.parent / (input_file.stem + '_modified.pdf')
        author = values[1] if values[1] else ' '
        checkbox = values[2]
        try:
            doc = pymupdf.open(input_file)
            if checkbox:
                print(f'Original doc metadata: {doc.metadata}')
                doc.metadata['author'] = ' '  # Remove main doc's author metadata
                print(f'Modified doc metadata: {doc.metadata}')
            for page in doc:
                for a in page.annots():
                    print(f'Original: {a.info}')
                    a.set_info(title=author)  # change author in annotations (title)
                    print(f'Modified: {a.info}')
            doc.save(output_file)
            sg.popup(f'{output_file.name} saved.')
        except Exception as e:
            sg.popup(str(e))
# Clean up the GUI
window.close()