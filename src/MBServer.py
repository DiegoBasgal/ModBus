from pyModbusTCP.server import ModbusServer, DataBank
import sys, time
from time import sleep
from random import uniform

class MBServer():
    
    connected = True

    def __init__(self, host_ip, port):
        # Creating a new modbus server instance
        self._server = ModbusServer(host=host_ip, port=port, no_block=True)
        self._db = DataBank
    
    def run(self):
        # Executing modbus server
        try:
            print("\n---------------------")
            print("\nServer starting", end="")
            for i in range(3):
                sys.stdout.write(".")
                sys.stdout.flush()
                sleep(1)

            self._server.start()
            print("\n\nServer Online.\n")

            try:
                while True:
                    self._db.set_words(1000, [int(uniform(0, 100))])
                    print("---------------------")
                    print("Modbus table:")
                    print(f"Holding register \r\n R1000: {self._db.get_words(1000)} \r\n R2000: {self._db.get_words(2000)}")
                    sleep(5)
            except KeyboardInterrupt:
                connected = False
                pass   
        
        except Exception as e:
            print("Error: ", e.args)