import tkinter as tk


def main():
    # Create the main window
    root = tk.Tk()

    # Create a label widget
    label = tk.Label(root, text='Hello, Tkinter!')
    label.pack()

    # Start the GUI event loop
    root.mainloop()



main()