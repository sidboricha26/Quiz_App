import tkinter
from tkinter import *
import random

questions = [
    "This is sample question 1 ?",
    "This is sample question 2 ?",
    "This is sample question 3 ?",
    "This is sample question 4 ?",
    "This is sample question 5 ?",
    "This is sample question 6 ?",
    "This is sample question 7 ?",
    "This is sample question 8 ?",
    "This is sample question 9 ?",
    "This is sample question 10 ?",
]

answers_choice = [
    ["1", "2", "3", "4",],
    ["1", "2", "3", "4",],
    ["1", "2", "3", "4",],
    ["1", "2", "3", "4",],
    ["1", "2", "3", "4",],
    ["1", "2", "3", "4",],
    ["1", "2", "3", "4",],
    ["1", "2", "3", "4",],
    ["1", "2", "3", "4",],
    ["1", "2", "3", "4",],
]

answers = [1,2,3,0,2,3,1,0,3,2]

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)

def show_result():
    lbl_Question.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()


def calc():
    global indexes, user_answer, answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer == answers[i]:
            score = score + 5
        x += 1
        show_result(score)


ques = 1
def selected():
    global radio_var, user_answer
    global lbl_Question, r1, r2, r3, r4
    global ques
    x = radio_var.get()
    user_answer.append(x)
    if ques < 5:
        lbl_Question.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()



def start_quiz():
    global  lbl_Question, r1,r2, r3, r4
    lbl_Question = Label(
        root,
        text=questions[indexes[0]],
        font= ("Consolas", 16),
        width= 500,
        justify= "center",
        wraplength= 400,
        bg="white",
    )
    lbl_Question.pack(pady=(100, 30))

    global radio_var
    radio_var = IntVar()
    radio_var.set(-1)

    r1 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font= ("Times", 12),
        value= 0,
        variable= radio_var,
        bg="white",
        command=selected,
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=radio_var,
        bg="white",
        command=selected,
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=radio_var,
        bg="white",
        command=selected,
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=radio_var,
        bg="white",
        command=selected,
    )
    r4.pack(pady=5)

def start_pressed():
    label_img.destroy()
    label_text.destroy()
    lbl_Rules.destroy()
    lbl_Instruct.destroy()
    btn_Start.destroy()
    gen()
    start_quiz()


root = tkinter.Tk()
root.title("Quiz Game")
root.geometry("700x600")
root.resizable(False, False)

img1 = PhotoImage(file="Images/main-icon-2.png")

label_img = Label(
    root,
    image= img1,
)
label_img.pack(pady=(40,0))

label_text = Label(
    root,
    text="Quiz Time",
    font=("Comic Sans MS", 24, "bold"),
)
label_text.pack(pady=(0, 30))

img2 = PhotoImage(file="Images/start-1.png")

btn_Start = Button(
    root,
    image= img2,
    relief= FLAT,
    border= 0,
    command= start_pressed,
)
btn_Start.pack(pady=(0, 10))

lbl_Instruct = Label(
    root,
    text="Read the Rules and\n Click Start once you are ready",
    bg="white",
    font= ("Consolas", 14),
    justify= "center",
)
lbl_Instruct.pack(pady=(10, 70))

lbl_Rules = Label(
    root,
    text="This quiz contain 10 questions\n "
         "You will get 20 seconds to solve a questions\n "
         "Once you select an option that will be a final choice\n "
         "Hence, think before you select",
    width= 100,
    font= ("Times", 14),
    bg="black",
    fg="yellow",
)
lbl_Rules.pack()

root.mainloop()