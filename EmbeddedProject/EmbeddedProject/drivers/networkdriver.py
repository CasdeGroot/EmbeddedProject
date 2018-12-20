import socket
from EmbeddedProject.drivers.driver import Driver
from EmbeddedProject.Utils.utils import get_attribute


class NetworkDriver(Driver):
    def __init__(self, network_config):
        Driver.__init__(self, network_config)
        self.send_ip = get_attribute("send_ip", network_config)
        self.send_port = int(get_attribute("send_port", network_config))
        self.connected = True
        self.start_listening()

    def init_communicator(self, network_config):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((get_attribute("listen_ip", network_config), int(get_attribute("listen_port", network_config))))
        return sock

    def receive(self):
        data, address = self.communicator.recvfrom(1024)
        print("Received packet from: " + address[0])
        print("Packet data: " + data.decode("ascii"))
        return data

    def write(self, serialized_packet):
        print("Sent packet to: " + self.send_ip)
        print("Packet data: " + serialized_packet.decode("ascii"))
        self.communicator.sendto(serialized_packet, (self.send_ip, self.send_port))
