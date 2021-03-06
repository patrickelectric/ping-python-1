#!/usr/bin/python -u

# PingMessage.py
# Python implementation of the Blue Robotics 'Ping' binary message protocol

#~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!
# THIS IS AN AUTOGENERATED FILE
# DO NOT EDIT
#~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!

import struct

'''
A reminder for struct formatting:
b = i8
B = u8
h = i16
H = u16
i = i32
I = u32
char[] = s
'''

PING1D_PROFILE = 1300
PING1D_VOLTAGE_5 = 1202
PING1D_SET_MODE_AUTO = 1003
PING1D_GOTO_BOOTLOADER = 1100
PING1D_UNDEFINED = 0
PING1D_FW_VERSION = 1200
PING1D_PCB_TEMPERATURE = 1214
PING1D_ASCII_TEXT = 3
PING1D_PING_RATE = 1206
PING1D_SET_SPEED_OF_SOUND = 1002
PING1D_SET_DEVICE_ID = 1000
PING1D_CONTINUOUS_START = 1400
PING1D_GAIN_INDEX = 1207
PING1D_GENERAL_INFO = 1210
PING1D_DEVICE_ID = 1201
PING1D_DISTANCE = 1212
PING1D_DISTANCE_SIMPLE = 1211
PING1D_SET_RANGE = 1001
PING1D_MODE_AUTO = 1205
PING1D_SPEED_OF_SOUND = 1203
PING1D_NACK = 2
PING1D_ACK = 1
PING1D_PULSE_USEC = 1208
PING1D_RANGE = 1204
PING1D_SET_PING_RATE = 1004
PING1D_PROCESSOR_TEMPERATURE = 1213
PING1D_SET_GAIN_INDEX = 1005
PING1D_PROTOCOL_VERSION = 5
PING1D_CONTINUOUS_STOP = 1401
PING1D_SET_PING_ENABLE = 1006

