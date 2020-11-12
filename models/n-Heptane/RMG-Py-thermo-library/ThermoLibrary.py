#!/usr/bin/env python
# encoding: utf-8

name = "n-Heptane"
shortDesc = "/work/westgroup/Importer/RMG-models/n-Heptane/n_heptane_v3.1_therm.dat"
longDesc = """
b'n-Heptane, Detailed Mechanism, Version 3.1\n\nThis mechanism represents an updated release of the previous version \navailable on the website (Version 3.0). The mechanism is based on the \npreviously developed and very successful mechanism of Curran et al. \n1998 [1]. Version 3.1 fixes some bugs found in Version 3.0. This \ndetailed chemical kinetic mechanism has been developed and validated \nby comparison to experiments in shock tubes and rapid compression \nmachines. Over the series of experiments numerically investigated, \nthe initial pressure ranged from 3 to 50 atm, the temperature from \n650 to 1200 K, and equivalence ratios from 0.3 to 1.0. The mechanism \nperforms well at both low and high temperature and over a broad \npressure range important for internal combustion engines.\n\nReferences for Mechanism\n\nMehl M., W.J. Pitz, C.K. Westbrook, H.J. Curran, "Kinetic Modeling of Gasoline Surrogate Components and Mixtures Under Engine Conditions", Proceedings of the Combustion Institute 33:193-200 (2011).\nDOI: https://doi.org/10.1016/j.proci.2010.05.027\n\nM. Mehl, W. J. Pitz, M. Sj?berg and J. E. Dec, "Detailed kinetic modeling of low-temperature heat release for PRF fuels in an HCCI engine," SAE 2009 International Powertrains, Fuels and Lubricants Meeting, SAE Paper No. 2009-01-1806, Florence, Italy, 2009. Available at www.sae.org.\nDOI: https://doi.org/10.4271/2009-01-1806\n\nOther reference\n\n[1] Curran, H. J., P. Gaffuri, W. J. Pitz, and C. K. Westbrook, "A Comprehensive Modeling Study of n-Heptane Oxidation" Combustion and Flame 114:149-177 (1998).\n\n\nDownloaded from https://www-pls.llnl.gov/?url=science_and_technology-chemistry-combustion-n_heptane_version_3 (BROKEN) in September 2013\n\nNew Link: https://combustion.llnl.gov/mechanisms/alkanes/n-heptane-detailed-mechanism-version-3\n\nAbstract\n========================\nReal fuels are complex mixtures of thousands of hydrocarbon compounds \nincluding linear and branched paraffins, naphthenes, olefins and \naromatics. It is generally agreed that their behavior can be effectively \nreproduced by simpler fuel surrogates containing a limited number of components.\n\nIn this work, an improved version of the kinetic model by the \nauthors is used to analyze the combustion behavior of several \ncomponents relevant to gasoline surrogate formulation. Particular \nattention is devoted to linear and branched saturated hydrocarbons \n(PRF mixtures), olefins (1-hexene) and aromatics (toluene). Model \npredictions for pure components, binary mixtures and multi-component \ngasoline surrogates are compared with recent experimental information \ncollected in rapid compression machine, shock tube and jet stirred \nreactors covering a wide range of conditions pertinent to internal \ncombustion engines (3?50 atm, 650?1200 K, stoichiometric fuel/air mixtures). \nSimulation results are discussed focusing attention on the mixing effects of the fuel components.'
"""
entry(
    index = 0,
    label = "CH2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00754,0.00304729,5.25109e-06,-5.12019e-09,1.27134e-12,-14118.8,8.1012], Tmin=(298,'K'), Tmax=(1486,'K')),
            NASAPolynomial(coeffs=[4.02068,0.00509903,-1.7643e-06,2.76026e-10,-1.60998e-14,-14928.7,1.06526], Tmin=(1486,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-118.385,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """6/29/04 RUSCI""",
    longDesc = 
"""
6/29/04 RUSCI
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 1,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8105,0.00081327,3.13165e-06,-2.39478e-09,5.06895e-13,4038.6,4.94843], Tmin=(298,'K'), Tmax=(1690,'K')),
            NASAPolynomial(coeffs=[3.44148,0.00352158,-1.24136e-06,1.97329e-10,-1.16539e-14,3974.1,6.24593], Tmin=(1690,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (33.3911,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """29/11/04""",
    longDesc = 
"""
29/11/04
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 2,
    label = "HOCHO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.28069,0.0152888,-5.6415e-06,-1.22969e-09,8.14273e-13,-46434.8,18.3142], Tmin=(298,'K'), Tmax=(1419,'K')),
            NASAPolynomial(coeffs=[7.67134,0.00443426,-1.60867e-06,2.5977e-10,-1.549e-14,-48970.9,-17.3024], Tmin=(1419,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-388.293,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (103.931,'J/mol/K'),
    ),
    shortDesc = """9/27/ 5 THERM""",
    longDesc = 
"""
9/27/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 3,
    label = "CH3O2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80498,0.00980785,-3.90941e-07,-2.23073e-09,6.43311e-13,-455.626,7.81789], Tmin=(298,'K'), Tmax=(1365,'K')),
            NASAPolynomial(coeffs=[6.34719,0.00792089,-2.76602e-06,4.35361e-10,-2.54985e-14,-1834.36,-7.42553], Tmin=(1365,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-3.95314,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """1/14/ 5 THERM""",
    longDesc = 
"""
1/14/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 4,
    label = "C2H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.06743,0.0146569,-1.52947e-05,8.30966e-09,-1.72932e-12,25957.9,8.62759], Tmin=(298,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[4.98265,0.00425993,-1.37484e-06,2.04718e-10,-1.15192e-14,25269.7,-5.81321], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (214.675,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (87.302,'J/mol/K'),
    ),
    shortDesc = """10/ 4/ 5 THERM""",
    longDesc = 
"""
10/ 4/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 5,
    label = "CH2CO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.97497,0.0121187,-2.34505e-06,-6.46668e-09,3.90565e-12,-7632.64,8.67355], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.03882,0.00580484,-1.92095e-06,2.79448e-10,-1.45887e-14,-8583.4,-7.65758], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-64.2064,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """121686""",
    longDesc = 
"""
121686
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 6,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,D} {4,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.04796,0.00445348,2.26828e-07,-1.48209e-09,2.25074e-13,19658.9,0.481844], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.75807,0.0020004,-2.02761e-07,-1.04113e-10,1.96516e-14,19015.1,-9.07126], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
        E0 = (164.809,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """32387""",
    longDesc = 
"""
32387
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 7,
    label = "C2H5O",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.287429,0.0286501,-1.83857e-05,6.03096e-09,-8.04563e-13,-3357.17,23.7514], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[8.23717,0.0110886,-3.78808e-06,5.87613e-10,-3.40713e-14,-6229.49,-19.3191], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-31.2946,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """8/ 9/ 4 THERM""",
    longDesc = 
"""
8/ 9/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 8,
    label = "C4H10",
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
            NASAPolynomial(coeffs=[-0.455757,0.0480323,-2.65498e-05,6.92545e-09,-6.38318e-13,-16896.1,26.4871], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[12.494,0.0217726,-7.44272e-06,1.15487e-09,-6.69713e-14,-21840.3,-44.5559], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-143.538,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 9,
    label = "CH3CHO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.7706,0.0184475,-7.24138e-06,2.34365e-10,3.35544e-13,-21807.9,16.5023], Tmin=(298,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[6.98519,0.00967898,-3.31842e-06,5.16026e-10,-2.99726e-14,-23980.7,-12.7485], Tmin=(1377,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-183.113,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """8/10/ 4 THERM""",
    longDesc = 
"""
8/10/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 10,
    label = "C2H5OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.179106,0.030906,-1.93597e-05,6.31831e-09,-8.53167e-13,-29567.1,24.4716], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[8.31742,0.0129603,-4.39286e-06,6.77735e-10,-3.91448e-14,-32522,-19.6503], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-249.19,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (199.547,'J/mol/K'),
    ),
    shortDesc = """8/ 9/ 4 THERM""",
    longDesc = 
"""
8/ 9/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 11,
    label = "C3H6",
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
            NASAPolynomial(coeffs=[0.394615,0.0289108,-1.54887e-05,3.88814e-09,-3.3789e-13,1177.6,21.9004], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[8.01596,0.0137024,-4.6625e-06,7.21254e-10,-4.1737e-14,-1767.49,-20.0161], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (6.6253,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """10/23/ 5 THERM""",
    longDesc = 
"""
10/23/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 12,
    label = "CH3CHCO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4838,0.0322203,-2.7025e-05,1.20499e-08,-2.18366e-12,-11527.7,17.1552], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[10.0219,0.00956966,-3.26222e-06,5.05232e-10,-2.92593e-14,-14248.3,-27.783], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-97.396,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """03/03/95 THERM""",
    longDesc = 
"""
03/03/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 13,
    label = "SC2H4OH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {8,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.61104,0.0263512,-1.82941e-05,6.91243e-09,-1.10384e-12,-8714.95,18.0115], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[8.34981,0.0103718,-3.49683e-06,5.37525e-10,-3.09661e-14,-11055.6,-18.1354], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-74.1142,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (174.604,'J/mol/K'),
    ),
    shortDesc = """8/ 9/ 4 THERM""",
    longDesc = 
"""
8/ 9/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 14,
    label = "C2H5O2H",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.57329,0.035238,-2.53204e-05,9.56802e-09,-1.48167e-12,-21527.8,19.0472], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[11.2306,0.0120482,-3.9673e-06,6.00755e-10,-3.42658e-14,-24797.8,-32.5607], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-180.182,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (220.334,'J/mol/K'),
    ),
    shortDesc = """1/14/ 5 THERM""",
    longDesc = 
"""
1/14/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 15,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.23058,0.00853179,1.02167e-06,-3.41047e-09,9.94691e-13,945.94,12.8378], Tmin=(298,'K'), Tmax=(1509,'K')),
            NASAPolynomial(coeffs=[4.64787,0.00690831,-2.34405e-06,3.61995e-10,-2.09254e-14,-299.209,-1.5774], Tmin=(1509,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (6.21658,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """8/ 9/ 4 THERM""",
    longDesc = 
"""
8/ 9/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 16,
    label = "CH3O2H",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {7,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.8388,0.0186096,-8.48165e-06,1.00387e-09,1.71612e-13,-17403.4,11.6092], Tmin=(298,'K'), Tmax=(1367,'K')),
            NASAPolynomial(coeffs=[8.80409,0.00809427,-2.85843e-06,4.5337e-10,-2.66981e-14,-19851.2,-21.7001], Tmin=(1367,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-145.504,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (149.66,'J/mol/K'),
    ),
    shortDesc = """1/14/ 5 THERM""",
    longDesc = 
"""
1/14/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 17,
    label = "HOCH2O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {6,S}
2 O u1 p2 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11183,0.00753851,3.77337e-06,-5.38746e-09,1.45616e-12,-22802.3,7.46807], Tmin=(298,'K'), Tmax=(1452,'K')),
            NASAPolynomial(coeffs=[6.39522,0.00743673,-2.50422e-06,3.8488e-10,-2.21779e-14,-24110.9,-6.63866], Tmin=(1452,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-189.583,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """2/16/99 THERM""",
    longDesc = 
"""
2/16/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 18,
    label = "PC4H9",
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
            NASAPolynomial(coeffs=[0.320731,0.0434654,-2.40585e-05,6.28245e-09,-5.80113e-13,7714.91,25.7301], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[12.078,0.0196265,-6.71302e-06,1.04206e-09,-6.04469e-14,3225.5,-38.7719], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (61.798,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 19,
    label = "PC2H4OH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.990023,0.0261564,-1.65928e-05,5.50525e-09,-7.57521e-13,-4960.32,22.8676], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[7.8851,0.0108288,-3.6683e-06,5.65734e-10,-3.26673e-14,-7449.75,-14.4674], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-43.7429,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (174.604,'J/mol/K'),
    ),
    shortDesc = """8/ 9/ 4 THERM""",
    longDesc = 
"""
8/ 9/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 20,
    label = "CH2O2H",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {6,S}
3 C u1 p0 c0 {1,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47228,0.0133401,-5.9292e-06,4.44481e-10,2.127e-13,5674.14,4.72608], Tmin=(298,'K'), Tmax=(1357,'K')),
            NASAPolynomial(coeffs=[9.10784,0.0052726,-1.88171e-06,3.00561e-10,-1.77866e-14,3774.4,-21.1741], Tmin=(1357,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (47.4747,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (124.717,'J/mol/K'),
    ),
    shortDesc = """1/14/ 5 THERM""",
    longDesc = 
"""
1/14/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 21,
    label = "C2H5CHO",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,D} {2,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.93108,0.00887944,2.03764e-05,-1.80149e-08,4.14086e-12,-25137.8,-0.58702], Tmin=(298,'K'), Tmax=(1375,'K')),
            NASAPolynomial(coeffs=[8.87216,0.0201711,-8.06488e-06,1.37618e-09,-8.48922e-14,-28384.9,-23.5069], Tmin=(1375,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-204.364,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """8/10/ 4 THERM""",
    longDesc = 
"""
8/10/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 22,
    label = "C2H",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u1 p0 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.27708,0.0017413,7.3118e-07,-9.71828e-10,2.36957e-13,66312.6,0.316342], Tmin=(298,'K'), Tmax=(1361,'K')),
            NASAPolynomial(coeffs=[4.66894,0.00201285,-7.01829e-07,1.10347e-10,-6.4579e-15,66031.1,-2.25425], Tmin=(1361,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (552.141,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (62.3585,'J/mol/K'),
    ),
    shortDesc = """10/ 4/ 5 THERM""",
    longDesc = 
"""
10/ 4/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[C]#C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 23,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05674,0.0119336,-8.72501e-06,3.82781e-09,-7.22888e-13,-2831.4,8.98878], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[5.41876,0.00566185,-1.87471e-06,2.84442e-10,-1.623e-14,-3614.76,-3.49278], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-24.1672,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (103.931,'J/mol/K'),
    ),
    shortDesc = """2/25/ 4 THERM""",
    longDesc = 
"""
2/25/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 24,
    label = "HCCOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89947,0.00970107,-3.11931e-07,-5.53773e-09,2.46573e-12,8701.19,4.49188], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.32832,0.00333642,-3.0247e-07,-1.78111e-10,3.24517e-14,7598.26,-14.0121], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
        E0 = (72.7798,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (103.931,'J/mol/K'),
    ),
    shortDesc = """32387""",
    longDesc = 
"""
32387
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 25,
    label = "CH3OCH2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91327,0.0203365,-9.59712e-06,2.07479e-09,-1.71343e-13,-1188.44,11.6067], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[8.17138,0.0110086,-3.82352e-06,5.99637e-10,-3.50318e-14,-3419.42,-17.8651], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-10.5012,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (174.604,'J/mol/K'),
    ),
    shortDesc = """7/20/98 THERM""",
    longDesc = 
"""
7/20/98 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]OC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 26,
    label = "CH3OCH3",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.50763,0.0239914,-8.6891e-06,-9.66836e-11,4.89319e-13,-23281.1,16.7317], Tmin=(298,'K'), Tmax=(1368,'K')),
            NASAPolynomial(coeffs=[8.27746,0.0132136,-4.53264e-06,7.05317e-10,-4.09933e-14,-26198.3,-21.5191], Tmin=(1368,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-195.358,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (199.547,'J/mol/K'),
    ),
    shortDesc = """7/20/98 THERM""",
    longDesc = 
"""
7/20/98 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
COC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 27,
    label = "CH3OCHO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.43526,0.0181948,1.91237e-06,-8.44249e-09,2.61759e-12,-44651.5,14.9522], Tmin=(298,'K'), Tmax=(1452,'K')),
            NASAPolynomial(coeffs=[10.6569,0.00938113,-3.37677e-06,5.42456e-10,-3.22295e-14,-48465.2,-32.7579], Tmin=(1452,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-371.945,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (174.604,'J/mol/K'),
    ),
    shortDesc = """4/15/ 8 THERM""",
    longDesc = 
"""
4/15/ 8 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
COC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 28,
    label = "HOCH2O2H",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.85717,0.0323153,-2.69929e-05,1.11694e-08,-1.81284e-12,-40031.4,19.0918], Tmin=(298,'K'), Tmax=(1422,'K')),
            NASAPolynomial(coeffs=[11.6304,0.00715134,-2.39035e-06,3.65773e-10,-2.102e-14,-43107.9,-32.4277], Tmin=(1422,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-333.788,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (170.447,'J/mol/K'),
    ),
    shortDesc = """4/ 9/98 THERM""",
    longDesc = 
"""
4/ 9/98 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 29,
    label = "NC5H12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
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
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.67881,0.0641231,-3.96458e-05,1.23445e-08,-1.53325e-12,-19647.5,33.9349], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[15.9247,0.0259703,-8.86821e-06,1.37515e-09,-7.97105e-14,-26082.4,-61.6997], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-167.105,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 30,
    label = "NC6H14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.969606,0.0729086,-4.38854e-05,1.32313e-08,-1.58437e-12,-22780.4,32.307], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[18.9634,0.030448,-1.03795e-05,1.60775e-09,-9.3127e-14,-30162.9,-76.2839], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-191.976,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 31,
    label = "C4H8-1",
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
            NASAPolynomial(coeffs=[-0.833377,0.0454141,-2.97609e-05,1.03518e-08,-1.51976e-12,-1491.62,29.4328], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[11.3457,0.0180843,-6.17277e-06,9.56926e-10,-5.54586e-14,-5886.59,-36.4627], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-16.1724,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (274.378,'J/mol/K'),
    ),
    shortDesc = """6/29/ 4 THERM""",
    longDesc = 
"""
6/29/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 32,
    label = "SC4H9",
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
            NASAPolynomial(coeffs=[0.84916,0.0382085,-1.49627e-05,2.04499e-10,8.24254e-13,6388.33,24.4467], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[11.6934,0.0196402,-6.65307e-06,1.02632e-09,-5.92826e-14,1963.82,-36.1627], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (51.2271,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 33,
    label = "CH3OCH2O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {4,S}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25889,0.0222146,-7.78556e-06,-2.41484e-10,4.51914e-13,-19237.7,12.368], Tmin=(298,'K'), Tmax=(2012,'K')),
            NASAPolynomial(coeffs=[8.60262,0.0135772,-4.84662e-06,7.77766e-10,-4.62634e-14,-21376.2,-17.5775], Tmin=(2012,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-160.383,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (199.547,'J/mol/K'),
    ),
    shortDesc = """2/ 9/96 THERM""",
    longDesc = 
"""
2/ 9/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
COC[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 34,
    label = "C2H3",
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
            NASAPolynomial(coeffs=[1.2533,0.0156258,-1.07804e-05,4.18055e-09,-7.0136e-13,35073.5,17.1342], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[5.07331,0.00658316,-2.23763e-06,3.45803e-10,-1.9994e-14,33723.5,-3.39793], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (288.956,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """10/ 4/ 5 THERM""",
    longDesc = 
"""
10/ 4/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 35,
    label = "OCHO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42992,0.0122803,-5.28461e-06,-3.73027e-10,5.07954e-13,-16204.3,18.0412], Tmin=(298,'K'), Tmax=(1412,'K')),
            NASAPolynomial(coeffs=[6.49816,0.00322319,-1.171e-06,1.89273e-10,-1.12937e-14,-18167.9,-10.0413], Tmin=(1412,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-136.876,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """9/27/ 5 THERM""",
    longDesc = 
"""
9/27/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 36,
    label = "CH2(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97126,-0.000169909,1.02537e-06,2.49255e-09,-1.98127e-12,49893.7,0.0575321], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.55289,0.00206679,-1.91412e-07,-1.10467e-10,2.02135e-14,49849.8,1.68657], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
        E0 = (414.85,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """31287""",
    longDesc = 
"""
31287
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 37,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76224,0.00115982,2.48958e-07,8.80084e-10,-7.33244e-13,45367.9,1.71258], Tmin=(250,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.63641,0.00193306,-1.68702e-07,-1.0099e-10,1.80826e-14,45341.3,2.15656], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (4000,'K'),
        E0 = (376.957,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """120186""",
    longDesc = 
"""
120186.
[CH2]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 38,
    label = "C4H8-2",
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
            NASAPolynomial(coeffs=[0.669214,0.037684,-1.8569e-05,3.69571e-09,-1.03095e-13,-3116.75,21.4868], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[10.7864,0.0184629,-6.28289e-06,9.72052e-10,-5.62579e-14,-7116.5,-34.4893], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-28.1048,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (274.378,'J/mol/K'),
    ),
    shortDesc = """6/29/ 4 THERM""",
    longDesc = 
"""
6/29/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 39,
    label = "O2CHO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 O u1 p2 c0 {1,S}
4 C u0 p0 c0 {1,S} {2,D} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96059,0.0106002,-5.25713e-06,1.01717e-09,-2.87488e-14,-17359.9,11.7807], Tmin=(298,'K'), Tmax=(1368,'K')),
            NASAPolynomial(coeffs=[7.24075,0.00463313,-1.63694e-06,2.59707e-10,-1.52965e-14,-18702.8,-6.49547], Tmin=(1368,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-144.249,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (103.931,'J/mol/K'),
    ),
    shortDesc = """6/26/95 THERM""",
    longDesc = 
"""
6/26/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 40,
    label = "CH3OCH2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
5  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.2103,0.0368877,-2.82562e-05,1.15731e-08,-1.9713e-12,-19494.1,19.1464], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[12.425,0.0118706,-4.07907e-06,6.35311e-10,-3.69428e-14,-22967.9,-35.374], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-162.625,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (220.334,'J/mol/K'),
    ),
    shortDesc = """7/20/98 THERM""",
    longDesc = 
"""
7/20/98 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
COCO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 41,
    label = "IC4H9",
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
            NASAPolynomial(coeffs=[-0.221458,0.0463756,-2.88283e-05,9.60201e-09,-1.39021e-12,6761.54,26.4801], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[12.1277,0.0198689,-6.85937e-06,1.07142e-09,-6.24185e-14,2119.52,-40.8727], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (53.2737,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 42,
    label = "IC4H10",
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
            NASAPolynomial(coeffs=[-0.972807,0.0508661,-3.12355e-05,1.02058e-08,-1.44169e-12,-17854.2,26.9573], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[12.5376,0.022025,-7.59339e-06,1.18498e-09,-6.89902e-14,-22942.2,-46.7742], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-152.08,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 43,
    label = "IC4H8",
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
            NASAPolynomial(coeffs=[0.938433,0.0390547,-2.16437e-05,5.87267e-09,-6.14435e-13,-3954.52,19.8338], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[11.2258,0.0181796,-6.20349e-06,9.61444e-10,-5.57088e-14,-7906.18,-36.6412], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-34.7478,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (274.378,'J/mol/K'),
    ),
    shortDesc = """10/23/ 5 THERM""",
    longDesc = 
"""
10/23/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 44,
    label = "IC4H9O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.21434,0.0545388,-3.67002e-05,1.34131e-08,-2.11742e-12,-11848.2,23.4153], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[15.9741,0.0213535,-7.39001e-06,1.15624e-09,-6.74408e-14,-17232.9,-56.5302], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-99.623,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (340.893,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)CO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 45,
    label = "HO2CHO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.42465,0.0219706,-1.68706e-05,6.25612e-09,-9.11646e-13,-35482.8,17.5028], Tmin=(298,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[9.87504,0.00464664,-1.67231e-06,2.68624e-10,-1.59595e-14,-38050.2,-22.4939], Tmin=(1378,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-295.788,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (124.717,'J/mol/K'),
    ),
    shortDesc = """6/26/95 THERM""",
    longDesc = 
"""
6/26/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 46,
    label = "TC4H9",
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
            NASAPolynomial(coeffs=[3.043,0.0291276,-4.01387e-06,-4.90274e-09,1.64015e-12,4047.81,12.1127], Tmin=(298,'K'), Tmax=(1372,'K')),
            NASAPolynomial(coeffs=[10.5855,0.0211892,-7.31668e-06,1.14296e-09,-6.65899e-14,318.311,-32.0671], Tmin=(1372,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (33.1716,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 47,
    label = "IC3H7",
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
            NASAPolynomial(coeffs=[1.63418,0.0240171,-4.72808e-06,-3.24355e-09,1.23539e-12,9207.53,18.3848], Tmin=(298,'K'), Tmax=(1373,'K')),
            NASAPolynomial(coeffs=[8.14705,0.0158727,-5.44612e-06,8.47208e-10,-4.92179e-14,6180.73,-19.1981], Tmin=(1373,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (75.0045,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 48,
    label = "CH3OCH2O2H",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u0 p2 c0 {2,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
5  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.19856,0.0459061,-3.66252e-05,1.49319e-08,-2.46057e-12,-36536.3,23.134], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.9371,0.0119466,-4.12746e-06,6.45423e-10,-3.76428e-14,-41100.1,-49.9553], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-304.953,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (241.12,'J/mol/K'),
    ),
    shortDesc = """7/20/98 THERM""",
    longDesc = 
"""
7/20/98 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
COCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 49,
    label = "O2C2H4OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,S} {10,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11839,0.0272241,-1.60824e-05,5.17033e-09,-7.3161e-13,-23085.8,12.8482], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[10.7433,0.0130958,-4.4537e-06,6.88549e-10,-3.9823e-14,-25591.1,-23.3255], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-190.991,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (220.334,'J/mol/K'),
    ),
    shortDesc = """2/14/95 THERM""",
    longDesc = 
"""
2/14/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 50,
    label = "SC4H9O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.32689,0.0562786,-4.01718e-05,1.57121e-08,-2.62948e-12,-13155.7,23.407], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[16.4031,0.0209361,-7.23393e-06,1.13059e-09,-6.58939e-14,-18507.5,-57.7332], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-110.282,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (340.893,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 51,
    label = "PC4H9O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.94364,0.0515513,-3.28284e-05,1.13065e-08,-1.70119e-12,-10835.8,21.3503], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[15.7845,0.0215211,-7.44909e-06,1.16558e-09,-6.79886e-14,-16014.6,-54.0389], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-90.628,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (340.893,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 52,
    label = "CH3COCH3",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,D} {2,S} {3,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24527,0.029976,-1.40027e-05,2.16454e-09,1.27637e-13,-27834.9,20.3683], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[9.62674,0.0145519,-4.97749e-06,7.72795e-10,-4.48367e-14,-31186.2,-26.1613], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-233.277,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """8/30/ 4 THERM""",
    longDesc = 
"""
8/30/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 53,
    label = "C4H6",
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
            NASAPolynomial(coeffs=[-1.43095,0.0478706,-4.15447e-05,1.9155e-08,-3.57159e-12,11755.1,29.0826], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[11.1634,0.0137164,-4.69716e-06,7.29694e-10,-4.23486e-14,7790.4,-36.9848], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (93.1667,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (228.648,'J/mol/K'),
    ),
    shortDesc = """4/ 4/ 0 THERM""",
    longDesc = 
"""
4/ 4/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 54,
    label = "NC3H7",
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
            NASAPolynomial(coeffs=[0.474365,0.031919,-1.7191e-05,4.45928e-09,-4.36675e-13,10631.5,23.2671], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[8.88635,0.0152273,-5.21906e-06,8.11259e-10,-4.71028e-14,7346.72,-23.0728], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (85.6054,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 55,
    label = "CH3CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,D} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.52884,0.0137152,-4.28607e-06,-7.71684e-10,4.83836e-13,-3025.47,14.034], Tmin=(298,'K'), Tmax=(1371,'K')),
            NASAPolynomial(coeffs=[6.56682,0.00755309,-2.59967e-06,4.05335e-10,-2.35876e-14,-4766.9,-8.83302], Tmin=(1371,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-26.2302,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """8/10/ 4 THERM""",
    longDesc = 
"""
8/10/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 56,
    label = "NC7H16",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.26836,0.0854356,-5.25347e-05,1.62946e-08,-2.02395e-12,-25658.7,35.3733], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[22.2149,0.0347676,-1.18407e-05,1.83298e-09,-1.0613e-13,-34276,-92.304], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-215.731,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (532.126,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 57,
    label = "C4H71-3",
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
            NASAPolynomial(coeffs=[-1.12475,0.0434883,-2.8775e-05,9.88047e-09,-1.4012e-12,15442,29.7651], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[10.947,0.0163724,-5.59896e-06,8.69148e-10,-5.04214e-14,11118.2,-35.4908], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (124.212,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """4/ 2/97 THERM""",
    longDesc = 
"""
4/ 2/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C[CH]C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 58,
    label = "C2H5CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 C u1 p0 c0 {1,D} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.35352,-0.0040874,3.64218e-05,-2.72458e-08,6.0644e-12,-6585.77,-10.5948], Tmin=(298,'K'), Tmax=(1362,'K')),
            NASAPolynomial(coeffs=[10.0147,0.0161528,-6.62976e-06,1.15291e-09,-7.21263e-14,-10043,-28.8571], Tmin=(1362,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-47.3239,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (199.547,'J/mol/K'),
    ),
    shortDesc = """8/10/ 4 THERM""",
    longDesc = 
"""
8/10/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 59,
    label = "C2H5O2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5863,0.0261836,-1.68306e-05,6.08749e-09,-9.57302e-13,-4585.89,15.0486], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[8.77641,0.0118767,-3.87683e-06,5.83211e-10,-3.31007e-14,-6787.49,-18.312], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-38.6361,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (199.547,'J/mol/K'),
    ),
    shortDesc = """1/14/ 5 THERM""",
    longDesc = 
"""
1/14/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 60,
    label = "CH3OCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {2,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.83313,0.0153448,1.89584e-06,-7.702e-09,2.41564e-12,-21343.2,13.9524], Tmin=(298,'K'), Tmax=(1423,'K')),
            NASAPolynomial(coeffs=[10.2053,0.0071227,-2.57594e-06,4.15104e-10,-2.47168e-14,-24687.1,-28.6407], Tmin=(1423,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-177.804,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (149.66,'J/mol/K'),
    ),
    shortDesc = """4/15/ 8 THERM""",
    longDesc = 
"""
4/15/ 8 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CO[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 61,
    label = "C5H91-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u1 p0 c0 {4,D} {14,S}
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
            NASAPolynomial(coeffs=[-0.168849,0.0540219,-3.74233e-05,1.37866e-08,-2.1259e-12,25160.5,28.8873], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[14.4574,0.0200073,-6.81379e-06,1.05475e-09,-6.10665e-14,20027.1,-49.7834], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (206.737,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 62,
    label = "CH3CO3",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {5,D}
3 O u1 p2 c0 {1,S}
4 C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {1,S} {2,D} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60373,0.027008,-2.08293e-05,8.50541e-09,-1.43846e-12,-23420.5,11.2015], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[11.2522,0.00833653,-2.89015e-06,4.52782e-10,-2.64354e-14,-26023.9,-29.637], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-194.244,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (174.604,'J/mol/K'),
    ),
    shortDesc = """4/ 3/ 0 THERM""",
    longDesc = 
"""
4/ 3/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 63,
    label = "CH3COCH2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u0 p0 c0 {3,D} {8,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.22337,0.0324547,-2.13543e-05,6.96778e-09,-8.9916e-13,-6594.19,20.5537], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[10.8892,0.0111541,-3.85517e-06,6.02834e-10,-3.51533e-14,-10074.1,-31.8043], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-56.567,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """8/30/ 4 THERM""",
    longDesc = 
"""
8/30/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 64,
    label = "IC4H9O2H",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {16,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.244182,0.0634028,-4.49162e-05,1.67407e-08,-2.61216e-12,-28696,27.2156], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[18.4309,0.0215338,-7.48624e-06,1.17499e-09,-6.86891e-14,-35148.3,-70.8031], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-240.301,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (361.68,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 65,
    label = "IC3H7CHO",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {1,D} {2,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.273021,0.0489696,-3.1277e-05,1.00053e-08,-1.27512e-12,-27605.5,28.3451], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[13.7502,0.0183127,-6.28573e-06,9.78251e-10,-5.68539e-14,-32693.7,-47.7271], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-232.285,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THERM""",
    longDesc = 
"""
2/22/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 66,
    label = "SC4H8OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {2,S} {4,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.04565,0.0572423,-4.43109e-05,1.80945e-08,-3.02843e-12,-12871.8,34.8383], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.8422,0.0178436,-6.16709e-06,1.00443e-09,-6.10698e-14,-18171.5,-49.6977], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-110.122,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (315.95,'J/mol/K'),
    ),
    shortDesc = """2/12/ 9 THERM""",
    longDesc = 
"""
2/12/ 9 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C(C)O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 67,
    label = "PC4H9O2H",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {16,S}
3  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.634644,0.0620008,-4.34478e-05,1.61408e-08,-2.53122e-12,-27634.6,26.7026], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[18.2687,0.021694,-7.5463e-06,1.18485e-09,-6.92818e-14,-33944.2,-68.4816], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-231.172,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (361.68,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 68,
    label = "C3H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.7542,0.0110803,2.79332e-07,-5.47921e-09,1.94963e-12,39888.8,0.585455], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.83105,0.0043572,-4.10907e-07,-2.36872e-10,4.37652e-14,38474.2,-21.7792], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
        E0 = (333.289,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """82489""",
    longDesc = 
"""
82489
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=C=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 69,
    label = "SC4H9O2H",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {16,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.340588,0.0652078,-4.8484e-05,1.91012e-08,-3.13833e-12,-30000.8,27.2835], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[18.8588,0.0211201,-7.33206e-06,1.1497e-09,-6.71657e-14,-36423.6,-72.0026], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-250.956,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (361.68,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 70,
    label = "C3H4-A",
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
            NASAPolynomial(coeffs=[2.53983,0.0163344,-1.76495e-06,-4.64736e-09,1.72913e-12,22512.4,9.9357], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[9.77626,0.00530214,-3.70112e-07,-3.02639e-10,5.08958e-14,19549.7,-30.7706], Tmin=(1400,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
        E0 = (186.309,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (157.975,'J/mol/K'),
    ),
    shortDesc = """101993""",
    longDesc = 
"""
101993
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 71,
    label = "C3H5-A",
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
            NASAPolynomial(coeffs=[-0.529132,0.0334559,-2.53401e-05,1.02866e-08,-1.73258e-12,19494.1,24.6172], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[8.45884,0.0112695,-3.83793e-06,5.94059e-10,-3.43918e-14,16468.3,-23.2704], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (157.807,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """10/23/ 5 THERM""",
    longDesc = 
"""
10/23/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 72,
    label = "CH2CHO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.47617,0.0208974,-1.50124e-05,5.62967e-09,-8.76624e-13,-482.051,16.3756], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[7.54146,0.00682297,-2.36939e-06,3.71634e-10,-2.1716e-14,-2614.37,-16.2603], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-6.18796,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """8/10/ 4 THERM""",
    longDesc = 
"""
8/10/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 73,
    label = "CH2CH2CHO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {2,S} {7,S} {8,S}
4 C u0 p0 c0 {1,D} {2,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.36273,-0.00390713,3.59751e-05,-2.69209e-08,5.9892e-12,-755.243,-9.5314], Tmin=(298,'K'), Tmax=(1363,'K')),
            NASAPolynomial(coeffs=[9.96856,0.0161918,-6.64162e-06,1.15445e-09,-7.21982e-14,-4164.5,-27.3972], Tmin=(1363,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (1.19419,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (199.547,'J/mol/K'),
    ),
    shortDesc = """8/10/ 4 THERM""",
    longDesc = 
"""
8/10/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 74,
    label = "C3H6OOH2-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
5  C u1 p0 c0 {1,S} {3,S} {4,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09194,0.046922,-3.90281e-05,1.72381e-08,-3.07969e-12,-1893.78,20.0178], Tmin=(298,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[14.2163,0.0143382,-4.78004e-06,7.29133e-10,-4.17762e-14,-5673.82,-43.5771], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-15.908,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (266.063,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 75,
    label = "C4H8OOH2-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
6  C u1 p0 c0 {3,S} {5,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.45436,0.0563121,-3.84161e-05,1.34229e-08,-1.92383e-12,-6689.16,25.4248], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[17.9338,0.0192154,-6.64487e-06,1.0394e-09,-6.0624e-14,-12576.8,-63.6194], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-56.3174,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 76,
    label = "CH2OCHO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 C u1 p0 c0 {1,S} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,D} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31032,0.0180474,-2.7152e-06,-4.60919e-09,1.70037e-12,-20291.1,17.155], Tmin=(298,'K'), Tmax=(1442,'K')),
            NASAPolynomial(coeffs=[10.096,0.00719887,-2.59813e-06,4.18111e-10,-2.48723e-14,-23638.9,-27.1144], Tmin=(1442,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-169.628,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (149.66,'J/mol/K'),
    ),
    shortDesc = """4/15/ 8 THERM""",
    longDesc = 
"""
4/15/ 8 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]OC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 77,
    label = "C2H5COC2H4P",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {1,D} {2,S} {3,S}
6  C u1 p0 c0 {3,S} {14,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.39449,0.0498732,-3.07394e-05,9.9508e-09,-1.37571e-12,-9321.24,20.1163], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[16.2001,0.0205107,-6.96978e-06,1.07826e-09,-6.24324e-14,-14506.7,-55.2273], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-77.6213,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (340.893,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THRM""",
    longDesc = 
"""
2/22/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(=O)CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 78,
    label = "CH3CO3H",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {9,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {1,S} {3,D} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.24136,0.0337964,-2.53887e-05,9.67584e-09,-1.49266e-12,-42467.8,17.0668], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[12.506,0.0094779,-3.30402e-06,5.19631e-10,-3.04234e-14,-45985.7,-37.9196], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-353.685,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (195.39,'J/mol/K'),
    ),
    shortDesc = """6/26/95 THERM""",
    longDesc = 
"""
6/26/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 79,
    label = "C3H5-S",
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
            NASAPolynomial(coeffs=[1.32807,0.0253108,-1.5153e-05,4.74346e-09,-6.24666e-13,30798.1,18.3329], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[7.88766,0.0113013,-3.84213e-06,5.93983e-10,-3.43567e-14,28348.5,-17.4292], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (254.008,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """10/23/ 5 THERM""",
    longDesc = 
"""
10/23/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 80,
    label = "C3H5-T",
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
            NASAPolynomial(coeffs=[2.17917,0.0203827,-7.91414e-06,4.76906e-10,2.70399e-13,29600.3,14.8786], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[7.37492,0.011751,-4.00021e-06,6.18947e-10,-3.58215e-14,27398.2,-14.3479], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (244.869,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """10/23/ 5 THERM""",
    longDesc = 
"""
10/23/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 81,
    label = "NC3H7O2H",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {13,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.13367,0.048492,-3.31801e-05,1.19308e-08,-1.80905e-12,-24784.5,22.7256], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[15.0896,0.0171715,-5.98499e-06,9.40964e-10,-5.50728e-14,-29835.2,-52.809], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-207.426,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (291.007,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 82,
    label = "CH3CO2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {4,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.37441,0.0249116,-1.74309e-05,6.248e-09,-9.09517e-13,-27233,18.1405], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[8.5406,0.00832951,-2.84722e-06,4.41927e-10,-2.56373e-14,-29729.1,-20.3884], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-228.459,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """2/14/95 THERM""",
    longDesc = 
"""
2/14/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC([O])=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 83,
    label = "IC3H7O2H",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {13,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.519266,0.0532111,-4.05157e-05,1.63347e-08,-2.73751e-12,-27104.8,24.0815], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[15.7046,0.0165925,-5.77251e-06,9.06453e-10,-5.30084e-14,-32326.9,-57.1735], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-227.121,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (291.007,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 84,
    label = "NC3H7O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.10731,0.0396165,-2.49492e-05,8.5945e-09,-1.3124e-12,-7937.46,18.9083], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[12.6327,0.0169911,-5.88867e-06,9.22195e-10,-5.38231e-14,-11919.5,-38.5349], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-66.7515,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 85,
    label = "IC3H7O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.49942,0.0443081,-3.22414e-05,1.29687e-08,-2.23371e-12,-10258.8,20.2336], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[13.2493,0.0164082,-5.67432e-06,8.87336e-10,-5.17362e-14,-14411,-42.9066], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-86.4329,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 86,
    label = "CH3COCH2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {6,D}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {2,D} {4,S} {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.95535,0.0270255,-1.37385e-05,3.53736e-09,-4.03923e-13,-20667.9,5.21436], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[12.769,0.0142555,-4.92821e-06,7.70449e-10,-4.49111e-14,-23479.9,-32.7156], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-169.463,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (245.277,'J/mol/K'),
    ),
    shortDesc = """2/14/95""",
    longDesc = 
"""
2/14/95
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)CO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 87,
    label = "C2H3CHO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {2,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.292355,0.0354321,-2.94936e-05,1.281e-08,-2.26144e-12,-11652.2,22.8878], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[10.4185,0.00948963,-3.29311e-06,5.16279e-10,-3.01587e-14,-14963,-30.7235], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-99.783,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """6/26/95 THERM""",
    longDesc = 
"""
6/26/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 88,
    label = "C3H2",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,T}
2 C u2 p0 c0 {1,S} {5,S}
3 C u0 p0 c0 {1,T} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16671,0.0248257,-4.59164e-05,4.26802e-08,-1.48215e-11,63504.2,8.86945], Tmin=(150,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.67098,0.00274875,-4.37094e-07,-6.4556e-11,1.66389e-14,62597.2,-12.3689], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (150,'K'),
        Tmax = (4000,'K'),
        E0 = (527.814,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (103.931,'J/mol/K'),
    ),
    shortDesc = """102193""",
    longDesc = 
"""
102193.
[CH]C#C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 89,
    label = "IC4H9O",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {5,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.766696,0.0555174,-3.81796e-05,1.37862e-08,-2.07313e-12,-10111.1,30.6331], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[14.6766,0.0200942,-6.90362e-06,1.07496e-09,-6.24925e-14,-15579,-52.604], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-87.1655,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """8/ 9/ 4 THERM""",
    longDesc = 
"""
8/ 9/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)C[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 90,
    label = "C7H15-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  C u1 p0 c0 {4,S} {6,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0379156,0.0756727,-4.07474e-05,9.32679e-09,-4.92361e-13,-2356.05,33.7322], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[21.6369,0.0323325,-1.09274e-05,1.68357e-09,-9.71774e-14,-10587.4,-85.221], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-21.0719,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (507.183,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 91,
    label = "C7H15-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  C u1 p0 c0 {3,S} {4,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0379156,0.0756727,-4.07474e-05,9.32679e-09,-4.92361e-13,-2356.05,33.7322], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[21.6369,0.0323325,-1.09274e-05,1.68357e-09,-9.71774e-14,-10587.4,-85.221], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-21.0719,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (507.183,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 92,
    label = "C7H15-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u1 p0 c0 {5,S} {21,S} {22,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.49957,0.0808826,-5.00533e-05,1.56549e-08,-1.96616e-12,-1045.9,34.6564], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[21.7941,0.032628,-1.11138e-05,1.72067e-09,-9.96367e-14,-9209.38,-86.4954], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-10.4556,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (507.183,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 93,
    label = "C7H15-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u1 p0 c0 {3,S} {4,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0379156,0.0756727,-4.07474e-05,9.32679e-09,-4.92361e-13,-2356.05,33.0427], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[21.6369,0.0323325,-1.09274e-05,1.68357e-09,-9.71774e-14,-10587.4,-85.9104], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-21.0719,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (507.183,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 94,
    label = "C5H11-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {3,S} {15,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.994216,0.0599861,-3.78319e-05,1.21311e-08,-1.57043e-12,4976.98,33.5998], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[15.4992,0.0238273,-8.13845e-06,1.26221e-09,-7.3173e-14,-1009.89,-55.8564], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (38.2617,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (365.837,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 95,
    label = "C6H13-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u1 p0 c0 {4,S} {18,S} {19,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.204871,0.0683801,-4.14448e-05,1.26156e-08,-1.5312e-12,1832.8,31.6075], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[18.5385,0.0283108,-9.65307e-06,1.49548e-09,-8.66336e-14,-5092.99,-70.4491], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (13.3119,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 96,
    label = "C6H13-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u1 p0 c0 {2,S} {3,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.22956,0.0633327,-3.24135e-05,6.46388e-09,-9.6142e-14,525.639,30.8006], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[18.3687,0.0280268,-9.47032e-06,1.45889e-09,-8.42002e-14,-6460.94,-69.0934], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (2.72793,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 97,
    label = "C6H13-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
6  C u1 p0 c0 {3,S} {5,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.22956,0.0633327,-3.24135e-05,6.46388e-09,-9.6142e-14,525.639,30.8006], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[18.3687,0.0280268,-9.47032e-06,1.45889e-09,-8.42002e-14,-6460.94,-69.0934], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (2.72793,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 98,
    label = "C5H11-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {2,S} {4,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.725188,0.0497344,-2.18806e-05,2.09008e-09,6.62753e-13,3464.18,26.7485], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[14.8745,0.0240594,-8.15588e-06,1.25867e-09,-7.27224e-14,-2147.34,-51.7908], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (27.2144,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (365.837,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 99,
    label = "C5H11-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {1,S} {2,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.725188,0.0497344,-2.18806e-05,2.09008e-09,6.62753e-13,3464.18,26.0591], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[14.8745,0.0240594,-8.15588e-06,1.25867e-09,-7.27224e-14,-2147.34,-52.4802], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (27.2144,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (365.837,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 100,
    label = "C7H133-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {6,D} {18,S}
6  C u0 p0 c0 {3,S} {5,D} {17,S}
7  C u1 p0 c0 {3,S} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.28817,0.078204,-5.22552e-05,1.82428e-08,-2.64174e-12,12986.8,38.9475], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.2595,0.0294019,-1.00313e-05,1.55475e-09,-9.0097e-14,5307.61,-77.3922], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (105.294,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC=CCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 101,
    label = "PC4H9O",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {5,S}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.499965,0.0537157,-3.44427e-05,1.08146e-08,-1.296e-12,-9116.44,30.9183], Tmin=(298,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[14.9316,0.0195927,-6.66958e-06,1.03223e-09,-5.97584e-14,-14617.9,-52.5562], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-78.5554,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """8/ 9/ 4 THERM""",
    longDesc = 
"""
8/ 9/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 102,
    label = "OCH2O2H",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {7,S}
3 O u1 p2 c0 {4,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.93823,0.0301466,-2.61053e-05,1.09464e-08,-1.78313e-12,-13816.7,18.5042], Tmin=(298,'K'), Tmax=(1420,'K')),
            NASAPolynomial(coeffs=[11.5398,0.00534291,-1.81879e-06,2.81969e-10,-1.63584e-14,-16823.7,-32.0701], Tmin=(1420,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-115.826,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (149.66,'J/mol/K'),
    ),
    shortDesc = """4/ 9/98 THERM""",
    longDesc = 
"""
4/ 9/98 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 103,
    label = "C2H4O2H",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {9,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46917,0.0271189,-2.08023e-05,8.44285e-09,-1.40756e-12,3896.88,14.3401], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[10.5229,0.00948091,-3.55728e-06,6.41446e-10,-4.21232e-14,1557.18,-23.1414], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (33.9376,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (195.39,'J/mol/K'),
    ),
    shortDesc = """1/14/ 5 THERM""",
    longDesc = 
"""
1/14/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 104,
    label = "C7H14-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {7,D} {21,S}
7  C u0 p0 c0 {5,S} {6,D} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.16533,0.079044,-4.96102e-05,1.58569e-08,-2.05346e-12,-11736.2,35.9871], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[20.6192,0.0314853,-1.07162e-05,1.65828e-09,-9.59912e-14,-19671.3,-82.2519], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-100.09,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (486.397,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 105,
    label = "C4H71-4",
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
            NASAPolynomial(coeffs=[-0.0409581,0.0406024,-2.6734e-05,9.28996e-09,-1.35368e-12,23031,27.9985], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[10.9215,0.0159294,-5.43642e-06,8.42696e-10,-4.88353e-14,19092.1,-31.2721], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (188.507,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """4/ 2/97 THERM""",
    longDesc = 
"""
4/ 2/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 106,
    label = "IC3H7CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {1,D} {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.503453,0.0441608,-2.82139e-05,8.93549e-09,-1.11327e-12,-9077.55,26.1991], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.3306,0.0161874,-5.56711e-06,8.67576e-10,-5.04697e-14,-13730.7,-43.3959], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-77.5242,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THERM""",
    longDesc = 
"""
2/22/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 107,
    label = "IC3H6CHO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  C u0 p0 c0 {1,D} {2,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.521482,0.0443114,-2.86617e-05,9.3032e-09,-1.20762e-12,-2996.77,26.8182], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.3102,0.0162098,-5.57576e-06,8.69004e-10,-5.05554e-14,-7621.78,-42.5051], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-26.95,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THERM""",
    longDesc = 
"""
2/22/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 108,
    label = "IC4H7",
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
            NASAPolynomial(coeffs=[-0.000720882,0.0436496,-3.16386e-05,1.23985e-08,-2.04378e-12,14365.4,23.3234], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[11.6383,0.0157681,-5.38539e-06,8.35173e-10,-4.84141e-14,10340.8,-39.026], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (116.641,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """10/23/ 5 THERM""",
    longDesc = 
"""
10/23/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(=C)C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 109,
    label = "TC3H6CHO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {3,S} {5,S}
5  C u0 p0 c0 {1,D} {4,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87053,0.041487,-2.66816e-05,9.01532e-09,-1.27871e-12,-8977.31,16.6174], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[13.1013,0.0166392,-5.68458e-06,8.81808e-10,-5.1129e-14,-13063.9,-44.2706], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-75.4505,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THERM""",
    longDesc = 
"""
2/22/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 110,
    label = "C7H14-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {7,D} {19,S}
7  C u0 p0 c0 {6,D} {20,S} {21,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.67721,0.0824612,-5.46504e-05,1.87862e-08,-2.65738e-12,-10216.9,38.5068], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[21.0898,0.0310608,-1.05645e-05,1.63406e-09,-9.45598e-14,-18326,-84.4391], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-87.8533,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (486.397,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 111,
    label = "C5H10-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.06223,0.0574218,-3.74487e-05,1.27365e-08,-1.7961e-12,-4465.47,32.274], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.5852,0.0224072,-7.63348e-06,1.18189e-09,-6.84385e-14,-10089.8,-52.3684], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-40.481,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (345.051,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 112,
    label = "C4H71-1",
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
            NASAPolynomial(coeffs=[0.119943,0.0415804,-2.89254e-05,1.08175e-08,-1.70622e-12,28039.1,25.8582], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[11.2162,0.0156658,-5.34225e-06,8.27633e-10,-4.79429e-14,24140.4,-33.8119], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (230.392,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """4/ 2/97 THERM""",
    longDesc = 
"""
4/ 2/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 113,
    label = "CH3COCH2O2H",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {12,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {3,D} {4,S} {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.9479,0.0360474,-2.2172e-05,6.98297e-09,-9.21269e-13,-38868.7,8.49926], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[15.2373,0.0144115,-5.0129e-06,7.87071e-10,-4.60226e-14,-42756.4,-47.7384], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-321.461,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (266.063,'J/mol/K'),
    ),
    shortDesc = """2/14/95""",
    longDesc = 
"""
2/14/95
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 114,
    label = "C4H8COCH3-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
6  C u1 p0 c0 {2,S} {4,S} {18,S}
7  C u0 p0 c0 {1,D} {3,S} {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32442,0.056036,-2.62898e-05,3.55349e-09,4.6256e-13,-13220.3,23.6967], Tmin=(298,'K'), Tmax=(1365,'K')),
            NASAPolynomial(coeffs=[19.2472,0.0247394,-8.34917e-06,1.28607e-09,-7.42515e-14,-19896.4,-70.0732], Tmin=(1365,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-110.264,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THRM""",
    longDesc = 
"""
2/22/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCC(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 115,
    label = "C4H71-2",
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
            NASAPolynomial(coeffs=[0.964124,0.0366781,-2.17105e-05,6.5588e-09,-8.11791e-13,26842.3,22.4366], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[10.7092,0.0161103,-5.49846e-06,8.52304e-10,-4.93905e-14,23187.4,-30.7648], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (221.256,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """4/ 2/97 THERM""",
    longDesc = 
"""
4/ 2/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 116,
    label = "CH3COCH2O",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  O u0 p2 c0 {5,D}
3  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {2,D} {3,S} {4,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72928,0.0263944,-1.09796e-05,8.58185e-10,3.39475e-13,-19155.2,11.8505], Tmin=(298,'K'), Tmax=(1370,'K')),
            NASAPolynomial(coeffs=[11.4638,0.0132124,-4.5658e-06,7.13898e-10,-4.16281e-14,-22383.3,-31.5128], Tmin=(1370,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-159.046,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """4/ 3/ 0 THERM""",
    longDesc = 
"""
4/ 3/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)C[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 117,
    label = "C4H8CHO-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
5  C u1 p0 c0 {2,S} {4,S} {14,S}
6  C u0 p0 c0 {1,D} {3,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67005,0.0458193,-2.2941e-05,4.53761e-09,-1.26594e-13,-6670.03,20.425], Tmin=(298,'K'), Tmax=(2014,'K')),
            NASAPolynomial(coeffs=[14.1408,0.0228358,-7.96904e-06,1.2604e-09,-7.42467e-14,-10796,-42.21], Tmin=(2014,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-55.6233,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (340.893,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 118,
    label = "NC4H9CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u1 p0 c0 {1,D} {4,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.4353,0.0493682,-2.89883e-05,8.42864e-09,-9.68287e-13,-11467.6,19.2696], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[16.1783,0.0207992,-7.11788e-06,1.1056e-09,-6.41697e-14,-16653.8,-55.8944], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-95.3974,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (340.893,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 119,
    label = "C5H10CHO-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u1 p0 c0 {2,S} {3,S} {17,S}
7  C u0 p0 c0 {1,D} {4,S} {18,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.417,0.0637354,-3.53662e-05,7.90793e-09,-2.83992e-13,-10063.3,33.0279], Tmin=(298,'K'), Tmax=(1371,'K')),
            NASAPolynomial(coeffs=[20.1227,0.0238797,-8.0293e-06,1.23389e-09,-7.11284e-14,-17416.2,-74.8169], Tmin=(1371,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-85.3039,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 120,
    label = "C7H132-6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
5  C u1 p0 c0 {1,S} {3,S} {18,S}
6  C u0 p0 c0 {2,S} {7,D} {19,S}
7  C u0 p0 c0 {4,S} {6,D} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.192192,0.0687557,-3.7091e-05,8.46587e-09,-4.34597e-13,11415.3,33.0601], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[20.0523,0.0290375,-9.79904e-06,1.50841e-09,-8.70207e-14,3879.94,-75.9218], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (93.429,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCC=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 121,
    label = "C6H12-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {16,S}
6  C u0 p0 c0 {5,D} {17,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.35275,0.0698655,-4.59408e-05,1.56967e-08,-2.21296e-12,-7343.69,35.3121], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[17.8338,0.0267378,-9.10037e-06,1.4082e-09,-8.15124e-14,-14206.3,-68.3819], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-64.1514,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (415.724,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 122,
    label = "C3H6CHO-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {2,S} {3,S} {11,S}
5  C u0 p0 c0 {1,D} {2,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.95068,0.0334223,-1.45357e-05,1.67282e-09,2.62012e-13,-3790.34,17.4324], Tmin=(298,'K'), Tmax=(1682,'K')),
            NASAPolynomial(coeffs=[11.1943,0.0181807,-6.35917e-06,1.00727e-09,-5.93944e-14,-6868.26,-28.0299], Tmin=(1682,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-31.8381,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """11/15/95 THERM""",
    longDesc = 
"""
11/15/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 123,
    label = "C2H3CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u1 p0 c0 {1,D} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.36242,0.0315274,-3.00219e-05,1.48167e-08,-2.87972e-12,4257.7,17.2627], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[9.37468,0.00791297,-2.67198e-06,4.11115e-10,-2.36979e-14,1929.7,-24.0893], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (33.6088,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """4/ 3/ 0 THERM""",
    longDesc = 
"""
4/ 3/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 124,
    label = "NC3H7O",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.21687,0.041479,-2.68724e-05,8.76686e-09,-1.13948e-12,-6213.58,27.8943], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[11.4772,0.0154937,-5.29459e-06,8.21477e-10,-4.76383e-14,-10399.9,-35.3681], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-54.8089,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """8/ 9/ 4 THERM""",
    longDesc = 
"""
8/ 9/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 125,
    label = "IC3H7O",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.818261,0.0468807,-3.74369e-05,1.55917e-08,-2.64308e-12,-8151.53,27.9483], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[12.3135,0.0138063,-4.91586e-06,8.21076e-10,-5.07493e-14,-12471.7,-41.7271], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-71.2928,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """8/ 9/ 4 THERM""",
    longDesc = 
"""
8/ 9/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 126,
    label = "C2H5COC2H5",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {1,D} {2,S} {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.59095,0.0545542,-3.33408e-05,1.05931e-08,-1.42003e-12,-33928.3,20.9983], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[16.7132,0.022477,-7.6183e-06,1.17658e-09,-6.80457e-14,-39602,-61.5362], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-282.814,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (365.837,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THERM""",
    longDesc = 
"""
2/22/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(=O)CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 127,
    label = "NC3H7COCH2",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {5,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {3,S} {6,D}
6  C u0 p0 c0 {5,D} {14,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.958299,0.0568163,-3.99113e-05,1.52672e-08,-2.49221e-12,-12306.2,23.4113], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[16.1502,0.0214093,-7.3606e-06,1.14657e-09,-6.66713e-14,-17696.9,-58.3865], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-103.536,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (345.051,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THERM""",
    longDesc = 
"""
2/22/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C([O])CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 128,
    label = "CH2OCH2O2H",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u0 p2 c0 {2,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
5  C u1 p0 c0 {1,S} {8,S} {9,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.52896,0.0424128,-3.73406e-05,1.66639e-08,-2.96443e-12,-14429.3,17.6899], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[15.1192,0.00923719,-3.19128e-06,4.99115e-10,-2.91162e-14,-18411.5,-48.5707], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-119.877,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (216.176,'J/mol/K'),
    ),
    shortDesc = """7/20/98 THERM""",
    longDesc = 
"""
7/20/98 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]OCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 129,
    label = "C3KET13",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {12,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
6  C u0 p0 c0 {3,D} {4,S} {11,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55241,0.041872,-2.9455e-05,1.09983e-08,-1.75046e-12,-34890.3,14.2083], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[15.8927,0.0140991,-4.96119e-06,7.84992e-10,-4.61489e-14,-39377.5,-52.6049], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-289.486,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (266.063,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 130,
    label = "NC3H7CHO",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {1,D} {3,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87416,0.041924,-2.35149e-05,6.26914e-09,-6.09444e-13,-27103.2,19.1569], Tmin=(298,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[13.5988,0.0181652,-6.17844e-06,9.5598e-10,-5.53443e-14,-31584.5,-45.179], Tmin=(1378,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-226.154,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """9/27/95 THERM""",
    longDesc = 
"""
9/27/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 131,
    label = "NC3H7CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {1,D} {3,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67257,0.0371199,-2.06863e-05,5.48874e-09,-5.35864e-13,-8580.51,16.4849], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[13.0026,0.0163105,-5.57643e-06,8.65671e-10,-5.02256e-14,-12552.3,-40.2609], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-71.5577,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """9/27/95 THERM""",
    longDesc = 
"""
9/27/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 132,
    label = "C4H72-2",
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
            NASAPolynomial(coeffs=[2.43874,0.0292296,-1.10908e-05,3.35089e-10,4.9567e-13,25086.4,15.222], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[10.1554,0.0165013,-5.61672e-06,8.69104e-10,-5.03037e-14,21824.2,-28.1885], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (207.864,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """4/ 2/97 THERM""",
    longDesc = 
"""
4/ 2/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C]=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 133,
    label = "IC4H7OH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.691,0.0427169,-2.49282e-05,7.00962e-09,-7.23263e-13,-21451.2,19.9501], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[13.5043,0.0178647,-5.99304e-06,9.18718e-10,-5.28435e-14,-25825.6,-44.4646], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-179.163,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """4/ 8/97 THERM""",
    longDesc = 
"""
4/ 8/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 134,
    label = "CH2CH2COCH3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,D} {2,S} {3,S}
5  C u1 p0 c0 {2,S} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.40256,0.0367294,-1.97317e-05,5.07323e-09,-4.99655e-13,-6150.07,19.3993], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[12.4694,0.0171022,-5.92157e-06,9.26817e-10,-5.40731e-14,-10137.8,-36.2186], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-51.7299,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """6/21/95 THER""",
    longDesc = 
"""
6/21/95 THER
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 135,
    label = "C2H5COCH2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,D} {2,S} {5,S}
5  C u1 p0 c0 {4,S} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.54014,0.0439486,-2.97002e-05,1.05495e-08,-1.58599e-12,-9507.97,19.9707], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[14.2099,0.0157866,-5.50529e-06,8.65871e-10,-5.06913e-14,-14128.5,-48.7133], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-80.1698,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """4/ 3/ 0 THERM""",
    longDesc = 
"""
4/ 3/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(=O)CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 136,
    label = "SC4H9O",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {8,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.409001,0.0538573,-3.39106e-05,1.01024e-08,-1.11268e-12,-11111,28.8555], Tmin=(298,'K'), Tmax=(1679,'K')),
            NASAPolynomial(coeffs=[14.3323,0.0204542,-7.12272e-06,1.12545e-09,-6.62698e-14,-16000.7,-50.2031], Tmin=(1679,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-94.9453,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """8/ 9/ 4 THERM""",
    longDesc = 
"""
8/ 9/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 137,
    label = "NC4H9CHO",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {1,D} {4,S} {16,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.59663,0.0543541,-3.21021e-05,9.35774e-09,-1.06689e-12,-29984.1,22.1281], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[16.7965,0.0225685,-7.67632e-06,1.18769e-09,-6.87546e-14,-35682.6,-60.9063], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-249.954,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (365.837,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 138,
    label = "C5H10-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.541561,0.053963,-3.23509e-05,9.77416e-09,-1.18535e-12,-5986.06,29.7143], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[14.1109,0.0228348,-7.78627e-06,1.20627e-09,-6.98796e-14,-11433.7,-50.1601], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-52.6515,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (345.051,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 139,
    label = "NC3H7COCH3",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {1,D} {3,S} {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24037,0.0542494,-3.14825e-05,9.14492e-09,-1.07666e-12,-33627.6,23.615], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[16.1842,0.0235246,-8.09675e-06,1.26231e-09,-7.34488e-14,-39337.5,-58.2981], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-280.713,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (365.837,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THERM""",
    longDesc = 
"""
2/22/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 140,
    label = "NC3H7COC2H5",
    molecule = 
"""
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {1,D} {3,S} {4,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.283,0.067085,-4.19985e-05,1.36804e-08,-1.86987e-12,-36803.9,24.8055], Tmin=(298,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[19.9628,0.0268078,-9.08527e-06,1.40288e-09,-8.11176e-14,-43721.6,-76.8703], Tmin=(1378,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-306.594,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THRM""",
    longDesc = 
"""
2/22/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(=O)CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 141,
    label = "AC3H5CHO",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {5,D} {8,S}
4  C u0 p0 c0 {1,D} {2,S} {9,S}
5  C u0 p0 c0 {3,D} {10,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.159653,0.0425761,-2.91901e-05,1.04044e-08,-1.53683e-12,-10786,28.2087], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[12.2811,0.0150167,-5.17605e-06,8.07797e-10,-4.70379e-14,-15098.5,-37.2056], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-92.2707,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 142,
    label = "C7H131-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {3,S} {6,S} {17,S}
6  C u0 p0 c0 {5,S} {7,D} {18,S}
7  C u0 p0 c0 {6,D} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.01708,0.0808916,-5.43384e-05,1.88066e-08,-2.66059e-12,6665.08,38.9797], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.6978,0.0293585,-9.99754e-06,1.54773e-09,-8.96231e-14,-1380.5,-83.5627], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (52.0735,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C[CH]CCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 143,
    label = "C7H131-5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {3,S} {17,S}
6  C u0 p0 c0 {2,S} {7,D} {18,S}
7  C u0 p0 c0 {6,D} {19,S} {20,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.337871,0.0722549,-4.22499e-05,1.14646e-08,-1.05307e-12,12922.3,35.6637], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[20.5321,0.0285989,-9.64126e-06,1.48314e-09,-8.55246e-14,5206.65,-78.1607], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (105.65,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC[CH]CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 144,
    label = "C7H131-6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {2,S} {4,S} {17,S}
6  C u0 p0 c0 {3,S} {7,D} {18,S}
7  C u0 p0 c0 {6,D} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.337871,0.0722549,-4.22499e-05,1.14646e-08,-1.05307e-12,12922.3,35.6637], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[20.5321,0.0285989,-9.64126e-06,1.48314e-09,-8.55246e-14,5206.65,-78.1607], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (105.65,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCC[CH]C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 145,
    label = "C7H131-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {2,S} {3,S} {17,S}
6  C u0 p0 c0 {3,S} {7,D} {18,S}
7  C u0 p0 c0 {6,D} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.337871,0.0722549,-4.22499e-05,1.14646e-08,-1.05307e-12,12922.3,35.6637], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[20.5321,0.0285989,-9.64126e-06,1.48314e-09,-8.55246e-14,5206.65,-78.1607], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (105.65,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC[CH]CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 146,
    label = "C7H131-7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {7,D} {16,S}
6  C u1 p0 c0 {4,S} {17,S} {18,S}
7  C u0 p0 c0 {5,D} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.856744,0.0777196,-5.19282e-05,1.80146e-08,-2.57342e-12,14241,36.8477], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.6754,0.0289092,-9.83223e-06,1.5208e-09,-8.80072e-14,6593.6,-79.3565], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (116.213,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCCC=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 147,
    label = "C7H132-5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
5  C u1 p0 c0 {1,S} {2,S} {18,S}
6  C u0 p0 c0 {2,S} {7,D} {20,S}
7  C u0 p0 c0 {4,S} {6,D} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.192192,0.0687557,-3.7091e-05,8.46587e-09,-4.34597e-13,11415.3,33.0601], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[20.0523,0.0290375,-9.79904e-06,1.50841e-09,-8.70207e-14,3879.94,-75.9218], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (93.429,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC[CH]CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 148,
    label = "C7H132-7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {6,D} {17,S}
6  C u0 p0 c0 {4,S} {5,D} {18,S}
7  C u1 p0 c0 {3,S} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.454324,0.0747545,-4.75103e-05,1.54448e-08,-2.04404e-12,12754.1,34.8465], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[20.2039,0.0293419,-9.98811e-06,1.54578e-09,-8.94872e-14,5262.91,-77.1645], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (104.13,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCC=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 149,
    label = "C7H132-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
5  C u1 p0 c0 {2,S} {7,S} {18,S}
6  C u0 p0 c0 {4,S} {7,D} {19,S}
7  C u0 p0 c0 {5,S} {6,D} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.50556,0.0774759,-4.92983e-05,1.58762e-08,-2.05625e-12,5160.84,36.4616], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[20.2284,0.0297818,-1.01488e-05,1.57188e-09,-9.105e-14,-2711.2,-81.3824], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (39.9755,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C[CH]CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 150,
    label = "C7H14-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {20,S}
7  C u0 p0 c0 {2,S} {6,D} {21,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.03027,0.0826324,-5.45514e-05,1.87706e-08,-2.67571e-12,-11514.1,40.2316], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.6823,0.0315389,-1.07571e-05,1.6669e-09,-9.6581e-14,-19645.1,-82.5235], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-99.0644,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (486.397,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 151,
    label = "C5H91-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {11,S}
4  C u0 p0 c0 {1,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.207302,0.0475323,-2.55232e-05,5.70571e-09,-2.53927e-13,18830,29.7528], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[13.9904,0.0199963,-6.73106e-06,1.03448e-09,-5.96149e-14,13607.5,-45.8753], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (154.407,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC[CH]C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 152,
    label = "C5H91-5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u1 p0 c0 {2,S} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.300352,0.052903,-3.502e-05,1.2128e-08,-1.7446e-12,20148.2,30.8939], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.1604,0.020271,-6.90765e-06,1.06973e-09,-6.1953e-14,14979.5,-47.2301], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (164.876,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 153,
    label = "C5H91-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.38014,0.0557608,-3.70144e-05,1.26884e-08,-1.78539e-12,12559,32.6441], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.186,0.0207129,-7.06961e-06,1.09607e-09,-6.35322e-14,7004.96,-51.4502], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (100.575,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C[CH]CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 154,
    label = "C6H12-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {6,D} {18,S}
6  C u0 p0 c0 {4,S} {5,D} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.837811,0.0664335,-4.08802e-05,1.27558e-08,-1.60665e-12,-8863.47,32.7785], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[17.3616,0.0271635,-9.25249e-06,1.43248e-09,-8.29473e-14,-15551,-66.1857], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-76.3629,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (415.724,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 155,
    label = "C6H12-3",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {6,D} {17,S}
6  C u0 p0 c0 {2,S} {5,D} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.74472,0.0702087,-4.60837e-05,1.58226e-08,-2.26114e-12,-8635.1,36.5274], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[17.4392,0.0272013,-9.28739e-06,1.44012e-09,-8.34783e-14,-15531.2,-67.2316], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-75.3627,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (415.724,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 156,
    label = "NC4H9COCH3",
    molecule = 
"""
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {1,D} {4,S} {6,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.04489,0.0662869,-3.9485e-05,1.19083e-08,-1.47157e-12,-36520.1,26.2127], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[19.3396,0.0280294,-9.64368e-06,1.50309e-09,-8.74432e-14,-43430.9,-73.8144], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-304.563,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THERM""",
    longDesc = 
"""
2/22/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 157,
    label = "C3H5O",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {8,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.19823,0.030558,-1.8063e-05,4.8615e-09,-4.19855e-13,9582.18,21.5566], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[10.2552,0.0114984,-3.84646e-06,5.8891e-10,-3.38558e-14,6265.61,-27.7655], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (77.8242,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """7/20/95 THERM""",
    longDesc = 
"""
7/20/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 158,
    label = "HOCH2OCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,S} {8,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
5 C u1 p0 c0 {1,S} {3,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.08181,0.0128768,2.04419e-06,-6.10155e-09,1.79821e-12,-43952.6,2.54054], Tmin=(298,'K'), Tmax=(1603,'K')),
            NASAPolynomial(coeffs=[11.3737,0.00817664,-2.92034e-06,4.66696e-10,-2.76277e-14,-46557.6,-28.6035], Tmin=(1603,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-364.664,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (170.447,'J/mol/K'),
    ),
    shortDesc = """8/31/99 THERM""",
    longDesc = 
"""
8/31/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=[C]OCO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 159,
    label = "C7H15O-3",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {6,S} {15,S}
5  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {8,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {21,S} {22,S} {23,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.09088,0.0923217,-6.44478e-05,2.36808e-08,-3.61068e-12,-19992.7,37.7738], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[24.3071,0.0331268,-1.13034e-05,1.75199e-09,-1.01527e-13,-28862.3,-98.7361], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-168.13,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (532.126,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC([O])CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 160,
    label = "C6H13O-2",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {5,S}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {3,S} {7,S} {14,S}
6  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.78125,0.0797869,-5.58105e-05,2.06261e-08,-3.17214e-12,-17117.2,34.6484], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[21.057,0.0287987,-9.83768e-06,1.5259e-09,-8.84677e-14,-24745.2,-82.714], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-144.39,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 161,
    label = "C5H11O-2",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {2,S} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.494528,0.067315,-4.72325e-05,1.75937e-08,-2.73652e-12,-14237.2,31.6371], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[17.8183,0.0244542,-8.36506e-06,1.29863e-09,-7.53357e-14,-20635.1,-66.7615], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-120.646,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 162,
    label = "C6H111-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {5,S} {14,S}
5  C u0 p0 c0 {4,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {16,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.68401,0.0682608,-4.55829e-05,1.5692e-08,-2.21118e-12,9682.84,35.7445], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[17.4386,0.025039,-8.5348e-06,1.3221e-09,-7.65893e-14,2886.67,-67.4868], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (76.9627,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C[CH]CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 163,
    label = "C6H112-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {6,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {16,S}
6  C u0 p0 c0 {4,S} {5,D} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.16992,0.0648326,-4.05263e-05,1.27525e-08,-1.60498e-12,8163.16,33.2149], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[16.9676,0.0254635,-8.68644e-06,1.3463e-09,-7.80191e-14,1541.57,-65.2971], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (64.7773,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C[CH]CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 164,
    label = "C6H111-5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  C u0 p0 c0 {2,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {16,S} {17,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0666672,0.059899,-3.38938e-05,8.58922e-09,-6.5433e-13,15949.3,32.7148], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[17.2621,0.0242963,-8.18564e-06,1.25872e-09,-7.25641e-14,9479.65,-62.023], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (130.649,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC[CH]C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 165,
    label = "C6H112-5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {2,S} {15,S}
5  C u0 p0 c0 {1,S} {6,D} {16,S}
6  C u0 p0 c0 {3,S} {5,D} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.463606,0.0563992,-2.87342e-05,5.59015e-09,-3.57958e-14,14427.2,30.1102], Tmin=(298,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[16.7818,0.0247357,-8.34368e-06,1.28403e-09,-7.40628e-14,8138.1,-59.7811], Tmin=(1377,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (118.316,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CC=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 166,
    label = "C6H111-6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {13,S}
5  C u1 p0 c0 {3,S} {14,S} {15,S}
6  C u0 p0 c0 {4,D} {16,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.617485,0.0654674,-4.36872e-05,1.51937e-08,-2.18414e-12,17273.9,34.0545], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[17.413,0.0245984,-8.37353e-06,1.29588e-09,-7.50183e-14,10861.4,-63.267], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (141.182,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCC=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 167,
    label = "C2H5COCH3",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {1,D} {2,S} {4,S}
6  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[1.60665,0.0413951,-2.23585e-05,5.78456e-09,-5.6953e-13,-30758.6,20.243], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[12.9004,0.0192212,-6.63871e-06,1.03733e-09,-6.0451e-14,-35206.2,-42.0804], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-256.949,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """4/ 3/ 0 THERM""",
    longDesc = 
"""
4/ 3/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 168,
    label = "C7H15O2-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {8,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {8,S} {18,S} {19,S}
7  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
8  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
9  C u0 p0 c0 {7,S} {22,S} {23,S} {24,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.20889,0.0884062,-5.79861e-05,2.03575e-08,-3.0646e-12,-19291.9,29.8117], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[25.2657,0.0350804,-1.21179e-05,1.89361e-09,-1.10354e-13,-28111.3,-100.705], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-160.472,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (552.912,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCCCO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 169,
    label = "NC5H11CHO",
    molecule = 
"""
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {1,D} {5,S} {19,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.37517,0.066567,-4.04423e-05,1.23836e-08,-1.52906e-12,-32874.1,24.8344], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[19.8891,0.0271869,-9.27392e-06,1.43744e-09,-8.33091e-14,-39752.3,-76.0742], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-273.807,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 170,
    label = "CH3CHCOCH3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {5,S} {12,S}
5  C u0 p0 c0 {1,D} {3,S} {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.812941,0.0429257,-2.6923e-05,8.59327e-09,-1.13188e-12,-10524.7,23.2953], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[13.1388,0.0166091,-5.76924e-06,9.04978e-10,-5.28827e-14,-15116.2,-43.8877], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-89.3785,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """4/ 3/ 0 THERM""",
    longDesc = 
"""
4/ 3/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 171,
    label = "C2H5COC2H4S",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {5,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {2,S} {6,D}
6  C u0 p0 c0 {4,S} {5,D} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.10728,0.0548903,-3.67696e-05,1.32867e-08,-2.06967e-12,-13743.5,23.2804], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[16.1904,0.0212169,-7.35413e-06,1.15187e-09,-6.72381e-14,-19265.1,-58.4937], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-115.443,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (345.051,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THRM""",
    longDesc = 
"""
2/22/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C([O])CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 172,
    label = "TC3H6OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {11,S}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0967,0.0380728,-2.75022e-05,1.07477e-08,-1.74896e-12,-14076.4,22.2476], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[11.2222,0.0136444,-4.51407e-06,7.10523e-10,-4.2269e-14,-17535,-31.8912], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-118.504,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (245.277,'J/mol/K'),
    ),
    shortDesc = """8/ 9/ 4 THERM""",
    longDesc = 
"""
8/ 9/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 173,
    label = "C4H7CHO1-4",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {1,D} {3,S} {12,S}
6  C u0 p0 c0 {4,D} {13,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.30688,0.0507912,-3.3151e-05,1.10391e-08,-1.49578e-12,-14559.6,24.0234], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[15.93,0.0184433,-6.21997e-06,9.57537e-10,-5.5258e-14,-19831.1,-55.1772], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-122.007,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """5/ 6/96 THERM""",
    longDesc = 
"""
5/ 6/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 174,
    label = "C6H13O2-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
8  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.525316,0.0823288,-5.89792e-05,2.29249e-08,-3.78641e-12,-18884.4,29.7738], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[22.8578,0.0298911,-1.0324e-05,1.61314e-09,-9.40034e-14,-26768.3,-90.3306], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-157.839,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (482.239,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CC)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 175,
    label = "C6H13O2-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
7  C u0 p0 c0 {1,S} {5,S} {17,S} {18,S}
8  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24283,0.0771349,-5.11549e-05,1.83242e-08,-2.83059e-12,-16577.7,27.9519], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.1225,0.030561,-1.0565e-05,1.6518e-09,-9.62963e-14,-24222,-85.256], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-138.225,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (482.239,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCCO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 176,
    label = "C6H13O2-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
8  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.525316,0.0823288,-5.89792e-05,2.29249e-08,-3.78641e-12,-18884.4,29.7738], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[22.8578,0.0298911,-1.0324e-05,1.61314e-09,-9.40034e-14,-26768.3,-90.3306], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-157.839,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (482.239,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 177,
    label = "C5H11O2-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.710786,0.0703522,-5.11565e-05,2.03005e-08,-3.42471e-12,-15990.3,27.9113], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[19.6656,0.0253946,-8.77477e-06,1.37146e-09,-7.9935e-14,-22652.1,-73.8934], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-133.993,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CC)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 178,
    label = "C5H11O2-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.710786,0.0703522,-5.11565e-05,2.03005e-08,-3.42471e-12,-15990.3,27.9113], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[19.6656,0.0253946,-8.77477e-06,1.37146e-09,-7.9935e-14,-22652.1,-73.8934], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-133.993,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 179,
    label = "C5H11O2-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.39788,0.0652789,-4.34224e-05,1.57152e-08,-2.46631e-12,-13679.1,25.5412], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[18.9703,0.0260356,-9.00707e-06,1.40889e-09,-8.21618e-14,-20125.4,-69.7478], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-114.352,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 180,
    label = "SC3H5CHO",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {1,D} {4,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.435795,0.0448719,-3.36583e-05,1.33067e-08,-2.17839e-12,-16039.5,23.7597], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.1696,0.0142484,-4.90844e-06,7.65789e-10,-4.45835e-14,-20403.3,-44.3673], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-135.521,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """11/15/95 THER""",
    longDesc = 
"""
11/15/95 THER
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 181,
    label = "C7H15O2-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {9,S} {17,S} {18,S}
7  C u0 p0 c0 {5,S} {8,S} {11,S} {12,S}
8  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
9  C u0 p0 c0 {6,S} {22,S} {23,S} {24,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.355253,0.0942381,-6.66955e-05,2.54796e-08,-4.13211e-12,-21579.5,32.9433], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[26.0536,0.0343832,-1.18713e-05,1.8545e-09,-1.08052e-13,-30684.2,-105.408], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-180.025,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (552.912,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(CC)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 182,
    label = "C7H15O2-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {17,S} {18,S}
8  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
9  C u0 p0 c0 {7,S} {22,S} {23,S} {24,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.355253,0.0942381,-6.66955e-05,2.54796e-08,-4.13211e-12,-21579.5,32.2539], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[26.0536,0.0343832,-1.18713e-05,1.8545e-09,-1.08052e-13,-30684.2,-106.097], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-180.025,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (552.912,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CCC)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 183,
    label = "C7H15O2-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {8,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {5,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {3,S} {22,S} {23,S} {24,S}
9  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.355253,0.0942381,-6.66955e-05,2.54796e-08,-4.13211e-12,-21579.5,32.9433], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[26.0536,0.0343832,-1.18713e-05,1.8545e-09,-1.08052e-13,-30684.2,-105.408], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-180.025,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (552.912,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCC(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 184,
    label = "C7H15O2H-3",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {25,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {9,S} {17,S} {18,S}
7  C u0 p0 c0 {5,S} {8,S} {11,S} {12,S}
8  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
9  C u0 p0 c0 {6,S} {22,S} {23,S} {24,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.602101,0.102885,-7.43423e-05,2.83646e-08,-4.51796e-12,-38626.9,36.7138], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.5706,0.0345345,-1.19627e-05,1.87305e-09,-1.09312e-13,-48841.5,-120.064], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-322.361,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (573.699,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 185,
    label = "TC4H9O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.08743,0.0582781,-4.33293e-05,1.76893e-08,-3.0677e-12,-14945.7,20.1872], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[16.7062,0.0207328,-7.17596e-06,1.12282e-09,-6.54941e-14,-20404.7,-63.5559], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-125.346,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (340.893,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 186,
    label = "O2CH2OCH2O2H",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {7,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {5,S} {7,S}
4  O u0 p2 c0 {2,S} {12,S}
5  O u1 p2 c0 {3,S}
6  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.99641,0.0583226,-5.5326e-05,2.59811e-08,-4.77141e-12,-32762.9,24.4215], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[19.2038,0.0104395,-3.60583e-06,5.63793e-10,-3.28807e-14,-37920.7,-65.1847], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-272.161,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (261.906,'J/mol/K'),
    ),
    shortDesc = """7/20/98 TRM""",
    longDesc = 
"""
7/20/98 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCOCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 187,
    label = "C3H6OOH2-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u1 p0 c0 {3,S} {10,S} {11,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09194,0.046922,-3.90281e-05,1.72381e-08,-3.07969e-12,-1893.78,20.0178], Tmin=(298,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[14.2163,0.0143382,-4.78004e-06,7.29133e-10,-4.17762e-14,-5673.82,-43.5771], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-15.908,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (266.063,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 188,
    label = "C6H13O2H-2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {22,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
8  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.438854,0.0910056,-6.66797e-05,2.58473e-08,-4.18106e-12,-35729.4,33.5762], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[25.3704,0.0300456,-1.04163e-05,1.63181e-09,-9.52693e-14,-44722.2,-104.961], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-298.498,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (503.026,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 189,
    label = "IC3H5OH",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {8,S} {9,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.58376,0.0316215,-1.73665e-05,4.18928e-09,-2.799e-13,-21264.3,18.8314], Tmin=(298,'K'), Tmax=(1374,'K')),
            NASAPolynomial(coeffs=[10.7381,0.0131698,-4.4153e-06,6.7701e-10,-3.89609e-14,-24729.8,-31.3634], Tmin=(1374,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-178.133,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """8/ 1/95 THERM""",
    longDesc = 
"""
8/ 1/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 190,
    label = "TC3H6OHCHO",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {14,S}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {2,D} {3,S} {13,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.210034,0.0563086,-3.95159e-05,1.3778e-08,-1.89069e-12,-48040.3,26.7836], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[17.0789,0.0174006,-5.93008e-06,9.18861e-10,-5.32512e-14,-53873,-63.8639], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-401.174,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (315.95,'J/mol/K'),
    ),
    shortDesc = """8/ 1/95 THERM""",
    longDesc = 
"""
8/ 1/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(O)C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 191,
    label = "C3H6OOH1-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {14,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
7  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14865,0.0533543,-4.08331e-05,1.67542e-08,-2.89288e-12,-18547.4,18.6305], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[18.5917,0.0165329,-5.81344e-06,9.19397e-10,-5.40321e-14,-23959.9,-64.2544], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-153.547,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (311.793,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TRM""",
    longDesc = 
"""
7/19/ 0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 192,
    label = "CH2CCH2OH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {4,D} {7,S} {8,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88423,0.0242428,-1.14152e-05,1.71775e-09,1.42177e-13,11793.6,15.2102], Tmin=(298,'K'), Tmax=(1372,'K')),
            NASAPolynomial(coeffs=[9.70702,0.0113973,-3.77994e-06,5.75209e-10,-3.29229e-14,9132.13,-22.5013], Tmin=(1372,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (97.7643,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (199.547,'J/mol/K'),
    ),
    shortDesc = """9/ 8/95 THERM""",
    longDesc = 
"""
9/ 8/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 193,
    label = "TC3H6O2CHO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {7,D}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {2,D} {4,S} {14,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17883,0.0541596,-3.83436e-05,1.38308e-08,-2.0419e-12,-22739.4,20.0751], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[18.5534,0.0168774,-5.90753e-06,9.31518e-10,-5.46345e-14,-28544.7,-68.2487], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-189.241,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (315.95,'J/mol/K'),
    ),
    shortDesc = """8/ 2/95 THERM""",
    longDesc = 
"""
8/ 2/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(C=O)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 194,
    label = "C3H4-P",
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
            NASAPolynomial(coeffs=[3.02973,0.0149896,-1.3985e-06,-3.96962e-09,1.38822e-12,21484.1,8.00459], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[9.7681,0.00521915,-3.75314e-07,-2.99219e-10,5.10788e-14,18602.8,-30.2068], Tmin=(1400,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
        E0 = (178.391,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """101993""",
    longDesc = 
"""
101993
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 195,
    label = "C5H11O2H-2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.268431,0.0790976,-5.89751e-05,2.33029e-08,-3.83795e-12,-32833,31.7836], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[22.1712,0.025554,-8.86857e-06,1.39034e-09,-8.12122e-14,-40602.7,-88.4831], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-274.647,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 196,
    label = "C6H113-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {2,S} {4,D} {14,S}
6  C u1 p0 c0 {2,S} {16,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.977624,0.0656665,-4.36212e-05,1.51942e-08,-2.20544e-12,15977.8,35.8177], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[17.0133,0.0250666,-8.56224e-06,1.32807e-09,-7.69999e-14,9538.6,-61.3921], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (129.972,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC=CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 197,
    label = "C6H12OOH3-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {7,S} {8,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
8  C u1 p0 c0 {3,S} {5,S} {20,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.01849,0.0805627,-5.46524e-05,1.90949e-08,-2.74736e-12,-12466.7,30.1432], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[24.2386,0.0282612,-9.75785e-06,1.52463e-09,-8.8853e-14,-20768.1,-95.3255], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-104.007,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]C(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 198,
    label = "C4H8OOH2-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {10,S}
6  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
7  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
8  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19248,0.0736763,-6.24428e-05,2.79371e-08,-5.10126e-12,-26177.4,22.9569], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[22.9951,0.0199239,-6.96327e-06,1.09678e-09,-6.42747e-14,-33009.5,-87.1462], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-217.021,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (382.466,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TRM""",
    longDesc = 
"""
7/19/ 0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O[O])C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 199,
    label = "C5H92-5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u1 p0 c0 {1,S} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.216351,0.0494614,-2.99439e-05,9.17729e-09,-1.13614e-12,18628.2,28.3575], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[13.6885,0.0206967,-7.0598e-06,1.09402e-09,-6.33886e-14,13634.6,-45.0307], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (152.677,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 200,
    label = "C7H133-7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {6,D} {17,S}
6  C u0 p0 c0 {3,S} {5,D} {18,S}
7  C u1 p0 c0 {2,S} {19,S} {20,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.28817,0.078204,-5.22552e-05,1.82428e-08,-2.64174e-12,12986.8,38.9475], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.2595,0.0294019,-1.00313e-05,1.55475e-09,-9.0097e-14,5307.61,-77.3922], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (105.294,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC=CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 201,
    label = "C5H92-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {5,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.861323,0.0523107,-3.19283e-05,9.73237e-09,-1.17586e-12,11038.6,30.0929], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[13.7128,0.0211392,-7.22186e-06,1.12036e-09,-6.49676e-14,5660.79,-49.2476], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (88.4449,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 202,
    label = "C7H133-6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
5  C u1 p0 c0 {2,S} {4,S} {18,S}
6  C u0 p0 c0 {1,S} {7,D} {20,S}
7  C u0 p0 c0 {2,S} {6,D} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.798785,0.0729104,-4.28677e-05,1.18819e-08,-1.16315e-12,11671.4,37.8868], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[20.0865,0.029125,-9.85196e-06,1.51881e-09,-8.77062e-14,3939.05,-76.0212], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (94.7732,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CC=CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 203,
    label = "C7H133-5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u1 p0 c0 {1,S} {7,S} {18,S}
6  C u0 p0 c0 {2,S} {7,D} {19,S}
7  C u0 p0 c0 {5,S} {6,D} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.36092,0.081027,-5.41952e-05,1.87684e-08,-2.67471e-12,5396.53,40.6609], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.2852,0.0298429,-1.01927e-05,1.58101e-09,-9.16702e-14,-2666.99,-81.6175], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (41.1037,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """6/24/99 THERM""",
    longDesc = 
"""
6/24/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]C=CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 204,
    label = "C6H112-6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {14,S}
5  C u0 p0 c0 {3,S} {4,D} {15,S}
6  C u1 p0 c0 {2,S} {16,S} {17,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.106007,0.0620508,-3.86461e-05,1.22632e-08,-1.57993e-12,15754.6,31.5419], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[16.9431,0.0250225,-8.52515e-06,1.32009e-09,-7.64493e-14,9515.57,-61.0793], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (128.95,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 205,
    label = "C6H111-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {14,S}
5  C u0 p0 c0 {2,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {16,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0666672,0.059899,-3.38938e-05,8.58922e-09,-6.5433e-13,15949.3,32.7148], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[17.2621,0.0242963,-8.18564e-06,1.25872e-09,-7.25641e-14,9479.65,-62.023], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (130.649,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC[CH]CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 206,
    label = "C3H6COC2H5-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {1,D} {2,S} {3,S}
7  C u1 p0 c0 {4,S} {17,S} {18,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.08959,0.0624878,-3.97257e-05,1.33753e-08,-1.92194e-12,-12199.3,23.2035], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[19.2391,0.0251659,-8.57508e-06,1.32847e-09,-7.69775e-14,-18540.5,-70.0617], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-101.406,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """2/22/96 TRM""",
    longDesc = 
"""
2/22/96 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC(=O)CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 207,
    label = "C4H8COCH3-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {1,D} {3,S} {5,S}
7  C u1 p0 c0 {4,S} {17,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.8308,0.061687,-3.69734e-05,1.12792e-08,-1.42171e-12,-11910.6,24.7214], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[18.9007,0.0259289,-8.93525e-06,1.39416e-09,-8.11665e-14,-18359.6,-68.5988], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-99.3509,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THRM""",
    longDesc = 
"""
2/22/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCC(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 208,
    label = "C3H6COC2H5-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,D} {2,S} {3,S}
7  C u1 p0 c0 {3,S} {5,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.83974,0.0559472,-2.81955e-05,5.56103e-09,-1.03164e-13,-13553.2,20.9458], Tmin=(298,'K'), Tmax=(1369,'K')),
            NASAPolynomial(coeffs=[19.1084,0.0249004,-8.41247e-06,1.29661e-09,-7.48883e-14,-19933.4,-68.9565], Tmin=(1369,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-112.419,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """2/22/96 TRM""",
    longDesc = 
"""
2/22/96 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CC(=O)CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 209,
    label = "C3H6COCH3-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {1,D} {2,S} {4,S}
6  C u1 p0 c0 {3,S} {14,S} {15,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.00033,0.0496075,-2.87471e-05,8.26667e-09,-9.51074e-13,-9010.11,22.2762], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[15.8053,0.0212787,-7.31842e-06,1.14049e-09,-6.63446e-14,-14282.8,-53.4017], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-75.4359,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (340.893,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THRM""",
    longDesc = 
"""
2/22/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 210,
    label = "C6H101-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {3,D} {5,S} {14,S}
5  C u0 p0 c0 {4,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.38508,0.0730622,-5.86808e-05,2.52425e-08,-4.4682e-12,4803.85,37.6104], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[17.2274,0.0228969,-7.84177e-06,1.21837e-09,-7.07191e-14,-1649.79,-66.307], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (35.6035,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (369.994,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC=CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 211,
    label = "IC4H6OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  C u1 p0 c0 {3,S} {8,S} {9,S}
5  C u0 p0 c0 {3,D} {10,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.863371,0.0468711,-3.4358e-05,1.33031e-08,-2.13915e-12,-3149.48,22.9076], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[14.0311,0.0155318,-5.32755e-06,8.28786e-10,-4.81545e-14,-7693.78,-47.6555], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-27.7647,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """8/19/95 THERM""",
    longDesc = 
"""
8/19/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(=C)CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 212,
    label = "IC4H7O",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74701,0.0407783,-2.4475e-05,7.06503e-09,-7.51571e-13,4869.79,19.4536], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[13.3458,0.0161219,-5.44376e-06,8.38199e-10,-4.83608e-14,611.444,-43.6819], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (39.6684,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (274.378,'J/mol/K'),
    ),
    shortDesc = """4/ 3/ 0 THERM""",
    longDesc = 
"""
4/ 3/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)C[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 213,
    label = "C5H81-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.32617,0.0638696,-5.57053e-05,2.58049e-08,-4.83406e-12,6551.83,34.2037], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[14.5574,0.0180939,-6.21672e-06,9.6792e-10,-5.62629e-14,1223.65,-54.389], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (49.6448,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (299.321,'J/mol/K'),
    ),
    shortDesc = """3/27/97 THERM""",
    longDesc = 
"""
3/27/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 214,
    label = "C2H3CHCHO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,D} {5,S} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {7,S}
4  C u1 p0 c0 {3,S} {8,S} {9,S}
5  C u0 p0 c0 {1,D} {2,S} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.00877993,0.0398631,-2.66131e-05,8.74645e-09,-1.14129e-12,6224.75,27.9592], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[12.4074,0.012732,-4.47199e-06,7.0682e-10,-4.15246e-14,1717.07,-39.4039], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (48.8678,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=CC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 215,
    label = "NC4H9COCH2",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {6,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {4,S} {7,D}
7  C u0 p0 c0 {6,D} {17,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.657241,0.069182,-4.79956e-05,1.78115e-08,-2.80456e-12,-15180.7,26.518], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[19.8576,0.0252406,-8.72523e-06,1.36422e-09,-7.95375e-14,-22053.2,-77.1141], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-127.301,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (415.724,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THERM""",
    longDesc = 
"""
2/22/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C([O])CCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 216,
    label = "C4H8COCH3-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
6  C u1 p0 c0 {2,S} {3,S} {18,S}
7  C u0 p0 c0 {1,D} {3,S} {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32442,0.056036,-2.62898e-05,3.55349e-09,4.6256e-13,-13220.3,23.6967], Tmin=(298,'K'), Tmax=(1365,'K')),
            NASAPolynomial(coeffs=[19.2472,0.0247394,-8.34917e-06,1.28607e-09,-7.42515e-14,-19896.4,-70.0732], Tmin=(1365,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-110.264,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THRM""",
    longDesc = 
"""
2/22/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CC(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 217,
    label = "NC3H7COC2H4S",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {6,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {3,S} {7,D}
7  C u0 p0 c0 {5,S} {6,D} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.82383,0.0674627,-4.57147e-05,1.66708e-08,-2.60417e-12,-16626.4,26.2565], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.341,0.0256927,-8.88366e-06,1.38917e-09,-8.09982e-14,-23341.6,-73.9481], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-139.257,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (415.724,'J/mol/K'),
    ),
    shortDesc = """2/22/96 TRM""",
    longDesc = 
"""
2/22/96 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C([O])CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 218,
    label = "C3H6CHO-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  C u0 p0 c0 {1,D} {3,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67672,0.0373064,-2.11281e-05,5.80473e-09,-6.09688e-13,-2497.14,17.5751], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[13.0323,0.0162418,-5.54388e-06,8.59724e-10,-4.9846e-14,-6459.16,-39.2399], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-20.9577,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """9/27/95 THERM""",
    longDesc = 
"""
9/27/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 219,
    label = "IC3H5CHO",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  C u0 p0 c0 {1,D} {3,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.627184,0.046678,-3.74431e-05,1.58331e-08,-2.73952e-12,-15720.3,21.6034], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[13.6204,0.0137917,-4.7337e-06,7.36655e-10,-4.20098e-14,-20002.5,-47.3185], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-132.493,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """7/19/95 THERM""",
    longDesc = 
"""
7/19/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 220,
    label = "AC3H5CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  C u1 p0 c0 {1,D} {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.9343,0.0377752,-2.61385e-05,9.34041e-09,-1.37598e-12,7742.24,25.6636], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[11.8647,0.0128853,-4.45461e-06,6.96613e-10,-4.06215e-14,3863.44,-33.299], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (62.5002,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 221,
    label = "C4H8CHO-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  C u1 p0 c0 {2,S} {3,S} {14,S}
6  C u0 p0 c0 {1,D} {3,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67005,0.0458193,-2.2941e-05,4.53761e-09,-1.26594e-13,-6670.03,20.425], Tmin=(298,'K'), Tmax=(2014,'K')),
            NASAPolynomial(coeffs=[14.1408,0.0228358,-7.96904e-06,1.2604e-09,-7.42467e-14,-10796,-42.21], Tmin=(2014,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-55.6233,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (340.893,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 222,
    label = "C6H11O1-4",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {7,D} {16,S}
7  C u0 p0 c0 {6,D} {17,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.17612,0.076782,-5.7919e-05,2.31284e-08,-3.81018e-12,-1678.3,37.0214], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[19.9304,0.0250879,-8.55881e-06,1.32643e-09,-7.68596e-14,-8792.49,-75.5242], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-16.5632,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (415.724,'J/mol/K'),
    ),
    shortDesc = """3/28/97 THERM""",
    longDesc = 
"""
3/28/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC([O])CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 223,
    label = "C6H111O2H-5",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {20,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {18,S} {19,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.671334,0.0872726,-6.78106e-05,2.77978e-08,-4.70537e-12,-20037.3,35.769], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[24.1598,0.0264142,-9.16605e-06,1.4369e-09,-8.39294e-14,-28453.9,-96.7105], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-168.333,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 224,
    label = "C6H112O2-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.861603,0.0749249,-5.46729e-05,2.16848e-08,-3.64612e-12,-3361.67,29.8764], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[21.1831,0.0266692,-9.21828e-06,1.44112e-09,-8.40099e-14,-10486.6,-79.2293], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-28.677,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCC(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 225,
    label = "C6H112O2H-5",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {20,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0977786,0.0836152,-6.24512e-05,2.46774e-08,-4.05916e-12,-21566.7,32.961], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[23.6805,0.0268319,-9.31238e-06,1.45996e-09,-8.52807e-14,-29789.4,-94.4537], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-180.638,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 226,
    label = "C6H111O2-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {18,S} {19,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.277529,0.078629,-6.01043e-05,2.4849e-08,-4.30167e-12,-1830.63,32.7344], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[21.6615,0.0262499,-9.07089e-06,1.41784e-09,-8.26434e-14,-9150.08,-81.4781], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-16.3642,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCC(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 227,
    label = "C4H8COCH3-4",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {7,D} {18,S}
7  C u0 p0 c0 {1,S} {5,S} {6,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.464937,0.0668009,-4.26203e-05,1.39372e-08,-1.88408e-12,-16315.9,28.2933], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[19.4544,0.0256278,-8.86916e-06,1.38781e-09,-8.09574e-14,-23309.7,-74.9578], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-137.025,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (415.724,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THRM""",
    longDesc = 
"""
2/22/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC=C(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 228,
    label = "C7H15O2H-1",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {8,S}
2  O u0 p2 c0 {1,S} {25,S}
3  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {8,S} {18,S} {19,S}
7  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
8  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
9  C u0 p0 c0 {7,S} {22,S} {23,S} {24,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.269179,0.0971212,-6.59766e-05,2.35449e-08,-3.52849e-12,-36345.1,33.4741], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[27.7186,0.0352624,-1.22144e-05,1.91237e-09,-1.11602e-13,-46226.7,-114.955], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-302.834,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (573.699,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 229,
    label = "C6H111O2-6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {18,S} {19,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2798,0.0721525,-5.02889e-05,1.89683e-08,-3.05539e-12,181.691,29.6254], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[20.9442,0.0268874,-9.2971e-06,1.45381e-09,-8.47642e-14,-6857.09,-76.462], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (1.07032,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCCCO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 230,
    label = "C2H3COCH3",
    molecule = 
"""
1  O u0 p2 c0 {3,D}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,D} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {10,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.245579,0.0426432,-2.91127e-05,1.03478e-08,-1.53551e-12,-17030.5,26.4431], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[12.5572,0.0149673,-5.20015e-06,8.15864e-10,-4.76824e-14,-21462.3,-40.1434], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-144.086,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """6/19/95 THERM""",
    longDesc = 
"""
6/19/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 231,
    label = "CH3CHOOCOCH3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {7,D}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {2,D} {4,S} {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.59405,0.0574729,-4.65071e-05,2.01817e-08,-3.61176e-12,-25344.5,26.0857], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[17.2171,0.017674,-6.10387e-06,9.53712e-10,-5.55757e-14,-30528,-56.796], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-211.196,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (315.95,'J/mol/K'),
    ),
    shortDesc = """6/27/95""",
    longDesc = 
"""
6/27/95
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)C(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 232,
    label = "C6H111O2H-6",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {20,S}
3  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {18,S} {19,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.311487,0.0810135,-5.85043e-05,2.22954e-08,-3.54988e-12,-18025,32.7266], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[23.4009,0.0270662,-9.39243e-06,1.47237e-09,-8.60004e-14,-26130.2,-91.422], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-150.901,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 233,
    label = "IC3H6CO",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {3,S} {5,D}
5  C u0 p0 c0 {1,D} {4,D}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.28039,0.0417017,-3.2509e-05,1.37243e-08,-2.40573e-12,-16394,13.8188], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[13.2548,0.0140143,-4.7891e-06,7.42924e-10,-4.30738e-14,-20053,-44.481], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-136.592,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """03/03/95 THERM""",
    longDesc = 
"""
03/03/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)=C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 234,
    label = "NC5H11CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  C u1 p0 c0 {1,D} {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.14479,0.0617864,-3.74135e-05,1.13284e-08,-1.36918e-12,-14345.1,22.3128], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[19.4784,0.0250466,-8.54861e-06,1.32558e-09,-7.68503e-14,-20792.4,-72.1996], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-119.184,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 235,
    label = "C5H10CHO-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
6  C u1 p0 c0 {3,S} {4,S} {17,S}
7  C u0 p0 c0 {1,D} {4,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.417,0.0637354,-3.53662e-05,7.90793e-09,-2.83992e-13,-10063.3,33.0279], Tmin=(298,'K'), Tmax=(1371,'K')),
            NASAPolynomial(coeffs=[20.1227,0.0238797,-8.0293e-06,1.23389e-09,-7.11284e-14,-17416.2,-74.8169], Tmin=(1371,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-85.3039,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]CC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 236,
    label = "C5H10CHO-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
6  C u1 p0 c0 {3,S} {5,S} {17,S}
7  C u0 p0 c0 {1,D} {4,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.417,0.0637354,-3.53662e-05,7.90793e-09,-2.83992e-13,-10063.3,33.0279], Tmin=(298,'K'), Tmax=(1371,'K')),
            NASAPolynomial(coeffs=[20.1227,0.0238797,-8.0293e-06,1.23389e-09,-7.11284e-14,-17416.2,-74.8169], Tmin=(1371,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-85.3039,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 237,
    label = "C5H10CHO-5",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {7,S}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {7,D} {17,S}
7  C u0 p0 c0 {1,S} {6,D} {18,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.26557,0.0736551,-5.04264e-05,1.74734e-08,-2.44117e-12,-13183.8,36.8188], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[20.2669,0.0247915,-8.54954e-06,1.33477e-09,-7.77453e-14,-20789,-79.3061], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-112.366,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (415.724,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC=C[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 238,
    label = "C5H10CHO-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {7,S} {14,S} {15,S}
6  C u1 p0 c0 {4,S} {16,S} {17,S}
7  C u0 p0 c0 {1,D} {5,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.15377,0.0619684,-3.78905e-05,1.17023e-08,-1.46276e-12,-8262.79,23.3779], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[19.4701,0.025049,-8.54839e-06,1.32543e-09,-7.68369e-14,-14687.8,-70.9736], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-68.5924,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 239,
    label = "IC4H8O",
    molecule = 
"""
multiplicity 3
1  O u1 p2 c0 {4,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
5  C u1 p0 c0 {2,S} {12,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.97374,0.0624619,-5.04348e-05,2.13345e-08,-3.67383e-12,-17327.4,36.2336], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[14.4625,0.0180563,-6.18009e-06,9.59941e-10,-5.57132e-14,-23023.1,-56.119], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-149.809,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """7/19/95 THERM""",
    longDesc = 
"""
7/19/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)C[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 240,
    label = "C6H113O2H-2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {20,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
4  C u0 p0 c0 {6,S} {8,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {3,S} {8,D} {19,S}
8  C u0 p0 c0 {4,S} {7,D} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.2674,0.089147,-7.04153e-05,2.94209e-08,-5.07122e-12,-20697.5,38.184], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[23.9773,0.0266036,-9.23895e-06,1.44906e-09,-8.46696e-14,-29203.2,-96.2905], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-174.403,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 241,
    label = "C3H6COCH3-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {2,S} {3,S} {15,S}
6  C u0 p0 c0 {1,D} {2,S} {4,S}
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
            NASAPolynomial(coeffs=[2.20585,0.0459606,-2.23176e-05,4.03645e-09,-1.91585e-14,-10291.8,22.4556], Tmin=(298,'K'), Tmax=(2017,'K')),
            NASAPolynomial(coeffs=[13.6995,0.0233998,-8.20838e-06,1.30268e-09,-7.69151e-14,-14477.4,-40.482], Tmin=(2017,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-86.2138,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (340.893,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THRM""",
    longDesc = 
"""
2/22/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CC(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 242,
    label = "C2H5COC2H3",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,D} {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {13,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.489126,0.0549952,-3.96989e-05,1.557e-08,-2.60071e-12,-20245.8,25.9411], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[15.5917,0.0196028,-6.79737e-06,1.06496e-09,-6.21767e-14,-25598.8,-55.3303], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-170.144,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THERM""",
    longDesc = 
"""
2/22/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(=O)CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 243,
    label = "C6H112O2H-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {20,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {3,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.753695,0.0873574,-6.83958e-05,2.84776e-08,-4.91363e-12,-20973.6,35.573], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[23.8606,0.0267263,-9.28634e-06,1.45697e-09,-8.51502e-14,-29323.9,-95.7046], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-176.257,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 244,
    label = "C3H6COCH3-3",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {6,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {6,D} {15,S}
6  C u0 p0 c0 {1,S} {4,S} {5,D}
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
            NASAPolynomial(coeffs=[0.636829,0.0550048,-3.53221e-05,1.18238e-08,-1.6555e-12,-13422.2,25.7839], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[15.7977,0.0217091,-7.46488e-06,1.163e-09,-6.76366e-14,-18967,-56.5048], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-113.187,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (345.051,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THRM""",
    longDesc = 
"""
2/22/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=C(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 245,
    label = "C7H15O-4",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {4,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {8,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {21,S} {22,S} {23,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.09088,0.0923217,-6.44478e-05,2.36808e-08,-3.61068e-12,-19992.7,37.0844], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[24.3071,0.0331268,-1.13034e-05,1.75199e-09,-1.01527e-13,-28862.3,-99.4256], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-168.13,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (532.126,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC([O])CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 246,
    label = "C7H13O1-3",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {5,S}
2  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {3,S} {7,S} {15,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {5,S} {8,D} {19,S}
8  C u0 p0 c0 {7,D} {20,S} {21,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.97187,0.0950411,-7.14211e-05,2.71212e-08,-4.11211e-12,-3699.99,46.8736], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[25.3924,0.0267015,-8.93163e-06,1.36777e-09,-7.86546e-14,-13199.2,-104.486], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-34.3801,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (486.397,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC([O])CCCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 247,
    label = "C6H11O1-3",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {6,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {7,D} {16,S}
7  C u0 p0 c0 {6,D} {17,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.54423,0.0815468,-6.04734e-05,2.2333e-08,-3.25461e-12,-939.931,43.2737], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[22.292,0.0224442,-7.53071e-06,1.15575e-09,-6.65675e-14,-9305.67,-89.4778], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-11.5944,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (415.724,'J/mol/K'),
    ),
    shortDesc = """3/28/97 THERM""",
    longDesc = 
"""
3/28/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC([O])CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 248,
    label = "C6H11O1-5",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {7,D} {16,S}
7  C u0 p0 c0 {6,D} {17,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.17612,0.076782,-5.7919e-05,2.31284e-08,-3.81018e-12,-1678.3,37.0214], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[19.9304,0.0250879,-8.55881e-06,1.32643e-09,-7.68596e-14,-8792.49,-75.5242], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-16.5632,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (415.724,'J/mol/K'),
    ),
    shortDesc = """3/28/97 THERM""",
    longDesc = 
"""
3/28/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCC(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 249,
    label = "C3H6CHO-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {2,S} {5,S} {11,S}
5  C u0 p0 c0 {1,D} {4,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35169,0.0423714,-2.69123e-05,8.70133e-09,-1.15287e-12,-6911.67,20.9382], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[13.4302,0.0162251,-5.60632e-06,8.76356e-10,-5.10864e-14,-11356.1,-44.7371], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-58.7582,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """11/15/95 THERM""",
    longDesc = 
"""
11/15/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 250,
    label = "OCH2OCHO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u1 p2 c0 {4,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
5 C u0 p0 c0 {1,S} {3,D} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.19691,0.015884,3.53541e-07,-6.10457e-09,1.94662e-12,-40224.3,6.11646], Tmin=(298,'K'), Tmax=(1475,'K')),
            NASAPolynomial(coeffs=[12.0234,0.00811263,-2.91356e-06,4.6734e-10,-2.77376e-14,-43364.7,-33.3692], Tmin=(1475,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-334.812,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (174.604,'J/mol/K'),
    ),
    shortDesc = """4/ 9/98 THERM""",
    longDesc = 
"""
4/ 9/98 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]COC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 251,
    label = "C2H3OOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {8,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35644,0.0337002,-2.75989e-05,1.14223e-08,-1.89489e-12,-5499.97,19.8354], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[11.575,0.00809909,-2.81809e-06,4.42698e-10,-2.58998e-14,-8848.53,-34.3859], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-47.2727,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (174.604,'J/mol/K'),
    ),
    shortDesc = """4/18/ 8 THERM""",
    longDesc = 
"""
4/18/ 8 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 252,
    label = "C4H7O1-4",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.292648,0.0483149,-3.48133e-05,1.31921e-08,-2.06486e-12,6299.79,30.363], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[13.1418,0.0164166,-5.56949e-06,8.60115e-10,-4.9723e-14,1679.68,-41.616], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (49.509,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (274.378,'J/mol/K'),
    ),
    shortDesc = """4/ 1/96 THERM""",
    longDesc = 
"""
4/ 1/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 253,
    label = "C5H9O2-4",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {6,D} {15,S}
6  C u0 p0 c0 {4,S} {5,D} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.66449,0.0651525,-4.57159e-05,1.55904e-08,-2.04144e-12,410.326,38.4891], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[18.6105,0.01871,-6.31628e-06,9.73434e-10,-5.62316e-14,-6595.76,-70.5163], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-0.142718,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (345.051,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 254,
    label = "C3H5OH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {8,S} {9,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.08899,0.0328482,-1.91323e-05,5.21635e-09,-4.82395e-13,-16628.2,22.2755], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[10.2818,0.0134248,-4.47039e-06,6.81924e-10,-3.909e-14,-19996,-27.7737], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-140.125,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """9/ 8/95 THERM""",
    longDesc = 
"""
9/ 8/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 255,
    label = "C6H13O-1",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {7,S}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {1,S} {5,S} {19,S} {20,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.275164,0.075432,-4.89209e-05,1.64641e-08,-2.29329e-12,-14928.3,33.1092], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[20.4847,0.0293217,-1.0027e-05,1.55645e-09,-9.02887e-14,-22431.3,-79.3221], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-125.867,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCC[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 256,
    label = "C5H11O-3",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.494528,0.067315,-4.72325e-05,1.75937e-08,-2.73652e-12,-14237.2,30.9476], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[17.8183,0.0244542,-8.36506e-06,1.29863e-09,-7.53357e-14,-20635.1,-67.451], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-120.646,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC([O])CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 257,
    label = "C7H15O-2",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {6,S}
2  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {4,S} {8,S} {17,S}
7  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {21,S} {22,S} {23,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.09088,0.0923217,-6.44478e-05,2.36808e-08,-3.61068e-12,-19992.7,37.7738], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[24.3071,0.0331268,-1.13034e-05,1.75199e-09,-1.01527e-13,-28862.3,-98.7361], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-168.13,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (532.126,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCC(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 258,
    label = "C2H5CHCO",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {1,D} {4,D}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.276601,0.0482967,-4.02377e-05,1.76564e-08,-3.14365e-12,-14171.7,24.7119], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[13.4101,0.0138767,-4.7413e-06,7.35504e-10,-4.26458e-14,-18379.1,-44.5295], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-120.066,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """9/27/95 THERM""",
    longDesc = 
"""
9/27/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 259,
    label = "C5H81-4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.64766,0.055419,-4.12156e-05,1.62877e-08,-2.66483e-12,11149.4,34.8094], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[13.5352,0.0185171,-6.26985e-06,9.66983e-10,-5.58485e-14,6001.19,-46.2553], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (88.4101,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (299.321,'J/mol/K'),
    ),
    shortDesc = """3/ 4/ 8 THERM""",
    longDesc = 
"""
3/ 4/ 8 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 260,
    label = "HO2CH2OCHO",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u0 p2 c0 {2,S} {10,S}
4  O u0 p2 c0 {6,D}
5  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {4,D} {9,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47936,0.0402952,-3.30109e-05,1.3436e-08,-2.18602e-12,-58063,15.2521], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[16.4584,0.00852684,-3.04113e-06,4.85597e-10,-2.87316e-14,-62396,-53.8924], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-482.357,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (216.176,'J/mol/K'),
    ),
    shortDesc = """8/31/99 THERM""",
    longDesc = 
"""
8/31/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=COCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 261,
    label = "TC4H9O2H",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {16,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.114506,0.0671508,-5.15578e-05,2.10256e-08,-3.56467e-12,-31792.9,24.0011], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[19.1617,0.0209157,-7.27347e-06,1.14181e-09,-6.67577e-14,-38320.2,-77.8231], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-266.029,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (361.68,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 262,
    label = "C4H6CHO1-43",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {6,S} {10,S}
5  C u0 p0 c0 {1,D} {2,S} {11,S}
6  C u1 p0 c0 {4,S} {12,S} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.13728,0.0485677,-3.21396e-05,1.08715e-08,-1.51624e-12,2440.81,23.6917], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[15.4179,0.0171673,-5.95215e-06,9.32713e-10,-5.44705e-14,-2759.58,-53.7765], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (18.9736,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """5/ 6/96 THRM""",
    longDesc = 
"""
5/ 6/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=CCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 263,
    label = "C4H7CO1-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  C u1 p0 c0 {1,D} {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09347,0.0459484,-3.00651e-05,9.99306e-09,-1.3471e-12,3966.59,21.4211], Tmin=(298,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[15.4637,0.0164159,-5.54672e-06,8.55055e-10,-4.93929e-14,-855.859,-51.0066], Tmin=(1378,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (32.5967,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """5/ 6/96 THERM""",
    longDesc = 
"""
5/ 6/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 264,
    label = "C4H6CHO1-44",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {6,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {9,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {4,D} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.750038,0.0514806,-3.71071e-05,1.4001e-08,-2.19007e-12,5635.43,25.9488], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[15.4722,0.0170165,-5.87513e-06,9.17941e-10,-5.34945e-14,499.122,-53.1446], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (45.3545,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (299.321,'J/mol/K'),
    ),
    shortDesc = """5/ 6/96 THRM""",
    longDesc = 
"""
5/ 6/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC=C[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 265,
    label = "C6H111O2H-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {20,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {18,S} {19,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.671334,0.0872726,-6.78106e-05,2.77978e-08,-4.70537e-12,-20037.3,35.769], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[24.1598,0.0264142,-9.16605e-06,1.4369e-09,-8.39294e-14,-28453.9,-96.7105], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-168.333,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 266,
    label = "C6H113O2H-1",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {20,S}
3  C u0 p0 c0 {5,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {6,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {8,D} {18,S}
8  C u0 p0 c0 {3,S} {7,D} {19,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.131134,0.081331,-5.80494e-05,2.16451e-08,-3.36478e-12,-19204.2,34.8563], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[23.6309,0.0266617,-9.30223e-06,1.46356e-09,-8.57042e-14,-27627.4,-93.2063], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-161.137,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 267,
    label = "C6H112O2H-6",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {20,S}
3  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
6  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.802061,0.0777041,-5.36127e-05,1.94324e-08,-2.95453e-12,-19541.5,30.3063], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[22.9488,0.0274439,-9.52133e-06,1.49235e-09,-8.71576e-14,-27475.7,-89.32], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-163.201,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 268,
    label = "C5H11O-1",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {6,S}
2  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0902926,0.0634117,-4.09269e-05,1.36983e-08,-1.89646e-12,-12033.4,30.5672], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[17.3225,0.0248218,-8.4816e-06,1.31587e-09,-7.63051e-14,-18335.7,-63.7682], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-102.038,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 269,
    label = "C6H111O2-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {18,S} {19,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.277529,0.078629,-6.01043e-05,2.4849e-08,-4.30167e-12,-1830.63,32.7344], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[21.6615,0.0262499,-9.07089e-06,1.41784e-09,-8.26434e-14,-9150.08,-81.4781], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-16.3642,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC(CC)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 270,
    label = "C6H11O2-4",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {18,S}
7  C u0 p0 c0 {5,S} {6,D} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.97396,0.0778641,-5.51856e-05,1.93459e-08,-2.65554e-12,-2466.99,40.4899], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[21.7536,0.0229478,-7.71428e-06,1.1854e-09,-6.83333e-14,-10629.7,-86.9112], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-23.7449,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (415.724,'J/mol/K'),
    ),
    shortDesc = """3/28/97 THERM""",
    longDesc = 
"""
3/28/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC([O])CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 271,
    label = "C6H113O2-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {5,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {6,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {8,D} {18,S}
8  C u0 p0 c0 {3,S} {7,D} {19,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.8224,0.0644791,-3.94591e-05,1.27102e-08,-1.75877e-12,-1486.17,22.0303], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[20.3168,0.0274248,-9.48325e-06,1.48293e-09,-8.6462e-14,-8099.18,-73.54], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-11.7008,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CCCO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 272,
    label = "HOCH2O2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {7,S}
3 O u1 p2 c0 {1,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.85442,0.0233664,-1.88116e-05,7.9671e-09,-1.36347e-12,-22986.6,15.1731], Tmin=(298,'K'), Tmax=(1412,'K')),
            NASAPolynomial(coeffs=[9.04546,0.00715223,-2.37006e-06,3.60083e-10,-2.0575e-14,-24941.5,-17.4211], Tmin=(1412,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-191.391,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (149.66,'J/mol/K'),
    ),
    shortDesc = """4/ 9/98 THERM""",
    longDesc = 
"""
4/ 9/98 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 273,
    label = "C7H13O2-4",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {2,S} {7,S} {13,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {4,S} {8,D} {21,S}
8  C u0 p0 c0 {6,S} {7,D} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.38155,0.0912476,-6.58712e-05,2.39221e-08,-3.45819e-12,-5230.02,43.9988], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[24.8889,0.0271728,-9.10354e-06,1.39555e-09,-8.03103e-14,-14537.8,-102.122], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-46.5597,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (486.397,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3 THERM""",
    longDesc = 
"""
5/14/ 3 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC([O])CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 274,
    label = "C4H7OOH1-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {14,S}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {12,S} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.79805,0.0523303,-3.64638e-05,1.31972e-08,-1.97166e-12,-13284.7,22.5862], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[16.6978,0.0180578,-6.22477e-06,9.71479e-10,-5.65687e-14,-18534.5,-57.661], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-110.884,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (315.95,'J/mol/K'),
    ),
    shortDesc = """4/1/96 THERM""",
    longDesc = 
"""
4/1/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 275,
    label = "C3H6OOH1-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
5  C u1 p0 c0 {3,S} {4,S} {11,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87775,0.0374167,-2.36058e-05,7.79931e-09,-1.06043e-12,-782.368,19.3941], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[12.4606,0.015889,-5.32742e-06,8.15819e-10,-4.68723e-14,-4203.05,-32.3859], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-6.26587,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (266.063,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 276,
    label = "C7H14OOH2-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {8,S} {9,S} {13,S} {14,S}
7  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
8  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
9  C u1 p0 c0 {5,S} {6,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,33.2997], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.202], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-127.882,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 277,
    label = "C4H8OOH1-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
6  C u1 p0 c0 {1,S} {4,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.36088,0.0446153,-2.14785e-05,3.1462e-09,3.03153e-13,-6899.5,12.4757], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[18.0477,0.0192137,-6.66503e-06,1.04468e-09,-6.10171e-14,-12307,-63.3581], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-56.2643,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """3/27/97 THERM""",
    longDesc = 
"""
3/27/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 278,
    label = "C4H8OOH2-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
6  C u1 p0 c0 {1,S} {3,S} {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.40329,0.0430479,-2.14076e-05,4.28267e-09,-1.27805e-13,-9794.32,13.0514], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[16.3838,0.0204423,-7.04525e-06,1.09928e-09,-6.39967e-14,-14561.6,-53.3147], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-80.0219,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """3/27/97 THERM""",
    longDesc = 
"""
3/27/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[C](C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 279,
    label = "PC2H4COC2H3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,D}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,D} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {6,D} {9,S}
5  C u1 p0 c0 {2,S} {10,S} {11,S}
6  C u0 p0 c0 {4,D} {12,S} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.76254,0.0535806,-4.36465e-05,1.99233e-08,-3.73335e-12,4422.61,26.6605], Tmin=(298,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[12.6733,0.0202366,-6.61089e-06,9.93879e-10,-5.63458e-14,774.011,-35.4544], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (35.2049,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THRM""",
    longDesc = 
"""
2/22/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(=O)C=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 280,
    label = "C5H11O2H-3",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.268431,0.0790976,-5.89751e-05,2.33029e-08,-3.83795e-12,-32833,31.7836], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[22.1712,0.025554,-8.86857e-06,1.39034e-09,-8.12122e-14,-40602.7,-88.4831], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-274.647,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 281,
    label = "C5H11O2H-1",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.474596,0.0738808,-5.12217e-05,1.87797e-08,-2.90292e-12,-30532.4,29.1362], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[21.4181,0.0262251,-9.10691e-06,1.42825e-09,-8.34474e-14,-38040.1,-83.9747], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-255.04,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 282,
    label = "C3H6OOH2-1O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {14,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
7  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.65197,0.0574638,-4.72191e-05,2.05592e-08,-3.68787e-12,-20882.9,20.1548], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.1759,0.0159857,-5.61306e-06,8.8688e-10,-5.20877e-14,-26441.2,-67.7513], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-173.169,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (311.793,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TRM""",
    longDesc = 
"""
7/19/ 0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 283,
    label = "C3H6OOH1-2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {14,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
7  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.65197,0.0574638,-4.72191e-05,2.05592e-08,-3.68787e-12,-20882.9,20.1548], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.1759,0.0159857,-5.61306e-06,8.8688e-10,-5.20877e-14,-26441.2,-67.7513], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-173.169,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (311.793,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TRM""",
    longDesc = 
"""
7/19/ 0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(COO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 284,
    label = "C6H112O2-6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
6  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.83281,0.0685685,-4.50094e-05,1.58889e-08,-2.41749e-12,-1344.26,26.9158], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[20.4744,0.0273033,-9.44419e-06,1.47714e-09,-8.61374e-14,-8199.6,-74.2677], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-11.2654,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCCCO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 285,
    label = "NC3H7COC2H4P",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {1,D} {3,S} {4,S}
7  C u1 p0 c0 {4,S} {17,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.08959,0.0624878,-3.97257e-05,1.33753e-08,-1.92194e-12,-12199.3,23.2035], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[19.2391,0.0251659,-8.57508e-06,1.32847e-09,-7.69775e-14,-18540.5,-70.0617], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-101.406,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (411.566,'J/mol/K'),
    ),
    shortDesc = """2/22/96 TRM""",
    longDesc = 
"""
2/22/96 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(=O)CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 286,
    label = "C6H101-4",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {13,S}
4  C u0 p0 c0 {2,S} {3,D} {14,S}
5  C u0 p0 c0 {1,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.38508,0.0730622,-5.86808e-05,2.52425e-08,-4.4682e-12,4803.85,37.6104], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[17.2274,0.0228969,-7.84177e-06,1.21837e-09,-7.07191e-14,-1649.79,-66.307], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (35.6035,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (369.994,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 287,
    label = "C6H101-5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  C u0 p0 c0 {4,D} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.38508,0.0730622,-5.86808e-05,2.52425e-08,-4.4682e-12,4803.85,37.6104], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[17.2274,0.0228969,-7.84177e-06,1.21837e-09,-7.07191e-14,-1649.79,-66.307], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (35.6035,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (369.994,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCC=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 288,
    label = "SC2H4COC2H3",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {1,S} {3,D} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {12,S} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.160114,0.0557954,-4.31353e-05,1.76457e-08,-2.99384e-12,-31.206,28.3441], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[15.8074,0.0169721,-5.91318e-06,9.29449e-10,-5.43903e-14,-5492.3,-56.9867], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-2.65814,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (299.321,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THRM""",
    longDesc = 
"""
2/22/96 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC([O])=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 289,
    label = "TC3H6OCHO",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {2,D} {3,S} {13,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.37083,0.0538476,-3.82478e-05,1.32882e-08,-1.79229e-12,-21839.1,25.8142], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[17.0371,0.0154401,-5.28333e-06,8.21085e-10,-4.76898e-14,-27587.2,-63.7271], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-183.218,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """8/25/95 THERM""",
    longDesc = 
"""
8/25/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)([O])C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 290,
    label = "CH2CHOOHCOCH3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {14,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {3,D} {4,S} {5,S}
7  C u1 p0 c0 {4,S} {12,S} {13,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.55205,0.0608201,-5.04704e-05,2.16348e-08,-3.75674e-12,-18956.4,27.1012], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[19.3158,0.0156593,-5.45396e-06,8.5716e-10,-5.01583e-14,-24775.2,-67.0297], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-157.918,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (311.793,'J/mol/K'),
    ),
    shortDesc = """6/27/95""",
    longDesc = 
"""
6/27/95
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(OO)C(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 291,
    label = "C6H13O2H-1",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {22,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
7  C u0 p0 c0 {1,S} {5,S} {17,S} {18,S}
8  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.428827,0.0852153,-5.8155e-05,2.08799e-08,-3.15227e-12,-33446.4,31.0485], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[24.5609,0.0307471,-1.06612e-05,1.67032e-09,-9.75224e-14,-42130.6,-99.4218], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-278.954,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (503.026,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 292,
    label = "IC3H5CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  C u1 p0 c0 {1,D} {3,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.85097,0.0418856,-3.62554e-05,1.65691e-08,-3.05851e-12,170.381,15.3014], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[13.0667,0.0116704,-3.99107e-06,6.19498e-10,-3.59348e-14,-3365.19,-43.5803], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (0.700816,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """4/ 3/ 0 THERM""",
    longDesc = 
"""
4/ 3/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 293,
    label = "C4H8OOH1-2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {7,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {9,S}
6  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22401,0.0704995,-5.66979e-05,2.42628e-08,-4.29715e-12,-23739.1,23.8372], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.3244,0.0205475,-7.19076e-06,1.13362e-09,-6.64744e-14,-30546.8,-83.2666], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-196.914,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (382.466,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TRM""",
    longDesc = 
"""
7/19/ 0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(COO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 294,
    label = "C3H51-2,3OOH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {3,S} {6,S}
3  O u0 p2 c0 {2,S} {13,S}
4  O u0 p2 c0 {1,S} {14,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
7  C u1 p0 c0 {5,S} {11,S} {12,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5562,0.0613504,-5.23205e-05,2.28208e-08,-4.02232e-12,-13135.3,22.1044], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[21.2378,0.013952,-4.94539e-06,7.86381e-10,-4.63926e-14,-19286.5,-76.9637], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-108.708,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (307.635,'J/mol/K'),
    ),
    shortDesc = """8/26/3 THRM""",
    longDesc = 
"""
8/26/3 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(COO)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 295,
    label = "C3H52-1,3OOH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {13,S}
4  O u0 p2 c0 {2,S} {14,S}
5  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
7  C u1 p0 c0 {5,S} {6,S} {12,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12254,0.0519554,-3.83734e-05,1.45852e-08,-2.29821e-12,-12275.9,14.8367], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[20.2818,0.0148155,-5.25503e-06,8.35963e-10,-4.93309e-14,-18008.5,-72.2688], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-100.844,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (307.635,'J/mol/K'),
    ),
    shortDesc = """8/26/3 THRM""",
    longDesc = 
"""
8/26/3 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OOC[CH]COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 296,
    label = "C4H8OOH2-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
8  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22401,0.0704995,-5.66979e-05,2.42628e-08,-4.29715e-12,-23739.1,23.8372], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.3244,0.0205475,-7.19076e-06,1.13362e-09,-6.64744e-14,-30546.8,-83.2666], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-196.914,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (382.466,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TRM""",
    longDesc = 
"""
7/19/ 0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 297,
    label = "C4H8OOH1-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {7,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
8  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22401,0.0704995,-5.66979e-05,2.42628e-08,-4.29715e-12,-23739.1,23.8372], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.3244,0.0205475,-7.19076e-06,1.13362e-09,-6.64744e-14,-30546.8,-83.2666], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-196.914,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (382.466,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TRM""",
    longDesc = 
"""
7/19/ 0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCOO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 298,
    label = "C3KET21",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {12,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {3,D} {4,S} {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.55686,0.0357077,-1.94712e-05,4.70695e-09,-3.69754e-13,-38671.1,9.97762], Tmin=(298,'K'), Tmax=(1371,'K')),
            NASAPolynomial(coeffs=[15.6378,0.0144059,-5.08808e-06,8.07076e-10,-4.75296e-14,-43065.8,-51.3106], Tmin=(1371,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-320.566,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (266.063,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species CH3COCH2O2H (i.e. same molecular structure according to RMG)
CC(=O)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 299,
    label = "C4H8OOH1-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {7,S}
2  O u0 p2 c0 {4,S} {8,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
7  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
8  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12352,0.0646726,-4.78358e-05,1.89657e-08,-3.18026e-12,-21466.4,20.4322], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[21.7116,0.0211216,-7.40101e-06,1.16773e-09,-6.8514e-14,-28048.3,-79.5885], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-177.521,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (382.466,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TRM""",
    longDesc = 
"""
7/19/ 0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 300,
    label = "C3H6COC2H5-3",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {7,S}
2  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {7,D} {18,S}
7  C u0 p0 c0 {1,S} {3,S} {6,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.82383,0.0674627,-4.57147e-05,1.66708e-08,-2.60417e-12,-16626.4,26.2565], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.341,0.0256927,-8.88366e-06,1.38917e-09,-8.09982e-14,-23341.6,-73.9481], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-139.257,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (415.724,'J/mol/K'),
    ),
    shortDesc = """2/22/96 TRM""",
    longDesc = 
"""
2/22/96 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=C([O])CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 301,
    label = "C4H8OOH1-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
6  C u1 p0 c0 {3,S} {5,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.94106,0.0518789,-3.10412e-05,8.63569e-09,-8.42842e-13,-4343.16,24.023], Tmin=(298,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[17.6442,0.0191707,-6.57169e-06,1.02247e-09,-5.94305e-14,-10185.9,-61.7116], Tmin=(1377,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-36.6486,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 302,
    label = "C4H8OOH1-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
6  C u1 p0 c0 {4,S} {13,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.45017,0.0572419,-4.06431e-05,1.52822e-08,-2.42123e-12,-3029.06,25.0738], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[17.8624,0.0195213,-6.80351e-06,1.06961e-09,-6.26001e-14,-8879.23,-63.4393], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-25.9397,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 303,
    label = "C4H8OOH1-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
6  C u1 p0 c0 {3,S} {4,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.51698,0.0544584,-3.84524e-05,1.48146e-08,-2.42809e-12,-3497.28,26.4917], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[15.8328,0.020722,-7.09869e-06,1.10302e-09,-6.40252e-14,-8530.34,-50.44], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-29.7642,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 304,
    label = "C3KET12",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {12,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {3,D} {4,S} {11,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.10507,0.0527397,-4.31806e-05,1.81618e-08,-3.10536e-12,-36362.8,25.4112], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[17.0756,0.0131013,-4.61949e-06,7.31991e-10,-4.30789e-14,-41700.9,-59.5779], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-303.449,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (266.063,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 305,
    label = "C4H8OOH2-1O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
6  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22401,0.0704995,-5.66979e-05,2.42628e-08,-4.29715e-12,-23739.1,23.8372], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.3244,0.0205475,-7.19076e-06,1.13362e-09,-6.64744e-14,-30546.8,-83.2666], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-196.914,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (382.466,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TRM""",
    longDesc = 
"""
7/19/ 0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 306,
    label = "C4H7CO1-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  C u1 p0 c0 {1,D} {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.46143,0.056294,-4.61644e-05,2.00772e-08,-3.57227e-12,-3301.51,24.9395], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[15.9313,0.0165162,-5.67719e-06,8.84328e-10,-5.1425e-14,-8363.67,-56.9426], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-29.13,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THERM""",
    longDesc = 
"""
2/22/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=C[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 307,
    label = "C4H7O",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.60619,0.0558563,-4.35596e-05,1.70589e-08,-2.65635e-12,4850.9,34.7113], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[15.3138,0.0143427,-4.81626e-06,7.39575e-10,-4.26141e-14,-729.343,-55.2938], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (36.1667,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (274.378,'J/mol/K'),
    ),
    shortDesc = """4/ 3/ 0 THERM""",
    longDesc = 
"""
4/ 3/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 308,
    label = "C7H13O3-5",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {13,S}
4  C u0 p0 c0 {6,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {4,S} {8,D} {20,S}
8  C u0 p0 c0 {3,S} {7,D} {21,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.04765,0.0994962,-7.94283e-05,3.2692e-08,-5.42562e-12,-5016.66,51.7525], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[24.6614,0.0271532,-9.04971e-06,1.38224e-09,-7.93365e-14,-14367,-100.41], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-46.5677,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (486.397,'J/mol/K'),
    ),
    shortDesc = """3/28/97 THERM""",
    longDesc = 
"""
3/28/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CC([O])CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 309,
    label = "C4H8OOH2-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  C u1 p0 c0 {3,S} {13,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.01712,0.0610561,-4.65789e-05,1.88024e-08,-3.15266e-12,-5373.91,26.306], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[18.4556,0.0189544,-6.59381e-06,1.03538e-09,-6.05467e-14,-11363.7,-66.9839], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-45.6438,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 310,
    label = "C4H7CHO1-1",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  C u0 p0 c0 {1,D} {5,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.896311,0.061664,-4.81456e-05,1.98018e-08,-3.3501e-12,-18668.5,31.8639], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[16.5148,0.0186176,-6.41424e-06,1.00074e-09,-5.82623e-14,-24513.3,-60.8627], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-158.202,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """2/22/96 THERM""",
    longDesc = 
"""
2/22/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 311,
    label = "C7H14OOH3-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {10,S}
4  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {8,S} {9,S} {13,S} {14,S}
7  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
8  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
9  C u1 p0 c0 {5,S} {6,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,33.2997], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.202], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-127.882,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 312,
    label = "C6H102-4",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,D} {13,S}
4  C u0 p0 c0 {2,S} {6,D} {14,S}
5  C u0 p0 c0 {3,D} {6,S} {15,S}
6  C u0 p0 c0 {4,D} {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.38508,0.0730622,-5.86808e-05,2.52425e-08,-4.4682e-12,4803.85,37.6104], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[17.2274,0.0228969,-7.84177e-06,1.21837e-09,-7.07191e-14,-1649.79,-66.307], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (35.6035,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (369.994,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC=CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 313,
    label = "C6H13O2H-3",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {22,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
8  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.438854,0.0910056,-6.66797e-05,2.58473e-08,-4.18106e-12,-35729.4,33.5762], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[25.3704,0.0300456,-1.04163e-05,1.63181e-09,-9.52693e-14,-44722.2,-104.961], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-298.498,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (503.026,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 314,
    label = "C7H15O2H-2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {25,S}
3  C u0 p0 c0 {1,S} {4,S} {8,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {5,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {3,S} {22,S} {23,S} {24,S}
9  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.602101,0.102885,-7.43423e-05,2.83646e-08,-4.51796e-12,-38626.9,36.7138], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.5706,0.0345345,-1.19627e-05,1.87305e-09,-1.09312e-13,-48841.5,-120.064], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-322.361,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (573.699,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 315,
    label = "C7H15O-1",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {8,S}
2  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {8,S} {17,S} {18,S}
7  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
8  C u0 p0 c0 {1,S} {6,S} {22,S} {23,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.45919,0.0874465,-5.69015e-05,1.92196e-08,-2.68753e-12,-17823.3,35.6475], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[23.649,0.0338196,-1.15718e-05,1.79692e-09,-1.04266e-13,-26528,-94.8882], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-149.71,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (532.126,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCCC[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 316,
    label = "C7H15O2H-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {25,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {17,S} {18,S}
8  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
9  C u0 p0 c0 {7,S} {22,S} {23,S} {24,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.602101,0.102885,-7.43423e-05,2.83646e-08,-4.51796e-12,-38626.9,36.0243], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.5706,0.0345345,-1.19627e-05,1.87305e-09,-1.09312e-13,-48841.5,-120.754], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-322.361,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (573.699,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CCC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 317,
    label = "C6H101OOH5-6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
5  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {8,D} {14,S}
7  C u1 p0 c0 {4,S} {15,S} {16,S}
8  C u0 p0 c0 {6,D} {17,S} {18,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.132873,0.0825962,-6.51873e-05,2.70764e-08,-4.62922e-12,4569.8,34.1909], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[23.7355,0.0242568,-8.42851e-06,1.32246e-09,-7.72936e-14,-3378.82,-91.5558], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (36.931,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(CCC=C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 318,
    label = "C6H102OOH5-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
6  C u1 p0 c0 {3,S} {8,S} {16,S}
7  C u0 p0 c0 {5,S} {8,D} {17,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.402203,0.0818779,-6.1907e-05,2.45653e-08,-4.03514e-12,-4544.2,33.2729], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[23.2753,0.0251409,-8.74931e-06,1.37423e-09,-8.03787e-14,-12693.3,-93.501], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-39.503,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C[CH]C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 319,
    label = "C6H101OOH4-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  C u1 p0 c0 {3,S} {7,S} {15,S}
7  C u0 p0 c0 {6,S} {8,D} {16,S}
8  C u0 p0 c0 {7,D} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.910298,0.0852583,-6.69193e-05,2.7497e-08,-4.64326e-12,-3024.69,35.7766], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[23.7244,0.0247402,-8.60684e-06,1.35156e-09,-7.90411e-14,-11341.3,-95.5723], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-27.2174,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C[CH]C(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 320,
    label = "C6H101OOH4-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
6  C u1 p0 c0 {3,S} {5,S} {15,S}
7  C u0 p0 c0 {4,S} {8,D} {16,S}
8  C u0 p0 c0 {7,D} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.631714,0.0774647,-5.64803e-05,2.12731e-08,-3.28311e-12,3249.1,33.0551], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[23.2488,0.0242528,-8.33845e-06,1.29945e-09,-7.56012e-14,-4568.43,-88.2821], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (26.3337,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC([CH]C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 321,
    label = "C6H103OOH1-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {3,S} {8,D} {17,S}
7  C u1 p0 c0 {4,S} {8,S} {16,S}
8  C u0 p0 c0 {6,D} {7,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.54281,0.0716314,-4.71542e-05,1.59384e-08,-2.23271e-12,-2668.22,25.4749], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[22.3753,0.0259192,-9.02065e-06,1.41687e-09,-8.2872e-14,-10281.4,-87.597], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-22.6019,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=C[CH]COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 322,
    label = "C6H102OOH5-6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {7,D} {15,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  C u1 p0 c0 {3,S} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.703138,0.0789566,-5.98556e-05,2.39725e-08,-3.98633e-12,3039.57,32.0891], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[23.2562,0.0246734,-8.57419e-06,1.34539e-09,-7.86366e-14,-4714.95,-88.6067], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (24.5994,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(CC=CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 323,
    label = "C6H101OOH5-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
4  C u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  C u1 p0 c0 {3,S} {4,S} {15,S}
7  C u0 p0 c0 {4,S} {8,D} {16,S}
8  C u0 p0 c0 {7,D} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.631714,0.0774647,-5.64803e-05,2.12731e-08,-3.28311e-12,3249.1,33.0551], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[23.2488,0.0242528,-8.33845e-06,1.29945e-09,-7.56012e-14,-4568.43,-88.2821], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (26.3337,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC[CH]C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 324,
    label = "C6H102OOH6-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {6,S} {7,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {8,S} {13,S} {14,S} {15,S}
6  C u1 p0 c0 {3,S} {4,S} {16,S}
7  C u0 p0 c0 {3,S} {8,D} {18,S}
8  C u0 p0 c0 {5,S} {7,D} {17,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.64692,0.0694745,-4.35534e-05,1.30171e-08,-1.44135e-12,3821.06,29.7878], Tmin=(298,'K'), Tmax=(1375,'K')),
            NASAPolynomial(coeffs=[22.8662,0.0240568,-8.17268e-06,1.26465e-09,-7.32522e-14,-3922.85,-85.5823], Tmin=(1375,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (31.4005,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC[CH]COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 325,
    label = "C4H6CHO1-13",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  C u0 p0 c0 {4,S} {6,D} {12,S}
6  C u0 p0 c0 {1,S} {5,D} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.868106,0.0581156,-4.44076e-05,1.74859e-08,-2.82132e-12,-1688.32,30.697], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[16.5958,0.0164088,-5.74433e-06,9.05905e-10,-5.31381e-14,-7683.24,-62.8092], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-17.0992,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (299.321,'J/mol/K'),
    ),
    shortDesc = """2/22/96 TRM""",
    longDesc = 
"""
2/22/96 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC=C[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 326,
    label = "C4H6CHO1-14",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {6,S} {10,S}
5  C u1 p0 c0 {2,S} {11,S} {12,S}
6  C u0 p0 c0 {1,D} {4,S} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0937898,0.0569789,-4.55153e-05,1.9103e-08,-3.28541e-12,5938.86,30.2936], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[16.0679,0.0165206,-5.7063e-06,8.91819e-10,-5.19829e-14,561.659,-55.6047], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (47.127,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """2/22/96 TRM""",
    longDesc = 
"""
2/22/96 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC=CC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 327,
    label = "C6H101OOH4-6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {8,D} {14,S}
7  C u1 p0 c0 {5,S} {15,S} {16,S}
8  C u0 p0 c0 {6,D} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.132873,0.0825962,-6.51873e-05,2.70764e-08,-4.62922e-12,4568.6,34.1909], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[23.7355,0.0242568,-8.42851e-06,1.32246e-09,-7.72936e-14,-3380.02,-91.5558], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (36.921,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(CC=C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 328,
    label = "AC3H5OOH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {5,D} {8,S}
5  C u0 p0 c0 {4,D} {9,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.43935,0.0402071,-2.95323e-05,1.14716e-08,-1.85171e-12,-9436.8,17.055], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[13.6838,0.0133968,-4.61534e-06,7.19989e-10,-4.1911e-14,-13316.5,-43.1904], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-78.6489,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (245.277,'J/mol/K'),
    ),
    shortDesc = """7/20/98 THERM""",
    longDesc = 
"""
7/20/98 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 329,
    label = "C6H101OOH4-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {2,S} {5,S} {8,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
8  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.29385,0.0953423,-8.12998e-05,3.63927e-08,-6.62213e-12,-14698.5,30.832], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[28.2643,0.0252451,-8.80644e-06,1.38537e-09,-8.11177e-14,-23483.9,-111.717], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-121.684,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC(OO)C(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 330,
    label = "NC4KET14",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {15,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
7  C u0 p0 c0 {3,D} {5,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40797,0.0537386,-3.72613e-05,1.36863e-08,-2.13799e-12,-37791.9,16.558], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[19.0284,0.0186605,-6.53616e-06,1.03102e-09,-6.04833e-14,-43467.9,-68.021], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-313.384,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 331,
    label = "C3H6OOH1-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {12,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u1 p0 c0 {3,S} {10,S} {11,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.88331,0.0440156,-3.07858e-05,1.13215e-08,-1.75323e-12,-168.779,21.4041], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[14.6882,0.0149941,-5.24057e-06,8.25463e-10,-4.83759e-14,-4773.43,-47.7984], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-2.1654,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (266.063,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 332,
    label = "C4H8OOH2-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u1 p0 c0 {4,S} {13,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.01712,0.0610561,-4.65789e-05,1.88024e-08,-3.15266e-12,-5373.91,26.306], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[18.4556,0.0189544,-6.59381e-06,1.03538e-09,-6.05467e-14,-11363.7,-66.9839], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-45.6438,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 333,
    label = "C6H101OOH6-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
6  C u1 p0 c0 {3,S} {5,S} {15,S}
7  C u0 p0 c0 {4,S} {8,D} {16,S}
8  C u0 p0 c0 {7,D} {17,S} {18,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.12489,0.0730056,-4.89258e-05,1.62744e-08,-2.13928e-12,5341.82,32.3393], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[23.1648,0.0239157,-8.14393e-06,1.26187e-09,-7.31482e-14,-2512.31,-86.8163], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (43.9023,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC[CH]COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 334,
    label = "C6H101OOH5-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {7,D} {15,S}
7  C u0 p0 c0 {6,D} {8,S} {16,S}
8  C u1 p0 c0 {7,S} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.910298,0.0852583,-6.69193e-05,2.7497e-08,-4.64326e-12,-3024.69,35.7766], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[23.7244,0.0247402,-8.60684e-06,1.35156e-09,-7.90411e-14,-11341.3,-95.5723], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-27.2174,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=CCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 335,
    label = "C6H101OOH6-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {7,D} {15,S}
7  C u0 p0 c0 {6,D} {8,S} {16,S}
8  C u1 p0 c0 {7,S} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.000608388,0.0793277,-5.80291e-05,2.22216e-08,-3.53369e-12,-1001.99,33.0696], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[23.007,0.0253677,-8.8273e-06,1.38638e-09,-8.10849e-14,-9038.82,-90.5352], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-9.77832,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=CCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 336,
    label = "C5H10OOH1-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {18,S}
3  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
7  C u1 p0 c0 {4,S} {5,S} {17,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.66305,0.0642512,-3.94125e-05,1.15348e-08,-1.25128e-12,-7222.88,27.0064], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[20.9225,0.0234863,-8.03644e-06,1.24881e-09,-7.25228e-14,-14324.6,-77.9153], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-60.4527,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THRM""",
    longDesc = 
"""
7/19/ 0 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 337,
    label = "C5H10OOH3-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {18,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
7  C u1 p0 c0 {3,S} {6,S} {17,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.27092,0.0682959,-4.63421e-05,1.61404e-08,-2.30884e-12,-9583.4,27.9668], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[21.0899,0.0237168,-8.19006e-06,1.27986e-09,-7.45974e-14,-16670.2,-79.1384], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-80.1779,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THRM""",
    longDesc = 
"""
7/19/ 0 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 338,
    label = "CHCHCHO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,D} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 C u1 p0 c0 {2,D} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.20905,0.0319125,-2.93444e-05,1.38077e-08,-2.58328e-12,17971.2,19.399], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[10.2666,0.00709613,-2.47273e-06,3.8874e-10,-2.27523e-14,15165.4,-27.9927], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (147.509,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """5/14/ 3""",
    longDesc = 
"""
5/14/ 3
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 339,
    label = "C7H14OOH2-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {7,S} {9,S} {12,S}
6  C u0 p0 c0 {1,S} {8,S} {10,S} {13,S}
7  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {7,S} {18,S} {19,S}
9  C u0 p0 c0 {5,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {6,S} {23,S} {24,S} {25,S}
11 C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-286.91,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CCC(C)OO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 340,
    label = "C6H101OOH6-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {8,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {8,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {6,S} {9,S} {14,S} {15,S}
8  C u0 p0 c0 {1,S} {5,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.04641,0.0898933,-7.28891e-05,3.13362e-08,-5.55187e-12,-12646.6,28.8961], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.5912,0.0258613,-9.02901e-06,1.42117e-09,-8.32457e-14,-21220.5,-106.984], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-104.188,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCC(COO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 341,
    label = "C6H101OOH4-6O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {8,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {5,S} {8,S} {12,S} {13,S}
7  C u0 p0 c0 {5,S} {9,S} {14,S} {15,S}
8  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.04641,0.0898933,-7.28891e-05,3.13362e-08,-5.55187e-12,-12646.6,28.8961], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.5912,0.0258613,-9.02901e-06,1.42117e-09,-8.32457e-14,-21220.5,-106.984], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-104.188,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC(CCO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 342,
    label = "C7H14OOH3-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {7,S} {9,S} {13,S}
6  C u0 p0 c0 {2,S} {7,S} {8,S} {12,S}
7  C u0 p0 c0 {5,S} {6,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {10,S} {14,S} {15,S}
9  C u0 p0 c0 {5,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {20,S} {21,S} {22,S}
11 C u0 p0 c0 {9,S} {23,S} {24,S} {25,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-286.91,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CC(CC)OO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 343,
    label = "C6H102OOH5-6O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {5,S} {9,S} {12,S} {13,S}
7  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
8  C u0 p0 c0 {10,S} {16,S} {17,S} {18,S}
9  C u0 p0 c0 {6,S} {10,D} {20,S}
10 C u0 p0 c0 {8,S} {9,D} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61044,0.0862028,-6.74604e-05,2.81731e-08,-4.89694e-12,-14172.2,26.1484], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[27.095,0.0262942,-9.18082e-06,1.44512e-09,-8.46498e-14,-22553.5,-104.64], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-116.54,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCC(CO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 344,
    label = "C5H10OOH1-2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {8,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {20,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
6  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
7  C u0 p0 c0 {6,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
9  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53073,0.0812167,-6.33055e-05,2.63901e-08,-4.5874e-12,-26733.8,23.9105], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[25.5479,0.0250385,-8.74244e-06,1.37611e-09,-8.06073e-14,-34634.5,-99.1022], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-221.22,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (453.139,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TM""",
    longDesc = 
"""
7/19/ 0 TM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(COO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 345,
    label = "C5H10OOH3-2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {20,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
6  C u0 p0 c0 {2,S} {5,S} {8,S} {11,S}
7  C u0 p0 c0 {5,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
9  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.08935,0.0857157,-7.04987e-05,3.07497e-08,-5.51133e-12,-29097,25.0298], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[26.285,0.0243678,-8.50102e-06,1.33737e-09,-7.83075e-14,-37153.7,-103.435], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-241.026,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (453.139,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TM""",
    longDesc = 
"""
7/19/ 0 TM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(OO)C(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 346,
    label = "C6H12OOH3-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {12,S}
6  C u0 p0 c0 {2,S} {5,S} {7,S} {11,S}
7  C u0 p0 c0 {6,S} {9,S} {13,S} {14,S}
8  C u0 p0 c0 {5,S} {10,S} {15,S} {16,S}
9  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {20,S} {21,S} {22,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.71726,0.0983623,-7.90355e-05,3.37038e-08,-5.93018e-12,-31959.5,28.4742], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[29.5549,0.028827,-1.00438e-05,1.57872e-09,-9.23849e-14,-41318.6,-119.673], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-264.788,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(O[O])C(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 347,
    label = "C6H102OOH6-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {7,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {5,S} {9,S} {12,S} {13,S}
7  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
8  C u0 p0 c0 {10,S} {16,S} {17,S} {18,S}
9  C u0 p0 c0 {6,S} {10,D} {20,S}
10 C u0 p0 c0 {8,S} {9,D} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61044,0.0862028,-6.74604e-05,2.81731e-08,-4.89694e-12,-14172.2,26.1484], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[27.095,0.0262942,-9.18082e-06,1.44512e-09,-8.46498e-14,-22553.5,-104.64], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-116.54,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCC(COO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 348,
    label = "C6H101OOH5-6O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {8,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {6,S} {9,S} {14,S} {15,S}
8  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.04641,0.0898933,-7.28891e-05,3.13362e-08,-5.55187e-12,-12646.6,28.8961], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.5912,0.0258613,-9.02901e-06,1.42117e-09,-8.32457e-14,-21220.5,-106.984], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-104.188,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCC(CO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 349,
    label = "C6H101OOH3-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
4  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  C u1 p0 c0 {3,S} {4,S} {15,S}
7  C u0 p0 c0 {3,S} {8,D} {16,S}
8  C u0 p0 c0 {7,D} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0952498,0.0803618,-6.06668e-05,2.37468e-08,-3.80815e-12,3831.05,35.1713], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[23.5865,0.0239558,-8.23516e-06,1.28335e-09,-7.46678e-14,-4178.39,-90.4585], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (30.7664,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC([CH]CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 350,
    label = "VTHF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {7,D} {15,S}
7  C u0 p0 c0 {6,D} {16,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.96655,0.0890554,-7.35045e-05,3.14932e-08,-5.45547e-12,-7322.33,55.5447], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[19.1885,0.0242678,-8.33135e-06,1.29674e-09,-7.53674e-14,-15445.6,-77.3983], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-69.1105,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (403.252,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC1CCCO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 351,
    label = "C6H111O2-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
5  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {4,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {18,S} {19,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.172342,0.0796366,-6.17326e-05,2.58869e-08,-4.53504e-12,-1313.17,32.8552], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[21.8247,0.0261477,-9.04382e-06,1.41447e-09,-8.24824e-14,-8686.2,-82.6422], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-12.1427,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(CCC)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 352,
    label = "ETES1",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
5  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {7,D} {17,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.96655,0.0890554,-7.35045e-05,3.14932e-08,-5.45547e-12,-7322.33,55.5447], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[19.1885,0.0242678,-8.33135e-06,1.29674e-09,-7.53674e-14,-15445.6,-77.3983], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-69.1114,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (394.937,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCC1CO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 353,
    label = "C6H102OOH6-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
5  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
6  C u1 p0 c0 {3,S} {8,S} {16,S}
7  C u0 p0 c0 {5,S} {8,D} {17,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.546105,0.0755507,-5.20173e-05,1.83935e-08,-2.69131e-12,-2522.56,30.4271], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[23.0774,0.0250917,-8.77976e-06,1.38405e-09,-8.11587e-14,-10636.3,-91.4736], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-22.1086,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C[CH]CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 354,
    label = "C5H10OOH2-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {18,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
7  C u1 p0 c0 {4,S} {6,S} {17,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.27092,0.0682959,-4.63421e-05,1.61404e-08,-2.30884e-12,-9583.4,27.9668], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[21.0899,0.0237168,-8.19006e-06,1.27986e-09,-7.45974e-14,-16670.2,-79.1384], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-80.1779,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THRM""",
    longDesc = 
"""
7/19/ 0 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 355,
    label = "C6H101OOH5-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {1,S} {5,S} {8,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
8  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.29385,0.0953423,-8.12998e-05,3.63927e-08,-6.62213e-12,-14698.5,30.832], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[28.2643,0.0252451,-8.80644e-06,1.38537e-09,-8.11177e-14,-23483.9,-111.717], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-121.684,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC(O[O])C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 356,
    label = "C6H101OOH3-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {1,S} {5,S} {9,S} {12,S}
7  C u0 p0 c0 {5,S} {8,S} {13,S} {14,S}
8  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
9  C u0 p0 c0 {6,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0223,0.097229,-8.42573e-05,3.825e-08,-7.03511e-12,-14160.3,31.6908], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.4867,0.0250954,-8.76367e-06,1.37964e-09,-8.08226e-14,-23041.2,-113.219], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-117.415,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(OO)C(CC)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 357,
    label = "C6H112O2-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {8,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {8,D} {18,S}
8  C u0 p0 c0 {6,S} {7,D} {19,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.172342,0.0796366,-6.17326e-05,2.58869e-08,-4.53504e-12,-1313.17,32.8552], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[21.8247,0.0261477,-9.04382e-06,1.41447e-09,-8.24824e-14,-8686.2,-82.6422], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-12.1427,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC=CCO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 358,
    label = "C5H10OOH2-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {20,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {7,S} {9,S} {11,S}
6  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
7  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
9  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.08935,0.0857157,-7.04987e-05,3.07497e-08,-5.51133e-12,-29097,25.0298], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[26.285,0.0243678,-8.50102e-06,1.33737e-09,-7.83075e-14,-37153.7,-103.435], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-241.026,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (453.139,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TM""",
    longDesc = 
"""
7/19/ 0 TM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CC(C)OO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 359,
    label = "SC3H5CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u1 p0 c0 {1,D} {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74191,0.039723,-3.20062e-05,1.38228e-08,-2.46272e-12,-664.428,17.0762], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[12.5515,0.0122522,-4.22382e-06,6.59185e-10,-3.83819e-14,-4253.5,-40.2864], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-6.47373,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """11/15/95 THERM""",
    longDesc = 
"""
11/15/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C[C]=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 360,
    label = "C6H101OOH3-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
6  C u1 p0 c0 {4,S} {5,S} {15,S}
7  C u0 p0 c0 {3,S} {8,D} {16,S}
8  C u0 p0 c0 {7,D} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0952498,0.0803618,-6.06668e-05,2.37468e-08,-3.80815e-12,3831.05,35.1713], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[23.5865,0.0239558,-8.23516e-06,1.28335e-09,-7.46678e-14,-4178.39,-90.4585], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (30.7664,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(C[CH]C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 361,
    label = "C6H101OOH3-6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {3,S} {8,D} {14,S}
7  C u1 p0 c0 {5,S} {15,S} {16,S}
8  C u0 p0 c0 {6,D} {17,S} {18,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0456628,0.0840204,-6.75655e-05,2.86243e-08,-4.98056e-12,5095.07,34.6344], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[23.8721,0.0241661,-8.40279e-06,1.31902e-09,-7.71171e-14,-2897.06,-92.5485], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (41.1605,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC(C=C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 362,
    label = "C6H101OOH6-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {6,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
6  C u1 p0 c0 {3,S} {4,S} {15,S}
7  C u0 p0 c0 {4,S} {8,D} {16,S}
8  C u0 p0 c0 {7,D} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.12489,0.0730056,-4.89258e-05,1.62744e-08,-2.13928e-12,5341.82,32.3393], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[23.1648,0.0239157,-8.14393e-06,1.26187e-09,-7.31482e-14,-2512.31,-86.8163], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (43.9023,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC[CH]CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 363,
    label = "C6H12OOH1-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {8,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
7  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
8  C u1 p0 c0 {5,S} {6,S} {20,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4674,0.0763927,-4.77257e-05,1.46094e-08,-1.73635e-12,-10117.7,29.5852], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[23.9324,0.0282541,-9.70103e-06,1.51047e-09,-8.78256e-14,-18365.9,-92.6287], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-84.2927,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC[CH]COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 364,
    label = "C6H12OOH2-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {1,S} {7,S} {8,S} {11,S}
4  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
8  C u1 p0 c0 {3,S} {5,S} {20,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.01849,0.0805627,-5.46524e-05,1.90949e-08,-2.74736e-12,-12466.7,30.1432], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[24.2386,0.0282612,-9.75785e-06,1.52463e-09,-8.8853e-14,-20768.1,-95.3255], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-104.007,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 365,
    label = "C6H101OOH3-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {7,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {8,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
7  C u0 p0 c0 {1,S} {6,S} {9,S} {12,S}
8  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0223,0.097229,-8.42573e-05,3.825e-08,-7.03511e-12,-14160.3,31.6908], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.4867,0.0250954,-8.76367e-06,1.37964e-09,-8.08226e-14,-23041.2,-113.219], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-117.415,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(CC(C)O[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 366,
    label = "C6H101OOH3-6O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {8,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {9,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
8  C u0 p0 c0 {2,S} {7,S} {16,S} {17,S}
9  C u0 p0 c0 {5,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.21544,0.0932821,-7.74588e-05,3.39725e-08,-6.10567e-12,-11995.6,32.5594], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.7417,0.0257731,-9.00776e-06,1.41884e-09,-8.31503e-14,-20797.1,-108.181], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-99.439,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(CCCO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 367,
    label = "C6H101OOH6-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {8,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {5,S} {8,S} {12,S} {13,S}
7  C u0 p0 c0 {5,S} {9,S} {14,S} {15,S}
8  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.04641,0.0898933,-7.28891e-05,3.13362e-08,-5.55187e-12,-12646.6,28.8961], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.5912,0.0258613,-9.02901e-06,1.42117e-09,-8.32457e-14,-21220.5,-106.984], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-104.188,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC(CCOO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 368,
    label = "C6H12OOH1-2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {9,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {16,S} {17,S}
7  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
8  C u0 p0 c0 {7,S} {10,S} {12,S} {13,S}
9  C u0 p0 c0 {1,S} {5,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {20,S} {21,S} {22,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19543,0.0938208,-7.19541e-05,2.9485e-08,-5.04752e-12,-29604.6,27.1618], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.7781,0.0295252,-1.02932e-05,1.61855e-09,-9.47402e-14,-38774.4,-115.091], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-245.018,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(COO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 369,
    label = "C6H12OOH2-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {1,S} {5,S} {9,S} {12,S}
7  C u0 p0 c0 {5,S} {8,S} {15,S} {16,S}
8  C u0 p0 c0 {7,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
10 C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.71726,0.0983623,-7.90355e-05,3.37038e-08,-5.93018e-12,-31959.5,28.4742], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[29.5549,0.028827,-1.00438e-05,1.57872e-09,-9.23849e-14,-41318.6,-119.673], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-264.788,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(O[O])C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 370,
    label = "C6H103OOH1-2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {7,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {7,S} {9,S} {11,S}
6  C u0 p0 c0 {8,S} {10,S} {12,S} {13,S}
7  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
8  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
9  C u0 p0 c0 {5,S} {10,D} {20,S}
10 C u0 p0 c0 {6,S} {9,D} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.741773,0.0940159,-7.80996e-05,3.42989e-08,-6.17488e-12,-13176.2,34.7824], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4463,0.0260362,-9.10125e-06,1.43372e-09,-8.40289e-14,-22040.8,-106.907], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-109.704,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CC(COO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 371,
    label = "C7H14OOH1-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {8,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {9,S} {14,S} {15,S}
6  C u0 p0 c0 {7,S} {9,S} {16,S} {17,S}
7  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
8  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
9  C u1 p0 c0 {5,S} {6,S} {23,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.11146,0.0891595,-5.67352e-05,1.7889e-08,-2.2226e-12,-12986.8,32.92], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[27.229,0.0324922,-1.1126e-05,1.72929e-09,-1.00428e-13,-22497.7,-108.902], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-108.045,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC[CH]CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 372,
    label = "C7H14OOH3-6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
9  C u1 p0 c0 {6,S} {8,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,33.2997], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.202], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-127.882,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 373,
    label = "IC3H5O2HCHO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {14,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  C u1 p0 c0 {4,S} {11,S} {12,S}
7  C u0 p0 c0 {3,D} {4,S} {13,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.05985,0.0582332,-4.37672e-05,1.6325e-08,-2.43462e-12,-16349.6,21.3688], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[20.6289,0.0148626,-5.25305e-06,8.33773e-10,-4.91277e-14,-22758.9,-78.2963], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-136.247,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (311.793,'J/mol/K'),
    ),
    shortDesc = """8/2/95 THERM""",
    longDesc = 
"""
8/2/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)(C=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 374,
    label = "C7H14OOH3-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
7  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
9  C u1 p0 c0 {3,S} {8,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,33.2997], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.202], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-127.882,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C(CCCC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 375,
    label = "C7H14OOH3-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {12,S}
4  C u0 p0 c0 {3,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
9  C u1 p0 c0 {3,S} {6,S} {23,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,33.2997], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.202], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-127.882,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]C(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 376,
    label = "C7H14OOH1-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {8,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {9,S} {16,S} {17,S}
7  C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
8  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
9  C u1 p0 c0 {6,S} {7,S} {23,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.11146,0.0891595,-5.67352e-05,1.7889e-08,-2.2226e-12,-12986.8,32.92], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[27.229,0.0324922,-1.1126e-05,1.72929e-09,-1.00428e-13,-22497.7,-108.902], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-108.045,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC[CH]COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 377,
    label = "C7H14OOH2-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {9,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {3,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
9  C u1 p0 c0 {4,S} {6,S} {23,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,33.2997], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.202], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-127.882,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC[CH]C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 378,
    label = "IC4H8O2H-T",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
6  C u1 p0 c0 {3,S} {4,S} {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77633,0.0450889,-2.62424e-05,7.74737e-09,-9.1152e-13,-5982.96,15.3503], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[15.2395,0.0206497,-6.94792e-06,1.06651e-09,-6.13783e-14,-10227.1,-47.0909], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-48.4284,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 379,
    label = "C7H14OOH2-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
7  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
8  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
9  C u1 p0 c0 {6,S} {22,S} {23,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.151527,0.0984303,-7.20555e-05,2.78535e-08,-4.48821e-12,-14012.6,35.3721], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.1418,0.032381,-1.12265e-05,1.75881e-09,-1.02687e-13,-23764.9,-114.883], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-117.104,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(CCCCC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 380,
    label = "C6H12OOH3-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
8  C u1 p0 c0 {3,S} {7,S} {20,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.01849,0.0805627,-5.46524e-05,1.90949e-08,-2.74736e-12,-12466.7,30.1432], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[24.2386,0.0282612,-9.75785e-06,1.52463e-09,-8.8853e-14,-20768.1,-95.3255], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-104.007,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C(CCC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 381,
    label = "C2H4O1-2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.44362,0.0291837,-1.96805e-05,6.67473e-09,-9.02139e-13,-7434.34,29.5212], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[6.99486,0.0100772,-3.45221e-06,5.36571e-10,-3.11564e-14,-10409.1,-15.9858], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-66.5024,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (157.975,'J/mol/K'),
    ),
    shortDesc = """9/ 1/ 0 THERM""",
    longDesc = 
"""
9/ 1/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C1CO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 382,
    label = "C6H12OOH2-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
8  C u1 p0 c0 {5,S} {19,S} {20,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.327958,0.0864936,-6.43068e-05,2.52817e-08,-4.13906e-12,-11117,32.1731], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[24.9425,0.0278897,-9.67889e-06,1.51736e-09,-8.86313e-14,-19645.6,-99.7839], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-93.2385,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(CCCC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 383,
    label = "TC4H8CHO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {2,S} {13,S} {14,S}
6  C u0 p0 c0 {1,D} {2,S} {15,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.958078,0.0642003,-4.70777e-05,1.75738e-08,-2.64896e-12,-6865.83,33.3781], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[17.9664,0.0194207,-6.67409e-06,1.03969e-09,-6.04703e-14,-13336.9,-67.9819], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-59.9035,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (340.893,'J/mol/K'),
    ),
    shortDesc = """9/ 7/95 THERM""",
    longDesc = 
"""
9/ 7/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)(C)C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 384,
    label = "C4H8CHO-4",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {6,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {14,S}
6  C u0 p0 c0 {1,S} {5,D} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.16494,0.0543945,-3.49001e-05,1.14583e-08,-1.54697e-12,-9806.2,23.4897], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[16.597,0.0207197,-7.14969e-06,1.11659e-09,-6.50492e-14,-15453.9,-60.318], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-82.5556,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (345.051,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC=C[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 385,
    label = "C4H8CHO-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u1 p0 c0 {3,S} {13,S} {14,S}
6  C u0 p0 c0 {1,D} {4,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.41843,0.0496272,-2.94996e-05,8.76069e-09,-1.04084e-12,-5380.56,20.4609], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[16.2387,0.0206786,-7.06217e-06,1.09553e-09,-6.35307e-14,-10571.8,-55.0447], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-44.7817,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (340.893,'J/mol/K'),
    ),
    shortDesc = """2/29/96 THERM""",
    longDesc = 
"""
2/29/96 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCC=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 386,
    label = "C5H10OOH2-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {18,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {6,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u1 p0 c0 {3,S} {4,S} {17,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.27092,0.0682959,-4.63421e-05,1.61404e-08,-2.30884e-12,-9583.4,27.9668], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[21.0899,0.0237168,-8.19006e-06,1.27986e-09,-7.45974e-14,-16670.2,-79.1384], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-80.1779,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THRM""",
    longDesc = 
"""
7/19/ 0 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 387,
    label = "C5H10OOH2-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {18,S}
3  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
5  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
7  C u1 p0 c0 {4,S} {16,S} {17,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.518862,0.0744935,-5.64623e-05,2.26489e-08,-3.77612e-12,-8223.73,30.2858], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[21.7441,0.0233958,-8.13003e-06,1.27567e-09,-7.45598e-14,-15526.1,-83.3092], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-69.3854,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THRM""",
    longDesc = 
"""
7/19/ 0 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(CCC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 388,
    label = "C7H14OOH4-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {8,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {20,S} {21,S} {22,S}
8  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
9  C u1 p0 c0 {3,S} {6,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,32.6103], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.891], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-127.882,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]C(CCC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 389,
    label = "C6H12OOH2-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {7,S} {8,S} {10,S} {11,S}
6  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
8  C u1 p0 c0 {4,S} {5,S} {20,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.01849,0.0805627,-5.46524e-05,1.90949e-08,-2.74736e-12,-12466.7,30.1432], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[24.2386,0.0282612,-9.75785e-06,1.52463e-09,-8.8853e-14,-20768.1,-95.3255], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-104.007,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 390,
    label = "C6H12OOH2-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
6  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
8  C u1 p0 c0 {5,S} {7,S} {20,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.01849,0.0805627,-5.46524e-05,1.90949e-08,-2.74736e-12,-12466.7,30.1432], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[24.2386,0.0282612,-9.75785e-06,1.52463e-09,-8.8853e-14,-20768.1,-95.3255], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-104.007,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 391,
    label = "C6H12OOH2-6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
8  C u1 p0 c0 {6,S} {19,S} {20,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.327958,0.0864936,-6.43068e-05,2.52817e-08,-4.13906e-12,-11117,32.1731], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[24.9425,0.0278897,-9.67889e-06,1.51736e-09,-8.86313e-14,-19645.6,-99.7839], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-93.2385,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 392,
    label = "C3H6O1-2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.21988,0.0428579,-3.1753e-05,1.21764e-08,-1.94154e-12,-12295.4,28.8468], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[11.9825,0.0123965,-4.39114e-06,6.97911e-10,-4.11585e-14,-16973.9,-42.2894], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-106.753,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (228.648,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1CO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 393,
    label = "C5H10OOH1-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {18,S}
3  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
6  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
7  C u1 p0 c0 {4,S} {6,S} {17,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.66305,0.0642512,-3.94125e-05,1.15348e-08,-1.25128e-12,-7222.88,27.0064], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[20.9225,0.0234863,-8.03644e-06,1.24881e-09,-7.25228e-14,-14324.6,-77.9153], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-60.4527,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THRM""",
    longDesc = 
"""
7/19/ 0 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 394,
    label = "C6H103OOH2-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {7,D} {15,S}
7  C u0 p0 c0 {4,S} {6,D} {16,S}
8  C u1 p0 c0 {3,S} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.512701,0.0846518,-6.80012e-05,2.88058e-08,-5.01541e-12,3916.7,37.5352], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[23.5707,0.0244363,-8.4992e-06,1.33441e-09,-7.80268e-14,-4140.7,-90.5552], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (30.8918,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C=CCC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 395,
    label = "C5H10OOH1-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {18,S}
3  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
7  C u1 p0 c0 {5,S} {16,S} {17,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.26957,0.0692172,-4.85627e-05,1.80145e-08,-2.81415e-12,-5923.85,27.6018], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[21.0114,0.0240561,-8.36617e-06,1.3134e-09,-7.67917e-14,-12975.8,-78.933], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-49.8084,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THRM""",
    longDesc = 
"""
7/19/ 0 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 396,
    label = "C6H113O2-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
4  C u0 p0 c0 {6,S} {8,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {3,S} {8,D} {19,S}
8  C u0 p0 c0 {4,S} {7,D} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.302934,0.0803128,-6.22466e-05,2.61217e-08,-4.58234e-12,-2490.49,35.0985], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[21.521,0.02642,-9.14097e-06,1.42998e-09,-8.33989e-14,-9928.51,-81.3291], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-22.4131,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CC(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 397,
    label = "C6H12OOH3-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  C u1 p0 c0 {6,S} {19,S} {20,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.327958,0.0864936,-6.43068e-05,2.52817e-08,-4.13906e-12,-11117,32.1731], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[24.9425,0.0278897,-9.67889e-06,1.51736e-09,-8.86313e-14,-19645.6,-99.7839], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-93.2385,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(CCC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 398,
    label = "C6H12OH-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {20,S}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
7  C u1 p0 c0 {4,S} {6,S} {19,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.730467,0.0680554,-3.71632e-05,8.47843e-09,-3.99384e-13,-17847.8,32.0923], Tmin=(298,'K'), Tmax=(1374,'K')),
            NASAPolynomial(coeffs=[20.8351,0.027516,-9.19213e-06,1.40614e-09,-8.0791e-14,-25400.6,-78.0442], Tmin=(1374,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-149.403,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """6/25/99 THERM""",
    longDesc = 
"""
6/25/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC[CH]CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 399,
    label = "C6H12OH-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {20,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
7  C u1 p0 c0 {2,S} {4,S} {19,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.203283,0.0728935,-4.592e-05,1.45115e-08,-1.81147e-12,-20003.6,33.6752], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[20.5389,0.0282512,-9.5328e-06,1.46688e-09,-8.45889e-14,-27335.7,-76.5278], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-167.523,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """6/25/99 THERM""",
    longDesc = 
"""
6/25/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]C(C)O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 400,
    label = "C6H12OH-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {20,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {6,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  C u1 p0 c0 {2,S} {4,S} {19,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.203283,0.0728935,-4.592e-05,1.45115e-08,-1.81147e-12,-20003.6,33.6752], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[20.5389,0.0282512,-9.5328e-06,1.46688e-09,-8.45889e-14,-27335.7,-76.5278], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-167.523,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """6/25/99 THERM""",
    longDesc = 
"""
6/25/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]C(O)CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 401,
    label = "C2H3O1-2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {1,S} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.62965,0.0293455,-2.43738e-05,1.00522e-08,-1.61259e-12,15245.9,32.2783], Tmin=(298,'K'), Tmax=(1492,'K')),
            NASAPolynomial(coeffs=[6.88486,0.00694721,-2.23215e-06,3.32191e-10,-1.87125e-14,12644.2,-12.3843], Tmin=(1492,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (123.517,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """4/ 3/ 0 THERM""",
    longDesc = 
"""
4/ 3/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]1CO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 402,
    label = "C6H12OOH1-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
5  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
7  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
8  C u1 p0 c0 {4,S} {5,S} {20,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4674,0.0763927,-4.77257e-05,1.46094e-08,-1.73635e-12,-10117.7,29.5852], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[23.9324,0.0282541,-9.70103e-06,1.51047e-09,-8.78256e-14,-18365.9,-92.6287], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-84.2927,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 403,
    label = "C7H14OOH3-2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {12,S}
6  C u0 p0 c0 {2,S} {5,S} {10,S} {13,S}
7  C u0 p0 c0 {5,S} {8,S} {18,S} {19,S}
8  C u0 p0 c0 {7,S} {9,S} {16,S} {17,S}
9  C u0 p0 c0 {8,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {6,S} {23,S} {24,S} {25,S}
11 C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-286.91,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(OO)C(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 404,
    label = "C7H14OOH1-2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {10,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {10,S} {12,S}
6  C u0 p0 c0 {5,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {8,S} {9,S} {15,S} {16,S}
8  C u0 p0 c0 {6,S} {7,S} {17,S} {18,S}
9  C u0 p0 c0 {7,S} {11,S} {13,S} {14,S}
10 C u0 p0 c0 {1,S} {5,S} {21,S} {22,S}
11 C u0 p0 c0 {9,S} {23,S} {24,S} {25,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89718,0.10623,-8.0277e-05,3.23649e-08,-5.4585e-12,-32279,30.2475], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[32.0144,0.0340056,-1.18416e-05,1.8606e-09,-1.08851e-13,-42717.2,-131.118], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-267.157,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCC(COO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 405,
    label = "C7H14OOH3-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {13,S}
6  C u0 p0 c0 {2,S} {5,S} {7,S} {12,S}
7  C u0 p0 c0 {6,S} {9,S} {16,S} {17,S}
8  C u0 p0 c0 {5,S} {11,S} {18,S} {19,S}
9  C u0 p0 c0 {7,S} {10,S} {14,S} {15,S}
10 C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
11 C u0 p0 c0 {8,S} {23,S} {24,S} {25,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-286.91,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(O[O])C(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 406,
    label = "C6H13O-3",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.78125,0.0797869,-5.58105e-05,2.06261e-08,-3.17214e-12,-17117.2,34.6484], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[21.057,0.0287987,-9.83768e-06,1.5259e-09,-8.84677e-14,-24745.2,-82.714], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-144.39,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (461.453,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC([O])CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 407,
    label = "O2C6H12OH-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {22,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
5  C u0 p0 c0 {2,S} {4,S} {7,S} {11,S}
6  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
7  C u0 p0 c0 {5,S} {9,S} {14,S} {15,S}
8  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
9  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.59446,0.0862866,-6.42669e-05,2.57424e-08,-4.29954e-12,-39569.2,28.3299], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[24.6632,0.0299542,-1.02286e-05,1.58602e-09,-9.19278e-14,-47412.8,-94.8235], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-328.384,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (503.026,'J/mol/K'),
    ),
    shortDesc = """6/25/99 THRM""",
    longDesc = 
"""
6/25/99 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(O)C(CC)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 408,
    label = "O2C6H12OH-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,S} {22,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
5  C u0 p0 c0 {2,S} {4,S} {8,S} {11,S}
6  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
9  C u0 p0 c0 {7,S} {16,S} {17,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.59446,0.0862866,-6.42669e-05,2.57424e-08,-4.29954e-12,-39569.2,28.3299], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[24.6632,0.0299542,-1.02286e-05,1.58602e-09,-9.19278e-14,-47412.8,-94.8235], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-328.384,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (503.026,'J/mol/K'),
    ),
    shortDesc = """6/25/99 THRM""",
    longDesc = 
"""
6/25/99 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(O[O])C(C)O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 409,
    label = "O2C6H12OH-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {8,S} {22,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
7  C u0 p0 c0 {6,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
9  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.52251,0.0803364,-5.57536e-05,2.08637e-08,-3.29895e-12,-37483.4,24.7961], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[23.7746,0.0306706,-1.04669e-05,1.62226e-09,-9.39991e-14,-44954.1,-89.4863], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-310.412,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (503.026,'J/mol/K'),
    ),
    shortDesc = """6/25/99 THRM""",
    longDesc = 
"""
6/25/99 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(CO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 410,
    label = "C5H10OOH1-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {8,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {20,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
6  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
7  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
8  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
9  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53073,0.0812167,-6.33055e-05,2.63901e-08,-4.5874e-12,-26733.8,23.9105], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[25.5479,0.0250385,-8.74244e-06,1.37611e-09,-8.06073e-14,-34634.5,-99.1022], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-221.22,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (453.139,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TM""",
    longDesc = 
"""
7/19/ 0 TM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCCOO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 411,
    label = "C6H12OOH2-6O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {9,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
8  C u0 p0 c0 {7,S} {9,S} {16,S} {17,S}
9  C u0 p0 c0 {2,S} {8,S} {18,S} {19,S}
10 C u0 p0 c0 {5,S} {20,S} {21,S} {22,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19543,0.0938208,-7.19541e-05,2.9485e-08,-5.04752e-12,-29604.6,27.1618], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.7781,0.0295252,-1.02932e-05,1.61855e-09,-9.47402e-14,-38774.4,-115.091], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-245.018,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCCCO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 412,
    label = "C6H12OOH1-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {9,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {9,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {10,S} {12,S} {13,S}
9  C u0 p0 c0 {1,S} {7,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {20,S} {21,S} {22,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19543,0.0938208,-7.19541e-05,2.9485e-08,-5.04752e-12,-29604.6,27.1618], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.7781,0.0295252,-1.02932e-05,1.61855e-09,-9.47402e-14,-38774.4,-115.091], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-245.018,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CCOO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 413,
    label = "C6H12OOH3-1O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {9,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {9,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {10,S} {12,S} {13,S}
9  C u0 p0 c0 {2,S} {7,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {20,S} {21,S} {22,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19543,0.0938208,-7.19541e-05,2.9485e-08,-5.04752e-12,-29604.6,27.1618], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.7781,0.0295252,-1.02932e-05,1.61855e-09,-9.47402e-14,-38774.4,-115.091], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-245.018,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CCO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 414,
    label = "C6H103OOH2-1O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {7,S} {9,S} {11,S}
6  C u0 p0 c0 {8,S} {10,S} {12,S} {13,S}
7  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
8  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
9  C u0 p0 c0 {5,S} {10,D} {20,S}
10 C u0 p0 c0 {6,S} {9,D} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.741773,0.0940159,-7.80996e-05,3.42989e-08,-6.17488e-12,-13176.2,34.7824], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4463,0.0260362,-9.10125e-06,1.43372e-09,-8.40289e-14,-22040.8,-106.907], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-109.704,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CC(CO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 415,
    label = "C5H10OOH1-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {8,S}
2  O u0 p2 c0 {4,S} {9,S}
3  O u0 p2 c0 {1,S} {20,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
8  C u0 p0 c0 {1,S} {7,S} {18,S} {19,S}
9  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81997,0.0772691,-5.67283e-05,2.23237e-08,-3.71501e-12,-24344.7,23.5135], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[24.8667,0.0256689,-8.97169e-06,1.41316e-09,-8.28159e-14,-32147.9,-95.1212], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-201.342,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (453.139,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TM""",
    longDesc = 
"""
7/19/ 0 TM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 416,
    label = "C6H12OOH2-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {8,S} {10,S} {12,S}
6  C u0 p0 c0 {2,S} {7,S} {9,S} {11,S}
7  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
8  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
9  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
10 C u0 p0 c0 {5,S} {20,S} {21,S} {22,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.71726,0.0983623,-7.90355e-05,3.37038e-08,-5.93018e-12,-31959.5,28.4742], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[29.5549,0.028827,-1.00438e-05,1.57872e-09,-9.23849e-14,-41318.6,-119.673], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-264.788,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCC(C)OO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 417,
    label = "C6H12OOH2-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {7,S} {8,S} {11,S}
6  C u0 p0 c0 {1,S} {7,S} {9,S} {12,S}
7  C u0 p0 c0 {5,S} {6,S} {15,S} {16,S}
8  C u0 p0 c0 {5,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
10 C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.71726,0.0983623,-7.90355e-05,3.37038e-08,-5.93018e-12,-31959.5,28.4742], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[29.5549,0.028827,-1.00438e-05,1.57872e-09,-9.23849e-14,-41318.6,-119.673], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-264.788,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CC(C)OO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 418,
    label = "C7H14OOH4-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {12,S}
6  C u0 p0 c0 {2,S} {5,S} {8,S} {13,S}
7  C u0 p0 c0 {5,S} {9,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {11,S} {18,S} {19,S}
9  C u0 p0 c0 {7,S} {10,S} {14,S} {15,S}
10 C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
11 C u0 p0 c0 {8,S} {23,S} {24,S} {25,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-286.91,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(OO)C(CC)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 419,
    label = "C5H10OOH2-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {20,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {10,S}
6  C u0 p0 c0 {1,S} {5,S} {8,S} {11,S}
7  C u0 p0 c0 {5,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
9  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.08935,0.0857157,-7.04987e-05,3.07497e-08,-5.51133e-12,-29097,25.0298], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[26.285,0.0243678,-8.50102e-06,1.33737e-09,-7.83075e-14,-37153.7,-103.435], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-241.026,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (453.139,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TM""",
    longDesc = 
"""
7/19/ 0 TM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(O[O])C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 420,
    label = "C6H12OOH2-1O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {9,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {9,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {16,S} {17,S}
7  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
8  C u0 p0 c0 {7,S} {10,S} {12,S} {13,S}
9  C u0 p0 c0 {2,S} {5,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {20,S} {21,S} {22,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19543,0.0938208,-7.19541e-05,2.9485e-08,-5.04752e-12,-29604.6,27.1618], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.7781,0.0295252,-1.02932e-05,1.61855e-09,-9.47402e-14,-38774.4,-115.091], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-245.018,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(CO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 421,
    label = "C5H10OOH2-1O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {8,S}
3  O u0 p2 c0 {1,S} {20,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {10,S}
6  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
7  C u0 p0 c0 {6,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
9  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53073,0.0812167,-6.33055e-05,2.63901e-08,-4.5874e-12,-26733.8,23.9105], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[25.5479,0.0250385,-8.74244e-06,1.37611e-09,-8.06073e-14,-34634.5,-99.1022], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-221.22,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (453.139,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TM""",
    longDesc = 
"""
7/19/ 0 TM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 422,
    label = "C6H12OOH3-2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {2,S} {5,S} {9,S} {12,S}
7  C u0 p0 c0 {5,S} {8,S} {15,S} {16,S}
8  C u0 p0 c0 {7,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
10 C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.71726,0.0983623,-7.90355e-05,3.37038e-08,-5.93018e-12,-31959.5,28.4742], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[29.5549,0.028827,-1.00438e-05,1.57872e-09,-9.23849e-14,-41318.6,-119.673], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-264.788,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(OO)C(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 423,
    label = "C7H14OOH2-1O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {10,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {10,S} {12,S}
6  C u0 p0 c0 {5,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {8,S} {9,S} {15,S} {16,S}
8  C u0 p0 c0 {6,S} {7,S} {17,S} {18,S}
9  C u0 p0 c0 {7,S} {11,S} {13,S} {14,S}
10 C u0 p0 c0 {2,S} {5,S} {21,S} {22,S}
11 C u0 p0 c0 {9,S} {23,S} {24,S} {25,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89718,0.10623,-8.0277e-05,3.23649e-08,-5.4585e-12,-32279,30.2475], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[32.0144,0.0340056,-1.18416e-05,1.8606e-09,-1.08851e-13,-42717.2,-131.118], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-267.157,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCC(CO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 424,
    label = "C7H14OOH1-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {10,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {8,S} {12,S}
6  C u0 p0 c0 {5,S} {7,S} {17,S} {18,S}
7  C u0 p0 c0 {6,S} {9,S} {15,S} {16,S}
8  C u0 p0 c0 {5,S} {10,S} {19,S} {20,S}
9  C u0 p0 c0 {7,S} {11,S} {13,S} {14,S}
10 C u0 p0 c0 {1,S} {8,S} {21,S} {22,S}
11 C u0 p0 c0 {9,S} {23,S} {24,S} {25,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89718,0.10623,-8.0277e-05,3.23649e-08,-5.4585e-12,-32279,30.2475], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[32.0144,0.0340056,-1.18416e-05,1.8606e-09,-1.08851e-13,-42717.2,-131.118], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-267.157,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(CCOO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 425,
    label = "C7H14OOH3-6O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {7,S} {9,S} {12,S}
6  C u0 p0 c0 {2,S} {8,S} {10,S} {13,S}
7  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {7,S} {18,S} {19,S}
9  C u0 p0 c0 {5,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {6,S} {23,S} {24,S} {25,S}
11 C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-286.91,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CCC(C)O[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 426,
    label = "C7H14OOH2-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {12,S}
6  C u0 p0 c0 {1,S} {5,S} {10,S} {13,S}
7  C u0 p0 c0 {5,S} {8,S} {18,S} {19,S}
8  C u0 p0 c0 {7,S} {9,S} {16,S} {17,S}
9  C u0 p0 c0 {8,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {6,S} {23,S} {24,S} {25,S}
11 C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-286.91,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(O[O])C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 427,
    label = "IC4H8OOH-TO2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
7  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
8  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17782,0.0717785,-5.88836e-05,2.56759e-08,-4.61679e-12,-25562.2,20.7846], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[22.6383,0.0203246,-7.12391e-06,1.12425e-09,-6.59733e-14,-32440.7,-88.0388], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-212.077,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (382.466,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TRM""",
    longDesc = 
"""
7/19/ 0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(COO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 428,
    label = "NC4KET12",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {15,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {3,D} {4,S} {14,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.805387,0.0652375,-5.18374e-05,2.13455e-08,-3.5986e-12,-39239.6,28.4908], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[20.2458,0.017644,-6.19055e-06,9.77688e-10,-5.74053e-14,-45814.2,-75.2145], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-327.264,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(C=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 429,
    label = "NC4KET13",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {15,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {3,D} {5,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.74883,0.0586937,-4.49606e-05,1.832e-08,-3.11765e-12,-40106.6,18.8072], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.6431,0.0180941,-6.33063e-06,9.9786e-10,-5.85076e-14,-45958.9,-71.6905], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-332.918,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CC=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 430,
    label = "NC4KET21",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {15,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {3,D} {4,S} {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.69786,0.048386,-3.05577e-05,1.02706e-08,-1.51713e-12,-41866.6,10.6715], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[18.6231,0.0190969,-6.70746e-06,1.05995e-09,-6.22564e-14,-47193,-65.5478], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-346.452,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(=O)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 431,
    label = "NC4KET23",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {15,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {3,D} {4,S} {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.450576,0.0648863,-5.04446e-05,2.03085e-08,-3.35952e-12,-42877.9,30.0154], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[19.9513,0.0179559,-6.31231e-06,9.98217e-10,-5.86637e-14,-49558.5,-74.3071], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-357.917,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 432,
    label = "NC4KET24",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {15,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
6  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {3,D} {4,S} {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.93007,0.0539296,-3.66165e-05,1.3088e-08,-1.99245e-12,-41411.9,18.6568], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[18.7707,0.0189491,-6.65182e-06,1.05081e-09,-6.17069e-14,-47232,-67.3335], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-343.975,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 433,
    label = "O2C4H8CHO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {8,D}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
8  C u0 p0 c0 {2,D} {4,S} {17,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.91848,0.0667246,-4.80871e-05,1.78589e-08,-2.71164e-12,-24983.8,23.8578], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[21.263,0.0214072,-7.38343e-06,1.15282e-09,-6.71508e-14,-31685.5,-79.9829], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-207.526,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (386.623,'J/mol/K'),
    ),
    shortDesc = """9/ 7/95 THERM""",
    longDesc = 
"""
9/ 7/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(C=O)CO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 434,
    label = "C7H14OOH4-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {8,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {9,S} {17,S} {18,S}
8  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
9  C u1 p0 c0 {7,S} {22,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.151527,0.0984303,-7.20555e-05,2.78535e-08,-4.48821e-12,-14012.6,34.6826], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.1418,0.032381,-1.12265e-05,1.75881e-09,-1.02687e-13,-23764.9,-115.573], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-117.104,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC(CCC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 435,
    label = "C6H102OOH4-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
4  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {8,S} {13,S} {14,S} {15,S}
6  C u1 p0 c0 {3,S} {4,S} {16,S}
7  C u0 p0 c0 {3,S} {8,D} {17,S}
8  C u0 p0 c0 {5,S} {7,D} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.582698,0.0769939,-5.55576e-05,2.06591e-08,-3.14739e-12,2316.57,32.7785], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[23.2398,0.0241563,-8.28585e-06,1.28952e-09,-7.49614e-14,-5562.93,-88.9427], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (18.4893,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C(C=CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 436,
    label = "TC4H9O",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.532084,0.0571613,-4.20177e-05,1.63745e-08,-2.64125e-12,-13496.3,26.2777], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[15.0819,0.0194454,-6.61334e-06,1.02279e-09,-5.91797e-14,-18811.1,-57.1659], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-114.954,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """8/ 9/ 4 THERM""",
    longDesc = 
"""
8/ 9/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 437,
    label = "IC4H8OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
5  C u1 p0 c0 {2,S} {3,S} {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29613,0.034765,-1.02506e-05,-2.04642e-09,1.18879e-12,-14562.7,15.8606], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[12.5606,0.0210637,-7.1502e-06,1.10439e-09,-6.38429e-14,-18620.3,-36.7889], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-120.903,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (315.95,'J/mol/K'),
    ),
    shortDesc = """2/14/95 THERM""",
    longDesc = 
"""
2/14/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 438,
    label = "O2HC4H8CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {17,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
8  C u1 p0 c0 {3,D} {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.82607,0.0693466,-4.93125e-05,1.69848e-08,-2.26118e-12,-24657.8,24.1168], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.822,0.0191411,-6.67919e-06,1.05127e-09,-6.15877e-14,-32309.4,-94.2581], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-205.228,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (382.466,'J/mol/K'),
    ),
    shortDesc = """9/ 7/95 THERM""",
    longDesc = 
"""
9/ 7/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)([C]=O)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 439,
    label = "C6H12OOH3-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
8  C u1 p0 c0 {5,S} {7,S} {20,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.01849,0.0805627,-5.46524e-05,1.90949e-08,-2.74736e-12,-12466.7,30.1432], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[24.2386,0.0282612,-9.75785e-06,1.52463e-09,-8.8853e-14,-20768.1,-95.3255], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-104.007,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 440,
    label = "C5H9O1-3",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {14,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.22533,0.0697272,-5.42286e-05,2.13591e-08,-3.36512e-12,1918.26,39.9711], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[18.627,0.018519,-6.21111e-06,9.52916e-10,-5.48704e-14,-4973.49,-70.9679], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (11.8239,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (345.051,'J/mol/K'),
    ),
    shortDesc = """4/ 7/97 THERM""",
    longDesc = 
"""
4/ 7/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC([O])CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 441,
    label = "C5H9O1-4",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {14,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.853019,0.064188,-4.91932e-05,2.00188e-08,-3.35963e-12,1195.1,33.8334], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[16.6809,0.0207592,-7.0929e-06,1.10032e-09,-6.37993e-14,-4675.68,-59.5056], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (7.1182,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (345.051,'J/mol/K'),
    ),
    shortDesc = """3/28/97 THERM""",
    longDesc = 
"""
3/28/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC(C)[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 442,
    label = "C6H112O2-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {3,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.709242,0.0761168,-5.65442e-05,2.28626e-08,-3.90915e-12,-2836.47,30.2207], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[21.3545,0.0265647,-9.19148e-06,1.43791e-09,-8.38625e-14,-10029.2,-80.4485], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-24.429,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (436.51,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC(CC)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 443,
    label = "C6H102OOH4-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {1,S} {5,S} {9,S} {12,S}
7  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
8  C u0 p0 c0 {10,S} {16,S} {17,S} {18,S}
9  C u0 p0 c0 {6,S} {10,D} {20,S}
10 C u0 p0 c0 {8,S} {9,D} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.58141,0.0935666,-7.8877e-05,3.51187e-08,-6.38735e-12,-15685.4,28.9658], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.9895,0.0255285,-8.91538e-06,1.40355e-09,-8.2224e-14,-24373.1,-110.867], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-129.729,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC(OO)C(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 444,
    label = "C6H102OOH4-6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {19,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {3,S} {8,S} {10,S} {11,S}
5  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {7,D} {15,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  C u1 p0 c0 {4,S} {17,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0498679,0.0826266,-6.56231e-05,2.76374e-08,-4.80771e-12,3633.75,34.702], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[23.4491,0.0245596,-8.54603e-06,1.34215e-09,-7.84946e-14,-4259.19,-89.94], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (29.0113,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(C=CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 445,
    label = "C7H14OOH4-1O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {10,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {12,S}
6  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
8  C u0 p0 c0 {7,S} {10,S} {19,S} {20,S}
9  C u0 p0 c0 {6,S} {11,S} {13,S} {14,S}
10 C u0 p0 c0 {2,S} {8,S} {21,S} {22,S}
11 C u0 p0 c0 {9,S} {23,S} {24,S} {25,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89718,0.10623,-8.0277e-05,3.23649e-08,-5.4585e-12,-32279,30.2475], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[32.0144,0.0340056,-1.18416e-05,1.8606e-09,-1.08851e-13,-42717.2,-131.118], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-267.157,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CCCO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 446,
    label = "C6H12OOH3-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {7,S} {8,S} {11,S}
6  C u0 p0 c0 {2,S} {7,S} {9,S} {12,S}
7  C u0 p0 c0 {5,S} {6,S} {15,S} {16,S}
8  C u0 p0 c0 {5,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
10 C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.71726,0.0983623,-7.90355e-05,3.37038e-08,-5.93018e-12,-31959.5,28.4742], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[29.5549,0.028827,-1.00438e-05,1.57872e-09,-9.23849e-14,-41318.6,-119.673], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-264.788,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CC(C)O[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 447,
    label = "C6H102OOH4-6O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {9,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
8  C u0 p0 c0 {10,S} {16,S} {17,S} {18,S}
9  C u0 p0 c0 {5,S} {10,D} {20,S}
10 C u0 p0 c0 {8,S} {9,D} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.77731,0.0896794,-7.21579e-05,3.08782e-08,-5.46384e-12,-13524.7,29.8041], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[27.2773,0.0261796,-9.1506e-06,1.4414e-09,-8.44747e-14,-22141,-106.013], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-111.798,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC(CCO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 448,
    label = "NC5KET32",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {18,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {7,S} {8,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
8  C u0 p0 c0 {3,D} {4,S} {5,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.724497,0.0771623,-6.1037e-05,2.55909e-08,-4.44696e-12,-46099,30.0523], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.9537,0.0226193,-7.91923e-06,1.24883e-09,-7.32468e-14,-53679.2,-88.6118], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-384.072,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(=O)C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 449,
    label = "NC5KET31",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {18,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {6,S} {8,S} {11,S} {12,S}
5  C u0 p0 c0 {7,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
8  C u0 p0 c0 {3,D} {4,S} {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14481,0.0664311,-4.75233e-05,1.85573e-08,-3.11996e-12,-44622.9,18.976], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[21.7724,0.0236117,-8.25814e-06,1.3013e-09,-7.62813e-14,-51354.3,-81.6386], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-370.046,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(=O)CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 450,
    label = "NC5KET25",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {18,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
7  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
8  C u0 p0 c0 {3,D} {5,S} {7,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.7627,0.0658725,-4.45145e-05,1.58213e-08,-2.388e-12,-44309.4,21.1181], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[21.91,0.0235018,-8.22261e-06,1.29607e-09,-7.59915e-14,-51324.2,-82.7709], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-367.857,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)CCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 451,
    label = "NC5KET24",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {18,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
5  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
8  C u0 p0 c0 {3,D} {5,S} {7,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19334,0.070405,-5.15856e-05,2.00742e-08,-3.28569e-12,-46636.9,22.952], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[22.5126,0.0229496,-8.02286e-06,1.2639e-09,-7.40777e-14,-53812.2,-86.3789], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-387.445,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)CC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 452,
    label = "NC5KET23",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {18,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
8  C u0 p0 c0 {3,D} {4,S} {7,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.109304,0.0775998,-5.94125e-05,2.36744e-08,-3.89094e-12,-45749.6,33.28], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[23.141,0.0224802,-7.87663e-06,1.24283e-09,-7.29253e-14,-53678.4,-90.0538], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-381.722,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(OO)C(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 453,
    label = "NC5KET21",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {18,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {8,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
8  C u0 p0 c0 {3,D} {5,S} {6,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.56687,0.0601979,-3.82936e-05,1.29221e-08,-1.89791e-12,-44770.3,12.9581], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[21.7535,0.0236666,-8.28611e-06,1.30664e-09,-7.66324e-14,-51281.5,-80.9341], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-370.355,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(=O)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 454,
    label = "NC5KET15",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {18,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
8  C u0 p0 c0 {3,D} {6,S} {17,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22565,0.0657621,-4.52753e-05,1.64811e-08,-2.54467e-12,-40687.6,19.0851], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[22.1776,0.023194,-8.09798e-06,1.27464e-09,-7.46625e-14,-47561.2,-83.5091], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-337.256,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CCCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 455,
    label = "NC5KET14",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {18,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {8,S} {12,S} {13,S}
7  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
8  C u0 p0 c0 {3,D} {6,S} {17,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53945,0.0708645,-5.32266e-05,2.12906e-08,-3.56677e-12,-42998.9,21.4543], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.7898,0.0226388,-7.89832e-06,1.2426e-09,-7.2761e-14,-50052.6,-87.1676], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-356.788,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCC=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 456,
    label = "NC5KET13",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {18,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
5  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
7  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
8  C u0 p0 c0 {3,D} {6,S} {17,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53945,0.0708645,-5.32266e-05,2.12906e-08,-3.56677e-12,-42998.9,21.4543], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.7898,0.0226388,-7.89832e-06,1.2426e-09,-7.2761e-14,-50052.6,-87.1676], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-356.788,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CC=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 457,
    label = "NC5KET12",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {18,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {4,S} {8,S} {13,S}
6  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
7  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
8  C u0 p0 c0 {3,D} {5,S} {17,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.564846,0.077489,-6.00818e-05,2.42433e-08,-4.0233e-12,-42126.2,31.2911], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[23.4427,0.0221541,-7.74818e-06,1.22107e-09,-7.15884e-14,-49935.1,-90.9971], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-351.112,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(C=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 458,
    label = "NC6KET12",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {5,S} {9,S} {16,S}
7  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
8  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
9  C u0 p0 c0 {3,D} {6,S} {20,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38274,0.0651972,-4.27848e-05,1.55395e-08,-2.34685e-12,-42018,27.1536], Tmin=(298,'K'), Tmax=(1431,'K')),
            NASAPolynomial(coeffs=[17.6693,0.029818,-9.43179e-06,1.38584e-09,-7.72739e-14,-46702.7,-48.7303], Tmin=(1431,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-347.162,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(C=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 459,
    label = "NC6KET13",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {4,S} {9,S} {15,S} {16,S}
8  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
9  C u0 p0 c0 {3,D} {7,S} {20,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.36497,0.0828625,-6.123e-05,2.40952e-08,-3.97858e-12,-45895.9,23.9438], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[25.9329,0.02718,-9.4634e-06,1.4868e-09,-8.69766e-14,-54144.3,-102.622], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-380.672,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CC=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 460,
    label = "NC6KET14",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
8  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
9  C u0 p0 c0 {3,D} {7,S} {20,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.36497,0.0828625,-6.123e-05,2.40952e-08,-3.97858e-12,-45895.9,23.9438], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[25.9329,0.02718,-9.4634e-06,1.4868e-09,-8.69766e-14,-54144.3,-102.622], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-380.672,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CCC=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 461,
    label = "NC6KET15",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
7  C u0 p0 c0 {6,S} {9,S} {15,S} {16,S}
8  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
9  C u0 p0 c0 {3,D} {7,S} {20,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.36497,0.0828625,-6.123e-05,2.40952e-08,-3.97858e-12,-45895.9,23.9438], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[25.9329,0.02718,-9.4634e-06,1.4868e-09,-8.69766e-14,-54144.3,-102.622], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-380.672,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCCC=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 462,
    label = "C5H10OOH3-1O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {8,S}
3  O u0 p2 c0 {1,S} {20,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
6  C u0 p0 c0 {5,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
9  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53073,0.0812167,-6.33055e-05,2.63901e-08,-4.5874e-12,-26733.8,23.9105], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[25.5479,0.0250385,-8.74244e-06,1.37611e-09,-8.06073e-14,-34634.5,-99.1022], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-221.22,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (453.139,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TM""",
    longDesc = 
"""
7/19/ 0 TM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CCO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 463,
    label = "C5H10OOH2-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {8,S}
3  O u0 p2 c0 {1,S} {20,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
6  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
7  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
8  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
9  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53073,0.0812167,-6.33055e-05,2.63901e-08,-4.5874e-12,-26733.8,23.9105], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[25.5479,0.0250385,-8.74244e-06,1.37611e-09,-8.06073e-14,-34634.5,-99.1022], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-221.22,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (453.139,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TM""",
    longDesc = 
"""
7/19/ 0 TM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCCO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 464,
    label = "NC6KET21",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
7  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
8  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
9  C u0 p0 c0 {3,D} {6,S} {7,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.39222,0.0722001,-4.62914e-05,1.57163e-08,-2.30616e-12,-47667.5,15.4472], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[24.8978,0.0282099,-9.85249e-06,1.55109e-09,-9.08649e-14,-55373.1,-96.3948], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-394.231,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(=O)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 465,
    label = "NC6KET23",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
8  C u0 p0 c0 {9,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {3,D} {4,S} {8,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.135623,0.0898799,-6.76979e-05,2.65961e-08,-4.32068e-12,-48635.8,36.0983], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[26.3431,0.0269862,-9.43297e-06,1.48602e-09,-8.70977e-14,-57801.3,-105.866], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-405.572,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(OO)C(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 466,
    label = "NC6KET24",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
5  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {9,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
8  C u0 p0 c0 {9,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {3,D} {6,S} {8,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.73253,0.0837366,-6.15876e-05,2.41189e-08,-3.9712e-12,-49492.4,26.7537], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[25.6847,0.0274782,-9.58628e-06,1.50811e-09,-8.83051e-14,-57917.7,-102.009], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-411.191,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CC(C)=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 467,
    label = "NC6KET25",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
7  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
8  C u0 p0 c0 {9,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {3,D} {6,S} {8,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.73253,0.0837366,-6.15876e-05,2.41189e-08,-3.9712e-12,-49492.4,26.7537], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[25.6847,0.0274782,-9.58628e-06,1.50811e-09,-8.83051e-14,-57917.7,-102.009], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-411.191,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)CCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 468,
    label = "NC6KET26",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
7  C u0 p0 c0 {1,S} {5,S} {16,S} {17,S}
8  C u0 p0 c0 {9,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {3,D} {6,S} {8,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.58935,0.077846,-5.24513e-05,1.8569e-08,-2.78455e-12,-47206.1,23.606], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[25.0574,0.0280369,-9.78502e-06,1.53978e-09,-9.01766e-14,-55417.5,-98.25], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-391.735,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)CCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 469,
    label = "NC6KET31",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
6  C u0 p0 c0 {7,S} {9,S} {14,S} {15,S}
7  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
8  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {3,D} {5,S} {6,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96919,0.0784437,-5.55362e-05,2.13589e-08,-3.52936e-12,-47520.1,21.4681], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[24.9195,0.0281507,-9.82267e-06,1.54542e-09,-9.0493e-14,-55446.4,-97.1141], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-393.931,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(=O)CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 470,
    label = "NC6KET32",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {8,S} {9,S} {12,S}
5  C u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
8  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {3,D} {4,S} {6,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.564145,0.0890854,-6.89132e-05,2.83152e-08,-4.8414e-12,-48997.9,32.4786], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[26.096,0.0271703,-9.4897e-06,1.49407e-09,-8.75316e-14,-57772.9,-104.067], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-407.956,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(=O)C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 471,
    label = "NC6KET34",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {8,S} {9,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
9  C u0 p0 c0 {3,D} {4,S} {6,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.564145,0.0890854,-6.89132e-05,2.83152e-08,-4.8414e-12,-48997.9,32.4786], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[26.096,0.0271703,-9.4897e-06,1.49407e-09,-8.75316e-14,-57772.9,-104.067], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-407.956,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(=O)C(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 472,
    label = "NC6KET35",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
5  C u0 p0 c0 {4,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {8,S} {9,S} {11,S} {12,S}
7  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
9  C u0 p0 c0 {3,D} {5,S} {6,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.47173,0.0826409,-6.21054e-05,2.53064e-08,-4.36121e-12,-49858,22.9726], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[25.5126,0.0276136,-9.62969e-06,1.51447e-09,-8.86568e-14,-57932.4,-100.67], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-413.58,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(=O)CC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 473,
    label = "NC6KET36",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {21,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
6  C u0 p0 c0 {8,S} {9,S} {12,S} {13,S}
7  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {3,D} {5,S} {6,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96919,0.0784437,-5.55362e-05,2.13589e-08,-3.52936e-12,-47520.1,21.4681], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[24.9195,0.0281507,-9.82267e-06,1.54542e-09,-9.0493e-14,-55446.4,-97.1141], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-393.931,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(=O)CCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 474,
    label = "C5H10OOH1-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {8,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {20,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {10,S}
6  C u0 p0 c0 {5,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
9  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53073,0.0812167,-6.33055e-05,2.63901e-08,-4.5874e-12,-26733.8,23.9105], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[25.5479,0.0250385,-8.74244e-06,1.37611e-09,-8.06073e-14,-34634.5,-99.1022], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-221.22,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (453.139,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TM""",
    longDesc = 
"""
7/19/ 0 TM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CCOO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 475,
    label = "C6H12OOH1-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {9,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {10,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {9,S} {16,S} {17,S}
9  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
10 C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19543,0.0938208,-7.19541e-05,2.9485e-08,-5.04752e-12,-29604.6,27.1618], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.7781,0.0295252,-1.02932e-05,1.61855e-09,-9.47402e-14,-38774.4,-115.091], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-245.018,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CCCOO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 476,
    label = "C3H6OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4  C u1 p0 c0 {2,S} {9,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.20494,0.0330858,-1.63894e-05,3.18104e-09,-6.84229e-14,-9129.62,24.7155], Tmin=(298,'K'), Tmax=(1674,'K')),
            NASAPolynomial(coeffs=[9.31288,0.0167579,-5.75555e-06,9.00584e-10,-5.26567e-14,-12017,-19.5011], Tmin=(1674,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-77.6086,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (245.277,'J/mol/K'),
    ),
    shortDesc = """1/ 7/98 THERM""",
    longDesc = 
"""
1/ 7/98 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 477,
    label = "C5H10OOH3-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {18,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  C u1 p0 c0 {5,S} {16,S} {17,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.518862,0.0744935,-5.64623e-05,2.26489e-08,-3.77612e-12,-8223.73,30.2858], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[21.7441,0.0233958,-8.13003e-06,1.27567e-09,-7.45598e-14,-15526.1,-83.3092], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-69.3854,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THRM""",
    longDesc = 
"""
7/19/ 0 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 478,
    label = "C5H10OOH2-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {18,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
7  C u1 p0 c0 {5,S} {16,S} {17,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.518862,0.0744935,-5.64623e-05,2.26489e-08,-3.77612e-12,-8223.73,30.2858], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[21.7441,0.0233958,-8.13003e-06,1.27567e-09,-7.45598e-14,-15526.1,-83.3092], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-69.3854,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THRM""",
    longDesc = 
"""
7/19/ 0 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 479,
    label = "C6H12OOH1-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {9,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
8  C u0 p0 c0 {7,S} {9,S} {16,S} {17,S}
9  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
10 C u0 p0 c0 {5,S} {20,S} {21,S} {22,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19543,0.0938208,-7.19541e-05,2.9485e-08,-5.04752e-12,-29604.6,27.1618], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.7781,0.0295252,-1.02932e-05,1.61855e-09,-9.47402e-14,-38774.4,-115.091], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-245.018,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCCCOO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 480,
    label = "C4H8OH-2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {16,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.10004,0.0617528,-4.77239e-05,1.99146e-08,-3.44416e-12,-32669.9,23.0901], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[18.2943,0.0209395,-7.12097e-06,1.10103e-09,-6.3689e-14,-38050.6,-62.9154], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-271.337,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (361.68,'J/mol/K'),
    ),
    shortDesc = """6/26/95 THERM""",
    longDesc = 
"""
6/26/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)C(C)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 481,
    label = "NC7KET12",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {5,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {7,S} {17,S} {18,S}
7  C u0 p0 c0 {1,S} {6,S} {10,S} {19,S}
8  C u0 p0 c0 {4,S} {9,S} {11,S} {12,S}
9  C u0 p0 c0 {8,S} {20,S} {21,S} {22,S}
10 C u0 p0 c0 {3,D} {7,S} {23,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.01241,0.108525,-8.59991e-05,3.49273e-08,-5.7379e-12,-46631.5,40.9175], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[31.404,0.0285485,-9.69586e-06,1.50017e-09,-8.68909e-14,-57404.5,-131.577], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-388.754,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCC(C=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 482,
    label = "PC4H8OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {14,S}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  C u1 p0 c0 {2,S} {3,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2033,0.0440218,-2.12296e-05,3.03715e-09,3.72028e-13,-11862.2,26.5515], Tmin=(298,'K'), Tmax=(1503,'K')),
            NASAPolynomial(coeffs=[14.0357,0.0194173,-6.5023e-06,9.95482e-10,-5.72035e-14,-16763.1,-44.1163], Tmin=(1503,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-99.7726,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (315.95,'J/mol/K'),
    ),
    shortDesc = """2/12/ 9 THERM""",
    longDesc = 
"""
2/12/ 9 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 483,
    label = "C4H8OH-1O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {6,S} {16,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88497,0.0563288,-3.98404e-05,1.53892e-08,-2.51941e-12,-30524.7,20.9293], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[17.4383,0.0216779,-7.37773e-06,1.14129e-09,-6.60391e-14,-35589.3,-57.1247], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-252.98,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (361.68,'J/mol/K'),
    ),
    shortDesc = """6/26/95 THERM""",
    longDesc = 
"""
6/26/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 484,
    label = "HOC3H6O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {13,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06954,0.0443106,-3.18636e-05,1.26409e-08,-2.12752e-12,-27589.4,18.3891], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[14.2691,0.0171838,-5.8342e-06,9.00994e-10,-5.20716e-14,-31450.2,-41.5295], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-228.792,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (291.007,'J/mol/K'),
    ),
    shortDesc = """1/ 7/98 THERM""",
    longDesc = 
"""
1/ 7/98 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(O)CO[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 485,
    label = "NC7KET13",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {4,S} {10,S} {18,S} {19,S}
9  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
10 C u0 p0 c0 {3,D} {8,S} {23,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21629,0.0947374,-6.90474e-05,2.6782e-08,-4.36392e-12,-48796.6,26.3157], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[29.0745,0.0317177,-1.10263e-05,1.73054e-09,-1.01162e-13,-58234.5,-118.064], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-404.568,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(CC=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 486,
    label = "C3H6O1-3",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {4,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.75718,0.0426372,-2.56831e-05,6.62981e-09,-5.31193e-13,-10099,36.7182], Tmin=(298,'K'), Tmax=(2035,'K')),
            NASAPolynomial(coeffs=[10.2364,0.0150515,-5.63637e-06,9.32463e-10,-5.66102e-14,-14621.2,-33.6725], Tmin=(2035,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-89.9071,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (232.805,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C1COC1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 487,
    label = "C4H8O2-3",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {7,S}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.98701,0.0632679,-5.20856e-05,2.24064e-08,-3.95417e-12,-17195.7,36.692], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[15.8264,0.0164401,-5.8068e-06,9.21146e-10,-5.42511e-14,-23533.5,-63.4845], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-148.637,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (299.321,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1OC1C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 488,
    label = "C4H8O1-3",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.5369,0.0543996,-3.4339e-05,1.0108e-08,-1.10263e-12,-15298.1,36.7401], Tmin=(298,'K'), Tmax=(1371,'K')),
            NASAPolynomial(coeffs=[15.4227,0.0170211,-6.06348e-06,9.67355e-10,-5.71992e-14,-22019.4,-61.3872], Tmin=(1371,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-132.757,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (303.478,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1CCO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 489,
    label = "C4H8O1-4",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.28506,0.0504801,-2.51999e-05,3.65744e-09,3.94863e-13,-23006.7,41.9349], Tmin=(298,'K'), Tmax=(1361,'K')),
            NASAPolynomial(coeffs=[14.2361,0.0181176,-6.46264e-06,1.03194e-09,-6.10557e-14,-29947.9,-55.2081], Tmin=(1361,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-197.511,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (307.635,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C1CCOC1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 490,
    label = "C4H8O1-2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.42033,0.0579309,-4.30236e-05,1.6668e-08,-2.64714e-12,-15395.1,36.6425], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[13.9197,0.0185551,-6.36014e-06,9.88845e-10,-5.74275e-14,-20945.3,-50.6788], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-133.217,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (299.321,'J/mol/K'),
    ),
    shortDesc = """4/ 3/ 0 THERM""",
    longDesc = 
"""
4/ 3/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC1CO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 491,
    label = "C5H10O1-2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.50916,0.0702821,-5.23078e-05,2.05331e-08,-3.37999e-12,-17926.4,38.3403], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[18.3451,0.0215894,-7.59915e-06,1.20266e-09,-7.07149e-14,-25291.9,-73.8748], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-153.573,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (369.994,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC1CO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 492,
    label = "C5H10O2-3",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.03892,0.0746407,-5.91275e-05,2.46308e-08,-4.24313e-12,-20108.9,40.0107], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[18.938,0.0210435,-7.40108e-06,1.17069e-09,-6.88106e-14,-27622.9,-77.4018], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-172.202,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (369.994,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC1OC1C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 493,
    label = "C5H10O2-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.50702,0.0713707,-4.99484e-05,1.76516e-08,-2.56653e-12,-20319.9,42.2613], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[19.1186,0.0212169,-7.53765e-06,1.20036e-09,-7.08867e-14,-28521.6,-80.3408], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-174.664,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (374.151,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1CC(C)O1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 494,
    label = "C5H10O1-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.94205,0.066844,-4.09941e-05,1.17685e-08,-1.2603e-12,-28094.3,45.8617], Tmin=(298,'K'), Tmax=(1371,'K')),
            NASAPolynomial(coeffs=[17.7075,0.0224726,-7.98404e-06,1.27147e-09,-7.50867e-14,-36306.6,-72.7393], Tmin=(1371,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-240.266,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (378.308,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1CCCO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 495,
    label = "C5H10O1-5",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.02905,0.060132,-2.12072e-05,-4.91313e-09,3.07578e-12,-29102.9,36.4699], Tmin=(298,'K'), Tmax=(1457,'K')),
            NASAPolynomial(coeffs=[21.3684,0.0197321,-7.12842e-06,1.1479e-09,-6.83163e-14,-38983.5,-100.032], Tmin=(1457,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-246.806,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (382.466,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C1CCOCC1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 496,
    label = "C5H10O1-3",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.70067,0.0651234,-3.97863e-05,1.12984e-08,-1.18141e-12,-18161.2,38.7589], Tmin=(298,'K'), Tmax=(1370,'K')),
            NASAPolynomial(coeffs=[18.5051,0.021791,-7.74804e-06,1.23454e-09,-7.29327e-14,-26215.2,-77.4524], Tmin=(1370,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-155.908,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (374.151,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC1CCO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 497,
    label = "C6H12O3-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.24329,0.0873752,-6.95554e-05,2.98574e-08,-5.31645e-12,-23012.8,42.5386], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.4401,0.0277276,-9.58423e-06,1.49835e-09,-8.73476e-14,-30957.1,-83.3772], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-196.066,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (440.667,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC1OC1CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 498,
    label = "C6H12O1-2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {2,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.60027,0.082514,-6.19869e-05,2.52987e-08,-4.35196e-12,-20847.5,40.3433], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[19.8238,0.0283076,-9.79701e-06,1.5329e-09,-8.94137e-14,-28615.6,-79.7147], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-177.507,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (440.667,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC1CO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 499,
    label = "C6H12O2-3",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.24329,0.0873752,-6.95554e-05,2.98574e-08,-5.31645e-12,-23012.8,42.5386], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.4401,0.0277276,-9.58423e-06,1.49835e-09,-8.73476e-14,-30957.1,-83.3772], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-196.066,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (440.667,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC1OC1C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 500,
    label = "C6H12O2-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.75894,0.0846044,-6.18101e-05,2.42425e-08,-4.01441e-12,-23221.6,44.9636], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[19.9502,0.0288253,-1.00218e-05,1.57295e-09,-9.19509e-14,-31567.4,-82.4847], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-198.49,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (444.824,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC1CC(C)O1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 501,
    label = "C6H12O2-5",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {4,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.21439,0.0867848,-6.36083e-05,2.52626e-08,-4.25063e-12,-33107.2,52.4812], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[18.6456,0.0302706,-1.05001e-05,1.64542e-09,-9.60802e-14,-41490.5,-75.6802], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-282.497,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (448.981,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1CCC(C)O1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 502,
    label = "C6H12O1-5",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
7  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.89881,0.0817947,-4.67359e-05,1.1523e-08,-8.38133e-13,-33993.8,46.0903], Tmin=(298,'K'), Tmax=(1369,'K')),
            NASAPolynomial(coeffs=[21.8696,0.0289645,-1.02843e-05,1.63714e-09,-9.66553e-14,-44340.7,-101.257], Tmin=(1369,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-289.23,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (453.139,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1CCCCO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 503,
    label = "C6H12O1-3",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.67891,0.0818734,-5.65068e-05,2.03434e-08,-3.05338e-12,-20964.4,45.4358], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[20.0943,0.0280281,-9.61073e-06,1.49564e-09,-8.69483e-14,-29462.3,-82.9672], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-179.646,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (444.824,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC1CCO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 504,
    label = "C7H14O2-5",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {4,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
8  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.24295,0.105687,-7.87952e-05,3.059e-08,-4.86103e-12,-36389.2,63.6526], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[22.6707,0.0334803,-1.14785e-05,1.78491e-09,-1.03672e-13,-46530.8,-96.1517], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-311.389,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (519.654,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC1CCC(C)O1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 505,
    label = "C7H14O3-5",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {10,S}
4  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {3,S} {8,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.39477,0.101847,-7.60046e-05,2.96538e-08,-4.74854e-12,-26711.8,55.1731], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[23.2693,0.0325585,-1.11625e-05,1.73574e-09,-1.00813e-13,-36435,-97.9457], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-228.625,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (515.497,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC1CC(CC)O1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 506,
    label = "C7H14O2-3",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {7,S} {10,S}
4  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
8  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.35015,0.101436,-7.70541e-05,3.06059e-08,-4.99101e-12,-26121.8,50.6558], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[24.4677,0.0313509,-1.07981e-05,1.68432e-09,-9.8041e-14,-35872.6,-103.165], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-222.412,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (511.34,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC1OC1C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 507,
    label = "C7H14O1-3",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {5,S} {18,S} {19,S}
8  C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.50036,0.100155,-7.29936e-05,2.79344e-08,-4.42246e-12,-24429.2,56.4768], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[22.6919,0.033251,-1.14458e-05,1.78456e-09,-1.03841e-13,-34159.1,-94.6347], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-209.877,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (515.497,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC1CCO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 508,
    label = "C7H14O3-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {8,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
7  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {5,S} {20,S} {21,S} {22,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.35015,0.101436,-7.70541e-05,3.06059e-08,-4.99101e-12,-26121.8,50.6558], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[24.4677,0.0313509,-1.07981e-05,1.68432e-09,-9.8041e-14,-35872.6,-103.165], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-222.412,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (511.34,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC1OC1CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 509,
    label = "C7H14O1-2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {4,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {2,S} {18,S} {19,S}
8  C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.65271,0.0970546,-7.14482e-05,2.77782e-08,-4.48129e-12,-23979.9,48.0801], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.5147,0.0321674,-1.10804e-05,1.72835e-09,-1.00601e-13,-33335.2,-97.4257], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-203.999,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (511.34,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCC1CO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 510,
    label = "C7H14O1-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {5,S} {18,S} {19,S}
8  C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.56018,0.100695,-7.10467e-05,2.59142e-08,-3.8685e-12,-34231.2,61.263], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[22.053,0.0340541,-1.16873e-05,1.81863e-09,-1.0568e-13,-44182.2,-92.4677], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-292.766,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (519.654,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC1CCCO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 511,
    label = "C5H10OOH1-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {18,S}
3  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  C u1 p0 c0 {3,S} {4,S} {17,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.66305,0.0642512,-3.94125e-05,1.15348e-08,-1.25128e-12,-7222.88,27.0064], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[20.9225,0.0234863,-8.03644e-06,1.24881e-09,-7.25228e-14,-14324.6,-77.9153], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-60.4527,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (407.409,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THRM""",
    longDesc = 
"""
7/19/ 0 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 512,
    label = "C6H12OOH1-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {8,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
7  C u0 p0 c0 {8,S} {17,S} {18,S} {19,S}
8  C u1 p0 c0 {5,S} {7,S} {20,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4674,0.0763927,-4.77257e-05,1.46094e-08,-1.73635e-12,-10117.7,29.5852], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[23.9324,0.0282541,-9.70103e-06,1.51047e-09,-8.78256e-14,-18365.9,-92.6287], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-84.2927,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 513,
    label = "C6H12OOH1-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {7,S} {8,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
8  C u1 p0 c0 {4,S} {5,S} {20,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4674,0.0763927,-4.77257e-05,1.46094e-08,-1.73635e-12,-10117.7,29.5852], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[23.9324,0.0282541,-9.70103e-06,1.51047e-09,-8.78256e-14,-18365.9,-92.6287], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-84.2927,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 514,
    label = "C6H12OOH3-6O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {9,S}
3  O u0 p2 c0 {1,S} {23,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {10,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {9,S} {16,S} {17,S}
9  C u0 p0 c0 {2,S} {8,S} {18,S} {19,S}
10 C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19543,0.0938208,-7.19541e-05,2.9485e-08,-5.04752e-12,-29604.6,27.1618], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.7781,0.0295252,-1.02932e-05,1.61855e-09,-9.47402e-14,-38774.4,-115.091], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-245.018,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CCCO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 515,
    label = "C6H12O1-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
7  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.9876,0.0836691,-5.83931e-05,2.19383e-08,-3.51302e-12,-30876.8,52.2312], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[18.1937,0.0305132,-1.05539e-05,1.65081e-09,-9.62757e-14,-39186.2,-72.8892], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-263.796,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (448.981,'J/mol/K'),
    ),
    shortDesc = """1/22/95 THERM""",
    longDesc = 
"""
1/22/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC1CCCO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 516,
    label = "C6H12OOH3-6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {21,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  C u1 p0 c0 {6,S} {19,S} {20,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.327958,0.0864936,-6.43068e-05,2.52817e-08,-4.13906e-12,-11117,32.1731], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[24.9425,0.0278897,-9.67889e-06,1.51736e-09,-8.86313e-14,-19645.6,-99.7839], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-93.2385,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 517,
    label = "NC6D1KET45",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
5  C u0 p0 c0 {7,S} {8,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {3,D} {4,S} {5,S}
8  C u0 p0 c0 {5,S} {9,D} {16,S}
9  C u0 p0 c0 {8,D} {17,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.36115,0.0904259,-7.50375e-05,3.23038e-08,-5.65763e-12,-32150.5,42.0074], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[25.1943,0.0233015,-8.16424e-06,1.2882e-09,-7.55882e-14,-40930,-98.9202], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-269.635,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC(=O)C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 518,
    label = "NC6D1KET65",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {4,S} {8,S} {12,S}
6  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
7  C u0 p0 c0 {6,S} {9,D} {15,S}
8  C u0 p0 c0 {3,D} {5,S} {16,S}
9  C u0 p0 c0 {7,D} {17,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.148871,0.0873133,-7.16904e-05,3.05825e-08,-5.31543e-12,-29173.9,36.2935], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[25.3953,0.0230473,-8.05739e-06,1.26947e-09,-7.44127e-14,-37643.4,-99.3641], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-243.727,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCC(C=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 519,
    label = "NC6D1KET46",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {7,S} {8,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
7  C u0 p0 c0 {3,D} {4,S} {5,S}
8  C u0 p0 c0 {5,S} {9,D} {16,S}
9  C u0 p0 c0 {8,D} {17,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.20616,0.0790495,-6.05529e-05,2.46671e-08,-4.19757e-12,-31165.9,31.3918], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[24.0046,0.0243109,-8.51114e-06,1.34213e-09,-7.87166e-14,-39070,-90.7535], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-259.443,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC(=O)CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 520,
    label = "NC6D2KET56",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {7,S} {8,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {9,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {3,D} {4,S} {5,S}
8  C u0 p0 c0 {4,S} {9,D} {18,S}
9  C u0 p0 c0 {6,S} {8,D} {17,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12404,0.0695391,-4.65433e-05,1.6278e-08,-2.4118e-12,-31960.7,22.1369], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[23.5243,0.0247725,-8.68259e-06,1.3702e-09,-8.04043e-14,-39470.2,-88.681], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-264.825,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCC(=O)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 521,
    label = "NC6D2KET65",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {8,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {8,D} {17,S}
8  C u0 p0 c0 {6,S} {7,D} {16,S}
9  C u0 p0 c0 {3,D} {4,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.455809,0.0834467,-6.59538e-05,2.72041e-08,-4.60895e-12,-30707.4,33.3548], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[24.9193,0.0234621,-8.20269e-06,1.29238e-09,-7.57556e-14,-38985,-97.1352], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-256.066,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CCC(C=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 522,
    label = "NC6D1KET56",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {3,D} {4,S} {6,S}
8  C u0 p0 c0 {5,S} {9,D} {16,S}
9  C u0 p0 c0 {8,D} {17,S} {18,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0187,0.0691654,-4.83997e-05,1.82279e-08,-2.9465e-12,-31338,17.5264], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[23.7619,0.0245056,-8.5752e-06,1.35176e-09,-7.92611e-14,-38514.4,-89.3197], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-258.763,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCC(=O)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 523,
    label = "NC6D1KET54",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
5  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
6  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {3,D} {4,S} {6,S}
8  C u0 p0 c0 {5,S} {9,D} {16,S}
9  C u0 p0 c0 {8,D} {17,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.201059,0.0854689,-6.79447e-05,2.80458e-08,-4.74058e-12,-32854,36.4494], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[25.0907,0.0233708,-8.18394e-06,1.29083e-09,-7.5723e-14,-41389.9,-98.4066], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-274.482,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC(OO)C(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 524,
    label = "NC6D1KET34",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {3,D} {4,S} {8,S}
8  C u0 p0 c0 {7,S} {9,D} {16,S}
9  C u0 p0 c0 {8,D} {17,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.879938,0.0906619,-7.60486e-05,3.30211e-08,-5.81959e-12,-34763.9,37.8353], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[25.7983,0.0228116,-8.00058e-06,1.26323e-09,-7.41574e-14,-43541.3,-103.595], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-290.842,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(=O)C(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 525,
    label = "NC6D1KET35",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
5  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {3,D} {5,S} {8,S}
8  C u0 p0 c0 {7,S} {9,D} {16,S}
9  C u0 p0 c0 {8,D} {17,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.859033,0.0849726,-7.03647e-05,3.07049e-08,-5.49125e-12,-35815.1,29.5315], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[25.2251,0.0232468,-8.1379e-06,1.28322e-09,-7.52598e-14,-43922.2,-99.8386], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-298.116,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(=O)CC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 526,
    label = "NC6D1KET36",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
7  C u0 p0 c0 {3,D} {5,S} {8,S}
8  C u0 p0 c0 {7,S} {9,D} {16,S}
9  C u0 p0 c0 {8,D} {17,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.64545,0.0794445,-6.17833e-05,2.55122e-08,-4.38629e-12,-33770.9,27.4198], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[24.6079,0.0238193,-8.34639e-06,1.31693e-09,-7.72709e-14,-41680.7,-95.4263], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-280.662,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(=O)CCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 527,
    label = "NC6D1KET64",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
5  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {9,D} {15,S}
8  C u0 p0 c0 {3,D} {6,S} {16,S}
9  C u0 p0 c0 {7,D} {17,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.15203,0.0790191,-6.20735e-05,2.58128e-08,-4.44363e-12,-30307,25.4105], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[24.776,0.0235074,-8.20009e-06,1.28997e-09,-7.55309e-14,-38002.2,-95.3274], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-251.286,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC(CC=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 528,
    label = "NC6D3KET12",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {8,S} {9,S} {12,S}
5  C u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {8,D} {16,S}
8  C u0 p0 c0 {4,S} {7,D} {17,S}
9  C u0 p0 c0 {3,D} {4,S} {18,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.463076,0.0825463,-6.39189e-05,2.57434e-08,-4.26673e-12,-30673.9,33.7911], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[24.9366,0.0235128,-8.2353e-06,1.2991e-09,-7.62141e-14,-39047.2,-97.0899], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-255.854,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CC(C=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 529,
    label = "NC6D3KET21",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {4,S} {9,D} {17,S}
8  C u0 p0 c0 {3,D} {5,S} {9,S}
9  C u0 p0 c0 {7,D} {8,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.56358,0.0740873,-5.34165e-05,2.03461e-08,-3.26584e-12,-33568.9,22.9824], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[24.2956,0.0241356,-8.46727e-06,1.33707e-09,-7.84956e-14,-41327,-94.2415], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-278.455,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=CC(=O)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 530,
    label = "NC6D2KET45",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {8,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {3,D} {4,S} {9,S}
8  C u0 p0 c0 {6,S} {9,D} {17,S}
9  C u0 p0 c0 {7,S} {8,D} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.344302,0.0871469,-7.08606e-05,2.99913e-08,-5.19127e-12,-36287,35.2066], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[25.3327,0.02322,-8.14428e-06,1.28595e-09,-7.54918e-14,-44885.4,-101.426], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-303.128,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC(=O)C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 531,
    label = "NC6D2KET46",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
6  C u0 p0 c0 {8,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {3,D} {4,S} {9,S}
8  C u0 p0 c0 {6,S} {9,D} {17,S}
9  C u0 p0 c0 {7,S} {8,D} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.04214,0.0674637,-5.76468e-05,2.75404e-08,-5.24364e-12,-30799.9,23.1802], Tmin=(298,'K'), Tmax=(1438,'K')),
            NASAPolynomial(coeffs=[14.7972,0.0263788,-7.98794e-06,1.13433e-09,-6.15921e-14,-34029.1,-41.1917], Tmin=(1438,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-255.316,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC(=O)CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 532,
    label = "NC7KET25",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
5  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
7  C u0 p0 c0 {5,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {10,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {3,D} {7,S} {9,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.52937,0.0958173,-6.96689e-05,2.6954e-08,-4.38728e-12,-52384,29.3851], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.833,0.0320168,-1.11508e-05,1.75226e-09,-1.0252e-13,-62014.2,-117.5], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-435.053,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CCC(C)=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 533,
    label = "NC7KET35",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
5  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {9,S} {10,S} {14,S} {15,S}
8  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
9  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
10 C u0 p0 c0 {3,D} {6,S} {7,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.52937,0.0958173,-6.96689e-05,2.6954e-08,-4.38728e-12,-52384,29.3851], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.833,0.0320168,-1.11508e-05,1.75226e-09,-1.0252e-13,-62014.2,-117.5], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-435.053,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(=O)CC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 534,
    label = "NC7KET32",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {6,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {9,S} {10,S} {15,S}
6  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {4,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {3,D} {5,S} {7,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.994514,0.108762,-8.76138e-05,3.66478e-08,-6.24245e-12,-50581.9,40.3445], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[30.9166,0.0291258,-9.92862e-06,1.53981e-09,-8.93271e-14,-61170.8,-129.265], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-421.681,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(=O)C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 535,
    label = "NC7KET34",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {5,S} {10,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {9,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {7,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {3,D} {4,S} {7,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.994514,0.108762,-8.76138e-05,3.66478e-08,-6.24245e-12,-50581.9,40.3445], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[30.9166,0.0291258,-9.92862e-06,1.53981e-09,-8.93271e-14,-61170.8,-129.265], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-421.681,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(OO)C(=O)CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 536,
    label = "NC7KET43",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {5,S} {10,S} {13,S}
5  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
6  C u0 p0 c0 {7,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {6,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {3,D} {4,S} {7,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.3227,0.094516,-6.99057e-05,2.79773e-08,-4.74244e-12,-52758.7,25.3458], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[28.6573,0.0321568,-1.11962e-05,1.75895e-09,-1.02892e-13,-62025.3,-116.135], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-437.476,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(=O)C(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 537,
    label = "NC7KET21",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {8,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {9,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {10,S} {17,S} {18,S}
8  C u0 p0 c0 {1,S} {10,S} {22,S} {23,S}
9  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
10 C u0 p0 c0 {3,D} {7,S} {8,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.96423,0.108159,-8.67776e-05,3.61807e-08,-6.14662e-12,-48240.5,41.3251], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[30.7083,0.0292465,-9.95808e-06,1.54316e-09,-8.94718e-14,-58761.6,-127.059], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-402.198,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCC(=O)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 538,
    label = "NC7KET36",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {9,S} {10,S} {14,S} {15,S}
8  C u0 p0 c0 {4,S} {21,S} {22,S} {23,S}
9  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
10 C u0 p0 c0 {3,D} {6,S} {7,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.52937,0.0958173,-6.96689e-05,2.6954e-08,-4.38728e-12,-52384,29.3851], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.833,0.0320168,-1.11508e-05,1.75226e-09,-1.0252e-13,-62014.2,-117.5], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-435.053,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(=O)CCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 539,
    label = "NC7KET23",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {6,S} {10,S} {17,S}
5  C u0 p0 c0 {6,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {5,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,S} {11,S} {12,S}
8  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {10,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {3,D} {4,S} {9,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.45571,0.108772,-8.59757e-05,3.51095e-08,-5.83436e-12,-50260.2,42.8185], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[30.5982,0.0297259,-1.01973e-05,1.58732e-09,-9.22942e-14,-60963.9,-127.838], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-419.46,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(OO)C(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 540,
    label = "NC7KET41",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {8,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {7,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {6,S} {9,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {10,S} {15,S} {16,S}
7  C u0 p0 c0 {4,S} {10,S} {17,S} {18,S}
8  C u0 p0 c0 {1,S} {4,S} {19,S} {20,S}
9  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {3,D} {6,S} {7,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77523,0.0905308,-6.36476e-05,2.42108e-08,-3.9477e-12,-50414.4,24.0464], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[28.074,0.0326743,-1.13799e-05,1.78819e-09,-1.04618e-13,-59540.2,-112.629], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-417.802,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(=O)CCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 541,
    label = "C7H14OOH3-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {8,S} {15,S} {16,S}
7  C u0 p0 c0 {3,S} {9,S} {17,S} {18,S}
8  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
9  C u1 p0 c0 {7,S} {22,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.151527,0.0984303,-7.20555e-05,2.78535e-08,-4.48821e-12,-14012.6,35.3721], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.1418,0.032381,-1.12265e-05,1.75881e-09,-1.02687e-13,-23764.9,-114.883], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-117.104,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC(CCCC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 542,
    label = "C7H14OOH1-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {9,S} {16,S} {17,S}
7  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
8  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
9  C u1 p0 c0 {5,S} {6,S} {23,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.11146,0.0891595,-5.67352e-05,1.7889e-08,-2.2226e-12,-12986.8,32.92], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[27.229,0.0324922,-1.1126e-05,1.72929e-09,-1.00428e-13,-22497.7,-108.902], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-108.045,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]CCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 543,
    label = "IO2C4H8OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,S} {16,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88826,0.0580363,-4.26691e-05,1.71759e-08,-2.91842e-12,-33388.2,18.3381], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[17.9798,0.0213452,-7.29108e-06,1.13069e-09,-6.55402e-14,-38577,-62.3554], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-276.746,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (361.68,'J/mol/K'),
    ),
    shortDesc = """8/23/95 THERM""",
    longDesc = 
"""
8/23/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(CO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 544,
    label = "TC4H8O2H-I",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u1 p0 c0 {3,S} {13,S} {14,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.5747,0.0604649,-4.84992e-05,2.05236e-08,-3.52975e-12,-6541.91,21.6853], Tmin=(298,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[17.806,0.0184953,-6.21268e-06,9.52754e-10,-5.4801e-14,-11755.6,-64.018], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-54.554,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 545,
    label = "C5H9OOH1-5",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {17,S}
3  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {7,D} {14,S}
7  C u0 p0 c0 {6,D} {15,S} {16,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.65166,0.0641855,-4.42152e-05,1.58118e-08,-2.33469e-12,-16185.6,24.9485], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[19.8576,0.0225573,-7.76951e-06,1.21189e-09,-7.05404e-14,-22627.6,-73.1968], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-134.765,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (386.623,'J/mol/K'),
    ),
    shortDesc = """3/27/97 THERM""",
    longDesc = 
"""
3/27/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 546,
    label = "C7H14OOH3-1O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {10,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {12,S}
6  C u0 p0 c0 {5,S} {7,S} {17,S} {18,S}
7  C u0 p0 c0 {6,S} {9,S} {15,S} {16,S}
8  C u0 p0 c0 {5,S} {10,S} {19,S} {20,S}
9  C u0 p0 c0 {7,S} {11,S} {13,S} {14,S}
10 C u0 p0 c0 {2,S} {8,S} {21,S} {22,S}
11 C u0 p0 c0 {9,S} {23,S} {24,S} {25,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89718,0.10623,-8.0277e-05,3.23649e-08,-5.4585e-12,-32279,30.2475], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[32.0144,0.0340056,-1.18416e-05,1.8606e-09,-1.08851e-13,-42717.2,-131.118], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-267.157,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(CCO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 547,
    label = "C7H14OOH1-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {10,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {12,S}
6  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
8  C u0 p0 c0 {7,S} {10,S} {19,S} {20,S}
9  C u0 p0 c0 {6,S} {11,S} {13,S} {14,S}
10 C u0 p0 c0 {1,S} {8,S} {21,S} {22,S}
11 C u0 p0 c0 {9,S} {23,S} {24,S} {25,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89718,0.10623,-8.0277e-05,3.23649e-08,-5.4585e-12,-32279,30.2475], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[32.0144,0.0340056,-1.18416e-05,1.8606e-09,-1.08851e-13,-42717.2,-131.118], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-267.157,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CCCOO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 548,
    label = "NC7KET14",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
5  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {8,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {10,S} {18,S} {19,S}
9  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
10 C u0 p0 c0 {3,D} {8,S} {23,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21629,0.0947374,-6.90474e-05,2.6782e-08,-4.36392e-12,-48796.6,26.3157], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[29.0745,0.0317177,-1.10263e-05,1.73054e-09,-1.01162e-13,-58234.5,-118.064], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-404.568,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CCC=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 549,
    label = "NC7KET31",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {8,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {9,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {10,S} {15,S} {16,S}
7  C u0 p0 c0 {8,S} {10,S} {17,S} {18,S}
8  C u0 p0 c0 {1,S} {7,S} {19,S} {20,S}
9  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {3,D} {6,S} {7,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77523,0.0905308,-6.36476e-05,2.42108e-08,-3.9477e-12,-50414.4,24.0464], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[28.074,0.0326743,-1.13799e-05,1.78819e-09,-1.04618e-13,-59540.2,-112.629], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-417.802,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(=O)CCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 550,
    label = "C5H9O1-5",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {14,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.60838,0.0609139,-4.36395e-05,1.64967e-08,-2.58694e-12,3424.51,33.5105], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[16.2565,0.0210561,-7.18324e-06,1.11331e-09,-6.45163e-14,-2410.03,-56.9404], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (25.8307,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (345.051,'J/mol/K'),
    ),
    shortDesc = """3/28/97 THERM""",
    longDesc = 
"""
3/28/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCCC[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 551,
    label = "MVOX",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {7,D} {15,S}
7  C u0 p0 c0 {6,D} {16,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.96655,0.0890554,-7.35045e-05,3.14932e-08,-5.45547e-12,-7322.33,55.5447], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[19.1885,0.0242678,-8.33135e-06,1.29674e-09,-7.53674e-14,-15445.6,-77.3983], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-69.111,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (399.095,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC1CC(C)O1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 552,
    label = "C7H14OOH2-4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
4  C u0 p0 c0 {6,S} {8,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {9,S} {13,S} {14,S}
7  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
8  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
9  C u1 p0 c0 {5,S} {6,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,33.2997], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.202], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-127.882,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]CC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 553,
    label = "C7H14OOH2-6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
9  C u1 p0 c0 {6,S} {8,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,33.2997], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.202], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-127.882,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CCCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 554,
    label = "C7H14OOH2-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {7,S} {8,S} {12,S}
6  C u0 p0 c0 {1,S} {7,S} {10,S} {13,S}
7  C u0 p0 c0 {5,S} {6,S} {18,S} {19,S}
8  C u0 p0 c0 {5,S} {9,S} {16,S} {17,S}
9  C u0 p0 c0 {8,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {6,S} {23,S} {24,S} {25,S}
11 C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-286.91,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CC(C)OO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 555,
    label = "C5H9OOH1-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {17,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {7,D} {14,S}
7  C u0 p0 c0 {6,D} {15,S} {16,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.767782,0.0693519,-5.2165e-05,2.06237e-08,-3.35844e-12,-17831.8,28.0374], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[20.218,0.0221512,-7.60711e-06,1.18421e-09,-6.88332e-14,-24429.7,-75.8288], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-149.057,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (386.623,'J/mol/K'),
    ),
    shortDesc = """3/27/97 THERM""",
    longDesc = 
"""
3/27/97 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 556,
    label = "C7H14O2-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {10,S}
4  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
8  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.39477,0.101847,-7.60046e-05,2.96538e-08,-4.74854e-12,-26711.8,55.1731], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[23.2693,0.0325585,-1.11625e-05,1.73574e-09,-1.00813e-13,-36435,-97.9457], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-228.625,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (515.497,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC1CC(C)O1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 557,
    label = "NC7KET24",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
6  C u0 p0 c0 {5,S} {8,S} {12,S} {13,S}
7  C u0 p0 c0 {4,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {10,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {3,D} {7,S} {9,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.52937,0.0958173,-6.96689e-05,2.6954e-08,-4.38728e-12,-52384,29.3851], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.833,0.0320168,-1.11508e-05,1.75226e-09,-1.0252e-13,-62014.2,-117.5], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-435.053,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CC(C)=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 558,
    label = "C7H14O2-6",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {5,S} {13,S} {14,S}
7  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.82018,0.107565,-7.89396e-05,2.98831e-08,-4.62102e-12,-38441.9,61.6932], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[23.3833,0.0336383,-1.16092e-05,1.81335e-09,-1.05656e-13,-49162.3,-105.501], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-329.126,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1CCCC(C)O1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 559,
    label = "C7H14OOH2-6O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {8,S} {11,S} {13,S}
6  C u0 p0 c0 {2,S} {7,S} {10,S} {12,S}
7  C u0 p0 c0 {6,S} {9,S} {14,S} {15,S}
8  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
9  C u0 p0 c0 {7,S} {8,S} {16,S} {17,S}
10 C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
11 C u0 p0 c0 {5,S} {23,S} {24,S} {25,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-286.91,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CCCC(C)OO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 560,
    label = "C7H14OOH4-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
9  C u1 p0 c0 {6,S} {8,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,32.6103], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.891], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-127.882,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CC(CCC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 561,
    label = "IC4H7OOH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {12,S} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.99117,0.0503349,-3.5628e-05,1.33952e-08,-2.11053e-12,-15109.5,15.4537], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[16.9235,0.0178397,-6.14273e-06,9.57895e-10,-5.57438e-14,-20004.1,-59.4746], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-124.985,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (315.95,'J/mol/K'),
    ),
    shortDesc = """7/19/95 THERM""",
    longDesc = 
"""
7/19/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 562,
    label = "NC7KET26",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {6,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {10,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {3,D} {7,S} {9,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.52937,0.0958173,-6.96689e-05,2.6954e-08,-4.38728e-12,-52384,29.3851], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.833,0.0320168,-1.11508e-05,1.75226e-09,-1.0252e-13,-62014.2,-117.5], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-435.053,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)CCCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 563,
    label = "C7H14OOH4-2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {7,S} {8,S} {12,S}
6  C u0 p0 c0 {2,S} {7,S} {10,S} {13,S}
7  C u0 p0 c0 {5,S} {6,S} {18,S} {19,S}
8  C u0 p0 c0 {5,S} {9,S} {16,S} {17,S}
9  C u0 p0 c0 {8,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {6,S} {23,S} {24,S} {25,S}
11 C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-286.91,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CC(C)O[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 564,
    label = "C6H101OOH4-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {2,S} {5,S} {9,S} {12,S}
7  C u0 p0 c0 {5,S} {8,S} {13,S} {14,S}
8  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
9  C u0 p0 c0 {6,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0223,0.097229,-8.42573e-05,3.825e-08,-7.03511e-12,-14160.3,31.6908], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.4867,0.0250954,-8.76367e-06,1.37964e-09,-8.08226e-14,-23041.2,-113.219], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-117.415,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(O[O])C(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 565,
    label = "IC4H8O2H-I",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u1 p0 c0 {3,S} {13,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.994785,0.0589212,-4.25202e-05,1.61371e-08,-2.55905e-12,-4080.29,25.8951], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[18.0246,0.0193668,-6.74676e-06,1.0604e-09,-6.20506e-14,-10085.9,-65.763], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-35.0284,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 566,
    label = "NC6D1KET43",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {7,S} {8,S} {10,S}
5  C u0 p0 c0 {6,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {3,D} {4,S} {5,S}
8  C u0 p0 c0 {4,S} {9,D} {16,S}
9  C u0 p0 c0 {8,D} {17,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.07757,0.0815204,-6.41161e-05,2.66231e-08,-4.58073e-12,-33362.6,30.3701], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[24.8135,0.0236679,-8.29974e-06,1.31027e-09,-7.69087e-14,-41485,-96.4575], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-277.716,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(OO)C(=O)CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 567,
    label = "NC7KET42",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {11,S}
5  C u0 p0 c0 {7,S} {9,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {10,S} {14,S} {15,S}
8  C u0 p0 c0 {4,S} {21,S} {22,S} {23,S}
9  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
10 C u0 p0 c0 {3,D} {6,S} {7,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.3227,0.094516,-6.99057e-05,2.79773e-08,-4.74244e-12,-52758.7,25.3458], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[28.6573,0.0321568,-1.11962e-05,1.75895e-09,-1.02892e-13,-62025.3,-116.135], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-437.476,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(=O)CC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 568,
    label = "C6H102OOH5-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
6  C u0 p0 c0 {2,S} {5,S} {9,S} {12,S}
7  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
8  C u0 p0 c0 {10,S} {16,S} {17,S} {18,S}
9  C u0 p0 c0 {6,S} {10,D} {20,S}
10 C u0 p0 c0 {8,S} {9,D} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.58141,0.0935666,-7.8877e-05,3.51187e-08,-6.38735e-12,-15685.4,28.9658], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.9895,0.0255285,-8.91538e-06,1.40355e-09,-8.2224e-14,-24373.1,-110.867], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-129.729,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC(O[O])C(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 569,
    label = "C6H102OOH6-4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {7,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
8  C u0 p0 c0 {10,S} {16,S} {17,S} {18,S}
9  C u0 p0 c0 {5,S} {10,D} {20,S}
10 C u0 p0 c0 {8,S} {9,D} {19,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.77731,0.0896794,-7.21579e-05,3.08782e-08,-5.46384e-12,-13524.7,29.8041], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[27.2773,0.0261796,-9.1506e-06,1.4414e-09,-8.44747e-14,-22141,-106.013], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-111.798,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC(CCOO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 570,
    label = "C7H14OOH3-7",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {3,S} {8,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {9,S} {17,S} {18,S}
8  C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
9  C u1 p0 c0 {7,S} {22,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.151527,0.0984303,-7.20555e-05,2.78535e-08,-4.48821e-12,-14012.6,35.3721], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.1418,0.032381,-1.12265e-05,1.75881e-09,-1.02687e-13,-23764.9,-114.883], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-117.104,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCCC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 571,
    label = "C6H101OOH6-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {8,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {5,S} {9,S} {11,S}
7  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
8  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
9  C u0 p0 c0 {6,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.21544,0.0932821,-7.74588e-05,3.39725e-08,-6.10567e-12,-11995.6,32.5594], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.7417,0.0257731,-9.00776e-06,1.41884e-09,-8.31503e-14,-20797.1,-108.181], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-99.439,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(CCCOO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 572,
    label = "C7H14OOH1-5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {24,S}
3  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {9,S} {16,S} {17,S}
6  C u0 p0 c0 {8,S} {9,S} {14,S} {15,S}
7  C u0 p0 c0 {1,S} {4,S} {18,S} {19,S}
8  C u0 p0 c0 {6,S} {20,S} {21,S} {22,S}
9  C u1 p0 c0 {5,S} {6,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.11146,0.0891595,-5.67352e-05,1.7889e-08,-2.2226e-12,-12986.8,32.92], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[27.229,0.0324922,-1.1126e-05,1.72929e-09,-1.00428e-13,-22497.7,-108.902], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-108.045,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/0 THERM""",
    longDesc = 
"""
7/19/0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]CCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 573,
    label = "C6H101OOH5-3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {21,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
7  C u0 p0 c0 {2,S} {6,S} {9,S} {12,S}
8  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
9  C u0 p0 c0 {7,S} {10,D} {18,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0223,0.097229,-8.42573e-05,3.825e-08,-7.03511e-12,-14160.3,31.6908], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.4867,0.0250954,-8.76367e-06,1.37964e-09,-8.08226e-14,-23041.2,-113.219], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-117.415,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (478.082,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(CC(C)OO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 574,
    label = "C6H11OOH1-5",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {20,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {18,S} {19,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.608693,0.0812533,-5.99544e-05,2.32307e-08,-3.71302e-12,-20730.7,30.4601], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[23.3879,0.0266183,-9.13554e-06,1.42154e-09,-8.26043e-14,-28521.1,-91.4098], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-172.9,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """3/27/97 THRM""",
    longDesc = 
"""
3/27/97 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species C6H111O2H-5 (i.e. same molecular structure according to RMG)
C=CCCC(C)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 575,
    label = "C6H11OOH1-4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {20,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {18,S} {19,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.608693,0.0812533,-5.99544e-05,2.32307e-08,-3.71302e-12,-20730.7,30.4601], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[23.3879,0.0266183,-9.13554e-06,1.42154e-09,-8.26043e-14,-28521.1,-91.4098], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-172.9,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (457.296,'J/mol/K'),
    ),
    shortDesc = """3/27/97 THRM""",
    longDesc = 
"""
3/27/97 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species C6H111O2H-4 (i.e. same molecular structure according to RMG)
C=CCC(CC)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 576,
    label = "TC3H6O2HCO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {14,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u1 p0 c0 {3,D} {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.03864,0.0580421,-4.32124e-05,1.58792e-08,-2.3221e-12,-22428.5,20.3681], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[20.6473,0.0148527,-5.25105e-06,8.33619e-10,-4.91256e-14,-28872,-79.5951], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-186.863,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (311.793,'J/mol/K'),
    ),
    shortDesc = """8/ 2/95 THERM""",
    longDesc = 
"""
8/ 2/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)([C]=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 577,
    label = "C2H3COC3H7",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,D} {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {15,S}
7  C u0 p0 c0 {6,D} {16,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.446467,0.0664587,-4.70074e-05,1.79961e-08,-2.93749e-12,-23062.8,27.7541], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[18.691,0.0241939,-8.38233e-06,1.31252e-09,-7.6599e-14,-29569.2,-70.5828], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-193.219,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (390.78,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(=O)CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 578,
    label = "C7H14O1-5",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {8,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {7,S} {16,S} {17,S}
7  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
8  C u0 p0 c0 {5,S} {20,S} {21,S} {22,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.14726,0.102607,-7.12373e-05,2.52355e-08,-3.63484e-12,-36282.2,59.3513], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[22.7681,0.0342097,-1.18172e-05,1.84695e-09,-1.07659e-13,-46816,-101.833], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-310.498,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (523.812,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC1CCCCO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 579,
    label = "NC6D2KET54",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {7,S} {8,S} {10,S}
5  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {9,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {3,D} {4,S} {5,S}
8  C u0 p0 c0 {4,S} {9,D} {18,S}
9  C u0 p0 c0 {6,S} {8,D} {17,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12404,0.0695391,-4.65433e-05,1.6278e-08,-2.4118e-12,-31960.7,22.1369], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[23.5243,0.0247725,-8.68259e-06,1.3702e-09,-8.04043e-14,-39470.2,-88.681], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-264.825,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC(OO)C(C)=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 580,
    label = "NC6D2KET64",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {9,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
5  C u0 p0 c0 {4,S} {9,S} {11,S} {12,S}
6  C u0 p0 c0 {8,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {4,S} {8,D} {17,S}
8  C u0 p0 c0 {6,S} {7,D} {16,S}
9  C u0 p0 c0 {3,D} {5,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.24971,0.0779954,-6.05507e-05,2.50027e-08,-4.29772e-12,-31264.8,24.4368], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[24.5803,0.0237403,-8.29551e-06,1.30646e-09,-7.65559e-14,-38936.4,-94.964], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-259.256,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC(CC=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 581,
    label = "C7H14OOH3-7O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {10,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {12,S}
6  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
7  C u0 p0 c0 {6,S} {9,S} {17,S} {18,S}
8  C u0 p0 c0 {5,S} {11,S} {13,S} {14,S}
9  C u0 p0 c0 {7,S} {10,S} {19,S} {20,S}
10 C u0 p0 c0 {2,S} {9,S} {21,S} {22,S}
11 C u0 p0 c0 {8,S} {23,S} {24,S} {25,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89718,0.10623,-8.0277e-05,3.23649e-08,-5.4585e-12,-32279,30.2475], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[32.0144,0.0340056,-1.18416e-05,1.8606e-09,-1.08851e-13,-42717.2,-131.118], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-267.157,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CCCCO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 582,
    label = "C7H14OOH1-5O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {10,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {26,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {8,S} {12,S}
6  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
7  C u0 p0 c0 {6,S} {9,S} {17,S} {18,S}
8  C u0 p0 c0 {5,S} {11,S} {13,S} {14,S}
9  C u0 p0 c0 {7,S} {10,S} {19,S} {20,S}
10 C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
11 C u0 p0 c0 {8,S} {23,S} {24,S} {25,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89718,0.10623,-8.0277e-05,3.23649e-08,-5.4585e-12,-32279,30.2475], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[32.0144,0.0340056,-1.18416e-05,1.8606e-09,-1.08851e-13,-42717.2,-131.118], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-267.157,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (594.485,'J/mol/K'),
    ),
    shortDesc = """7/19/0 TRM""",
    longDesc = 
"""
7/19/0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CCCCOO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 583,
    label = "NC6D1KET53",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {10,S}
5  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {3,D} {5,S} {6,S}
8  C u0 p0 c0 {4,S} {9,D} {16,S}
9  C u0 p0 c0 {8,D} {17,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24869,0.081625,-6.49725e-05,2.7359e-08,-4.76412e-12,-33362.8,29.1096], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[24.7813,0.0236294,-8.27119e-06,1.30417e-09,-7.64852e-14,-41354.9,-96.4101], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-277.511,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(CC(C)=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 584,
    label = "NC6D1KET63",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {19,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {4,S} {9,D} {15,S}
8  C u0 p0 c0 {3,D} {6,S} {16,S}
9  C u0 p0 c0 {7,D} {17,S} {18,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.70061,0.0815598,-6.58033e-05,2.80679e-08,-4.93298e-12,-29739.3,27.13], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[25.0462,0.0233305,-8.1511e-06,1.2836e-09,-7.52126e-14,-37592.7,-97.1357], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-246.901,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC(CCC=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 585,
    label = "CC4H8O",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.27768,0.0652482,-5.00209e-05,1.97452e-08,-3.15606e-12,-13770.7,47.8501], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[13.5132,0.0191666,-6.53902e-06,1.01367e-09,-5.87547e-14,-20031.1,-52.2147], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-123.588,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (303.478,'J/mol/K'),
    ),
    shortDesc = """6/29/95 THERM""",
    longDesc = 
"""
6/29/95 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species C4H8O1-3 (i.e. same molecular structure according to RMG)
CC1CCO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 586,
    label = "IC4H8OOH-IO2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
7  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
8  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.39424,0.0676573,-5.17084e-05,2.10796e-08,-3.5996e-12,-22478.7,22.503], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[21.897,0.0209638,-7.34665e-06,1.15927e-09,-6.80225e-14,-29266.5,-82.0541], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-186.461,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (382.466,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TRM""",
    longDesc = 
"""
7/19/ 0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(CO[O])COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 587,
    label = "NC7KET37",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {8,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {10,S} {17,S} {18,S}
7  C u0 p0 c0 {9,S} {10,S} {15,S} {16,S}
8  C u0 p0 c0 {1,S} {5,S} {19,S} {20,S}
9  C u0 p0 c0 {7,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {3,D} {6,S} {7,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77523,0.0905308,-6.36476e-05,2.42108e-08,-3.9477e-12,-50414.4,24.0464], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[28.074,0.0326743,-1.13799e-05,1.78819e-09,-1.04618e-13,-59540.2,-112.629], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-417.802,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(=O)CCCCOO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 588,
    label = "NC7KET15",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
6  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {10,S} {18,S} {19,S}
9  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
10 C u0 p0 c0 {3,D} {8,S} {23,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21629,0.0947374,-6.90474e-05,2.6782e-08,-4.36392e-12,-48796.6,26.3157], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[29.0745,0.0317177,-1.10263e-05,1.73054e-09,-1.01162e-13,-58234.5,-118.064], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-404.568,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (548.755,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(CCCC=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 589,
    label = "IC4KETIT",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {15,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {3,D} {4,S} {14,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.14244,0.0633841,-4.73085e-05,1.77145e-08,-2.67265e-12,-40936.7,23.4845], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[20.937,0.0171091,-6.01892e-06,9.52354e-10,-5.59926e-14,-47782,-82.7718], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-341.197,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(C=O)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 590,
    label = "IC4KETII",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {15,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {3,D} {4,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.15502,0.0610622,-4.49711e-05,1.70515e-08,-2.65949e-12,-38274.8,26.9612], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[19.5143,0.0182377,-6.38909e-06,1.00802e-09,-5.9144e-14,-44688.5,-71.7168], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-319.106,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (336.736,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 THERM""",
    longDesc = 
"""
7/19/ 0 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C=O)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 591,
    label = "TC4H8OOH-IO2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
7  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
8  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17782,0.0717785,-5.88836e-05,2.56759e-08,-4.61679e-12,-25562.2,20.7846], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[22.6383,0.0203246,-7.12391e-06,1.12425e-09,-6.59733e-14,-32440.7,-88.0388], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-212.077,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (382.466,'J/mol/K'),
    ),
    shortDesc = """7/19/ 0 TRM""",
    longDesc = 
"""
7/19/ 0 TRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)(CO[O])OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 592,
    label = "IIC4H7Q2-I",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {16,S}
4  O u0 p2 c0 {2,S} {17,S}
5  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
8  C u1 p0 c0 {5,S} {14,S} {15,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.93056,0.0605819,-4.23666e-05,1.49122e-08,-2.10979e-12,-16841.5,13.6228], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.05,0.0192149,-6.66623e-06,1.04496e-09,-6.10371e-14,-23208.7,-83.995], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-137.555,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (378.308,'J/mol/K'),
    ),
    shortDesc = """7/15/96 THeRM""",
    longDesc = 
"""
7/15/96 THeRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(COO)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 593,
    label = "TIC4H7Q2-I",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {3,S} {6,S}
3  O u0 p2 c0 {2,S} {16,S}
4  O u0 p2 c0 {1,S} {17,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
7  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
8  C u1 p0 c0 {5,S} {14,S} {15,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.48426,0.0661225,-5.27349e-05,2.18216e-08,-3.66789e-12,-19890.7,12.672], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[23.3849,0.018707,-6.44022e-06,1.00428e-09,-5.84468e-14,-26118.1,-87.661], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-162.679,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (378.308,'J/mol/K'),
    ),
    shortDesc = """5/ 6/96 THeRM""",
    longDesc = 
"""
5/ 6/96 THeRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)(COO)OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 594,
    label = "IIC4H7Q2-T",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {16,S}
4  O u0 p2 c0 {2,S} {17,S}
5  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {8,S} {13,S} {14,S} {15,S}
8  C u1 p0 c0 {5,S} {6,S} {7,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.16274,0.0434463,-1.76972e-05,4.88791e-10,9.03915e-13,-19650.2,0.262067], Tmin=(298,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[21.507,0.020536,-7.12383e-06,1.11655e-09,-6.52112e-14,-25111.8,-74.338], Tmin=(1377,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-159.399,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (378.308,'J/mol/K'),
    ),
    shortDesc = """7/15/96 THeRM""",
    longDesc = 
"""
7/15/96 THeRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](COO)COO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 595,
    label = "C7H14OH-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,S} {23,S}
2  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {8,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {8,S} {20,S} {21,S}
8  C u1 p0 c0 {5,S} {7,S} {22,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.458849,0.0804447,-4.57034e-05,1.14685e-08,-8.17742e-13,-20764.1,35.0409], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[24.1266,0.0316637,-1.05671e-05,1.61536e-09,-9.27675e-14,-29548.6,-94.2377], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-173.472,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (527.969,'J/mol/K'),
    ),
    shortDesc = """6/25/99 THERM""",
    longDesc = 
"""
6/25/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC[CH]CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 596,
    label = "C7H14OH-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {23,S}
2  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {7,S} {8,S} {13,S}
5  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
8  C u1 p0 c0 {4,S} {5,S} {22,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0617452,0.0852265,-5.42482e-05,1.73729e-08,-2.20759e-12,-22921,36.5946], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[23.8037,0.0325613,-1.09916e-05,1.69187e-09,-9.75842e-14,-31495.6,-92.6355], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-191.601,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (527.969,'J/mol/K'),
    ),
    shortDesc = """6/25/99 THERM""",
    longDesc = 
"""
6/25/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC[CH]C(C)O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 597,
    label = "C7H14OH-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {23,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {11,S}
3  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
8  C u1 p0 c0 {2,S} {5,S} {22,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0617452,0.0852265,-5.42482e-05,1.73729e-08,-2.20759e-12,-22921,36.5946], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[23.8037,0.0325613,-1.09916e-05,1.69187e-09,-9.75842e-14,-31495.6,-92.6355], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-191.601,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (527.969,'J/mol/K'),
    ),
    shortDesc = """6/25/99 THERM""",
    longDesc = 
"""
6/25/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]C(O)CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 598,
    label = "C5H10OH-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
6  C u1 p0 c0 {3,S} {5,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.951874,0.0558286,-2.87751e-05,5.54685e-09,1.10579e-14,-14816.9,29.3877], Tmin=(298,'K'), Tmax=(1371,'K')),
            NASAPolynomial(coeffs=[17.5642,0.0233577,-7.81504e-06,1.19675e-09,-6.88114e-14,-21160.6,-61.9821], Tmin=(1371,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-124.422,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (386.623,'J/mol/K'),
    ),
    shortDesc = """1/14/99 THERM""",
    longDesc = 
"""
1/14/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC[CH]CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 599,
    label = "C5H10OH-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {17,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u1 p0 c0 {2,S} {3,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.468531,0.0605595,-3.75901e-05,1.16489e-08,-1.41506e-12,-17015.8,30.0652], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[17.2743,0.023941,-8.07389e-06,1.24188e-09,-7.15927e-14,-23105.4,-61.1106], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-142.869,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (386.623,'J/mol/K'),
    ),
    shortDesc = """1/14/99 THERM""",
    longDesc = 
"""
1/14/99 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[CH]C(C)O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 600,
    label = "O2C5H10OH-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,S} {19,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
5  C u0 p0 c0 {2,S} {4,S} {7,S} {10,S}
6  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89617,0.0737919,-5.55489e-05,2.2498e-08,-3.79046e-12,-36623,24.546], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[21.526,0.025404,-8.65953e-06,1.3411e-09,-7.76664e-14,-43247.3,-80.0797], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-303.999,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """1/14/99 THRM""",
    longDesc = 
"""
1/14/99 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC(O[O])C(C)O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 601,
    label = "O2C5H10OH-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {7,S} {19,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
8  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.70461,0.0683289,-4.77921e-05,1.81239e-08,-2.90871e-12,-34482.3,22.2673], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[20.606,0.0261751,-8.9227e-06,1.38185e-09,-8.00236e-14,-40749.6,-73.8943], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-285.67,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (432.353,'J/mol/K'),
    ),
    shortDesc = """1/14/99 THRM""",
    longDesc = 
"""
1/14/99 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(CO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 602,
    label = "O2C7H14OH-1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {9,S} {25,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {11,S}
5  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {6,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {10,S} {12,S} {13,S}
9  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
10 C u0 p0 c0 {8,S} {22,S} {23,S} {24,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.3406,0.0923429,-6.37138e-05,2.36027e-08,-3.68903e-12,-40414,27.3239], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[26.9432,0.0351661,-1.20111e-05,1.86269e-09,-1.07975e-13,-49088,-105.078], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-334.57,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (573.699,'J/mol/K'),
    ),
    shortDesc = """6/25/99 THRM""",
    longDesc = 
"""
6/25/99 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCCC(CO)O[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 603,
    label = "O2C7H14OH-3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,S} {25,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
5  C u0 p0 c0 {2,S} {4,S} {7,S} {12,S}
6  C u0 p0 c0 {4,S} {8,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {10,S} {17,S} {18,S}
8  C u0 p0 c0 {6,S} {9,S} {13,S} {14,S}
9  C u0 p0 c0 {8,S} {19,S} {20,S} {21,S}
10 C u0 p0 c0 {7,S} {22,S} {23,S} {24,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.43174,0.0981682,-7.19259e-05,2.82501e-08,-4.63278e-12,-42502.2,30.7742], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[27.8711,0.0344299,-1.17691e-05,1.82618e-09,-1.05902e-13,-51569.1,-110.657], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-352.541,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (573.699,'J/mol/K'),
    ),
    shortDesc = """6/25/99 THRM""",
    longDesc = 
"""
6/25/99 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC(O[O])C(O)CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 604,
    label = "O2C7H14OH-2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,S} {25,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
5  C u0 p0 c0 {2,S} {4,S} {9,S} {12,S}
6  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
7  C u0 p0 c0 {6,S} {8,S} {15,S} {16,S}
8  C u0 p0 c0 {7,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
10 C u0 p0 c0 {8,S} {19,S} {20,S} {21,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.43174,0.0981682,-7.19259e-05,2.82501e-08,-4.63278e-12,-42502.2,30.7742], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[27.8711,0.0344299,-1.17691e-05,1.82618e-09,-1.05902e-13,-51569.1,-110.657], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-352.541,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (573.699,'J/mol/K'),
    ),
    shortDesc = """6/25/99 THRM""",
    longDesc = 
"""
6/25/99 THRM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCCC(O[O])C(C)O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 605,
    label = "EDHF",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {7,D} {16,S}
7  C u0 p0 c0 {4,S} {6,D} {17,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.96655,0.0890554,-7.35045e-05,3.14932e-08,-5.45547e-12,-7322.33,55.5447], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[19.1885,0.0242678,-8.33135e-06,1.29674e-09,-7.53674e-14,-15445.6,-77.3983], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-69.111,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (399.095,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC1C=CCO1
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 606,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25471.6,-0.460118], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25471.6,-0.460118], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (211.783,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """120186""",
    longDesc = 
"""
120186
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[H]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 607,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29812,0.000824944,-8.14302e-07,-9.47543e-11,4.13487e-13,-1012.52,-3.29409], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.99142,0.000700064,-5.63383e-08,-9.23158e-12,1.58275e-15,-835.034,-1.35511], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-8.64347,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """121286""",
    longDesc = 
"""
121286
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[H][H]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 608,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94643,-0.00163817,2.42103e-06,-1.60284e-09,3.8907e-13,29147.6,2.964], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.54206,-2.75506e-05,-3.1028e-09,4.55107e-12,-4.36805e-16,29230.8,4.92031], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (243.001,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """120186""",
    longDesc = 
"""
120186
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 609,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21294,0.00112749,-5.75615e-07,1.31388e-09,-8.76855e-13,-1005.25,6.03474], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.69758,0.00061352,-1.25884e-07,1.77528e-11,-1.13644e-15,-1233.93,3.18917], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-8.60473,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """121386""",
    longDesc = 
"""
121386
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O][O]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 610,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41896,0.000319256,-3.08293e-07,3.64407e-10,-1.00195e-13,3452.64,2.54433], Tmin=(298,'K'), Tmax=(1710,'K')),
            NASAPolynomial(coeffs=[2.85376,0.00102994,-2.32666e-07,1.93751e-11,-3.1576e-16,3699.5,5.78757], Tmin=(1710,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (28.5879,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """7/13/ 0 RUCIC""",
    longDesc = 
"""
7/13/ 0 RUCIC
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[OH]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 611,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38684,0.00347498,-6.3547e-06,6.96858e-09,-2.50659e-12,-30208.1,2.59023], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67215,0.00305629,-8.73026e-07,1.201e-10,-6.39162e-15,-29899.2,6.86282], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-251.778,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """20387""",
    longDesc = 
"""
20387
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 612,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29868,0.00140824,-3.96322e-06,5.64152e-09,-2.44486e-12,-1020.9,3.95037], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.92664,0.00148798,-5.68476e-07,1.0097e-10,-6.75335e-15,-922.798,5.98053], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-8.62479,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """121286""",
    longDesc = 
"""
121286
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
N#N
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 613,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3018,-0.00474912,2.11583e-05,-2.42764e-08,9.29225e-12,294.808,3.71666], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.01721,0.00223982,-6.33658e-07,1.14246e-10,-1.07909e-14,111.857,3.7851], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (2.67719,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """L 5/89""",
    longDesc = 
"""
L 5/89.
[O]O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 614,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38875,0.00656923,-1.48501e-07,-4.62581e-09,2.47151e-12,-17663.2,6.78536], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.57317,0.00433614,-1.47469e-06,2.3489e-10,-1.43165e-14,-18007,0.501137], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-147.353,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (78.9875,'J/mol/K'),
    ),
    shortDesc = """120186""",
    longDesc = 
"""
120186
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 615,
    label = "AR",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.366], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.366], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-6.19738,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """120186""",
    longDesc = 
"""
120186
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[Ar]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 616,
    label = "CO",
    molecule = 
"""
1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19036,0.00089442,-3.24928e-08,-1.046e-10,2.41966e-14,-14286.9,5.33278], Tmin=(298,'K'), Tmax=(1429,'K')),
            NASAPolynomial(coeffs=[3.11217,0.00115948,-3.3848e-07,4.41403e-11,-2.12862e-15,-14271.9,5.71725], Tmin=(1429,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-119.178,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """29/11/04""",
    longDesc = 
"""
29/11/04
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[C-]#[O+]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 617,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5793,0.00824685,-6.42716e-06,2.54637e-09,-4.1203e-13,-48416.3,8.81141], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[5.18953,0.00206006,-7.33575e-07,1.17004e-10,-6.91729e-15,-49317.9,-5.18289], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-403.253,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (62.3585,'J/mol/K'),
    ),
    shortDesc = """29/11/04""",
    longDesc = 
"""
29/11/04
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C=O
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 618,
    label = "CH3OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.82177,0.0123326,-2.73742e-06,-1.07387e-09,4.23645e-13,-25222.2,14.8104], Tmin=(298,'K'), Tmax=(1985,'K')),
            NASAPolynomial(coeffs=[3.92868,0.00981626,-3.40615e-06,5.3551e-10,-3.13776e-14,-26145.4,2.69464], Tmin=(1985,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-211.806,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """2/25/ 4 THERM""",
    longDesc = 
"""
2/25/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CO
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 619,
    label = "CH4",
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
            NASAPolynomial(coeffs=[3.72113,-0.00250293,1.90247e-05,-1.46871e-08,3.43791e-12,-10142.4,1.22777], Tmin=(298,'K'), Tmax=(1462,'K')),
            NASAPolynomial(coeffs=[4.09618,0.00744331,-2.63872e-06,4.19578e-10,-2.47508e-14,-11383.6,-4.67561], Tmin=(1462,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-84.6092,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """29/11/04""",
    longDesc = 
"""
29/11/04
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 620,
    label = "CH3",
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
            NASAPolynomial(coeffs=[3.43858,0.00407753,3.19831e-07,-9.47669e-10,2.21828e-13,16316.4,2.52807], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[3.51281,0.00511413,-1.67632e-06,2.52495e-10,-1.43303e-14,16123.8,1.62436], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (135.157,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH3]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 621,
    label = "C",
    molecule = 
"""
1 C u0 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49858,8.08578e-05,-2.6977e-07,3.04073e-10,-1.10665e-13,85458.8,4.75346], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.60209,-0.000178708,9.08704e-08,-1.14993e-11,3.31084e-16,85421.5,4.19518], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (710.556,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[C]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 622,
    label = "CH",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2002,0.00207288,-5.13443e-06,5.73389e-09,-1.95553e-12,70452.6,3.33159], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.19622,0.00234038,-7.0582e-07,9.00758e-11,-3.85504e-15,70867.2,9.17837], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (585.372,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """121286""",
    longDesc = 
"""
121286
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 623,
    label = "C2H6",
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
            NASAPolynomial(coeffs=[0.0478623,0.0240569,-1.15156e-05,2.48666e-09,-1.78344e-13,-11092.3,20.6544], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[6.05973,0.0130383,-4.48104e-06,6.97762e-10,-4.05606e-14,-13575.1,-12.8608], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-95.9911,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 624,
    label = "C2H5",
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
        E0 = (109.231,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH2]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 625,
    label = "C2H4",
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
            NASAPolynomial(coeffs=[0.23388,0.0196335,-1.16833e-05,3.64246e-09,-4.77443e-13,5464.89,19.7084], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[5.22176,0.00896137,-3.04869e-06,4.71466e-10,-2.7274e-14,3603.9,-7.47789], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (41.8192,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """10/ 4/ 5 THERM""",
    longDesc = 
"""
10/ 4/ 5 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 626,
    label = "HE",
    molecule = 
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.915349], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.915349], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-6.19738,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """120186""",
    longDesc = 
"""
120186
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[He]
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

entry(
    index = 627,
    label = "C3H8",
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
            NASAPolynomial(coeffs=[-0.30823,0.0365332,-1.97611e-05,5.15283e-09,-5.06337e-13,-13979.2,24.0479], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[9.3145,0.0173577,-5.94222e-06,9.2294e-10,-5.35577e-14,-17723.4,-28.9242], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-119.814,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """8/ 4/ 4 THERM""",
    longDesc = 
"""
8/ 4/ 4 THERM
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC
_imported from n-Heptane/n_heptane_v3.1_therm.dat.
""",
)

