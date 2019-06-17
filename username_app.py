from tkinter import *
import ctypes
import platform


class UsernameApp:

    def __init__(self):
        self.window_ann_name = Tk()
        lbl = Label(self.window_ann_name, text="Enter your username:")
        lbl.grid(column=0, row=0)

        self.username_txt_area = Text(self.window_ann_name, height=1, width=30)
        self.username_txt_area.grid(column=1, row=0)
        self.username_txt_area.focus_set()

        submit_bt = Button(self.window_ann_name,
                        text="Submit",
                        fg="blue",
                        height=2,
                        command=self.submit_bt_username)
        submit_bt.grid(column=3, row=0)

        self.window_ann_name.bind('<Return>', self.return_bt_username_window)

        width = self.window_ann_name.winfo_screenwidth()  # width of screen
        height = self.window_ann_name.winfo_screenheight()  # height of screen
        
        print(platform.system())
        self.window_ann_name.geometry(str(int(width/2))+'x'+str(int(height/7)))
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        self.window_ann_name.mainloop()


    def return_bt_username_window(self, event):
        self.submit_bt_username()

    def submit_bt_username(self):

        self.username = self.username_txt_area.get("1.0",END)
        self.username = str(self.username).strip().lower()
        self.window_ann_name.destroy()



if __name__ == "__main__":
    username_app = UsernameApp()
    print(username_app.username)