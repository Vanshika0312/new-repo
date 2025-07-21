import customtkinter as ctk

from tkinter import messagebox
import yt_dlp

ctk.set_appearance_mode("dark")    
ctk.set_default_color_theme("blue") 

app = ctk.CTk()
app.title("🎥 YouTube Downloader")
app.geometry("500x300")
app.resizable(False, False)

def download_video():
    url = url_entry.get()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    ydl_opts = {
        'format': '18',  
        'outtmpl': '%(title)s.%(ext)s',
    }

    try:
        status_label.configure(text="⬇ Downloading...", text_color="orange")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_label.configure(text=" Download Complete!", text_color="green")
    except Exception as e:
        status_label.configure(text=f" Error: {e}", text_color="red")

title_label = ctk.CTkLabel(app, text="🎬 YouTube Video Downloader", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

url_entry = ctk.CTkEntry(app, width=400, placeholder_text="Paste YouTube video URL here")
url_entry.pack(pady=10)

download_btn = ctk.CTkButton(app, text="Download", command=download_video)
download_btn.pack(pady=20)

status_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
status_label.pack(pady=10)

app.mainloop()
