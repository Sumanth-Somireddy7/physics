from math import sqrt,log10,floor,ceil,gcd
from decimal import *
import numpy as np

def get_pos_nums(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    pos_nums.reverse()
    return pos_nums

def conv(c,em,ea):
    converted_speed = 0
    converted_speed_m_s = 0
    if em=='cm/min':
        converted_speed_m_s = c*0.0001666667
        if ea=='cm/min':
            converted_speed = c
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
            
        elif ea =='ft/hr':
            converted_speed = converted_speed_m_s*11811
            
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
            
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
            
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
            
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
            
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
            
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
            
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
           
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
            
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
            
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
            
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
            
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
            
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
            
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
            
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
            
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
            
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
            
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
            
    elif em == 'cm/s':
        converted_speed_m_s = c*0.01
        if ea=='cm/s':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'ft/hr':
        converted_speed_m_s = c*8.46667e-5
        if ea=='ft/hr':
            converted_speed = c
        if ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'ft/min':
        converted_speed_m_s = c*0.00508
        if ea=='ft/min':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'ft/s':
        converted_speed_m_s = c*0.3048
        if em=='ft/s':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'in/min':
        converted_speed_m_s = c*0.000423333
        if ea=='in/min':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'in/s':
        converted_speed_m_s = c*0.0254
        if ea=='in/s':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'km/hr':
        converted_speed_m_s = c*0.277778
        if ea=='km/hr':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'km/s':
        converted_speed_m_s = c*1000
        if ea=='km/s':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'knot mi/hr':
        converted_speed_m_s = c*1.943844
        if ea=='knot mi/hr':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'knot uk':
        converted_speed_m_s = c*0.514444
        if ea=='knot uk':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'm/hr':
        converted_speed_m_s = c*0.000277778
        if ea=='m/hr':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'm/min':
        converted_speed_m_s = c*0.0166667
        if ea=='m/min':
            converted_speed=c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'm/s':
        converted_speed_m_s = c*1
        if ea=='m/s':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'mi/hr':
        converted_speed_m_s = c*0.44704
        if ea=='mi/hr':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'mi/min':
        converted_speed_m_s = c*26.8224
        if ea=='mi/min':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'mi/s':
        converted_speed_m_s = c*1609.34
        if ea=='mi/s':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'c':
        converted_speed_m_s = c*2.998e+8
        if ea=='c':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'yd/hr':
        converted_speed_m_s = c*0.000254
        if ea=='yd/hr':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'yd/min':
        converted_speed_m_s = c*0.01524
        if ea=='yd/min':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/s':
            converted_speed = converted_speed_m_s*1.09361
    elif em == 'yd/s':
        converted_speed_m_s = c*0.9144
        if ea=='yd/s':
            converted_speed = c
        elif ea =='cm/min':
            converted_speed = converted_speed_m_s*0.0001666667
        elif ea =='cm/s':
            converted_speed = converted_speed_m_s*100
        elif ea == 'ft/hr':
            converted_speed = converted_speed_m_s*11811
        elif ea == 'ft/min':
            converted_speed = converted_speed_m_s*196.85
        elif ea == 'ft/s':
            converted_speed = converted_speed_m_s*3.28084
        elif ea == 'in/min':
            converted_speed = converted_speed_m_s*2362.2
        elif ea == 'in/s':
            converted_speed = converted_speed_m_s*39.3701
        elif ea == 'km/hr':
            converted_speed = converted_speed_m_s*3.6
        elif ea == 'km/s':
            converted_speed = converted_speed_m_s*0.001
        elif ea == 'knot mi/hr':
            converted_speed = converted_speed_m_s*1.94384
        elif ea == 'knot uk':
            converted_speed = converted_speed_m_s*1.943844
        elif ea == 'm/hr':
            converted_speed = converted_speed_m_s*3600
        elif ea == 'm/min':
            converted_speed = converted_speed_m_s*60
        elif ea == 'm/s':
            converted_speed = converted_speed_m_s*1
        elif ea == 'mi/hr':
            converted_speed = converted_speed_m_s*2.23694
        elif ea == 'mi/min':
            converted_speed = converted_speed_m_s*0.0372823
        elif ea == 'mi/s':
            converted_speed = converted_speed_m_s*0.000621371
        elif ea == 'c':
            converted_speed = converted_speed_m_s*3.3356E-9
        elif ea == 'yd/hr':
            converted_speed = converted_speed_m_s*3937.01
        elif ea == 'yd/min':
            converted_speed = converted_speed_m_s*65.6168
    return [converted_speed,converted_speed_m_s]
def fricf(mu,nf):
    fr = mu*nf
    return fr
def fricm(fr,nf):
    mu = fr/nf
    return mu
def fricn(fr,mu):
    nf = fr/mu
    return nf
def fx2(x1,t2,t1,v):
    return (v*(t2-t1))+x1
def fx1(x2,t2,t1,v):
    return x2-(v*(t2-t1))
def ft2(x2,x1,t1,v):
    return ((x2-x1)/v)+t1
def ft1(x2,x1,t2,v):
    return t2-((x2-x1)/v)
def fv(x2,x1,t2,t1):
    return (x2-x1)/(t2-t1)
def hpp(d,t,f):
    return f*(d/t)
def hpd(p,t,f):
    return (p*t)/f
def hpt(p,d,f):
    return f*(d/p)
def hpf(p,d,t):
    return (p*t)/d
def imj(f,t):
    return f*t
def imf(j,t):
    return j/t
def imt(j,f):
    return j/f
def irxl(i,f):
    return 2*3.14*i*f
def iri(xl,f):
    return xl/(2*3.14*f)
def irf(xl,i):
    return xl/(2*3.14*i) 
def heatq(k,dt,d):
    return (k*dt)/d
def heatk(q,dt,d):
    return (q*d)/dt
def heatdt(q,k,d):
    return (q*d)/k
def heatd(q,k,dt):
    return (k*dt)/q
def machv(c,m):
    return m*c
def machc(v,m):
    return v/m
def machm(v,c):
    return v/c
def lcf(c,l):
    return 1/((2*3.14)*(sqrt(l*c)))
def lcc(f,l):
    return 1/(((2*3.14*f)**2)*l)
def lcl(f,c):
    return 1/(((2*3.14*f)**2)*c)

def calc(vmi,vmax,vout,il):
    r = (1000*(vmi-vout))/(il+10)
    rp = ((vmax-vout)**2)/r
    zp = (1000*((vmax-vout)/r)*vout)/1000
    zv = vout
    return [r,zv,zp,rp]
def ca(v,r):
    return (v**2)/r
def cv(a,r):
    return sqrt(a*r)
def cr(a,v):
    return (v**2)/a

def rfcr(f,c):
    return 1/((2*3.14)*f*c)
def rfcf(r,c):
    return 1/((2*3.14)*r*c)
def rfcc(r,f):
    return 1/((2*3.14)*r*f)
def kinsa(u,v,t):
    a = (v-u)/t
    s = (u*t)+(0.5*(a*(t**2)))
    return [s,a]
def kinsu(a,v,t):
    u = v-(a*t)
    s = (u*t)+(0.5*(a*(t**2)))
    return [s,u]
def kinsv(a,u,t):
    v = u+(a*t)
    s = (u*t)+(0.5*(a*(t**2)))
    return [s,v]
def kinst(a,u,v):
    t = (v-u)/a
    s = (u*t)+(0.5*(a*(t**2)))
    return [s,t]
def kinau(s,v,t):
    u = ((2*s)/t)-v
    a = (v-u)/t
    return [a,u]
def kinav(s,u,t):
    a = (2*(s-(u*t)))/t**2
    v = u+(a*t)
    return [a,v]
def kinat(s,u,v):
    a = ((v**2)-(u**2))/(2*s)
    t = (v-u)/a
    return [a,t]
def kinuv(s,a,t):
    u = (s-(0.5*(a*(t**2))))/t
    v = u+(a*t)
    return [u,v]
def kinut(s,a,v):
    u = sqrt((v**2)-(2*a*s))
    t = (v-u)/a
    return [u,t]
def kinvt(s,a,u):
    v = sqrt((u**2)+(2*a*s))
    t = (v-u)/a
    return [v,t]
def viprv(r,i,p):
    return i*r
def viprr(v,i,p):
    return v/i
def vipri(v,r,p):
    return v/r
def viprp(v,r,i):
    return (v**2)/r

def shdc(m,t1,t2,q):
    return q/(m*(t2-t1))
def shdm(c,t1,t2,q):
    return q/(c*(t2-t1))
def shdt1(c,m,t2,q):
    return t2-(q/(c*m))
def shdt2(c,m,t1,q):
    return t1 + (q/(c*m))
def shdq(c,m,t1,t2):
    return c*(m*(t2-t1))


def roundtoone(num1):
    return round(num1,1)

def roundtwo(num1):
    return round(num1,2)

def roundthree(num1):
    return round(num1,3)

def roundit(x, sig):
    return round(x, sig-int(floor(log10(abs(x))))-1)

def min_15_round(n1,n2):
    if n2 in ('00','01','02','03','04','05','06','07'):
        return n1+':'+'00'
    elif  n2 in ('08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22'):
        return n1+':'+'15'
    elif n2 in ('23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37'):
        return n1+':'+'30'
    elif n2 in ('38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52'):
        return n1+':'+'45'
    elif n2 in ('53', '54', '55', '56', '57', '58', '59', '60'):
        if n1=='23':
            return '00'+':'+'00'
        else:
            return str(int(n1)+1)+':'+'00'
    else:
        return 'No'

def roundeighth(num1):
    return ceil(num1*8)/8

def ipd(n):
    cube_root = n**(1./3.)
    if round(cube_root) ** 3 == n:
        return [round(cube_root),'is a perfect cube',True]
    else:
        return [cube_root,'is not a perfect cube',False]
    

def byte4(f1,f2,mu,to):
    st = str(f1)+str(f2)+' '+'x'+' '+str(mu)+' '+'±'+' '+str(to)
    return st
def byte5(f1,f2,f3,mu,to):
    st = str(f1)+str(f2)+str(f3)+'x'+str(mu)+'±'+str(to)
    return st

def cancel(n1,n2):
    n1 = int(n1)
    n2 = int(n2)
    div = gcd(n1,n2)
    resn = n1//div
    resd = n2//div
    return [resn,resd,div]

def feetinch(f,i):
    if i >6 and i<=12:
        f = f+1
        i = 0
        msg = "greater than 6"
        ro = "Round up the Feet"
        cas = True
    elif i==6:
        f = f+1
        i = 0
        msg = "equal to 6"
        ro = "Round up the feet"
        cas = True
    elif i<6:
        i = 0
        msg = "less than 6"
        ro = "Round down the feet"
        cas = True
    else:
        f = ''
        i = ''
        msg = ''
        ro = ''
        cas = False
    return [f,i,msg,ro,cas]

def nearfeet(num1):
    whole = round(num1)
    if num1>=1000:
        thou = round(Decimal(num1),-3)
    else:
        thou = 0
    if num1>=100:
        hund = round(Decimal(num1),-2)
    else:
        hund = 0
    if num1>=10:
        tens = round(Decimal(num1),-1)
    else:
        tens = 0
    return [whole,tens,hund,thou]

def h_3(num1):
    numstr = str(num1).split('.')
    if len(numstr[0])>=4:
        ttcas = True
        tfcas = False
        t = get_pos_nums(int(num1))
        tens = t[-3]
        getcontext().prec = 100
        res1 = round(Decimal(num1),-3)
        if tens>5:
            st = 'which is greater than 5'
            st1 = 'So round up the number'
        elif tens==5:
            st = 'which is equal to 5'
            st1 = 'So, round up the number'
        else:
            st = 'which is less than 5'
            st1 = 'So, round down the number'
    else:
        st = "We can't round to thousands because, there must be minimum of 4 digits before decimal point."
        st1 = "Here there are only "+str(len(numstr[0]))+" digits before decimal. Hence it is 0"
        tens = 0
        ttcas = False
        tfcas = True
    return [st,st1,tens,ttcas,tfcas]

def h_2(num1):
    numstr = str(num1).split('.')
    if len(numstr[0])>=3:
        htcas = True
        hfcas = False
        t = get_pos_nums(int(num1))
        tens = t[-2]
        getcontext().prec = 100
        res1 = round(Decimal(num1),-2)
        if tens>5:
            st = 'which is greater than 5'
            st1 = 'So round up the number'
        elif tens==5:
            st = 'which is equal to 5'
            st1 = 'So, round up the number'
        else:
            st = 'which is less than 5'
            st1 = 'So, round down the number'
    else:
        st = "We can't round to hundreds because, there must be minimum of 3 digits before decimal point."
        st1 = "Here there are only "+str(len(numstr[0]))+" digits before decimal. Hence it is 0"
        tens = 0
        htcas = False
        hfcas = True
    return [st,st1,tens,htcas,hfcas]

def h_1(num1):
    numstr = str(num1).split('.')
    if len(numstr[0])>=1:
        if int(numstr[0])>10:
            tetcas = True
            tefcas = False
            tens = int(numstr[0][-1])
            getcontext().prec = 100
            res1 = round(Decimal(num1),-1)
            if tens>5:
                st = 'which is greater than 5'
                st1 = 'So round up the number'
            elif tens==5:
                st = 'which is equal to 5'
                st1 = 'So, round up the number'
            else:
                st = 'which is less than 5'
                st1 = 'So, round down the number'
        else:
            tetcas = False
            tefcas = True
            st = "The number is less than 10 and can't be rounded to nearest ten. So, it is 0"
            st1 = ''
            tens = 0
    else:
        st = "We can't round to tens because, there must be minimum of 1 digit before decimal point."
        st1 = "Here there are only "+str(len(numstr[0]))+" digits before decimal. Hence it is 0"
        tens = 0
        tetcas = False
        tefcas = True
    return [st,st1,tens,tetcas,tefcas]

def m_cm(f,i):
    if i >50 and i<=100:
        f = f+1
        i = 0
        msg = "greater than 50"
        ro = "Round up the meter"
        cas = True
    elif i==50:
        f = f+1
        i = 0
        msg = "equal to 50"
        ro = "Round up the meter"
        cas = True
    elif i<50:
        i = 0
        msg = "less than 50"
        ro = "Round down the meter"
        cas = True
    else:
        f = ''
        i = ''
        msg = ''
        ro = ''
        cas = False
    return [f,i,msg,ro,cas]
def cm_mm(f,i):
    if i >5 and i<=10:
        f = f+1
        i = 0
        msg = "greater than 5"
        ro = "Round up the centimeter"
        cas = True
    elif i==5:
        f = f+1
        i = 0
        msg = "equal to 5"
        ro = "Round up the centimeter"
        cas = True
    elif i<5:
        i = 0
        msg = "less than 5"
        ro = "Round down the centimeter"
        cas = True
    else:
        f = ''
        i = ''
        msg = ''
        ro = ''
        cas = False
    return [f,i,msg,ro,cas]

def km_m(f,i):
    if i >500 and i<=1000:
        f = f+1
        i = 0
        msg = "greater than 500"
        ro = "Round up the kilometer"
        cas = True
    elif i==500:
        f = f+1
        i = 0
        msg = "equal to 500"
        ro = "Round up the kilometer"
        cas = True
    elif i<500:
        i = 0
        msg = "less than 500"
        ro = "Round down the kilometer"
        cas = True
    else:
        f = ''
        i = ''
        msg = ''
        ro = ''
        cas = False
    return [f,i,msg,ro,cas]

def mm_mi(f,i):
    if i >500 and i<=1000:
        f = f+1
        i = 0
        msg = "greater than 500"
        ro = "Round up the meter"
        cas = True
    elif i==500:
        f = f+1
        i = 0
        msg = "equal to 500"
        ro = "Round up the meter"
        cas = True
    elif i<500:
        i = 0
        msg = "less than 500"
        ro = "Round down the meter"
        cas = True
    else:
        f = ''
        i = ''
        msg = ''
        ro = ''
        cas = False
    return [f,i,msg,ro,cas]

def min_30_round(n1,n2):
    if n2 in ('00','01','02','03','04','05','06','07','08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22','23', '24', '25', '26', '27', '28', '29', '30'):
        return n1+':'+'30'
    elif n2 in ('31', '32', '33', '34', '35', '36', '37','38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52','53', '54', '55', '56', '57', '58', '59'):
        if n1=='23':
            return '00'+':'+'00'
        else:
            return str(int(n1)+1)+':'+'00'
    else:
        return 'No'