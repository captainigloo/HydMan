"""
This file includes the commands and responses of Atlas Sensors
"""

##################################################################
# 		Common commands and responses for all sensors
##################################################################

resp_OK                 	= "*OK"

# commands and responses for Device information
# NOTE : at the end of response, the firmware version is attached...
cmd_get_device_info			= "I"

resp_info					= "?I"		
resp_info_EC				= "?I,EC,"		# EC
resp_info_pH				= "?I,pH,"		# pH
resp_info_ORP				= "?I,ORP,"		# ORP
resp_info_DO				= "?I,D.O.,"	# DO
resp_info_FLO				= "?I,FLO,"		# flow

# command of locking device
cmd_lock                    = "PLOCK,1"

# Query response code
cmd_enable_resp_code		= "RESPONSE,1"
cmd_disable_resp_code		= "RESPONSE,0"
cmd_get_resp_code_status	= "RESPONSE,?"

resp_resp_code_on			= "?RESPONSE,1"
resp_resp_code_off			= "?RESPONSE,0"

resp_code_unknown_cmd		= "*ER"
resp_code_overvolted		= "*OV"
resp_code_undervolted		= "*UV"
resp_code_reset				= "*RS"
resp_code_comp_boot_up		= "*RE"
resp_code_sleep				= "*SL"
resp_code_wake_up			= "*WA"

# LED
cmd_enable_LED          	= "L,1"
cmd_disable_LED         	= "L,0"
cmd_get_LED_status      	= "L,?"

resp_LED_on             	= "?L,1"
resp_LED_off            	= "?L,0"

# Continuous reading mode
cmd_enable_con_read     	= "C,1"
cmd_disable_con_read    	= "C,0"
cmd_get_con_read_status 	= "C,?"

resp_con_read_on      		= "?C,1"
resp_con_read_off     		= "?C,0"


# Status of Device
# NOTE : at the end of response, the voltage value is attached...
cmd_get_status				= "STATUS"

resp_reason					= "?STATUS"

resp_reason_power_on		= "?STATUS,P,"
resp_reason_software		= "?STATUS,S,"
resp_reason_brown_out		= "?STATUS,B,"
resp_reason_watchdog		= "?STATUS,W,"
resp_reason_unknown			= "?STATUS,U,"

# Device Identification
# NOTE : at the end of cmd/resp, device name is attached
cmd_set_device_name			= "NAME," 
cmd_get_device_name			= "NAME,?"

resp_device_name			= "?NAME"

# Factory reset
cmd_factory_rst				= "Factory"

resp_factory_rst			= "*RE"

# Low Power state
cmd_low_power				= "SLEEP"

resp_sleep					= "*SL"
resp_wake_up				= "*WA"

# I2C 
# NOTE : at the end of cmd, the I2C address is attached
cmd_goto_i2c				= "I2C,"

resp_i2c_error				= "*ER"
resp_i2c_ok					= "*RS"

# change baud rate
# NOTE : at the end of cmd, the baud rate value is attached
cmd_set_baud_rate			= "SERIAL,"

# Single reading mode
cmd_single_read				= "R"

# Temperature Compensation
# NOTE : at the end of cmd/resp, the temperature value is attached
cmd_set_temperature    	 	= "T,"
cmd_get_temperature     	= "T,?"

resp_temperature			= "?T"

# Calibration
cmd_cal_clear				= "Cal,clear"
cmd_get_cal					= "Cal,?"

resp_cal					= "?CAL"
resp_not_cal				= "?CAL,0"
resp_cal_single				= "?CAL,1"
resp_cal_dual				= "?CAL,2"
resp_cal_triple				= "?CAL,3"

##################################################################


##################################################################
# 							DO
##################################################################

# Salinity Compensation
# NOTE : at the end of cmd/resp, the salinity value is attached
cmd_set_salinity     		= "S,"
cmd_get_salinity        	= "S,?"

resp_salinity				= "?S"

