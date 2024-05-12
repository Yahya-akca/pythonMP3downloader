import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import os

def download_video():
    url = url_entry.get()
    destination = destination_entry.get() or '.'
    
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        messagebox.showinfo("Başarılı", f"{yt.title} başarılı bir şekilde indirildi.")
    except Exception as e:
        messagebox.showerror("Hata", f"İndirme başarısız oldu: {str(e)}")

# GUI oluştur
root = tk.Tk()
root.title("YouTube Video İndirici")

url_label = tk.Label(root, text="Video URL:")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

destination_label = tk.Label(root, text="Dosya Konumu:")
destination_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
destination_entry = tk.Entry(root, width=50)
destination_entry.grid(row=1, column=1, padx=5, pady=5)

download_button = tk.Button(root, text="İndir", command=download_video)
download_button.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()
