import json
import tkinter
from tkinter import *
import random

answers = [1,1,1,1,3,1,0,1,3,3]

user_answer = []

# load questions and answer choices from json file instead of the file
with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

# convert the dictionary in lists of questions and answers_choice
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

indexes = []
#function that randomly select 5 questions
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)

#function to show result based on the answer selected by user
def show_result(score):
    lbl_Question.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    #result image
    label_image = Label(
        root,
        bg= "white",
        border= 0,
    )
    label_image.pack(pady=(50, 30))

    #result text
    label_resultxt = Label(
        root,
        font= ("Consolas", 20),
        bg= "white",
    )
    label_resultxt.pack()

    if score >= 20:
        img = PhotoImage(file="Images/great.png")
        label_image.configure(image=img)
        label_image.image = img
        label_resultxt.configure(text="You are Excellent !!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="Images/ok.png")
        label_image.configure(image=img)
        label_image.image = img
        label_resultxt.configure(text="You can be better")
    else:
        img = PhotoImage(file="Images/bad.png")
        label_image.configure(image=img)
        label_image.image = img
        label_resultxt.configure(text="You should work hard")

#function to calculate score
def calc():
    global indexes, user_answer, answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    show_result(score)


ques = 1
#function to select a option
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

#Question
def start_quiz():

    global lbl_Question, r1, r2, r3, r4
    lbl_Question = Label(
        root,
        text=questions[indexes[0]],
        font= ("Ebrima Bold", 16),
        width= 500,
        justify= "center",
        wraplength= 400,
        bg="white",
    )
    lbl_Question.pack(pady=(100, 30))


    global radio_var
    radio_var = IntVar()
    radio_var.set(-1)

    # 4 Options button
    r1 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font= ("Ebrima Bold", 12),
        value= 0,
        variable= radio_var,
        bg="white",
        command=selected,
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Ebrima Bold", 12),
        value=1,
        variable=radio_var,
        bg="white",
        command=selected,
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Ebrima Bold", 12),
        value=2,
        variable=radio_var,
        bg="white",
        command=selected,
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Ebrima Bold", 12),
        value=3,
        variable=radio_var,
        bg="white",
        command=selected,
    )
    r4.pack(pady=5)

#Start button function
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

#Main Quiz image
img1 = PhotoImage(file="Images/main-icon-2.png")

label_img = Label(
    root,
    image= img1,
)
label_img.pack(pady=(40,0))

#Quiz Time label
label_text = Label(
    root,
    text="Quiz Time",
    font=("Comic Sans MS", 24, "bold"),
)
label_text.pack(pady=(0, 30))

#Start butto image
img2 = PhotoImage(file="Images/start-1.png")

btn_Start = Button(
    root,
    image= img2,
    relief= FLAT,
    border= 0,
    command= start_pressed,
)
btn_Start.pack(pady=(0, 10))

#instruction about quiz
lbl_Instruct = Label(
    root,
    text="Read the Rules and\n Click Start once you are ready",
    bg="white",
    font= ("Consolas", 14),
    justify= "center",
)
lbl_Instruct.pack(pady=(10, 90))

#Rules about quiz
lbl_Rules = Label(
    root,
    text="This quiz contain 5 questions\n "
         "Once you select an option that will be a final choice\n "
         "Hence, think before you select",
    width= 100,
    font= ("Times", 14),
    bg="black",
    fg="yellow",
)
lbl_Rules.pack()

root.mainloop()