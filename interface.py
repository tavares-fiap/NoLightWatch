import tkinter as tk
from tkinter import filedialog
import os
from main import analisar_video

CAMINHO_VIDEOS = "./videos"

def listar_videos():
    return [f for f in os.listdir(CAMINHO_VIDEOS) if f.endswith(".mp4")]

def escolher_video():
    caminho = filedialog.askopenfilename(
        title="Escolher vídeo",
        filetypes=[("Vídeos MP4", "*.mp4"), ("Todos os arquivos", "*.*")]
    )
    if caminho:
        analisar_video(caminho)

def usar_camera():
    analisar_video(0)

def analisar_selecionado():
    selecao = lista_videos.curselection()
    if selecao:
        nome_arquivo = lista_videos.get(selecao[0])
        caminho_completo = os.path.join(CAMINHO_VIDEOS, nome_arquivo)
        analisar_video(caminho_completo)

# Janela principal
janela = tk.Tk()
janela.title("Detector de Gestos e Quedas")
janela.geometry("400x350")

# Lista de vídeos disponíveis
label_lista = tk.Label(janela, text="Escolha um vídeo da pasta:")
label_lista.pack()

lista_videos = tk.Listbox(janela, width=50, height=6)
for video in listar_videos():
    lista_videos.insert(tk.END, video)
lista_videos.pack(pady=5)

btn_analisar_lista = tk.Button(janela, text="Analisar vídeo selecionado", command=analisar_selecionado)
btn_analisar_lista.pack(pady=5)

# Outros botões
btn_video = tk.Button(janela, text="Escolher vídeo manualmente", command=escolher_video)
btn_camera = tk.Button(janela, text="Usar webcam", command=usar_camera)
btn_sair = tk.Button(janela, text="Sair", command=janela.destroy)

btn_video.pack(pady=5)
btn_camera.pack(pady=5)
btn_sair.pack(pady=10)

janela.mainloop()
