import logging
from typing import Dict, Tuple


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


test_settings: Dict[str, str] = {
    "theme": "dark",
    "language": "english",
    "notifications": "enabled"
}


def add_setting(settings: Dict[str, str], pair: Tuple[str, str]) -> str:
    """
    Adds a new key-value setting to the settings dictionary.
    Returns a success or failure message.
    """
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        msg = f"Setting '{key}' already exists! Cannot add a new setting with this name."
        logging.warning(msg)
        return msg

    settings[key] = value
    msg = f"Setting '{key}' added with value '{value}' successfully!"
    logging.info(msg)
    return msg


def update_setting(settings: Dict[str, str], pair: Tuple[str, str]) -> str:
    """
    Updates an existing setting in the dictionary.
    Returns a success or failure message.
    """
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key not in settings:
        msg = f"Setting '{key}' does not exist! Cannot update a non-existing setting."
        logging.error(msg)
        return msg

    settings[key] = value
    msg = f"Setting '{key}' updated to '{value}' successfully!"
    logging.info(msg)
    return msg


def delete_setting(settings: Dict[str, str], key: str) -> str:
    """
    Deletes a setting from the dictionary.
    Returns a success or failure message.
    """
    key = key.lower()
    if key not in settings:
        msg = "Setting not found!"
        logging.error(msg)
        return msg

    del settings[key]
    msg = f"Setting '{key}' deleted successfully!"
    logging.info(msg)
    return msg


def view_settings(settings: Dict[str, str]) -> str:
    """
    Formats the current settings into a readable string.
    Returns the string representation of all settings.
    """
    if not settings:
        msg = "No settings available."
        logging.warning(msg)
        return msg

    result = "Current User Settings:\n"
    for k, v in settings.items():
        result += f"{k.capitalize()}: {v}\n"
    return result


if __name__ == "__main__":
    logging.info("Testing User Configuration Manager")
    
    print(view_settings(test_settings))

    # Test Add
    add_setting(test_settings, ("volume", "high"))
    add_setting(test_settings, ("theme", "light")) # Should fail
    
    # Test Update
    update_setting(test_settings, ("language", "spanish"))
    update_setting(test_settings, ("color_blind_mode", "on")) # Should fail
    
    # Test Delete
    delete_setting(test_settings, ("notifications"))
    delete_setting(test_settings, ("font_size")) # Should fail
    
    print("\nUpdated Settings:")
    print(view_settings(test_settings))
