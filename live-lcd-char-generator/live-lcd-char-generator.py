import serial
import sys
import tkinter as tk

def serialPorts():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
    
def connectCOM(serial, port, baud):
  print("Connecting port " + port + " with baud rate " + str(baud))
  serial.baudrate = baud
  serial.port = port
  serial.open()
  serial.timeout = 1
  print("OK")
  
def disconnectCOM(serial, port):
  print("Disconnecting port " + port)
  serial.close()
  print("OK")
    
def buttonCallback(serial, b, x, y, output):
  if b.value == 0:
    b.configure(bg="green2")
    b.value = 1
  elif b.value == 1:
    b.configure(bg="dark green")
    b.value = 0
  updateOutput(buttons, output)
  sendOutput(serial, buttons)
    
def clear(serial, buttons, output):
  for row in buttons:
    for b in row:
      b.value = 0
      b.configure(bg="dark green")
  updateOutput(buttons, output)
  sendOutput(serial, buttons)

def fill(serial, buttons, output):
  for row in buttons:
    for b in row:
      b.value = 1
      b.configure(bg="green2")
  updateOutput(buttons, output)
  sendOutput(serial, buttons)
      
def invert(serial, buttons, output):
  for row in buttons:
    for b in row:
      if b.value == 0:  
        b.value = 1
        b.configure(bg="green2")
      elif b.value == 1:  
        b.value = 0
        b.configure(bg="dark green")
  updateOutput(buttons, output)
  sendOutput(serial, buttons)
    
def updateOutput(buttons, output):
  output.configure(state='normal')
  output.delete("1.0", tk.END)
  output.insert(tk.END, "uint8_t ch[] = {\n")
  for row in buttons:
    num = ""
    for d in row:
      num += str(d.value)
    output.insert(tk.END, "   " + str(hex(int(num, 2))) + ",\n")
  output.insert(tk.END, "};")
  output.configure(state='disabled')
  
def sendOutput(serial, buttons):
  output = "SYMBOL "
  for row in buttons:
    num = ""
    for d in row:
      num += str(d.value)
    output += str(int(num, 2)) + " "
  output += "0 \n"
  serial.write(bytes(output, "utf-8"))
  serial.write(bytes("HOME\n", "utf-8"))
  serial.write(bytes("CURSOR 10 2\n", "utf-8"))
  serial.write(bytes("PRINTB 0\n", "utf-8"))
  
  
    
if __name__ == '__main__':
  print("\nHello!\n")
  ports = serialPorts()
  print("Available Serial Ports: " + str(ports))
  port = input("Type name of your Arduino board port: ")
  while port not in ports:
    port = input("Type valid port name: ")
  
  serial = serial.Serial()
  connectCOM(serial, port, 9600)
  
  width, height = 5, 8
  
  root = tk.Tk()
  root.title('Live LCD Char Generator')
  root.resizable(False, False)
  root.grid_columnconfigure(width, minsize=5)
  
  tk.Label(root, text="Port: " + str(port) + ", Symbol: " + str(width) + "x" + str(height)).grid(row=0, column=0, columnspan=100)
  
  output = tk.Text(root, width=16, height=height+2)
  output.grid(row=4, column=width + 1, rowspan=100, columnspan=5)
  
  pixel = tk.PhotoImage(width=1, height=1)
  buttons = []
  
  for y in range(height):
    rows = []
    for x in range(width):
      b = tk.Button(root, image=pixel, width=30, height=30, padx=0, pady=0, bg="dark green")
      b.configure( command=lambda x=x, y=y, b=b: buttonCallback(serial, b, x, y, output))
      b.value = 0
      b.grid(column=x, row=y + 1)
     
      rows.append(b)
    buttons.append(rows)
  
  tk.Button(root, width=9, height=1, padx=10, pady=0, text="Clear", command=lambda: clear(serial, buttons, output)).grid(row=1, column=width + 1)
  tk.Button(root, width=9, height=1, padx=10, pady=0, text="Fill", command=lambda: fill(serial, buttons, output)).grid(row=2, column=width + 1)
  tk.Button(root, width=9, height=1, padx=10, pady=0, text="Invert", command=lambda: invert(serial, buttons, output)).grid(row=3, column=width + 1)

  updateOutput(buttons, output)
  
  root.mainloop()
  
  disconnectCOM(serial, port)