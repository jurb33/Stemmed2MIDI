import os
import lalalai_splitter
import PySimpleGUI as sg
import basic_pitch as bp

def main():
#layout of the window
    layout = [
        [sg.Text('Stemmed2MIDI', font=("Any", 24))],  # Title text with larger font
        [sg.FilesBrowse('Upload Files', key='-FILES-', file_types=(("Audio Files", "*.mp3 *.wav *.etc..."),), enable_events=True, tooltip='You can select up to 20 files')],
        [sg.Text('Select Neural Network:', visible=False, key='-NN-TEXT-'), sg.Combo(['Phenoix', 'Orion'], key='-NN-', visible=False, enable_events=True)],  # Initially hidden
        [sg.Text('Select Stem Type:', visible=False, key='-STEM-TEXT-'), sg.Combo([], key='-STEM-', visible=False, enable_events=True)],  # Initially hidden, options set dynamically
        [sg.Text('Filter Strength:', visible=False, key='-FILTER-TEXT-'), sg.Slider(range=(0, 2), default_value=1, orientation='horizontal', tick_interval=1, visible=False, key='-FILTER-')],
        [sg.Button("Process my Audio:", visible=True, key='-PROCESS-AUDIO-') ]
    ]

    window = sg.Window('Stemmed2MIDI', layout)
    while True:
        event, values = window.read()
        
        # if user closes window or clicks cancel
        if event == sg.WINDOW_CLOSED:
            break

        # check if files were selected
        if event == '-FILES-':
            selected_files = values['-FILES-'].split(';')  #file paths are returned separated by semicolons when group selected
            if len(selected_files) > 0:
                window['-NN-TEXT-'].update(visible=True)
                window['-NN-'].update(visible=True)

        #check if neural network type was selected
        if event == '-NN-':
            neural_network = values['-NN-']
            if neural_network == 'Phenoix':
                options = ['Vocals & Instrumental', 'Drum', 'Bass', 'Piano', 'Electric Guitar', 'Acoustic Guitar', 'Synthesizer', 'Voice', 'Strings', 'Wind']
            elif neural_network == 'Orion':
                options = ['Vocals', 'Voice']
            else:
                options = []  # Just in case
            window['-STEM-TEXT-'].update(visible=True)
            window['-STEM-'].update(values=options, visible=True)  # Update combo with the right options
            window['-FILTER-TEXT-'].update(visible=True)
            window['-FILTER-'].update(visible=True)

        if event == '-PROCESS-AUDIO-':
           #TODO send file to be processed and fed to Audio2Midi
           print("Values:")
           print(values['-STEM-'])
           print(values['-FILTER-'])
           print(values['-NN-'])


    # close the window once exited
    window.close()



#runs entire, do not remove
main()