#!/usr/bin/env python
# encoding: utf-8

name = "iBut-Sarathy"
shortDesc = u"/Users/pierreb/Code/RMG-models/iBut-Sarathy/thermo.txt"
longDesc = u"""

"""
entry(
    index = 1,
    label = "h2",
    molecule =
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34433,0.00798052,-1.94782e-05,2.01572e-08,-7.37612e-12,-917.935,0.68301], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.93287,0.000826608,-1.46402e-07,1.541e-11,-6.88805e-16,-813.066,-1.02433], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""tpis78""",
    longDesc =
u"""
tpis78.
[H][H]
Imported from thermo.txt.
""",
)

entry(
    index = 2,
    label = "co2",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35681,0.00898413,-7.12206e-06,2.4573e-09,-1.42885e-13,-48372,9.9009], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.63651,0.00274146,-9.95898e-07,1.60387e-10,-9.16199e-15,-49024.9,-1.9349], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""l 7/88""",
    longDesc =
u"""
l 7/88.
O=C=O
Imported from thermo.txt.
""",
)

entry(
    index = 3,
    label = "co",
    molecule =
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57953,-0.000610354,1.01681e-06,9.07006e-10,-9.04424e-13,-14344.1,3.50841], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.04849,0.00135173,-4.85794e-07,7.88536e-11,-4.69807e-15,-14266.1,6.0171], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""rus 79""",
    longDesc =
u"""
rus 79.
[C]=O
Imported from thermo.txt.
""",
)

entry(
    index = 4,
    label = "ch4",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.14911,-0.0136622,4.91454e-05,-4.84247e-08,1.66603e-11,-10246.6,-4.63849], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.65326,0.0100263,-3.31661e-06,5.36483e-10,-3.14697e-14,-10009.6,9.90506], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 8/99""",
    longDesc =
u"""
g 8/99.
C
Imported from thermo.txt.
""",
)

entry(
    index = 5,
    label = "c2h4",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9592,-0.00757051,5.7099e-05,-6.91588e-08,2.69884e-11,5089.78,4.0973], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.99183,0.0104834,-3.71721e-06,5.94628e-10,-3.5363e-14,4268.66,-0.269082], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 1/00""",
    longDesc =
u"""
g 1/00.
C=C
Imported from thermo.txt.
""",
)

entry(
    index = 6,
    label = "c2h2",
    molecule =
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.80868,0.0233616,-3.55172e-05,2.80153e-08,-8.50075e-12,26429,13.9397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.65878,0.00488397,-1.60829e-06,2.46975e-10,-1.38606e-14,25759.4,-3.99838], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 1/91""",
    longDesc =
u"""
g 1/91.
C#C
Imported from thermo.txt.
""",
)

entry(
    index = 7,
    label = "c2h6",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.29143,-0.00550155,5.99438e-05,-7.08466e-08,2.68686e-11,-11522.2,2.66679], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.04666,0.0153539,-5.47039e-06,8.77827e-10,-5.23168e-14,-12447.3,-0.968698], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 8/88""",
    longDesc =
u"""
g 8/88.
CC
Imported from thermo.txt.
""",
)

entry(
    index = 8,
    label = "c3h6",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83464,0.00329079,5.05228e-05,-6.66251e-08,2.63707e-11,788.717,7.53408], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.0387,0.0162964,-5.82131e-06,9.35937e-10,-5.58603e-14,-741.715,-8.43826], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 2/00""",
    longDesc =
u"""
g 2/00.
C=CC
Imported from thermo.txt.
""",
)

entry(
    index = 9,
    label = "c3h8",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.21093,0.00170887,7.0653e-05,-9.20061e-08,3.64618e-11,-14381.1,5.61004], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.6692,0.0206109,-7.36512e-06,1.18434e-09,-7.06915e-14,-16275.4,-13.1943], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 2/00""",
    longDesc =
u"""
g 2/00.
CCC
Imported from thermo.txt.
""",
)

entry(
    index = 10,
    label = "c3h4-a",
    molecule =
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61304,0.0121226,1.85399e-05,-3.45251e-08,1.53351e-11,21541.6,10.2261], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.31687,0.0111337,-3.96294e-06,6.35642e-10,-3.78755e-14,20117.5,-10.9958], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""l 8/89""",
    longDesc =
u"""
l 8/89.
C=C=C
Imported from thermo.txt.
""",
)

entry(
    index = 11,
    label = "ch3oh",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.65851,-0.0162983,6.91938e-05,-7.58373e-08,2.80428e-11,-25612,-0.897331], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.52727,0.0103179,-3.62893e-06,5.77448e-10,-3.42183e-14,-26002.9,5.16759], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t06/02""",
    longDesc =
u"""
t06/02.
CO
Imported from thermo.txt.
""",
)

entry(
    index = 12,
    label = "c4h8-1",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.13226,0.00533863,6.02929e-05,-7.60365e-08,2.87325e-11,-2167.18,3.82937], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.86795,0.0224449,-8.07705e-06,1.3018e-09,-7.77958e-14,-4238.53,-16.5663], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t05/09""",
    longDesc =
u"""
t05/09.
C=CCC
Imported from thermo.txt.
""",
)

entry(
    index = 13,
    label = "c4h6",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.112845,0.034369,-1.11074e-05,-9.21067e-09,6.20652e-12,11802.3,23.09], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.86731,0.0149187,-3.15487e-06,-4.18413e-10,1.57613e-13,9133.85,-23.3282], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""h6w/94""",
    longDesc =
u"""
h6w/94
c4h6              t05/04c  4 h  6    0    0 g   200.000  6000.00  1000.00      1
7.62637466e+00 1.72523403e-02-6.09184911e-06 9.70800102e-10-5.76169721e-14    2
9.55306395e+03-1.48325259e+01 4.10599669e+00 5.05575563e-03 5.83885454e-05    3
-8.05950198e-08 3.27447711e-11 1.15092468e+04 8.42978067e+00 1.33302095e+04    4

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC=C
Imported from thermo.txt.
""",
)

entry(
    index = 14,
    label = "c4h10",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.14474,0.0001645,9.67849e-05,-1.25486e-07,4.97846e-11,-17598.9,-1.08059], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.44548,0.0257857,-9.23613e-06,1.48632e-09,-8.87891e-14,-20138.4,-26.3478], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g12/00""",
    longDesc =
u"""
g12/00.
CCCC
Imported from thermo.txt.
""",
)

entry(
    index = 15,
    label = "c2h5oh",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.8587,-0.00374017,6.95554e-05,-8.86548e-08,3.51688e-11,-29996.1,4.80185], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.56244,0.0152042,-5.38968e-06,8.6225e-10,-5.12898e-14,-31525.6,-9.47302], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""l 8/88""",
    longDesc =
u"""
l 8/88.
CCO
Imported from thermo.txt.
""",
)

entry(
    index = 16,
    label = "c2h3",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36378,0.000265766,2.79621e-05,-3.72987e-08,1.5159e-11,34475,7.9151], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.15027,0.00754021,-2.62998e-06,4.15974e-10,-2.45408e-14,33856.6,1.72812], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""atct/a""",
    longDesc =
u"""
atct/a.
[CH]=C
Imported from thermo.txt.
""",
)

entry(
    index = 17,
    label = "ch2co",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.81423,0.0199009,-2.21416e-05,1.45029e-08,-3.98877e-12,-7053.95,13.6079], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.35869,0.00695642,-2.64803e-06,4.65068e-10,-3.08642e-14,-7902.94,-3.98526], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
ch2co             g 4/02c  2 h  2 o  1    0 g   200.000  6000.00  1000.00      1
5.75871449e+00 6.35124053e-03-2.25955361e-06 3.62321512e-10-2.15855515e-14    2
-8.08533464e+03-4.96490444e+00 2.13241136e+00 1.81319455e-02-1.74093315e-05    3
9.35336040e-09-2.01724844e-12-7.14808520e+03 1.33807969e+01-5.84267744e+03    4
Hf from Simmie&Metcalfe 2008, S and Cp from WKM b3lyp calculation

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C=O
Imported from thermo.txt.
""",
)

entry(
    index = 18,
    label = "ch3cho",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.72946,-0.00319329,4.75349e-05,-5.74586e-08,2.19311e-11,-21572.9,4.10302], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.40411,0.0117231,-4.22631e-06,6.83725e-10,-4.09849e-14,-22593.1,-3.48079], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""l 8/88""",
    longDesc =
u"""
l 8/88.
CC=O
Imported from thermo.txt.
""",
)

entry(
    index = 19,
    label = "h2o",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19864,-0.0020364,6.52034e-06,-5.48793e-09,1.77197e-12,-30293.7,-0.849009], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67704,0.00297318,-7.73769e-07,9.44335e-11,-4.269e-15,-29885.9,6.88255], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""l 5/89""",
    longDesc =
u"""
l 5/89.
O
Imported from thermo.txt.
""",
)

entry(
    index = 20,
    label = "ch2cho",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79503,0.0101099,1.61751e-05,-3.10303e-08,1.39436e-11,162.945,12.3647], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.53928,0.00780239,-2.76414e-06,4.42099e-10,-2.62954e-14,-1188.59,-8.72091], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t03/10""",
    longDesc =
u"""
t03/10.
C=C[O]
Imported from thermo.txt.
""",
)

entry(
    index = 21,
    label = "ch2o",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.79372,-0.00990833,3.7322e-05,-3.79285e-08,1.31773e-11,-14322.8,0.602798], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.16953,0.00619321,-2.25056e-06,3.65976e-10,-2.20149e-14,-14492.3,6.04208], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 8/88""",
    longDesc =
u"""
g 8/88.
C=O
Imported from thermo.txt.
""",
)

entry(
    index = 22,
    label = "c2h5",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3273,0.0176657,-6.14927e-06,-3.01143e-10,4.38618e-13,13428.4,17.1789], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[5.88784,0.0103077,-3.46844e-06,5.32499e-10,-3.06513e-14,11506.5,-8.49652], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 4/ 4 therm""",
    longDesc =
u"""
8/ 4/ 4 therm
c2h5              iu1/07c  2 h  5    0    0 g   200.000  6000.00  1000.00      1
4.32195633e+00 1.23930542e-02-4.39680960e-06 7.03519917e-10-4.18435239e-14    2
1.21759475e+04 1.71103809e-01 4.24185905e+00-3.56905235e-03 4.82667202e-05    3
-5.85401009e-08 2.25804514e-11 1.29690344e+04 4.44703782e+00 1.43965189e+04    4

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH2]
Imported from thermo.txt.
""",
)

entry(
    index = 23,
    label = "h",
    molecule =
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25473.7,-0.446683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25473.7,-0.446683], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""l 6/94""",
    longDesc =
u"""
l 6/94.
[H]
Imported from thermo.txt.
""",
)

entry(
    index = 24,
    label = "o",
    molecule =
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16827,-0.00327932,6.64306e-06,-6.12807e-09,2.11266e-12,29122.3,2.05193], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.54364,-2.73162e-05,-4.1903e-09,4.95482e-12,-4.79554e-16,29226,4.92229], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""l 1/90""",
    longDesc =
u"""
l 1/90.
[O]
Imported from thermo.txt.
""",
)

entry(
    index = 25,
    label = "o2",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78246,-0.00299673,9.8473e-06,-9.6813e-09,3.24373e-12,-1063.94,3.65768], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.66096,0.000656366,-1.4115e-07,2.05798e-11,-1.29913e-15,-1215.98,3.41536], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""rus 89""",
    longDesc =
u"""
rus 89.
[O][O]
Imported from thermo.txt.
""",
)

entry(
    index = 26,
    label = "oh",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99198,-0.00240107,4.61664e-06,-3.87916e-09,1.3632e-12,3368.9,-0.103998], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.83853,0.00110741,-2.94e-07,4.20699e-11,-2.4229e-15,3697.81,5.84495], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""iu3/03""",
    longDesc =
u"""
iu3/03.
[OH]
Imported from thermo.txt.
""",
)

entry(
    index = 27,
    label = "ho2",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3018,-0.00474912,2.11583e-05,-2.42764e-08,9.29225e-12,264.018,3.71666], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.17229,0.00188118,-3.46277e-07,1.94658e-11,1.76257e-16,31.0207,2.95768], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""t 1/09""",
    longDesc =
u"""
t 1/09.
[O]O
Imported from thermo.txt.
""",
)

entry(
    index = 28,
    label = "h2o2",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.31515,-0.000847391,1.76404e-05,-2.26763e-08,9.0895e-12,-17706.7,3.27373], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.57977,0.00405326,-1.29845e-06,1.98211e-10,-1.13969e-14,-18007.2,0.664971], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t 8/03""",
    longDesc =
u"""
t 8/03.
OO
Imported from thermo.txt.
""",
)

entry(
    index = 29,
    label = "c",
    molecule =
"""
multiplicity 3
1 C u2 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55424,-0.000321538,7.33792e-07,-7.32235e-10,2.66521e-13,85442.7,4.53131], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.60558,-0.000195934,1.06737e-07,-1.64239e-11,8.18706e-16,85411.7,4.19239], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""l 7/88""",
    longDesc =
u"""
l 7/88.
[C]
Imported from thermo.txt.
""",
)

entry(
    index = 30,
    label = "ch",
    molecule =
"""
multiplicity 4
1 C u3 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48976,0.000324322,-1.68998e-06,3.16284e-09,-1.40618e-12,70612.6,2.08428], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.52094,0.00176536,-4.61477e-07,5.92897e-11,-3.34745e-15,70946.8,7.40518], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""iu3/03""",
    longDesc =
u"""
iu3/03.
[CH]
Imported from thermo.txt.
""",
)

entry(
    index = 31,
    label = "ch2",
    molecule =
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71758,0.00127391,2.17347e-06,-3.48858e-09,1.65209e-12,45872.4,1.75298], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.14632,0.00303671,-9.96474e-07,1.50484e-10,-8.57336e-15,46041.3,4.72342], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""iu3/03""",
    longDesc =
u"""
iu3/03.
[CH2]
Imported from thermo.txt.
""",
)

entry(
    index = 32,
    label = "ch2(s)",
    molecule =
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19331,-0.00233105,8.15676e-06,-6.62986e-09,1.93233e-12,50366.2,-0.746734], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.13502,0.00289594,-8.16668e-07,1.13573e-10,-6.36263e-15,50504.1,4.06031], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""iu6/03""",
    longDesc =
u"""
iu6/03.
Duplicate of species ch2 (i.e. same molecular structure according to RMG)
[CH2]
Imported from thermo.txt.
""",
)

entry(
    index = 33,
    label = "ch3",
    molecule =
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65718,0.0021266,5.45839e-06,-6.6181e-09,2.46571e-12,16422.7,1.67354], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.97812,0.00579785,-1.97558e-06,3.07298e-10,-1.79174e-14,16509.5,4.72248], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""iu0702""",
    longDesc =
u"""
iu0702.
[CH3]
Imported from thermo.txt.
""",
)

entry(
    index = 34,
    label = "hco",
    molecule =
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.23755,-0.00332075,1.4003e-05,-1.3424e-08,4.37416e-12,3872.41,3.30835], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.92002,0.00252279,-6.71004e-07,1.05616e-10,-7.43798e-15,3653.43,3.58077], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t 5/03""",
    longDesc =
u"""
t 5/03.
[CH]=O
Imported from thermo.txt.
""",
)

entry(
    index = 35,
    label = "ch2oh",
    molecule =
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47834,-0.0013507,2.78485e-05,-3.64869e-08,1.47907e-11,-3500.73,3.30913], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.09314,0.00594761,-2.06497e-06,3.23008e-10,-1.88126e-14,-4034.1,-1.84691], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""iu2/03""",
    longDesc =
u"""
iu2/03.
[CH2]O
Imported from thermo.txt.
""",
)

entry(
    index = 36,
    label = "ch3o",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71181,-0.00280463,3.76551e-05,-4.73072e-08,1.86588e-11,1295.7,6.57241], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.75779,0.00744142,-2.69705e-06,4.38091e-10,-2.63537e-14,378.112,-1.9668], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""iu1/03""",
    longDesc =
u"""
iu1/03.
C[O]
Imported from thermo.txt.
""",
)

entry(
    index = 37,
    label = "c2h",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u1 p0 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89868,0.0132988,-2.80733e-05,2.89485e-08,-1.07502e-11,67061.6,6.18548], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.6627,0.00382492,-1.36633e-06,2.13455e-10,-1.23217e-14,67168.4,3.92206], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t 5/10""",
    longDesc =
u"""
t 5/10.
[C]#C
Imported from thermo.txt.
""",
)

entry(
    index = 38,
    label = "hcco",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {4,S}
2 C u0 p0 c0 {1,T} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87608,0.0221205,-3.58869e-05,3.05403e-08,-1.01281e-11,20163.4,13.6968], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.91479,0.00371409,-1.30137e-06,2.06473e-10,-1.21477e-14,19359.6,-5.50567], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t 4/09""",
    longDesc =
u"""
t 4/09.
C#C[O]
Imported from thermo.txt.
""",
)

entry(
    index = 39,
    label = "hccoh",
    molecule =
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.05541,0.0252003,-3.80822e-05,3.09891e-08,-9.898e-12,9768.72,12.2272], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.3751,0.00549429,-1.88137e-06,2.93804e-10,-1.71772e-14,8932.78,-8.24498], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t12/09""",
    longDesc =
u"""
t12/09.
C#CO
Imported from thermo.txt.
""",
)

entry(
    index = 40,
    label = "c3h5-a",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.36318,0.0198138,1.24971e-05,-3.33556e-08,1.58466e-11,19245.6,17.1732], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.50079,0.0143247,-5.67816e-06,1.10808e-09,-9.03639e-14,17482.4,-11.2431], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""pd5/98""",
    longDesc =
u"""
pd5/98
c3h5-a            t 9/96c  3 h  5    0    0 g   200.000  6000.00  1000.00      1
0.70094568e+01 0.13106629e-01-0.46533442e-05 0.74514323e-09-0.44350051e-13    2
0.16412909e+05-0.13946114e+02 0.14698036e+01 0.19034365e-01 0.14480425e-04    3
-0.35468652e-07 0.16647594e-10 0.18325831e+05 0.16724114e+02 0.19675772e+05    4
c3h5-t            t 6/96c  3 h  5    0    0 g   200.000  6000.00  1000.00      1
0.61101805e+01 0.14673395e-01-0.53676822e-05 0.86904932e-09-0.51932006e-13    2
0.25532442e+05-0.83555712e+01 0.25544033e+01 0.10986798e-01 0.30174305e-04    3
-0.47253568e-07 0.19771073e-10 0.27150242e+05 0.13207592e+02 0.28582707e+05    4
c3h5-s            a12/04c  3 h  5    0    0 g   200.000  6000.00  1000.00      1
6.05091412e+00 1.34052084e-02-4.73450586e-06 7.55380897e-10-4.48421084e-14    2
2.90860210e+04-6.73692060e+00 3.33277282e+00 1.06102499e-02 2.17559727e-05    3
-3.47145235e-08 1.44476835e-11 3.03404530e+04 9.78922358e+00 3.19361425e+04    4

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=C
Imported from thermo.txt.
""",
)

entry(
    index = 41,
    label = "n2",
    molecule =
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53101,-0.000123661,-5.02999e-07,2.43531e-09,-1.40881e-12,-1046.98,2.96747], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.95258,0.0013969,-4.92632e-07,7.8601e-11,-4.60755e-15,-923.949,5.87189], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 8/02""",
    longDesc =
u"""
g 8/02.
N#N
Imported from thermo.txt.
""",
)

entry(
    index = 42,
    label = "ar",
    molecule =
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 5/97""",
    longDesc =
u"""
g 5/97.
[Ar]
Imported from thermo.txt.
""",
)

entry(
    index = 43,
    label = "ch3co",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03587,0.000877295,3.071e-05,-3.92476e-08,1.52969e-11,-2682.07,7.86177], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.31372,0.00917378,-3.32204e-06,5.39475e-10,-3.24524e-14,-3645.04,-1.67576], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""iu2/03""",
    longDesc =
u"""
iu2/03.
C[C]=O
Imported from thermo.txt.
""",
)

entry(
    index = 44,
    label = "nc4h9oh",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.633228,0.0561201,-3.58349e-05,1.14386e-08,-1.42875e-12,-35065.8,31.7522], Tmin=(298,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[14.9263,0.0215141,-7.2862e-06,1.12363e-09,-6.48833e-14,-40608.1,-52.3687], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/12/ 9 therm""",
    longDesc =
u"""
2/12/ 9 therm
!!!
!!
!!
!!  added for mani butanol mech   !!!

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCO
Imported from thermo.txt.
""",
)

entry(
    index = 45,
    label = "c4h8oh-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {5,S} {13,S}
5  O u0 p2 c0 {4,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.992817,0.0509978,-3.43044e-05,1.19152e-08,-1.6798e-12,-13666.4,24.3356], Tmin=(298,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[14.8735,0.0190136,-6.42348e-06,9.88882e-10,-5.70318e-14,-18508.5,-50.3291], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/12/ 9 therm""",
    longDesc =
u"""
2/12/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]O
Imported from thermo.txt.
""",
)

entry(
    index = 46,
    label = "c4h8oh-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {2,S} {13,S}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2033,0.0440218,-2.12296e-05,3.03715e-09,3.72028e-13,-11862.2,26.5515], Tmin=(298,'K'), Tmax=(1503,'K')),
            NASAPolynomial(coeffs=[14.0357,0.0194173,-6.5023e-06,9.95482e-10,-5.72035e-14,-16763.1,-44.1163], Tmin=(1503,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/12/ 9 therm""",
    longDesc =
u"""
2/12/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CO
Imported from thermo.txt.
""",
)

