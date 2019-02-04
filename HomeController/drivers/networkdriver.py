import socket
from drivers.driver import Driver
from Utils.utils import get_attribute


class NetworkDriver(Driver):
    """
    Driver that handles the UDP communication
    """
    def __init__(self, network_config):
        """
        initialises the udp driver
        @param network_config: configuration for the driver
                needed fields:
                  "driver": The driver file (package(s).module.class),
                  "send_ip": IP of the other communicator,
                  "send_port": Port where the other communicator listens to,
                  "listen_ip": IP of ethernet port that listens to incoming messages,
                  "listen_port": Listen port,
                  "handler": the handler file (package(s).module.class),
                  "enable": if driver needs to be enabled (used mostly for debugging purpose)
        """
        Driver.__init__(self, network_config)
        """
        initialises the driver
        """
        self.send_ip = get_attribute("send_ip", network_config)
        self.send_port = int(get_attribute("send_port", network_config))
        self.connected = True
        self.handshake_thread.start()
        self.start_listening()

    def init_communicator(self, network_config):
        """
        Initialises the udp socket and binds the socket to an ip and port
        @param network_config: configuration for the udp socket
        @return: None
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((get_attribute("listen_ip", network_config), int(get_attribute("listen_port", network_config))))
        return sock

    def receive(self):
        """
        receive message from udp socket
        @return: the received data (byte array)
        """
        data, address = self.communicator.recvfrom(1024)
        print("Received packet from: " + address[0])
        print("Packet data: " + data.decode("ascii"))
        return data

    def write(self, serialized_packet):
        """
        write byte array to send ip and send port via socket
        @param serialized_packet:
        @return: None
        """
        print("Sent packet: " + serialized_packet.decode("ascii"))
        self.communicator.sendto(serialized_packet, (self.send_ip, self.send_port))
