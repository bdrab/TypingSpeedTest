import tkinter as tk
import random
import tkinter.messagebox


TEXT_TO_WRITE = "The story revolves around a girl called Little Red Riding Hood. " \
                "In Perrault's versions of the tale, she is named after her red hooded cape/cloak that she wears. " \
                "The girl walks through the woods to deliver food to her sickly grandmother " \
                "(wine and cake depending on the translation). In the Grimms' version, " \
                "her mother had ordered her to stay strictly on the path. A Big Bad Wolf wants to eat the girl " \
                "and the food in the basket. He secretly stalks her behind trees, bushes, shrubs, and patches of " \
                "little and tall grass. He approaches Little Red Riding Hood, who naively tells him where she is " \
                "going."

WORDS = ["gesture", "finished", "eternal", "pluck", "separate", "wander", "coal", "vehicle", "spit", "cage", "greeting",
         "glass", "access", "wash", "shell", "blue", "leadership", "command", "crackpot", "drop", "convince", "gene",
         "tolerant", "carry", "glance", "bear", "flash", "separation", "marble", "obese", "link", "fuss", "willpower",
         "preparation", "recycle", "emphasis", "relaxation", "painter", "functional", "pursuit", "iron", "bench",
         "reality", "girl", "solo", "tree", "ensure", "formation", "franchise", "part", "profit", "digress",
         "circulate", "brown", "sour", "distributor", "means", "index", "girlfriend", "orange", "acceptance", "heal",
         "makeup", "seminar", "coincide", "screen", "thanks", "confusion", "faint", "bay", "behave", "occupation",
         "drill", "loan", "retirement", "estate", "few", "wrong", "pie", "nationalism", "bring", "proud", "god",
         "reptile", "topple", "solid", "redundancy", "method", "artificial", "soul", "deprivation", "zero", "fail",
         "management", "heavy", "refund", "cross", "prevalence", "dimension", "safe"]


def first_mode():

    user_words = []
    selected_words = []
    words_list = []

    def start_counting():
        text_field["state"] = "normal"
        window_first_mode.after(60000, print_result)
        start_button["state"] = "disabled"
        window_first_mode.bind("<Return>", save_user_word)
        words_list.extend(WORDS)
        find_new_word()

    def print_result():
        start_button["state"] = "normal"
        text_field["state"] = "disabled"
        window_first_mode.unbind("<Return>")
        correct_word = 0
        for word in user_words:
            if word in selected_words:
                correct_word += 1

        if tkinter.messagebox.askyesno(title="Congratulations!", message=f"Your score: {correct_word} words/minute. "
                                                                         f"\n Would you like to play again?"):
            start_counting()
        else:
            window_first_mode.destroy()

    def save_user_word(key_pressed):
        user_words.append(text_field.get("1.0", "end").replace("\n", ""))
        text_field.delete('1.0', "end")
        find_new_word()

    def find_new_word():
        word = random.choice(words_list)
        words_list.remove(word)
        selected_words.append(word)
        text_label.config(text=word)

    window_first_mode = tk.Toplevel()
    window_first_mode.geometry("370x150")
    window_first_mode.resizable(height=False, width=False)

    text_label = tk.Label(window_first_mode,
                          text="Click 'START' to start test and press 'ENTER' after every word.",
                          wraplength=window_first_mode.winfo_y())
    text_label.grid(row=0, column=0, columnspan=2)

    start_button = tk.Button(window_first_mode,
                             text="Start",
                             width=20,
                             command=start_counting,
                             font=("Helvetica bold", 13))
    start_button.grid(row=1, column=0)

    exit_button_popup = tk.Button(window_first_mode,
                                  text="EXIT",
                                  width=20,
                                  command=window_first_mode.destroy,
                                  font=("Helvetica bold", 13))
    exit_button_popup.grid(row=1, column=1)

    text_field = tk.Text(window_first_mode, height=5, width=31)
    text_field.grid(row=2, column=0, columnspan=2, pady=10)
    text_field["state"] = "disabled"
    window_first_mode.grab_set()


def second_mode():
    def start_counting():
        text_field["state"] = "normal"
        window_second_mode.after(60000, print_result)
        start_button["state"] = "disabled"

    def print_result():
        correct_word = 0
        index = 0

        user_input = text_field.get("1.0", "end").replace("\n", "")
        text_to_check = TEXT_TO_WRITE.split(" ")
        user_input_words = user_input.split(" ")
        user_input_words = [word for word in user_input_words if word != ""]
        for count, word in enumerate(user_input_words):
            if word == text_to_check[index]:
                correct_word += 1
                index += 1
            elif word == text_to_check[index + 1]:
                correct_word += 1
                index += 2
            elif word == text_to_check[index - 1]:
                correct_word += 1
                index -= 1
            elif word == text_to_check[index + 2]:
                correct_word += 1
                index += 3
            elif word == text_to_check[index - 2]:
                correct_word += 1
                index -= 2
            else:
                index += 1

        if tkinter.messagebox.askyesno(title="Congratulations!", message=f"Your score: {correct_word} points. "
                                                                         f"\n Would you like to play again?"):
            start_counting()
        else:
            window_second_mode.destroy()
        start_button["state"] = "normal"
        text_field["state"] = "disabled"

    window_second_mode = tk.Toplevel()
    window_second_mode.geometry("500x500")
    window_second_mode.resizable(height=False, width=False)
    text_label = tk.Label(window_second_mode, text=TEXT_TO_WRITE, font=("Helvetica bold", 13), wraplength=500)
    text_label.grid(row=0, column=0, columnspan=2)

    start_button = tk.Button(window_second_mode, text="Start", width=20, command=start_counting)
    start_button.grid(row=1, column=0)

    exit_button_popup = tk.Button(window_second_mode, text="EXIT", width=20, command=window_second_mode.destroy)
    exit_button_popup.grid(row=1, column=1)

    text_field = tk.Text(window_second_mode, height=5, width=62)
    text_field.grid(row=2, column=0, columnspan=2)
    text_field["state"] = "disabled"
    window_second_mode.grab_set()


window = tk.Tk()
window.title("TSTest")
window.geometry("220x80")
window.resizable(height=False, width=False)
window.update()


first_mode_label = tk.Label(text="First mode / type words", wraplength=window.winfo_width())
first_mode_label.grid(row=1, column=0)
first_mode_button = tk.Button(text="START", command=first_mode)
first_mode_button.grid(row=1, column=1)

second_mode_label = tk.Label(text="Second mode / type sentences", wraplength=window.winfo_width())
second_mode_label.grid(row=2, column=0)
second_mode_button = tk.Button(text="START", command=second_mode)
second_mode_button.grid(row=2, column=1)


exit_button = tk.Button(text="EXIT", command=window.destroy)
exit_button.grid(row=4, column=0, columnspan=2)

tk.mainloop()
