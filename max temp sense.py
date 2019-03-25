# Max Temperature/Humidity finder
from sense_hat import SenseHat

def find_max_temp():
    global max_temp
    print(sense.temperature)
    if sense.temperature > max_temp:
        max_temp = sense.temperature

def find_max_humid():
    global max_humid
    print(sense.humidity)
    if sense.humidity > max_humid:
        max_humid = sense.humidity

def celsius_to_farenheit(temp):
    return temp * 9/5 + 32
            
sense = SenseHat()
bg_color = [0,0,0]
measuring_color = [255,0,0]
text_color = [0,0,255]
running = True

while running:
    sense.clear(bg_color)
    max_temp = 0.0
    max_humid = 0.0
    print("Press or hold up to take measurement, down to end, right to exit.")
    event = sense.stick.wait_for_event(emptybuffer = True)
    if event.direction == 'right':
        print('Exiting...')
        running = False
        continue
    sense.clear(measuring_color)
    while event.direction != 'down':
        if event.direction == 'up' and event.action != 'released':
            find_max_temp()
            find_max_humid()
        event = sense.stick.wait_for_event()
    sense.clear(bg_color)    
    sense.show_message("Max Temp: %.2f deg F, Max Humid: %.2f" % \
        (celsius_to_farenheit(max_temp), max_humid), scroll_speed = 0.05,\
            back_colour = bg_color, text_colour = text_color)
