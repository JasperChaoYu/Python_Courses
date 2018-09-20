import ast
import tkinter
import numpy
import operator

calculator_button_width = 70
calculator_button_height = 55

calculator_button_x = [calculator_button_width * i for i in range(5)]
calculator_button_y = [100 + calculator_button_height * i for i in range(6)]

signs = ['add', 'minus', 'multi', 'divide']
clears = ['AC', 'EXIT']
numbers = [str(i) for i in range(10)]

sign_operator = {
    'add': operator.add,
    'minus': operator.sub,
    'multi': operator.mul,
    'divide': operator.truediv
}

max_length = 20

window = tkinter.Tk()

def button_pressed(pressed):
    global calculator, current_number, pressed_lists, tmp_result, result_label, current_sign, pressed_sign, pressed_is
    if pressed in ['is']:
        if len(current_number) > 0 and not pressed_sign == '' :
            tmp_result = sign_operator[pressed_sign](ast.literal_eval(tmp_result),  ast.literal_eval(current_number))
        elif pressed_sign == '':
            tmp_result = current_number
        else:
            tmp_result = tmp_result
        pressed_sign = ''
        pressed_lists.clear()
        current_sign = ''
        pressed_is = True
    elif pressed in clears:
        pressed_lists.clear()
        current_sign = ''
        pressed_sign = ''
        tmp_result = '0'
    elif pressed in ['back']:
        if len(pressed_lists) > 0:
            pressed_lists.pop()
    elif pressed in signs:
        if current_sign == '':
            if tmp_result == '0' or pressed_is:
                tmp_result = current_number
                pressed_is = False
            else:
                tmp_result = sign_operator[pressed_sign](ast.literal_eval(tmp_result),  ast.literal_eval(current_number))
        current_sign = pressed
        pressed_lists.clear()
    else:
        if not current_sign == '':
            pressed_sign = current_sign
            pressed_lists.clear()
            current_sign = ''
        if pressed == '.':
            if  len(pressed_lists) > 0 and not '.' in pressed_lists:
                pressed_lists.append(pressed)
            elif len(pressed_lists) == 0:
                pressed_lists.append('0')
                pressed_lists.append(pressed)
        else:
            pressed_lists.append(pressed)  
    tmp_result = str(tmp_result)
    current_number = ''.join(pressed_lists)
    if pressed in numbers + ['back']:
        result_label_text = current_number
    else:
        result_label_text = tmp_result
    text_results = str(result_label_text).split('.')
    #print('text: %s' %text_results)
    front_text = text_results[0]
    #print('front: %s' %front_text)
    if len(front_text) > max_length:
        result_label_text = '%e' %int(front_text)
    else:
        result_label_text = front_text
    if len(text_results) > 1:
        back_text = text_results[1]
        #print('back: %s' %back_text)
        result_label_text += ('.' + back_text)            
        if len(result_label_text) > max_length:
            result_label_text = numpy.round(float(result_label_text), decimals = (max_length - len(result_label_text)))
            result_label_text = str(result_label_text)
    #print('result: %s' %result_label_text)
    result_label.config(text = result_label_text)
        
    #print('pressed: %4s\t\tnumber: %9s\t\ttmp_result: %9s\t\tcurrent_sign: %7s\t\tpressed_sign: %7s'
     #     %(pressed, current_number, tmp_result, current_sign, pressed_sign))
          
