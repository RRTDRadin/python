import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwith=1
        )
        frame.grid(row=i,colum=j, padx=5,pady=5)
        lable = tk.Lable(master=frame, text=f"Row {i}\nColum {j}")
        lable.pack()

window.mainloop()