import numpy as np
import tkinter as tk

def calculate_distances():
    # Get the number of datasets from the entry widget
    num_datasets = int(entry_num_datasets.get())

    # Initialize an empty list to store the datasets
    datasets = []

    # Prompt the user to input each dataset
    for i in range(num_datasets):
        dataset = []
        for j in range(2):
            entry_value = entry_datasets[i][j].get()
            dataset.append(int(entry_value))
        datasets.append(np.array(dataset))

    distances = []  # List to store the distances

    # Calculate the Euclidean distance between each pair of datasets
    for i in range(len(datasets) - 1):
        for j in range(i + 1, len(datasets)):
            distance = np.linalg.norm(datasets[j] - datasets[i])
            distances.append(distance)

    # Display the distances in the result label
    result_label.config(text="Distances: " + ", ".join([str(round(d, 2)) for d in distances]))

# Create the main window
window = tk.Tk()
window.title("Euclidean Distance Calculator")

# Create a label and an entry widget for the number of datasets
label_num_datasets = tk.Label(window, text="Number of Datasets:")
label_num_datasets.pack()
entry_num_datasets = tk.Entry(window)
entry_num_datasets.pack()

# Create entry widgets for each dataset
entry_datasets = []
for i in range(20):
    dataset_frame = tk.Frame(window)
    dataset_frame.pack()
    
    dataset_entries = []
    for j in range(2):
        label = tk.Label(dataset_frame, text="Dataset {}: ".format(i+1))
        label.pack(side="left")
        
        entry_dataset = tk.Entry(dataset_frame, width=5)
        entry_dataset.pack(side="left")
        
        dataset_entries.append(entry_dataset)
    entry_datasets.append(dataset_entries)

# Create a button to calculate the distances
calculate_button = tk.Button(window, text="Calculate Distances", command=calculate_distances)
calculate_button.pack()

# Create a label to display the distances
result_label = tk.Label(window, text="")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
