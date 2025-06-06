# 🔦 Detector de Gestos e Quedas em Ambientes sem Iluminação

## 🎯 Descrição do Problema
Durante apagões, a falta de iluminação pode causar situações perigosas: quedas, pedidos de ajuda não percebidos, e riscos em ambientes sensíveis como hospitais ou residências de idosos. Não são todos os locais que contam com vigilância constante ou sistemas inteligentes para lidar com isso.

## 💡 Visão Geral da Solução
Desenvolvemos um sistema em Python utilizando MediaPipe capaz de:
- Detectar **gestos de socorro** (ambas as mãos levantadas).
- Detectar **quedas** com base na postura e altura do tronco.
- Emitir alertas sonoros automáticos.
- Funcionar via **webcam ou vídeos**.
- Operar sem hardware adicional (sem Arduino ou ESP32).

### 🔧 Tecnologias Usadas
- Python
- MediaPipe (pose estimation)
- OpenCV
- Tkinter (interface gráfica)
- Pygame (emissão de sons)

### 🧠 Como Funciona
- Utilizamos os pontos do corpo captados pela MediaPipe para identificar movimentos específicos.
- O gesto de socorro é detectado quando as duas mãos estão acima da cabeça.
- A queda é identificada pela posição horizontal do corpo e proximidade com o chão.

### 🖼️ Ilustrações
![Captura de tela 2025-06-04 114542](https://github.com/user-attachments/assets/d43805e8-c315-4450-b115-09b4c48295cd)

(*Imagem mostrando a janela do Tkinter com botões de "Usar webcam" e "Analisar vídeo selecionado"*).

![Captura de tela 2025-06-04 114733](https://github.com/user-attachments/assets/085b50c0-f735-4404-9c92-0002b99f33b1)

(*Imagem de uma pessoa com as mãos levantadas, com a mensagem “PEDIDO DE AJUDA DETECTADO” sobreposta.*)

![Captura de tela 2025-06-04 114559](https://github.com/user-attachments/assets/4f261655-2689-4adf-9fd6-951e3ddedd89)

(*Imagem de uma pessoa no chão, com a linha vermelha no meio da tela e a mensagem “QUEDA DETECTADA”.*)

## ▶️ Vídeo Demonstrativo
[🔗 Clique aqui para assistir ao vídeo](https://youtu.be/0sk_BvmYFnE)

## 📁 Como Executar
1. Instale as dependências:
   ```bash
   pip install opencv-python mediapipe pygame
2. Execute a interface:
    ```bash
    python interface.py
3. Escolha um vídeo da pasta /videos , use a webcam ou envie seu proprio video para analise.

### 👥 Integrantes
Pedro Henrique Pedrosa Tavares - RM 97877

Pedro Oliveira Valotto - RM 551445

Guilherme Rocha Bianchini - RM 97974