entry(
    index = 47,
    label = "c4h8oh-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2033,0.0440218,-2.12296e-05,3.03715e-09,3.72028e-13,-11862.2,26.5515], Tmin=(298,'K'), Tmax=(1503,'K')),
            NASAPolynomial(coeffs=[14.0357,0.0194173,-6.5023e-06,9.95482e-10,-5.72035e-14,-16763.1,-44.1163], Tmin=(1503,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/12/ 9 therm""",
    longDesc =
u"""
2/12/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCO
Imported from thermo.txt.
""",
)

entry(
    index = 48,
    label = "c4h8oh-4",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.192787,0.0514524,-3.32585e-05,1.07551e-08,-1.36212e-12,-10465.7,30.0451], Tmin=(298,'K'), Tmax=(1406,'K')),
            NASAPolynomial(coeffs=[14.5279,0.0193383,-6.54321e-06,1.00844e-09,-5.82078e-14,-15540.5,-47.3601], Tmin=(1406,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/12/ 9 therm""",
    longDesc =
u"""
2/12/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCO
Imported from thermo.txt.
""",
)

entry(
    index = 49,
    label = "pc4h9o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.61811,0.00213096,0.000102736,-1.34294e-07,5.2667e-11,-9214.2,5.86105], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.1282,0.0243645,-9.02472e-06,1.4795e-09,-8.93697e-14,-12979.6,-37.5313], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t09/08""",
    longDesc =
u"""
t09/08.
CCCC[O]
Imported from thermo.txt.
""",
)

entry(
    index = 50,
    label = "c4h6oh1-32",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,D} {4,S} {5,S}
3  C u0 p0 c0 {1,S} {2,D} {9,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.546057,0.045853,-3.19247e-05,1.15775e-08,-1.7212e-12,-2695.75,25.4487], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[13.2534,0.0161728,-5.45337e-06,8.38722e-10,-4.83473e-14,-7097.74,-42.7798], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""12/22/8 therm""",
    longDesc =
u"""
12/22/8 therm

Added by mani for modified mechanism

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(O)=CC
Imported from thermo.txt.
""",
)

entry(
    index = 51,
    label = "c4h7oh1-1",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.18168,0.0597646,-5.14757e-05,2.34495e-08,-4.3043e-12,-23141.7,31.28], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[14.4613,0.0171472,-5.75989e-06,8.83304e-10,-5.08054e-14,-27994.2,-50.6229], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/ 9/ 9 therm""",
    longDesc =
u"""
1/ 9/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CO
Imported from thermo.txt.
""",
)

entry(
    index = 52,
    label = "c4h6oh1-13",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u1 p0 c0 {3,S} {5,S} {11,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.44169,0.0577093,-5.03763e-05,2.29681e-08,-4.19598e-12,-5065.15,31.4119], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[14.0552,0.0154544,-5.196e-06,7.97457e-10,-4.58973e-14,-9847.32,-49.6781], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/ 9/ 9 thrm""",
    longDesc =
u"""
1/ 9/ 9 thrm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C[CH]O
Imported from thermo.txt.
""",
)

entry(
    index = 53,
    label = "c4h5oh-13",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {5,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.78823,0.0621535,-6.31374e-05,3.2178e-08,-6.33964e-12,-9819.72,31.6908], Tmin=(298,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[14.2093,0.01286,-4.31562e-06,6.61231e-10,-3.80037e-14,-14220.4,-50.0577], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/ 9/ 9 therm""",
    longDesc =
u"""
1/ 9/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC=CO
Imported from thermo.txt.
""",
)

entry(
    index = 54,
    label = "c4h7oh2-1",
    molecule =
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.64307,0.0405262,-2.08714e-05,4.42297e-09,-1.58661e-13,-21038.4,21.2411], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[12.8147,0.0186084,-6.28026e-06,9.66423e-10,-5.57277e-14,-25336.4,-40.2405], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""12/22/ 8 therm""",
    longDesc =
u"""
12/22/ 8 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCO
Imported from thermo.txt.
""",
)

entry(
    index = 55,
    label = "c4h7oh1-4",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.501376,0.0512577,-3.59905e-05,1.31423e-08,-1.96123e-12,-19988.8,31.6484], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[13.6752,0.0179085,-6.04472e-06,9.30196e-10,-5.36379e-14,-24867.6,-44.3698], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""12/22/ 8 therm""",
    longDesc =
u"""
12/22/ 8 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCO
Imported from thermo.txt.
""",
)

entry(
    index = 56,
    label = "sc4h9oh",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.314971,0.0554805,-3.42666e-05,9.72621e-09,-9.0456e-13,-37241.6,29.2788], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[16.1287,0.0196313,-6.46854e-06,9.80179e-10,-5.59418e-14,-43069.5,-59.7112], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 57,
    label = "sc4h8ohm",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.27642,0.0458145,-2.16702e-05,2.18504e-09,7.16497e-13,-12018.7,24.3183], Tmin=(298,'K'), Tmax=(1486,'K')),
            NASAPolynomial(coeffs=[16.2324,0.0177621,-5.98899e-06,9.22205e-10,-5.32395e-14,-17767.7,-58.2256], Tmin=(1486,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(O)CC
Imported from thermo.txt.
""",
)

entry(
    index = 58,
    label = "sc4h8oh-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {5,S}
5  O u0 p2 c0 {4,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69661,0.0396411,-1.59801e-05,1.23395e-10,9.71729e-13,-16743.5,18.3605], Tmin=(298,'K'), Tmax=(1484,'K')),
            NASAPolynomial(coeffs=[14.6215,0.0185849,-6.15342e-06,9.35523e-10,-5.35176e-14,-21468.3,-47.9355], Tmin=(1484,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[C](C)O
Imported from thermo.txt.
""",
)

entry(
    index = 59,
    label = "sc4h8oh-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.04565,0.0572423,-4.43109e-05,1.80945e-08,-3.02843e-12,-12569.8,35.5278], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.8422,0.0178436,-6.16709e-06,1.00443e-09,-6.10698e-14,-17869.5,-49.0082], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 60,
    label = "sc4h8oh-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.27642,0.0458145,-2.16702e-05,2.18504e-09,7.16497e-13,-12723.3,24.3183], Tmin=(298,'K'), Tmax=(1486,'K')),
            NASAPolynomial(coeffs=[16.2324,0.0177621,-5.98899e-06,9.22205e-10,-5.32395e-14,-18472.3,-58.2256], Tmin=(1486,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 61,
    label = "sc4h9o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.43663,0.010029,8.56583e-05,-1.18678e-07,4.74412e-11,-10713.4,8.21507], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.3515,0.024007,-8.828e-06,1.44359e-09,-8.71115e-14,-14646.6,-41.3525], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""a09/04""",
    longDesc =
u"""
a09/04.
CCC(C)[O]
Imported from thermo.txt.
""",
)

entry(
    index = 62,
    label = "tc4h9oh",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.61681,0.0593246,-4.28641e-05,1.65888e-08,-2.67494e-12,-39760.5,26.886], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[15.1649,0.021315,-7.21751e-06,1.11284e-09,-6.42499e-14,-45155.3,-57.5127], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 63,
    label = "tc4h8oh",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.151512,0.0547779,-4.03996e-05,1.59609e-08,-2.61959e-12,-13738.6,26.5782], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[14.7376,0.0191807,-6.49228e-06,1.00076e-09,-5.77691e-14,-18675.5,-51.2562], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 64,
    label = "ic4h9oh",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.837465,0.0576521,-3.90215e-05,1.40131e-08,-2.11159e-12,-36126.6,31.1702], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[14.7423,0.0219844,-7.51584e-06,1.16633e-09,-6.76422e-14,-41661.7,-52.8466], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)CO
Imported from thermo.txt.
""",
)

entry(
    index = 65,
    label = "ic4h8oh-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {5,S} {13,S}
5  O u0 p2 c0 {4,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.533515,0.0534789,-3.86599e-05,1.51267e-08,-2.49241e-12,-14684.2,24.9705], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[14.7535,0.0194562,-6.64962e-06,1.03168e-09,-5.98231e-14,-19608.3,-51.2243], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)[CH]O
Imported from thermo.txt.
""",
)

entry(
    index = 66,
    label = "ic4h8oh-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0498328,0.0530374,-3.64646e-05,1.33332e-08,-2.04587e-12,-13278.7,28.5747], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[14.3193,0.0198485,-6.79059e-06,1.05431e-09,-6.11666e-14,-18354.4,-48.8096], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)CO
Imported from thermo.txt.
""",
)

entry(
    index = 67,
    label = "ic4h8oh-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0498328,0.0530374,-3.64646e-05,1.33332e-08,-2.04587e-12,-11517.3,29.6718], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[14.3193,0.0198485,-6.79059e-06,1.05431e-09,-6.11666e-14,-16593,-47.7125], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)CO
Imported from thermo.txt.
""",
)

entry(
    index = 68,
    label = "ic4h9o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  O u1 p2 c0 {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80297,0.0156874,6.81105e-05,-9.83347e-08,3.95262e-11,-10083.2,9.78963], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.631,0.0247982,-9.01551e-06,1.46715e-09,-8.83215e-14,-13785.5,-38.1956], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""a08/04""",
    longDesc =
u"""
a08/04.
CC(C)C[O]
Imported from thermo.txt.
""",
)

entry(
    index = 69,
    label = "ic3h6oh",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0816697,0.0434237,-3.40695e-05,1.40357e-08,-2.36274e-12,-9138.5,26.8606], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[12.1111,0.0133516,-4.7147e-06,7.86163e-10,-4.86392e-14,-13123.2,-37.0535], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 70,
    label = "c3h6oh-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {4,S} {10,S}
4  O u0 p2 c0 {3,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.31781,0.0385018,-2.61359e-05,9.39955e-09,-1.40537e-12,-10945,21.1274], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[11.4914,0.0148557,-5.02888e-06,7.75158e-10,-4.47423e-14,-14501.5,-33.5713], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]O
Imported from thermo.txt.
""",
)

entry(
    index = 71,
    label = "c4h7oh2-2",
    molecule =
"""
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.732341,0.0615686,-5.61186e-05,2.68939e-08,-5.12983e-12,-26688.1,26.2559], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[14.8693,0.0168754,-5.67925e-06,8.71819e-10,-5.0173e-14,-31338.5,-54.7028], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11/23/ 9 therm""",
    longDesc =
u"""
11/23/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 72,
    label = "c4h7oh1-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.22861,0.069133,-6.68957e-05,3.31871e-08,-6.44724e-12,-25050.4,33.5657], Tmin=(298,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[15.4923,0.0163665,-5.50846e-06,8.4567e-10,-4.86717e-14,-30119.4,-57.6588], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11/23/ 9 therm""",
    longDesc =
u"""
11/23/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(O)CC
Imported from thermo.txt.
""",
)

entry(
    index = 73,
    label = "c4h7oh1-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.81269,0.0594831,-4.83144e-05,2.02853e-08,-3.42393e-12,-21347.6,35.6753], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[15.0127,0.0162207,-5.35573e-06,8.12678e-10,-4.64265e-14,-26730.4,-53.177], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11/23/ 9 therm""",
    longDesc =
u"""
11/23/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 74,
    label = "ch3chchoh",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0353977,0.0434969,-3.7448e-05,1.70906e-08,-3.13775e-12,-20250.3,24.1528], Tmin=(298,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[11.1222,0.0127745,-4.25316e-06,6.48216e-10,-3.71191e-14,-23669.1,-34.1335], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/ 3/ 9""",
    longDesc =
u"""
2/ 3/ 9
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CO
Imported from thermo.txt.
""",
)

entry(
    index = 75,
    label = "c3h6oh-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.38219,0.0322642,-1.3982e-05,9.59442e-10,5.73234e-13,-7990.5,23.9928], Tmin=(298,'K'), Tmax=(1530,'K')),
            NASAPolynomial(coeffs=[10.8612,0.0149944,-4.99957e-06,7.63353e-10,-4.37872e-14,-11700.6,-28.5286], Tmin=(1530,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/15/10 therm""",
    longDesc =
u"""
5/15/10 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CO
Imported from thermo.txt.
""",
)

entry(
    index = 76,
    label = "c3h5oh",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15012,0.0128538,4.28438e-05,-6.67819e-08,2.80408e-11,-16641.4,13.5066], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.72477,0.0163943,-5.90853e-06,9.53262e-10,-5.70318e-14,-19049.7,-19.7199], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t06/10""",
    longDesc =
u"""
t06/10.
C=CCO
Imported from thermo.txt.
""",
)

entry(
    index = 77,
    label = "ic3h6choh",
    molecule =
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.483554,0.0537594,-4.38037e-05,1.92102e-08,-3.44527e-12,-25559.9,22.2004], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[14.3069,0.0172823,-5.80601e-06,8.90344e-10,-5.12055e-14,-29976.8,-50.6124], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11/23/ 9 therm""",
    longDesc =
u"""
11/23/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)=CO
Imported from thermo.txt.
""",
)

entry(
    index = 78,
    label = "ic3h5ch2oh",
    molecule =
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.78075,0.0426831,-2.52897e-05,7.50851e-09,-8.8242e-13,-21851.7,19.4105], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[13.2472,0.0183544,-6.21538e-06,9.58477e-10,-5.53477e-14,-26108.2,-43.091], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11/23/9 therm""",
    longDesc =
u"""
11/23/9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)CO
Imported from thermo.txt.
""",
)

entry(
    index = 79,
    label = "c4h8oh-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {16,S}
6  O u0 p2 c0 {3,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61861,0.0568332,-4.12487e-05,1.60925e-08,-2.63257e-12,-35510.6,15.03], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[18.9121,0.0202526,-6.94226e-06,1.07922e-09,-6.26652e-14,-40797,-66.9029], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 5/11 therm""",
    longDesc =
u"""
5/ 5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(O)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 80,
    label = "c4h8oh-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {3,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89779,0.056072,-3.90996e-05,1.47175e-08,-2.34863e-12,-31881.2,19.5266], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[17.9101,0.0211247,-7.24788e-06,1.12743e-09,-6.5493e-14,-37187.8,-61.277], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 5/11 therm""",
    longDesc =
u"""
5/ 5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 81,
    label = "c4h8oh-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {3,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89779,0.056072,-3.90996e-05,1.47175e-08,-2.34863e-12,-31881.2,19.5266], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[17.9101,0.0211247,-7.24788e-06,1.12743e-09,-6.5493e-14,-37187.8,-61.277], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 5/11 therm""",
    longDesc =
u"""
5/ 5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 82,
    label = "c4h8oh-4o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  O u0 p2 c0 {4,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77317,0.0509447,-3.11985e-05,9.92964e-09,-1.3292e-12,-30233.8,17.166], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[17.5586,0.0215199,-7.40583e-06,1.15436e-09,-6.71542e-14,-35389.3,-58.0067], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCCCO
Imported from thermo.txt.
""",
)

entry(
    index = 83,
    label = "c4h7oh-1ooh-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71801,0.0566057,-3.89366e-05,1.36468e-08,-1.93331e-12,-29028.7,17.2622], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[19.9606,0.0193792,-6.64705e-06,1.03395e-09,-6.00687e-14,-34722,-70.1919], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]C(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 84,
    label = "c4h7oh-1ooh-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71801,0.0566057,-3.89366e-05,1.36468e-08,-1.93331e-12,-29028.7,17.2622], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[19.9606,0.0193792,-6.64705e-06,1.03395e-09,-6.00687e-14,-34722,-70.1919], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CC(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 85,
    label = "c4h7oh-1ooh-4",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C u1 p0 c0 {3,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.11212,0.0625689,-4.94225e-05,2.05292e-08,-3.48601e-12,-27699.7,18.8264], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[20.458,0.0189141,-6.47616e-06,1.00611e-09,-5.83971e-14,-33420.7,-73.2367], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 86,
    label = "c4h7oh-2ooh-4",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66799,0.0607031,-4.56569e-05,1.8118e-08,-2.96349e-12,-24116,22.0127], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[19.4831,0.0197022,-6.73956e-06,1.04636e-09,-6.07075e-14,-29799.5,-67.7107], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/11 therm""",
    longDesc =
u"""
5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(CO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 87,
    label = "c4h7oh-2ooh-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87545,0.0564466,-3.71202e-05,1.17976e-08,-1.40575e-12,-25386,22.2914], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.8248,0.0186203,-6.21191e-06,9.49492e-10,-5.45276e-14,-31351,-69.2022], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C(CO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 88,
    label = "c4h7oh-2ooh-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {6,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87545,0.0564466,-3.71202e-05,1.17976e-08,-1.40575e-12,-25386,22.2914], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.8248,0.0186203,-6.21191e-06,9.49492e-10,-5.45276e-14,-31351,-69.2022], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC([CH]O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 89,
    label = "c4h7oh-3ooh-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {6,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87545,0.0564466,-3.71202e-05,1.17976e-08,-1.40575e-12,-25386,22.2914], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.8248,0.0186203,-6.21191e-06,9.49492e-10,-5.45276e-14,-31351,-69.2022], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C[CH]O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 90,
    label = "c4h7oh-3ooh-4",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66799,0.0607031,-4.56569e-05,1.8118e-08,-2.96349e-12,-24116,22.0127], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[19.4831,0.0197022,-6.73956e-06,1.04636e-09,-6.07075e-14,-29799.5,-67.7107], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/11 therm""",
    longDesc =
u"""
5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(CCO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 91,
    label = "c4h7oh-3ooh-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87545,0.0564466,-3.71202e-05,1.17976e-08,-1.40575e-12,-25386,22.2914], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.8248,0.0186203,-6.21191e-06,9.49492e-10,-5.45276e-14,-31351,-69.2022], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC([CH]CO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 92,
    label = "c4h7oh-4ooh-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27401,0.0530234,-3.10154e-05,7.83177e-09,-5.27518e-13,-23657.9,22.2123], Tmin=(298,'K'), Tmax=(1375,'K')),
            NASAPolynomial(coeffs=[19.6563,0.0189502,-6.3665e-06,9.77839e-10,-5.63478e-14,-29671.1,-67.1013], Tmin=(1375,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OCC[CH]COO
Imported from thermo.txt.
""",
)

entry(
    index = 93,
    label = "c4h7oh-4ooh-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27401,0.0530234,-3.10154e-05,7.83177e-09,-5.27518e-13,-23657.9,22.2123], Tmin=(298,'K'), Tmax=(1375,'K')),
            NASAPolynomial(coeffs=[19.6563,0.0189502,-6.3665e-06,9.77839e-10,-5.63478e-14,-29671.1,-67.1013], Tmin=(1375,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OC[CH]CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 94,
    label = "c4h7oh-4ooh-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {6,S} {14,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27401,0.0530234,-3.10154e-05,7.83177e-09,-5.27518e-13,-23657.9,22.2123], Tmin=(298,'K'), Tmax=(1375,'K')),
            NASAPolynomial(coeffs=[19.6563,0.0189502,-6.3665e-06,9.77839e-10,-5.63478e-14,-29671.1,-67.1013], Tmin=(1375,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O[CH]CCCOO
Imported from thermo.txt.
""",
)

entry(
    index = 95,
    label = "c4h7oh-1ooh-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {8,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.24254,0.0695694,-5.69274e-05,2.43581e-08,-4.2341e-12,-48843.6,11.0773], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[24.7055,0.0196542,-6.75423e-06,1.05192e-09,-6.11636e-14,-55171.8,-91.8953], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(O[O])C(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 96,
    label = "c4h7oh-1ooh-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {8,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.24254,0.0695694,-5.69274e-05,2.43581e-08,-4.2341e-12,-48843.6,11.0773], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[24.7055,0.0196542,-6.75423e-06,1.05192e-09,-6.11636e-14,-55171.8,-91.8953], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CC(O)OO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 97,
    label = "c4h7oh-1ooh-4o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {8,S}
6  O u0 p2 c0 {3,S} {17,S}
7  O u0 p2 c0 {4,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.95731,0.0650835,-4.9939e-05,2.01269e-08,-3.33682e-12,-47169.8,9.47647], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[24.3473,0.0200694,-6.92223e-06,1.08074e-09,-6.29468e-14,-53377.6,-88.6046], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCCC(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 98,
    label = "c4h7oh-2ooh-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {7,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {3,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.24254,0.0695694,-5.69274e-05,2.43581e-08,-4.2341e-12,-48843.6,11.0773], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[24.7055,0.0196542,-6.75423e-06,1.05192e-09,-6.11636e-14,-55171.8,-91.8953], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(OO)C(O)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 99,
    label = "c4h7oh-2ooh-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.75209,0.0678608,-5.34337e-05,2.21853e-08,-3.78003e-12,-45251.1,14.4907], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[23.6719,0.0205751,-7.08127e-06,1.10393e-09,-6.42301e-14,-51546.3,-86.0807], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O[O])C(CO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 100,
    label = "c4h7oh-2ooh-4o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {4,S} {16,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.609,0.0628059,-4.56336e-05,1.74592e-08,-2.77429e-12,-43600.7,12.2178], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.3188,0.0209757,-7.24198e-06,1.13138e-09,-6.5925e-14,-49748.3,-82.8042], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCC(CO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 101,
    label = "c4h7oh-3ooh-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {3,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.24254,0.0695694,-5.69274e-05,2.43581e-08,-4.2341e-12,-48843.6,11.0773], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[24.7055,0.0196542,-6.75423e-06,1.05192e-09,-6.11636e-14,-55171.8,-91.8953], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CC(O)O[O])OO
Imported from thermo.txt.
""",
)

entry(
    index = 102,
    label = "c4h7oh-3ooh-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.75209,0.0678608,-5.34337e-05,2.21853e-08,-3.78003e-12,-45251.1,14.4907], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[23.6719,0.0205751,-7.08127e-06,1.10393e-09,-6.42301e-14,-51546.3,-86.0807], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(OO)C(CO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 103,
    label = "c4h7oh-3ooh-4o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {4,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.609,0.0628059,-4.56336e-05,1.74592e-08,-2.77429e-12,-43600.7,12.2178], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.3188,0.0209757,-7.24198e-06,1.13138e-09,-6.5925e-14,-49748.3,-82.8042], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCC(CCO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 104,
    label = "c4h7oh-4ooh-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {7,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
5  O u0 p2 c0 {4,S} {8,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.95731,0.0650835,-4.9939e-05,2.01269e-08,-3.33682e-12,-47169.8,9.47647], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[24.3473,0.0200694,-6.92223e-06,1.08074e-09,-6.29468e-14,-53377.6,-88.6046], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OC(O)CCCOO
Imported from thermo.txt.
""",
)

entry(
    index = 105,
    label = "c4h7oh-4ooh-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
5  O u0 p2 c0 {4,S} {8,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.609,0.0628059,-4.56336e-05,1.74592e-08,-2.77429e-12,-43600.7,12.2178], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.3188,0.0209757,-7.24198e-06,1.13138e-09,-6.5925e-14,-49748.3,-82.8042], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OC(CO)CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 106,
    label = "c4h7oh-4ooh-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {8,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {4,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.609,0.0628059,-4.56336e-05,1.74592e-08,-2.77429e-12,-43600.7,12.2178], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.3188,0.0209757,-7.24198e-06,1.13138e-09,-6.5925e-14,-49748.3,-82.8042], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OC(CCO)COO
Imported from thermo.txt.
""",
)

entry(
    index = 107,
    label = "c4ohket1-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {14,D}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0852653,0.077694,-6.89792e-05,3.10732e-08,-5.56679e-12,-71352.8,28.2412], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[22.687,0.0172992,-5.98355e-06,9.36157e-10,-5.46125e-14,-78413.8,-90.4022], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(OO)C(=O)O
Imported from thermo.txt.
""",
)

entry(
    index = 108,
    label = "c4ohket1-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,D}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.52579,0.0670741,-5.57888e-05,2.42518e-08,-4.28226e-12,-72829.3,17.5174], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[21.5061,0.0182242,-6.28434e-06,9.81118e-10,-5.71472e-14,-79004.5,-82.8778], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CC(=O)O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 109,
    label = "c4ohket1-4",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,D}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40309,0.0619468,-4.78938e-05,1.94727e-08,-3.2657e-12,-71182.5,15.1461], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[21.1521,0.018627,-6.44609e-06,1.00876e-09,-5.88537e-14,-77205.4,-79.5948], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C(O)CCCOO
Imported from thermo.txt.
""",
)

entry(
    index = 110,
    label = "c4ohket2-1",
    molecule =
"""
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {2,S} {14,D}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.69717,0.0590263,-4.52485e-05,1.83435e-08,-3.07503e-12,-66165.3,11.8723], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[21.2925,0.0184855,-6.39052e-06,9.99235e-10,-5.82604e-14,-71798.3,-76.7045], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(=O)C(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 111,
    label = "c4ohket2-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.45736,0.0947202,-9.37479e-05,4.64802e-08,-8.99314e-12,-58713.1,55.1971], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[21.9367,0.0180406,-6.26171e-06,9.81856e-10,-5.7364e-14,-66454.7,-81.3588], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(OO)C(=O)CO
Imported from thermo.txt.
""",
)

entry(
    index = 112,
    label = "c4ohket2-4",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.951453,0.0781774,-7.16125e-05,3.43461e-08,-6.59816e-12,-58571.8,41.2254], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[20.3289,0.0195152,-6.79335e-06,1.06714e-09,-6.24204e-14,-65232.2,-70.1674], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C(CO)CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 113,
    label = "c4ohket3-1",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.69717,0.0590263,-4.52485e-05,1.83435e-08,-3.07503e-12,-66104.9,11.8723], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[21.2925,0.0184855,-6.39052e-06,9.99235e-10,-5.82604e-14,-71737.9,-76.7045], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)CC(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 114,
    label = "c4ohket3-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.13949,0.0706039,-5.86386e-05,2.50476e-08,-4.31329e-12,-60938.8,28.9322], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[21.6548,0.0180944,-6.23992e-06,9.74312e-10,-5.6759e-14,-67586.8,-79.5918], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)C(CO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 115,
    label = "c4ohket3-4",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.51407,0.0707102,-6.09595e-05,2.7313e-08,-4.92725e-12,-58905,28.6322], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[21.3468,0.0182026,-6.24296e-06,9.71183e-10,-5.64299e-14,-65201.5,-75.7364], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C(CCO)COO
Imported from thermo.txt.
""",
)

