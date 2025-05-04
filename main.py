def is_bulky(width: int, height: int ,length: int):
  '''check if a package is bulky'''
  # edge case
  if not all(isinstance(dim, int) and dim > 0 for dim in (width, height, length)):
     raise ValueError("Dimensions must be positive integers")
  return width*height*length>=1000000 or any(dim >= 150 for dim in [width, height, length])

def is_heavy(mass: int):
  '''check if a package is heavy'''
  # edge case
  if not isinstance(mass, int) or mass <= 0:
     raise ValueError("Mass must be a positive integer")
  return mass >= 20

def sort(width, height, length, mass):
  # edge case
  if not all(isinstance(dim, int) and dim > 0 for dim in (width, height, length, mass)):
     raise ValueError("All inputs must be positive integers")
  
  bulky = is_bulky(width, height, length)
  heavy = is_heavy(mass)

  if bulky and heavy:
      return "REJECTED"
  elif bulky or heavy:
      return "SPECIAL"
  else:
      return "STANDARD"