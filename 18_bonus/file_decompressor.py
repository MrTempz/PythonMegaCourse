import PySimpleGUI as sg
import zip_extractor

label1 = sg.Text('Select archive to decompress:')
input1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose', key='archive')
layout = [[label1, input1, choose_button1]]

label2 = sg.Text('Select destination folder:')
input2 = sg.Input()
choose_button2= sg.FolderBrowse('Choose', key='folder')
layout.append([label2, input2, choose_button2])

compress_button = sg.Button("Extract")
output_label = sg.Text('', key='output')
layout.append([compress_button, output_label])

window = sg.Window('File decompressor', layout=layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    filepath = values['archive']
    folder = values['folder']
    zip_extractor.unpack_archive(arch_filepath=filepath, dest_dir=folder)
    window['output'].update(value='Decompression completed')

window.close()
