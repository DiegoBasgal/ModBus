from time import sleep
from pyModbusTCP.server import DataBank, ModbusServer

class mbServer():

    def __init__(self, host_ip, port):
        # Creating a new modbus server instance
        self._db = DataBank()
        self._server = ModbusServer(host=host_ip,port=port,no_block=True,data_bank=self._db)
       
    def run(self):
        # Executing modbus server
        try:
            print("\n---------------------")
            print("\nServer starting")
            self._server.start()
            print("\n\nServer Online.\n")
            try:
                while True:
                    print("\n---------------------")
                    print("Modbus Table:")
                    print(f'HR 10: {self._db.get_holding_registers(9)}')
                
                    if self._db.get_holding_registers(9) == [0]:
                        self._db.set_holding_registers(9, [int(0)])

                    sleep(2)

            except KeyboardInterrupt:
                pass

        except Exception as e:
            print("Error: ",e.args)