# variable length fields are formatted with 's', and always occur at the end of the payload
# the format string for these messages is adjusted at runtime, and 's' inserted appropriately at runtime
# see PingMessage.getPayloadFormat()
payloadDict = {
    PING1D_PROFILE: {"name": "profile",
                       "format": "IHHIIIIH",
                       "field_names": (
                         "distance",
                         "confidence",
                         "pulse_usec",
                         "ping_number",
                         "scan_start",
                         "scan_length",
                         "gain_index",
                         "num_points",
                         "data",
                       ),
                       "payload_length": 26},
    PING1D_VOLTAGE_5: {"name": "voltage_5",
                       "format": "H",
                       "field_names": (
                         "mvolts",
                       ),
                       "payload_length": 2},
    PING1D_SET_MODE_AUTO: {"name": "set_mode_auto",
                       "format": "B",
                       "field_names": (
                         "mode_auto",
                       ),
                       "payload_length": 1},
    PING1D_GOTO_BOOTLOADER: {"name": "goto_bootloader",
                       "format": "",
                       "field_names": (
                       ),
                       "payload_length": 0},
    PING1D_UNDEFINED: {"name": "undefined",
                       "format": "",
                       "field_names": (
                       ),
                       "payload_length": 0},
    PING1D_FW_VERSION: {"name": "fw_version",
                       "format": "BBHH",
                       "field_names": (
                         "device_type",
                         "device_model",
                         "fw_version_major",
                         "fw_version_minor",
                       ),
                       "payload_length": 6},
    PING1D_PCB_TEMPERATURE: {"name": "pcb_temperature",
                       "format": "H",
                       "field_names": (
                         "temp",
                       ),
                       "payload_length": 2},
    PING1D_ASCII_TEXT: {"name": "ascii_text",
                       "format": "",
                       "field_names": (
                         "msg",
                       ),
                       "payload_length": 0},
    PING1D_PING_RATE: {"name": "ping_rate",
                       "format": "H",
                       "field_names": (
                         "ping_rate",
                       ),
                       "payload_length": 2},
    PING1D_SET_SPEED_OF_SOUND: {"name": "set_speed_of_sound",
                       "format": "I",
                       "field_names": (
                         "speed_of_sound",
                       ),
                       "payload_length": 4},
    PING1D_SET_DEVICE_ID: {"name": "set_device_id",
                       "format": "B",
                       "field_names": (
                         "device_id",
                       ),
                       "payload_length": 1},
    PING1D_CONTINUOUS_START: {"name": "continuous_start",
                       "format": "H",
                       "field_names": (
                         "id",
                       ),
                       "payload_length": 2},
    PING1D_GAIN_INDEX: {"name": "gain_index",
                       "format": "I",
                       "field_names": (
                         "gain_index",
                       ),
                       "payload_length": 4},
    PING1D_GENERAL_INFO: {"name": "general_info",
                       "format": "HHHHBB",
                       "field_names": (
                         "fw_version_major",
                         "fw_version_minor",
                         "mvolts",
                         "ping_rate",
                         "gain_index",
                         "mode_auto",
                       ),
                       "payload_length": 10},
    PING1D_DEVICE_ID: {"name": "device_id",
                       "format": "B",
                       "field_names": (
                         "device_id",
                       ),
                       "payload_length": 1},
    PING1D_DISTANCE: {"name": "distance",
                       "format": "IHHIIII",
                       "field_names": (
                         "distance",
                         "confidence",
                         "pulse_usec",
                         "ping_number",
                         "scan_start",
                         "scan_length",
                         "gain_index",
                       ),
                       "payload_length": 24},
    PING1D_DISTANCE_SIMPLE: {"name": "distance_simple",
                       "format": "IB",
                       "field_names": (
                         "distance",
                         "confidence",
                       ),
                       "payload_length": 5},
    PING1D_SET_RANGE: {"name": "set_range",
                       "format": "II",
                       "field_names": (
                         "scan_start",
                         "scan_length",
                       ),
                       "payload_length": 8},
    PING1D_MODE_AUTO: {"name": "mode_auto",
                       "format": "B",
                       "field_names": (
                         "mode_auto",
                       ),
                       "payload_length": 1},
    PING1D_SPEED_OF_SOUND: {"name": "speed_of_sound",
                       "format": "I",
                       "field_names": (
                         "speed_of_sound",
                       ),
                       "payload_length": 4},
    PING1D_NACK: {"name": "nack",
                       "format": "H",
                       "field_names": (
                         "nacked_id",
                         "nack_msg",
                       ),
                       "payload_length": 2},
    PING1D_ACK: {"name": "ack",
                       "format": "H",
                       "field_names": (
                         "acked_id",
                       ),
                       "payload_length": 2},
    PING1D_PULSE_USEC: {"name": "pulse_usec",
                       "format": "H",
                       "field_names": (
                         "pulse_usec",
                       ),
                       "payload_length": 2},
    PING1D_RANGE: {"name": "range",
                       "format": "II",
                       "field_names": (
                         "scan_start",
                         "scan_length",
                       ),
                       "payload_length": 8},
    PING1D_SET_PING_RATE: {"name": "set_ping_rate",
                       "format": "H",
                       "field_names": (
                         "ping_rate",
                       ),
                       "payload_length": 2},
    PING1D_PROCESSOR_TEMPERATURE: {"name": "processor_temperature",
                       "format": "H",
                       "field_names": (
                         "temp",
                       ),
                       "payload_length": 2},
    PING1D_SET_GAIN_INDEX: {"name": "set_gain_index",
                       "format": "B",
                       "field_names": (
                         "gain_index",
                       ),
                       "payload_length": 1},
    PING1D_PROTOCOL_VERSION: {"name": "protocol_version",
                       "format": "I",
                       "field_names": (
                         "protocol_version",
                       ),
                       "payload_length": 4},
    PING1D_CONTINUOUS_STOP: {"name": "continuous_stop",
                       "format": "H",
                       "field_names": (
                         "id",
                       ),
                       "payload_length": 2},
    PING1D_SET_PING_ENABLE: {"name": "set_ping_enable",
                       "format": "B",
                       "field_names": (
                         "enable",
                       ),
                       "payload_length": 1},
}

asciiMsgs = [PING1D_NACK, PING1D_ASCII_TEXT]
varMsgs = [PING1D_PROFILE,]

