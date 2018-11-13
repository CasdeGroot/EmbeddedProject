import EmbeddedProject.drivers.usbdriver as usb

def test_readPortNoName():
    assert usb.open_serial_port() is None
