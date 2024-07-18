from tkinter import *
import sympy

def Math_Calc():
  """
  This function performs mathematical calculations using sympy.
  """
  def calculate():
    equation = equation_entry.get()
    if equation.lower() == 'quit':
      window.destroy()  # Close the window if user enters 'quit'
    else:
      try:
        result = sympy.sympify(equation)
        result_label.config(text="Your answer is: " + str(result))
      except (sympy.SympifyError, TypeError) as e:
        result_label.config(text="Invalid expression. Please try again.")

  # Create the main window
  window = Tk()
  window.title("Math Calculator")

  # Label for equation input
  equation_label = Label(window, text="Enter equation:")
  equation_label.pack(padx=10, pady=5)

  # Entry field for user input
  equation_entry = Entry(window, width=30)
  equation_entry.pack(padx=10, pady=5)

  # Button to trigger calculation
  calculate_button = Button(window, text="Calculate", command=calculate)
  calculate_button.pack(padx=10, pady=5)

  # Label to display result
  result_label = Label(window, text="")
  result_label.pack(padx=10, pady=5)

  # Run the main loop
  window.mainloop()

# Call the Math_Calc function to start the calculator GUI
Math_Calc()