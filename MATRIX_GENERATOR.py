
# MATRIX GENERATOR: Design by: VanSilver
# Date: 22/01/2024 Version: 1.0.0 === Build basic GUI 
import tkinter as tk
import pyperclip
from PIL import Image, ImageTk

ver = "1.0.0"
class LEDMatrixEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("LED Matrix Generator")
        self.root.configure(bg="#F0F0F0")  # Màu nền chung cho cửa sổ
        # Thêm icon vào cửa sổ
        icon_img = self.create_led_icon()
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_img)
        self.matrix = [[0 for _ in range(8)] for _ in range(8)]

        self.create_matrix_buttons()
        self.create_bcd_display()
        self.create_copy_button()
        self.create_clear_button()
        # Tạo tên người viết phần mềm
        self.create_name_design_widgets()

    def create_matrix_buttons(self):
        self.buttons = []
        for i in range(8):
            row_buttons = []
            for j in range(8):
                button = tk.Button(self.root, width=6, height=3, command=lambda i=i, j=j: self.toggle_led(i, j), relief=tk.FLAT, overrelief=tk.RAISED, bg="#D3D3D3")  # Màu nền cho nút LED
                button.grid(row=i, column=j, padx=2, pady=2)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def create_bcd_display(self):
        self.bcd_vars = [tk.StringVar(value='0x00') for _ in range(8)]
        for i in range(8):
            bcd_label = tk.Label(self.root, textvariable=self.bcd_vars[i], font=("Arial", 14), bg="#F0F0F0")  # Màu nền cho nhãn BCD
            bcd_label.grid(row=i, column=8, padx=5, pady=5)

    def create_copy_button(self):
        copy_button = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard, height=2, bg="#4CAF50", fg="white", font=("Arial", 12))  # Màu sắc cho nút copy
        copy_button.grid(row=8, column=0, columnspan=4, padx=10, pady=10)

    def create_clear_button(self):
        clear_button = tk.Button(self.root, text="Clear Matrix", command=self.clear_matrix, height=2, bg="#FF5733", fg="white", font=("Arial", 12))  # Màu sắc cho nút clear
        clear_button.grid(row=8, column=4, columnspan=4, padx=10, pady=10)
    def create_name_design_widgets(self):
        version = tk.Label(self.root, text="Version "+ver, background='#F0F0F0', font=('Arial', 10, 'italic'), foreground='#333333')
        version.grid(row=9, column=0, columnspan=4, padx=10, pady=5, sticky='w')
        label = tk.Label(self.root, text="Design by: VanSilver", background='#F0F0F0', font=('Victorian', 12, 'italic'), foreground='#333333')
        label.grid(row=9, column=0, columnspan=15, padx=10, pady=5, sticky='e')

    def toggle_led(self, row, col):
        self.matrix[row][col] = 1 - self.matrix[row][col]
        self.update_matrix_buttons()
        self.update_bcd_display()

    def update_matrix_buttons(self):
        for i in range(8):
            for j in range(8):
                color = "#000" if self.matrix[i][j] == 1 else "#D3D3D3"
                self.buttons[i][j].configure(bg=color)

    def update_bcd_display(self):
        for i in range(8):
            bcd_value = '0x{:02X}'.format(int(''.join(map(str, self.matrix[i])), 2))
            self.bcd_vars[i].set(bcd_value)

    def copy_to_clipboard(self):
        bcd_values = [var.get() for var in self.bcd_vars]
        clipboard_text = ", ".join(bcd_values)  # Thêm dấu phẩy sau mỗi mã BCD
        pyperclip.copy(clipboard_text)

    def clear_matrix(self):
        self.matrix = [[0 for _ in range(8)] for _ in range(8)]
        self.update_matrix_buttons()
        self.update_bcd_display()

    def create_led_icon(self):
        # Tạo ảnh từ dữ liệu pixel của LED matrix (đơn giản chỉ để làm ví dụ)
        matrix_data = [
            [255, 0, 0, 255, 255, 0, 0, 255],
            [255, 0, 0, 255, 255, 0, 0, 255],
            [255, 0, 0, 255, 255, 0, 0, 255],
            [255, 0, 0, 255, 255, 0, 0, 255],
            [255, 0, 0, 255, 255, 0, 0, 255],
            [255, 0, 0, 255, 255, 0, 0, 255],
            [255, 255, 0, 0, 0, 0, 255, 255],
            [255, 255, 255, 0, 0, 255, 255, 255],
        ]

        # Tạo ảnh từ dữ liệu pixel
        image = Image.new('RGB', (8, 8), color='black')
        for i in range(8):
            for j in range(8):
                image.putpixel((j, i), (matrix_data[i][j], matrix_data[i][j], matrix_data[i][j]))

        # Chuyển ảnh thành icon
        icon = ImageTk.PhotoImage(image)
        return icon
    
if __name__ == "__main__":
    root = tk.Tk()
    app = LEDMatrixEditor(root)
    root.geometry("550x590")  # Đặt kích thước cửa sổ là 600x700 pixels
    root.resizable(False, False)
    root.mainloop()
