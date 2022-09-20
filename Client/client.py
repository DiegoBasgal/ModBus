from time import sleep
from pyModbusTCP.client import ModbusClient

class mbClient():
   
    def __init__(self, server_ip, port, scan_time=1):
        # Constructor
        self._scan_time = scan_time
        self._client = ModbusClient(host=server_ip,port = port)

    def run(self):
        # Method used for client connection
        self._client.open()

        try:
            while True:
                # Input option cases
                sel = input(f"\nSelect wich operation to execute:\n1 - Read \n2 - Write \n3 - Config \n4 - Exit\n\nOp: ")
                
                # Case 1 -> read operations
                if sel == "1":
                    print("\n---------------------------------")
                    operation = input(f"\nSelect wich register to read:\n1 - Holding Register \n2 - Coil \n3 - Input Register \n4 - Discrete Input\n\nOperation: ")
                    print("\n---------------------------------")
                      
                    if operation != [1, 2, 3, 4]:
                        addr = input("\nEnter the Modbus table address: ")
                        n_reads = input("\nEnter number of reads value: ")

                        for i in range (0, int(n_reads)):
                            print(f"Reads: {i+1}: {self.readData(int(operation), int(addr))}")
                            sleep(self._scan_time)
                    else:
                        ("Invalid operation")

                # Case 2 -> write operations
                elif sel == "2":
                    print("\n---------------------------------")
                    operation = input(f"\nSelect wich register to write:\n1 - Holding Register \n2 - Coil\n\n Operation: ")
                    print("\n---------------------------------")
                    addr = input("\nEnter the Modbus table address: ")
                    value = input("\nEnter write value: ")
                    self.writeData(int(operation), int(addr), int(value))

                # Case 3 -> Sweep time
                elif sel == "3":
                    print("\n---------------------------------")
                    s_time = input("\nEnter the desired sweep time [s]: ")
                    self._scan_time = float(s_time)

                # Case 4 -> Disconnect
                elif sel == "4":
                    print("\n---------------------------------")
                    print("\nDisconnecting...")
                    self._client.close()
                else:
                    print("Invalid operation") 

        except Exception as e:
            print('Error: ',e.args)

    def readData(self, operation, addr):
        # Method used for reading data from modbus table
        if operation == 1:
            return self._client.read_holding_registers(addr, 1)[0]
        if operation == 2:
            return self._client.read_coil(addr, 1)[0]
        if operation == 3:
            return self._client.read_input_registers(addr, 1)[0]
        if operation == 4:
            return self._client.read_discrete_registers(addr, 1)[0]

    def writeData(self, operation, addr, value):
        # Method used for writing data from modbus table
        if operation == 1:
            return self._client.write_single_register(addr, value)
        if operation == 2:
            return self._client.write_single_coil(addr, value)
