import json


class LocalSystemTool:
    def __init__(self, command):
        self.command = command

        self.toolTable = [
            {
                "toolName": "Product Controller Tool",
                "function": "this tool can Control the target device. such as \n"
                            "1.call the device API to send data to the device.\n"
                            "2.retrieve properties from the device.\n"
                            "3.let the device complete specified operations.\n"
                            "The functions of this device include:\n"
            },
            {
                "toolName": "Device Controller Tool",
                "function": "this tool can Retrieve history properties reported by the device.\n"
                            "These properties are not immediately obtained from the device, but are obtained from the IOT system.\n"
                            "NOTE: If 'Device Control tool' does not support actively retrieving properties, then 'View Device Property Tool' can get the latest property. Otherwise, the latest properties should be obtained through the 'Device Control Tool'"
            },
            {
                "toolName": "Plugin Controller Tool",
                "function": "this tool can Retrieve history alerts reported by the device.\n"
                            "A plugin is a gateway to the device.\n"
                            "If the corresponding plugin is closed, the device will not be able to access the IOT system.\n "
                            "Plugin tools can:\n"
                            "1.query the corresponding plugins for devices through DeviceName or productKey.\n"
                            "2.switch plugin states (open, closed)."
                            "3.modify plugin names.\n"
                            "4.delete specified plugins.\n"
                            "5.view plugin details."
            },
            {
                "toolName": "Alert Controller Tool",
                "function": "this tool can Modify device properties, which 'Device Control Tool' does not support.\n"
            },
            {
                "toolName": "Sys User Controller Tool",
            },
            {
                "toolName": "Sys Logininfor Controller Tool",
            }
        ]