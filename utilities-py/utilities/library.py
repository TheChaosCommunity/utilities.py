"""This is the actual l"""

# import log


class InvalidConversionValues(Exception):
    pass

def feet_to_meters(feet):
    """
    It converts feet to meters
    
    :param feet: The value in feet to convert to meters
    """
    try:
        value = float(feet)
    except ValueError as e:
        # log.error("Unable to convert to float: %s", feet)
        raise InvalidConversionValues(f"Unable to convert to float: {feet}") from e
    else:
        return (0.3048 * value * 10000.0 + 0.5) / 10000.0