entry(
    index = 116,
    label = "c4ohket4-1",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {13,D} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.16735,0.0588905,-4.59621e-05,1.89634e-08,-3.22083e-12,-62484.6,9.80401], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[21.5778,0.0181482,-6.25278e-06,9.75476e-10,-5.67846e-14,-67980.3,-77.5385], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CCCC(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 117,
    label = "c4ohket4-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05634,0.05968,-4.56588e-05,1.83349e-08,-3.02426e-12,-58792.8,16.137], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[20.963,0.0182984,-6.22814e-06,9.6412e-10,-5.58336e-14,-64484.3,-74.0092], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CCC(CO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 118,
    label = "c4ohket4-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.47178,0.0708975,-5.964e-05,2.55727e-08,-4.3867e-12,-57293.7,27.535], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[22.207,0.0172661,-5.87916e-06,9.10526e-10,-5.2753e-14,-63913.9,-81.8822], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/5/11 therm""",
    longDesc =
u"""
5/5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CC(CCO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 119,
    label = "c4h7oho1-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.01747,0.0656146,-5.08423e-05,1.98532e-08,-3.09581e-12,-38440.9,36.0001], Tmin=(298,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[17.6144,0.0176039,-6.04917e-06,9.42341e-10,-5.481e-14,-44954.8,-68.523], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/6/11 therm""",
    longDesc =
u"""
5/6/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1CC(O)O1
Imported from thermo.txt.
""",
)

entry(
    index = 120,
    label = "c4h7oho1-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.34051,0.0674933,-5.25481e-05,2.09908e-08,-3.38682e-12,-38992.7,41.7712], Tmin=(298,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[16.2428,0.0191411,-6.56649e-06,1.02164e-09,-5.93649e-14,-45482.8,-62.3943], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/6/11 therm""",
    longDesc =
u"""
5/6/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species c4h7oho1-2 (i.e. same molecular structure according to RMG)
CC1CC(O)O1
Imported from thermo.txt.
""",
)

entry(
    index = 121,
    label = "c4h7oho1-4",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.33895,0.0658008,-4.69211e-05,1.67038e-08,-2.35942e-12,-46542.7,47.7301], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[15.3975,0.0199868,-6.88757e-06,1.0749e-09,-6.25967e-14,-53353.9,-58.2489], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/6/11 therm""",
    longDesc =
u"""
5/6/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OC1CCCO1
Imported from thermo.txt.
""",
)

entry(
    index = 122,
    label = "c4h7oho2-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.50126,0.0676404,-5.65916e-05,2.46417e-08,-4.3262e-12,-35511.4,39.0979], Tmin=(298,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[16.2166,0.0185631,-6.32654e-06,9.79819e-10,-5.67491e-14,-41463.9,-59.5074], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/6/11 therm""",
    longDesc =
u"""
5/6/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1OC1CO
Imported from thermo.txt.
""",
)

entry(
    index = 123,
    label = "c4h7oho2-4",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.6021,0.0656886,-5.03737e-05,2.01541e-08,-3.29036e-12,-33819.4,45.4415], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[14.8299,0.0202137,-6.90692e-06,1.07159e-09,-6.21414e-14,-39962,-52.6629], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/6/11 therm""",
    longDesc =
u"""
5/6/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OCC1CCO1
Imported from thermo.txt.
""",
)

entry(
    index = 124,
    label = "c4h7oho3-4",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.16844,0.0641214,-5.09793e-05,2.12995e-08,-3.633e-12,-33298.2,39.0311], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[15.6003,0.0191959,-6.56866e-06,1.02007e-09,-5.91908e-14,-39136.2,-55.1996], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/6/11 therm""",
    longDesc =
u"""
5/6/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OCCC1CO1
Imported from thermo.txt.
""",
)

entry(
    index = 125,
    label = "c4h8oh-1o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.75612,0.067286,-4.71674e-05,1.62375e-08,-2.18438e-12,-52177.4,23.3649], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[22.4306,0.0200916,-6.95452e-06,1.08867e-09,-6.35359e-14,-59384.9,-87.9227], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/11 therm""",
    longDesc =
u"""
5/11 therm

Added for mani low T mech (apr 28)

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 126,
    label = "c4h8oh-2o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.88752,0.0653048,-4.82018e-05,1.8788e-08,-3.02614e-12,-48726.9,23.4786], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[19.9115,0.0218266,-7.45937e-06,1.15739e-09,-6.71188e-14,-54868,-72.8646], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/11 therm""",
    longDesc =
u"""
5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 127,
    label = "c4h8oh-3o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.88752,0.0653048,-4.82018e-05,1.8788e-08,-3.02614e-12,-48726.9,23.4786], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[19.9115,0.0218266,-7.45937e-06,1.15739e-09,-6.71188e-14,-54868,-72.8646], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/11 therm""",
    longDesc =
u"""
5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 128,
    label = "c4h8oh-4o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {4,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.75594,0.0602185,-4.03722e-05,1.4052e-08,-2.01954e-12,-47078.8,21.1482], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[19.5531,0.0222362,-7.62401e-06,1.18553e-09,-6.88564e-14,-53067.1,-69.5573], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/11 therm""",
    longDesc =
u"""
5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OCCCCOO
Imported from thermo.txt.
""",
)

entry(
    index = 129,
    label = "c4h8oh-1o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 O u1 p2 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.01831,0.0576337,-3.95938e-05,1.37265e-08,-1.91369e-12,-32687.6,24.7968], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[17.9799,0.0191216,-6.59971e-06,1.03096e-09,-6.00743e-14,-38671.7,-66.6622], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 5/11 therm""",
    longDesc =
u"""
5/ 5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC([O])O
Imported from thermo.txt.
""",
)

entry(
    index = 130,
    label = "c4h8oh-2o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.322902,0.0596523,-4.41961e-05,1.74297e-08,-2.86189e-12,-29702.8,29.0606], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[16.7892,0.0200395,-6.89348e-06,1.07426e-09,-6.24869e-14,-35358,-59.0525], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 5/11 therm""",
    longDesc =
u"""
5/ 5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC([O])CO
Imported from thermo.txt.
""",
)

entry(
    index = 131,
    label = "c4h8oh-3o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  O u1 p2 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.322902,0.0596523,-4.41961e-05,1.74297e-08,-2.86189e-12,-29702.8,29.0606], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[16.7892,0.0200395,-6.89348e-06,1.07426e-09,-6.24869e-14,-35358,-59.0525], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 5/11 therm""",
    longDesc =
u"""
5/ 5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC([O])CCO
Imported from thermo.txt.
""",
)

entry(
    index = 132,
    label = "c4h8oh-4o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.60162,0.0563612,-3.86672e-05,1.38719e-08,-2.06647e-12,-27482.5,29.2394], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[16.4248,0.0201734,-6.90353e-06,1.07228e-09,-6.22346e-14,-33087.1,-56.0701], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 5/11 therm""",
    longDesc =
u"""
5/ 5/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]CCCCO
Imported from thermo.txt.
""",
)

entry(
    index = 133,
    label = "hoch2cho",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.850564,0.0352163,-2.95845e-05,1.34558e-08,-2.51908e-12,-37452.1,32.86], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[8.56649,0.0106729,-3.70802e-06,5.8167e-10,-3.3989e-14,-40560.6,-16.9686], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 6/11 therm""",
    longDesc =
u"""
5/ 6/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CCO
Imported from thermo.txt.
""",
)

entry(
    index = 134,
    label = "hoch2co",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,D}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.049991,0.0293806,-2.49753e-05,1.14315e-08,-2.14545e-12,-18927.4,29.8449], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[7.96737,0.0086303,-3.00259e-06,4.71462e-10,-2.75678e-14,-21526.3,-12.0025], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 6/11 therm""",
    longDesc =
u"""
5/ 6/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=[C]CO
Imported from thermo.txt.
""",
)

entry(
    index = 135,
    label = "hoc2h4cho",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  O u0 p2 c0 {2,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.71184,0.0342801,-2.0644e-05,6.25585e-09,-7.60656e-13,-42574.5,17.1499], Tmin=(298,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[12.2895,0.0139824,-4.69687e-06,7.21075e-10,-4.15306e-14,-46135.8,-35.0722], Tmin=(1377,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 6/11 therm""",
    longDesc =
u"""
5/ 6/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CCCO
Imported from thermo.txt.
""",
)

entry(
    index = 136,
    label = "hoc2h4co",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,D}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49759,0.0294657,-1.76503e-05,5.27836e-09,-6.2719e-13,-24048.6,14.5475], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[11.7921,0.0119744,-4.02818e-06,6.19034e-10,-3.56788e-14,-27140.8,-30.7086], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 6/11 therm""",
    longDesc =
u"""
5/ 6/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=[C]CCO
Imported from thermo.txt.
""",
)

entry(
    index = 137,
    label = "ic4h8oh-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {16,S}
6  O u0 p2 c0 {2,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.08336,0.061887,-4.48341e-05,1.66256e-08,-2.50627e-12,-36374.3,20.3816], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[20.2204,0.0193385,-6.67393e-06,1.0425e-09,-6.07449e-14,-42636.9,-76.9315], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/2/95 therm""",
    longDesc =
u"""
6/2/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)C(O)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 138,
    label = "ic4h8oh-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {2,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.62972,0.0593554,-4.52639e-05,1.88258e-08,-3.27414e-12,-34301,17.4358], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[18.0915,0.0208235,-7.11062e-06,1.10246e-09,-6.38944e-14,-39515.4,-64.8903], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(CO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 139,
    label = "ic4h8oh-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {16,S}
6  O u0 p2 c0 {3,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06971,0.0538413,-3.49291e-05,1.19289e-08,-1.71696e-12,-31251,19.1106], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[17.7642,0.0213135,-7.32798e-06,1.14154e-09,-6.63815e-14,-36607.2,-60.5685], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CO)CO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 140,
    label = "ic4h7oh-1ooh-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.31449,0.0496202,-3.03935e-05,9.34183e-09,-1.14646e-12,-31370.3,8.265], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[19.0601,0.020161,-6.91892e-06,1.07649e-09,-6.25452e-14,-36443.4,-66.5544], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)C(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 141,
    label = "ic4h7oh-1ooh-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61741,0.0646115,-5.193e-05,2.17906e-08,-3.71408e-12,-28750.5,19.7881], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[20.6576,0.0187145,-6.40102e-06,9.93749e-10,-5.76531e-14,-34631.4,-75.7515], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)C(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 142,
    label = "ic4h7oh-2ooh-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34871,0.0641961,-5.21038e-05,2.23817e-08,-3.91984e-12,-26527.7,20.857], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[19.6901,0.0193608,-6.58471e-06,1.0183e-09,-5.8915e-14,-32137.4,-70.7747], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)(CO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 143,
    label = "ic4h7oh-2ooh-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {6,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92297,0.0646148,-5.42454e-05,2.414e-08,-4.35867e-12,-29691.3,16.6198], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[20.1035,0.0189914,-6.45274e-06,9.97186e-10,-5.76632e-14,-35147.4,-73.7665], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)([CH]O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 144,
    label = "ic4h7oh-3ooh-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {6,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30477,0.0593334,-4.42423e-05,1.74455e-08,-2.84588e-12,-26631.6,17.4725], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[19.7713,0.0194918,-6.67486e-06,1.03712e-09,-6.02041e-14,-32239.4,-70.5197], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC([CH]O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 145,
    label = "ic4h7oh-3ooh-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.04384,0.0414593,-1.69782e-05,9.9004e-10,6.66164e-13,-26189.5,8.36685], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[17.8146,0.0211815,-7.26397e-06,1.12972e-09,-6.56227e-14,-31028.7,-57.4593], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](CO)COO
Imported from thermo.txt.
""",
)

entry(
    index = 146,
    label = "ic4h7oh-3ooh-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.72974,0.0589187,-4.21077e-05,1.5692e-08,-2.40821e-12,-23467.9,22.1159], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[19.3573,0.019862,-6.80718e-06,1.05829e-09,-6.14595e-14,-29229.2,-67.122], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(CO)COO
Imported from thermo.txt.
""",
)

entry(
    index = 147,
    label = "ic4h7oh-1ooh-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {2,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.97302,0.0728627,-6.31086e-05,2.84825e-08,-5.16472e-12,-51263.3,8.99243], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[24.8936,0.0193505,-6.61696e-06,1.02705e-09,-5.95746e-14,-57504.3,-95.552], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(O[O])C(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 148,
    label = "ic4h7oh-1ooh-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.23725,0.0680751,-5.38305e-05,2.2242e-08,-3.75371e-12,-48185,11.4935], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[24.5575,0.0198694,-6.84882e-06,1.06885e-09,-6.22382e-14,-54600.4,-91.1998], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CO[O])C(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 149,
    label = "ic4h7oh-2ooh-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {2,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.97302,0.0728627,-6.31086e-05,2.84825e-08,-5.16472e-12,-51263.3,8.99243], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[24.8936,0.0193505,-6.61696e-06,1.02705e-09,-5.95746e-14,-57504.3,-95.552], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(OO)C(O)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 150,
    label = "ic4h7oh-2ooh-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.347,0.0660813,-5.18057e-05,2.15871e-08,-3.70707e-12,-46021.9,10.7895], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[23.4974,0.020687,-7.1112e-06,1.10765e-09,-6.44068e-14,-52076.4,-85.7112], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CO)(CO[O])OO
Imported from thermo.txt.
""",
)

entry(
    index = 151,
    label = "ic4h7oh-3ooh-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {8,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {2,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.23725,0.0680751,-5.38305e-05,2.2242e-08,-3.75371e-12,-48185,11.4935], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[24.5575,0.0198694,-6.84882e-06,1.06885e-09,-6.22382e-14,-54600.4,-91.1998], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(COO)C(O)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 152,
    label = "ic4h7oh-3ooh-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.347,0.0660813,-5.18057e-05,2.15871e-08,-3.70707e-12,-46021.9,10.7895], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[23.4974,0.020687,-7.1112e-06,1.10765e-09,-6.44068e-14,-52076.4,-85.7112], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CO)(COO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 153,
    label = "ic4h7oh-3ooh-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {4,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.76826,0.0606569,-4.16028e-05,1.47692e-08,-2.16683e-12,-42969.2,11.8548], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[23.1775,0.021168,-7.32492e-06,1.14611e-09,-6.68563e-14,-49171,-82.1255], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCC(CO)COO
Imported from thermo.txt.
""",
)

entry(
    index = 154,
    label = "ic4ohket1-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {14,D}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.680112,0.0747628,-6.24774e-05,2.61507e-08,-4.35923e-12,-73833.7,23.2486], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[23.6,0.0167387,-5.83969e-06,9.19008e-10,-5.38336e-14,-81261.1,-98.1162], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(OO)C(=O)O
Imported from thermo.txt.
""",
)

entry(
    index = 155,
    label = "ic4ohket1-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {14,D}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.17959,0.0687127,-5.37947e-05,2.13734e-08,-3.42382e-12,-71662.6,24.7901], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[21.9405,0.0181065,-6.3012e-06,9.89882e-10,-5.79103e-14,-78618.8,-85.8905], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(COO)C(=O)O
Imported from thermo.txt.
""",
)

entry(
    index = 156,
    label = "ic4ohket3-1",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81359,0.0666124,-5.42086e-05,2.26264e-08,-3.80266e-12,-62950.9,19.9947], Tmin=(298,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[22.1259,0.0176265,-6.0623e-06,9.448e-10,-5.49652e-14,-69227.9,-82.2791], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C=O)C(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 157,
    label = "ic4ohket3-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25372,0.0679496,-5.49731e-05,2.26213e-08,-3.73538e-12,-59817,22.241], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[22.3543,0.0174287,-5.99501e-06,9.3454e-10,-5.43821e-14,-66377.3,-84.3401], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C=O)(CO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 158,
    label = "ic4ohket3-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00425,0.0597701,-4.11711e-05,1.40012e-08,-1.87498e-12,-57664.3,22.0971], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[21.2403,0.0186236,-6.46217e-06,1.01318e-09,-5.91919e-14,-64097.8,-76.283], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CC(CO)COO
Imported from thermo.txt.
""",
)

entry(
    index = 159,
    label = "ic4h7oho1-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {2,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.20646,0.0676422,-5.45301e-05,2.23924e-08,-3.69441e-12,-40797.1,34.0333], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[17.7503,0.0175775,-6.05888e-06,9.45745e-10,-5.50824e-14,-47325.5,-71.8278], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1(C)OC1O
Imported from thermo.txt.
""",
)

entry(
    index = 160,
    label = "ic4h7oho1-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {3,S}
6  O u0 p2 c0 {2,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.33284,0.0655595,-4.92125e-05,1.88244e-08,-2.89506e-12,-37862.5,41.8267], Tmin=(298,'K'), Tmax=(1406,'K')),
            NASAPolynomial(coeffs=[15.7282,0.0194424,-6.64093e-06,1.03023e-09,-5.97437e-14,-44252.3,-59.8592], Tmin=(1406,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1COC1O
Imported from thermo.txt.
""",
)

entry(
    index = 161,
    label = "ic4h7oho2-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.39126,0.0659795,-5.37117e-05,2.27988e-08,-3.92144e-12,-35643.3,37.9682], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[16.0601,0.0186418,-6.34367e-06,9.81605e-10,-5.6822e-14,-41614,-59.6016], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1(CO)CO1
Imported from thermo.txt.
""",
)

entry(
    index = 162,
    label = "ic4h7oho3-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  O u0 p2 c0 {2,S} {3,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.1011,0.0654073,-4.84309e-05,1.8291e-08,-2.77756e-12,-32599.9,47.9503], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[14.9212,0.0197077,-6.64689e-06,1.02282e-09,-5.89922e-14,-39003.7,-53.6367], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OCC1COC1
Imported from thermo.txt.
""",
)

entry(
    index = 163,
    label = "ic4h8oh-1o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.44832,0.0708464,-5.53935e-05,2.22859e-08,-3.62346e-12,-53309.8,22.3288], Tmin=(298,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[21.8381,0.0202119,-6.90935e-06,1.07244e-09,-6.22143e-14,-60037.8,-86.0228], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)C(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 164,
    label = "ic4h8oh-2o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.5713,0.0687842,-5.4629e-05,2.30402e-08,-3.98013e-12,-51139.1,21.6142], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[20.1179,0.0214862,-7.30501e-06,1.12942e-09,-6.53322e-14,-57205.7,-76.6206], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(CO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 165,
    label = "ic4h8oh-3o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.95132,0.0635107,-4.46372e-05,1.63521e-08,-2.4686e-12,-48079.2,23.5724], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[19.7861,0.0219856,-7.52669e-06,1.16926e-09,-6.78676e-14,-54297.8,-72.2784], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CO)COO
Imported from thermo.txt.
""",
)

entry(
    index = 166,
    label = "ic4h8oh-1o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {15,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.334936,0.0601624,-4.25243e-05,1.51695e-08,-2.17491e-12,-33700.4,26.0112], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[18.2017,0.0189517,-6.54568e-06,1.02304e-09,-5.96354e-14,-39924.9,-70.0759], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/111 therm""",
    longDesc =
u"""
7/111 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)C([O])O
Imported from thermo.txt.
""",
)

entry(
    index = 167,
    label = "ic4h8oh-2o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {15,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.161304,0.0626866,-4.8749e-05,2.01357e-08,-3.43325e-12,-32008.4,28.5125], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[17.1996,0.0196206,-6.73461e-06,1.04805e-09,-6.0907e-14,-37834,-63.9159], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/111 therm""",
    longDesc =
u"""
7/111 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)([O])CO
Imported from thermo.txt.
""",
)

entry(
    index = 168,
    label = "ic4h8oh-3o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.739725,0.0525825,-3.49167e-05,1.25896e-08,-1.93806e-12,-37854.4,28.2308], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[14.3327,0.0214891,-7.25535e-06,1.11656e-09,-6.43819e-14,-42710.8,-45.1229], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/111 therm""",
    longDesc =
u"""
7/111 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C[O])CO
Imported from thermo.txt.
""",
)

entry(
    index = 169,
    label = "tc4h8oh-o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {16,S}
6  O u0 p2 c0 {2,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89006,0.0578243,-4.19768e-05,1.65162e-08,-2.74658e-12,-34743,16.9868], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[18.4676,0.0207601,-7.14638e-06,1.11413e-09,-6.48226e-14,-40179.3,-66.5921], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(O)CO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 170,
    label = "tc4h7oh-ooh",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6652,0.0624372,-4.85239e-05,1.99269e-08,-3.36703e-12,-26978.5,20.1442], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[20.0254,0.0193676,-6.65192e-06,1.03558e-09,-6.01964e-14,-32787.3,-72.251], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)(O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 171,
    label = "tc4h8o-ooh",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.00329,0.0645078,-4.92698e-05,1.95417e-08,-3.1807e-12,-25376.3,20.1889], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.8821,0.0189962,-6.60459e-06,1.03676e-09,-6.06166e-14,-31813.7,-80.7401], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)([O])COO
