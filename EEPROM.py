import time
from nielvis import SPI, DigitalInputOutput, Bank, DIOChannel, SPIClockPhase, SPIClockPolarity, SPIDataDirection

# specify the bank
bank = Bank.A
# specify the frequency, in Hz, of the generated clock signal
frequency = 1000000
# specify the clock phase at which the data remains stable in the SPI
# transmission cycle（trailing即在时钟上升沿信号变换，在时钟下降沿信号保持
clock_phase = SPIClockPhase.TRAILING
# specify the base level of the clock signal and the logic level of the
# leading and trailing edges
clock_polarity = SPIClockPolarity.HIGH
# specify the order in which the bits in the SPI frame are transmitted
data_direction = SPIDataDirection.  MSB
# specify the number of bits that make up one SPI transmission frame
frame_length = 8
# specify the chip select channel, the DIO channel should be low when writing
# or reading data
cs_channel = DIOChannel.DIO0
MISO_channel = DIOChannel.DIO6
wp_channel = DIOChannel.DIO1
MOSI_channel = DIOChannel.DIO7
sck_channel = DIOChannel.DIO5

# configure the chip select channel
cs = DigitalInputOutput(bank, [cs_channel])
MISO = DigitalInputOutput(bank, [MISO_channel])
MOSI = DigitalInputOutput(bank, [MOSI_channel])
sck = DigitalInputOutput(bank, [sck_channel])
with SPI(frequency,
         bank,
         clock_phase,
         clock_polarity,
         data_direction,
         frame_length) as spi:
########################################specify the bytes to write to the SPI channel####################################

    #cmod_wren: Set the write enable latch
    comd_wren = [0b00000110]
    #write commond: writing the data to address 000000000
    comd_write = [0b00000010]
    #writing address
    write_address = [0b00001000]
    #data:
    data1_write = [0b00100001]
    data2_write = [0b01000011]
    # set the chip select of SPI to low
    cs.write(False, [cs_channel])
    # set write enable latch
    spi.write(comd_wren)
    # set the chip select of SPI to high after writing to set the write enable latch
    cs.write(True, [cs_channel])
    # set the chip select of SPI to low
    cs.write(False, [cs_channel])
    #send write commond  and address
    spi.write(comd_write)
    spi.write(write_address)
    #write data
    spi.write(data1_write)
    #set the chip select of SPI to high level after writing
    cs.write(True, [cs_channel])
    # read commond:读出‘00000000’地址的数据
    comd_read = [0b00000011]
    # specify the number of frame (int) to read from the SPI channel
    number_frames = 1
    # set the chip select of SPI to low
    cs.write(False, [cs_channel])
    #send read commond
    spi.write(comd_read)
    spi.write(write_address)
    # read 16 bytes of data from SPI channel
    value_array = spi.read(number_frames)
    # set the chip select of SPI to high after reading
    cs.write(True, [cs_channel])
    # print the data
    print("value read from SPI.read: ", value_array[0])
cs.close()
