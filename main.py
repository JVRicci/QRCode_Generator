import qrcode
from tkinter import messagebox, Tk, Label, Entry, Button
from PIL import Image, ImageTk
import pyperclip

def generate_qrcode():
    url = website_entry.get()

    if len(url) == 0 or not url.startswith("http"):
        messagebox.showinfo(title="Erro!", message="Favor insira uma URL válida")
    else:
        opcao_escolhida = messagebox.askokcancel(
            title=url,
            message=f"Endereço: {url} \nPronto para salvar?")

        if opcao_escolhida:
            qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save("qrExport.png")
            show_qrcode()

def paste_url():
    website_entry.insert(0, pyperclip.paste())

def show_qrcode():
    global img_label
    
    try:
        image_path = "./qrExport.png"
        img = Image.open(image_path)
        img = img.resize((200, 200), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        if "img_label" not in globals():
            img_label = Label(window, image = photo)
            img_label.image = photo
            img_label.grid(row = 6, column = 1, columnspan = 2)
        else:
            img_label.configure(image=photo)
            img_label.image = photo
        
    except FileNotFoundError:
        messagebox.showerror(f"Erro",f"Imagem não encontrada:\n{image_path}")
    except Exception as e:
        messagebox.showerror(f"Erro ao abrir imagem",f" {e}")
    
    label = Label(window, image=photo)
    label.image = photo
    label.grid(row = 6, column = 1, columnspan = 2)
    

if __name__ == "__main__":
    window = Tk()
    window.title("Gerador de Código QR")
    window.config(padx = 20, pady = 10)
    window.resizable(False, False)
    # Labels
    website_label = Label(text="URL:")
    website_label.grid(row = 1, column = 0)

    # Entries
    website_entry = Entry(width=30)
    website_entry.grid(row = 1, column = 1, columnspan = 2, pady = 10)
    website_entry.focus()
    add_button = Button(text = "Colar URL", width = 10, command = paste_url)
    add_button.grid(row = 1, column = 4, columnspan = 2)
    add_button = Button(text = "Gerar QR Code", width = 36, command = generate_qrcode)
    add_button.grid(row = 4, column = 1, columnspan = 2)
        
    window.mainloop()