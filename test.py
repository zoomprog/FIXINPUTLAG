import winreg


def set_mouse_registry_settings():
    try:
        # Open the registry key for the current user
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Control Panel\Mouse', 0, winreg.KEY_SET_VALUE)

        # Set the MouseSensitivity value
        winreg.SetValueEx(key, 'MouseSensitivity', 0, winreg.REG_SZ, '10')

        # Set the SmoothMouseXCurve value
        smooth_mouse_x_curve = bytes.fromhex(
            '00 00 00 00 00 00 00 00 C0 CC 0C 00 00 00 00 00 80 99 19 00 00 00 00 00 40 66 26 00 00 00 00 00 00 33 33 00 00 00 00 00')
        winreg.SetValueEx(key, 'SmoothMouseXCurve', 0, winreg.REG_BINARY, smooth_mouse_x_curve)

        # Set the SmoothMouseYCurve value
        smooth_mouse_y_curve = bytes.fromhex(
            '00 00 00 00 00 00 00 00 00 00 38 00 00 00 00 00 00 00 70 00 00 00 00 00 00 00 A8 00 00 00 00 00 00 00 E0 00 00 00 00 00')
        winreg.SetValueEx(key, 'SmoothMouseYCurve', 0, winreg.REG_BINARY, smooth_mouse_y_curve)

        # Close the key
        winreg.CloseKey(key)

        # Open the registry key for the default user
        key = winreg.OpenKey(winreg.HKEY_USERS, r'.DEFAULT\Control Panel\Mouse', 0, winreg.KEY_SET_VALUE)

        # Set the MouseSpeed value
        winreg.SetValueEx(key, 'MouseSpeed', 0, winreg.REG_SZ, '0')

        # Set the MouseThreshold1 value
        winreg.SetValueEx(key, 'MouseThreshold1', 0, winreg.REG_SZ, '0')

        # Set the MouseThreshold2 value
        winreg.SetValueEx(key, 'MouseThreshold2', 0, winreg.REG_SZ, '0')

        # Close the key
        winreg.CloseKey(key)

        print("Registry settings updated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function to set the registry settings
set_mouse_registry_settings()
