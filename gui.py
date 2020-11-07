import tkinter as tk
from tkinter import ttk

class GUI():
    def __init__(self):
        root = tk.Tk()
        root.title("RecipeDB")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Main frame
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky="NWES")
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        # Controls frame
        controls = ttk.Frame(mainframe, padding="3 3 12 12")
        controls.grid(column=0, row=0, sticky="NWS")
        controls.columnconfigure(0, weight=1)
        controls.columnconfigure(1, weight=0)
        controls.rowconfigure(0, weight=1)

        # Content frame
        content = ttk.Frame(mainframe, padding="3 3 12 12")
        content.grid(column=1, row=0, sticky="NES")
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)

        # Search bar and button
        search = tk.StringVar()
        search_entry = ttk.Entry(controls, width=20, textvariable=search)
        search_entry.grid(column=0, row=0, sticky="NW")
        search_button = ttk.Button(controls, text="Search", command=self.placeholder)
        search_button.grid(column=1, row=0, sticky="NW")

        # Content field
        text_field = tk.Text(content, width = 50, height = 30, wrap = "word")
        vs = ttk.Scrollbar(content, orient = 'vertical', command = text_field.yview)
        text_field['yscroll'] = vs.set
        text_field.grid(column=0, row=0, sticky="NWES")
        vs.grid(column=1, row=0, sticky="NES")

        search_entry.focus()
        root.bind("<Return>", self.placeholder)

        root.mainloop()
    
    def placeholder(self):
        pass
