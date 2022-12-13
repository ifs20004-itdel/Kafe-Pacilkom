# import modul 
import tkinter as tk
import tkinter.ttk as ttk
import json

class Menu:
    def __init__(self, kode_menu, nama_menu, harga):
        self.kode_menu = kode_menu
        self.nama_menu = nama_menu
        self.harga = int(harga)
    
class Meals(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kegurihan):
        super().__init__(kode_menu, nama_menu, harga)
        
        self.tingkat_kegurihan = tingkat_kegurihan

class Drinks(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kemanisan):
        super().__init__(kode_menu, nama_menu, harga)
        
        self.tingkat_kemanisan = tingkat_kemanisan

class Sides(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_keviralan):
        super().__init__(kode_menu, nama_menu, harga)
        
        self.tingkat_keviralan = tingkat_keviralan

#  Class pembeli, menampung data pembeli
class Pembeli():
    def __init__(self, nama, nomeja,total_harga, data_pesanan):
        self.nama = nama
        self.nomeja = nomeja
        self.total_harga = total_harga
        self.data_pesanan = data_pesanan

class Main(tk.Frame):
    pembeli  = []
    meja = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
            # close tampilan utama, and tampilkan tampilan nama pelanggan
            self.master.withdraw()
            self.geometry("400x200")
            self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
            self.meja = Main.meja

            # Fungsi untuk kembali ke tampilan utama
            def show_main_window():
                self.master.deiconify()
                self.destroy()
            
            def show_menu_window():
                nama = self.ent_nama.get()
                self.withdraw()
                MenuWindow(nama,self.meja[0], self.master)
                # self.meja.remove(self.meja[0])
            
            # Fungsi untuk menonaktifkan tombol close pada child window
            def disable_event(event=None):
                pass
            
            self.protocol("WM_DELETE_WINDOW", disable_event)
            self.lbl_nama = tk.Label(self, text="Siapa nama Anda?",  width=30)
            self.lbl_nama.grid(column=0, row=0, pady=(80,0))

            self.ent_nama = tk.Entry(self)
            self.ent_nama.grid(column=1, row=0, pady=(80,0))

            self.button_back = tk.Button(self, text="Kembali", width=17, command=show_main_window, bg="#4472C4", fg="white").place(x=50, y=150)
            self.button_forward = tk.Button(self, text="Lanjut", width=17, command=show_menu_window, bg="#4472C4", fg="white").place(x=200, y=150)

            self.mainloop()

