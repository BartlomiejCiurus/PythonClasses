__author__ = 'Bartlomiej Ciurus'

from decimal import Decimal
from fractions import Fraction

# representing different types of numbers

real = 2.5  # by str() and repr(): 2.5
positiveInteger = 2  # by str() and repr(): 2.5
negativeInteger = -4  # by str() and repr(): -4
complexNumber = 2 + 2j  # by str() and repr(): (2+2j)
decimalNumber = Decimal(423.42)  # by str(): 423.42000000000001591615728102624416351318359375
# by repr(): Decimal('423.42000000000001591615728102624416351318359375')
binaryNumber = bin(25)  # by str(): 0b11001 by repr(): '0b11001'
fraction = Fraction(-8, 5)  # by str(): -8/5 by repr(): Fraction(-8, 5)
scientificNotation = '%.2E' % Decimal('40800000000.00000000000000')  # by str(): 4.08E+10 by repr(): '4.08E+10'

# types conversion

explicitConversionToRealNumber = 2 + 2.5