Imported from thermo.txt.
""",
)

entry(
    index = 172,
    label = "tc4h7oh-ooh-o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.59539,0.0645724,-4.85135e-05,1.92481e-08,-3.16805e-12,-46461.3,10.402], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[23.8871,0.0205929,-7.13242e-06,1.11665e-09,-6.51639e-14,-52743.9,-87.4853], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)(CO[O])COO
Imported from thermo.txt.
""",
)

entry(
    index = 173,
    label = "tc4ohket",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.03925,0.0626863,-4.58551e-05,1.66097e-08,-2.37315e-12,-59780.9,18.9043], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[22.2941,0.0175537,-6.05587e-06,9.45996e-10,-5.51317e-14,-66360.9,-84.2993], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/11 therm""",
    longDesc =
u"""
7/20/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)(C=O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 174,
    label = "tc4h7oho",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {3,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.207,0.0691818,-5.53831e-05,2.29683e-08,-3.85319e-12,-36105.6,46.1581], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[15.4361,0.0194651,-6.60154e-06,1.01936e-09,-5.89265e-14,-42504.1,-57.9118], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/11 therm""",
    longDesc =
u"""
7/20/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1(O)COC1
Imported from thermo.txt.
""",
)

entry(
    index = 175,
    label = "tc4h8oh-o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.88556,0.0670362,-5.10679e-05,2.0599e-08,-3.43069e-12,-51589.6,20.9117], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[20.4509,0.0214971,-7.37407e-06,1.14702e-09,-6.66342e-14,-57854.8,-78.0836], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 176,
    label = "tc4h8oh-o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u1 p2 c0 {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.161304,0.0626866,-4.8749e-05,2.01357e-08,-3.43325e-12,-32008.4,28.5125], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[17.1996,0.0196206,-6.73461e-06,1.04805e-09,-6.0907e-14,-37834,-63.9159], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(O)C[O]
Imported from thermo.txt.
""",
)

entry(
    index = 177,
    label = "sc4h8oh-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {16,S}
6  O u0 p2 c0 {1,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.04499,0.0633077,-5.13735e-05,2.26739e-08,-4.13663e-12,-34768.9,21.2978], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[18.5508,0.0205982,-7.0693e-06,1.09981e-09,-6.3893e-14,-40206.3,-66.0768], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(C)(O)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 178,
    label = "sc4h8oh-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {16,S}
6  O u0 p2 c0 {2,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13524,0.0614284,-4.69261e-05,1.92132e-08,-3.2661e-12,-34030.5,21.5777], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[18.7569,0.0203739,-6.98231e-06,1.08532e-09,-6.30161e-14,-39638.1,-66.997], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)C(C)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 179,
    label = "sc4h8oh-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {16,S}
6  O u0 p2 c0 {3,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06236,0.0562088,-3.8954e-05,1.43977e-08,-2.2421e-12,-32395,18.9519], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[18.4221,0.0207528,-7.1341e-06,1.11123e-09,-6.46148e-14,-37838.3,-63.801], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)CCO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 180,
    label = "sc4h8oh-mo2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {16,S}
6  O u0 p2 c0 {3,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06236,0.0562088,-3.8954e-05,1.43977e-08,-2.2421e-12,-32395,18.9519], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[18.4221,0.0207528,-7.1341e-06,1.11123e-09,-6.46148e-14,-37838.3,-63.801], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(O)CO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 181,
    label = "sc4h7oh-1ooh-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.01582,0.0637762,-4.97398e-05,2.00215e-08,-3.25559e-12,-28273.3,24.0867], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[20.3778,0.0181097,-6.02526e-06,9.19152e-10,-5.27087e-14,-34310.4,-73.4425], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C(C)(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 182,
    label = "sc4h7oh-1ooh-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.83356,0.067874,-5.7877e-05,2.60824e-08,-4.76176e-12,-27006.8,23.7011], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[20.0944,0.019241,-6.59202e-06,1.02444e-09,-5.9473e-14,-32812.6,-72.3538], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(C)(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 183,
    label = "sc4h7oh-1ooh-m",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.83356,0.067874,-5.7877e-05,2.60824e-08,-4.76176e-12,-27006.8,23.7011], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[20.0944,0.019241,-6.59202e-06,1.02444e-09,-5.9473e-14,-32812.6,-72.3538], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(O)(CC)OO
Imported from thermo.txt.
""",
)

entry(
    index = 184,
    label = "sc4h7oh-2ooh-m",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.93206,0.064436,-4.81328e-05,1.82251e-08,-2.78012e-12,-26240.2,24.1999], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[21.2004,0.018553,-6.4143e-06,1.00323e-09,-5.85117e-14,-32796.6,-78.8936], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(O)C(C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 185,
    label = "sc4h7oh-2ooh-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.93206,0.064436,-4.81328e-05,1.82251e-08,-2.78012e-12,-26240.2,24.1999], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[21.2004,0.018553,-6.4143e-06,1.00323e-09,-5.85117e-14,-32796.6,-78.8936], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(OO)C(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 186,
    label = "sc4h7oh-2ooh-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {3,S} {6,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.00186,0.0811011,-7.59166e-05,3.60883e-08,-6.74914e-12,-28959.1,36.1316], Tmin=(298,'K'), Tmax=(1406,'K')),
            NASAPolynomial(coeffs=[21.1923,0.018059,-6.13087e-06,9.47041e-10,-5.47511e-14,-35531.4,-79.0654], Tmin=(1406,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](O)C(C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 187,
    label = "sc4h7oh-3ooh-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {3,S} {6,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.113252,0.0748698,-6.62069e-05,3.00982e-08,-5.45131e-12,-27347.8,32.669], Tmin=(298,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[20.8839,0.0184144,-6.27435e-06,9.71626e-10,-5.62716e-14,-33748.7,-76.0348], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](O)CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 188,
    label = "sc4h7oh-3ooh-m",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.71887,0.0597729,-4.12319e-05,1.41706e-08,-1.93579e-12,-24579.6,22.2439], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[20.7189,0.0190151,-6.58535e-06,1.03113e-09,-6.01847e-14,-30925.4,-74.828], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(O)CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 189,
    label = "sc4h7oh-3ooh-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {2,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1778,0.0560382,-3.70231e-05,1.19375e-08,-1.46539e-12,-25917.1,21.0927], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[19.8063,0.0187686,-6.28707e-06,9.63331e-10,-5.54068e-14,-31763,-68.6284], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)[CH]COO
Imported from thermo.txt.
""",
)

entry(
    index = 190,
    label = "sc4h7oh-mooh-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.71887,0.0597729,-4.12319e-05,1.41706e-08,-1.93579e-12,-24579.6,22.2439], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[20.7189,0.0190151,-6.58535e-06,1.03113e-09,-6.01847e-14,-30925.4,-74.828], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 191,
    label = "sc4h7oh-mooh-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1778,0.0560382,-3.70231e-05,1.19375e-08,-1.46539e-12,-25917.1,21.0927], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[19.8063,0.0187686,-6.28707e-06,9.63331e-10,-5.54068e-14,-31763,-68.6284], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C(O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 192,
    label = "sc4h7oh-mooh-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {2,S} {6,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.113252,0.0748698,-6.62069e-05,3.00982e-08,-5.45131e-12,-27347.8,32.669], Tmin=(298,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[20.8839,0.0184144,-6.27435e-06,9.71626e-10,-5.62716e-14,-33748.7,-76.0348], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11 therm""",
    longDesc =
u"""
11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[C](O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 193,
    label = "sc4h7oh-1ooh-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {2,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29729,0.0727203,-6.01577e-05,2.63611e-08,-4.72263e-12,-47895.7,20.1854], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.3924,0.0209519,-7.24228e-06,1.13231e-09,-6.60146e-14,-54475,-86.1661], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O[O])C(C)(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 194,
    label = "sc4h7oh-1ooh-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06467,0.0679516,-5.28018e-05,2.19147e-08,-3.77798e-12,-46227.9,18.3596], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[22.991,0.0213697,-7.40369e-06,1.15933e-09,-6.76622e-14,-52656.1,-82.6013], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)(CCO[O])OO
Imported from thermo.txt.
""",
)

entry(
    index = 195,
    label = "sc4h7oh-1ooh-mo2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06467,0.0679516,-5.28018e-05,2.19147e-08,-3.77798e-12,-46227.9,18.3596], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[22.991,0.0213697,-7.40369e-06,1.15933e-09,-6.76622e-14,-52656.1,-82.6013], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(O)(CO[O])OO
Imported from thermo.txt.
""",
)

entry(
    index = 196,
    label = "sc4h7oh-2ooh-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {1,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29729,0.0727203,-6.01577e-05,2.63611e-08,-4.72263e-12,-47895.7,20.1854], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.3924,0.0209519,-7.24228e-06,1.13231e-09,-6.60146e-14,-54475,-86.1661], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(OO)C(C)(O)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 197,
    label = "sc4h7oh-2ooh-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.97745,0.067621,-5.31395e-05,2.19849e-08,-3.73284e-12,-45767.9,13.6745], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[23.9399,0.0203922,-7.02825e-06,1.09672e-09,-6.3854e-14,-52093,-87.1804], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)C(CO[O])OO
Imported from thermo.txt.
""",
)

entry(
    index = 198,
    label = "sc4h7oh-2ooh-mo2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.97745,0.067621,-5.31395e-05,2.19849e-08,-3.73284e-12,-45767.9,13.6745], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[23.9399,0.0203922,-7.02825e-06,1.09672e-09,-6.3854e-14,-52093,-87.1804], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(OO)C(O)CO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 199,
    label = "sc4h7oh-3ooh-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {8,S}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {1,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06467,0.0679516,-5.28018e-05,2.19147e-08,-3.77798e-12,-46227.9,18.3596], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[22.991,0.0213697,-7.40369e-06,1.15933e-09,-6.76622e-14,-52656.1,-82.6013], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)(CCOO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 200,
    label = "sc4h7oh-3ooh-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {8,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {1,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.97745,0.067621,-5.31395e-05,2.19849e-08,-3.73284e-12,-45767.9,13.6745], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[23.9399,0.0203922,-7.02825e-06,1.09672e-09,-6.3854e-14,-52093,-87.1804], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)C(COO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 201,
    label = "sc4h7oh-3ooh-mo2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
5  O u0 p2 c0 {4,S} {8,S}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.86412,0.0624568,-4.51868e-05,1.71648e-08,-2.70605e-12,-44122.6,11.2585], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[23.5904,0.0207853,-7.18543e-06,1.12353e-09,-6.55075e-14,-50294.2,-83.9197], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCC(O)CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 202,
    label = "sc4h7oh-mooh-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {8,S}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {1,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06467,0.0679516,-5.28018e-05,2.19147e-08,-3.77798e-12,-46227.9,18.3596], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[22.991,0.0213697,-7.40369e-06,1.15933e-09,-6.76622e-14,-52656.1,-82.6013], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(O)(COO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 203,
    label = "sc4h7oh-mooh-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {8,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {1,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.97745,0.067621,-5.31395e-05,2.19849e-08,-3.73284e-12,-45767.9,13.6745], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[23.9399,0.0203922,-7.02825e-06,1.09672e-09,-6.3854e-14,-52093,-87.1804], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O[O])C(O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 204,
    label = "sc4h7oh-mooh-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {8,S}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {4,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.86412,0.0624568,-4.51868e-05,1.71648e-08,-2.70605e-12,-44122.6,11.2585], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[23.5904,0.0207853,-7.18543e-06,1.12353e-09,-6.55075e-14,-50294.2,-83.9197], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""therm""",
    longDesc =
u"""
therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCC(O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 205,
    label = "sc4ohket2-1",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96338,0.0608378,-4.28195e-05,1.49923e-08,-2.08826e-12,-61959.6,19.1022], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[21.5642,0.0184113,-6.40291e-06,1.00539e-09,-5.87984e-14,-68481.7,-81.0932], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)C(C)(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 206,
    label = "sc4ohket2-3",
    molecule =
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {14,D}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.816366,0.0811656,-7.43886e-05,3.45644e-08,-6.35627e-12,-60029.4,38.186], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[22.3575,0.0175642,-6.07076e-06,9.49256e-10,-5.53521e-14,-67125.1,-82.905], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)C(=O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 207,
    label = "sc4ohket2-m",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.20356,0.0643658,-4.79701e-05,1.81631e-08,-2.78894e-12,-61895.6,25.1233], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[21.706,0.0183854,-6.41489e-06,1.00944e-09,-5.9122e-14,-68609.4,-79.4402], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)C(O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 208,
    label = "sc4ohket3-1",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50279,0.065795,-5.67123e-05,2.58987e-08,-4.79549e-12,-61730,16.4915], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[21.2618,0.0184079,-6.34006e-06,9.88834e-10,-5.75508e-14,-67399.9,-76.9475], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)C(C=O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 209,
    label = "sc4ohket3-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.26883,0.0740864,-6.54409e-05,2.95065e-08,-5.29697e-12,-59530.3,26.9638], Tmin=(298,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[22.3743,0.0173715,-5.96462e-06,9.28543e-10,-5.39778e-14,-66091.8,-83.7111], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)(CC=O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 210,
    label = "sc4ohket3-m",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.55247,0.0584021,-4.4238e-05,1.77934e-08,-2.9709e-12,-59353.4,14.0405], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.8749,0.018777,-6.47722e-06,1.01134e-09,-5.89077e-14,-64925.6,-73.18], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CCC(O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 211,
    label = "sc4ohketm-1",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67231,0.0618044,-4.5949e-05,1.71538e-08,-2.55735e-12,-58441,15.4443], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[22.3225,0.0175134,-6.03719e-06,9.42487e-10,-5.49005e-14,-64774.6,-84.3437], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(O)(C=O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 212,
    label = "sc4ohketm-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.82195,0.0689337,-5.51451e-05,2.23628e-08,-3.64649e-12,-59921.3,25.3535], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[22.6236,0.0174929,-6.08208e-06,9.549e-10,-5.58418e-14,-66810.1,-85.2704], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species sc4ohketm-1 (i.e. same molecular structure according to RMG)
CCC(O)(C=O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 213,
    label = "sc4ohketm-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.62207,0.0641667,-4.78379e-05,1.79546e-08,-2.71075e-12,-58262.9,23.3375], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[22.2531,0.0178874,-6.23602e-06,9.80807e-10,-5.74267e-14,-64997,-81.8759], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CC(O)CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 214,
    label = "sc4h7oho1-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.16611,0.0807831,-7.93754e-05,3.91548e-08,-7.4732e-12,-38770.6,38.1985], Tmin=(298,'K'), Tmax=(1413,'K')),
            NASAPolynomial(coeffs=[15.857,0.0170056,-5.40015e-06,7.96413e-10,-4.45517e-14,-44515,-69.354], Tmin=(1413,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1OC1(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 215,
    label = "sc4h7oho1-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.24916,0.0693656,-5.56763e-05,2.3176e-08,-3.90466e-12,-36099,46.3548], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[15.4161,0.019513,-6.62444e-06,1.02357e-09,-5.91962e-14,-42502.1,-57.8132], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species sc4h7oho1-2 (i.e. same molecular structure according to RMG)
CC1OC1(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 216,
    label = "sc4h7oho1-m",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.42791,0.0661371,-5.39629e-05,2.29777e-08,-3.96611e-12,-35637.5,38.1396], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[16.0458,0.0186795,-6.36208e-06,9.85023e-10,-5.70425e-14,-41614.1,-59.5347], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC1(O)CO1
Imported from thermo.txt.
""",
)

entry(
    index = 217,
    label = "sc4h7oho2-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.50126,0.0676404,-5.65916e-05,2.46417e-08,-4.3262e-12,-35511.4,39.0979], Tmin=(298,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[16.2166,0.0185631,-6.32654e-06,9.79819e-10,-5.67491e-14,-41463.9,-59.5074], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)C1CO1
Imported from thermo.txt.
""",
)

entry(
    index = 218,
    label = "sc4h7oho2-m",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.27023,0.070625,-5.80396e-05,2.47766e-08,-4.27068e-12,-35979.8,47.0767], Tmin=(298,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[15.4543,0.0196288,-6.69326e-06,1.03701e-09,-6.00786e-14,-42312.3,-57.0668], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1OCC1O
Imported from thermo.txt.
""",
)

entry(
    index = 219,
    label = "sc4h7oho3-m",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.50351,0.0697097,-5.33975e-05,2.12226e-08,-3.43037e-12,-43487.1,54.1797], Tmin=(298,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[14.2286,0.0211385,-7.2242e-06,1.12098e-09,-6.50133e-14,-50059.9,-50.8605], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OC1CCOC1
Imported from thermo.txt.
""",
)

entry(
    index = 220,
    label = "sc4h8oh-1o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0807,0.0723688,-6.02795e-05,2.66744e-08,-4.80902e-12,-51622.3,25.0309], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[20.516,0.0213775,-7.31733e-06,1.13646e-09,-6.59469e-14,-57878.2,-77.4742], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(C)(O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 221,
    label = "sc4h8oh-2o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.10791,0.0704213,-5.50659e-05,2.24796e-08,-3.74235e-12,-50867.5,25.6624], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[20.9297,0.0210251,-7.19767e-06,1.11814e-09,-6.49003e-14,-57433.2,-79.6804], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)C(C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 222,
    label = "sc4h8oh-3o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.97319,0.0654273,-4.743e-05,1.78813e-08,-2.76811e-12,-49221,23.3348], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[20.572,0.0214331,-7.36147e-06,1.14611e-09,-6.66263e-14,-55627.8,-76.3618], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 223,
    label = "sc4h8oh-mo2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.97319,0.0654273,-4.743e-05,1.78813e-08,-2.76811e-12,-49221,23.3348], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[20.572,0.0214331,-7.36147e-06,1.14611e-09,-6.66263e-14,-55627.8,-76.3618], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 224,
    label = "sc4h8oh-1o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.200135,0.0628475,-4.89967e-05,2.03076e-08,-3.4756e-12,-32002.1,29.3848], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[17.1903,0.0196505,-6.74965e-06,1.05089e-09,-6.10912e-14,-37836.3,-63.1877], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(C)([O])O
Imported from thermo.txt.
""",
)

entry(
    index = 225,
    label = "sc4h8oh-2o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.282355,0.0641795,-5.12587e-05,2.18364e-08,-3.83685e-12,-31868.7,30.4297], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[17.3909,0.0196576,-6.79047e-06,1.06118e-09,-6.18472e-14,-37761.4,-63.4709], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC([O])C(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 226,
    label = "sc4h8oh-3o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.322902,0.0596523,-4.41961e-05,1.74297e-08,-2.86189e-12,-29702.8,29.0606], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[16.7892,0.0200395,-6.89348e-06,1.07426e-09,-6.24869e-14,-35358,-59.0525], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)CC[O]
Imported from thermo.txt.
""",
)

entry(
    index = 227,
    label = "sc4h8oh-mo",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.322902,0.0596523,-4.41961e-05,1.74297e-08,-2.86189e-12,-29702.8,29.0606], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[16.7892,0.0200395,-6.89348e-06,1.07426e-09,-6.24869e-14,-35358,-59.0525], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/11 therm""",
    longDesc =
u"""
7/11 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(O)C[O]
Imported from thermo.txt.
""",
)

entry(
    index = 228,
    label = "oh*",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63727,0.000185091,-1.67616e-06,2.3872e-09,-8.43144e-13,50021.3,1.35886], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.88273,0.00101397,-2.27688e-07,2.17468e-11,-5.12631e-16,50265,5.59571], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121286""",
    longDesc =
u"""
121286
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species oh (i.e. same molecular structure according to RMG)
[OH]
Imported from thermo.txt.
""",
)

entry(
    index = 229,
    label = "ch*",
    molecule =
"""
multiplicity 4
1 C u3 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2002,0.00207288,-5.13443e-06,5.73389e-09,-1.95553e-12,103937,3.33159], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.19622,0.00234038,-7.0582e-07,9.00758e-11,-3.85504e-15,104196,9.17837], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""073003""",
    longDesc =
u"""
073003
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species ch (i.e. same molecular structure according to RMG)
[CH]
Imported from thermo.txt.
""",
)

entry(
    index = 230,
    label = "he",
    molecule =
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 5/97""",
    longDesc =
u"""
g 5/97.
[He]
Imported from thermo.txt.
""",
)