class SelesaiGunakanMeja(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        # close tampilan utama, and tampilkan tampilan nama pelanggan
        self.master.withdraw()
        self.master.geometry("400x200")
        self.geometry("500x450")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.meja = Main.meja

        self.lbl_command = tk.Label(self, text="Silakan klik meja yang selesai digunakan:")
        self.lbl_command.grid(column=1, columnspan=3, row=0, padx=5, pady=(20,0))

        # self.btn_meja = tk.Button
        for i in range(10):
            if(i>4):
                # Jika angka terdapat pada list, warna abu abu
                if i in self.meja:   
                    self.btn_meja = tk.Button(self, text=str(i), width=10, height=1, bg="grey", fg="white")
                    self.btn_meja.grid(column=2, row=i-4, padx=(0,5), pady=10)
                elif i not in self.meja:
                    self.btn_meja = tk.Button(self, text=str(i), width=10, height=1, bg='red', fg="white", command=lambda i=i: self.selesai_gunakan(i), activebackground='blue')
                    self.btn_meja.grid(column=2, row=i-4, padx=(0,5), pady=10)
            else:
                if i in self.meja:
                    self.btn_meja = tk.Button(self, text=str(i), width=10, height=1, bg="grey", fg="white")
                    self.btn_meja.grid(column=1, row=i+1, pady=10)
                elif i not in self.meja:
                    self.btn_meja = tk.Button(self, text=str(i), width=10, height=1, bg='red', fg="white", command=lambda i=i: self.selesai_gunakan(i), activebackground='blue')
                    self.btn_meja.grid(column=1, row=i+1, pady=10)

        self.lbl_info = tk.Label(self, text="Info", font=("Arial", 10, "bold"))
        self.lbl_info.grid(column=0, row=6, pady=(2,0), padx=(40,0), sticky="w")

        self.lbl_info = tk.Label(self, text="Merah: Terisi", font=("Arial", 10))
        self.lbl_info.grid(column=0, row=7, pady=(2,0), padx=(40,0), sticky="w")

        self.lbl_info = tk.Label(self, text="Abu-abu: Kosong", font=("Arial", 10))
        self.lbl_info.grid(column=0, row=8, pady=(2,0), padx=(40,0), sticky="w")
        
        self.btn_kembali = tk.Button(self, text="Kembali", width=15, command=self.show_main_window, bg="#4472C4", fg="white")
        self.btn_kembali.grid(column=1, columnspan=2, row=10, padx=10, pady=20 )

    def selesai_gunakan(self, i):
        self.destroy()
        self.num = i
        # print(self.num)
        # print(self.meja)
        resi(self.num, self.master)

    def show_main_window(self):
        self.master.deiconify()
        self.destroy()
        self.mainloop()

class resi(tk.Toplevel):
    def __init__(self, nomeja, master = None):
        super().__init__(master)
        self.geometry("900x470")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.pembeli = Main.pembeli
        self.nama = ""
        self.item = []

        # Find the user from table pembeli by searching the table meja 
        for i in self.pembeli:
            if nomeja == i.nomeja:
                self.nama = i.nama
                self.item = i.data_pesanan
                # print(self.item)

        self.lbl_nama = tk.Label(self, text=f"Nama pemesan: {self.nama}" ,font=("Arial", 10, "bold"))
        self.lbl_nama.grid(column=0, row=0, pady=(10,0), padx=(60,2))

        self.lbl_meja = tk.Label(self, text=f"Meja: {nomeja}", font=("Arial", 10, "bold"))
        self.lbl_meja.grid(column=4, columnspan=2, row=0, pady=(2,0), padx=(60,2))
        
        file_json = open('menu-data.json')
        data = json.load(file_json)
        title = ['Meals', 'Drinks', 'Sides']
        
        # Tampung seluruh data json ke dalam list of object
        Meal = []
        Drink = []
        Side = []
        i = 0
        tk_gurih = 1
        tk_manis = 2
        tk_viral = 2

        for menu in data:
            for item in menu ['item']:
                if title[i] == 'Meals':
                    Meal.append(Meals(item['kodeMenu'], item['namaMenu'], item['harga'],tk_gurih))
                    tk_gurih += 2
                elif title[i] == 'Drinks':
                    Drink.append(Drinks(item['kodeMenu'], item['namaMenu'], item['harga'], tk_manis))
                    tk_manis += 2
                elif title[i] == 'Sides':
                    Side.append(Sides(item['kodeMenu'], item['namaMenu'], item['harga'], tk_viral))
                    tk_viral += 2
            i += 1
        
        listofMeal = [('Kode', 'Nama', 'Harga','Kegurihan')]
        for menu in Meal:
            mytuple = (menu.kode_menu, menu.nama_menu, menu.harga, menu.tingkat_kegurihan)
            listofMeal.append(mytuple)
                
        listofDrink =  [('Kode', 'Nama', 'Harga','Kemanisan')]
        for menu in Drink:
            mytuple = (menu.kode_menu, menu.nama_menu, menu.harga, menu.tingkat_kemanisan)
            listofDrink.append(mytuple)

        listofSide =  [('Kode', 'Nama', 'Harga','Keviralan')]
        for menu in Side:
            mytuple = (menu.kode_menu, menu.nama_menu, menu.harga, menu.tingkat_keviralan)
            listofSide.append(mytuple)

        self.lbl_title = tk.Label(self, text="Meals", width=30)
        self.lbl_title.grid(column=0, row=2, pady=(20,0))
        tableMeal = Table(listofMeal, title[0], self)
        tableMeal.grid(columnspan=5, rowspan=4,  padx=(100,2))

        self.lbl_title = tk.Label(self, text="Drinks", width=30)
        self.lbl_title.grid(column=0, row=8, pady=(20,0))
        tableDrink = Table(listofDrink, title[1], self)
        tableDrink.grid(columnspan=5, rowspan=4,  padx=(100,2))

        self.lbl_title = tk.Label(self, text="Sides", width=30)
        self.lbl_title.grid(column=0, row=14, pady=(40,0))
        tableSide = Table(listofSide, title[2], self)
        tableSide.grid(columnspan=5, rowspan=4, padx=(100,2))

        #  Grid combobox
        self.lbl = tk.Entry(self,fg="black",font=("Arial", 10, "bold"))
        self.lbl.grid(row=4, column = 4, padx=(300,0), pady=(20,0))
        self.lbl.insert(tk.END, self.item[0])
        self.lbl['state'] = 'readonly'

        self.lbl1 = tk.Entry(self, fg="black", font=("Arial", 10, "bold"))
        self.lbl1.grid(row=6, column =4, padx=(300,0))
        self.lbl1.insert(tk.END, self.item[1])
        self.lbl1['state'] = 'readonly'          

        self.lbl2 = tk.Entry(self, fg="black", font=("Arial", 10, "bold"))
        self.lbl2.grid(row=10, column =4,padx=(300,0), pady=(20,0))
        self.lbl2.insert(tk.END, self.item[2])
        self.lbl2['state'] = 'readonly'

        self.lbl3 = tk.Entry(self, fg="black", font=("Arial", 10, "bold"))
        self.lbl3.grid(row=12, column =4, padx=(300,0))
        self.lbl3.insert(tk.END, self.item[3])
        self.lbl3['state'] = 'readonly'

        self.lbl4 = tk.Entry(self,fg="black", font=("Arial", 10, "bold"))
        self.lbl4.grid(row=16, column =4, padx=(300,0),  pady=(20,0))
        self.lbl4.insert(tk.END, self.item[4])
        self.lbl4['state'] = 'readonly'

        self.lbl5 = tk.Entry(self,fg="black", font=("Arial", 10, "bold"))
        self.lbl5.grid(row=18, column = 4, padx=(300,0))
        self.lbl5.insert(tk.END, self.item[5])
        self.lbl5['state'] = 'readonly'

        def go_back():
            self.destroy()
            SelesaiGunakanMeja(self.master)

        def destroying():
            Main.meja.append(nomeja)
            self.destroy()
            SelesaiGunakanMeja(self.master)
            
        #  Grid button
        self.btn = tk.Button(self, text="Kembali", padx=50, bg="#4472C4", command=go_back)
        self.btn.grid(row=20, columnspan=2, column=1, padx=(30,0), pady=(20,0))
        self.btn = tk.Button(self, text="Selesai Gunakan Meja", padx=10, bg="#4472C4", command=destroying)
        self.btn.grid(row=20, columnspan=2, column=3, padx=(30,0), pady=(20,0))

        self.mainloop()

class MenuWindow(tk.Toplevel):
    meja = Main.meja
    
    def __init__(self, nama, nomeja, master = None):
        super().__init__(master)
        self.geometry("900x470")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.nama = nama
        self.nomeja = nomeja
        self.lbl_nama = tk.Label(self, text=f"Nama pemesan: {self.nama}" )
        self.lbl_nama.grid(column=0, row=0, pady=(10,0), padx=(60,2))
        
        try:
            self.num = self.nomeja
        except IndexError:
            self.exit()
            main = Main(self.master)
            main.mainloop()
        
        self.lbl_meja = tk.Label(self, text=f"No Meja: {self.num}")
        self.lbl_meja.grid(column=4, row=0, pady=(10,0), padx=(40,2))

        self.btn_ubah = tk.Button(self, text="Ubah", width=5,  bg="#4472C4", fg="white", command=lambda: self.ubah_meja(self.num, self.nama))
        self.btn_ubah.grid(column=5, row=0, pady=(10,0), padx=(0,2))

        file_json = open('menu-data.json')
        data = json.load(file_json)
        title = ['Meals', 'Drinks', 'Sides']
        
        # Tampung seluruh data json ke dalam list of object
        Meal = []
        Drink = []
        Side = []

        i = 0
        tk_gurih = 1
        tk_manis = 2
        tk_viral = 2

        for menu in data:
            for item in menu ['item']:
                if title[i] == 'Meals':
                    Meal.append(Meals(item['kodeMenu'], item['namaMenu'], item['harga'],tk_gurih))
                    tk_gurih += 2
                elif title[i] == 'Drinks':
                    Drink.append(Drinks(item['kodeMenu'], item['namaMenu'], item['harga'], tk_manis))
                    tk_manis += 2
                elif title[i] == 'Sides':
                    Side.append(Sides(item['kodeMenu'], item['namaMenu'], item['harga'], tk_viral))
                    tk_viral += 2
            i += 1
        
        listofMeal = [('Kode', 'Nama', 'Harga','Kegurihan')]
        for menu in Meal:
            mytuple = (menu.kode_menu, menu.nama_menu, menu.harga, menu.tingkat_kegurihan)
            listofMeal.append(mytuple)
                
        listofDrink =  [('Kode', 'Nama', 'Harga','Kemanisan')]
        for menu in Drink:
            mytuple = (menu.kode_menu, menu.nama_menu, menu.harga, menu.tingkat_kemanisan)
            listofDrink.append(mytuple)

        listofSide =  [('Kode', 'Nama', 'Harga','Keviralan')]
        for menu in Side:
            mytuple = (menu.kode_menu, menu.nama_menu, menu.harga, menu.tingkat_keviralan)
            listofSide.append(mytuple)

        self.lbl_title = tk.Label(self, text="Meals", width=30)
        self.lbl_title.grid(column=0, row=2, pady=(20,0))
        tableMeal = Table(listofMeal, title[0], self)
        tableMeal.grid(columnspan=5, rowspan=4,  padx=(100,2))

        self.lbl_title = tk.Label(self, text="Drinks", width=30)
        self.lbl_title.grid(column=0, row=8, pady=(20,0))
        tableDrink = Table(listofDrink, title[1], self)
        tableDrink.grid(columnspan=5, rowspan=4,  padx=(100,2))

        self.lbl_title = tk.Label(self, text="Sides", width=30)
        self.lbl_title.grid(column=0, row=14, pady=(40,0))
        tableSide = Table(listofSide, title[2], self)
        tableSide.grid(columnspan=5, rowspan=4, padx=(100,2))

        btn_kembali = tk.Button(self, text="Kembali", width=30, command=self.show_main_window, bg="#4472C4", fg="white")
        btn_kembali.grid(column=1, row=22, pady=(30,0))
        btn_OK = tk.Button(self, text="OK", width=30, command=lambda: self.pesan(get_total), bg="#4472C4", fg="white")
        btn_OK.grid(column=2, row=22, pady=(30,0))

        vars = tk.StringVar()
        vars1 = tk.StringVar()
        vars2 = tk.StringVar()
        vars3 = tk.StringVar()
        vars4 = tk.StringVar()
        vars5 = tk.StringVar()

        # Combobox 1
        values = tuple([k for k in range(10)])

        self.opsi_jumlah = ttk.Combobox(self, values = values, textvariable=vars, width=16)
        self.opsi_jumlah1 = ttk.Combobox(self, values = values, textvariable=vars1, width=16)
        self.opsi_jumlah2 = ttk.Combobox(self, values = values, textvariable=vars2, width=16)
        self.opsi_jumlah3 = ttk.Combobox(self, values = values, textvariable=vars3, width=16)
        self.opsi_jumlah4 = ttk.Combobox(self, values = values, textvariable=vars4, width=16)
        self.opsi_jumlah5 = ttk.Combobox(self, values = values, textvariable=vars5, width=16)

        #  Grid combobox
        self.opsi_jumlah.grid(rowspan = 2, row=4, column = 4)
        self.opsi_jumlah.current(0)
        self.opsi_jumlah['state'] = ['readonly']

        self.opsi_jumlah1.grid(rowspan = 2, row=6, column = 4)
        self.opsi_jumlah1.current(0)
        self.opsi_jumlah1['state'] = ['readonly']

        self.opsi_jumlah2.grid(rowspan=2, row = 10, column = 4)
        self.opsi_jumlah2.current(0)
        self.opsi_jumlah2['state'] = ['readonly']

        self.opsi_jumlah3.grid(rowspan = 2, row=12, column = 4)
        self.opsi_jumlah3.current(0)
        self.opsi_jumlah3['state'] = ['readonly']

        self.opsi_jumlah4.grid(rowspan=2, row= 16, column = 4)
        self.opsi_jumlah4.current(0)
        self.opsi_jumlah4['state'] = ['readonly']

        self.opsi_jumlah5.grid(rowspan = 2, row=18, column = 4)
        self.opsi_jumlah5.current(0)
        self.opsi_jumlah5['state'] = ['readonly']

        def get_total(*arg):
            temp = [-1,-1,-1,-1,-1,-1,-1]
            price = [52000,56000, 25000,30000,10000,10000]
            if vars.get():
                temp[0] = int(vars.get())
            if vars1.get():
                temp[1] = int(vars1.get())
            if vars2.get():
                temp[2] = int(vars2.get())
            if vars3.get():
                temp[3] = int(vars3.get())
            if vars4.get():
                temp[4] = int(vars4.get())
            if vars5.get():
                temp[5] = int(vars5.get())

            total_price = 0
            for i in range(6):
                if i != -1:
                    total_price += temp[i] * price[i]
            temp[6] = total_price
            #  Label
            self.lbl_total = tk.Label(self, text=f"Total: {total_price}", width=10, font=("Arial", 12, "bold"))
            self.lbl_total.grid(column=2, row=21, pady=(10,0))
            
            return temp

        vars.trace("w", get_total)
        vars1.trace("w", get_total)
        vars2.trace("w", get_total)
        vars3.trace("w", get_total)
        vars4.trace("w", get_total)
        vars5.trace("w", get_total)
        
        # Label Total
        self.lbl_total = tk.Label(self, text=f"Total: ", width=10, font=("Arial", 12, "bold"))
        self.lbl_total.grid(column=2, row=21, pady=(10,0))

        self.mainloop()
    
    # Fungsi untuk kembali ke tampilan utama
    def show_main_window(self):
        self.master.deiconify()
        self.destroy()

    # Fungsi untuk mengubah nomor meja
    def ubah_meja(self, temp, nama):
        self.destroy()
        UbahMeja(self.meja,temp,nama,self.master)

    def pesan(self,get_total):
        # Panggil fungsi get_total untuk mendapatkan total harga
        total = get_total()
        temp = self.nomeja
        self.master.deiconify()
        self.destroy()
        Main.pembeli.append(Pembeli(self.nama,self.nomeja,total[6], total))
        self.meja.remove(temp)
        self.mainloop()

# Class untuk membuat sebuah table dari data json yang telah diolah.
class Table(tk.Frame):
    def __init__(self, data, title, master=None):
        super().__init__(master)
        self.master = master
        self.data = data
        self.total_rows = len(data)
        self.total_columns = len(data[0])
        # self.combo ()
        self.title = title
        self.sum = 0
        self.generate_table()

    def generate_table(self):
        # header table
        lbl_jumlah = tk.Label(self, text="Jumlah", borderwidth=1, relief='sunken', padx=40)
        lbl_jumlah.grid(row = 0, column=4)

        for i in range(self.total_columns):
            self.e = tk.Entry(self, width=20, fg='black', font=('Arial',10))
            self.e.grid(row=0, column=i)
            self.e.insert(tk.END, self.data[0][i])
            self.e['state'] = 'readonly'

        for i in range(1,self.total_rows):
            # header table
            for j in range(self.total_columns):
                self.e = tk.Entry(self, width=20, fg='black', font=('Arial',10))
                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, self.data[i][j])
                self.e['state'] = 'readonly'

