import time
from nielvis import DigitalInputOutput, Bank, DIOChannel, Button

# specify the bank A
bank_A = Bank.A
# specify the DIO channels
R1 = DIOChannel.DIO0
R2 = DIOChannel.DIO1
R3 = DIOChannel.DIO2
R4 = DIOChannel.DIO3
R5 = DIOChannel.DIO4
R6 = DIOChannel.DIO5
R7 = DIOChannel.DIO6
R8 = DIOChannel.DIO7

# specify the bank B
bank_B = Bank.B
# specify the DIO_A channels
Cg1 = DIOChannel.DIO0
Cg2 = DIOChannel.DIO1
Cg3 = DIOChannel.DIO2
Cg4 = DIOChannel.DIO3
Cg5 = DIOChannel.DIO4
Cg6 = DIOChannel.DIO5
Cg7 = DIOChannel.DIO6
Cg8 = DIOChannel.DIO7
Cr1 = DIOChannel.DIO8
Cr2 = DIOChannel.DIO9
Cr3 = DIOChannel.DIO10
Cr4 = DIOChannel.DIO11
Cr5 = DIOChannel.DIO12
Cr6 = DIOChannel.DIO13
Cr7 = DIOChannel.DIO14
Cr8 = DIOChannel.DIO15


with DigitalInputOutput(bank_A, [R1, R2, R3, R4, R5, R6, R7, R8]) as DIO_A:
	with DigitalInputOutput(bank_B,[Cg1, Cg2, Cg3, Cg4, Cg5, Cg6, Cg7, Cg8, Cr1, Cr2, Cr3, Cr4, Cr5, Cr6, Cr7, Cr8]) as DIO_B:
		while True:
			value1 = False
			value2 = True
			#初始状态：R1-R8=H	Cg1-Cg8=L
			DIO_A.write(value2, [R1, R2, R3, R4, R5, R6, R7, R8])
			DIO_B.write(value1, [Cg1, Cg2, Cg3, Cg4, Cg5, Cg6, Cg7, Cg8, Cr1, Cr2, Cr3, Cr4, Cr5, Cr6, Cr7, Cr8])

			#所有的黄灯亮
			DIO_A.write(value1, [R1, R2, R3, R4, R5, R6, R7, R8])
			DIO_B.write(value2, [Cr1, Cr2, Cr3, Cr4, Cr5, Cr6, Cr7, Cr8, Cg1, Cg2, Cg3, Cg4, Cg5, Cg6, Cg7, Cg8])
			time.sleep(1)

			#所有灯恢复初始状态
			DIO_A.write(value2, [R1, R2, R3, R4, R5, R6, R7, R8])
			DIO_B.write(value1, [Cr1, Cr2, Cr3, Cr4, Cr5, Cr6, Cr7, Cr8, Cg1, Cg2, Cg3, Cg4, Cg5, Cg6, Cg7, Cg8])
			time.sleep(1)

			#所有红灯亮
			DIO_A.write(value1, [R1, R2, R3, R4, R5, R6, R7, R8])
			DIO_B.write(value2, [Cr1, Cr2, Cr3, Cr4, Cr5, Cr6, Cr7, Cr8])
			time.sleep(10000)

			#所有灯恢复初始状态
			DIO_A.write(value2, [R1, R2, R3, R4, R5, R6, R7, R8])
			DIO_B.write(value1, [Cr1, Cr2, Cr3, Cr4, Cr5, Cr6, Cr7, Cr8])
			time.sleep(1)

			#所有绿灯亮
			DIO_A.write(value1, [R1, R2, R3, R4, R5, R6, R7, R8])
			DIO_B.write(value2, [Cg1, Cg2, Cg3, Cg4, Cg5, Cg6, Cg7, Cg8])
			time.sleep(3)

			#恢复初始状态
			DIO_A.write(value2, [R1, R2, R3, R4, R5, R6, R7, R8])
			DIO_B.write(value1, [Cg1, Cg2, Cg3, Cg4, Cg5, Cg6, Cg7, Cg8])
			time.sleep(1)

			DIO_A.write(value1, [R1])
			DIO_B.write(value2, [Cr1, Cr8])
			time.sleep(1)
			DIO_A.write(value1, [R2])
			DIO_B.write(value2, [Cr2, Cr7])
			time.sleep(1)
			DIO_A.write(value1, [R3])
			DIO_B.write(value2, [Cr3, Cr6])
			time.sleep(1)
			DIO_A.write(value1, [R4])
			DIO_B.write(value2, [Cr4, Cr5])
			time.sleep(1)
			DIO_A.write(value1, [R5])
			DIO_B.write(value2, [Cr5, Cr4])
			time.sleep(1)
			DIO_A.write(value1, [R6])
			DIO_B.write(value2, [Cr6, Cr3])
			time.sleep(1)
			DIO_A.write(value1, [R7])
			DIO_B.write(value2, [Cr7, Cr2])
			time.sleep(1)
			DIO_A.write(value1, [R8])
			DIO_B.write(value2, [Cr8, Cr1])
			time.sleep(1)

			# 恢复初始状态
			DIO_A.write(value2, [R1, R2, R3, R4, R5, R6, R7, R8])
			DIO_B.write(value1, [Cg1, Cg2, Cg3, Cg4, Cg5, Cg6, Cg7, Cg8])
			time.sleep(1)

			DIO_A.write(value1, [R1])
			DIO_B.write(value2, [Cr1, Cr8])
			time.sleep(1)
			DIO_A.write(value1, [R2])
			DIO_B.write(value2, [Cr2, Cr7])
			time.sleep(1)
			DIO_A.write(value1, [R3])
			DIO_B.write(value2, [Cr3, Cr6])
			time.sleep(1)
			DIO_A.write(value1, [R4])
			DIO_B.write(value2, [Cr4, Cr5])
			time.sleep(1)
			DIO_A.write(value1, [R5])
			DIO_B.write(value2, [Cr4, Cr5])
			time.sleep(1)
			DIO_A.write(value1, [R6])
			DIO_B.write(value2, [Cr4, Cr5])
			time.sleep(1)
			DIO_A.write(value1, [R7])
			DIO_B.write(value2, [Cr4, Cr5])
			time.sleep(1)
			DIO_A.write(value1, [R8])
			DIO_B.write(value2, [Cr4, Cr5])
			time.sleep(1)
			# 恢复初始状态
			DIO_A.write(value2, [R1, R2, R3, R4, R5, R6, R7, R8])
			DIO_B.write(value1, [Cg1, Cg2, Cg3, Cg4, Cg5, Cg6, Cg7, Cg8])
			time.sleep(1)

			DIO_A.write(value1, [R1])
			DIO_B.write(value2, [Cr1, Cr8])
			time.sleep(1)
			DIO_A.write(value1, [R2])
			DIO_B.write(value2, [Cr2, Cr7])
			time.sleep(1)
			DIO_A.write(value1, [R3])
			DIO_B.write(value2, [Cr3, Cr6])
			time.sleep(1)
			DIO_A.write(value1, [R4])
			DIO_B.write(value2, [Cr4, Cr5])
			time.sleep(1)
			DIO_A.write(value1, [R5])
			DIO_B.write(value2, [Cr5, Cr4])
			time.sleep(1)
			DIO_A.write(value1, [R6])
			DIO_B.write(value2, [Cr6, Cr3])
			time.sleep(1)
			DIO_A.write(value1, [R7])
			DIO_B.write(value2, [Cr7, Cr2])
			time.sleep(1)
			DIO_A.write(value1, [R8])
			DIO_B.write(value2, [Cr8, Cr1])
			time.sleep(1)
			#按键后退出
			with Button() as button:
				if button.read():
					break
