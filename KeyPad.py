"""
KeyPad工作原理:先写入clumn位，将其置为低位，然后扫描该列的每一行，读出其状态，从而定位出已按下按键的位置，最后进行位置译码，输出按下按键的值
"""
import time
from nielvis import DigitalInputOutput, Bank, DIOChannel, Button

# specify the bank
bank = Bank.A
# specify the DIO channels
channel0 = DIOChannel.DIO3
channel1 = DIOChannel.DIO2
channel2 = DIOChannel.DIO1
channel3 = DIOChannel.DIO0
channel4 = DIOChannel.DIO7
channel5 = DIOChannel.DIO6
channel6 = DIOChannel.DIO5
channel7 = DIOChannel.DIO4
# configure a DIO session
with DigitalInputOutput(bank, [channel0, channel1, channel2, channel3,channel4, channel5, channel6, channel7]) as DIO:
    # define the value as a Boolean
	value = False
	#循环扫描valumn1-valumn4
	while True:
		data_out1 = 'x'
		data_out2 = ' '
		for num in range(0,4):
			data = [1,1,1,1]
			if num == 0:
				DIO.write(value, [channel0])										#valumn1置为FALSE扫描第一列
				data = DIO.read([channel4, channel5, channel6, channel7])			#将第一列写入data中，触发按键为0，未触发为1
				if data[0] == 0:
					data_out1 = '1'
				if data[1] == 0:
					data_out1 = '4'
				if data[2] == 0:
					data_out1 = '7'
				if data[3] == 0:
					data_out1 = '0'
			if num == 1:
				DIO.write(value, [channel1])										#valumn2置为FALSE扫描第一列
				data = DIO.read([channel4, channel5, channel6, channel7])			#将第二列写入data中，触发按键为0，未触发为1
				if data[0] == 0:
					data_out1 = '2'
				if data[1] == 0:
					data_out1 = '5'
				if data[2] == 0:
					data_out1 = '8'
				if data[3] == 0:
					data_out1 = 'F'
			if num == 2:
				DIO.write(value, [channel2])										#valumn3置为FALSE扫描第一列
				data = DIO.read([channel4, channel5, channel6, channel7])			#将第三列写入data中，触发按键为0，未触发为1
				if data[0] == 0:				
					data_out1 = '3'
				if data[1] == 0:
					data_out1 = '6'
				if data[2] == 0:
					data_out1 = '9'
				if data[3] == 0:
					data_out1 = 'E'
			if num == 3:
				DIO.write(value, [channel3])										#valumn4置为FALSE扫描第一列
				data = DIO.read([channel4, channel5, channel6, channel7])			#将第四列写入data中，触发按键为0，未触发为1
				if data[0] == 0:
					data_out1 = 'A'
				if data[1] == 0:
					data_out1 = 'B'
				if data[2] == 0:
					data_out1 = 'C'
				if data[3] == 0:
					data_out1 = 'D'
			data_out2 =data_out2 + data_out1
		if data_out1 != 'x':
			print(data_out2)
		with Button() as button:
			if button.read():
				break