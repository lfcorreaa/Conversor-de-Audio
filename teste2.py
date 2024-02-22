import PySimpleGUI as sg
from pytube import YouTube

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)
        return True
    except Exception as e:
        return str(e)

sg.theme('DarkBlue')
sg.SetOptions(background_color='#FFA500', text_element_background_color='#FFA500')

layout = [
    [sg.Image(r"C:\Users\luizl\Downloads\imagemyoutube.png", size=(125, 75)),
     sg.Text('Youtuber DownLoader')],
    [sg.Text('URL do vídeo do YouTube:')],
    [sg.Input(key='-URL-')],
    [sg.Text('Pasta de Download:')],
    [sg.InputText(key='-OUTPUT_PATH-'), sg.FolderBrowse()],
    [sg.Button('Baixar', key='-DOWNLOAD-')],
]

window = sg.Window('Baixar Áudio do YouTube', layout, finalize=True, no_titlebar=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-DOWNLOAD-':
        url = values['-URL-']
        output_path = values['-OUTPUT_PATH-']

        result = download_video(url, output_path)

        if result is True:
            sg.popup('Download concluído!', title='Sucesso')
        else:
            sg.popup_error(f'Erro no download: {result}')

window.close()