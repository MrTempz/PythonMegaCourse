import PySimpleGUI as sg
import zip_creator

label1 = sg.Text('Select files to compress:')
input1 = sg.Input()
choose_button1 = sg.FilesBrowse('Choose', key='files')
layout = [[label1, input1, choose_button1]]

label2 = sg.Text('Select destination folder:')
input2 = sg.Input()
choose_button2= sg.FolderBrowse('Choose', key='folder')
layout.append([label2, input2, choose_button2])

compress_button = sg.Button("Compress")
output_label = sg.Text('', key='output')
layout.append([compress_button, output_label])

window = sg.Window('File compressor', layout=layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    filepaths = values['files'].split(';')
    folder = values['folder']
    zip_creator.make_archive(filepaths=filepaths, dest_dir=folder)
    window['output'].update(value='Compression completed')

window.close()
