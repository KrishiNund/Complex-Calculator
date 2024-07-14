# used to create the gui
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import *
from tkinter import ttk

from threading import *

# to make the gui more aesthetic and modern
import customtkinter
from customtkinter import *

# used for simple and advanced mathematical operations
import math
from sympy import *

# used for converting the currencies and then extracting the result
from google_currency import convert
import re

# used to embed graphs on the tkinter window
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import sympy as sp


# ===================================================================================================================================================================================================================
class Calculator_Window():
    # defining the main properties of a calculator(mainly its physical ones)
    def __init__(self):
        # customising window's appearance
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        # creating main window and adjusting its properties
        self.window = CTk()
        self.window.title("Calculator")
        self.window.geometry(self.center_window())
        self.window.resizable(True, True)

        # creating the frames for the different calculators
        self.navigation_bar_frame = None
        self.navigation_bar()

        self.basic_calculator_frame = None
        self.basic_calculator()

        self.scientific_calculator_frame = None
        self.scientific_calculator()

        self.programmer_calculator_frame = None
        self.decimal = 0
        # self.output_label=None
        self.programmer_calculator()

        self.currency_calculator_frame = None
        self.currency_calculator()

        self.graphing_calculator_frame = None
        self.graphing_calculator()

        # toggle menu
        self.menu = None
        self.toggle_menu()
        self.toggle_menu_frame = None
        self.darkandlightmode()

        # buttons for the different calculators
        self.basic_buttons()
        self.scientific_buttons()

        # raising basic calculator as it is our default calculator
        self.basic_calculator_frame.tkraise()

    # for centering the window when it pops up
    def center_window(self):
        self.window_height = 520
        self.window_width = 350
        scr_width = self.window.winfo_screenwidth()
        scr_height = self.window.winfo_screenheight()

        x_coordinate = int((scr_width / 2) - (self.window_width / 2))
        y_coordinate = int((scr_height / 2) - (self.window_height / 2))

        return f'{self.window_width}x{self.window_height}+{x_coordinate}+{y_coordinate}'

    # __________________________________________________________creating the navigation bar and the buttons found in it__________________________________________________________________________________________________
    # ===================================================================================================================================================================================================================
    # contains the menu button and dark/light mode button
    def navigation_bar(self):
        self.navigation_bar_frame = CTkFrame(self.window, border_width=3, border_color=("lavender", "lavender"),
                                             width=self.window_width, height=30, corner_radius=5,
                                             fg_color=("#bf4040", "#000000"))
        self.navigation_bar_frame.grid(row=0, column=0)

    # switches the theme from dark to light and vice versa
    def darkandlightmode(self):
        def on():
            self.toggle_photo.configure(file=r"images/icons8-toggle-on-30.png")
            self.toggle_button.configure(command=off, background="black", bd=0, relief="flat", highlightthickness=0,
                                         activebackground="#000000", activeforeground='#000000')
            customtkinter.set_appearance_mode("dark")

        def off():
            self.toggle_photo.configure(file=r"images/icons8-toggle-off-30.png")
            self.toggle_button.configure(command=on, background="light grey", bd=0, relief="flat", highlightthickness=0,
                                         activebackground="#bf4040", activeforeground='#bf4040')
            customtkinter.set_appearance_mode("light")

        self.toggle_photo = PhotoImage(file=r"images/icons8-toggle-on-30.png")
        self.toggle_button = Button(self.window, image=self.toggle_photo, command=off, background="black", bd=0,
                                    relief="flat", highlightthickness=0, activebackground="#000000",
                                    activeforeground='#000000')
        self.toggle_button.place(x=480, y=5)

    def switch_to_scientific(self):
        self.basic_calculator_frame.lower()
        self.scientific_calculator_frame.tkraise()
        self.collapse_menu()

    def switch_to_basic(self):
        self.basic_calculator_frame.tkraise()
        self.scientific_calculator_frame.lower()
        self.collapse_menu()

    def switch_to_programmer(self):
        self.programmer_calculator_frame.tkraise()
        self.scientific_calculator_frame.lower()
        self.collapse_menu()

    def switch_to_currency(self):
        self.currency_calculator_frame.tkraise()
        self.scientific_calculator_frame.lower()
        self.collapse_menu()

    def switch_to_graphing(self):
        self.graphing_calculator_frame.tkraise()
        self.scientific_calculator_frame.lower()
        self.collapse_menu()

    # for closing the menu frame
    def collapse_menu(self):
        if self.toggle_menu_frame is not None:
            self.toggle_menu_frame.destroy()
            self.menu.configure(text="☰")
            self.menu.configure(command=self.show_menu)

    # expands to show menu frame and its options
    def show_menu(self):
        self.toggle_menu_frame = CTkFrame(self.window, height=self.window_height - 30, fg_color=("#ffe6e6", "#e6e6ff"),
                                          corner_radius=0, border_width=3)
        self.toggle_menu_frame.place(x=0, y=30)

        self.menu.configure(text='X')
        self.menu.configure(command=self.collapse_menu)

        # creating the options inside the menu
        basic_calc = CTkButton(self.toggle_menu_frame, text='Basic Calculator', fg_color=("#ff6666", "#8585ad"),
                               font=('Forte', 12, 'bold'), corner_radius=30, command=self.switch_to_basic)
        basic_calc.place(x=10, y=20)

        scientific_calc = CTkButton(self.toggle_menu_frame, text='Scientific Calculator',
                                    fg_color=("#ff6666", "#8585ad"), font=('Forte', 12, 'bold'), corner_radius=30,
                                    command=self.switch_to_scientific)
        scientific_calc.place(x=10, y=70)

        programmer_calc = CTkButton(self.toggle_menu_frame, text='Programmer Calculator',
                                    fg_color=("#ff6666", "#8585ad"), font=('Forte', 12, 'bold'), corner_radius=30,
                                    command=self.switch_to_programmer)
        programmer_calc.place(x=10, y=120)

        currency_calc = CTkButton(self.toggle_menu_frame, text='Currency Calculator', fg_color=("#ff6666", "#8585ad"),
                                  font=('Forte', 12, 'bold'), corner_radius=30, command=self.switch_to_currency)
        currency_calc.place(x=10, y=170)

        graphing_calc = CTkButton(self.toggle_menu_frame, text='Graphing Calculator', fg_color=("#ff6666", "#8585ad"),
                                  font=('Forte', 12, 'bold'), corner_radius=30, command=self.switch_to_graphing)
        graphing_calc.place(x=10, y=220)

    # This is the menu button which when clicked will display a dropdown menu
    def toggle_menu(self):

        self.menu = CTkButton(self.navigation_bar_frame, text='☰', fg_color=("#bf4040", "#000000"),
                              font=('Forte', 14, 'bold'), border_width=0, width=20, height=20, command=self.show_menu)
        self.menu.place(x=5, y=4)

    # _______________________________________________________________________creating the basic calculator,its buttons and functions_________________________________________________________________________________
    # ===================================================================================================================================================================================================================

    def basic_calculator(self):
        self.basic_calculator_frame = CTkFrame(self.window, border_width=5, width=self.window_width,
                                               height=self.window_height - 30, corner_radius=0,
                                               fg_color=("#ffe6e6", "#29293d"), border_color=("#ff9999", "#b3b3cc"))
        self.basic_calculator_frame.grid(row=1, column=0)

        # creating entry bar
        self.basic_entry_bar = CTkEntry(self.basic_calculator_frame, width=250, height=50, border_width=5,
                                        border_color='silver', corner_radius=20)
        self.basic_entry_bar.place(x=50, y=15)

    # creating buttons_functions

    # inverts the sign of a number,e.g from +ve to -ve and vice versa
    def invert(self, entry_bar):
        self.entry_bar = entry_bar
        string_num = self.entry_bar.get()
        try:
            num = float(string_num)
            if num > 0 or num < 0:
                new_num = num / -1
                self.entry_bar.delete(0, END)
                self.entry_bar.insert(0, str(new_num))
        except ValueError:
            messagebox.showerror("Error", "Invalid operation!")
            self.entry_bar.delete(0, END)

    # will insert number/symbol passed to it to the entry bar
    def click(self, number, entry_bar):
        self.entry_bar = entry_bar
        current = self.entry_bar.get()
        self.entry_bar.delete(0, END)
        self.entry_bar.insert(0, str(current) + str(number))

    # deletes contents of the entry bar
    def clear_entry(self, entry_bar):
        self.entry_bar = entry_bar
        self.entry_bar.delete(0, END)

    # evaluates arithmetic operations
    def equal(self, entry_bar):
        self.entry_bar = entry_bar
        try:
            string = self.entry_bar.get()
            string = string.replace('sin', 'math.sin')
            string = string.replace('cos', 'math.cos')
            string = string.replace('tan', 'math.tan')
            string = string.replace('sqrt', 'math.sqrt')
            string = string.replace('pi', 'math.pi')
            string = string.replace('e', 'math.exp')
            result = eval(string)
            self.entry_bar.delete(0, END)
            self.entry_bar.insert(0, result)
        except (ValueError, SyntaxError, ZeroDivisionError, NameError, AttributeError, TypeError):
            messagebox.showerror("Error", "Invalid Operation!")
            self.entry_bar.delete(0, END)

    # thread to perform calculations in a separate thread, hence speeding them up
    def equal_button_clicked(self, entry_bar):
        thread = Thread(target=lambda: self.equal(entry_bar))
        thread.start()

    def basic_buttons(self):
        #     # buttons layout
        self.modulus_button = CTkButton(self.basic_calculator_frame, text="%", fg_color=("#ff3333", "#0a0a0f"),
                                        command=lambda: self.click("%", self.basic_entry_bar), width=60)
        self.modulus_button.place(x=20, y=90)

        clear_entry_button = CTkButton(self.basic_calculator_frame, text="(", fg_color=("#ff3333", "#0a0a0f"),
                                       command=lambda: self.click("(", self.basic_entry_bar), width=60)
        clear_entry_button.place(x=100, y=90)

        clear_button = CTkButton(self.basic_calculator_frame, text=")", fg_color=("#ff3333", "#0a0a0f"),
                                 command=lambda: self.click(")", self.basic_entry_bar), width=60)
        clear_button.place(x=180, y=90)

        del_button = CTkButton(self.basic_calculator_frame, text="Del", fg_color=("#ff3333", "#0a0a0f"),
                               command=lambda: self.clear_entry(self.basic_entry_bar), width=60)
        del_button.place(x=260, y=90)

        seven_button = CTkButton(self.basic_calculator_frame, text="7", fg_color=("#ff6666", "#8585ad"),
                                 command=lambda: self.click(7, self.basic_entry_bar), width=60)
        seven_button.place(x=20, y=150)

        eight_button = CTkButton(self.basic_calculator_frame, text="8", fg_color=("#ff6666", "#8585ad"),
                                 command=lambda: self.click(8, self.basic_entry_bar), width=60)
        eight_button.place(x=100, y=150)

        nine_button = CTkButton(self.basic_calculator_frame, text="9", fg_color=("#ff6666", "#8585ad"),
                                command=lambda: self.click(9, self.basic_entry_bar), width=60)
        nine_button.place(x=180, y=150)

        divide_button = CTkButton(self.basic_calculator_frame, text="/", fg_color=("#ff6666", "#8585ad"),
                                  command=lambda: self.click("/", self.basic_entry_bar), width=60)
        divide_button.place(x=260, y=150)

        four_button = CTkButton(self.basic_calculator_frame, text="4", fg_color=("#ff6666", "#8585ad"),
                                command=lambda: self.click(4, self.basic_entry_bar), width=60)
        four_button.place(x=20, y=210)

        five_button = CTkButton(self.basic_calculator_frame, text="5", fg_color=("#ff6666", "#8585ad"),
                                command=lambda: self.click(5, self.basic_entry_bar), width=60)
        five_button.place(x=100, y=210)

        six_button = CTkButton(self.basic_calculator_frame, text="6", fg_color=("#ff6666", "#8585ad"),
                               command=lambda: self.click(6, self.basic_entry_bar), width=60)
        six_button.place(x=180, y=210)

        multiply_button = CTkButton(self.basic_calculator_frame, text="x", fg_color=("#ff6666", "#8585ad"),
                                    command=lambda: self.click("*", self.basic_entry_bar), width=60)
        multiply_button.place(x=260, y=210)

        one_button = CTkButton(self.basic_calculator_frame, text="1", fg_color=("#ff6666", "#8585ad"),
                               command=lambda: self.click(1, self.basic_entry_bar), width=60)
        one_button.place(x=20, y=270)

        two_button = CTkButton(self.basic_calculator_frame, text="2", fg_color=("#ff6666", "#8585ad"),
                               command=lambda: self.click(2, self.basic_entry_bar), width=60)
        two_button.place(x=100, y=270)

        three_button = CTkButton(self.basic_calculator_frame, text="3", fg_color=("#ff6666", "#8585ad"),
                                 command=lambda: self.click(3, self.basic_entry_bar), width=60)
        three_button.place(x=180, y=270)

        equal_button = CTkButton(self.basic_calculator_frame, text="=", font=("Arial", 35),
                                 fg_color=("#ffb3b3", "#c2c2d6"),
                                 command=lambda: self.equal_button_clicked(self.basic_entry_bar), width=60, height=150)
        equal_button.place(x=260, y=270)

        sign_invert_button = CTkButton(self.basic_calculator_frame, text="+/-", fg_color=("#ff6666", "#8585ad"),
                                       command=lambda: self.invert(self.basic_entry_bar), width=60)
        sign_invert_button.place(x=20, y=330)

        zero_button = CTkButton(self.basic_calculator_frame, text="0", fg_color=("#ff6666", "#8585ad"),
                                command=lambda: self.click(0, self.basic_entry_bar), width=60)
        zero_button.place(x=100, y=330)

        decimal_dot_button = CTkButton(self.basic_calculator_frame, text=".", fg_color=("#ff6666", "#8585ad"),
                                       command=lambda: self.click(".", self.basic_entry_bar), width=60)
        decimal_dot_button.place(x=180, y=330)

        add_button = CTkButton(self.basic_calculator_frame, text="+", fg_color=("#ff6666", "#8585ad"),
                               command=lambda: self.click('+', self.basic_entry_bar), width=60)
        add_button.place(x=20, y=390)

        subtract_button = CTkButton(self.basic_calculator_frame, text="-", fg_color=("#ff6666", "#8585ad"),
                                    command=lambda: self.click("-", self.basic_entry_bar), width=60)
        subtract_button.place(x=100, y=390)

        exponent_button = CTkButton(self.basic_calculator_frame, text="^", fg_color=("#ff6666", "#8585ad"),
                                    command=lambda: self.click("**", self.basic_entry_bar), width=60)
        exponent_button.place(x=180, y=390)

    # _______________________________________________________________________creating the scientific calculator,its buttons and functions_________________________________________________________________________________
    # ====================================================================================================================================================================================================================
    def scientific_calculator(self):
        self.scientific_calculator_frame = CTkFrame(self.window, border_width=5, width=self.window_width,
                                                    height=self.window_height - 30, corner_radius=0,
                                                    fg_color=("#ffe6e6", "#29293d"),
                                                    border_color=("#ff9999", "#b3b3cc"))
        self.scientific_calculator_frame.grid(row=1, column=0)

        self.scientific_entry_bar = CTkEntry(self.scientific_calculator_frame, width=250, height=50, border_width=5,
                                             border_color='silver', corner_radius=20)
        self.scientific_entry_bar.place(x=50, y=10)

    # converts a number to its standard form, e.g 1001=1.001 E3
    def normalize(self):
        try:
            contents = float(self.scientific_entry_bar.get())
            normalized_form = f'{contents:.5E}'
            self.scientific_entry_bar.delete(0, END)
            self.scientific_entry_bar.insert(0, str(normalized_form))
        except (ValueError, SyntaxError):
            messagebox.showerror("Error", "Invalid Operation!")
            self.scientific_entry_bar.delete(0, END)

    # converts angle in degrees to radians since by default angle are assumed to be in radians by the math module
    def deg_to_rad(self):
        try:
            angle_in_degrees = float(self.entry_bar.get())

            angle_in_radians = math.radians(angle_in_degrees)
            self.scientific_entry_bar.delete(0, END)
            self.scientific_entry_bar.insert(0, str(angle_in_radians))
        except (ValueError, SyntaxError):
            messagebox.showerror("Error", "Invalid Operation!")
            self.scientific_entry_bar.delete(0, END)

    # differentiates simple and advanced mathematical operations such as x,sin(x),2x+1
    def differentiate(self):
        try:
            x = Symbol('x')
            expression = self.scientific_entry_bar.get()
            result = diff(expression, x)
            self.scientific_entry_bar.delete(0, END)
            self.scientific_entry_bar.insert(0, str(result))
        except(ValueError, SyntaxError, TypeError, AttributeError):
            messagebox.showerror("Error", "Invalid Operation!")
            self.scientific_entry_bar.delete(0, END)

    # integrates simple and advanced mathematical operations such as x, sin(x), 2x+1
    def integrate(self):
        try:
            x = Symbol('x')
            expression = self.scientific_entry_bar.get()

            result = integrate(expression, x)
            self.scientific_entry_bar.delete(0, END)
            self.scientific_entry_bar.insert(0, str(result))
        except(ValueError, SyntaxError, TypeError, AttributeError):
            messagebox.showerror("Error", "Invalid Operation!")
            self.scientific_entry_bar.delete(0, END)

    # performs logarithmic operations such as log(5). This assumes log to be log to the base 10.
    # log of a negative number will result in an error
    def log(self):
        contents = self.scientific_entry_bar.get()
        if contents:
            try:
                number_entered = float(contents)
                if number_entered < 0:
                    self.scientific_entry_bar.delete(0, END)
                    self.scientific_entry_bar.insert(0, "Math Error")
                else:
                    result = math.log10(number_entered)
                    self.scientific_entry_bar.delete(0, END)
                    self.scientific_entry_bar.insert(0, str(result))
            except ValueError:
                messagebox.showerror("Error", "Invalid Operation!")
                self.scientific_entry_bar.delete(0, END)
        else:
            messagebox.showerror("Error", "Invalid Operation!")
            self.scientific_entry_bar.delete(0, END)

    # performs natural logarithmic operations such as ln(1)
    # ln of a negative number will result in an error
    def ln(self):
        contents = self.scientific_entry_bar.get()
        if contents:
            try:
                number_entered = float(contents)
                if number_entered < 0:
                    self.scientific_entry_bar.delete(0, END)
                    self.scientific_entry_bar.insert(0, "Math error")
                else:
                    result = ln(number_entered)
                    self.scientific_entry_bar.delete(0, END)
                    self.scientific_entry_bar.insert(0, str(result))
            except ValueError:
                messagebox.showerror("Error", "Invalid Operation!")
                self.scientific_entry_bar.delete(0, END)
        else:
            messagebox.showerror("Error", "Invalid Operation!")
            self.scientific_entry_bar.delete(0, END)

    def scientific_buttons(self):

        modulus_button = CTkButton(self.scientific_calculator_frame, text="%", fg_color=("#ff3333", "#0a0a0f"),
                                   command=lambda: self.click("%", self.scientific_entry_bar), width=60)
        modulus_button.place(x=20, y=80)

        clear_entry_button = CTkButton(self.scientific_calculator_frame, text="(", fg_color=("#ff3333", "#0a0a0f"),
                                       command=lambda: self.click("(", self.scientific_entry_bar), width=60)
        clear_entry_button.place(x=100, y=80)

        clear_button = CTkButton(self.scientific_calculator_frame, text=")", fg_color=("#ff3333", "#0a0a0f"),
                                 command=lambda: self.click(")", self.scientific_entry_bar), width=60)
        clear_button.place(x=180, y=80)

        del_button = CTkButton(self.scientific_calculator_frame, text="Del", fg_color=("#ff3333", "#0a0a0f"),
                               command=lambda: self.clear_entry(self.scientific_entry_bar), width=60)
        del_button.place(x=260, y=80)

        seven_button = CTkButton(self.scientific_calculator_frame, text="7", fg_color=("#ff6666", "#8585ad"),
                                 command=lambda: self.click(7, self.scientific_entry_bar), width=60)
        seven_button.place(x=20, y=120)

        eight_button = CTkButton(self.scientific_calculator_frame, text="8", fg_color=("#ff6666", "#8585ad"),
                                 command=lambda: self.click(8, self.scientific_entry_bar), width=60)
        eight_button.place(x=100, y=120)

        nine_button = CTkButton(self.scientific_calculator_frame, text="9", fg_color=("#ff6666", "#8585ad"),
                                command=lambda: self.click(9, self.scientific_entry_bar), width=60)
        nine_button.place(x=180, y=120)

        divide_button = CTkButton(self.scientific_calculator_frame, text="/", fg_color=("#ff6666", "#8585ad"),
                                  command=lambda: self.click("/", self.scientific_entry_bar), width=60)
        divide_button.place(x=260, y=120)

        four_button = CTkButton(self.scientific_calculator_frame, text="4", fg_color=("#ff6666", "#8585ad"),
                                command=lambda: self.click(4, self.scientific_entry_bar), width=60)
        four_button.place(x=20, y=160)

        five_button = CTkButton(self.scientific_calculator_frame, text="5", fg_color=("#ff6666", "#8585ad"),
                                command=lambda: self.click(5, self.scientific_entry_bar), width=60)
        five_button.place(x=100, y=160)

        six_button = CTkButton(self.scientific_calculator_frame, text="6", fg_color=("#ff6666", "#8585ad"),
                               command=lambda: self.click(6, self.scientific_entry_bar), width=60)
        six_button.place(x=180, y=160)

        multiply_button = CTkButton(self.scientific_calculator_frame, text="x", fg_color=("#ff6666", "#8585ad"),
                                    command=lambda: self.click("*", self.scientific_entry_bar), width=60)
        multiply_button.place(x=260, y=160)

        one_button = CTkButton(self.scientific_calculator_frame, text="1", fg_color=("#ff6666", "#8585ad"),
                               command=lambda: self.click(1, self.scientific_entry_bar), width=60)
        one_button.place(x=20, y=200)

        two_button = CTkButton(self.scientific_calculator_frame, text="2", fg_color=("#ff6666", "#8585ad"),
                               command=lambda: self.click(2, self.scientific_entry_bar), width=60)
        two_button.place(x=100, y=200)

        three_button = CTkButton(self.scientific_calculator_frame, text="3", fg_color=("#ff6666", "#8585ad"),
                                 command=lambda: self.click(3, self.scientific_entry_bar), width=60)
        three_button.place(x=180, y=200)

        logarithm_button = CTkButton(self.scientific_calculator_frame, text="log", fg_color=("#ff6666", "#8585ad"),
                                     command=self.log, width=60)
        logarithm_button.place(x=260, y=200)

        sign_invert_button = CTkButton(self.scientific_calculator_frame, text="+/-", fg_color=("#ff6666", "#8585ad"),
                                       command=lambda: self.invert(self.scientific_entry_bar), width=60)
        sign_invert_button.place(x=20, y=240)

        zero_button = CTkButton(self.scientific_calculator_frame, text="0", fg_color=("#ff6666", "#8585ad"),
                                command=lambda: self.click(0, self.scientific_entry_bar), width=60)
        zero_button.place(x=100, y=240)

        decimal_dot_button = CTkButton(self.scientific_calculator_frame, text=".", fg_color=("#ff6666", "#8585ad"),
                                       command=lambda: self.click(".", self.scientific_entry_bar), width=60)
        decimal_dot_button.place(x=180, y=240)

        square_root_button = CTkButton(self.scientific_calculator_frame, text="√", fg_color=("#ff6666", "#8585ad"),
                                       command=lambda: self.click("sqrt", self.scientific_entry_bar), width=60)
        square_root_button.place(x=260, y=240)

        add_button = CTkButton(self.scientific_calculator_frame, text="+", fg_color=("#ff6666", "#8585ad"),
                               command=lambda: self.click('+', self.scientific_entry_bar), width=60)
        add_button.place(x=20, y=280)

        subtract_button = CTkButton(self.scientific_calculator_frame, text="-", fg_color=("#ff6666", "#8585ad"),
                                    command=lambda: self.click("-", self.scientific_entry_bar), width=60)
        subtract_button.place(x=100, y=280)

        power_button = CTkButton(self.scientific_calculator_frame, text="^", fg_color=("#ff6666", "#8585ad"),
                                 command=lambda: self.click("**", self.scientific_entry_bar), width=60)
        power_button.place(x=180, y=280)

        x_button = CTkButton(self.scientific_calculator_frame, text="𝑥", font=("Arial", 20),
                             fg_color=("#ff6666", "#8585ad"),
                             command=lambda: self.click("x", self.scientific_entry_bar), width=60)
        x_button.place(x=260, y=280)

        # trigonometric expressions
        sine_button = CTkButton(self.scientific_calculator_frame, text="sin", fg_color=("#ff6666", "#8585ad"),
                                command=lambda: self.click("sin", self.scientific_entry_bar), width=60)
        sine_button.place(x=20, y=320)

        cossine_button = CTkButton(self.scientific_calculator_frame, text="cos", fg_color=("#ff6666", "#8585ad"),
                                   command=lambda: self.click("cos", self.scientific_entry_bar), width=60)
        cossine_button.place(x=100, y=320)

        tan_button = CTkButton(self.scientific_calculator_frame, text="tan", fg_color=("#ff6666", "#8585ad"),
                               command=lambda: self.click("tan", self.scientific_entry_bar), width=60)
        tan_button.place(x=180, y=320)

        equal_button = CTkButton(self.scientific_calculator_frame, text="=", font=("Arial", 35),
                                 fg_color=("#ffb3b3", "#c2c2d6"), command=lambda: self.equal(self.scientific_entry_bar),
                                 width=60, height=150)
        equal_button.place(x=260, y=320)

        pi_button = CTkButton(self.scientific_calculator_frame, text="π", fg_color=("#ff6666", "#8585ad"),
                              command=lambda: self.click("pi", self.scientific_entry_bar), width=60)
        pi_button.place(x=20, y=360)

        factorial_button = CTkButton(self.scientific_calculator_frame, text="!", fg_color=("#ff6666", "#8585ad"),
                                     command=lambda: self.click("factorial", self.scientific_entry_bar), width=60)
        factorial_button.place(x=100, y=360)

        scientific_notation_button = CTkButton(self.scientific_calculator_frame, text="E",
                                               fg_color=("#ff6666", "#8585ad"),
                                               command=lambda: self.click("E", self.scientific_entry_bar), width=60)
        scientific_notation_button.place(x=180, y=360)

        convert_to_scientific_notation_button = CTkButton(self.scientific_calculator_frame, text="N",
                                                          fg_color=("#ff6666", "#8585ad"), command=self.normalize,
                                                          width=60)
        convert_to_scientific_notation_button.place(x=20, y=400)

        radians_to_degrees_button = CTkButton(self.scientific_calculator_frame, text="°/π",
                                              fg_color=("#ff6666", "#8585ad"), command=self.deg_to_rad, width=60)
        radians_to_degrees_button.place(x=100, y=400)

        differentiation_button = CTkButton(self.scientific_calculator_frame, text="f'(x)",
                                           fg_color=("#ff6666", "#8585ad"), command=self.differentiate, width=60)
        differentiation_button.place(x=180, y=400)

        integration_button = CTkButton(self.scientific_calculator_frame, text="∫", fg_color=("#ff6666", "#8585ad"),
                                       command=self.integrate, width=60)
        integration_button.place(x=20, y=440)

        exponent_button = CTkButton(self.scientific_calculator_frame, text="e", fg_color=("#ff6666", "#8585ad"),
                                    command=lambda: self.click("e", self.scientific_entry_bar), width=60)
        exponent_button.place(x=100, y=440)

        natural_logarithm_button = CTkButton(self.scientific_calculator_frame, text="ln",
                                             fg_color=("#ff6666", "#8585ad"), command=self.ln, width=60)
        natural_logarithm_button.place(x=180, y=440)

    # _______________________________________________________________________creating the programmer calculator,its buttons and functions_________________________________________________________________________________
    # ====================================================================================================================================================================================================================
    def programmer_calculator(self):
        self.programmer_calculator_frame = CTkFrame(self.window, border_width=5, width=self.window_width,
                                                    height=self.window_height - 30, corner_radius=0,
                                                    fg_color=("#ffe6e6", "#29293d"),
                                                    border_color=("#ff9999", "#b3b3cc"))
        self.programmer_calculator_frame.grid(row=1, column=0)

        header = CTkLabel(self.programmer_calculator_frame, text='Numerical Conversion', font=('Forte', 20, 'bold'))
        header.place(x=100, y=30)

        # provides a list of common numeral systems to choose from
        num_type = ["Decimal", "Binary", "Hexadecimal", "Octal"]
        convert_from_label = CTkLabel(self.programmer_calculator_frame,
                                      text='Convert From : ',
                                      font=('Forte', 10),
                                      height=50)

        convert_from_label.place(x=10, y=60)

        # records choice of numeral system for convert_from
        self.choice1_p = StringVar(value=num_type[0])
        convert_from_combobox = CTkComboBox(self.programmer_calculator_frame,
                                            values=num_type,
                                            font=('Forte', 10),
                                            corner_radius=20,
                                            width=90,
                                            height=25,
                                            dropdown_font=('Forte', 10),
                                            variable=self.choice1_p
                                            )

        convert_from_combobox.place(x=80, y=70)

        convert_to_label = CTkLabel(self.programmer_calculator_frame, text='Convert To : ', font=('Forte', 10),
                                    height=50)
        convert_to_label.place(x=190, y=60)

        # records choice of numeral system for convert_to
        self.choice2_p = StringVar(value=num_type[0])
        convert_to_combobox = CTkComboBox(self.programmer_calculator_frame,
                                          values=num_type,
                                          corner_radius=20,
                                          font=('Forte', 10),
                                          width=90,
                                          height=25,
                                          dropdown_font=('Forte', 10),
                                          variable=self.choice2_p)

        convert_to_combobox.place(x=250, y=70)

        input_num_label = CTkLabel(self.programmer_calculator_frame,
                                   text='Enter desired amount : ',
                                   font=('Forte', 10),
                                   height=50)
        input_num_label.place(x=40, y=120)
        self.num = CTkEntry(self.programmer_calculator_frame,
                            placeholder_text="Input here...",
                            font=('Forte', 10),
                            width=150,
                            height=35,
                            border_width=2,
                            corner_radius=40)

        self.num.place(x=140, y=125)

        convert_button = CTkButton(self.programmer_calculator_frame, width=80, height=30, border_width=0,
                                   corner_radius=20, text="Convert", fg_color=("#ff6666", "#8585ad"),
                                   font=('Forte', 20, 'bold'), command=self.convert_number_thread)
        convert_button.place(x=130, y=200)

    def convert_number_thread(self):
        # Create a new thread for performing the conversion
        conversion_thread = Thread(target=self.convert_number)
        conversion_thread.start()

    def output(self, convert_from, convert_to, initial_value, converted_value):
        initial_value = initial_value.upper()
        converted_value = str(converted_value).upper()
        self.output_label = CTkLabel(self.programmer_calculator_frame,
                                     text=f'{initial_value} in {convert_from} = {converted_value} in {convert_to}',
                                     font=('Forte', 10),
                                     height=40,
                                     width=300,
                                     fg_color='gray75',
                                     text_color='black',
                                     corner_radius=25
                                     )
        self.output_label.place(x=20, y=260)

    def convert_number(self):
        convert_from_P = str(self.choice1_p.get())
        convert_to_P = str(self.choice2_p.get())
        initial_value = self.num.get()

        # if nothing is typed and convert button is pressed
        if initial_value == "":
            messagebox.showerror('Error', 'Please input a number of a hexadecimal value.')
            return

        if convert_from_P == "Hexadecimal":
            try:
                int(initial_value, 16)
            except (ValueError, TypeError):
                messagebox.showerror('Error', 'Please input proper value')

            else:
                self.decimal = int(initial_value, 16)
                if convert_to_P == "Binary":
                    binary = bin(self.decimal)
                    self.output(convert_from_P, convert_to_P, initial_value, binary[2:])
                    self.output_label.configure(width=300)

                elif convert_to_P == "Octal":
                    octal = oct(self.decimal)
                    self.output(convert_from_P, convert_to_P, initial_value, octal[2:])
                    self.output_label.configure(width=300)
                elif convert_to_P == "Decimal":
                    self.output(convert_from_P, convert_to_P, initial_value, self.decimal)
                    self.output_label.configure(width=300)
                else:
                    self.output(convert_from_P, convert_to_P, initial_value, initial_value)
                    self.output_label.configure(width=300)

        if convert_from_P == "Binary":
            try:
                int(initial_value, 2)
            except (ValueError, TypeError):
                messagebox.showerror('Error', 'Please input proper value')
            else:
                self.decimal = int(initial_value, 2)

                if convert_to_P == "Hexadecimal":
                    hexa = hex(self.decimal)
                    self.output(convert_from_P, convert_to_P, initial_value, hexa[2:])
                    self.output_label.configure(width=300)
                elif convert_to_P == "Octal":
                    octal = oct(self.decimal)
                    self.output(convert_from_P, convert_to_P, initial_value, octal[2:])
                    self.output_label.configure(width=300)
                elif convert_to_P == "Decimal":
                    self.output(convert_from_P, convert_to_P, initial_value, self.decimal)
                    self.output_label.configure(width=300)
                else:
                    self.output(convert_from_P, convert_to_P, initial_value, initial_value)
                    self.output_label.configure(width=300)

        if convert_from_P == "Octal":
            try:
                int(initial_value, 8)
            except (ValueError, TypeError):
                messagebox.showerror('Error', 'Please input proper value')
            else:
                self.decimal = int(initial_value, 8)
                if convert_to_P == "Binary":
                    binary = bin(self.decimal)
                    self.output(convert_from_P, convert_to_P, initial_value, binary[2:])
                    self.output_label.configure(width=300)
                elif convert_to_P == "Hexadecimal":
                    hexa = hex(self.decimal)
                    self.output(convert_from_P, convert_to_P, initial_value, hexa[2:])
                    self.output_label.configure(width=300)
                elif convert_to_P == "Decimal":
                    self.output(convert_from_P, convert_to_P, initial_value, self.decimal)
                    self.output_label.configure(width=300)
                else:
                    self.output(convert_from_P, convert_to_P, initial_value, initial_value)
                    self.output_label.configure(width=300)

        if convert_from_P == "Decimal":
            try:
                int(initial_value)
            except (ValueError, TypeError):
                messagebox.showerror('Error', 'Please input proper value')
            else:
                self.decimal = int(initial_value)
                if convert_to_P == "Hexadecimal":
                    hexa = hex(self.decimal)
                    self.output(convert_from_P, convert_to_P, initial_value, hexa[2:])
                    self.output_label.configure(width=300)
                elif convert_to_P == "Octal":
                    octal = oct(self.decimal)
                    self.output(convert_from_P, convert_to_P, initial_value, octal[2:])
                    self.output_label.configure(width=300)
                elif convert_to_P == "Binary":
                    binary = bin(self.decimal)
                    self.output(convert_from_P, convert_to_P, initial_value, binary[2:])
                    self.output_label.configure(width=300)
                else:
                    self.output(convert_from_P, convert_to_P, initial_value, initial_value)
                    self.output_label.configure(width=300)

    # _______________________________________________________________________creating the currency calculator,its buttons and functions_________________________________________________________________________________
    # ====================================================================================================================================================================================================================
    def currency_calculator(self):
        self.currency_calculator_frame = CTkFrame(self.window, border_width=5, width=self.window_width,
                                                  height=self.window_height - 30, corner_radius=0,
                                                  fg_color=("#ffe6e6", "#29293d"), border_color=("#ff9999", "#b3b3cc"))
        self.currency_calculator_frame.grid(row=1, column=0)

        header = CTkLabel(self.currency_calculator_frame,
                          text='Currency Exchange',
                          font=('Forte', 20, 'bold'))

        header.place(anchor=CENTER,
                     relx=.5,
                     rely=.05)

        # Currency code dictionary
        currency_code = {
            "AFN": "Afghan Afghani",
            "ALL": "Albanian Lek",
            "DZD": "Algerian Dinar",
            "AOA": "Angolan Kwanzaa",
            "ARS": "Argentine Peso",
            "AMD": "Armenian Dram",
            "AWG": "Aruba Florin",
            "AUD": "Australian Dollar",
            "AZN": "Azerbaijani Mana",
            "BSD": "Bahamian Dollar",
            "BHD": "Bahrain Dinar",
            "BBD": "Bajan dollar",
            "BDT": "Bangladeshi Take",
            "BYR": "Belarusian Ruble",
            "BYN": "Belarusian Ruble",
            "BZD": "Belize Dollar",
            "BMD": "Bermudan Dollar",
            "BTN": "Bhutan currency",
            "BTC": "Bitcoin",
            "BCH": "Bitcoin Cash",
            "BOB": "Bolivian Bolivian",
            "BAM": "Bosnia-Herzegovina Convertible Mark",
            "BWP": "Botswana Pula",
            "BRL": "Brazilian Real",
            "BND": "Brunei Dollar",
            "BGN": "Bulgarian Lev",
            "BIF": "Burundian Franc",
            "XPF": "CFP Franc",
            "KHR": "Cambodian riel",
            "CAD": "Canadian Dollar",
            "CVE": "Cape Verdana Escudo",
            "KYD": "Cayman Islands Dollar",
            "XAF": "Central African CFA franc",
            "CLP": "Chilean Peso",
            "CLF": "Chilean Unit of Account (UF)",
            "CNY": "Chinese Yuan",
            "CNH": "Chinese Yuan (offshore)",
            "COP": "Colombian Peso",
            "KMF": "Comoran franc",
            "CDF": "Congolese Franc",
            "CRC": "Costa Rican Colon",
            "HRK": "Croatian Kuna",
            "CUP": "Cuban Peso",
            "CZK": "Czech Koruna",
            "DKK": "Danish Krone",
            "DJF": "Djiboutian Franc",
            "DOP": "Dominican Peso",
            "XCD": "East Caribbean Dollar",
            "EGP": "Egyptian Pound",
            "ETH": "Ether",
            "ETB": "Ethiopian Birr",
            "EUR": "Euro",
            "FJD": "Fijian Dollar",
            "GMD": "Gambian dalasi",
            "GEL": "Georgian Lari",
            "GHC": "Ghanaian Cedi",
            "GHS": "Ghanaian Cedi",
            "GIP": "Gibraltar Pound",
            "GTQ": "Guatemalan Quetzal",
            "GNF": "Guinean Franc",
            "GYD": "Guyanaese Dollar",
            "HTG": "Haitian Gourde",
            "HNL": "Honduran Lempira",
            "HKD": "Hong Kong Dollar",
            "HUF": "Hungarian Forint",
            "ISK": "Icelandic Króna",
            "INR": "Indian Rupee",
            "IDR": "Indonesian Rupiah",
            "IRR": "Iranian Rial",
            "IQD": "Iraqi Dinar",
            "ILS": "Israeli New Shekel",
            "JMD": "Jamaican Dollar",
            "JPY": "Japanese Yen",
            "JOD": "Jordanian Dinar",
            "KZT": "Kazakhstani Tenge",
            "KES": "Kenyan Shilling",
            "KWD": "Kuwaiti Dinar",
            "KGS": "Kyrgystani Som",
            "LAK": "Laotian Kip",
            "LBP": "Lebanese pound",
            "LSL": "Lesotho loti",
            "LRD": "Liberian Dollar",
            "LYD": "Libyan Dinar",
            "LTC": "Litecoin",
            "MOP": "Macanese Pataca",
            "MKD": "Macedonian Denar",
            "MGA": "Malagasy Ariary",
            "MWK": "Malawian Kwacha",
            "MYR": "Malaysian Ringgit",
            "MVR": "Maldivian Rufiyaa",
            "MRO": "Mauritanian Ouguiya (1973–2017)",
            "MUR": "Mauritian Rupee",
            "MXN": "Mexican Peso",
            "MDL": "Moldovan Leu",
            "MAD": "Moroccan Dirham",
            "MZM": "Mozambican metical",
            "MZN": "Mozambican metical",
            "MMK": "Myanmar Kyat",
            "TWD": "New Taiwan dollar",
            "NAD": "Namibian dollar",
            "NPR": "Nepalese Rupee",
            "ANG": "Netherlands Antillean Guilder",
            "NZD": "New Zealand Dollar",
            "NIO": "Nicaraguan Córdoba",
            "NGN": "Nigerian Naira",
            "NOK": "Norwegian Krone",
            "OMR": "Omani Rial",
            "PKR": "Pakistani Rupee",
            "PAB": "Panamanian Balboa",
            "PGK": "Papua New Guinean Kina",
            "PYG": "Paraguayan Guarani",
            "PHP": "Philippine Piso",
            "PLN": "Poland złoty",
            "GBP": "Pound sterling",
            "QAR": "Qatari Rial",
            "ROL": "Romanian Leu",
            "RON": "Romanian Leu",
            "RUR": "Russian Ruble",
            "RUB": "Russian Ruble",
            "RWF": "Rwandan franc",
            "SVC": "Salvadoran Colón",
            "SAR": "Saudi Riyal",
            "CSD": "Serbian Dinar",
            "RSD": "Serbian Dinar",
            "SCR": "Seychellois Rupee",
            "SLL": "Sierra Leonean Leone",
            "SGD": "Singapore Dollar",
            "PEN": "Sol",
            "SBD": "Solomon Islands Dollar",
            "SOS": "Somali Shilling",
            "ZAR": "South African Rand",
            "KRW": "South Korean won",
            "VEF": "Sovereign Bolivar",
            "XDR": "Special Drawing Rights",
            "LKR": "Sri Lankan Rupee",
            "SSP": "Sudanese pound",
            "SDG": "Sudanese pound",
            "SRD": "Surinamese Dollar",
            "SZL": "Swazi Lilangeni",
            "SEK": "Swedish Krona",
            "CHF": "Swiss Franc",
            "TJS": "Tajikistani Somoni",
            "TZS": "Tanzanian Shilling",
            "THB": "Thai Baht",
            "TOP": "Tongan Paʻanga",
            "TTD": "Trinidad & Tobago Dollar",
            "TND": "Tunisian Dinar",
            "TRY": "Turkish lira",
            "TMM": "Turkmenistan manat",
            "TMT": "Turkmenistan manat",
            "UGX": "Ugandan Shilling",
            "UAH": "Ukrainian hryvnia",
            "AED": "United Arab Emirates Dirham",
            "USD": "United States Dollar",
            "UYU": "Uruguayan Peso",
            "UZS": "Uzbekistani Som",
            "VND": "Vietnamese dong",
            "XOF": "West African CFA franc",
            "YER": "Yemeni Rial",
            "ZMW": "Zambian Kwacha"
        }
        # Get the list of currency codes
        self.cur = list(currency_code.keys())

        # Create the "Convert From" label and combobox
        convert_from_label = CTkLabel(self.currency_calculator_frame,
                                      text='Convert From : ',
                                      font=('Forte', 10),
                                      height=50)

        convert_from_label.place(x=10, y=60)

        # records choice of initial currency
        self.choice1 = StringVar(value=self.cur[0])
        convert_from_combobox = CTkComboBox(self.currency_calculator_frame,
                                            values=self.cur,
                                            corner_radius=20,
                                            font=('Forte', 10),
                                            width=100,
                                            height=35,
                                            dropdown_font=('Forte', 10),
                                            variable=self.choice1
                                            )

        convert_from_combobox.place(x=80, y=70)

        # Create the "Convert To" label and combobox
        convert_to_label = CTkLabel(self.currency_calculator_frame,
                                    text='Convert To : ',
                                    font=('Forte', 10),
                                    height=50)
        convert_to_label.place(x=185, y=60)
        # records choice of currency we want to convert to
        self.choice2 = StringVar(value=self.cur[0])
        convert_to_combobox = CTkComboBox(self.currency_calculator_frame,
                                          values=self.cur,
                                          corner_radius=20,
                                          font=('Forte', 10),
                                          width=100,
                                          height=35,
                                          dropdown_font=('Forte', 10),
                                          variable=self.choice2)

        convert_to_combobox.place(x=240, y=70)

        # Create the "Enter desired amount" label and entry
        input_amt_label = CTkLabel(self.currency_calculator_frame,
                                   text='Enter desired amount : ',
                                   font=('Forte', 10),
                                   height=50)
        input_amt_label.place(x=20, y=120)

        self.amt = CTkEntry(self.currency_calculator_frame,
                            placeholder_text="Input here...",
                            width=200,
                            height=35,
                            border_width=2,
                            corner_radius=40)

        self.amt.place(x=125, y=125)

        # Create the "Convert" button
        convert_button = CTkButton(self.currency_calculator_frame,
                                   width=100,
                                   height=40,
                                   border_width=0,
                                   corner_radius=20,
                                   text="Convert",
                                   fg_color=("#ff6666", "#8585ad"),
                                   font=('Forte', 20, 'bold'),
                                   command=self.convert_amt)
        convert_button.place(x=125, y=200)

    def convert_amt(self):
        # Get the selected currencies and amount from the GUI
        self.convert_from = str(self.choice1.get()).lower()
        self.convert_to = str(self.choice2.get()).lower()

        try:
            float(self.amt.get())
        except ValueError:
            messagebox.showerror('Error', 'Please input an integer or a float number')
            return
        else:
            self.amount = float(self.amt.get())

        # Check if the selected currencies are valid
        if self.convert_to.upper() not in self.cur or self.convert_from.upper() not in self.cur:
            messagebox.showerror('Error', 'Please use proper Country Currency Codes')
            return

        # Create a new thread for the conversion
        conversion_thread = Thread(target=self.perform_conversion)
        conversion_thread.start()
        # Function to perform the currency conversion

    def perform_conversion(self):
        # Call the convert function from the google_currency library
        convert_str = convert(self.convert_from, self.convert_to, self.amount)
        print(convert_str)

        # Extract the converted amount using regex
        search_amt = re.search(r'"amount":\s*"([\d.]+)"', convert_str)

        try:
            search_amt.group(1)
        except AttributeError:
            # Show error message if there was an issue with the conversion
            messagebox.showerror('Error',
                                 'Due to some Network Error, the conversion has been interrupted.  \nWe apologise for any inconvenience.')
            return
        else:
            # Retrieve the converted amount from the regex match
            self.converted_output = search_amt.group(1)

        # Update the GUI with the conversion result
        self.currency_calculator_frame.after(0, self.show_output, self.amount, self.convert_from, self.converted_output,
                                             self.convert_to)

    def show_output(self, amount, convert_from, output, convert_to):
        # Create a label to display the conversion result
        show_output_label = CTkLabel(self.currency_calculator_frame,
                                text=f'{self.amount} {self.convert_from.upper()} = {self.converted_output} {self.convert_to.upper()}',
                                font=('Forte', 12),
                                height=50,
                                width=300,
                                fg_color='gray75',
                                text_color='black',
                                corner_radius=25
                                )
        show_output_label.place(x=10, y=260)

    # _______________________________________________________________________creating the graphing calculator,its buttons and functions___________________________________________________________________________________
    # ====================================================================================================================================================================================================================
    def graphing_calculator(self):
        self.graphing_calculator_frame = CTkFrame(self.window, border_width=5, width=self.window_width,
                                                  height=self.window_height - 30, corner_radius=0,
                                                  fg_color=("#ffe6e6", "#29293d"), border_color=("#ff9999", "#b3b3cc"))
        self.graphing_calculator_frame.grid(row=1, column=0)

        # Create a header label
        header = CTkLabel(self.graphing_calculator_frame, text='Graph Plotter', font=('Forte', 20, 'bold'))
        header.place(anchor=CENTER, relx=.5, rely=.05)

        # Create a label for the formula entry
        formula_label = CTkLabel(self.graphing_calculator_frame, text='Mathematical Formula:',
                                 font=('Forte', 12, 'bold'))
        formula_label.place(x=10, y=70)

        # Create an entry field for the formula
        self.formula_entry = CTkEntry(self.graphing_calculator_frame, placeholder_text="F(x) = ...", width=100)
        self.formula_entry.place(x=150, y=70)
        # Create a button to plot the graph
        plot_button = CTkButton(self.graphing_calculator_frame, text='Plot Graph', fg_color=("#ff6666", "#8585ad"),
                                command=self.plot_graph_thread, width=40, font=('Forte', 12, 'bold'))
        plot_button.place(x=260, y=70)

    # Function to plot the graph
    def plot_graph(self):
        # Get the mathematical expression from the entry field
        expression = self.formula_entry.get()
        try:
            # Create a symbol 'x' using sympy
            x = sp.symbols('x')

            # Parse the expression using simplify
            expr = sp.sympify(expression)

            # Create a lambda function from the sympy expression using numpy for numerical evaluation
            func = sp.lambdify(x, expr, modules=["numpy"])

            # Generate x and y values for plotting
            x_vals = np.linspace(-10, 10, 100)
            y_vals = func(x_vals)

            # Create a Figure object
            fig = Figure(figsize=(5, 4), dpi=100)

            # Add a subplot to the Figure
            plot = fig.add_subplot(111)

            # Plot the x and y values
            plot.plot(x_vals, y_vals)

            # Set labels and title for the plot
            plot.set_xlabel('x')
            plot.set_ylabel('y')
            plot.set_title('Graph of the Mathematical Expression')

            # Enable grid lines on the plot
            plot.grid(True)

            # Create a FigureCanvasTkAgg object and embed the figure in the Tkinter window
            canvas = FigureCanvasTkAgg(fig, self.graphing_calculator_frame)
            canvas.draw()
            canvas.get_tk_widget().place(anchor=CENTER, relx=.5, rely=.6)
        # Display an error message box if there is an exception
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def plot_graph_thread(self):
        # Create a new thread for plotting the graph
        graph_thread = Thread(target=self.plot_graph)
        graph_thread.start()

    # ====================================================================================================================================================================================================================
    # needed to run the gui
    def run(self):
        self.window.mainloop()


# creates calculator_window object
calculator = Calculator_Window()
calculator.run()
