from CHIP_IO import GPIO
import yaml

CONFIG_FILE = "water.yaml"
PIN_DEFAULT = "CSID0"
TIME_DEFAULT = 60

class Water(object):
    def __init__(self):
        conf = self.loadConf()
        self._pin = conf['pin'] if 'pin' in conf else PIN_DEFAULT
        self._time = conf['time'] if 'time' in conf else TIME_DEFAULT
        self.setupPin(self._pin)

    def loadConf(self):
        config = {}
        try:
            fd = open(CONFIG_FILE, 'r')
            config = yaml.load(fd)
        except:
            pass
        return config

    def setupPin(self, pin):
        GPIO.setup(pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    @property
    def pin(self):
        return self._pin

    @property
    def time(self):
        return self._time
