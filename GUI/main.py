import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Web Fuzzer")
root.geometry("1200x1200") # Set initial width x height
button = tk.Button(root, text="Stop", command=root.destroy)
button.pack()

# Start the application
root.mainloop()