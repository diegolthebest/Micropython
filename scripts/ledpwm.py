from machine import Pin, PWM

pin = 4
pwm_pin = PWM(Pin(pin))
pwm_pin.freq(10)

percent=50

pwm_pin.duty_u16(percent*655)