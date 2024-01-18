from tkinter import *
import time

# Create a tkinter window
window = Tk()
window.title("Tkinter Label Text Updater")
window.geometry("1280x720")
window.config(bg = "skyblue")
content1 = "None"
content2 = "None"
content3 = "OFF"
# Create a label to display the content of the file
window.title("Visitor Counter and Power Management")
title = Label(window, text = "Visitor Counter and Power Management", font = ("Segoe Script", 45), bg = "skyblue")
title.pack(pady = 10)
name1 = Label(window, text = "Number of Visitors in the room : ", font = ("Kristen ITC", 50), bg = "skyblue")
name1.pack()
val1 = Label(window, text=f"{content1}", font = ("Advanced Pixel LCD-7", 30), bg = "skyblue")
val1.pack(pady=0)
name2 = Label(window, text = "Total Number of Visitors Visited : ", font = ("Kristen ITC", 50), bg = "skyblue")
name2.pack()
val2 = Label(window, text=f"{content2}", font = ("Advanced Pixel LCD-7", 30), bg = "skyblue")
val2.pack(pady=0)
stateval = Label(window, text=f"{content3}", font = ("Advanced Pixel LCD-7", 20), bg = "red", fg = "black")
stateval.pack(side = "right", anchor="se")
statelb = Label(window, text="Power State : ", font = ("Advanced Pixel LCD-7", 20), bg = "red", fg = "black")
statelb.pack(side = "right", anchor="se")
name = Label(window, text= 'Programmed by Anupam Kanoongo', font= 'Arial 30 bold').pack(side = "left", anchor = "s")



# Function to update the label
def update_label():
    try:
        # Read the content of the file
        with open("totalin.txt") as file:
            file.seek(0)
            content1 = file.readlines()
            
        if "-" not in content1[0]:
            # Update the label with the content of the file
            val1.config(text=content1)

        # Read the content of the file
        with open("total.txt") as file:
            file.seek(0)
            content2 = file.readlines()

        if "-" not in content2[0]:
            # Update the label with the content of the file
            val2.config(text=content2)
        
        if "-" in content1[0] or content1[0] == "0":
            # Update the label with the content of the file
            stateval.config(text="OFF")

        else:
            stateval.config(text="ON")
    except:
        pass
    # Schedule the update_label function to be called after 1000 milliseconds (1 second)
    window.after(1000, update_label)

# Start the tkinter event loop
window.after(0, update_label)  # Call update_label function after 0 milliseconds to start the update process
window.mainloop()