entry(
    index = 231,
    label = "c2h3oh",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.127972,0.0338506,-3.30645e-05,1.64859e-08,-3.19935e-12,-15991.5,23.0439], Tmin=(298,'K'), Tmax=(1410,'K')),
            NASAPolynomial(coeffs=[8.32598,0.00803387,-2.63928e-06,3.98411e-10,-2.26551e-14,-18322.1,-20.208], Tmin=(1410,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/ 3/ 9 therm""",
    longDesc =
u"""
2/ 3/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CO
Imported from thermo.txt.
""",
)

entry(
    index = 232,
    label = "c4h71-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.54747,0.00463771,6.6134e-05,-8.97457e-08,3.61716e-11,14384.3,7.30313], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.08107,0.0195527,-6.93149e-06,1.10889e-09,-6.59584e-14,12282.3,-16.7138], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t05/04""",
    longDesc =
u"""
t05/04.
C=C[CH]C
Imported from thermo.txt.
""",
)

entry(
    index = 233,
    label = "ic3h7cho",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.22518,0.0448246,-2.87283e-05,9.75592e-09,-1.39154e-12,-29163.2,20.9037], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[12.9448,0.0186021,-6.29697e-06,9.70675e-10,-5.60318e-14,-33389,-42.5142], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11/23/ 9 therm""",
    longDesc =
u"""
11/23/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)C=O
Imported from thermo.txt.
""",
)

entry(
    index = 234,
    label = "nc3h7",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08211,0.0052324,5.13554e-05,-6.99344e-08,2.81819e-11,10407.5,8.39535], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.49637,0.0177338,-6.24898e-06,9.95389e-10,-5.902e-14,8859.74,-8.5639], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""a 5/05""",
    longDesc =
u"""
a 5/05.
[CH2]CC
Imported from thermo.txt.
""",
)

entry(
    index = 235,
    label = "pc2h4oh",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47893,0.00759782,2.81795e-05,-4.26953e-08,1.78879e-11,-4714.46,6.38921], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.02825,0.0120038,-4.21306e-06,6.69471e-10,-3.96372e-14,-5924.93,-9.40356], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t12/01""",
    longDesc =
u"""
t12/01.
[CH2]CO
Imported from thermo.txt.
""",
)

entry(
    index = 236,
    label = "sc2h4oh",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 O u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.22283,0.00512175,3.48387e-05,-4.91944e-08,2.01184e-11,-8205.04,8.01676], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.35842,0.0124356,-4.33097e-06,6.8453e-10,-4.03713e-14,-9379,-6.05106], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t10/04""",
    longDesc =
u"""
t10/04.
C[CH]O
Imported from thermo.txt.
""",
)

entry(
    index = 237,
    label = "sc4h9",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.42089,-0.000912147,8.84999e-05,-1.12116e-07,4.38223e-11,6289.27,5.0421], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.72287,0.0243427,-8.65476e-06,1.38713e-09,-8.26084e-14,4150.04,-14.395], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t 6/04""",
    longDesc =
u"""
t 6/04.
C[CH]CC
Imported from thermo.txt.
""",
)

entry(
    index = 238,
    label = "c4h8-2",
    molecule =
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.57279,0.00376541,6.52227e-05,-8.3091e-08,3.20311e-11,-3601.28,0.537797], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.89115,0.0224971,-8.12144e-06,1.31274e-09,-7.84452e-14,-5516.43,-17.6436], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t 5/09""",
    longDesc =
u"""
t 5/09.
CC=CC
Imported from thermo.txt.
""",
)

entry(
    index = 239,
    label = "c3h3",
    molecule =
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35111,0.0327411,-4.73827e-05,3.7631e-08,-1.18541e-11,38397.9,15.2059], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.14222,0.00761902,-2.6746e-06,4.24915e-10,-2.51475e-14,37200.9,-12.5849], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t06/09""",
    longDesc =
u"""
t06/09.
C#C[CH2]
Imported from thermo.txt.
""",
)

entry(
    index = 240,
    label = "c3h4-p",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.68039,0.0157997,2.50706e-06,-1.36576e-08,6.61543e-12,20802.4,9.87694], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.02524,0.0113365,-4.02234e-06,6.43761e-10,-3.82996e-14,19620.9,-8.60438], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t 2/90""",
    longDesc =
u"""
t 2/90.
C#CC
Imported from thermo.txt.
""",
)

entry(
    index = 241,
    label = "pc4h9o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.00937,-0.000266942,0.000116727,-1.51712e-07,6.00701e-11,-27503.2,-4.64153], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.8219,0.0286824,-1.02148e-05,1.63573e-09,-9.73134e-14,-30779.8,-39.4378], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t03/09""",
    longDesc =
u"""
t03/09.
CCCCOO
Imported from thermo.txt.
""",
)

entry(
    index = 242,
    label = "pc4h9o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.72178,-0.0052448,0.00012351,-1.57238e-07,6.17434e-11,-10519.6,-0.764798], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.343,0.0262571,-9.56671e-06,1.55187e-09,-9.30636e-14,-13863.1,-35.1216], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t04/09""",
    longDesc =
u"""
t04/09.
CCCCO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 243,
    label = "ch2cch2oh",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 O u0 p2 c0 {1,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88423,0.0242428,-1.14152e-05,1.71775e-09,1.42177e-13,11793.6,15.2102], Tmin=(298,'K'), Tmax=(1372,'K')),
            NASAPolynomial(coeffs=[9.70702,0.0113973,-3.77994e-06,5.75209e-10,-3.29229e-14,9132.13,-22.5013], Tmin=(1372,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""9/ 8/95 therm""",
    longDesc =
u"""
9/ 8/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]CO
Imported from thermo.txt.
""",
)

entry(
    index = 244,
    label = "c4h5-n",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 C u1 p0 c0 {2,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.163053,0.0398301,-3.40001e-05,1.51472e-08,-2.46658e-12,41429.8,23.5362], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.8502,0.010779,-1.36721e-06,-7.72005e-10,1.83663e-13,38840.3,-26.0018], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""h6w/94""",
    longDesc =
u"""
h6w/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC=C
Imported from thermo.txt.
""",
)

entry(
    index = 245,
    label = "c4h71-4",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.07355,0.00527619,6.23441e-05,-8.54203e-08,3.4589e-11,22461.5,5.60318], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.49074,0.0191057,-6.74371e-06,1.07343e-09,-6.36252e-14,20465.9,-17.4556], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t05/04""",
    longDesc =
u"""
t05/04.
[CH2]CC=C
Imported from thermo.txt.
""",
)

entry(
    index = 246,
    label = "ic3h7",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.47421,-0.00842537,8.04608e-05,-9.49288e-08,3.59831e-11,9049.39,3.40542], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.30597,0.0189855,-6.74315e-06,1.07994e-09,-6.42785e-14,7787.49,-2.23234], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""a 5/05""",
    longDesc =
u"""
a 5/05.
C[CH]C
Imported from thermo.txt.
""",
)

entry(
    index = 247,
    label = "c2h5cho",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.2453,0.00668297,4.93338e-05,-6.71986e-08,2.67262e-11,-24147.3,6.90739], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.44086,0.0177302,-6.34082e-06,1.02041e-09,-6.09462e-14,-26005.6,-14.4195], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t05/10""",
    longDesc =
u"""
t05/10.
CCC=O
Imported from thermo.txt.
""",
)

entry(
    index = 248,
    label = "hocho",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89836,-0.00355878,3.55205e-05,-4.385e-08,1.71078e-11,-46770.6,7.34954], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.61383,0.00644964,-2.29083e-06,3.6716e-10,-2.18737e-14,-47514.8,0.847884], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""l 8/88""",
    longDesc =
u"""
l 8/88.
O=CO
Imported from thermo.txt.
""",
)

entry(
    index = 249,
    label = "c2h5co",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {9,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.25722,-0.00917612,7.6119e-05,-9.05515e-08,3.46198e-11,-5916.16,2.23331], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.52325,0.0154212,-5.50898e-06,8.8589e-10,-5.28846e-14,-7196.32,-5.19862], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""a10/04""",
    longDesc =
u"""
a10/04.
CC[C]=O
Imported from thermo.txt.
""",
)

entry(
    index = 250,
    label = "pc4h9",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.73738,0.00969052,6.63846e-05,-9.24799e-08,3.74006e-11,7573.82,4.91063], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.97402,0.0239704,-8.48704e-06,1.35644e-09,-8.06235e-14,5191.62,-23.1076], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t 7/04""",
    longDesc =
u"""
t 7/04.
[CH2]CCC
Imported from thermo.txt.
""",
)

entry(
    index = 251,
    label = "ch3coch3",
    molecule =
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.55639,-0.00283864,7.05723e-05,-8.78131e-08,3.40291e-11,-27832.5,2.3196], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.29797,0.0175657,-6.31678e-06,1.02026e-09,-6.10904e-14,-29536.9,-12.7592], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""atct a""",
    longDesc =
u"""
atct a.
CC(C)=O
Imported from thermo.txt.
""",
)

entry(
    index = 252,
    label = "ic3h5oh",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.956995,0.0522712,-5.19795e-05,2.63316e-08,-5.18631e-12,-22403.4,25.8663], Tmin=(298,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[12.1621,0.0120412,-4.03021e-06,6.16303e-10,-3.53702e-14,-26046,-41.2659], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11/23/ 9""",
    longDesc =
u"""
11/23/ 9
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)O
Imported from thermo.txt.
""",
)

entry(
    index = 253,
    label = "c4h5-i",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {4,D} {8,S} {9,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0199329,0.0380057,-2.75594e-05,7.78356e-09,4.02094e-13,37496.2,24.3942], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.2291,0.00948501,-9.04064e-08,-1.25961e-09,2.47815e-13,34642.8,-28.5645], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""h6w/94""",
    longDesc =
u"""
h6w/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]C=C
Imported from thermo.txt.
""",
)

entry(
    index = 254,
    label = "ch3coch2",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u1 p0 c0 {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.70187,0.00551654,4.27506e-05,-5.94681e-08,2.40685e-11,-5928.45,7.12933], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.54411,0.0143443,-5.08381e-06,8.13201e-10,-4.83673e-14,-7486.72,-11.4793], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""a10/04""",
    longDesc =
u"""
a10/04.
[CH2]C(C)=O
Imported from thermo.txt.
""",
)

entry(
    index = 255,
    label = "h2cc",
    molecule =
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u2 p0 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28155,0.00697648,-2.38552e-06,-1.21044e-09,9.81895e-13,48621.8,5.92039], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.27803,0.00475628,-1.6301e-06,2.54628e-10,-1.48864e-14,48316.7,0.640237], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""l12/89""",
    longDesc =
u"""
l12/89.
[C]=C
Imported from thermo.txt.
""",
)

entry(
    index = 256,
    label = "tc4h9o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77057,0.0268033,4.12718e-05,-7.22055e-08,3.02642e-11,-12707.9,12.1533], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.7372,0.0233707,-8.50517e-06,1.3852e-09,-8.34398e-14,-16694,-45.3156], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t08/04""",
    longDesc =
u"""
t08/04.
CC(C)(C)[O]
Imported from thermo.txt.
""",
)

entry(
    index = 257,
    label = "ch3o2h",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90541,0.0174995,5.28244e-06,-2.52827e-08,1.34368e-11,-16889.5,11.3742], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.76538,0.008615,-2.98007e-06,4.68638e-10,-2.75339e-14,-18298,-14.3993], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""a 7/05""",
    longDesc =
u"""
a 7/05.
COO
Imported from thermo.txt.
""",
)

entry(
    index = 258,
    label = "ch3o2",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62497,0.00359398,2.26538e-05,-2.95392e-08,1.11978e-11,79.304,9.96382], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.80391,0.00995845,-3.85301e-06,6.8474e-10,-4.58403e-14,-747.135,1.45281], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
ch3o2             t04/10c  1 h  3 o  2    0 g   200.000  6000.00   1000.00     1
5.55530486e+00 9.12236137e-03-3.23851661e-06 5.18713798e-10-3.08834151e-14    2
-1.03569402e+03-3.99158547e+00 4.97169544e+00-5.29356557e-03 4.77334149e-05    3
-5.77065617e-08 2.22219969e-11-1.29022161e+02 2.81501182e+00 1.43618036e+03    4
ch3o2      1/14/ 5 thermc   1h   3o   2    0g   300.000  5000.000 1365.000    11
6.34718801e+00 7.92089358e-03-2.76601913e-06 4.35360631e-10-2.54984762e-14    2
-1.83436055e+03-7.42552545e+00 3.80497590e+00 9.80784660e-03-3.90940624e-07    3
-2.23072602e-09 6.43310820e-13-4.55625796e+02 7.81789100e+00                   4
Hf from JMS, thermo from wkm: ub3lyp tight, ultrafine, unscaled

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 259,
    label = "c2h2oh",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 O u0 p2 c0 {1,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.562398,0.0264599,-2.28454e-05,9.14479e-09,-1.06712e-12,14837.5,21.044], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.8134,0.00805828,-3.11729e-06,5.54591e-10,-3.71804e-14,13158.3,-10.9864], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
wkm therm from princeton days
c2h2oh     1/26/ 9 wkm  c   2h   3o   1    0g   300.000  5000.000 1470.000    11
6.93453102e+00 7.23098468e-03-1.99956432e-06 1.43274685e-10 5.18910992e-15    2
1.28905371e+04-1.02350453e+01 1.43806872e+00 2.93422585e-02-2.90685031e-05    3
1.38331994e-08-2.56485091e-12 1.32889028e+04 1.50985534e+01                   4
Hf from average of atomisation technique of cbs-qb3, cbs-apno and g3. Frequencies from
tight mp2/6-311g(d,p) calc, scaled by 0.9496. Hindered rotor accounted for.
This is the minimum energy trans conformer

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CO
Imported from thermo.txt.
""",
)

entry(
    index = 260,
    label = "ch2ch2cho",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {6,D} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.36273,-0.00390713,3.59751e-05,-2.69209e-08,5.9892e-12,-755.243,-9.5314], Tmin=(298,'K'), Tmax=(1363,'K')),
            NASAPolynomial(coeffs=[9.96856,0.0161918,-6.64162e-06,1.15445e-09,-7.21982e-14,-4164.5,-27.3972], Tmin=(1363,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/10/ 4 therm""",
    longDesc =
u"""
8/10/ 4 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC=O
Imported from thermo.txt.
""",
)

entry(
    index = 261,
    label = "c4h4",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.91525,0.0527509,-7.16559e-05,5.50724e-08,-1.72862e-11,32978.5,31.42], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.65071,0.0161294,-7.19389e-06,1.49818e-09,-1.18641e-13,31196,-9.79521], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""h6w/94""",
    longDesc =
u"""
h6w/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC=C
Imported from thermo.txt.
""",
)

entry(
    index = 262,
    label = "c4h71-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u1 p0 c0 {3,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19858,0.0119617,4.23865e-05,-6.30299e-08,2.59475e-11,27525.7,8.57181], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.15646,0.0190309,-6.73262e-06,1.07333e-09,-6.36886e-14,25582.6,-16.1429], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t05/04""",
    longDesc =
u"""
t05/04.
[CH]=CCC
Imported from thermo.txt.
""",
)

entry(
    index = 263,
    label = "ic4h10",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.45479,0.00826059,8.29886e-05,-1.14648e-07,4.6457e-11,-18459.4,4.92741], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.76992,0.0254997,-9.14143e-06,1.47328e-09,-8.808e-14,-21405.3,-30.033], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 8/00""",
    longDesc =
u"""
g 8/00.
CC(C)C
Imported from thermo.txt.
""",
)

entry(
    index = 264,
    label = "tc4h9",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.45911,-0.0102016,0.000106311,-1.25717e-07,4.75543e-11,4434.2,1.30649], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.72557,0.0253649,-9.05306e-06,1.45475e-09,-8.67934e-14,2574.31,-8.8992], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t 6/04""",
    longDesc =
u"""
t 6/04.
C[C](C)C
Imported from thermo.txt.
""",
)

entry(
    index = 265,
    label = "ic4h8",
    molecule =
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30612,0.0133377,5.65726e-05,-8.46898e-08,3.52403e-11,-4041.28,9.92305], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.94232,0.02129,-7.61851e-06,1.22641e-09,-7.32634e-14,-6672.93,-24.6775], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t05/09""",
    longDesc =
u"""
t05/09.
C=C(C)C
Imported from thermo.txt.
""",
)

entry(
    index = 266,
    label = "ch3ocho",
    molecule =
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,D} {8,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.96757,-0.00938085,7.07648e-05,-8.29932e-08,3.13523e-11,-45571.3,0.750341], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.33361,0.0134851,-4.84306e-06,7.81719e-10,-4.67917e-14,-46831.7,-6.91543], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t 6/08""",
    longDesc =
u"""
t 6/08.
COC=O
Imported from thermo.txt.
""",
)

entry(
    index = 267,
    label = "ch3och2",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {3,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19173,0.0190391,-6.81451e-06,8.63578e-11,3.23902e-13,-1389.48,16.2441], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[6.73135,0.0118023,-4.00104e-06,6.17227e-10,-3.56435e-14,-3349.33,-9.40783], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/20/11""",
    longDesc =
u"""
1/20/11
ch3och2           a10/04c  2 h  5 o  1    0 g   200.000  6000.00  1000.00      1
5.94067593e+00 1.29906358e-02-4.56921036e-06 7.26888932e-10-4.30599587e-14    2
-2.58503562e+03-4.52841964e+00 4.53195381e+00 7.81884271e-03 1.94968539e-05    3
-2.74538336e-08 1.06521135e-11-1.70629244e+03 5.06122980e+00 1.15460803e+02    4
HJC

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]OC
Imported from thermo.txt.
""",
)

entry(
    index = 268,
    label = "ch3och3",
    molecule =
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.4186,0.018728,-1.40895e-06,-4.28368e-09,1.36818e-12,-23677.2,12.8878], Tmin=(298,'K'), Tmax=(1367,'K')),
            NASAPolynomial(coeffs=[7.36359,0.013891,-4.74083e-06,7.34874e-10,-4.25868e-14,-26114.8,-16.1333], Tmin=(1367,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/20/11""",
    longDesc =
u"""
1/20/11
ch3och3           t03/10c  2 h  6 o  1    0 g   200.000  6000.00  1000.00      1
5.64844274e+00 1.63381875e-02-5.86802189e-06 9.46836384e-10-5.66504295e-14    2
-2.50864216e+04-5.96267354e+00 5.30562273e+00-2.14253958e-03 5.30873092e-05    3
-6.23146897e-08 2.30730916e-11-2.39655820e+04 7.13244569e-01-2.21221696e+04    4
HJC

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
COC
Imported from thermo.txt.
""",
)

entry(
    index = 269,
    label = "ho2cho",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,D} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.42465,0.0219706,-1.68706e-05,6.25612e-09,-9.11646e-13,-35482.8,17.5028], Tmin=(298,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[9.87504,0.00464664,-1.67231e-06,2.68624e-10,-1.59595e-14,-38050.2,-22.4939], Tmin=(1378,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/26/95 therm""",
    longDesc =
u"""
6/26/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=COO
Imported from thermo.txt.
""",
)

entry(
    index = 270,
    label = "ocho",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u1 p2 c0 {1,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.68826,-0.00414872,2.55066e-05,-2.84474e-08,1.04423e-11,-16986.7,4.28426], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14394,0.00559739,-1.99794e-06,3.16179e-10,-1.85614e-14,-17246,5.07779], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""atct/a""",
    longDesc =
u"""
atct/a.
[O]C=O
Imported from thermo.txt.
""",
)

entry(
    index = 271,
    label = "ic4h9",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34477,0.023187,3.28261e-05,-5.96399e-08,2.58981e-11,6662.01,9.6886], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.61251,0.0228582,-8.06391e-06,1.28557e-09,-7.62731e-14,4152.19,-26.6485], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t 6/04""",
    longDesc =
u"""
t 6/04.
[CH2]C(C)C
Imported from thermo.txt.
""",
)

entry(
    index = 272,
    label = "c2h5o",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.30743,0.00641472,3.11397e-05,-4.33141e-08,1.72762e-11,-3402.75,5.90258], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.689,0.0131257,-4.70388e-06,7.58586e-10,-4.54133e-14,-4745.78,-9.69838], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""iu2/03""",
    longDesc =
u"""
iu2/03.
CC[O]
Imported from thermo.txt.
""",
)

entry(
    index = 273,
    label = "tc3h6oh",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  O u0 p2 c0 {3,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0967,0.0380728,-2.75022e-05,1.07477e-08,-1.74896e-12,-14076.4,22.2476], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[11.2222,0.0136444,-4.51407e-06,7.10523e-10,-4.2269e-14,-17535,-31.8912], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 9/ 4 therm""",
    longDesc =
u"""
8/ 9/ 4 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)O
Imported from thermo.txt.
""",
)

entry(
    index = 274,
    label = "ic4h7",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.3874,0.0206785,2.893e-05,-5.37553e-08,2.3567e-11,14758.4,15.5529], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.3497,0.0192508,-6.8136e-06,1.08485e-09,-6.42422e-14,12440.7,-18.7061], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t05/04""",
    longDesc =
u"""
t05/04.
[CH2]C(=C)C
Imported from thermo.txt.
""",
)

