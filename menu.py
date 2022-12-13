import tkinter as tk
import tkinter.ttk as ttk
class Table(tk.Frame):
  def __init__(self, data, master = None):
    super().__init__(master)
    self.pack()
    self.data = data
    self.total_rows = len(self.data)
    self.total_columns = len(self.data[0])
    self.generate_table()
 
  def generate_table(self):
    for i in range(self.total_rows):
        for j in range(self.total_columns - 1):
            entry = tk.Entry(self, width = 20, fg = 'blue')
            entry.grid(row = i, column = j)
            entry.insert(tk.END, self.data[i][j])
            entry['state'] = 'readonly'
 
        # kolom paling kanan -> combobox
        values = tuple([k for k in range(10)])
        opsi_jumlah = ttk.Combobox(self, values = values)
        opsi_jumlah.grid(row = i, column = self.total_columns - 1)
 
if __name__ == "__main__":
  menu_list = [('M01', 'Thai Beef Salad', 52000, 1, 1),
               ('M02', 'Bakso', 20000, 2, 3),
               ('M03', 'Mie Ayam', 20000, 2, 2),
               ('M04', 'Semangkok Mecin', 20000, 5, 3)]
 
  gui = tk.Tk()
  table = Table(menu_list, gui)
  gui.mainloop()