class PingMessage(object):
    ## header start byte 1
    start_1 = ord("B")

    ## header start byte 2
    start_2 = ord("R")

    ## header struct format
    header_format = "BBHHBB"

    ## checksum struct format
    checksum_format = "H"

    ## data endianness for struct formatting
    endianess = "<"
    
    ## names of the header fields
    header_field_names = (
        "start_1",
        "start_2",
        "payload_length",
        "message_id",
        "src_device_id",
        "dst_device_id")

    ## number of bytes in a header
    headerLength = 8

    ## number of bytes in a checksum
    checksumLength = 2

    ## Messge constructor
    #
    # @par Ex request:
    # @code
    # m = PingMessage()
    # m.request_id = m_id
    # m.packMsgData()
    # write(m.msgData)
    # @endcode
    # 
    # @par Ex set:
    # @code
    # m = PingMessage(PING1D_SET_RANGE)
    # m.start_mm = 1000
    # m.length_mm = 2000
    # m.update_checksum()
    # write(m.msgData)
    # @endcode
    # 
    # @par Ex receive:
    # @code
    # m = PingMessage(rxByteArray)
    # if m.message_id == PING1D_RANGE
    #     start_mm = m.start_mm
    #     length_mm = m.length_mm
    # @endcode
    def __init__(self, id=0, msgData=None):

        ## The message id
        self.message_id = id
        ## The request id for request messages
        self.request_id = None
        ## Number of bytes in the message payload
        self.payload_length = payloadDict[id]["payload_length"]
        ## The message destination
        self.dst_device_id = 0
        ## The message source
        self.src_device_id = 0
        ## The message checksum
        self.checksum = 0

        ## The raw data buffer for this message
        # update with packMsgData()
        self.msgData = None
        if msgData is not None:
            self.unpackMsgData(msgData)

        ## The name of this message
        self.name = payloadDict[self.message_id]["name"]
        ## The struct formatting string for the message payload
        self.payload_format = payloadDict[id]["format"]
        ## The field names of this message
        self.payload_field_names = payloadDict[id]["field_names"]

    ## Pack object attributes into self.msgData (bytearray)
    # @return self.msgData
    def packMsgData(self):
        # Prepare struct packing format string
        format = PingMessage.endianess + PingMessage.header_format + self.getPayloadFormat()

        # Prepare complete list of field names (header + payload)
        attrs = PingMessage.header_field_names + payloadDict[self.message_id]["field_names"]

        # Prepare iterable ordered list of values to pack
        values = []
        for attr in attrs:
            # this is a hack for requests
            if attr == "message_id" and self.request_id is not None:
                values.append(self.request_id)
            else:
                values.append(getattr(self, attr))

        # Pack message contents into bytearray
        self.msgData = bytearray(struct.pack(format, *values))

        # Update and append checksum
        self.msgData += bytearray(struct.pack(PingMessage.endianess + PingMessage.checksum_format, self.updateChecksum()))

        return self.msgData

    ## Unpack a bytearray into object attributes
    def unpackMsgData(self, msgData):
        self.msgData = msgData

        # Extract header
        header = struct.unpack(PingMessage.endianess + PingMessage.header_format, self.msgData[0:PingMessage.headerLength])

        for i, attr in enumerate(PingMessage.header_field_names):
            setattr(self, attr, header[i])

        if self.payload_length > 0:
            # Extract payload
            try:
                payload = struct.unpack(PingMessage.endianess + self.getPayloadFormat(), self.msgData[PingMessage.headerLength:PingMessage.headerLength + self.payload_length])
            except Exception as e:
                print("error unpacking payload: %s" % e)
                print("msgData: %s, header: %s" % (msgData, header))
                print("format: %s, buf: %s" % (PingMessage.endianess + self.getPayloadFormat(), self.msgData[PingMessage.headerLength:PingMessage.headerLength + self.payload_length]))
            for i, attr in enumerate(payloadDict[self.message_id]["field_names"]):
                setattr(self, attr, payload[i])

        # Extract checksum
        self.checksum = struct.unpack(PingMessage.endianess + PingMessage.checksum_format, self.msgData[PingMessage.headerLength + self.payload_length: PingMessage.headerLength + self.payload_length + PingMessage.checksumLength])[0]

    ## Calculate the checksum from the internal bytearray self.msgData
    def calculateChecksum(self):
        checksum = 0
        for byte in self.msgData[0:PingMessage.headerLength + self.payload_length]:
            checksum += byte
        return checksum

    ## Update the object checksum value
    # @return the object checksum value
    def updateChecksum(self):
        self.checksum = self.calculateChecksum()
        return self.checksum

    ## Verify that the object checksum attribute is equal to the checksum calculated according to the internal bytearray self.msgData
    def verifyChecksum(self):
        return self.checksum == self.calculateChecksum()

    ## Get the python struct formatting string for the message payload
    # @return the payload struct format string
    def getPayloadFormat(self):
        if self.message_id in varMsgs or self.message_id in asciiMsgs:
            varLength = self.payload_length - payloadDict[self.message_id]["payload_length"] # Subtract static length portion from payload length
            if varLength <= 0:
                return "" # variable data portion is empty

            return payloadDict[self.message_id]["format"] + str(varLength) + "s"
        else:
            return payloadDict[self.message_id]["format"]

    ## Dump object into string representation
    # @return string representation of the object
    def __repr__(self):
        headerString = "Header:"
        for attr in PingMessage.header_field_names:
            headerString += " " + attr + ": " + str(getattr(self, attr))

        if self.payload_length == 0: # this is a hack/guard for empty body requests
            payloadString = ""
        else:
            payloadString = "Payload:"

            # handle variable length messages
            if self.message_id in varMsgs:

                # static fields are handled as usual
                for attr in payloadDict[self.message_id]["field_names"][:-1]:
                    payloadString += "\n  - " + attr + ": " + str(getattr(self, attr))

                # the variable length field is always the last field
                attr = payloadDict[self.message_id]["field_names"][-1:][0]

                # format this field as a list of hex values (rather than a string if we did not perform this handling)
                payloadString += "\n  - " + attr + ": " + str([hex(ord(item)) for item in getattr(self, attr)])

            else: # handling of static length messages and text messages
                for attr in payloadDict[self.message_id]["field_names"]:
                    payloadString += "\n  - " + attr + ": " + str(getattr(self, attr))

        representation = (
            "\n\n--------------------------------------------------\n"
            "ID: " + str(self.message_id) + " - " + self.name + "\n" +
            headerString + "\n" +
            payloadString + "\n" +
            "Checksum: " + str(self.checksum) + " check: " + str(self.calculateChecksum()) + " pass: " + str(self.verifyChecksum())
        )

        return representation

