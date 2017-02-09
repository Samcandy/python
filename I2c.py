import smbus

i2c = smbus.SMBus(1)  # 指定使用/dev/i2c-1
addr = 0x50           # eeprom 在 i2c bus 上的位置
reg = 0x00            # 打算要存取的暫存器位置
value = 0x64          # 等一下要寫入的值
i2c.write_byte_data(addr, reg, val)  # 寫入的動作
print i2c.read_byte_data(addr,reg)   # 把剛剛寫入的值讀出來確定一下