entry(
    index = 275,
    label = "hoch2o",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11183,0.00753851,3.77337e-06,-5.38746e-09,1.45616e-12,-22802.3,7.46807], Tmin=(298,'K'), Tmax=(1452,'K')),
            NASAPolynomial(coeffs=[6.39522,0.00743673,-2.50422e-06,3.8488e-10,-2.21779e-14,-24110.9,-6.63866], Tmin=(1452,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/16/99 therm""",
    longDesc =
u"""
2/16/99 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]CO
Imported from thermo.txt.
""",
)

entry(
    index = 276,
    label = "ch2ocho",
    molecule =
"""
multiplicity 2
1 C u1 p0 c0 {3,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {4,D} {7,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31032,0.0180474,-2.7152e-06,-4.60919e-09,1.70037e-12,-20291.1,17.155], Tmin=(298,'K'), Tmax=(1442,'K')),
            NASAPolynomial(coeffs=[10.096,0.00719887,-2.59813e-06,4.18111e-10,-2.48723e-14,-23638.9,-27.1144], Tmin=(1442,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/15/ 8 therm""",
    longDesc =
u"""
4/15/ 8 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]OC=O
Imported from thermo.txt.
""",
)

entry(
    index = 277,
    label = "c4h71-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,D} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77146,0.0146544,3.70081e-05,-5.72714e-08,2.36641e-11,25801.5,9.11907], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.16689,0.019568,-6.95695e-06,1.11504e-09,-6.64079e-14,23753.7,-17.7041], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t05/04""",
    longDesc =
u"""
t05/04.
C=[C]CC
Imported from thermo.txt.
""",
)

entry(
    index = 278,
    label = "ic3h7o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u1 p2 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.818261,0.0468807,-3.74369e-05,1.55917e-08,-2.64308e-12,-8151.53,27.9483], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[12.3135,0.0138063,-4.91586e-06,8.21076e-10,-5.07493e-14,-12471.7,-41.7271], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 9/ 4 therm""",
    longDesc =
u"""
8/ 9/ 4 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)[O]
Imported from thermo.txt.
""",
)

entry(
    index = 279,
    label = "ch3och2o",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u1 p2 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25889,0.0222146,-7.78556e-06,-2.41484e-10,4.51914e-13,-19237.7,12.368], Tmin=(298,'K'), Tmax=(2012,'K')),
            NASAPolynomial(coeffs=[8.60262,0.0135772,-4.84662e-06,7.77766e-10,-4.62634e-14,-21376.2,-17.5775], Tmin=(2012,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/ 9/96 therm""",
    longDesc =
u"""
2/ 9/96 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
COC[O]
Imported from thermo.txt.
""",
)

entry(
    index = 280,
    label = "nc3h7cho",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.30068,0.00500213,8.1222e-05,-1.07816e-07,4.25781e-11,-27119.8,4.93593], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.2351,0.0232201,-8.46144e-06,1.3759e-09,-8.27046e-14,-30034.6,-28.2583], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t05/09""",
    longDesc =
u"""
t05/09.
CCCC=O
Imported from thermo.txt.
""",
)

entry(
    index = 281,
    label = "c3ket21",
    molecule =
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.55686,0.0357077,-1.94712e-05,4.70695e-09,-3.69754e-13,-38671.1,9.97762], Tmin=(298,'K'), Tmax=(1371,'K')),
            NASAPolynomial(coeffs=[15.6378,0.0144059,-5.08808e-06,8.07076e-10,-4.75296e-14,-43065.8,-51.3106], Tmin=(1371,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 282,
    label = "nc3h7o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.21935,0.00738557,6.02826e-05,-8.3868e-08,3.39623e-11,-6234.92,8.0814], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.38041,0.0195206,-6.97374e-06,1.12145e-09,-6.69468e-14,-8486.25,-18.9916], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t07/10""",
    longDesc =
u"""
t07/10.
CCC[O]
Imported from thermo.txt.
""",
)

entry(
    index = 283,
    label = "nc3h7co",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67257,0.0371199,-2.06863e-05,5.48874e-09,-5.35864e-13,-8580.51,16.4849], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[13.0026,0.0163105,-5.57643e-06,8.65671e-10,-5.02256e-14,-12552.3,-40.2609], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""9/27/95 therm""",
    longDesc =
u"""
9/27/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[C]=O
Imported from thermo.txt.
""",
)

entry(
    index = 284,
    label = "c4h72-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u1 p0 c0 {2,S} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.61389,-0.00906923,8.28486e-05,-9.61204e-08,3.59334e-11,24497.2,-5.90519], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.26612,0.0199858,-7.12031e-06,1.14276e-09,-6.81207e-14,23191.6,-10.9942], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t05/04""",
    longDesc =
u"""
t05/04.
C[C]=CC
Imported from thermo.txt.
""",
)

entry(
    index = 285,
    label = "c2h3cho",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {5,D} {8,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.292355,0.0354321,-2.94936e-05,1.281e-08,-2.26144e-12,-11652.2,22.8878], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[10.4185,0.00948963,-3.29311e-06,5.16279e-10,-3.01587e-14,-14963,-30.7235], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/26/95 therm""",
    longDesc =
u"""
6/26/95 therm
c2h3cho           t11/10c  3 h  4 o  1    0 g   200.000  6000.00  1000.00      1
8.20654919e+00 1.28492916e-02-4.64285331e-06 7.51738738e-10-4.51298116e-14    2
-1.18838341e+04-1.49881933e+01 4.69868861e+00 4.99965957e-03 4.38587397e-05    3
-6.12883900e-08 2.48508985e-11-1.00875286e+04 7.29812046e+00-8.18629119e+03    4

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC=O
Imported from thermo.txt.
""",
)

entry(
    index = 286,
    label = "c2h5o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {4,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.57329,0.035238,-2.53204e-05,9.56802e-09,-1.48167e-12,-21527.8,19.0472], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[11.2306,0.0120482,-3.9673e-06,6.00755e-10,-3.42658e-14,-24797.8,-32.5607], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/14/ 5 therm""",
    longDesc =
u"""
1/14/ 5 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 287,
    label = "c2h5o2",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.50099,0.00687965,4.74144e-05,-6.92287e-08,2.87395e-11,-5395.48,7.9149], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.88872,0.0135833,-4.91117e-06,7.92343e-10,-4.73526e-14,-7441.07,-19.079], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t10/10""",
    longDesc =
u"""
t10/10.
CCO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 288,
    label = "c2h3co",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.36242,0.0315274,-3.00219e-05,1.48167e-08,-2.87972e-12,4257.7,17.2627], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[9.37468,0.00791297,-2.67198e-06,4.11115e-10,-2.36979e-14,1929.7,-24.0893], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 therm""",
    longDesc =
u"""
4/ 3/ 0 therm
c2h3co            a10/04c  3 h  3 o  1    0 g   200.000  6000.00  1000.00      1
6.90703955e+00 1.02341927e-02-3.65649593e-06 5.87914100e-10-3.51359226e-14    2
7.62708561e+03-7.29856114e+00 4.11237192e+00 5.05829116e-03 3.17832265e-05    3
-4.55489258e-08 1.86325507e-11 8.99713585e+03 1.01743843e+01 1.06476509e+04    4

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C[C]=O
Imported from thermo.txt.
""",
)

entry(
    index = 289,
    label = "c3h6cho-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {9,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67672,0.0373064,-2.11281e-05,5.80473e-09,-6.09688e-13,-2497.14,17.5751], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[13.0323,0.0162418,-5.54388e-06,8.59724e-10,-4.9846e-14,-6459.16,-39.2399], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""9/27/95 therm""",
    longDesc =
u"""
9/27/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC=O
Imported from thermo.txt.
""",
)

entry(
    index = 290,
    label = "ic3h6cho",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {9,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.521482,0.0443114,-2.86617e-05,9.3032e-09,-1.20762e-12,-2996.77,26.8182], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.3102,0.0162098,-5.57576e-06,8.69004e-10,-5.05554e-14,-7621.78,-42.5051], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/22/96 therm""",
    longDesc =
u"""
2/22/96 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)C=O
Imported from thermo.txt.
""",
)

entry(
    index = 291,
    label = "o2cho",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96059,0.0106002,-5.25713e-06,1.01717e-09,-2.87488e-14,-17359.9,11.7807], Tmin=(298,'K'), Tmax=(1368,'K')),
            NASAPolynomial(coeffs=[7.24075,0.00463313,-1.63694e-06,2.59707e-10,-1.52965e-14,-18702.8,-6.49547], Tmin=(1368,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/26/95 therm""",
    longDesc =
u"""
6/26/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OC=O
Imported from thermo.txt.
""",
)

entry(
    index = 292,
    label = "ch2o2h",
    molecule =
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47228,0.0133401,-5.9292e-06,4.44481e-10,2.127e-13,5674.14,4.72608], Tmin=(298,'K'), Tmax=(1357,'K')),
            NASAPolynomial(coeffs=[9.10784,0.0052726,-1.88171e-06,3.00561e-10,-1.77866e-14,3774.4,-21.1741], Tmin=(1357,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/14/ 5 therm""",
    longDesc =
u"""
1/14/ 5 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]OO
Imported from thermo.txt.
""",
)

entry(
    index = 293,
    label = "ch2chchcho",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {5,S}
2  C u0 p0 c0 {1,D} {4,S} {6,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {7,D} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  O u0 p2 c0 {4,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.082,0.036493,-1.52256e-05,-5.62607e-18,2.16114e-21,3567.13,32.7143], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.90968,0.0134364,-7.62977e-07,-1.69115e-09,2.9554e-13,1488.99,-17.9662], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t03/97""",
    longDesc =
u"""
t03/97.
[CH2]C=CC=O
Imported from thermo.txt.
""",
)

entry(
    index = 294,
    label = "ch3chchcho",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.55578,0.0409641,-1.69869e-05,-6.00928e-18,2.31369e-21,-14139.5,37.4708], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.8795,-0.0209131,4.45361e-05,-2.60375e-08,4.86836e-12,-19527.9,-68.72], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""t 5/92""",
    longDesc =
u"""
t 5/92
Low T polynomial Tmin changed from 298.15 to 298.0 K when importing to RMG.
CC=CC=O
Imported from thermo.txt.
""",
)

entry(
    index = 295,
    label = "ch3oco",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.75564,0.00780915,1.62273e-05,-2.41211e-08,9.42645e-12,-21515.7,4.78096], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.00172,0.0101977,-3.65622e-06,5.89475e-10,-3.52561e-14,-22613.6,-9.05268], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t10/07""",
    longDesc =
u"""
t10/07.
CO[C]=O
Imported from thermo.txt.
""",
)

entry(
    index = 296,
    label = "c2h3choch2",
    molecule =
"""
multiplicity 3
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {5,S} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u1 p0 c0 {5,S} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.797985,0.0344034,-1.24599e-05,-5.18063e-18,1.9936e-21,-648.928,21.8897], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-4.72093,0.0391414,-6.52873e-06,-7.68209e-09,2.51473e-12,1753.52,51.719], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""a 8/83""",
    longDesc =
u"""
a 8/83
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=CO[CH2]
Imported from thermo.txt.
""",
)

entry(
    index = 297,
    label = "ch3chchco",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.082,0.036493,-1.52256e-05,-5.62607e-18,2.16114e-21,3567.13,32.7143], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.90968,0.0134364,-7.62977e-07,-1.69115e-09,2.9554e-13,1488.99,-17.9662], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t03/97""",
    longDesc =
u"""
t03/97.
CC=C[C]=O
Imported from thermo.txt.
""",
)

entry(
    index = 298,
    label = "ch3och2o2h",
    molecule =
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  O u0 p2 c0 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.737369,0.046741,-3.73052e-05,1.50735e-08,-2.43782e-12,-37326,25.7933], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[14.6617,0.0120545,-4.13605e-06,6.43722e-10,-3.74189e-14,-41889.6,-48.1293], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/20/11""",
    longDesc =
u"""
1/20/11
ch3och2o2h 7/20/98 thermc   2h   6o   3    0g   300.000  5000.000 1392.000    41
1.49370964e+01 1.19465829e-02-4.12746359e-06 6.45422590e-10-3.76427939e-14    2
-4.11001068e+04-4.99552737e+01 1.19855761e+00 4.59060764e-02-3.66252420e-05    3
1.49318970e-08-2.46057445e-12-3.65363161e+04 2.31339904e+01                   4
HJC

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
COCOO
Imported from thermo.txt.
""",
)

entry(
    index = 299,
    label = "c4h2",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,T}
2 C u0 p0 c0 {1,S} {4,T}
3 C u0 p0 c0 {1,T} {5,S}
4 C u0 p0 c0 {2,T} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00519,0.01981,-9.86588e-06,-6.63516e-09,6.07741e-12,54240.7,1.84574], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.03141,0.00604725,-1.94879e-06,2.75486e-10,-1.38561e-14,52947.4,-23.8507], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121686""",
    longDesc =
u"""
121686
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC#C
Imported from thermo.txt.
""",
)

entry(
    index = 300,
    label = "tc3h6ocho",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.37083,0.0538476,-3.82478e-05,1.32882e-08,-1.79229e-12,-21839.1,25.8142], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[17.0371,0.0154401,-5.28333e-06,8.21085e-10,-4.76898e-14,-27587.2,-63.7271], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/25/95 therm""",
    longDesc =
u"""
8/25/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)([O])C=O
Imported from thermo.txt.
""",
)

entry(
    index = 301,
    label = "ic3h7co",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.503453,0.0441608,-2.82139e-05,8.93549e-09,-1.11327e-12,-9077.55,26.1991], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.3306,0.0161874,-5.56711e-06,8.67576e-10,-5.04697e-14,-13730.7,-43.3959], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/22/96 therm""",
    longDesc =
u"""
2/22/96 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)[C]=O
Imported from thermo.txt.
""",
)

entry(
    index = 302,
    label = "tc3h6cho",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87053,0.041487,-2.66816e-05,9.01532e-09,-1.27871e-12,-8977.31,16.6174], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[13.1013,0.0166392,-5.68458e-06,8.81808e-10,-5.1129e-14,-13063.9,-44.2706], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/22/96 therm""",
    longDesc =
u"""
2/22/96 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)C=O
Imported from thermo.txt.
""",
)

entry(
    index = 303,
    label = "c4h3-i",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.08304,0.0408343,-6.21597e-05,5.16794e-08,-1.70292e-11,58005.1,13.6175], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.09782,0.00922071,-3.38784e-06,4.91605e-10,-1.45298e-14,56600.6,-19.8026], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ab1/93""",
    longDesc =
u"""
ab1/93
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#C[C]=C
Imported from thermo.txt.
""",
)

entry(
    index = 304,
    label = "c4h3-n",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,T}
3 C u1 p0 c0 {1,D} {6,S}
4 C u0 p0 c0 {2,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.316841,0.0469121,-6.80938e-05,5.31799e-08,-1.6523e-11,62476.2,24.6226], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.43283,0.016861,-9.43131e-06,2.57039e-09,-2.74563e-13,61600.7,-1.5674], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""h6w/94""",
    longDesc =
u"""
h6w/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC#C
Imported from thermo.txt.
""",
)

entry(
    index = 305,
    label = "c2h5coch3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.087973,0.0462285,-2.79764e-05,8.48737e-09,-1.03074e-12,-30506.3,28.2501], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[12.9205,0.0189952,-6.51524e-06,1.01338e-09,-5.88684e-14,-35280.5,-41.7145], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11/23/ 9 therm""",
    longDesc =
u"""
11/23/ 9 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(C)=O
Imported from thermo.txt.
""",
)

entry(
    index = 306,
    label = "c2h5coch2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,D}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.54014,0.0439486,-2.97002e-05,1.05495e-08,-1.58599e-12,-9507.97,19.9707], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[14.2099,0.0157866,-5.50529e-06,8.65871e-10,-5.06913e-14,-14128.5,-48.7133], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 therm""",
    longDesc =
u"""
4/ 3/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(=O)CC
Imported from thermo.txt.
""",
)

entry(
    index = 307,
    label = "ch2ch2coch3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.40256,0.0367294,-1.97317e-05,5.07323e-09,-4.99655e-13,-6150.07,19.3993], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[12.4694,0.0171022,-5.92157e-06,9.26817e-10,-5.40731e-14,-10137.8,-36.2186], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/21/95 ther""",
    longDesc =
u"""
6/21/95 ther
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(C)=O
Imported from thermo.txt.
""",
)

entry(
    index = 308,
    label = "ch3chcoch3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.812941,0.0429257,-2.6923e-05,8.59327e-09,-1.13188e-12,-10524.7,23.2953], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[13.1388,0.0166091,-5.76924e-06,9.04978e-10,-5.28827e-14,-15116.2,-43.8877], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 therm""",
    longDesc =
u"""
4/ 3/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C(C)[O]
Imported from thermo.txt.
""",
)

entry(
    index = 309,
    label = "c3h6cho-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35169,0.0423714,-2.69123e-05,8.70133e-09,-1.15287e-12,-6911.67,20.9382], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[13.4302,0.0162251,-5.60632e-06,8.76356e-10,-5.10864e-14,-11356.1,-44.7371], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11/15/95 therm""",
    longDesc =
u"""
11/15/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]C=O
Imported from thermo.txt.
""",
)

entry(
    index = 310,
    label = "ch3och2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.72101,0.0378155,-2.89669e-05,1.16796e-08,-1.93234e-12,-20530.9,21.9296], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[12.2024,0.0119225,-4.06625e-06,6.3008e-10,-3.65065e-14,-24032.7,-33.8665], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/20/11""",
    longDesc =
u"""
1/20/11
HJC

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
COCO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 311,
    label = "ch3coch2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.95535,0.0270255,-1.37385e-05,3.53736e-09,-4.03923e-13,-20667.9,5.21436], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[12.769,0.0142555,-4.92821e-06,7.70449e-10,-4.49111e-14,-23479.9,-32.7156], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/14/95""",
    longDesc =
u"""
2/14/95
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)CO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 312,
    label = "o2ch2cho",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.29466,0.0444936,-4.26577e-05,2.07392e-08,-3.96829e-12,-11827.6,36.0779], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[11.1808,0.00914479,-3.1509e-06,4.91944e-10,-2.86639e-14,-15579,-28.7893], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""boz_03""",
    longDesc =
u"""
boz_03
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCC=O
Imported from thermo.txt.
""",
)

entry(
    index = 313,
    label = "ho2ch2co",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {4,S}
3 C u1 p0 c0 {1,S} {7,D}
4 O u0 p2 c0 {2,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22682,0.0356781,-3.26402e-05,1.47652e-08,-2.64794e-12,-11873.5,19.1581], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[10.4146,0.011268,-5.17495e-06,1.00333e-09,-6.68166e-14,-14095.6,-22.7894], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""boz_03""",
    longDesc =
u"""
boz_03
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=[C]COO
Imported from thermo.txt.
""",
)

entry(
    index = 314,
    label = "hoch2oco",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {7,S}
4 C u1 p0 c0 {2,S} {8,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.08181,0.0128768,2.04419e-06,-6.10155e-09,1.79821e-12,-43952.6,2.54054], Tmin=(298,'K'), Tmax=(1603,'K')),
            NASAPolynomial(coeffs=[11.3737,0.00817664,-2.92034e-06,4.66696e-10,-2.76277e-14,-46557.6,-28.6035], Tmin=(1603,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/31/99 therm""",
    longDesc =
u"""
8/31/99 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=[C]OCO
Imported from thermo.txt.
""",
)

entry(
    index = 315,
    label = "och2ocho",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,D} {8,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92798,0.0185731,-4.14657e-07,-6.9406e-09,2.32311e-12,-40707.1,10.2049], Tmin=(298,'K'), Tmax=(1426,'K')),
            NASAPolynomial(coeffs=[12.4378,0.00782259,-2.82874e-06,4.55809e-10,-2.71392e-14,-44452.6,-38.5337], Tmin=(1426,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/20/11""",
    longDesc =
u"""
1/20/11
och2ocho   4/ 9/98 thermc   2h   3o   3    0g   300.000  5000.000 1475.000    21
1.20233916e+01 8.11262659e-03-2.91356462e-06 4.67340384e-10-2.77375525e-14    2
-4.33647231e+04-3.33691809e+01 5.19690837e+00 1.58839723e-02 3.53540547e-07    3
-6.10456923e-09 1.94661801e-12-4.02242792e+04 6.11645828e+00                   4
HJC

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]COC=O
Imported from thermo.txt.
""",
)

entry(
    index = 316,
    label = "c3h6cho-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  C u0 p0 c0 {1,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.95068,0.0334223,-1.45357e-05,1.67282e-09,2.62012e-13,-3790.34,17.4324], Tmin=(298,'K'), Tmax=(1682,'K')),
            NASAPolynomial(coeffs=[11.1943,0.0181807,-6.35917e-06,1.00727e-09,-5.93944e-14,-6868.26,-28.0299], Tmin=(1682,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11/15/95 therm""",
    longDesc =
u"""
11/15/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CC=O
Imported from thermo.txt.
""",
)

entry(
    index = 317,
    label = "c2h4o1-2",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75905,-0.00944122,8.03097e-05,-1.00808e-07,4.00399e-11,-7560.81,7.84975], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.48876,0.0120462,-4.33369e-06,7.00283e-10,-4.19491e-14,-9180.43,-7.07996], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""l 8/88""",
    longDesc =
u"""
l 8/88.
C1CO1
Imported from thermo.txt.
""",
)

entry(
    index = 318,
    label = "c2h4o2h",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46917,0.0271189,-2.08023e-05,8.44285e-09,-1.40756e-12,3896.88,14.3401], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[10.5229,0.00948091,-3.55728e-06,6.41446e-10,-4.21232e-14,1557.18,-23.1414], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/14/ 5 therm""",
    longDesc =
u"""
1/14/ 5 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]COO
Imported from thermo.txt.
""",
)

entry(
    index = 319,
    label = "c2h3o1-2",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {6,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58349,-0.00602276,6.32427e-05,-8.18541e-08,3.30445e-11,18568.1,9.59726], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.60158,0.00917614,-3.28029e-06,5.27904e-10,-3.15362e-14,17144.6,-5.47229], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""a 1/05""",
    longDesc =
u"""
a 1/05.
[CH]1CO1
Imported from thermo.txt.
""",
)

entry(
    index = 320,
    label = "tc3h6ohcho",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.210034,0.0563086,-3.95159e-05,1.3778e-08,-1.89069e-12,-48040.3,26.7836], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[17.0789,0.0174006,-5.93008e-06,9.18861e-10,-5.32512e-14,-53873,-63.8639], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 1/95 therm""",
    longDesc =
u"""
8/ 1/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(O)C=O
Imported from thermo.txt.
""",
)

entry(
    index = 321,
    label = "c3h5o",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.19823,0.030558,-1.8063e-05,4.8615e-09,-4.19855e-13,9582.18,21.5566], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[10.2552,0.0114984,-3.84646e-06,5.8891e-10,-3.38558e-14,6265.61,-27.7655], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/95 therm""",
    longDesc =
u"""
7/20/95 therm
c3h5o             a11/04c  3 h  5 o  1    0 g   200.000  6000.00  1000.00      1
8.15052559e+00 1.42542561e-02-5.05387276e-06 8.08732845e-10-4.81184188e-14    2
8.72987262e+03-1.69520239e+01 3.53458477e+00 8.02398508e-03 4.85256807e-05    3
-7.23549959e-08 3.03822687e-11 1.08059525e+04 1.11545728e+01 1.25165081e+04    4

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC[O]
Imported from thermo.txt.
""",
)

entry(
    index = 322,
    label = "nc3h7o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.99489,-0.00750355,0.000101251,-1.25013e-07,4.84676e-11,-7530.04,-2.0374], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.2449,0.0214801,-7.69336e-06,1.23945e-09,-7.40912e-14,-9811.88,-22.0401], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t04/10""",
    longDesc =
u"""
t04/10.
CCCO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 323,
    label = "nc3h7o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.08978,-0.00486163,0.000103254,-1.33201e-07,5.30799e-11,-24419.5,1.74859], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.4116,0.0213764,-7.5582e-06,1.20207e-09,-7.11798e-14,-26893.5,-23.5429], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t02/10""",
    longDesc =
u"""
t02/10.
CCCOO
Imported from thermo.txt.
""",
)

