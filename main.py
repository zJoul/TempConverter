# -*-coding:utf-8 -*
import converter


def conv_help():
    for s in options:
        print options[s][0], '[', s, ']'


options = {
    1: ['Celsius to Fahrenheit', converter.celsius_to_fahrenheit],
    2: ['Fahrenheit to Celsius', converter.fahrenheit_to_celsius],
}

print '┌────────────────┐'
print '│Convert Temp :  │'
print '└────────────────┘'

conv = False
while conv not in options.keys():
    conv_help()
    try:
        conv = int(raw_input('Choose the conversion way: '))
    except ValueError:
        print 'Please enter an integer.'

try:
    temp = int(raw_input('Temperature: '))
    if not isinstance(temp, (int, float)):
        raise TypeError
    print options[conv][1](temp)
except ValueError:
    print '[VE] Not a number'
except TypeError:
    print '[TE] Not a number'
