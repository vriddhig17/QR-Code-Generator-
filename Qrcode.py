from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from qrcode import QRCode

def generate_qr_code(data, error_correction, box_size, color, background_color):
    qr = QRCode(
        version=1,
        error_correction=error_correction,
        box_size=box_size,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color=background_color)
    return img

def save_qr_code_image(img, file_path):
    img.save(file_path)

def create_input_gui():
    def generate_qr_code_button_click():
        data = data_entry.get()
        error_correction = error_correction_var.get()
        box_size = int(box_size_entry.get())
        color = color_entry.get()
        background_color = background_color_entry.get()

        qr_code_img = generate_qr_code(data, error_correction, box_size, color, background_color)
        file_path = filedialog.asksaveasfilename(defaultextension=".png")

        if file_path:
            save_qr_code_image(qr_code_img, file_path)
            messagebox.showinfo("Success", "QR code saved successfully!")

    root = Tk()
    root.title("QR Code Generator")

    Label(root, text="Data:").grid(row=0, column=0)
    data_entry = Entry(root)
    data_entry.grid(row=0, column=1)

    Label(root, text="Error Correction:").grid(row=1, column=0)
    error_correction_var = StringVar()
    error_correction_var.set("L")
    error_correction_option_menu = OptionMenu(root, error_correction_var, "L", "M", "Q", "H")
    error_correction_option_menu.grid(row=1, column=1)

    Label(root, text="Box Size:").grid(row=2, column=0)
    box_size_entry = Entry(root)
    box_size_entry.grid(row=2, column=1)

    Label(root, text="Color:").grid(row=3, column=0)
    color_entry = Entry(root)
    color_entry.grid(row=3, column=1)

    Label(root, text="Background Color:").grid(row=4, column=0)
    background_color_entry = Entry(root)
    background_color_entry.grid(row=4, column=1)

    generate_qr_code_button = Button(root, text="Generate QR Code", command=generate_qr_code_button_click)
    generate_qr_code_button.grid(row=5, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    create_input_gui()