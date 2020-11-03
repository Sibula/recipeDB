from tkinter import *
from tkinter import ttk


def placeholder(*args):
    pass


def main():
    root = Tk()
    root.title("RecipeDB")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Main frame
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    # Controls frame
    controls = ttk.Frame(mainframe, padding="3 3 12 12")
    controls.grid(column=0, row=0, sticky=(N, W, S))
    controls.columnconfigure(0, weight=1)
    controls.columnconfigure(1, weight=0)
    controls.rowconfigure(0, weight=1)

    # Content frame
    content = ttk.Frame(mainframe, padding="3 3 12 12")
    content.grid(column=1, row=0, sticky=(N, E, S))
    content.columnconfigure(0, weight=1)
    content.rowconfigure(0, weight=1)

    # Search bar and button
    search = StringVar()
    search_entry = Entry(controls, width=20, textvariable=search)
    search_entry.grid(column=0, row=0, sticky=(N, W))
    search_button = Button(controls, text="Search", command=placeholder)
    search_button.grid(column=1, row=0, sticky=(N, W))

    # Content field
    text_field = Text(content, width = 50, height = 30, wrap = "word")
    vs = ttk.Scrollbar(content, orient = 'vertical', command = text_field.yview)
    text_field['yscroll'] = vs.set
    text_field.grid(column=0, row=0, sticky=(N, W, E, S))
    vs.grid(column=1, row=0, sticky=(N, E, S))


    search_entry.focus()
    root.bind("<Return>", placeholder)

    root.mainloop()


if __name__ == '__main__':
    main()
