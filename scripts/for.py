from include.rcc_library import Raft
import utime

myraft=Raft()

for i in range(3):
    myraft.led_on()
    utime.sleep_ms(500)
    myraft.led_off()
    utime.sleep_ms(500)
    myraft.led_on()
    utime.sleep_ms(2000)
    myraft.led_off()
    utime.sleep_ms(500)

