# Program Name: GUI_mortgage.py
# Program Description:
#   This is the Eight lab
#
#   In this program I have written code which makes a GUI for the mortgage calculator
# @Author: Akshay Rajendran
# @Date: 7/30/22

import tkinter as tk
import turtle
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Mortgage Calculator")

        self.main_window.geometry("400x200")
        self.main_window.resizable(0,0)

        self.main_window_color = "#ADD8E6"
        self.main_window.config(bg = self.main_window_color)

        self.top_frame = tk.Frame()
        self.top_mid_frame = tk.Frame()
        self.top_mid_mid_frame = tk.Frame()
        self.mid_frame = tk.Frame()
        self.mid_bottom_frame = tk.Frame()
        self.bottom_frame = tk.Frame()
        self.bottom_bottom_frame = tk.Frame()

        self.prompt_label = tk.Label(self.top_frame, text = "loan amount")
        self.loan_entry = tk.Entry(self.top_frame, width = 10)

        self.prompt_label.pack(side = 'left')
        self.loan_entry.pack(side = 'left')

        self.promp_label = tk.Label(self.top_mid_frame, text = "interest")
        self.interest_entry = tk.Entry(self.top_mid_frame, width = 10)

        self.promp_label.pack(side='left')
        self.interest_entry.pack(side='left')

        self.prom_label = tk.Label(self.top_mid_mid_frame, text = "loan term (years)")
        self.loan_term_entry = tk.Entry(self.top_mid_mid_frame, width = 10)

        self.prom_label.pack(side='left')
        self.loan_term_entry.pack(side='left')

        self.descr_label = tk.Label(self.mid_frame, text = "monthly payment")
        self.value = tk.StringVar()

        self.miles_lable = tk.Label(self.mid_frame, textvariable = self.value)

        self.descr_label.pack(side = "left")
        self.miles_lable.pack(side = "left")

        self.cheese_label = tk.Label(self.mid_bottom_frame, text = "Total payment")
        self.chose = tk.StringVar()

        self.why_label = tk.Label(self.mid_bottom_frame, textvariable = self.chose)

        self.cheese_label.pack(side = "left")
        self.why_label.pack(side = "left")

        self.calc_button = tk.Button(self.bottom_frame,
                                     text = "Calculate",
                                     command = self.Calculate)
        self.quit_button = tk.Button(self.bottom_frame,
                                     text = "Quit",
                                     command = self.main_window.destroy)
        self.chart_button = tk.Button(self.bottom_frame,
                                      text = "chart",
                                      command = self.img)

        self.calc_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        self.chart_button.pack(side = "left")

        self.pro_label = tk.Label(self.bottom_bottom_frame, text = "Akshay Rajendran - CNET 142, 2022-07-30 22:31:30.192038")

        self.pro_label.pack()

        self.top_frame.pack()
        self.top_mid_frame.pack()
        self.top_mid_mid_frame.pack()
        self.mid_frame.pack()
        self.mid_bottom_frame.pack()
        self.bottom_frame.pack()
        self.bottom_bottom_frame.pack()
        tk.mainloop()

    def Calculate(self):
        if float(self.loan_entry.get()) < 0:
            tk.messagebox.showinfo("Must be a positive number > 0")
        else:
            loan = (float(self.interest_entry.get()) / 100)/12
            num_payments = (float(self.loan_term_entry.get())) * 12
            calculate = float(self.loan_entry.get()) * loan * pow((1 + loan), num_payments)/(pow((1 + loan), num_payments)-1)
            more_math = num_payments * calculate
            self.value.set(round(calculate, 2))
            self.chose.set(round(more_math, 2))

    def img(self):
        screen = turtle.getscreen()
        screen.bgcolor("white")
        screen.bgpic("Historical mortgage rate .png")

if __name__ == '__main__':
    my_gui = MyGUI()