# Class untuk mengubah nomor meja
class UbahMeja(tk.Toplevel):
    def __init__(self, data, temp, nama, master=None):
        super().__init__(master)
        self.master = master
        self.data = data
        self.temp = temp
        self.nama = nama
        self.master.geometry("450x250")
        self.geometry("550x500")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        self.lbl_command = tk.Label(self, text="Silakan klik meja kosong yang diinginkan:", anchor='center')
        self.lbl_command.grid(columnspan=3, row=0, padx=(150,0), pady=(20,15))

        self.finalNum = self.temp
        for i in range(10):
            if(i>4):
                # Jika angka terdapat pada list, warna abu abu
                if i in self.data:
                    if i == self.temp:
                        self.btn_meja = tk.Button(self, text=str(i), width=15, height=1, bg="blue", fg="white")
                        self.btn_meja.grid(column=2, row=i-4, padx=(0,5), pady=10)
                    else:    
                        self.btn_meja = tk.Button(self, text=str(i), width=15, height=1, bg="grey", fg="white", command=lambda i=i: self.ubah_nomor(i), activebackground='blue')
                        self.btn_meja.grid(column=2, row=i-4, padx=(0,5), pady=10)
                elif i not in self.data:
                    self.btn_meja = tk.Button(self, text=str(i), width=15, height=1, bg='red', fg="white")
                    self.btn_meja.grid(column=2, row=i-4, padx=(0,5), pady=10)
            else:
                if i in self.data:
                    if i == self.temp:
                        self.btn_meja = tk.Button(self, text=str(i), width=15, height=1, bg='blue', fg="white")
                        self.btn_meja.grid(column=1, row=i+1, pady=10)
                    else:
                        self.btn_meja = tk.Button(self, text=str(i), width=15, height=1, bg="grey", fg="white", command=lambda i=i: self.ubah_nomor(i), activebackground='blue')
                        self.btn_meja.grid(column=1, row=i+1, pady=10)
                elif i not in self.data:
                    if i == self.temp:
                        self.btn_meja = tk.Button(self, text=str(i), width=15, height=1, bg='blue', fg="white")
                        self.btn_meja.grid(column=1, row=i+1, pady=10)
                    else:
                        self.btn_meja = tk.Button(self, text=str(i), width=15, height=1, bg='red', fg="white")
                        self.btn_meja.grid(column=1, row=i+1, pady=10)


        self.lbl_info = tk.Label(self, text="Info", font=("Arial", 10, "bold"))
        self.lbl_info.grid(column=0, row=6, pady=(2,0), padx=(40,0), sticky="w")

        self.lbl_info = tk.Label(self, text="Merah: Terisi", font=("Arial", 10))
        self.lbl_info.grid(column=0, row=7, pady=(2,0), padx=(40,0), sticky="w")

        self.lbl_info = tk.Label(self, text="Abu-abu: Kosong", font=("Arial", 10))
        self.lbl_info.grid(column=0, row=8, pady=(2,0), padx=(40,0), sticky="w")

        self.lbl_info = tk.Label(self, text="Biru: Meja Anda", font=("Arial", 10))
        self.lbl_info.grid(column=0, row=9, pady=(2,0), padx=(40,0), sticky="w")

        self.btn_kembali  =  tk.Button(self, text="Kembali", width=15, command=lambda:self.show_menu_window(nama), bg="#4472C4", fg="white")
        self.btn_kembali.grid(column=1, row=10, padx=10, pady=20 )

        self.btn_oke  =  tk.Button(self, text="OK", width=15, bg="#4472C4", fg="white", command=lambda: self.ubah(self.finalNum))
        self.btn_oke.grid(column=2, row=10, padx=10, pady=20 )

    def ubah_nomor(self, number):
        self.finalNum = number

    def show_menu_window( self, nama ):
        self.destroy()
        MenuWindow(nama, self.temp, self.master)

    def ubah(self, number):
        self.destroy()
        MenuWindow(self.nama,number, self.master)       

def main():
    # TODO mengolah data menu
    window = tk.Tk()
    cafe = Main(window)
    cafe.mainloop()

if __name__ == '__main__':
    main()