# Pressure compensation
# NOTE : at the end of cmd/resp, the pressure value is attached
cmd_set_pressure			= "P,"
cmd_get_pressure			= "P,?"

resp_pressure				= "?P"

# set Saturation percentage
cmd_enable_saturation		= "O,%,1"
cmd_disable_saturation		= "O,%,0"
cmd_get_saturation_status	= "O,?"

resp_saturation_on			= "?,O,%,DO"

# Calibration
cmd_cal_atmospheric			= "Cal"
cmd_cal_0_dissolved			= "Cal,0"

##################################################################


##################################################################
# 							EC
##################################################################

# set probe type
# NOTE : at the end of cmd/resp, the K value is attached
cmd_set_probe				= "K,"
cmd_get_probe				= "K,?"

resp_probe					= "?K,"

# Removing parameters from the output string
cmd_set_enable_param_ec		= "O,EC,1"
cmd_set_disable_param_ec	= "O,EC,0"
cmd_set_enable_param_tds	= "O,TDS,1"
cmd_set_disable_param_tds	= "O,TDS,0"
cmd_set_enable_param_salinity	= "O,S,1"
cmd_set_disable_param_salinity	= "O,S,0"
cmd_set_enable_param_gravity	= "O,SG,1"
cmd_set_disable_param_gravity	= "O,SG,0"
cmd_get_param_status		= "O,?"

# Calibration
# NOTE : at the end of cmd, the value(expressed in microsiemens) is attached
cmd_cal_dry					= "Cal,dry"
cmd_cal_single_n			= "Cal,one,"
cmd_cal_dual_low_n			= "Cal,low,"
cmd_cal_dual_high_n			= "Cal,high,"

##################################################################


##################################################################
# 							pH
##################################################################

# Calibration
# NOTE : at the end of cmd, the pH value is attached
cmd_cal_low					= "Cal,low,4.00"
cmd_cal_mid					= "Cal,mid,7.00"
cmd_cal_high				= "Cal,high,10.00"

# Slope 
# NOTE : at the end of resp, the pair of pH(acid, base) is attached
cmd_get_slope				= "SLOPE,?"
resp_slope					= "?SLOPE,"


##################################################################


##################################################################
# 							ORP
##################################################################

# Calibration
# NOTE : at the end of cmd, the ORP value is attached
cmd_set_cal					= "Cal,"

##################################################################


##################################################################
# 							FLOW
# to see how to program FLOW sensor, see page 28 of datasheet carefully.
##################################################################

# Clear
cmd_clear					= "CLEAR"

# Set K-value
# NOTE : at the end of cmd/resp, the pair of K-value(volume per pulse,number of pulses) is attached
cmd_set_K_val				= "K,"
cmd_get_K_val				= "K,?"
cmd_set_K_clear				= "K,clear"

# Set time base
cmd_set_tb_sec				= "TK,S"
cmd_set_tb_min				= "TK,M"
cmd_set_tb_hour				= "TK,H"
cmd_get_tb					= "TK,?"

resp_tb_sec					= "?TK,S"
resp_tb_min					= "?TK,M"
resp_tb_hour				= "?TK,H"

# Setting the onboard resistors
# NOTE : at the end of resp, thevalue of resistor is attached
cmd_disable_resistor		= "P,0"
cmd_enable_1k_pull_up		= "P,1"
cmd_enable_1k_pull_down		= "P,-1"
cmd_enable_10k_pull_up		= "P,10"
cmd_enable_10k_pull_down	= "P,-10"
cmd_enable_100k_pull_up		= "P,100"
cmd_enable_100k_pull_down	= "P,-100"
cmd_get_resistor			= "P,?"

resp_resistor				= "?P,"

# Change the parameters from the output string
cmd_set_flow_sec			= "TO,S"
cmd_set_flow_min			= "TO,M"
cmd_set_flow_hour			= "TO,H"
cmd_get_flow				= "TO,?"

resp_flow_sec				= "?TO,S"
resp_flow_min				= "?TO,M"
resp_flow_hour				= "?TO,H"

##################################################################


