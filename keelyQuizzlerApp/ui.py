from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Keely's Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score:", bg=THEME_COLOR, fg="white", font=("ariel", 25, "bold"))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Filler text",
            fill=THEME_COLOR,
            font=("ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        false_image = PhotoImage(file="images/false.png")
        true_image = PhotoImage(file="images/true.png")

        self.true_button = Button(image=true_image, command=self.answer_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="Congratulations you have finished the quiz!!")
            self.score.config(text=f"Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


