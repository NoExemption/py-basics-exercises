import pyserial

try:
    ser = serial.Serial('COM6', 9600)  # 根据实际情况修改波特率
    if ser.is_open:
        print("串口已打开")
        ser.write(b"your_command\n")  # 将"your_command"替换为机械臂的实际指令
        response = ser.readlines()
        for line in response:
            print(line.decode('utf - 8').strip())
        ser.close()
    else:
        print("串口未打开")
except serial.SerialException as e:
    print(f"串口错误: {e}")