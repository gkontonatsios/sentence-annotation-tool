from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
import tkinter as tk
import re
from db_utils import insert_db_record
from tkinter import messagebox
import pandas as pd
from sklearn.utils import shuffle
from username_app import UsernameApp
from db_utils import get_visited_comments, create_db_table, get_num_annotated_comments
from nltk.tokenize import sent_tokenize
from help_app import HelpApp

import configparser

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
csv_file = config['FILE_PATHS']['CSV_FILE']


class NSSAnnotatorApp:

    def __init__(self):
        create_db_table()

        self.load_df()

        username_app = UsernameApp()
        self.username = username_app.username

        self.comment_idx = 0

        index = 0
        self.window = Tk()
        self.window.title("Sentence-level Feedback Annotator")

        self.text = scrolledtext.ScrolledText(self.window, height=4, wrap="word", font=("Helvetica", 15))

        self.text.pack(fill="both", expand=True)

        self.text.tag_configure("warning", background="lightgreen", foreground="black")
        self.text.tag_raise("sel")


        self.text.grid(column=0, row=0,  columnspan=4, rowspan=2)

        self.list_of_feedback_var = []
        self.feedback_var = StringVar(self.window)
        self.feedback_var.set("Feedback category") # default value

        self.windows_of_feedback_categories = []
        w = OptionMenu(self.window,
                    self.feedback_var,
                    "Feedback category",
                    "Teaching Quality and Delivery",
                    "Tutor Support and Engagement",
                    "Assessment",
                    "Feedback",
                    "Course Organisation",
                    "Learning Resources and Facilities",
                    "Curriculm Content and Authenticity",
                    "Placements and Work Experience",
                    "Student life",
                    "Overall Experience",
                    "Not relevant")
        w.grid(column=4, row=0)
        self.windows_of_feedback_categories.append(w)

        self.list_of_feedback_var.append(self.feedback_var)
        self.current_row_of_feedback_var = 0

        self.sentiment_var = StringVar(self.window)
        self.sentiment_var.set("Sentiment category") # default value
        w = OptionMenu(self.window, self.sentiment_var, "Sentiment category", "Positive", "Negative")
        w.grid(column=5, row=0)


        submitt_annot_bt = tk.Button(self.window,
                        text="Submit annotations",
                        fg="blue",
                        height=2,
                        command=self.submit_annotations)
        submitt_annot_bt.grid(column=3, row=3)


        
        self.window.bind('p', self.p_key)
        self.window.bind('n', self.n_key)
        # self.window.bind('t', self.t_key)


        self.window.bind('1', self.one_key)
        self.window.bind('2', self.two_key)
        self.window.bind('3', self.three_key)
        self.window.bind('4', self.four_key)
        self.window.bind('5', self.five_key)
        self.window.bind('6', self.six_key)
        self.window.bind('7', self.seven_key)
        self.window.bind('8', self.eight_key)
        self.window.bind('9', self.nine_key)
        self.window.bind('o', self.o_key)
        self.window.bind('i', self.i_key)
        self.window.bind('h', self.h_key)
        self.window.bind('m', self.m_key)

        self.window.bind('q', self.q_key)

        self.window.bind('<Return>', self.return_bt_main_window)


        self.menubar = Menu(self.window)

        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Help", command=self.show_help)
        self.menubar.add_cascade(label="File", menu=filemenu)


        
        self.window.config(menu=self.menubar)

        self.show_comment()
        # print()
        self.window.geometry('1100x200')
        self.window.mainloop()

    def return_bt_main_window(self, event):
        self.submit_annotations()


    def submit_annotations(self):
        if self.feedback_var.get() == 'Feedback category':
            messagebox.showinfo("Error", "You need to select a feedback category before submitting your annotations")
            return
        if self.sentiment_var.get() == 'Sentiment category':
            messagebox.showinfo("Error", "You need to select a sentiment category before submitting your annotations") 
            return

        feedback_categories = []
        for feedback_var in self.list_of_feedback_var:
            feedback_categories.append(feedback_var.get())

        insert_db_record(df=self.df,
                         username=self.username,
                         current_sentence_idx=self.current_sentence_idx,
                         current_sentences=self.current_sentences,
                         comment_idx=self.comment_idx,
                         feedback_categories=feedback_categories,
                         sentiment_category=self.sentiment_var.get())
        self.next_sentence()


    def show_comment(self):

        visited_comment_ids = get_visited_comments(username=self.username)

        # check whether all comments have been annotated
        if len(visited_comment_ids) == len(self.comments):
            # if true exit application
            self.end_of_comments()


        while str(self.df.index.values[self.comment_idx]) in visited_comment_ids:
            self.comment_idx = self.comment_idx + 1


        self.current_comment = self.comments[self.comment_idx]


        try:
            self.current_comment = re.sub(r'\n+', '\n', self.current_comment).strip()
        except:
            self.comment_idx = self.comment_idx + 1
            self.show_comment()

        self.current_comment = str(self.current_comment).replace('\n', '. ')
        self.current_sentences = get_sentences(comment=self.current_comment)

    #     print(current_sentences)

        self.current_sentence_idx = 0
        self.current_sentence = self.current_sentences[self.current_sentence_idx]

        self.current_sentence_begin_character = self.current_comment.index(self.current_sentence)
        self.current_sentence_end_character = self.current_sentence_begin_character+len(self.current_sentence)

        self.text.config(state='normal')
        self.text.delete('1.0', END)
        self.text.insert("1.0", self.current_comment)




        self.highlight_sentence(begin=self.current_sentence_begin_character,
                                end=self.current_sentence_end_character)

        self.text.config(state='disabled')

        if hasattr(self, 'lbl'):
            self.lbl.destroy()

        self.lbl = Label(self.window, text="Type of response:"+str(self.df['QUESTION_PROMPT'].values[self.comment_idx]), font=("Helvetica", 15), bg="lightblue")

        if str(self.df['QUESTION_PROMPT'].values[self.comment_idx]) == 'Best things about this unit...'\
            or str(self.df['QUESTION_PROMPT'].values[self.comment_idx]) == 'Best things about my course...':
            self.sentiment_var.set("Positive")
        else:
            self.sentiment_var.set("Negative")

        self.lbl.grid(column=0, row=3)
        self.window.update()

    def load_df(self):


        self.df = pd.read_csv(csv_file, index_col=0, encoding = "ISO-8859-1")
        index = 0
        self.df = shuffle(self.df)
        self.comments = list(self.df['QUESTION_RESPONSE'])


    def p_key(self, event):
        self.sentiment_var.set("Positive")

    def n_key(self, event):
        self.sentiment_var.set("Negative")

    # def t_key(self, event):
    #     self.sentiment_var.set("Neutral")
    
    def one_key(self, event):
        self.list_of_feedback_var[-1].set("Teaching Quality and Delivery")
        # self.feedback_var.set("Teaching Quality and Delivery")
    
    def two_key(self, event):
        self.list_of_feedback_var[-1].set("Tutor Support and Engagement")

    def three_key(self, event):
        self.list_of_feedback_var[-1].set("Assessment")
    
    def four_key(self, event):
        self.list_of_feedback_var[-1].set("Feedback")
    
    def five_key(self, event):
        self.list_of_feedback_var[-1].set("Course Organisation")
    
    def six_key(self, event):
        self.list_of_feedback_var[-1].set("Learning Resources and Facilities")
    
    def seven_key(self, event):
        self.list_of_feedback_var[-1].set("Curriculm Content and Authenticity")
    
    def eight_key(self, event):
        self.list_of_feedback_var[-1].set("Placements and Work Experience")
    
    def nine_key(self, event):
        self.list_of_feedback_var[-1].set("Student life")

    def o_key(self, event):
        self.feedback_var.set("Overall Experience")
    
    def i_key(self, event):
        self.feedback_var.set("Not relevant")

    def show_help(self):
        help_app = HelpApp()

    def h_key(self, event):
        help_app = HelpApp()

    def q_key(self, event):
        messagebox.showinfo("Info", "You annotated "+str(get_num_annotated_comments(username=self.username))+" responses")

    def m_key(self, event):
        self.current_row_of_feedback_var = self.current_row_of_feedback_var + 1
        self.new_feedback_var = StringVar(self.window)
        self.new_feedback_var.set("Feedback category")  # default value
        w = OptionMenu(self.window,
                       self.new_feedback_var,
                       "Feedback category",
                       "Teaching Quality and Delivery",
                       "Tutor Support and Engagement",
                       "Assessment",
                       "Feedback",
                       "Course Organisation",
                       "Learning Resources and Facilities",
                       "Curriculm Content and Authenticity",
                       "Placements and Work Experience",
                       "Student life",
                       "Overall Experience",
                       "Not relevant")
        w.grid(column=4, row=self.current_row_of_feedback_var)
        self.list_of_feedback_var.append(self.new_feedback_var)
        self.windows_of_feedback_categories.append(w)

    def highlight_sentence(self, begin, end):
        self.clear_tags()
        self.text.tag_configure("warning", background="lightgreen", foreground="black")
        self.text.tag_raise("sel")
        self.text.tag_add("warning", "1."+str(begin), "1."+str(end))

    def clear_tags(self):
        for tag in self.text.tag_names():
            self.text.tag_delete(tag)

    def end_of_comments(self):
        # self.window.destroy()
        messagebox.showinfo("Information", "You have annotated "+str(len(self.comments))+"/"+str(len(self.comments))+" comments.\n Application will exit.")
        exit()


    def reset_dropdown_menus(self):
        self.feedback_var.set("Feedback category")

        if len(self.list_of_feedback_var) > 1:
            for window in self.windows_of_feedback_categories[1:]:
                window.destroy()

            temp_feedback_var = self.list_of_feedback_var[0]
            self.list_of_feedback_var = []
            self.list_of_feedback_var.append(temp_feedback_var)
            self.current_row_of_feedback_var = 0

        # self.sentiment_var.set("Sentiment category")

    def next_sentence(self):

        self.reset_dropdown_menus()

        if self.current_sentence_idx == len(self.current_sentences)-1:
            self.lbl.destroy()
            self.comment_idx = self.comment_idx + 1
            self.show_comment()
            return

        self.current_sentence_idx = self.current_sentence_idx + 1
        self.current_sentence = self.current_sentences[self.current_sentence_idx]

        self.current_sentence_begin_character = self.current_comment.index(self.current_sentence)
        self.current_sentence_end_character = self.current_sentence_begin_character+len(self.current_sentence)

        self.highlight_sentence(begin=self.current_sentence_begin_character, end=self.current_sentence_end_character)
        # self.text.see(str(self.current_sentence_idx+1)+'.0')

def get_sentences(comment):
    sentences = []
    for sentence in sent_tokenize(comment):
        if sentence != '.':
            sentences.append(sentence)
    return sentences

if __name__ == "__main__":
    main_app = NSSAnnotatorApp()