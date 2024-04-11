from pathlib import Path
import tkinter as tk

# The list of tags you want to display.
tags = list(filter(None, Path('tags.txt').read_text(encoding='utf-8').split('\n')))

# This function will be called when a tag in the ListBox is clicked.
def add_or_remove_tag(event):
    # Get the index of the selected tag.
    indices = listbox.curselection()
    # If no item is selected, do nothing.
    if not indices:
        return
    index = indices[0]
    # Get the tag's text.
    tag_text = listbox.get(index)
    # Retrieve the current text from the Text widget and split it into a list of tags.
    current_tags_text = text_box.get("1.0", tk.END).strip()
    current_tags = current_tags_text.split(", ") if current_tags_text else []
    if tag_text in current_tags:
        # If the tag is already in the list, remove it.
        current_tags.remove(tag_text)
    else:
        # If the tag is not in the list, add it.
        current_tags.append(tag_text)
    # Update the Text widget with the new list of tags.
    new_text = ", ".join(current_tags)
    text_box.delete("1.0", tk.END)
    text_box.insert("1.0", new_text)

# Create the main window.
root = tk.Tk()
root.title("Tag Selector")

# Create the listbox to display the tags.
listbox = tk.Listbox(root, width=50, height=40)
listbox.pack(side=tk.LEFT, fill=tk.Y)
# Bind the ListBox click event to the add_or_remove_tag function.
listbox.bind('<<ListboxSelect>>', add_or_remove_tag)

# Add the tags to the listbox.
for tag in tags:
    listbox.insert(tk.END, tag)

# Create the Text widget that will display the selected tags.
text_box = tk.Text(root, width=100, height=40, wrap=tk.WORD)
text_box.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Start the application.
root.mainloop()