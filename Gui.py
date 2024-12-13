import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    text = text_entry.get()
    if text.strip():
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("start output.mp3" if os.name == "nt" else "afplay output.mp3")
    else:
        messagebox.showwarning("Error", "Please Enter a Text First !")

def reset_text():
    text_entry.delete(0, tk.END)

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Gui project")
root.geometry("600x400")
root.configure(bg="#31363F")

header = tk.Label(
    root, 
    text="Text to Speech ...", 
    font=("Helvetica", 28, "bold"), 
    bg="#31363F", 
    fg="#FFD700"  
)
header.pack(pady=10)

sub_header = tk.Label(
    root, 
    text="Enter your text :", 
    font=("Helvetica", 14, "bold"),  
    bg="#31363F",  
    fg="#000000"  
)
sub_header.pack(pady=5)

text_entry = tk.Entry(
    root, 
    width=40, 
    font=("Helvetica", 14), 
    bg="#1A1A1A",  
    fg="#FFFFFF",  
    insertbackground="#FFD700",  
    bd=2,
    relief="flat",
    justify="center"  
)
text_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#31363F")  
button_frame.pack(pady=20)

play_button = tk.Button(
    button_frame, 
    text="Play", 
    font=("Helvetica", 12, "bold"), 
    bg="#4CAF50",  
    fg="#FFFFFF", 
    activebackground="#66BB6A", 
    activeforeground="#FFD700", 
    width=12,
    height=1,
    bd=0,
    command=play_text
)
play_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(
    button_frame, 
    text="Set", 
    font=("Helvetica", 12, "bold"), 
    bg="#FF9800",  
    fg="#FFFFFF", 
    activebackground="#FFB74D", 
    activeforeground="#FFD700", 
    width=12,
    height=1,
    bd=0,
    command=reset_text
)
reset_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(
    button_frame, 
    text="Exit", 
    font=("Helvetica", 12, "bold"), 
    bg="#F44336",  
    fg="#FFFFFF", 
    activebackground="#E57373", 
    activeforeground="#FFD700", 
    width=12,
    height=1,
    bd=0,
    command=exit_program
)
exit_button.grid(row=0, column=2, padx=10)

footer = tk.Label(
    root, 
    text="Developed by: Eng / Ahmed Fekry Ezzat", 
    font=("Helvetica", 12, "italic"),  
    bg="#31363F",  
    fg="#000000"  
)
footer.pack(side="bottom", pady=10)

root.mainloop()
