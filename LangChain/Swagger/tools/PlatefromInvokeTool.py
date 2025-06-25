
class DeviceInvokeTool:
    @staticmethod
    def get_name():
        return "DeviceInvokeTool"

    @staticmethod
    def get_description():
        return """
        This tool is designed to interact programmatically with the platform’s internal APIs, providing streamlined access to a wide range of Create, Read, Update, and Delete (CRUD) operations. It serves as a general-purpose client for managing resources within the platform, such as devices, users, tasks, and configurations.

        Key Features:

        Full CRUD Operations: Supports creation, retrieval, updating, and deletion of platform-managed resources.

        Modular API Access: Easily extends to cover different modules including device management, user access control, alert rules, automation tasks, and more.
        
        Use Case Scenario:

        The utility allows developers and operators to manage the platform through code or automation scripts. For example, one can register new devices, update user permissions, delete obsolete tasks, or fetch real-time status of alerts—all through a consistent, well-structured interface that abstracts the raw API calls.
        """