# A class to digest a serial stream and decode PingMessages
class PingParser(object):
    NEW_MESSAGE       = 0    # Just got a complete checksum-verified message
    WAIT_START        = 1    # Waiting for the first character of a message 'B'
    WAIT_HEADER       = 2    # Waiting for the second character in the two-character sequence 'BR'
    WAIT_LENGTH_L     = 3    # Waiting for the low byte of the payload length field
    WAIT_LENGTH_H     = 4    # Waiting for the high byte of the payload length field
    WAIT_MSG_ID_L     = 5    # Waiting for the low byte of the payload id field
    WAIT_MSG_ID_H     = 6    # Waiting for the high byte of the payload id field
    WAIT_SRC_ID       = 7    # Waiting for the source device id
    WAIT_DST_ID       = 8    # Waiting for the destination device id
    WAIT_PAYLOAD      = 9    # Waiting for the last byte of the payload to come in
    WAIT_CHECKSUM_L   = 10   # Waiting for the checksum low byte
    WAIT_CHECKSUM_H   = 11   # Waiting for the checksum high byte

    def __init__(self):
        self.buf = bytearray()
        self.state = PingParser.WAIT_START
        self.payload_length = 0 # payload length remaining to be parsed for the message currently being parsed
        self.message_id = 0 # message id of the message currently being parsed
        self.errors = 0
        self.parsed = 0
        self.rxMsg = None # most recently parsed message

    # Feed the parser a single byte
    # Returns the current parse state
    # If the byte fed completes a valid message, return PingParser.NEW_MESSAGE
    # The decoded message will be available in the self.rxMsg attribute until a new message is decoded
    def parseByte(self, byte):
        if type(byte) != int:
            byte = ord(byte)
        #print("byte: %d, state: %d, rem: %d, id: %d" % (byte, self.state, self.payload_length, self.message_id))
        if self.state == PingParser.WAIT_START:
            if byte == ord('B'):
                self.buf.append(byte)
                self.state += 1
        elif self.state == PingParser.WAIT_HEADER:
            if byte == ord('R'):
                self.buf.append(byte)
                self.state += 1
            else:
                self.state = PingParser.WAIT_START
        elif self.state == PingParser.WAIT_LENGTH_L:
            self.payload_length = byte
            self.buf.append(byte)
            self.state += 1
        elif self.state == PingParser.WAIT_LENGTH_H:
            self.payload_length = (byte << 8) | self.payload_length
            self.buf.append(byte)
            self.state += 1
        elif self.state == PingParser.WAIT_MSG_ID_L:
            self.message_id = byte
            self.buf.append(byte)
            self.state += 1
        elif self.state == PingParser.WAIT_MSG_ID_H:
            self.message_id = (byte << 8) | self.message_id
            self.buf.append(byte)
            self.state += 1
        elif self.state == PingParser.WAIT_SRC_ID:
            self.buf.append(byte)
            self.state += 1
        elif self.state == PingParser.WAIT_DST_ID:
            self.buf.append(byte)
            self.state += 1
            if (self.payload_length == 0): # no payload bytes
                self.state +=1
        elif self.state == PingParser.WAIT_PAYLOAD:
            self.buf.append(byte)
            self.payload_length -= 1
            if self.payload_length == 0:
                self.state += 1
        elif self.state == PingParser.WAIT_CHECKSUM_L:
            self.buf.append(byte)
            self.state += 1
        elif self.state == PingParser.WAIT_CHECKSUM_H:
            self.buf.append(byte)
            self.rxMsg = PingMessage(msgData = self.buf)

            #print(self.rxMsg)

            self.buf = bytearray()
            self.state = PingParser.WAIT_START
            self.payload_length = 0
            self.message_id = 0

            if self.rxMsg.verifyChecksum():
                self.parsed += 1
                return PingParser.NEW_MESSAGE
            else:
                self.errors += 1

        return self.state