entry(
    index = 324,
    label = "c3h6ooh1-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87775,0.0374167,-2.36058e-05,7.79931e-09,-1.06043e-12,-782.368,19.3941], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[12.4606,0.015889,-5.32742e-06,8.15819e-10,-4.68723e-14,-4203.05,-32.3859], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]COO
Imported from thermo.txt.
""",
)

entry(
    index = 325,
    label = "hoch2o2h",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {7,S}
4 O u0 p2 c0 {2,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.85717,0.0323153,-2.69929e-05,1.11694e-08,-1.81284e-12,-40031.4,19.0918], Tmin=(298,'K'), Tmax=(1422,'K')),
            NASAPolynomial(coeffs=[11.6304,0.00715134,-2.39035e-06,3.65773e-10,-2.102e-14,-43107.9,-32.4277], Tmin=(1422,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 9/98 therm""",
    longDesc =
u"""
4/ 9/98 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OCOO
Imported from thermo.txt.
""",
)

entry(
    index = 326,
    label = "c4h8ooh1-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {5,S} {14,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.36088,0.0446153,-2.14785e-05,3.1462e-09,3.03153e-13,-6899.5,12.4757], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[18.0477,0.0192137,-6.66503e-06,1.04468e-09,-6.10171e-14,-12307,-63.3581], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""3/27/97 therm""",
    longDesc =
u"""
3/27/97 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]OO
Imported from thermo.txt.
""",
)

entry(
    index = 327,
    label = "ic4h9o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.21434,0.0545388,-3.67002e-05,1.34131e-08,-2.11742e-12,-11848.2,23.4153], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[15.9741,0.0213535,-7.39001e-06,1.15624e-09,-6.74408e-14,-17232.9,-56.5302], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)CO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 328,
    label = "ic4h9o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.244182,0.0634028,-4.49162e-05,1.67407e-08,-2.61216e-12,-28696,27.2156], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[18.4309,0.0215338,-7.48624e-06,1.17499e-09,-6.86891e-14,-35148.3,-70.8031], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)COO
Imported from thermo.txt.
""",
)

entry(
    index = 329,
    label = "o2c2h4oh",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  O u0 p2 c0 {1,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11839,0.0272241,-1.60824e-05,5.17033e-09,-7.3161e-13,-23085.8,12.8482], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[10.7433,0.0130958,-4.4537e-06,6.88549e-10,-3.9823e-14,-25591.1,-23.3255], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/14/95 therm""",
    longDesc =
u"""
2/14/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCO
Imported from thermo.txt.
""",
)

entry(
    index = 330,
    label = "c4h8ooh2-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {3,S} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.40329,0.0430479,-2.14076e-05,4.28267e-09,-1.27805e-13,-9794.32,13.0514], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[16.3838,0.0204423,-7.04525e-06,1.09928e-09,-6.39967e-14,-14561.6,-53.3147], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""3/27/97 therm""",
    longDesc =
u"""
3/27/97 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[C](C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 331,
    label = "c3ket12",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,D} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.10507,0.0527397,-4.31806e-05,1.81618e-08,-3.10536e-12,-36362.8,25.4112], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[17.0756,0.0131013,-4.61949e-06,7.31991e-10,-4.30789e-14,-41700.9,-59.5779], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C=O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 332,
    label = "c3h6ooh1-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {6,S}
5  O u0 p2 c0 {1,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.65197,0.0574638,-4.72191e-05,2.05592e-08,-3.68787e-12,-20882.9,20.1548], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.1759,0.0159857,-5.61306e-06,8.8688e-10,-5.20877e-14,-26441.2,-67.7513], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 trm""",
    longDesc =
u"""
7/19/ 0 trm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(COO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 333,
    label = "c4h6o23",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67053,0.00492586,8.86967e-05,-1.26219e-07,5.23991e-11,-10278.8,14.5722], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.60658,0.020831,-8.42229e-06,1.56718e-09,-1.09391e-13,-13239.3,-23.2465], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""t 3/97""",
    longDesc =
u"""
t 3/97.
C1=COCC1
Imported from thermo.txt.
""",
)

entry(
    index = 334,
    label = "c4h5-2",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {4,D} {8,S} {9,S}
3 C u1 p0 c0 {1,S} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96963,0.0244422,-9.12514e-06,-4.24669e-18,1.63047e-21,35503.3,12.0361], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.5382,-0.00856771,2.35595e-05,-1.36764e-08,2.44369e-12,33259.1,-45.3695], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""h6w/94""",
    longDesc =
u"""
h6w/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C=[C]C
Imported from thermo.txt.
""",
)

entry(
    index = 335,
    label = "c4h612",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {4,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.02347,0.0349592,-2.2009e-05,6.94227e-09,-7.87919e-13,18118,19.7507], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.8156,-0.0042575,1.05118e-05,-4.47384e-09,5.84814e-13,12673.4,-69.8266], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""a 8/83""",
    longDesc =
u"""
a 8/83
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C=CC
Imported from thermo.txt.
""",
)

entry(
    index = 336,
    label = "c4h6-2",
    molecule =
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {2,S} {3,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13733,0.0264862,-9.05687e-06,-5.53864e-19,2.12819e-22,15710.9,13.5294], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.03381,0.00821245,7.1754e-06,-5.88343e-09,1.03439e-12,14335.1,-20.9858], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""a 8/83""",
    longDesc =
u"""
a 8/83
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC#CC
Imported from thermo.txt.
""",
)

entry(
    index = 337,
    label = "c3h6ooh2-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.65197,0.0574638,-4.72191e-05,2.05592e-08,-3.68787e-12,-20882.9,20.1548], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.1759,0.0159857,-5.61306e-06,8.8688e-10,-5.20877e-14,-26441.2,-67.7513], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 trm""",
    longDesc =
u"""
7/19/ 0 trm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CO[O])OO
Imported from thermo.txt.
""",
)

entry(
    index = 338,
    label = "c2h3ooh",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35644,0.0337002,-2.75989e-05,1.14223e-08,-1.89489e-12,-5499.97,19.8354], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[11.575,0.00809909,-2.81809e-06,4.42698e-10,-2.58998e-14,-8848.53,-34.3859], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/18/ 8 therm""",
    longDesc =
u"""
4/18/ 8 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=COO
Imported from thermo.txt.
""",
)

entry(
    index = 339,
    label = "c3h6ooh2-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09194,0.046922,-3.90281e-05,1.72381e-08,-3.07969e-12,-1893.78,20.0178], Tmin=(298,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[14.2163,0.0143382,-4.78004e-06,7.29133e-10,-4.17762e-14,-5673.82,-43.5771], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 340,
    label = "ic3h7o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.49942,0.0443081,-3.22414e-05,1.29687e-08,-2.23371e-12,-10258.8,20.2336], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[13.2493,0.0164082,-5.67432e-06,8.87336e-10,-5.17362e-14,-14411,-42.9066], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 341,
    label = "c3h6o1-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42807,0.00625177,6.13196e-05,-8.60387e-08,3.51371e-11,-12844.7,10.4245], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.01491,0.017392,-6.26028e-06,1.01188e-09,-6.06239e-14,-15198.1,-18.828], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""a01/05""",
    longDesc =
u"""
a01/05.
CC1CO1
Imported from thermo.txt.
""",
)

entry(
    index = 342,
    label = "ic3h7o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.519266,0.0532111,-4.05157e-05,1.63347e-08,-2.73751e-12,-27104.8,24.0815], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[15.7046,0.0165925,-5.77251e-06,9.06453e-10,-5.30084e-14,-32326.9,-57.1735], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 343,
    label = "c3h6ooh2-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09194,0.046922,-3.90281e-05,1.72381e-08,-3.07969e-12,-1893.78,20.0178], Tmin=(298,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[14.2163,0.0143382,-4.78004e-06,7.29133e-10,-4.17762e-14,-5673.82,-43.5771], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 344,
    label = "c4h8ooh1-2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {2,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.51698,0.0544584,-3.84524e-05,1.48146e-08,-2.42809e-12,-3497.28,26.4917], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[15.8328,0.020722,-7.09869e-06,1.10302e-09,-6.40252e-14,-8530.34,-50.44], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]COO
Imported from thermo.txt.
""",
)

entry(
    index = 345,
    label = "c4h8o1-2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.42033,0.0579309,-4.30236e-05,1.6668e-08,-2.64714e-12,-15395.1,36.6425], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[13.9197,0.0185551,-6.36014e-06,9.88845e-10,-5.74275e-14,-20945.3,-50.6788], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 therm""",
    longDesc =
u"""
4/ 3/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC1CO1
Imported from thermo.txt.
""",
)

entry(
    index = 346,
    label = "c4h8ooh1-2o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22401,0.0704995,-5.66979e-05,2.42628e-08,-4.29715e-12,-23739.1,23.8372], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.3244,0.0205475,-7.19076e-06,1.13362e-09,-6.64744e-14,-30546.8,-83.2666], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 trm""",
    longDesc =
u"""
7/19/ 0 trm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(COO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 347,
    label = "nc4ket12",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.805387,0.0652375,-5.18374e-05,2.13455e-08,-3.5986e-12,-39239.6,28.4908], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[20.2458,0.017644,-6.19055e-06,9.77688e-10,-5.74053e-14,-45814.2,-75.2145], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(C=O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 348,
    label = "c2h5chco",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.276601,0.0482967,-4.02377e-05,1.76564e-08,-3.14365e-12,-14171.7,24.7119], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[13.4101,0.0138767,-4.7413e-06,7.35504e-10,-4.26458e-14,-18379.1,-44.5295], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""9/27/95 therm""",
    longDesc =
u"""
9/27/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=C=O
Imported from thermo.txt.
""",
)

entry(
    index = 349,
    label = "c3h51-2,3ooh",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {7,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  O u0 p2 c0 {4,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5562,0.0613504,-5.23205e-05,2.28208e-08,-4.02232e-12,-13135.3,22.1044], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[21.2378,0.013952,-4.94539e-06,7.86381e-10,-4.63926e-14,-19286.5,-76.9637], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/26/3 thrm""",
    longDesc =
u"""
8/26/3 thrm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(COO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 350,
    label = "c3ket13",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,D} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55241,0.041872,-2.9455e-05,1.09983e-08,-1.75046e-12,-34890.3,14.2083], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[15.8927,0.0140991,-4.96119e-06,7.84992e-10,-4.61489e-14,-39377.5,-52.6049], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CCCOO
Imported from thermo.txt.
""",
)

entry(
    index = 351,
    label = "c4h8ooh2-1",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.01712,0.0610561,-4.65789e-05,1.88024e-08,-3.15266e-12,-5373.91,26.306], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[18.4556,0.0189544,-6.59381e-06,1.03538e-09,-6.05467e-14,-11363.7,-66.9839], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(CC)OO
Imported from thermo.txt.
""",
)

entry(
    index = 352,
    label = "ch3co2",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.37441,0.0249116,-1.74309e-05,6.248e-09,-9.09517e-13,-27233,18.1405], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[8.5406,0.00832951,-2.84722e-06,4.41927e-10,-2.56373e-14,-29729.1,-20.3884], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/14/95 therm""",
    longDesc =
u"""
2/14/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC([O])=O
Imported from thermo.txt.
""",
)

entry(
    index = 353,
    label = "ch3co3",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 O u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60373,0.027008,-2.08293e-05,8.50541e-09,-1.43846e-12,-23420.5,11.2015], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[11.2522,0.00833653,-2.89015e-06,4.52782e-10,-2.64354e-14,-26023.9,-29.637], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 therm""",
    longDesc =
u"""
4/ 3/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 354,
    label = "c2h3coch3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.245579,0.0426432,-2.91127e-05,1.03478e-08,-1.53551e-12,-17030.5,26.4431], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[12.5572,0.0149673,-5.20015e-06,8.15864e-10,-4.76824e-14,-21462.3,-40.1434], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/19/95 therm""",
    longDesc =
u"""
6/19/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(C)=O
Imported from thermo.txt.
""",
)

entry(
    index = 355,
    label = "ch3co3h",
    molecule =
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {8,D}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 O u0 p2 c0 {2,D}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.24136,0.0337964,-2.53887e-05,9.67584e-09,-1.49266e-12,-42467.8,17.0668], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[12.506,0.0094779,-3.30402e-06,5.19631e-10,-3.04234e-14,-45985.7,-37.9196], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/26/95 therm""",
    longDesc =
u"""
6/26/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 356,
    label = "ch2choohcoch3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.55205,0.0608201,-5.04704e-05,2.16348e-08,-3.75674e-12,-18956.4,27.1012], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[19.3158,0.0156593,-5.45396e-06,8.5716e-10,-5.01583e-14,-24775.2,-67.0297], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/27/95""",
    longDesc =
u"""
6/27/95
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(OO)C(C)=O
Imported from thermo.txt.
""",
)

entry(
    index = 357,
    label = "sc4h9o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.340588,0.0652078,-4.8484e-05,1.91012e-08,-3.13833e-12,-30000.8,27.2835], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[18.8588,0.0211201,-7.33206e-06,1.1497e-09,-6.71657e-14,-36423.6,-72.0026], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 358,
    label = "ch3choococh3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.59405,0.0574729,-4.65071e-05,2.01817e-08,-3.61176e-12,-25344.5,26.0857], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[17.2171,0.017674,-6.10387e-06,9.53712e-10,-5.55757e-14,-30528,-56.796], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/27/95""",
    longDesc =
u"""
6/27/95
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)C(C)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 359,
    label = "sc4h9o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.28258,0.00926839,8.83567e-05,-1.23824e-07,5.03388e-11,-12997.7,4.27237], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.205,0.0248733,-9.02932e-06,1.46076e-09,-8.74287e-14,-16496.6,-39.6133], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t04/09""",
    longDesc =
u"""
t04/09.
CCC(C)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 360,
    label = "ho2ch2ocho",
    molecule =
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,D} {9,S}
3  O u0 p2 c0 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.515433,0.0476082,-3.63878e-05,1.24225e-08,-1.50813e-12,-58273,28.1993], Tmin=(298,'K'), Tmax=(1428,'K')),
            NASAPolynomial(coeffs=[17.8528,0.00754042,-2.74896e-06,4.45343e-10,-2.66154e-14,-64138,-64.7357], Tmin=(1428,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/20/11""",
    longDesc =
u"""
1/20/11
ho2ch2ocho 8/31/99 thermc   2h   4o   4    0g   300.000  5000.000 1387.000    41
1.64584298e+01 8.52683511e-03-3.04113500e-06 4.85596908e-10-2.87316334e-14    2
-6.23959608e+04-5.38924139e+01 3.47935703e+00 4.02952392e-02-3.30109296e-05    3
1.34360117e-08-2.18601580e-12-5.80629934e+04 1.52521392e+01                   4
HJC

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=COCOO
Imported from thermo.txt.
""",
)

entry(
    index = 361,
    label = "ic4h8o2h-t",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77633,0.0450889,-2.62424e-05,7.74737e-09,-9.1152e-13,-5982.96,15.3503], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[15.2395,0.0206497,-6.94792e-06,1.06651e-09,-6.13783e-14,-10227.1,-47.0909], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)COO
Imported from thermo.txt.
""",
)

entry(
    index = 362,
    label = "tc4h8o2h-i",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.5747,0.0604649,-4.84992e-05,2.05236e-08,-3.52975e-12,-6541.91,21.6853], Tmin=(298,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[17.806,0.0184953,-6.21268e-06,9.52754e-10,-5.4801e-14,-11755.6,-64.018], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)(C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 363,
    label = "tc4h9o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.45495,0.0289185,3.68274e-05,-7.18116e-08,3.1878e-11,-15610.4,9.17831], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.4566,0.0240864,-8.56308e-06,1.36853e-09,-8.12707e-14,-18969,-41.8792], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t04/08""",
    longDesc =
u"""
t04/08.
CC(C)(C)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 364,
    label = "ic3h5cho",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {8,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.627184,0.046678,-3.74431e-05,1.58331e-08,-2.73952e-12,-15720.3,21.6034], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[13.6204,0.0137917,-4.7337e-06,7.36655e-10,-4.20098e-14,-20002.5,-47.3185], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/95 therm""",
    longDesc =
u"""
7/19/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)C=O
Imported from thermo.txt.
""",
)

entry(
    index = 365,
    label = "tc4h9o2h",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96033,0.0406267,1.85652e-05,-5.72129e-08,2.73015e-11,-32046.7,7.55566], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.2702,0.0256463,-9.02796e-06,1.43759e-09,-8.52382e-14,-35853.9,-54.4967], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t02/10""",
    longDesc =
u"""
t02/10.
CC(C)(C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 366,
    label = "c4h4o",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,D} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {5,S} {8,S}
4 C u0 p0 c0 {1,D} {5,S} {9,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.847469,0.0131774,5.99736e-05,-9.71563e-08,4.22734e-11,-5367.85,21.4945], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.38935,0.0140291,-5.07755e-06,8.24137e-10,-4.9532e-14,-8682.42,-27.9163], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""t03/97""",
    longDesc =
u"""
t03/97.
C1C=COC=1
Imported from thermo.txt.
""",
)

entry(
    index = 367,
    label = "ic3h5co",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  C u1 p0 c0 {2,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.85097,0.0418856,-3.62554e-05,1.65691e-08,-3.05851e-12,170.381,15.3014], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[13.0667,0.0116704,-3.99107e-06,6.19498e-10,-3.59348e-14,-3365.19,-43.5803], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 therm""",
    longDesc =
u"""
4/ 3/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)[C]=O
Imported from thermo.txt.
""",
)

entry(
    index = 368,
    label = "c3h5-s",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.913729,0.0264323,-1.1759e-05,-2.30357e-09,2.77155e-12,30916.9,19.9893], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.37253,0.0157805,-5.99229e-06,9.30897e-10,-3.6551e-14,29614.8,-3.41865], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""pd5/98""",
    longDesc =
u"""
pd5/98
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC
Imported from thermo.txt.
""",
)

entry(
    index = 369,
    label = "c3h5-t",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.73292,0.0223946,-5.14906e-06,-6.75965e-09,3.82532e-12,29040.5,16.5689], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.42555,0.0155111,-5.66784e-06,7.92244e-10,-1.6878e-14,27843,-3.35272], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""pd5/98""",
    longDesc =
u"""
pd5/98
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]C
Imported from thermo.txt.
""",
)

entry(
    index = 370,
    label = "c3h6o1-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.15284,-0.0186402,0.000129981,-1.5863e-07,6.20669e-11,-11324.4,4.73561], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.80717,0.0188825,-6.79082e-06,1.09714e-09,-6.57155e-14,-13654.8,-13.5382], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""a11/04""",
    longDesc =
u"""
a11/04.
C1COC1
Imported from thermo.txt.
""",
)

entry(
    index = 371,
    label = "c4h8ooh2-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.45436,0.0563121,-3.84161e-05,1.34229e-08,-1.92383e-12,-6689.16,25.4248], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[17.9338,0.0192154,-6.64487e-06,1.0394e-09,-6.0624e-14,-12576.8,-63.6194], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C(C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 372,
    label = "ic4h8ooh-to2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17782,0.0717785,-5.88836e-05,2.56759e-08,-4.61679e-12,-25562.2,20.7846], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[22.6383,0.0203246,-7.12391e-06,1.12425e-09,-6.59733e-14,-32440.7,-88.0388], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 trm""",
    longDesc =
u"""
7/19/ 0 trm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(COO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 373,
    label = "tc4h8ooh-io2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17782,0.0717785,-5.88836e-05,2.56759e-08,-4.61679e-12,-25562.2,20.7846], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[22.6383,0.0203246,-7.12391e-06,1.12425e-09,-6.59733e-14,-32440.7,-88.0388], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 trm""",
    longDesc =
u"""
7/19/ 0 trm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(CO[O])OO
Imported from thermo.txt.
""",
)

entry(
    index = 374,
    label = "c4h8o2-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.98701,0.0632679,-5.20856e-05,2.24064e-08,-3.95417e-12,-17195.7,36.692], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[15.8264,0.0164401,-5.8068e-06,9.21146e-10,-5.42511e-14,-23533.5,-63.4845], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/22/95 therm""",
    longDesc =
u"""
1/22/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1OC1C
Imported from thermo.txt.
""",
)

entry(
    index = 375,
    label = "c4h8ooh2-4",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.01712,0.0610561,-4.65789e-05,1.88024e-08,-3.15266e-12,-5373.91,26.306], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[18.4556,0.0189544,-6.59381e-06,1.03538e-09,-6.05467e-14,-11363.7,-66.9839], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 376,
    label = "ch2och2o2h",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u1 p0 c0 {3,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.908332,0.0447997,-3.69442e-05,1.48367e-08,-2.32279e-12,-15099.2,26.642], Tmin=(298,'K'), Tmax=(1419,'K')),
            NASAPolynomial(coeffs=[15.1031,0.00918263,-3.15895e-06,4.92789e-10,-2.87001e-14,-19661.2,-48.5173], Tmin=(1419,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/20/11""",
    longDesc =
u"""
1/20/11
ch3och2o2  7/20/98 thermc   2h   5o   3    0g   300.000  5000.000 1389.000    31
1.24249729e+01 1.18705986e-02-4.07906532e-06 6.35310809e-10-3.69427867e-14    2
-2.29679238e+04-3.53740145e+01 2.21029612e+00 3.68877454e-02-2.82561555e-05    3
1.15730533e-08-1.97130470e-12-1.94940940e+04 1.91463601e+01                   4
ch2och2o2h 7/20/98 thermc   2h   5o   3    0g   300.000  5000.000 1393.000    41
1.51191783e+01 9.23718883e-03-3.19127505e-06 4.99114678e-10-2.91162488e-14    2
-1.84114867e+04-4.85706618e+01 2.52895507e+00 4.24128290e-02-3.73406386e-05    3
1.66639333e-08-2.96443312e-12-1.44293306e+04 1.76899251e+01                   4
HJC

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]OCOO
Imported from thermo.txt.
""",
)

entry(
    index = 377,
    label = "o2ch2och2o2h",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
3  O u0 p2 c0 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {11,S}
6  O u0 p2 c0 {4,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 O u1 p2 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.12258,0.0664377,-6.55341e-05,3.13442e-08,-5.79043e-12,-34153,34.9113], Tmin=(298,'K'), Tmax=(1411,'K')),
            NASAPolynomial(coeffs=[19.6208,0.00996132,-3.4148e-06,5.31365e-10,-3.08902e-14,-39868,-67.2721], Tmin=(1411,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/20/11""",
    longDesc =
u"""
1/20/11
o2ch2och2o2h 7/20/98 trmc   2h   5o   5    0g   300.000  5000.000 1402.000    51
1.92038046e+01 1.04394841e-02-3.60582939e-06 5.63792843e-10-3.28807214e-14    2
-3.79207055e+04-6.51847273e+01 1.99640551e+00 5.83226232e-02-5.53259778e-05    3
2.59810540e-08-4.77141005e-12-3.27628742e+04 2.44215005e+01                   4
HJC

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCOCOO
Imported from thermo.txt.
""",
)

