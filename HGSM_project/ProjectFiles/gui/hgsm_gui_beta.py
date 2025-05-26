import tkinter as tk
from tkinter import ttk


class AppGUI(tk.Tk):
    def __init__(self, title, size, minsize, resizable):

        # app window as main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(minsize[0],minsize[1])
        if resizable == 'N':
            self.resizable(width=False, height=False)

        # widgets
        self.grocery_list = GroceryList(self)
        self.list_manager = ListManager(self)
        self.storage_manager = StorageManager(self)

        # run the app
        self.mainloop()

class GroceryList(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.place(x=0, y=0, relwidth=0.6, relheight=0.4)
        self.create_widgets()

    def create_widgets(self):
        # define styles
        style = ttk.Style()
        style.configure('Custom.TCheckbutton', background='white', relief='flat')

        # define widgets
        list_label = ttk.Label(self, text='Grocery List', background='grey', anchor='center')
        column_names = ('ITEM', 'Q', '✓')
        display_dimensions = ((40,20), (5,20), (5,20))
        checkbox_frame = ttk.Frame(self)

        # create the grid
        self.columnconfigure(0, weight=3)
        self.columnconfigure((1, 2), weight=1)

        # place the widgets
        list_label.grid(row=0, column=0, sticky='nsew', columnspan=3, pady=(0, 10))
        for index, name in enumerate(column_names):
            label = ttk.Label(self, text=name, anchor='center')
            label.grid(row=1, column=index, sticky='nsew')

        for index, dimension in enumerate(display_dimensions):
            display = tk.Text(self, width=dimension[0], height=dimension[1], state='disabled')
            display.grid(row=2, column=index, sticky='nsew')

        # checkbox_frame.grid(row=2, column=2, sticky='nsew')
        checkbox = ttk.Checkbutton(self, style='Custom.TCheckbutton')
        checkbox.grid(row=2, column=2, sticky='')


class ListManager(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.place(relx=0.6, y=0, relwidth=0.4, relheight=0.4)
        self.create_widgets()

    def create_widgets(self):

        # define widgets
        manager_label = ttk.Label(self, text='List Manager', background='grey', anchor='center')
        column_name = ('ITEM', 'Q')
        display_dimensions = ((30,5),(5,5))
        m_button_frame = ttk.Frame(self)
        buttons = ('ADD', 'REMOVE')

        # create grid
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        m_button_frame.columnconfigure((0, 1), weight=1)

        # place the widgets
        manager_label.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=(0, 10))
        m_button_frame.grid(row=3, column=0, columnspan=2, sticky='nsew', pady=40)

        for index, name in enumerate(column_name):
            label = ttk.Label(self, text=name, anchor='center')
            label.grid(row=1, column=index, sticky='nsew')

        for index, dimension in enumerate(display_dimensions):
            display = tk.Text(self, width=dimension[0], height=dimension[1])
            display.grid(row=2, column=index, sticky='nsew', padx=2.5)

        for index, name in enumerate(buttons):
            button = ttk.Button(m_button_frame, text=name)
            button.grid(row=3, column=index, sticky='nsew')

class StorageManager(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.place(x=0,rely=0.4, relwidth=1, relheight=0.6)
        self.create_widgets()

    def create_widgets(self):

        # define widgets
        storage_label = ttk.Label(self, text='Home Grocery Storage Status', background='grey', anchor='center')
        column_names = ('ITEM', 'Q', 'Expiration', 'Place')
        display_dimensions = ((20,10), (5,10), (20,10), (20, 10))
        buttons = ('View All', 'Fridge', 'Freezer', 'Pantry')

        s_button_frame = ttk.Frame(self, padding=20)

        # create grid
        self.columnconfigure((0, 2, 3), weight=2)
        self.columnconfigure(1, weight=1)
        s_button_frame.columnconfigure((0, 1, 2, 3), weight=1)

        # place widgets
        storage_label.grid(row=0, column=0, columnspan=4, sticky='nsew', pady=10)
        for index, name in enumerate(column_names):
            label = ttk.Label(self, text=name, anchor='center')
            label.grid(row=1, column=index, sticky='nsew')

        for index, dimension in enumerate(display_dimensions):
            display = tk.Text(self, width=dimension[0], height=dimension[1], state='disabled')
            display.grid(row=2, column=index, sticky='nsew')

        s_button_frame.grid(row=3, column=0, columnspan=4, sticky='nsew')
        for index, name in enumerate(buttons):
            button = ttk.Button(s_button_frame, text=name)
            button.grid(row=0, column=index, sticky='ew')

AppGUI('GO GUI v0.1',(900,600),(600, 600), 'N')