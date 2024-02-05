# Physical constant
gravity = 9.8
elementary_charge = 1.602176634 * (10 ** -19)
planck = 6.62607015 * (10 ** -34)
electron_mass = 9.1093837015 * (10 ** -31)
light_speech = 299792458

# Chemical constant
avogadro = 602214076 * (10 ** 15)

# Mathematical constant
pi = 3.141592653589793
e = 2.718281828459045

# Series
power_series = ['x⁰', 'x¹', 'x²', 'x³', 'x⁴', 'x⁵', 'x⁶', 'x⁷', 'x⁸', 'x⁹', 'x¹⁰', 'x¹¹', 'x¹²', 'x¹³', 'x¹⁴', 'x¹⁵',
                'x¹⁶', 'x¹⁷', 'x¹⁸', 'x¹⁹', 'x²⁰', 'x²¹', 'x²²', 'x²³', 'x²⁴', 'x²⁵', 'x²⁶', 'x²⁷', 'x²⁸', 'x²⁹', 'x³⁰',
                'x³¹', 'x³²', 'x³³', 'x³⁴', 'x³⁵', 'x³⁶', 'x³⁷', 'x³⁸', 'x³⁹', 'x⁴⁰', 'x⁴¹', 'x⁴²', 'x⁴³', 'x⁴⁴', 'x⁴⁵',
                'x⁴⁶', 'x⁴⁷', 'x⁴⁸', 'x⁴⁹', 'x⁵⁰', 'x⁵¹', 'x⁵²', 'x⁵³', 'x⁵⁴', 'x⁵⁵', 'x⁵⁶', 'x⁵⁷', 'x⁵⁸', 'x⁵⁹', 'x⁶⁰',
                'x⁶¹', 'x⁶²', 'x⁶³', 'x⁶⁴', 'x⁶⁵', 'x⁶⁶', 'x⁶⁷', 'x⁶⁸', 'x⁶⁹', 'x⁷⁰', 'x⁷¹', 'x⁷²', 'x⁷³', 'x⁷⁴', 'x⁷⁵',
                'x⁷⁶', 'x⁷⁷', 'x⁷⁸', 'x⁷⁹', 'x⁸⁰', 'x⁸¹', 'x⁸²', 'x⁸³', 'x⁸⁴', 'x⁸⁵', 'x⁸⁶', 'x⁸⁷', 'x⁸⁸', 'x⁸⁹', 'x⁹⁰',
                'x⁹¹', 'x⁹²', 'x⁹³', 'x⁹⁴', 'x⁹⁵', 'x⁹⁶', 'x⁹⁷', 'x⁹⁸', 'x⁹⁹']
"""
power_series = []
base = "x"
n = 10

for power in range(0, n):
    superscript_power = str(power).translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
    power_series.append(f'{base}{superscript_power}')
print(power_series)
print(f'{1}{power_series[1]}')
"""