def open_calculator():
    global calculator, current_number, pressed_lists, tmp_result, result_label, current_sign, pressed_sign, pressed_is

    calculator = tkinter.Tk()
    calculator.title('Calculator')
    calculator.minsize(max(calculator_button_x), max(calculator_button_y))    

    current_number = ''
    pressed_lists = []
    tmp_result = '0'
    current_sign = ''
    pressed_sign = ''
    pressed_is = False

    result_label = tkinter.Label(calculator, text = '0', font = (100))
    result_label.place(x = 70, y = 0, width = 200, height = 100)

    calculators_button = {}

    def exit_calculator():
        calculator.destroy()

    i = 1
    calculators_button.update({str(i): tkinter.Button(calculator, text = str(i), command = lambda: button_pressed('1'))})
    x_num = ((i - 1) % 3)
    y_num = int(3 - numpy.ceil(i / 3)) + 1
    calculators_button[str(i)].place(x = calculator_button_x[x_num], 
                                               y = calculator_button_y[y_num], 
                                               width = calculator_button_width, 
                                               height = calculator_button_height)
    i = 2
    calculators_button.update({str(i): tkinter.Button(calculator, text = str(i), command = lambda: button_pressed('2'))})
    x_num = ((i - 1) % 3)
    y_num = int(3 - numpy.ceil(i / 3)) + 1
    calculators_button[str(i)].place(x = calculator_button_x[x_num], 
                                               y = calculator_button_y[y_num], 
                                               width = calculator_button_width, 
                                               height = calculator_button_height)
    i = 3
    calculators_button.update({str(i): tkinter.Button(calculator, text = str(i), command = lambda: button_pressed('3'))})
    x_num = ((i - 1) % 3)
    y_num = int(3 - numpy.ceil(i / 3)) + 1
    calculators_button[str(i)].place(x = calculator_button_x[x_num], 
                                               y = calculator_button_y[y_num], 
                                               width = calculator_button_width, 
                                               height = calculator_button_height)
    i = 4
    calculators_button.update({str(i): tkinter.Button(calculator, text = str(i), command = lambda: button_pressed('4'))})
    x_num = ((i - 1) % 3)
    y_num = int(3 - numpy.ceil(i / 3)) + 1
    calculators_button[str(i)].place(x = calculator_button_x[x_num], 
                                               y = calculator_button_y[y_num], 
                                               width = calculator_button_width, 
                                               height = calculator_button_height)
    i = 5
    calculators_button.update({str(i): tkinter.Button(calculator, text = str(i), command = lambda: button_pressed('5'))})
    x_num = ((i - 1) % 3)
    y_num = int(3 - numpy.ceil(i / 3)) + 1
    calculators_button[str(i)].place(x = calculator_button_x[x_num], 
                                               y = calculator_button_y[y_num], 
                                               width = calculator_button_width, 
                                               height = calculator_button_height)
    i = 6
    calculators_button.update({str(i): tkinter.Button(calculator, text = str(i), command = lambda: button_pressed('6'))})
    x_num = ((i - 1) % 3)
    y_num = int(3 - numpy.ceil(i / 3)) + 1
    calculators_button[str(i)].place(x = calculator_button_x[x_num], 
                                               y = calculator_button_y[y_num], 
                                               width = calculator_button_width, 
                                               height = calculator_button_height)
    i = 7
    calculators_button.update({str(i): tkinter.Button(calculator, text = str(i), command = lambda: button_pressed('7'))})
    x_num = ((i - 1) % 3)
    y_num = int(3 - numpy.ceil(i / 3)) + 1
    calculators_button[str(i)].place(x = calculator_button_x[x_num], 
                                               y = calculator_button_y[y_num], 
                                               width = calculator_button_width, 
                                               height = calculator_button_height)
    i = 8
    calculators_button.update({str(i): tkinter.Button(calculator, text = str(i), command = lambda: button_pressed('8'))})
    x_num = ((i - 1) % 3)
    y_num = int(3 - numpy.ceil(i / 3)) + 1
    calculators_button[str(i)].place(x = calculator_button_x[x_num], 
                                               y = calculator_button_y[y_num], 
                                               width = calculator_button_width, 
                                               height = calculator_button_height)
    i = 9
    calculators_button.update({str(i): tkinter.Button(calculator, text = str(i), command = lambda: button_pressed('9'))})
    x_num = ((i - 1) % 3)
    y_num = int(3 - numpy.ceil(i / 3)) + 1
    calculators_button[str(i)].place(x = calculator_button_x[x_num], 
                                               y = calculator_button_y[y_num], 
                                               width = calculator_button_width, 
                                               height = calculator_button_height)

    calculators_button.update({'0': tkinter.Button(calculator, text = '0', command = lambda: button_pressed('0'))})
    calculators_button['0'].place(x = calculator_button_x[0], 
                                            y = calculator_button_y[4], 
                                            width = calculator_button_width, 
                                            height = calculator_button_height)
    calculators_button.update({'.': tkinter.Button(calculator, text = '.', command = lambda: button_pressed('.'))})
    calculators_button['.'].place(x = calculator_button_x[1], 
                                           y = calculator_button_y[4], 
                                           width = calculator_button_width, 
                                           height = calculator_button_height)
    calculators_button.update({'is': tkinter.Button(calculator, text = '=', command = lambda: button_pressed('is'))})
    calculators_button['is'].place(x = calculator_button_x[2], 
                                             y = calculator_button_y[4], 
                                             width = calculator_button_width, 
                                             height = calculator_button_height)

    calculators_button.update({'add': tkinter.Button(calculator, text = '+', command = lambda: button_pressed('add'))})
    calculators_button['add'].place(x = calculator_button_x[3], 
                                                y = calculator_button_y[3], 
                                                width = calculator_button_width, 
                                                height = calculator_button_height)
    calculators_button.update({'minus': tkinter.Button(calculator, text = '-', command = lambda: button_pressed('minus'))})
    calculators_button['minus'].place(x = calculator_button_x[3], 
                                                   y = calculator_button_y[2], 
                                                   width = calculator_button_width, 
                                                   height = calculator_button_height)
    calculators_button.update({'multi': tkinter.Button(calculator, text = '×', command = lambda: button_pressed('multi'))})
    calculators_button['multi'].place(x = calculator_button_x[3], 
                                                 y = calculator_button_y[1], 
                                                 width = calculator_button_width, 
                                                 height = calculator_button_height)
    calculators_button.update({'divide': tkinter.Button(calculator, text = '÷', command = lambda: button_pressed('divide'))})
    calculators_button['divide'].place(x = calculator_button_x[3], 
                                                   y = calculator_button_y[0], 
                                                   width = calculator_button_width, 
                                                   height = calculator_button_height)

    calculators_button.update({'back': tkinter.Button(calculator, text = '<-', command = lambda: button_pressed('back'))})
    calculators_button['back'].place(x = calculator_button_x[2], 
                                                 y = calculator_button_y[0], 
                                                 width = calculator_button_width, 
                                                 height = calculator_button_height)
    calculators_button.update({'AC': tkinter.Button(calculator, text = 'AC', command = lambda: button_pressed('AC'))})
    calculators_button['AC'].place(x = calculator_button_x[1], 
                                              y = calculator_button_y[0], 
                                              width = calculator_button_width, 
                                              height = calculator_button_height)
    calculators_button.update({'exit': tkinter.Button(calculator, text = 'EXIT', command = lambda: exit_calculator())})
    calculators_button['exit'].place(x = calculator_button_x[0], 
                                               y = calculator_button_y[0], 
                                               width = calculator_button_width, 
                                               height = calculator_button_height)

    calculator.mainloop()
    
label = tkinter.Label(window, text = "~~Welcome to Jasper's calculator~~") 
label.pack()
button = tkinter.Button(window, text = "Starts!", command = lambda: open_calculator())
button.pack()     

window.mainloop()