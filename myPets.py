import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

import pet_db


label_font = "Helvetica 8 bold"
text_font = "Helvetica 8"

class myPetDB(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # rows = 0
        # while rows < 50:
        #     self.rowconfigure(rows, weight=1)
        #     self.columnconfigure(rows, weight=1)
        #     rows += 1

        container = tk.Frame(self) # create a frame for the window
        container.pack(side="top", fill="both", expand = True) #fill will stretch in both directions, expand allows change with window size
        container.grid_rowconfigure(0, weight=1) #0 is minimum number, weight suggests imporance?
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # a place to store the window layouts

        for F in (ViewPet, AddPet): # for all the layouts add items to the frames dictionary
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ViewPet) #call the function show_frame to show the search page

    def show_frame(self, cont):
        # if cont==BrowsePage:
        #     self.frames[BrowsePage].prev_b.invoke() #refresh the browse page view with the new data
        frame = self.frames[cont]
        frame.tkraise()
        #set the current frame, then raise to be the focus


class ViewPet(tk.Frame):
    
    def __init__(self, parent, controller):
        curr_pet = pet_db.find_records('pets', 7)
        curr_stats = pet_db.find_records('stats', 7)
        curr_pic = pet_db.find_records('images', 7)
        print(curr_pet)
        print(curr_stats)
        print(curr_pic)

        tk.Frame.__init__(self,parent) #initialize the Frame parent
        my_tabs = ttk.Notebook(self)
        #my_tabs.grid(row=1, column=0, padx=5, pady=5, columnspan=50, rowspan=49, sticky='NSEW')
        my_tabs.pack(anchor='n', fill='both', expand=True, padx=5, pady=5)
        main_tab = ttk.Frame(my_tabs)
        
        my_tabs.add(main_tab, text='My Pets', sticky='NSEW')
        main_tab_frame = ttk.LabelFrame(main_tab, text=curr_pet[0][1])
        #main_tab_frame.grid(row=1, column=0, padx=5, pady=5)
        main_tab_frame.pack(anchor='n', fill='both', expand=True, padx=5, pady=5)

        my_image = Image.open(curr_pic[0][1])
        w, h = my_image.size
        f = h//200
        show_image = my_image.resize((int(w/f), int(h/f)))
        my_photo = ImageTk.PhotoImage(show_image)  

        pet_image = tk.Label(main_tab_frame, image=my_photo) 
        pet_image.image = my_photo  # strangely, you must keep a reference to the Tkinter object, for example by attaching it to a widget attribute
        pet_image.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        stats_frame = ttk.LabelFrame(main_tab_frame, text="Molly's Stats")
        stats_frame.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        
        dob_label = ttk.Label(stats_frame, text = "D.O.B. ", font = label_font)
        dob_label.grid(row=0, column=0, sticky='e')
        dob_data = ttk.Label(stats_frame, text = curr_pet[0][1], font=text_font)
        dob_data.grid(row=0, column=1, sticky="w")

        breed_label = ttk.Label(stats_frame, text = "Breed ", font = label_font)
        breed_label.grid(row=1, column=0, sticky='e')
        breed_data = ttk.Label(stats_frame, text = curr_pet[0][3], font=text_font)
        breed_data.grid(row=1, column=1, sticky="w")

        sex_label = ttk.Label(stats_frame, text = "Sex ", font = label_font)
        sex_label.grid(row=2, column=0, sticky='e')
        sex_data = ttk.Label(stats_frame, text = curr_pet[0][4], font=text_font)
        sex_data.grid(row=2, column=1, sticky="w")




class AddPet(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent) #initialize the Frame parent


if __name__ == "__main__":
    app = myPetDB()
    #app.geometry('500x500')
    app.mainloop()