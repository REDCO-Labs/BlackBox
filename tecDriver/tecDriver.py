
# << EXAMPLE from thorlabs_mtd415t repository >>


from thorlabs_mtd415t import MTD415TDevice
from time import sleep

# create a new temperature controller instance with auto save enabled
temp_controller = MTD415TDevice('/dev/ttyUSB0', auto_save=True)

# set tec current limit
temp_controller.tec_current_limit = 0.5

# set pid gains
temp_controller.p_gain = 1
temp_controller.i_gain = 0.1
temp_controller.d_gain = 0

# clear any errors
temp_controller.clear_errors()

# set temperature setpoint
temp_controller.temp_setpoint = 15.025

# check current temperature after 10s
sleep(10)
temp_controller.temp  # => 15.020

# close serial port
temp_controller.close()
temp_controller.is_open  # => False
