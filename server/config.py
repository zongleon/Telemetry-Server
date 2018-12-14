# Keys in the SQLite table
dataKeys = [
    "controllerTemp",
    "controllerOutCurrent",
    "controllerInCurrent",
    "controllerDutyCycle",
    "controllerRpm",
    "controllerInVoltage",
    "vescFault",
    "alltraxFault",
    "batteryPackVoltage",
    "batteryCellVoltage0",
    "batteryCellVoltage1",
    "batteryCellVoltage2",
    "batteryCellVoltage3",
    "batteryCellVoltage4",
    "batteryCellVoltage5",
    "batteryCellVoltage6",
    "batteryCellVoltage7",
    "batteryCellVoltage8",
    "batteryCellVoltage9",
    "batteryBusTemp1",
    "batteryBusTemp2",
    "batteryBusTemp3",
    "batteryBusTemp4",
    "bmvTimeRemaining",
    "bmvConsumedAh",
    "bmvVoltage",
    "bmvAuxVoltage",
    "bmvCurrent",
    "bmvPower",
    "bmvStateOfCharge",
    "motorRpm",
    "propRpm",
    "motorTemp",
    "gyroTrimAngle",
    "gyroRollAngle",
    "gyroYawAngle",
    "gpsSpeed",
    "gpsHeading",
    "gpsTimestamp",
    "gpsLatitude",
    "gpsLongitude",
    "gpsNumSatellites",
    "usbGpsLatitude",
    "usbGpsLongitude",
    "usbGpsNumSatellites",
    "throttle"
]

# Defines thresholds for any values
# Each item in the dict is a data key, mapped to an array
# element 0 is the minimum, element 1 is maximum
# alarm is TRUE if the data is out of this range
alarmThresholds = {
    'bmvVoltage' : [32,40],
    'bmvAuxVoltage' : [32,40],
    'bmvCurrent' : [-20,100],
    'bmvStateOfCharge' : [50,100],
    'motorTemp' : [50,150],
    'motorRpm' : [0,3600]
}

# Blacklist for serial ports
portBlacklist = [
    "/dev/cu.Bluetooth-Incoming-Port",
    "/dev/ttyAMA0",
    "/dev/cu.JBLCharge3-SPPDev-1"
]

# Database path
# Folder must exist
dbFolder = "~/SOLAR_SPLASH/telemetry/"
dbFile = "test1.db"

# Prefix for each session of telemetry data
dbTablePrefix = "dataSession"

# Whether to erase the database on start
dbEraseOnStart = True

# Debug: Ignore all devices, don't connect to anything
ignoreDevices = False

# Interval at which devices are polled
pollRate = 0

# Interval at which devices are scanned
scanRate = 1

# Interval at which data is saved to database
saveRate = 1


# Number of seconds until a data point is invalidated
dataTimeOut = 5

# Port for the HTTP interface
httpPort = 8081


#--- Control Algorithms Configuration ---
# Control algorithms can set telemetry data points based on other data points.
# For example, this can be used to drive the autopilot system in endurance.
# Will be automatically disabled if the server is "slave",eg, receiving radio telemetry.
isSlave = False

# Interval at which control algorithms are updated, if relevant
controlAlgorithmUpdateRate = 0.1

# Control algorithm which saves some mock data for testing
controlAlgorithmMockData = True

# Control algorithm which auto regulates throttle for endurance
controlAlgorithmEnduranceThrottle = False
