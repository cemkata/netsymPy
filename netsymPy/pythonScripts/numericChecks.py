def is_valid_numeric(inString):
    """Validates if the value is int or float."""
    return is_int(inString) or is_float(inString)

def is_port(inString):
    """Validates if the port is valid."""
    if is_int(inString):
       intiger = int(inString)
       return intiger >= 0 and intiger < 65536
                        #the 0 is acepted, beacuse later it will be modifyed
    else:
      return False

def is_valid_procent(inString):
    """Validates if the procent is valid."""
    if is_float(inString):
        procent = float(inString)
        return procent >= 0 and procent < 100
                        #the 0 is acepted, beacuse later it will be modifyed
    else:
      return False

def is_int(inString):
    try:
        int(inString)
        return True
    except (ValueError, TypeError) as e:
        return False

def is_float(inString):
    try:
        float(inString)
        return True
    except (ValueError, TypeError) as e:
        return False