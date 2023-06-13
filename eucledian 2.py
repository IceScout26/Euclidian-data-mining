import math
import tkinter as tk
from tkinter import ttk
import pandas as pd

# Fungsi untuk menghitung jarak Euclidean antara dua data
def euclidean_distance(data1, data2):
    distance = math.sqrt((data1[0] - data2[0])**2 + (data1[1] - data2[1])**2)
    return distance

# Fungsi untuk menghitung jarak Euclidean antara data training
def calculate_distances():
    # Menghapus data tabel hasil sebelumnya (jika ada)
    distances_table.delete(*distances_table.get_children())

    # Mengambil data training dari input pengguna
    data_training = []
    for i in range(num_entries):
        x = data_entries_x[i].get()
        y = data_entries_y[i].get()
        data_training.append([float(x), float(y)])

    # Menghitung jarak Euclidean antara data training
    distances = []
    for i in range(len(data_training)):
        for j in range(i + 1, len(data_training)):
            data1 = data_training[i]
            data2 = data_training[j]
            distance = euclidean_distance(data1, data2)
            distances.append((i+1, j+1, distance))

    # Membuat dataframe dari data training
    df_training = pd.DataFrame(data_training, columns=['X', 'Y'])

    # Membuat dataframe dari hasil jarak Euclidean
    df_distances = pd.DataFrame(distances, columns=['Data 1', 'Data 2', 'Jarak Euclidean'])

    # Mengambil data jarak terkecil
    data_terkecil = distances[0]

    # Menampilkan data training pada tabel
    for index, row in df_training.iterrows():
        data_table.insert('', tk.END, text=index+1, values=(row['X'], row['Y']))

    # Menampilkan hasil jarak Euclidean pada tabel
    for index, row in df_distances.iterrows():
        distances_table.insert('', tk.END, text=index+1, values=(row['Data 1'], row['Data 2'], row['Jarak Euclidean']))

    # Menampilkan kesimpulan jarak terkecil
    label_kesimpulan.config(text=f"Jarak terkecil: Data {data_terkecil[0]} dan Data {data_terkecil[1]}, Jarak Euclidean: {data_terkecil[2]}")

# Fungsi untuk mengubah jumlah entri data training
def change_num_entries():
    global num_entries
    new_num_entries = int(num_entries_entry.get())
    if new_num_entries > num_entries:
        for i in range(num_entries, new_num_entries):
            entry_x = tk.Entry(frame_input_x, width=5)
            entry_x.pack(side=tk.LEFT)
            data_entries_x.append(entry_x)
            
            entry_y = tk.Entry(frame_input_y, width=5)
            entry_y.pack(side=tk.LEFT)
            data_entries_y.append(entry_y)
    elif new_num_entries < num_entries:
        for i in range(num_entries, new_num_entries, -1):
            data_entries_x[-1].destroy()
            data_entries_x.pop()
            
            data_entries_y[-1].destroy()
            data_entries_y.pop()
    num_entries = new_num_entries

# Membuat window GUI
window = tk.Tk()
window.title("Euclidean Distance")
window.geometry("600x400")

# Frame untuk input jumlah data training
frame_num_entries = tk.Frame(window)
frame_num_entries.pack(padx=10, pady=10)

# Label untuk jumlah data training
label_num_entries = tk.Label(frame_num_entries, text="Jumlah Data Training:")
label_num_entries.pack(side=tk.LEFT)

# Entry untuk jumlah data training
num_entries_entry = tk.Entry(frame_num_entries, width=5)
num_entries_entry.pack(side=tk.LEFT)

# Tombol untuk mengubah jumlah data training
button_change_entries = tk.Button(frame_num_entries, text="Ubah", command=change_num_entries)
button_change_entries.pack(side=tk.LEFT)

# Frame untuk input data training
frame_input = tk.Frame(window)
frame_input.pack(padx=10, pady=10)

# Label input data training
label_input = tk.Label(frame_input, text="Input Data Training")
label_input.pack()

# Frame untuk input data X
frame_input_x = tk.Frame(frame_input)
frame_input_x.pack()

# Frame untuk input data Y
frame_input_y = tk.Frame(frame_input)
frame_input_y.pack()

# List untuk menyimpan entry data X dan Y
data_entries_x = []
data_entries_y = []

# Jumlah awal entri data training
num_entries = 3

# Membuat entry data X dan Y awal
for i in range(num_entries):
    entry_x = tk.Entry(frame_input_x, width=5)
    entry_x.pack(side=tk.LEFT)
    data_entries_x.append(entry_x)

    entry_y = tk.Entry(frame_input_y, width=5)
    entry_y.pack(side=tk.LEFT)
    data_entries_y.append(entry_y)

# Tombol hitung
button_hitung = tk.Button(frame_input, text="Hitung", command=calculate_distances)
button_hitung.pack(pady=10)

