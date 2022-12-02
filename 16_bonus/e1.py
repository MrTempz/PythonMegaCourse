import PySimpleGUI as sg

sg.theme('DarkBlack1')

label1 = sg.Text('Enter feet:')
input1 = sg.InputText(key='feet')
error_label1 = sg.Text('', key='feet_error')
layout = [[label1, input1, error_label1]]

label2 = sg.Text('Enter inches:')
input2 = sg.InputText(key='inches')
error_label2 = sg.Text('', key='inches_error')
layout.append([label2, input2, error_label2])

convert_button = sg.Button('Convert')
exit_button = sg.Button('Exit')
output_label = sg.Text('', key='output')
layout.append([convert_button, exit_button, output_label])

window = sg.Window('Converter', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Convert':
        try:
            feet = float(values['feet'])
            window['feet_error'].update(value='')
        except:
            feet = None
            window['feet_error'].update(value='Not a correct number')
            window['output'].update(value='One or both above numbers are incorrect')
        
        try:
            inches = float(values['inches'])
            window['inches_error'].update(value='')
        except:
            inches = None
            window['inches_error'].update(value='Not a correct number')
            window['output'].update(value='One or both above numbers are incorrect')

        try:
            result = f'{(feet*12 + inches)*2.54/100} m'
        except:
            result = 'One or both above numbers are incorrect'
            sg.popup('One or both above numbers are incorrect')
        window['output'].update(value=result)
    elif event == 'Exit':
        break

window.close()
