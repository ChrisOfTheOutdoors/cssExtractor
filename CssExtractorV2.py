import os
import tkinter as tk
from tkinter import filedialog

# Open a file dialog to let the user choose the folder containing the HTML files
root = tk.Tk()
root.withdraw()
folder_path = filedialog.askdirectory()

# Set the name for the master CSS file
master_css_file = 'master.css'

# Initialize a set to store all the unique classes and ids across all HTML files
all_classes_and_ids = set()

# Loop through each HTML file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.html'):
        # Set the name for the CSS file that will be generated for this HTML file
        css_filename = os.path.splitext(filename)[0] + '.css'
        
        # Initialize a set to store the unique classes and ids in this HTML file
        classes_and_ids = set()
        
        # Open the HTML file and loop through each line
        with open(os.path.join(folder_path, filename), 'r') as f:
            for line in f:
                # Check if the line contains a class or id
                if 'class="' in line:
                    start = line.index('class="') + len('class="')
                    end = line.index('"', start)
                    class_name = line[start:end]
                    classes_and_ids.add('.' + class_name)
                if 'id="' in line:
                    start = line.index('id="') + len('id="')
                    end = line.index('"', start)
                    id_name = line[start:end]
                    classes_and_ids.add('#' + id_name)
        
        # Write the classes and ids in this HTML file to its corresponding CSS file
        with open(os.path.join(folder_path, css_filename), 'w') as f:
            for class_or_id in classes_and_ids:
                if class_or_id not in all_classes_and_ids:
                    f.write(class_or_id + ' {}\n')
                    all_classes_and_ids.add(class_or_id)
                    
# Write the master CSS file containing all the classes and ids that are used on every page
with open(os.path.join(folder_path, master_css_file), 'w') as f:
    for class_or_id in all_classes_and_ids:
        f.write(class_or_id + ' {}\n')