if __name__ == "__main__":
    import argparse
    import serial
    import time

    parser = argparse.ArgumentParser(description="Ping python library example.")
    parser.add_argument('--device', action="store", required=True, type=str, help="Ping device port.")
    parser.add_argument('--baudrate', action="store", type=int, default=115200, help="Ping device baudrate.")
    args = parser.parse_args()

    p = PingParser()

    # Hand-written data buffers for testing and verification
    test_voltage_5_buf = bytearray([0x42, 0x52, 0x02, 0x00, 0xB2, 0x04, 0x05, 0x06, 0x01, 0x01, 0x59, 0x01])
    test_nack_buf = bytearray([0x42, 0x52, 0x06, 0x00, 0x03, 0x00, 0x05, 0x06, 0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x00, 0xBC, 0x02])
    test_profile_buf = bytearray([0x42, 0x52,  0x1E, 0x00,  0x14, 0x05,  0x05, 0x06,
                               0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x00, 0x00,
                               0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x00, 0x00,
                               0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x00, 0x00,
                               0x68, 0x65, 0x6c, 0x6c, 0x6f,
                               0x1, 0x2, 0x63, 0x64,
                               0xB2, 0x0A])

    # A static length message
    print("\n\n---Testing voltage_5---\n")
    for byte in test_voltage_5_buf:
        p.parseByte(byte)
    print(p.rxMsg)

    # A text message
    print("\n\n---Testing nack---\n")
    for byte in test_nack_buf:
        p.parseByte(byte)
    print(p.rxMsg)

    # A dynamic vector message
    print("\n\n---Testing profile---\n")
    for byte in test_profile_buf:
        p.parseByte(byte)
    print(p.rxMsg)

    print("\n\n\n")

    # Connect to a device
    s = serial.Serial(args.device, args.baudrate)
    while True:
        m = PingMessage(PING1D_SET_PING_RATE)
        m.ping_rate = 40
        m.packMsgData()
        s.write(m.msgData)
        time.sleep(0.01)
        print(m)
        while s.in_waiting:
            if p.parseByte(s.read()) == PingParser.NEW_MESSAGE:
                print(p.rxMsg)

        m = PingMessage()
        m.request_id = PING1D_PROFILE
        m.packMsgData()
        s.write(m.msgData)
        time.sleep(0.05)
        while s.in_waiting:
            if p.parseByte(s.read()) == PingParser.NEW_MESSAGE:
                print(p.rxMsg)
        m.request_id = PING1D_VOLTAGE_5
        m.packMsgData()
        s.write(m.msgData)
        time.sleep(0.01)
        while s.in_waiting:
            if p.parseByte(s.read()) == PingParser.NEW_MESSAGE:
                print(p.rxMsg)
        m.request_id = PING1D_DISTANCE_SIMPLE
        m.packMsgData()
        s.write(m.msgData)
        time.sleep(0.01)
        while s.in_waiting:
            if p.parseByte(s.read()) == PingParser.NEW_MESSAGE:
                print(p.rxMsg)
        print("parsed: %d errors: %d" % (p.parsed, p.errors))
