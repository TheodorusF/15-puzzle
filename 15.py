from tkinter import *
import random


class YouButt:
    def __init__(self, x, y, btn=False, button=None):
        self.x = x
        self.y = y
        self.b_x = x
        self.b_y = y
        self.count = 0

    def begin(self):
        if self.x == self.b_x and self.y == self.b_y:
            return True
        return False

    def move(self, other):
        if self.x == other.x - 1 and self.y == other.y:
            self.x, other.x = other.x, self.x
            self.count += 1
            print('Right')
            return True

        if self.x == other.x + 1 and self.y == other.y:
            self.x, other.x = other.x, self.x
            self.count += 1
            print('Left')
            return True

        if self.y == other.y - 1 and self.x == other.x:
            self.y, other.y = other.y, self.y
            self.count += 1
            print('Up')
            return True

        if self.y == other.y + 1 and self.x == other.x:
            self.y, other.y = other.y, self.y
            self.count += 1
            print('Down')
            return True
        print('Wrong')
        return True


def moves(buttons):
    number = 0
    for button in buttons:
        number += button.count
    return number


def move_buttons(buttons, y, x, zero_button, main_window, scale, move_label):
    for button in buttons:
        if button.x == x and button.y == y:
            if button.move(zero_button):
                move_label['text'] = "Число ходов: " + str(moves(buttons))
            button.button.grid(row=button.y, column=button.x)
            button.button.config(
                command=lambda n_x=button.x, n_y=button.y: button_click(buttons, n_y, n_x, zero_button, main_window, scale, move_label))


def button_click(buttons, y, x, zero_button, main_window, scale, move_label):
    move_buttons(buttons, y, x, zero_button, main_window, scale, move_label)
    if this_is_end(buttons):
        end(buttons, zero_button, main_window, scale)


def this_is_end(buttons):
    for button in buttons:
        if not button.begin():
            return False
    return True


def end(buttons, zero_button, main_window, scale):
    im = PhotoImage(file=str(scale*scale - 1) + '.gif').subsample(2)
    zero_button.button = Button(main_window, image=im)
    zero_button.image = im
    zero_button.button.grid(row=2, column=2)
    zero_button.btn = True
    print(moves(buttons))

    end_window = Toplevel()
    end_window.geometry('120x100')
    lable_0 = Label(end_window, text='Число ходов: ' + str(moves(buttons)))
    lable_0.grid(row=0, column=0)

    if moves(buttons) > 31:
        lable_1 = Label(end_window, text='Можно и поменьше', font='georgia 5')
        lable_1.grid(row=1, column=0)

    lable_3 = Label(end_window, text='Время: -')
    lable_3.grid(row=2, column=0)

    exit_button = Button(end_window, text='Выход', command=main_window.quit)
    exit_button.grid(row=3, column=0)
    end_window.mainloop()


def mixer(buttons, zero_button, scale, main_window, move_label):
    for _ in range(200):
        r = random.randrange(scale)
        d = random.randrange(scale)
        move_buttons(buttons, r, d, zero_button, main_window, scale, move_label)

    for button in buttons:
        button.count = 0

    move_label['text'] = "Число ходов: 0"


def menu(menu_frame):
    text_label_2 = Label(menu_frame, text="Время: ", font='15', bg='grey')
    text_label_3 = Label(menu_frame, text='(В полной версии игры)', font='georgia 5')
    restart = Button(menu_frame, text='РЕСТАРТ')
    text_label_2.grid(row=1, column=0, padx=5)
    restart.grid(row=2, column=0, padx=5)
    text_label_3.grid(row=3, column=0, padx=5)




def game(*args):

    images = []
    for _ in args:
        images.append(_)

    scale = 3

    buttons = []
    for i in range(scale):
        for j in range(scale):
            buttons.append(YouButt(j, i, True))

    zero_button = buttons.pop()
    zero_button.btn = False

    count = 0

    main_window = Tk()
    main_window.configure(bg='Grey')
    main_window.geometry('700x533')
    main_window.title('Пятнашки v1.03')
    main_frame = Frame(main_window, bg='#f5f3ea', width=533, height=533)
    menu_frame = Frame(main_window, bg='grey', width=200, height=533)
    move_label = Label(menu_frame, text="Число ходов: " + str(0), font='15', bg='grey')
    move_label.grid(row=0, column=0, padx=5)

    for i in range(scale):
        for j in range(scale):
            if count != scale*scale-1:
                im = PhotoImage(file=str(images[count])).subsample(2)
                buttons[count].button = Button(main_frame, image=im)
                buttons[count].button.image = im
                buttons[count].button.config(
                    command=lambda y=i, x=j: button_click(buttons, y, x, zero_button, main_frame, scale, move_label))
                buttons[count].button.grid(row=i, column=j)
            count += 1

    menu(menu_frame)

    mixer(buttons, zero_button, scale, main_frame, move_label)
    main_frame.grid(row=0, column=0)
    menu_frame.grid(row=0, column=1)
    main_window.mainloop()


if __name__ == '__main__':
    game('0.gif', '1.gif', '2.gif', '3.gif', '4.gif', '5.gif', '6.gif', '7.gif', '8.gif')