# import modul 
import tkinter as tk
import tkinter.ttk as ttk

class Menu:
    def __init__(self, kode_menu, nama_menu, harga):
        self.kode_menu = kode_menu
        self.nama_menu = nama_menu
        self.harga = int(harga)

class Meals(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kegurihan):
        super().__init__(kode_menu, nama_menu, harga)
        # TODO handle info tambahan

class Drinks(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kemanisan):
        super().__init__(kode_menu, nama_menu, harga)
        # TODO handle info tambahan

class Sides(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_keviralan):
        super().__init__(kode_menu, nama_menu, harga)
        # TODO handle info tambahan

class Main(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.geometry("400x200")
        self.pack()
        master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        button1 = tk.Button(self, text="Buat Pesanan", width=30, command=self.buat_pesanan, bg="#4472C4", fg="white")
        button2 = tk.Button(self, text="Selesai Gunakan Meja", width=30, command=self.selesai_gunakan_meja, bg="#4472C4", fg="white")
        button1.grid(row=0, column=0, padx=10, pady=40)
        button2.grid(row=1, column=0)
        
    def buat_pesanan(self):
        BuatPesanan(self.master)

    def selesai_gunakan_meja(self):
        SelesaiGunakanMeja(self.master)

class BuatPesanan(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        self.lbl_nama = tk.Label(self, text="Siapa nama Anda?")
        self.lbl_nama.grid(column=0, row=0, pady=(80,0))

        #TODO

        self.mainloop()

class SelesaiGunakanMeja(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        self.lbl_command = tk.Label(self, text="Silakan klik meja yang selesai digunakan:")
        self.lbl_command.grid(column=0, row=0)

        #TODO

        self.mainloop()

def main():
    with open('menu.txt', 'r') as f:
            lines = f.read().splitlines() 
    
    # TODO mengolah data menu
    
    window = tk.Tk()
    cafe = Main(window)
    window.mainloop()


if __name__ == '__main__':
    main()