# Frame untuk tabbed view
frame_tabs = ttk.Notebook(window)
frame_tabs.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Frame untuk tab data training
frame_training = ttk.Frame(frame_tabs)
frame_tabs.add(frame_training, text='Data Training')

# Label tabel data training
label_training = tk.Label(frame_training, text="Data Training")
label_training.pack()

# Membuat tabel data training
data_table = ttk.Treeview(frame_training)
data_table['columns'] = ('X', 'Y')
data_table.column('#0', width=0, stretch=tk.NO)
data_table.column('X', anchor=tk.CENTER, width=100)
data_table.column('Y', anchor=tk.CENTER, width=100)
data_table.heading('#0', text='', anchor=tk.CENTER)
data_table.heading('X', text='X', anchor=tk.CENTER)
data_table.heading('Y', text='Y', anchor=tk.CENTER)
data_table.pack(pady=10)

# Frame untuk tab hasil jarak Euclidean
frame_distances = ttk.Frame(frame_tabs)
frame_tabs.add(frame_distances, text='Hasil Jarak Euclidean')

# Label tabel hasil jarak Euclidean
label_distances = tk.Label(frame_distances, text="Hasil Jarak Euclidean")
label_distances.pack()

# Membuat tabel hasil jarak Euclidean
distances_table = ttk.Treeview(frame_distances)import math
import tkinter as tk
from tkinter import ttk
import pandas as pd

# Fungsi untuk menghitung jarak Euclidean antara dua data
def euclidean_distance(data1, data2):
    distance = math.sqrt((data1[0] - data2[0])**2 + (data1[1] - data2[1])**2)
    return distance

# Fungsi untuk menghitung jarak Euclidean antara data training
def calculate_distances():
    # Menghapus data tabel hasil sebelumnya (jika ada)
    distances_table.delete(*distances_table.get_children())

    # Mengambil data training dari input pengguna
    data_training = []
    for i in range(num_entries):
        x = data_entries_x[i].get()
        y = data_entries_y[i].get()
        data_training.append([float(x), float(y)])

    # Menghitung jarak Euclidean antara data training
    distances = []
    for i in range(len(data_training)):
        for j in range(i + 1, len(data_training)):
            data1 = data_training[i]
            data2 = data_training[j]
            distance = euclidean_distance(data1, data2)
            distances.append((i+1, j+1, distance))

    # Membuat dataframe dari data training
    df_training = pd.DataFrame(data_training, columns=['X', 'Y'])

    # Membuat dataframe dari hasil jarak Euclidean
    df_distances = pd.DataFrame(distances, columns=['Data 1', 'Data 2', 'Jarak Euclidean'])

    # Mengambil data jarak terkecil
    data_terkecil = distances[0]

    # Menampilkan data training pada tabel
    for index, row in df_training.iterrows():
        data_table.insert('', tk.END, text=index+1, values=(row['X'], row['Y']))

    # Menampilkan hasil jarak Euclidean pada tabel
    for index, row in df_distances.iterrows():
        distances_table.insert('', tk.END, text=index+1, values=(row['Data 1'], row['Data 2'], row['Jarak Euclidean']))

    # Menampilkan kesimpulan jarak terkecil
    label_kesimpulan.pack_forget()  # Menghapus label kesimpulan sebelumnya (jika ada)
    label_kesimpulan.config(text=f"Jarak terkecil: Data {data_terkecil[0]} dan Data {data_terkecil[1]}, Jarak Euclidean: {data_terkecil[2]}")
    label_kesimpulan.pack(pady=10)

# Fungsi untuk mengubah jumlah entri data training
def change_num_entries():
    global num_entries
    new_num_entries = int(num_entries_entry.get())
    if new_num_entries > num_entries:
        for i in range(num_entries, new_num_entries):
            label_x = tk.Label(frame_input_x, text="x" + str(i+1) + ":")
            label_x.pack(side=tk.LEFT)
            entry_x = tk.Entry(frame_input_x, width=5)
            entry_x.pack(side=tk.LEFT)
            data_entries_x.append(entry_x)

            label_y = tk.Label(frame_input_y, text="y" + str(i+1) + ":")
            label_y.pack(side=tk.LEFT)
            entry_y = tk.Entry(frame_input_y, width=5)
            entry_y.pack(side=tk.LEFT)
            data_entries_y.append(entry_y)
    elif new_num_entries < num_entries:
        for i in range(num_entries, new_num_entries, -1):
            data_entries_x[-1].destroy()
            data_entries_x.pop()

            data_entries_y[-1].destroy()
            data_entries_y.pop()
    num_entries = new_num_entries

# Membuat window GUI
window = tk.Tk()
window.title("Euclidean Distance")
window.geometry("600x400")

# Frame untuk input jumlah data training
frame_num_entries = tk.Frame(window)
frame_num_entries.pack(padx=10, pady=10)

# Label untuk jumlah data training
label_num_entries = tk.Label(frame_num_entries, text="Jumlah Data Training:")
label_num_entries.pack(side=tk.LEFT)

