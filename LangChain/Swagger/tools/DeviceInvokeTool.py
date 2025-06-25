

class DeviceInvokeTool:
    @staticmethod
    def get_name():
        return "DeviceInvokeTool"

    @staticmethod
    def get_description():
        return """
        This tool is designed to serve as a unified interface for executing commands on edge devices from a centralized platform. It acts as a bridge between the platform and the device-side APIs, enabling remote invocation of device functions in a secure, reliable, and scalable manner.
    
        Key Features:
    
        Remote Command Execution: Initiate and dispatch control commands to connected devices from the platform.
    
        API Abstraction: Simplifies device-side API calls into standardized platform-side interfaces.
    
        Protocol Adaptability: Supports integration with devices using HTTP, MQTT, CoAP, or custom protocols.
    
        Execution Feedback: Collects and reports execution status and results back to the platform.
    
        Security & Permissions: Ensures only authorized commands are executed on each device.
    
        Use Case Scenario:
    
        When a platform user initiates a device control command (e.g., reboot, fetch sensor data, trigger actuator), this utility captures the command, translates it into the appropriate device API format, and securely forwards it to the target device. The device processes the command and returns the result, which the utility captures and reports back to the platform for user visibility.
        """