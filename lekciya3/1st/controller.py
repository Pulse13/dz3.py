import model_del as model
import viev

def button_click():
    value_a = viev.get_value()
    value_b = viev.get_value()
    model.init(value_a, value_b)
    result = model.delen()
    viev.view(result)

import model as model1
import viev

def button_click():
    value_a = viev.get_value()
    value_b = viev.get_value()
    model1.init(value_a, value_b)
    result = model1.sum()
    viev.view(result)


import model_mult as model2
import viev

def button_click():
    value_a = viev.get_value()
    value_b = viev.get_value()
    model2.init(value_a, value_b)
    result = model2.mult()
    viev.view(result)