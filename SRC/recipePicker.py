import tkinter as tk
from PIL import ImageTk, Image
import sqlite3

bg_colour = "#3d6466"

def fetch_db():
    # connect to the database
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()

    # fetch all the table names
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()

    # close the connection
    connection.close()

    # return the result
    return all_tables
def fetch_db():
    connection = sqlite3.connect("D:\CODING\Proyectos\TKInter\APP_YT_TUTORIAL\DATA\database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema where type='table';") 
    all_tables = cursor.fetchall()
    print (all_tables[0])
    connection.close()

def load_frame1():
    """
    Load the contents of frame1.
    """

    frame1.pack_propagate(False)

    # Load logo image
    logo_img = ImageTk.PhotoImage(file="d:/CODING/Proyectos/TKInter/APP_YT_TUTORIAL/ASSETS/RRecipe_logo.png")

    # Create and display logo widget
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

    # Create and display instructions widget
    tk.Label(
        frame1,
        text="ready for your random recipe?",
        bg=bg_colour,
        fg="white",
        font=("Coolvetica", 20)
    ).pack()

    # Create and display button widget
    tk.Button(
        frame1,
        text="SHUFFLE",
        font=("Coolvetica", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="#000000",
        command=lambda: load_frame2()
    ).pack(pady=20)

def load_frame2():
    fetch_db()
    


# initiallize app
root = tk.Tk()
root.title("Recipe Picker") 

#place app in the center
root.eval('tk::PlaceWindow . center')

#create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()
root.mainloop()