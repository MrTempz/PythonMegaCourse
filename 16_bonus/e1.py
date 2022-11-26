import PySimpleGUI as sg

label1 = sg.Text('Enter feet:')
input1 = sg.InputText()
layout = [[label1, input1]]

label2 = sg.Text('Enter inches:')
input2 = sg.InputText()
layout.append([label2, input2])

compress_button = sg.Button("Convert")
layout.append([compress_button])

window = sg.Window('Converter', layout=layout)
window.read()
window.close()
