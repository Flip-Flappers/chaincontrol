import json


class LocalSystemTool:
    def __init__(self, command):
        self.command = command

        self.toolTable = [
            {
                "toolName": "Device Control Tool",
                "function": "this tool can Control the target device. such as \n"
                            "1.call the device API to send data to the device.\n"
                            "2.retrieve properties from the device.\n"
                            "3.let the device complete specified operations.\n"
                            "The functions of this device include:\n"
            },
            {
                "toolName": "View Device Property Tool",
                "function": "this tool can Retrieve history properties reported by the device.\n"
                            "These properties are not immediately obtained from the device, but are obtained from the IOT system.\n"
                            "NOTE: If 'Device Control tool' does not support actively retrieving properties, then 'View Device Property Tool' can get the latest property. Otherwise, the latest properties should be obtained through the 'Device Control Tool'"
            },
            {
                "toolName": "View Device Alert Tool",
                "function": "this tool can Retrieve history alerts reported by the device.\n"
                            "These alerts are not immediately obtained from the device, but are obtained from the IOT system.\n"
            },
            {
                "toolName": "View Device Status Tool",
                "function": "this tool can Show the status of the device.\n"
            },
            {
                "toolName": "Modify Device properties Tool",
                "function": "this tool can Modify device properties, which 'Device Control Tool' does not support.\n"
            }
        ]