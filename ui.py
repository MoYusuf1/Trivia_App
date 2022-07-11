from tkinter import *
import quiz_brain
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        # window configuration
        self.window.title("Trivia")
        self.window.config(width=400, height=600, bg=THEME_COLOR)
        self.canvas = Canvas(bg="white", highlightthickness=0, width=300, height=250)

        # canvas configuration
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.false_png = PhotoImage(file="images/false.png")

        # adding a false button
        self.false_button = Button(image=self.false_png, command=self.false_pressed, highlightthickness=0, fg=THEME_COLOR,
                                   highlightbackground=THEME_COLOR)
        self.false_button.grid(row=2, column=0, pady=20)
        self.true_png = PhotoImage(file="images/true.png")

        # adding a true button
        self.true_button = Button(image=self.true_png, command=self.true_pressed,highlightthickness=0, fg=THEME_COLOR,
                                  highlightbackground=THEME_COLOR)
        self.true_button.grid(row=2, column=1, pady=20)
        self.scoreboard = Label(text="Score: 0", font=("Arial", 20, "bold"), bg=THEME_COLOR)

        # adding a scoreboard
        self.scoreboard.grid(row=0, column=1, pady=20)

        # adding the question
        self.question_text = self.canvas.create_text(150, 125, width=270, text="Question Text", fill=THEME_COLOR,
                                                     font=("Arial", 25, "bold"))
        # shows the first question
        self.get_next_question()
        # looping the window
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=f"{q_text}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've Reached The End!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