# Entry untuk jumlah data training
num_entries_entry = tk.Entry(frame_num_entries, width=5)
num_entries_entry.pack(side=tk.LEFT)

# Tombol untuk mengubah jumlah data training
button_change_entries = tk.Button(frame_num_entries, text="Ubah", command=change_num_entries)
button_change_entries.pack(side=tk.LEFT)

# Frame untuk input data training
frame_input = tk.Frame(window)
frame_input.pack(padx=10, pady=10)

# Label input data training
label_input = tk.Label(frame_input, text="Input Data Training")
label_input.pack()

# Frame untuk input data X
frame_input_x = tk.Frame(frame_input)
frame_input_x.pack()

# Frame untuk input data Y
frame_input_y = tk.Frame(frame_input)
frame_input_y.pack()

# List untuk menyimpan entry data X dan Y
data_entries_x = []
data_entries_y = []

# Jumlah awal entri data training
num_entries = 3

# Membuat entry data X dan Y awal
for i in range(num_entries):
    label_x = tk.Label(frame_input_x, text="x" + str(i+1) + ":")
    label_x.pack(side=tk.LEFT)
    entry_x = tk.Entry(frame_input_x, width=5)
    entry_x.pack(side=tk.LEFT)
    data_entries_x.append(entry_x)

    label_y = tk.Label(frame_input_y, text="y" + str(i+1) + ":")
    label_y.pack(side=tk.LEFT)
    entry_y = tk.Entry(frame_input_y, width=5)
    entry_y.pack(side=tk.LEFT)
    data_entries_y.append(entry_y)

# Tombol hitung
button_hitung = tk.Button(frame_input, text="Hitung", command=calculate_distances)
button_hitung.pack(pady=10)

# Frame untuk tabbed view
frame_tabs = ttk.Notebook(window)
frame_tabs.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Frame untuk tab data training
frame_training = ttk.Frame(frame_tabs)
frame_tabs.add(frame_training, text='Data Training')

# Label tabel data training
label_training = tk.Label(frame_training, text="Data Training")
label_training.pack()

# Membuat tabel data training
data_table = ttk.Treeview(frame_training)
data_table['columns'] = ('X', 'Y')
data_table.column('#0', width=0, stretch=tk.NO)
data_table.column('X', anchor=tk.CENTER, width=100)
data_table.column('Y', anchor=tk.CENTER, width=100)
data_table.heading('#0', text='', anchor=tk.CENTER)
data_table.heading('X', text='X', anchor=tk.CENTER)
data_table.heading('Y', text='Y', anchor=tk.CENTER)
data_table.pack(pady=10)

# Frame untuk tab hasil jarak Euclidean
frame_distances = ttk.Frame(frame_tabs)
frame_tabs.add(frame_distances, text='Hasil Jarak Euclidean')

# Label tabel hasil jarak Euclidean
label_distances = tk.Label(frame_distances, text="Hasil Jarak Euclidean")
label_distances.pack()

# Membuat tabel hasil jarak Euclidean
distances_table = ttk.Treeview(frame_distances)
distances_table['columns'] = ('Data 1', 'Data 2', 'Jarak Euclidean')
distances_table.column('#0', width=0, stretch=tk.NO)
distances_table.column('Data 1', anchor=tk.CENTER, width=100)
distances_table.column('Data 2', anchor=tk.CENTER, width=100)
distances_table.column('Jarak Euclidean', anchor=tk.CENTER, width=150)
distances_table.heading('#0', text='', anchor=tk.CENTER)
distances_table.heading('Data 1', text='Data 1', anchor=tk.CENTER)
distances_table.heading('Data 2', text='Data 2', anchor=tk.CENTER)
distances_table.heading('Jarak Euclidean', text='Jarak Euclidean', anchor=tk.CENTER)
distances_table.pack(pady=10)

# Label kesimpulan jarak terkecil
label_kesimpulan = tk.Label(window, text="")
label_kesimpulan.pack()

# Menjalankan GUI
window.mainloop()

distances_table['columns'] = ('Data 1', 'Data 2', 'Jarak Euclidean')
distances_table.column('#0', width=0, stretch=tk.NO)
distances_table.column('Data 1', anchor=tk.CENTER, width=100)
distances_table.column('Data 2', anchor=tk.CENTER, width=100)
distances_table.column('Jarak Euclidean', anchor=tk.CENTER, width=150)
distances_table.heading('#0', text='', anchor=tk.CENTER)
distances_table.heading('Data 1', text='Data 1', anchor=tk.CENTER)
distances_table.heading('Data 2', text='Data 2', anchor=tk.CENTER)
distances_table.heading('Jarak Euclidean', text='Jarak Euclidean', anchor=tk.CENTER)
distances_table.pack(pady=10)

# Label kesimpulan jarak terkecil
label_kesimpulan = tk.Label(window, text="")
label_kesimpulan.pack(pady=10)

# Menjalankan window GUI
window.mainloop()
