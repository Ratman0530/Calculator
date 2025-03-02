import tkinter as tk  # It helps you design the frontend/GUI

class Calculator:  # We make a class called Calculator
    def __init__(self): 
        self.window = tk.Tk()  # Initialize the screen of the App
        self.window.geometry("320x500")  # 320 is width, 500 is height
        self.window.resizable(0, 0)  # Disable window resizing
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()  # Define display frame first
        self.total_label, self.label = self.create_display_labels()  # Now create labels

        self.buttons_frame = self.create_buttons_frame()  # Define buttons frame

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), ".": (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)


        self.create_digit_buttons() # calling the function where we made the buttons
        self.create_operation_buttons()
        self.create_special_buttons()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                               bg="#222222", fg="#636363", padx=24, font=("Arial", 16))
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                         bg="#222222", fg="#636363", padx=24, font=("Arial", 20))
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=250, bg="#222222")  # Define frame correctly
        frame.pack(expand=True, fill="both")  # Pack to make it visible
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.total_expression += str(value)
        self.update_total_label()
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="#222222", fg="#636363", font=("Arial", 15), borderwidth=1, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

        return button

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += operator
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operation_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="#222222", fg="#636363", font=("Arial", 15), borderwidth=1, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

        return button

    def clear(self):
        self.current_expression = "0"
        self.total_expression = "0"
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg="#222222", fg="#636363", font=("Arial", 15), borderwidth=1, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

        return button

    def evaluate(self):
        try:
            self.current_expression = str(eval(self.total_expression))
        except Exception:
            self.current_expression = "Error"
        finally:
            self.update_total_label()
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="#222222", fg="#636363", font=("Arial", 15), borderwidth=1, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

        return button

    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        self.update_label()

    def create_backspace_button(self):
        button = tk.Button(self.buttons_frame, text="⌫", bg="#222222", fg="#636363", font=("Arial", 15), borderwidth=1, command=self.backspace)
        button.grid(row=0, column=2, sticky=tk.NSEW)

        return button
    
    def square(self):
        self.current_expression = str(eval(f"({self.current_expression})**2"))
        self.update_label()

    def create_power_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00B2", bg="#222222", fg="#636363", font=("Arial", 15), borderwidth=1, command=self.square)
        button.grid(row=0, column=3, sticky=tk.NSEW)

        return button

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_backspace_button()
        self.create_power_button()


    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame


    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')  # The f is a string formatting operator

        self.total_label.config(text=expression)      
        

    def update_label(self):
        self.label.config(text=self.current_expression)


    def run(self):
        self.window.mainloop()  # This will run your app

# Create an instance of the Calculator class and run it
calc = Calculator()
calc.run()
