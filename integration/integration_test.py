# import addition
# import multiplication
import math

import area

def test_area_positive():
 assert round(area.calculate_area_of_triangle(3, 4, 5), 2) == 6.0

def test_area_negative():
  assert area.calculate_area_of_triangle(-4, 3, 5) == "Error"