entry(
    index = 378,
    label = "c4h8o1-3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.5369,0.0543996,-3.4339e-05,1.0108e-08,-1.10263e-12,-15298.1,36.7401], Tmin=(298,'K'), Tmax=(1371,'K')),
            NASAPolynomial(coeffs=[15.4227,0.0170211,-6.06348e-06,9.67355e-10,-5.71992e-14,-22019.4,-61.3872], Tmin=(1371,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/22/95 therm""",
    longDesc =
u"""
1/22/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1CCO1
Imported from thermo.txt.
""",
)

entry(
    index = 379,
    label = "c3h6ooh1-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.88331,0.0440156,-3.07858e-05,1.13215e-08,-1.75323e-12,-168.779,21.4041], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[14.6882,0.0149941,-5.24057e-06,8.25463e-10,-4.83759e-14,-4773.43,-47.7984], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 380,
    label = "c3h6ooh1-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {6,S}
5  O u0 p2 c0 {3,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14865,0.0533543,-4.08331e-05,1.67542e-08,-2.89288e-12,-18547.4,18.6305], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[18.5917,0.0165329,-5.81344e-06,9.19397e-10,-5.40321e-14,-23959.9,-64.2544], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 trm""",
    longDesc =
u"""
7/19/ 0 trm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCCOO
Imported from thermo.txt.
""",
)

entry(
    index = 381,
    label = "ic4ketit",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.14244,0.0633841,-4.73085e-05,1.77145e-08,-2.67265e-12,-40936.7,23.4845], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[20.937,0.0171091,-6.01892e-06,9.52354e-10,-5.59926e-14,-47782,-82.7718], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(C=O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 382,
    label = "c4h8ooh1-3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.94106,0.0518789,-3.10412e-05,8.63569e-09,-8.42842e-13,-4343.16,24.023], Tmin=(298,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[17.6442,0.0191707,-6.57169e-06,1.02247e-09,-5.94305e-14,-10185.9,-61.7116], Tmin=(1377,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 383,
    label = "c4h8ooh2-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19248,0.0736763,-6.24428e-05,2.79371e-08,-5.10126e-12,-26177.4,22.9569], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[22.9951,0.0199239,-6.96327e-06,1.09678e-09,-6.42747e-14,-33009.5,-87.1462], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 trm""",
    longDesc =
u"""
7/19/ 0 trm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O[O])C(C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 384,
    label = "c4h8ooh2-4o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22401,0.0704995,-5.66979e-05,2.42628e-08,-4.29715e-12,-23739.1,23.8372], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.3244,0.0205475,-7.19076e-06,1.13362e-09,-6.64744e-14,-30546.8,-83.2666], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 trm""",
    longDesc =
u"""
7/19/ 0 trm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCO[O])OO
Imported from thermo.txt.
""",
)

entry(
    index = 385,
    label = "c4h8ooh1-4",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.45017,0.0572419,-4.06431e-05,1.52822e-08,-2.42123e-12,-3029.06,25.0738], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[17.8624,0.0195213,-6.80351e-06,1.06961e-09,-6.26001e-14,-8879.23,-63.4393], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCOO
Imported from thermo.txt.
""",
)

entry(
    index = 386,
    label = "c4h8ooh1-3o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22401,0.0704995,-5.66979e-05,2.42628e-08,-4.29715e-12,-23739.1,23.8372], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.3244,0.0205475,-7.19076e-06,1.13362e-09,-6.64744e-14,-30546.8,-83.2666], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 trm""",
    longDesc =
u"""
7/19/ 0 trm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCOO)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 387,
    label = "c4h8ooh1-4o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {4,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12352,0.0646726,-4.78358e-05,1.89657e-08,-3.18026e-12,-21466.4,20.4322], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[21.7116,0.0211216,-7.40101e-06,1.16773e-09,-6.8514e-14,-28048.3,-79.5885], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 trm""",
    longDesc =
u"""
7/19/ 0 trm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCCCOO
Imported from thermo.txt.
""",
)

entry(
    index = 388,
    label = "c4h8ooh2-1o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22401,0.0704995,-5.66979e-05,2.42628e-08,-4.29715e-12,-23739.1,23.8372], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.3244,0.0205475,-7.19076e-06,1.13362e-09,-6.64744e-14,-30546.8,-83.2666], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 trm""",
    longDesc =
u"""
7/19/ 0 trm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CO[O])OO
Imported from thermo.txt.
""",
)

entry(
    index = 389,
    label = "hoch2o2",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.85442,0.0233664,-1.88116e-05,7.9671e-09,-1.36347e-12,-22986.6,15.1731], Tmin=(298,'K'), Tmax=(1412,'K')),
            NASAPolynomial(coeffs=[9.04546,0.00715223,-2.37006e-06,3.60083e-10,-2.0575e-14,-24941.5,-17.4211], Tmin=(1412,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 9/98 therm""",
    longDesc =
u"""
4/ 9/98 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCO
Imported from thermo.txt.
""",
)

entry(
    index = 390,
    label = "nc4ket14",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40797,0.0537386,-3.72613e-05,1.36863e-08,-2.13799e-12,-37791.9,16.558], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[19.0284,0.0186605,-6.53616e-06,1.03102e-09,-6.04833e-14,-43467.9,-68.021], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CCCCOO
Imported from thermo.txt.
""",
)

entry(
    index = 391,
    label = "nc4ket13",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.74883,0.0586937,-4.49606e-05,1.832e-08,-3.11765e-12,-40106.6,18.8072], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.6431,0.0180941,-6.33063e-06,9.9786e-10,-5.85076e-14,-45958.9,-71.6905], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CC=O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 392,
    label = "ic4h6oh",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.863371,0.0468711,-3.4358e-05,1.33031e-08,-2.13915e-12,-3149.48,22.9076], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[14.0311,0.0155318,-5.32755e-06,8.28786e-10,-4.81545e-14,-7693.78,-47.6555], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/19/95 therm""",
    longDesc =
u"""
8/19/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(=C)CO
Imported from thermo.txt.
""",
)

entry(
    index = 393,
    label = "ic4h7o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74701,0.0407783,-2.4475e-05,7.06503e-09,-7.51571e-13,4869.79,19.4536], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[13.3458,0.0161219,-5.44376e-06,8.38199e-10,-4.83608e-14,611.444,-43.6819], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 therm""",
    longDesc =
u"""
4/ 3/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)C[O]
Imported from thermo.txt.
""",
)

entry(
    index = 394,
    label = "ic4h7oh",
    molecule =
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.691,0.0427169,-2.49282e-05,7.00962e-09,-7.23263e-13,-21451.2,19.9501], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[13.5043,0.0178647,-5.99304e-06,9.18718e-10,-5.28435e-14,-25825.6,-44.4646], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 8/97 therm""",
    longDesc =
u"""
4/ 8/97 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species ic3h5ch2oh (i.e. same molecular structure according to RMG)
C=C(C)CO
Imported from thermo.txt.
""",
)

entry(
    index = 395,
    label = "nc4ket23",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.450576,0.0648863,-5.04446e-05,2.03085e-08,-3.35952e-12,-42877.9,30.0154], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[19.9513,0.0179559,-6.31231e-06,9.98217e-10,-5.86637e-14,-49558.5,-74.3071], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)C(C)OO
Imported from thermo.txt.
""",
)

entry(
    index = 396,
    label = "nc4ket21",
    molecule =
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {14,D}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.69786,0.048386,-3.05577e-05,1.02706e-08,-1.51713e-12,-41866.6,10.6715], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[18.6231,0.0190969,-6.70746e-06,1.05995e-09,-6.22564e-14,-47193,-65.5478], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(=O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 397,
    label = "nc4ket24",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.93007,0.0539296,-3.66165e-05,1.3088e-08,-1.99245e-12,-41411.9,18.6568], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[18.7707,0.0189491,-6.65182e-06,1.05081e-09,-6.17069e-14,-47232,-67.3335], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 398,
    label = "c4h8o1-4",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.28506,0.0504801,-2.51999e-05,3.65744e-09,3.94863e-13,-23006.7,41.9349], Tmin=(298,'K'), Tmax=(1361,'K')),
            NASAPolynomial(coeffs=[14.2361,0.0181176,-6.46264e-06,1.03194e-09,-6.10557e-14,-29947.9,-55.2081], Tmin=(1361,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/22/95 therm""",
    longDesc =
u"""
1/22/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C1CCOC1
Imported from thermo.txt.
""",
)

entry(
    index = 399,
    label = "ic3h6co",
    molecule =
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.28039,0.0417017,-3.2509e-05,1.37243e-08,-2.40573e-12,-16394,13.8188], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[13.2548,0.0140143,-4.7891e-06,7.42924e-10,-4.30738e-14,-20053,-44.481], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""03/03/95 therm""",
    longDesc =
u"""
03/03/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)=C=O
Imported from thermo.txt.
""",
)

entry(
    index = 400,
    label = "ch3chco",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4838,0.0322203,-2.7025e-05,1.20499e-08,-2.18366e-12,-11527.7,17.1552], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[10.0219,0.00956966,-3.26222e-06,5.05232e-10,-2.92593e-14,-14248.3,-27.783], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""03/03/95 therm""",
    longDesc =
u"""
03/03/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C=O
Imported from thermo.txt.
""",
)

entry(
    index = 401,
    label = "och2o2h",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {7,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.93823,0.0301466,-2.61053e-05,1.09464e-08,-1.78313e-12,-13816.7,18.5042], Tmin=(298,'K'), Tmax=(1420,'K')),
            NASAPolynomial(coeffs=[11.5398,0.00534291,-1.81879e-06,2.81969e-10,-1.63584e-14,-16823.7,-32.0701], Tmin=(1420,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 9/98 therm""",
    longDesc =
u"""
4/ 9/98 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]COO
Imported from thermo.txt.
""",
)

entry(
    index = 402,
    label = "ic4ketii",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.15502,0.0610622,-4.49711e-05,1.70515e-08,-2.65949e-12,-38274.8,26.9612], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[19.5143,0.0182377,-6.38909e-06,1.00802e-09,-5.9144e-14,-44688.5,-71.7168], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C=O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 403,
    label = "tc3h6o2cho",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17883,0.0541596,-3.83436e-05,1.38308e-08,-2.0419e-12,-22739.4,20.0751], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[18.5534,0.0168774,-5.90753e-06,9.31518e-10,-5.46345e-14,-28544.7,-68.2487], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 2/95 therm""",
    longDesc =
u"""
8/ 2/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(C=O)O[O]
Imported from thermo.txt.
""",
)

entry(
    index = 404,
    label = "ic3h5o2hcho",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {10,D} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.05985,0.0582332,-4.37672e-05,1.6325e-08,-2.43462e-12,-16349.6,21.3688], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[20.6289,0.0148626,-5.25305e-06,8.33773e-10,-4.91277e-14,-22758.9,-78.2963], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/2/95 therm""",
    longDesc =
u"""
8/2/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)(C=O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 405,
    label = "tc3h6o2hco",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {6,S}
5  C u1 p0 c0 {1,S} {13,D}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {5,D}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.03864,0.0580421,-4.32124e-05,1.58792e-08,-2.3221e-12,-22428.5,20.3681], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[20.6473,0.0148527,-5.25105e-06,8.33619e-10,-4.91256e-14,-28872,-79.5951], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 2/95 therm""",
    longDesc =
u"""
8/ 2/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)([C]=O)OO
Imported from thermo.txt.
""",
)

entry(
    index = 406,
    label = "c4h7o",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.60619,0.0558563,-4.35596e-05,1.70589e-08,-2.65635e-12,4850.9,34.7113], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[15.3138,0.0143427,-4.81626e-06,7.39575e-10,-4.26141e-14,-729.343,-55.2938], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 therm""",
    longDesc =
u"""
4/ 3/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(C)[O]
Imported from thermo.txt.
""",
)

entry(
    index = 407,
    label = "c3h52-1,3ooh",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {2,S} {12,S}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {4,S} {13,S}
7  O u0 p2 c0 {5,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12254,0.0519554,-3.83734e-05,1.45852e-08,-2.29821e-12,-12275.9,14.8367], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[20.2818,0.0148155,-5.25503e-06,8.35963e-10,-4.93309e-14,-18008.5,-72.2688], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/26/3 thrm""",
    longDesc =
u"""
8/26/3 thrm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OOC[CH]COO
Imported from thermo.txt.
""",
)

entry(
    index = 408,
    label = "ac3h5ooh",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.43935,0.0402071,-2.95323e-05,1.14716e-08,-1.85171e-12,-9436.8,17.055], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[13.6838,0.0133968,-4.61534e-06,7.19989e-10,-4.1911e-14,-13316.5,-43.1904], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/98 therm""",
    longDesc =
u"""
7/20/98 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCOO
Imported from thermo.txt.
""",
)

entry(
    index = 409,
    label = "sc3h5cho",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.435795,0.0448719,-3.36583e-05,1.33067e-08,-2.17839e-12,-16039.5,23.7597], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.1696,0.0142484,-4.90844e-06,7.65789e-10,-4.45835e-14,-20403.3,-44.3673], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11/15/95 ther""",
    longDesc =
u"""
11/15/95 ther
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species ch3chchcho (i.e. same molecular structure according to RMG)
CC=CC=O
Imported from thermo.txt.
""",
)

entry(
    index = 410,
    label = "c3h6oh",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.20494,0.0330858,-1.63894e-05,3.18104e-09,-6.84229e-14,-9129.62,24.7155], Tmin=(298,'K'), Tmax=(1674,'K')),
            NASAPolynomial(coeffs=[9.31288,0.0167579,-5.75555e-06,9.00584e-10,-5.26567e-14,-12017,-19.5011], Tmin=(1674,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/ 7/98 therm""",
    longDesc =
u"""
1/ 7/98 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCO
Imported from thermo.txt.
""",
)

entry(
    index = 411,
    label = "hoc3h6o2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06954,0.0443106,-3.18636e-05,1.26409e-08,-2.12752e-12,-27589.4,18.3891], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[14.2691,0.0171838,-5.8342e-06,9.00994e-10,-5.20716e-14,-31450.2,-41.5295], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/ 7/98 therm""",
    longDesc =
u"""
1/ 7/98 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCCO
Imported from thermo.txt.
""",
)

entry(
    index = 412,
    label = "ic4h8o2h-i",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.994785,0.0589212,-4.25202e-05,1.61371e-08,-2.55905e-12,-4080.29,25.8951], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[18.0246,0.0193668,-6.74676e-06,1.0604e-09,-6.20506e-14,-10085.9,-65.763], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 therm""",
    longDesc =
u"""
7/19/ 0 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)COO
Imported from thermo.txt.
""",
)

entry(
    index = 413,
    label = "ic4h8ooh-io2",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.39424,0.0676573,-5.17084e-05,2.10796e-08,-3.5996e-12,-22478.7,22.503], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[21.897,0.0209638,-7.34665e-06,1.15927e-09,-6.80225e-14,-29266.5,-82.0541], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 trm""",
    longDesc =
u"""
7/19/ 0 trm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CO[O])COO
Imported from thermo.txt.
""",
)

entry(
    index = 414,
    label = "cc4h8o",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.27768,0.0652482,-5.00209e-05,1.97452e-08,-3.15606e-12,-13770.7,47.8501], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[13.5132,0.0191666,-6.53902e-06,1.01367e-09,-5.87547e-14,-20031.1,-52.2147], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/29/95 therm""",
    longDesc =
u"""
6/29/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1COC1
Imported from thermo.txt.
""",
)

entry(
    index = 415,
    label = "iic4h7q2-i",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {5,S} {16,S}
8  O u0 p2 c0 {6,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.93056,0.0605819,-4.23666e-05,1.49122e-08,-2.10979e-12,-16841.5,13.6228], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.05,0.0192149,-6.66623e-06,1.04496e-09,-6.10371e-14,-23208.7,-83.995], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/15/96 therm""",
    longDesc =
u"""
7/15/96 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(COO)COO
Imported from thermo.txt.
""",
)

entry(
    index = 416,
    label = "iic4h7q2-t",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {5,S} {16,S}
8  O u0 p2 c0 {6,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.16274,0.0434463,-1.76972e-05,4.88791e-10,9.03915e-13,-19650.2,0.262067], Tmin=(298,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[21.507,0.020536,-7.12383e-06,1.11655e-09,-6.52112e-14,-25111.8,-74.338], Tmin=(1377,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/15/96 therm""",
    longDesc =
u"""
7/15/96 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](COO)COO
Imported from thermo.txt.
""",
)

entry(
    index = 417,
    label = "tc4h8cho",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {12,D} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.958078,0.0642003,-4.70777e-05,1.75738e-08,-2.64896e-12,-6865.83,33.3781], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[17.9664,0.0194207,-6.67409e-06,1.03969e-09,-6.04703e-14,-13336.9,-67.9819], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""9/ 7/95 therm""",
    longDesc =
u"""
9/ 7/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)(C)C=O
Imported from thermo.txt.
""",
)

entry(
    index = 418,
    label = "ic4h8o",
    molecule =
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.97374,0.0624619,-5.04348e-05,2.13345e-08,-3.67383e-12,-17327.4,36.2336], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[14.4625,0.0180563,-6.18009e-06,9.59941e-10,-5.57132e-14,-23023.1,-56.119], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/95 therm""",
    longDesc =
u"""
7/19/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)C[O]
Imported from thermo.txt.
""",
)

entry(
    index = 419,
    label = "ic4h7ooh",
    molecule =
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.99117,0.0503349,-3.5628e-05,1.33952e-08,-2.11053e-12,-15109.5,15.4537], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[16.9235,0.0178397,-6.14273e-06,9.57895e-10,-5.57438e-14,-20004.1,-59.4746], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/95 therm""",
    longDesc =
u"""
7/19/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)COO
Imported from thermo.txt.
""",
)

entry(
    index = 420,
    label = "tic4h7q2-i",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  O u0 p2 c0 {5,S} {17,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.48426,0.0661225,-5.27349e-05,2.18216e-08,-3.66789e-12,-19890.7,12.672], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[23.3849,0.018707,-6.44022e-06,1.00428e-09,-5.84468e-14,-26118.1,-87.661], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 6/96 therm""",
    longDesc =
u"""
5/ 6/96 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)(COO)OO
Imported from thermo.txt.
""",
)

entry(
    index = 421,
    label = "o2c4h8cho",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,D} {16,S}
6  O u0 p2 c0 {2,S} {17,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
17 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.91848,0.0667246,-4.80871e-05,1.78589e-08,-2.71164e-12,-24983.8,23.8578], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[21.263,0.0214072,-7.38343e-06,1.15282e-09,-6.71508e-14,-31685.5,-79.9829], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""9/ 7/95 therm""",
    longDesc =
u"""
9/ 7/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(C=O)CO[O]
Imported from thermo.txt.
""",
)

entry(
    index = 422,
    label = "o2hc4h8co",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  C u1 p0 c0 {1,S} {16,D}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {6,D}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.82607,0.0693466,-4.93125e-05,1.69848e-08,-2.26118e-12,-24657.8,24.1168], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.822,0.0191411,-6.67919e-06,1.05127e-09,-6.15877e-14,-32309.4,-94.2581], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""9/ 7/95 therm""",
    longDesc =
u"""
9/ 7/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)([C]=O)COO
Imported from thermo.txt.
""",
)

entry(
    index = 423,
    label = "hcoh",
    molecule =
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.82157,0.0357332,-3.80862e-05,1.86206e-08,-3.45958e-12,11295.7,34.8488], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[9.18749,0.00152011,-6.27604e-07,1.09728e-10,-6.89655e-15,7813.65,-27.3434], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""mar94""",
    longDesc =
u"""
mar94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]O
Imported from thermo.txt.
""",
)

entry(
    index = 424,
    label = "cc3h4",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.024621,0.0231972,-1.84744e-06,-1.59276e-08,8.68462e-12,32334.1,22.7298], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.69999,0.0103574,-3.45512e-06,5.06529e-10,-2.66823e-14,30199.1,-13.3788], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""t12/81""",
    longDesc =
u"""
t12/81
wkm 12/10/10

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C1=CC1
Imported from thermo.txt.
""",
)

entry(
    index = 425,
    label = "sc3h5co",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74191,0.039723,-3.20062e-05,1.38228e-08,-2.46272e-12,-664.428,17.0762], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[12.5515,0.0122522,-4.22382e-06,6.59185e-10,-3.83819e-14,-4253.5,-40.2864], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""11/15/95 therm""",
    longDesc =
u"""
11/15/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species ch3chchco (i.e. same molecular structure according to RMG)
CC=C[C]=O
Imported from thermo.txt.
""",
)

entry(
    index = 426,
    label = "h2c4o",
    molecule =
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {7,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.81097,0.01314,9.86507e-07,-6.12072e-09,1.64e-12,25458,2.11342], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.2689,0.00489616,-4.88508e-07,-2.70857e-10,5.10701e-14,23469,-28.1598], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""120189""",
    longDesc =
u"""
120189
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C=C=C=O
Imported from thermo.txt.
""",
)

entry(
    index = 427,
    label = "ic4h8oh",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29613,0.034765,-1.02506e-05,-2.04642e-09,1.18879e-12,-14562.7,15.8606], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[12.5606,0.0210637,-7.1502e-06,1.10439e-09,-6.38429e-14,-18620.3,-36.7889], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/14/95 therm""",
    longDesc =
u"""
2/14/95 therm
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species ic4h8oh-2 (i.e. same molecular structure according to RMG)
C[C](C)CO
Imported from thermo.txt.
""",
)

entry(
    index = 428,
    label = "c4h6o25",
    molecule =
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {1,S} {3,D} {11,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67053,0.00492586,8.86967e-05,-1.26219e-07,5.23991e-11,-14657.2,14.5722], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.60658,0.020831,-8.42229e-06,1.56718e-09,-1.09391e-13,-17617.7,-23.2465], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""t 3/97""",
    longDesc =
u"""
t 3/97.
C1=CCOC1
Imported from thermo.txt.
""",
)
