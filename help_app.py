import tkinter as tk
from tkinter import *


class HelpApp:

    def __init__(self):
        window_ann_name = Tk()


        row = 0

        tk.Label(window_ann_name, text='Key', relief=tk.RIDGE, width=16, bg="lightgrey", font=("Helvetica", 16)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Function', relief=tk.RIDGE, width=55, bg="lightgrey", font=("Helvetica", 16)).grid(row=row,column=1)

        row = row + 1
        tk.Label(window_ann_name, text='p', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Positive - Sentiment ', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)

        row = row + 1
        tk.Label(window_ann_name, text='n', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Negative - Sentiment ', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)

        # row = row + 1
        # tk.Label(window_ann_name, text='t', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        # tk.Label(window_ann_name, text='Neutral - Sentiment ', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)

        row = row + 1
        tk.Label(window_ann_name, text='1', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Teaching Quality and Delivery - Feedback Category', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)
        # tk.Label(window_ann_name, text='Responses  relating to any aspect of teaching delivery \n including tutor characteristics and abilities to manage teaching, motivate and inspire. - \n Feedback Category', relief=tk.RIDGE, height=3, width=65, bg="white", font=("Helvetica", 15)).grid(row=row,column=2)

        row = row + 1
        tk.Label(window_ann_name, text='2', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Tutor Support and Engagement - Feedback Category', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)
        # tk.Label(window_ann_name,
        #          text='Reponses relating to direct tutors support and engagement including: \n time committed; accuracy and timeliness of communications; \nperceptions of approachability.',
        #          relief=tk.RIDGE, height=3, width=65, bg="white", font=("Helvetica", 15)).grid(row=row, column=2)

        row = row + 1
        tk.Label(window_ann_name, text='3', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Assessment - Feedback Category', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)

        row = row + 1
        tk.Label(window_ann_name, text='4', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Feedback - Feedback Category', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)

        row = row + 1
        tk.Label(window_ann_name, text='5', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Course Organisation - Feedback Category', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)

        row = row + 1
        tk.Label(window_ann_name, text='6', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Learning Resources and Facilities - Feedback Category', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)

        row = row + 1
        tk.Label(window_ann_name, text='7', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Curriculm Content and Authenticity - Feedback Category', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)

        row = row + 1
        tk.Label(window_ann_name, text='8', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Placements and Work Experience - Feedback Category', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)

        row = row + 1
        tk.Label(window_ann_name, text='9', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Student life - Feedback Category', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)

        row = row + 1
        tk.Label(window_ann_name, text='o', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Overall Experience - Feedback Category', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)

        row = row + 1
        tk.Label(window_ann_name, text='i', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,column=0)
        tk.Label(window_ann_name, text='Not relevant - Feedback Category', relief=tk.RIDGE, width=55, bg="white", font=("Helvetica", 15)).grid(row=row,column=1)

        row = row + 1
        tk.Label(window_ann_name, text='q', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,
                                                                                                                column=0)
        tk.Label(window_ann_name, text='Number of annotated responses', relief=tk.RIDGE, width=55, bg="white",
                 font=("Helvetica", 15)).grid(row=row, column=1)

        row = row + 1
        tk.Label(window_ann_name, text='m', relief=tk.RIDGE, width=16, bg="white", font=("Helvetica", 15)).grid(row=row,
                                                                                                                column=0)
        tk.Label(window_ann_name, text='Add more feedback labels', relief=tk.RIDGE, width=55, bg="white",
                 font=("Helvetica", 15)).grid(row=row, column=1)


        window_ann_name.title("Keyboard shortcuts")
        # window_ann_name.geometry('200x200')
        window_ann_name.mainloop()

if __name__ == '__main__':
    help_app = HelpApp()
    # root = Tk()
    # scrollbar = Scrollbar(root)
    # scrollbar.pack(side=RIGHT, fill=Y)
    #
    # mylist = Listbox(root, yscrollcommand=scrollbar.set)
    # for line in range(100):
    #     mylist.insert(END, "This is line number " + str(line))
    #
    # mylist.pack(side=LEFT, fill=BOTH)
    # scrollbar.config(command=mylist.yview)
    #
    # mainloop()
