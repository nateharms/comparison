from rmgpy.kinetics import Arrhenius, PDepArrhenius, ThirdBody, Troe, Lindemann
from rmgpy.molecule import Molecule
"Extra information about kinetics, as a list of dicts"

info = [
{
 "reaction": 'h + o2 <=> o + oh',
 "chemkinKinetics": """
h+o2=o+oh                                           9.650e+14 -0.262    16.200   
""",
 "rmgPyKinetics": Arrhenius(
    A = (9.65e+14, 'cm^3/(mol*s)'),
    n = -0.262,
    Ea = (16200, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'o + h2 <=> h + oh',
 "chemkinKinetics": """
o+h2=h+oh                                           5.080e+04 2.670     6.292    
""",
 "rmgPyKinetics": Arrhenius(A=(50800, 'cm^3/(mol*s)'), n=2.67, Ea=(6292, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'oh + h2 <=> h + h2o',
 "chemkinKinetics": """
oh+h2=h+h2o                                         2.247e+08 1.520     3.450    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.247e+08, 'cm^3/(mol*s)'),
    n = 1.52,
    Ea = (3450, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'o + h2o <=> oh + oh',
 "chemkinKinetics": """
o+h2o=oh+oh                                         3.445e+06 2.020     13.400   
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.445e+06, 'cm^3/(mol*s)'),
    n = 2.02,
    Ea = (13400, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h2 <=> h + h',
 "chemkinKinetics": """
h2+M=h+h+M                                          4.577e+19 -1.400    104.400  
co2/3.80/ ch4/2.00/ co/1.90/ c2h6/3.00/ h2o/12.00/ h2/2.50/ he/0.83/ 
""",
 "rmgPyKinetics": ThirdBody(
    arrheniusLow = Arrhenius(
        A = (4.577e+19, 'cm^3/(mol*s)'),
        n = -1.4,
        Ea = (104400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.9,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 12,
        Molecule(SMILES='O=C=O'): 3.8,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.83,
        Molecule(SMILES='[H][H]'): 2.5,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'o + o <=> o2',
 "chemkinKinetics": """
o+o+M=o2+M                                          6.165e+15 -0.500    0.000    
co2/3.80/ ch4/2.00/ co/1.90/ c2h6/3.00/ h2o/12.00/ h2/2.50/ ar/0.83/ he/0.83/ 
""",
 "rmgPyKinetics": ThirdBody(
    arrheniusLow = Arrhenius(
        A = (6.165e+15, 'cm^6/(mol^2*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.9,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 12,
        Molecule(SMILES='O=C=O'): 3.8,
        Molecule(SMILES='[Ar]'): 0.83,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.83,
        Molecule(SMILES='[H][H]'): 2.5,
    },
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'o + h <=> oh',
 "chemkinKinetics": """
o+h+M=oh+M                                          4.714e+18 -1.000    0.000    
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/12.00/ h2/2.50/ ar/0.75/ he/0.75/ 
""",
 "rmgPyKinetics": ThirdBody(
    arrheniusLow = Arrhenius(A=(4.714e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 12,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.75,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.75,
        Molecule(SMILES='[H][H]'): 2.5,
    },
),
 "possibleReactionFamilies": ['Oa_R_Recombination',  ],
},

{
 "reaction": 'h + oh <=> h2o',
 "chemkinKinetics": """
h+oh+M=h2o+M                                        2.500e+22 -2.000    0.000    
co2/3.80/ ch4/2.00/ co/1.90/ c2h6/3.00/ h2o/12.00/ h2/2.50/ ar/0.38/ he/0.38/ 
""",
 "rmgPyKinetics": ThirdBody(
    arrheniusLow = Arrhenius(A=(2.5e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.9,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 12,
        Molecule(SMILES='O=C=O'): 3.8,
        Molecule(SMILES='[Ar]'): 0.38,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.38,
        Molecule(SMILES='[H][H]'): 2.5,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'h + o2 <=> ho2',
 "chemkinKinetics": """
h+o2(+M)=ho2(+M)                                    4.650e+12 0.440     0.000    
co2/3.80/ ch4/2.00/ co/1.90/ c2h6/3.00/ h2o/10.00/ h2/1.30/ ar/0.00/ he/0.00/ 
    LOW/ 1.737e+19 -1.230    0.000    /
    TROE/ 6.700e-01 1e-30     1e+30     1e+30    /
DUPLICATE
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(4.65e+12, 'cm^3/(mol*s)'), n=0.44, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.737e+19, 'cm^6/(mol^2*s)'),
        n = -1.23,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.67,
    T3 = (1e-30, 'K'),
    T1 = (1e+30, 'K'),
    T2 = (1e+30, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.9,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 10,
        Molecule(SMILES='O=C=O'): 3.8,
        Molecule(SMILES='[Ar]'): 0,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0,
        Molecule(SMILES='[H][H]'): 1.3,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'h + o2 <=> ho2',
 "chemkinKinetics": """
h+o2(+M)=ho2(+M)                                    4.650e+12 0.440     0.000    

    LOW/ 6.810e+18 -1.200    0.000    /
    TROE/ 7.000e-01 1e-30     1e+30     1e+30    /
DUPLICATE
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(4.65e+12, 'cm^3/(mol*s)'), n=0.44, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (6.81e+18, 'cm^6/(mol^2*s)'),
        n = -1.2,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.7,
    T3 = (1e-30, 'K'),
    T1 = (1e+30, 'K'),
    T2 = (1e+30, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'h + o2 <=> ho2',
 "chemkinKinetics": """
h+o2(+M)=ho2(+M)                                    4.650e+12 0.440     0.000    

    LOW/ 6.128e+18 -1.200    0.000    /
    TROE/ 5.900e-01 1e-30     1e+30     1e+30    /
DUPLICATE
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(4.65e+12, 'cm^3/(mol*s)'), n=0.44, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (6.128e+18, 'cm^6/(mol^2*s)'),
        n = -1.2,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.59,
    T3 = (1e-30, 'K'),
    T1 = (1e+30, 'K'),
    T2 = (1e+30, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ho2 + h <=> oh + oh',
 "chemkinKinetics": """
ho2+h=oh+oh                                         7.079e+13 0.000     0.295    
""",
 "rmgPyKinetics": Arrhenius(A=(7.079e+13, 'cm^3/(mol*s)'), n=0, Ea=(295, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'h2 + o2 <=> h + ho2',
 "chemkinKinetics": """
h2+o2=h+ho2                                         5.176e+05 2.433     53.502   
""",
 "rmgPyKinetics": Arrhenius(
    A = (517600, 'cm^3/(mol*s)'),
    n = 2.433,
    Ea = (53502, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ho2 + o <=> oh + o2',
 "chemkinKinetics": """
ho2+o=oh+o2                                         3.250e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ho2 + oh <=> h2o + o2',
 "chemkinKinetics": """
ho2+oh=h2o+o2                                       2.890e+13 0.000     -0.497   
""",
 "rmgPyKinetics": Arrhenius(A=(2.89e+13, 'cm^3/(mol*s)'), n=0, Ea=(-497, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ho2 + ho2 <=> h2o2 + o2',
 "chemkinKinetics": """
ho2+ho2=h2o2+o2                                     1.030e+14 0.000     11.040   
DUPLICATE
""",
 "rmgPyKinetics": Arrhenius(A=(1.03e+14, 'cm^3/(mol*s)'), n=0, Ea=(11040, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ho2 + ho2 <=> h2o2 + o2',
 "chemkinKinetics": """
ho2+ho2=h2o2+o2                                     1.940e+11 0.000     -1.409   
DUPLICATE
""",
 "rmgPyKinetics": Arrhenius(A=(1.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1409, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h2o2 <=> oh + oh',
 "chemkinKinetics": """
h2o2(+M)=oh+oh(+M)                                  2.000e+12 0.900     48.749   
co2/3.80/ ch4/2.00/ co/1.90/ c2h6/3.00/ h2o/0.00/ o2/0.68/ h2o2/5.20/ h2/2.50/ ar/0.68/ he/0.00/ 
    LOW/ 3.658e+24 -2.300    48.749   /
    TROE/ 4.300e-01 1e-30     1e+30    /
DUPLICATE
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(2e+12, 's^-1'), n=0.9, Ea=(48749, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (3.658e+24, 'cm^3/(mol*s)'),
        n = -2.3,
        Ea = (48749, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.43,
    T3 = (1e-30, 'K'),
    T1 = (1e+30, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.9,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 0,
        Molecule(SMILES='[O][O]'): 0.68,
        Molecule(SMILES='O=C=O'): 3.8,
        Molecule(SMILES='[Ar]'): 0.68,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0,
        Molecule(SMILES='[H][H]'): 2.5,
        Molecule(SMILES='OO'): 5.2,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'h2o2 <=> oh + oh',
 "chemkinKinetics": """
h2o2(+M)=oh+oh(+M)                                  2.000e+12 0.900     48.749   

    LOW/ 1.609e+24 -2.300    48.749   /
    TROE/ 4.400e-01 1e-30     1e+30    /
DUPLICATE
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(2e+12, 's^-1'), n=0.9, Ea=(48749, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.609e+24, 'cm^3/(mol*s)'),
        n = -2.3,
        Ea = (48749, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.44,
    T3 = (1e-30, 'K'),
    T1 = (1e+30, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'h2o2 <=> oh + oh',
 "chemkinKinetics": """
h2o2(+M)=oh+oh(+M)                                  2.000e+12 0.900     48.749   

    LOW/ 1.865e+25 -2.300    48.749   /
    TROE/ 5.100e-01 1e-30     1e+30    /
DUPLICATE
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(2e+12, 's^-1'), n=0.9, Ea=(48749, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.865e+25, 'cm^3/(mol*s)'),
        n = -2.3,
        Ea = (48749, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.51,
    T3 = (1e-30, 'K'),
    T1 = (1e+30, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'h2o2 + h <=> h2o + oh',
 "chemkinKinetics": """
h2o2+h=h2o+oh                                       2.410e+13 0.000     3.970    
""",
 "rmgPyKinetics": Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'h2o2 + h <=> h2 + ho2',
 "chemkinKinetics": """
h2o2+h=h2+ho2                                       2.150e+10 1.000     6.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.15e+10, 'cm^3/(mol*s)'), n=1, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h2o2 + o <=> oh + ho2',
 "chemkinKinetics": """
h2o2+o=oh+ho2                                       9.550e+06 2.000     3.970    
""",
 "rmgPyKinetics": Arrhenius(A=(9.55e+06, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h2o2 + oh <=> h2o + ho2',
 "chemkinKinetics": """
h2o2+oh=h2o+ho2                                     1.740e+12 0.000     0.318    
DUPLICATE
""",
 "rmgPyKinetics": Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(318, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h2o2 + oh <=> h2o + ho2',
 "chemkinKinetics": """
h2o2+oh=h2o+ho2                                     7.590e+13 0.000     7.269    
DUPLICATE
""",
 "rmgPyKinetics": Arrhenius(A=(7.59e+13, 'cm^3/(mol*s)'), n=0, Ea=(7269, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'co + o <=> co2',
 "chemkinKinetics": """
co+o+M=co2+M                                        3.000e+14 0.000     3.000    
co2/3.80/ ch4/2.00/ co/1.90/ c2h6/3.00/ h2o/6.00/ h2/2.50/ he/0.50/ 
""",
 "rmgPyKinetics": ThirdBody(
    arrheniusLow = Arrhenius(A=(3e+14, 'cm^6/(mol^2*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.9,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 3.8,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.5,
        Molecule(SMILES='[H][H]'): 2.5,
    },
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'co + o2 <=> co2 + o',
 "chemkinKinetics": """
co+o2=co2+o                                         1.050e+12 0.000     42.540   
""",
 "rmgPyKinetics": Arrhenius(A=(1.05e+12, 'cm^3/(mol*s)'), n=0, Ea=(42540, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'co + oh <=> co2 + h',
 "chemkinKinetics": """
co+oh=co2+h                                         6.341e+04 2.053     -0.356   
DUPLICATE
""",
 "rmgPyKinetics": Arrhenius(
    A = (63410, 'cm^3/(mol*s)'),
    n = 2.053,
    Ea = (-355.67, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'co + oh <=> co2 + h',
 "chemkinKinetics": """
co+oh=co2+h                                         5.757e+12 -0.664    0.332    
DUPLICATE
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.757e+12, 'cm^3/(mol*s)'),
    n = -0.664,
    Ea = (331.83, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'co + ho2 <=> co2 + oh',
 "chemkinKinetics": """
co+ho2=co2+oh                                       1.570e+05 2.180     17.940   
""",
 "rmgPyKinetics": Arrhenius(
    A = (157000, 'cm^3/(mol*s)'),
    n = 2.18,
    Ea = (17940, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hco <=> h + co',
 "chemkinKinetics": """
hco+M=h+co+M                                        4.750e+11 0.660     14.870   
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/12.00/ h2/2.00/ 
""",
 "rmgPyKinetics": ThirdBody(
    arrheniusLow = Arrhenius(
        A = (4.75e+11, 'cm^3/(mol*s)'),
        n = 0.66,
        Ea = (14870, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 12,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hco + o2 <=> co + ho2',
 "chemkinKinetics": """
hco+o2=co+ho2                                       7.580e+12 0.000     0.410    
""",
 "rmgPyKinetics": Arrhenius(A=(7.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(410, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hco + h <=> co + h2',
 "chemkinKinetics": """
hco+h=co+h2                                         7.340e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.34e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hco + o <=> co + oh',
 "chemkinKinetics": """
hco+o=co+oh                                         3.020e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.02e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hco + o <=> co2 + h',
 "chemkinKinetics": """
hco+o=co2+h                                         3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hco + oh <=> co + h2o',
 "chemkinKinetics": """
hco+oh=co+h2o                                       1.020e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.02e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hco + ho2 => co2 + h + oh',
 "chemkinKinetics": """
hco+ho2=>co2+h+oh                                   3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hco + hco => h2 + co + co',
 "chemkinKinetics": """
hco+hco=>h2+co+co                                   3.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hco + ch3 <=> ch4 + co',
 "chemkinKinetics": """
hco+ch3=ch4+co                                      2.650e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.65e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2o + o2 <=> hco + ho2',
 "chemkinKinetics": """
ch2o+o2=hco+ho2                                     8.070e+15 0.000     53.420   
""",
 "rmgPyKinetics": Arrhenius(A=(8.07e+15, 'cm^3/(mol*s)'), n=0, Ea=(53420, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hco + o2 <=> o2cho',
 "chemkinKinetics": """
hco+o2=o2cho                                        1.200e+11 0.000     -1.100   
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch2o + o2cho <=> hco + ho2cho',
 "chemkinKinetics": """
ch2o+o2cho=hco+ho2cho                               1.990e+12 0.000     11.660   
""",
 "rmgPyKinetics": Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ocho + oh <=> ho2cho',
 "chemkinKinetics": """
ocho+oh=ho2cho                                      2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'h + co2 <=> ocho',
 "chemkinKinetics": """
h+co2=ocho                                          7.500e+13 0.000     29.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(29000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'hco + hco <=> ch2o + co',
 "chemkinKinetics": """
hco+hco=ch2o+co                                     1.800e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h + o <=> oh*',
 "chemkinKinetics": """
h+o+M=oh*+M                                         1.500e+13 0.000     5.975    
h2o/6.50/ n2/0.40/ o2/0.40/ h2/1.00/ ar/0.35/ 
""",
 "rmgPyKinetics": ThirdBody(
    arrheniusLow = Arrhenius(A=(1.5e+13, 'cm^6/(mol^2*s)'), n=0, Ea=(5975, 'cal/mol'), T0=(1, 'K')),
    efficiencies = {
        Molecule(SMILES='[O][O]'): 0.4,
        Molecule(SMILES='[H][H]'): 1,
        Molecule(SMILES='[Ar]'): 0.35,
        Molecule(SMILES='N#N'): 0.4,
        Molecule(SMILES='O'): 6.5,
    },
),
 "possibleReactionFamilies": ['Oa_R_Recombination',  ],
},

{
 "reaction": 'oh* + h2o <=> oh + h2o',
 "chemkinKinetics": """
oh*+h2o=oh+h2o                                      5.930e+12 0.500     -0.860   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.93e+12, 'cm^3/(mol*s)'),
    n = 0.5,
    Ea = (-860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'oh* + h2 <=> oh + h2',
 "chemkinKinetics": """
oh*+h2=oh+h2                                        2.950e+12 0.500     -0.444   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.95e+12, 'cm^3/(mol*s)'),
    n = 0.5,
    Ea = (-444, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'oh* + n2 <=> oh + n2',
 "chemkinKinetics": """
oh*+n2=oh+n2                                        1.080e+11 0.500     -1.242   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.08e+11, 'cm^3/(mol*s)'),
    n = 0.5,
    Ea = (-1242, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'oh* + oh <=> oh + oh',
 "chemkinKinetics": """
oh*+oh=oh+oh                                        6.010e+12 0.500     -0.764   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.01e+12, 'cm^3/(mol*s)'),
    n = 0.5,
    Ea = (-764, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'oh* + h <=> oh + h',
 "chemkinKinetics": """
oh*+h=oh+h                                          1.310e+12 0.500     -0.167   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.31e+12, 'cm^3/(mol*s)'),
    n = 0.5,
    Ea = (-167, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'oh* + ar <=> oh + ar',
 "chemkinKinetics": """
oh*+ar=oh+ar                                        1.690e+12 0.000     4.135    
""",
 "rmgPyKinetics": Arrhenius(A=(1.69e+12, 'cm^3/(mol*s)'), n=0, Ea=(4135, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'oh* + o2 <=> oh + o2',
 "chemkinKinetics": """
oh*+o2=oh+o2                                        2.100e+12 0.500     -0.478   
""",
 "rmgPyKinetics": Arrhenius(A=(2.1e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(-478, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'oh* + co2 <=> oh + co2',
 "chemkinKinetics": """
oh*+co2=oh+co2                                      2.750e+12 0.500     -0.968   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.75e+12, 'cm^3/(mol*s)'),
    n = 0.5,
    Ea = (-968, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'oh* + co <=> oh + co',
 "chemkinKinetics": """
oh*+co=oh+co                                        3.230e+12 0.500     -0.787   
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.23e+12, 'cm^3/(mol*s)'),
    n = 0.5,
    Ea = (-787, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'oh* + ch4 <=> oh + ch4',
 "chemkinKinetics": """
oh*+ch4=oh+ch4                                      3.360e+12 0.500     -0.635   
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.36e+12, 'cm^3/(mol*s)'),
    n = 0.5,
    Ea = (-635, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch + o2 <=> co + oh*',
 "chemkinKinetics": """
ch+o2=co+oh*                                        4.040e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.04e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h + o <=> co + ch*',
 "chemkinKinetics": """
c2h+o=co+ch*                                        6.200e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c + h <=> ch*',
 "chemkinKinetics": """
c+h+M=ch*+M                                         6.000e+14 0.000     6.940    

""",
 "rmgPyKinetics": ThirdBody(
    arrheniusLow = Arrhenius(A=(6e+14, 'cm^6/(mol^2*s)'), n=0, Ea=(6940, 'cal/mol'), T0=(1, 'K')),
    efficiencies = {},
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h + o2 <=> co2 + ch*',
 "chemkinKinetics": """
c2h+o2=co2+ch*                                      2.170e+10 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.17e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch* + ar <=> ch + ar',
 "chemkinKinetics": """
ch*+ar=ch+ar                                        4.000e+11 0.500     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch* + h2o <=> ch + h2o',
 "chemkinKinetics": """
ch*+h2o=ch+h2o                                      5.300e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch* + co <=> ch + co',
 "chemkinKinetics": """
ch*+co=ch+co                                        2.440e+12 0.500     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.44e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch* + co2 <=> ch + co2',
 "chemkinKinetics": """
ch*+co2=ch+co2                                      2.410e-01 4.300     -1.694   
""",
 "rmgPyKinetics": Arrhenius(A=(0.241, 'cm^3/(mol*s)'), n=4.3, Ea=(-1694, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch* + o2 <=> ch + o2',
 "chemkinKinetics": """
ch*+o2=ch+o2                                        2.480e+06 2.140     -1.720   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.48e+06, 'cm^3/(mol*s)'),
    n = 2.14,
    Ea = (-1720, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch* + h2 <=> ch + h2',
 "chemkinKinetics": """
ch*+h2=ch+h2                                        1.470e+14 0.000     1.361    
""",
 "rmgPyKinetics": Arrhenius(A=(1.47e+14, 'cm^3/(mol*s)'), n=0, Ea=(1361, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch* + ch4 <=> ch + ch4',
 "chemkinKinetics": """
ch*+ch4=ch+ch4                                      1.730e+13 0.000     0.167    
""",
 "rmgPyKinetics": Arrhenius(A=(1.73e+13, 'cm^3/(mol*s)'), n=0, Ea=(167, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch* + n2 <=> ch + n2',
 "chemkinKinetics": """
ch*+n2=ch+n2                                        3.030e+02 3.400     -0.381   
""",
 "rmgPyKinetics": Arrhenius(A=(303, 'cm^3/(mol*s)'), n=3.4, Ea=(-381, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hco + h <=> ch2o',
 "chemkinKinetics": """
hco+h(+M)=ch2o(+M)                                  1.090e+12 0.480     -0.260   
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ he/0.70/ 
    LOW/ 1.350e+24 -2.570    1.425    /
    TROE/ 7.824e-01 271       2.76e+03  6.57e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (1.09e+12, 'cm^3/(mol*s)'),
        n = 0.48,
        Ea = (-260, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (1.35e+24, 'cm^6/(mol^2*s)'),
        n = -2.57,
        Ea = (1425, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.7824,
    T3 = (271, 'K'),
    T1 = (2755, 'K'),
    T2 = (6570, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.7,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'co + h2 <=> ch2o',
 "chemkinKinetics": """
co+h2(+M)=ch2o(+M)                                  4.300e+07 1.500     79.600   
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ he/0.70/ 
    LOW/ 5.070e+27 -3.420    84.348   /
    TROE/ 9.320e-01 197       1.54e+03  1.03e+04 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (4.3e+07, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (79600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (5.07e+27, 'cm^6/(mol^2*s)'),
        n = -3.42,
        Ea = (84348, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.932,
    T3 = (197, 'K'),
    T1 = (1540, 'K'),
    T2 = (10300, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.7,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2o + oh <=> hco + h2o',
 "chemkinKinetics": """
ch2o+oh=hco+h2o                                     7.820e+07 1.630     -1.055   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.82e+07, 'cm^3/(mol*s)'),
    n = 1.63,
    Ea = (-1055, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2o + h <=> hco + h2',
 "chemkinKinetics": """
ch2o+h=hco+h2                                       5.740e+07 1.900     2.740    
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.74e+07, 'cm^3/(mol*s)'),
    n = 1.9,
    Ea = (2740, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2o + o <=> hco + oh',
 "chemkinKinetics": """
ch2o+o=hco+oh                                       6.260e+09 1.150     2.260    
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.26e+09, 'cm^3/(mol*s)'),
    n = 1.15,
    Ea = (2260, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2o + ch3 <=> hco + ch4',
 "chemkinKinetics": """
ch2o+ch3=hco+ch4                                    3.830e+01 3.360     4.312    
""",
 "rmgPyKinetics": Arrhenius(A=(38.3, 'cm^3/(mol*s)'), n=3.36, Ea=(4312, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2o + ho2 <=> hco + h2o2',
 "chemkinKinetics": """
ch2o+ho2=hco+h2o2                                   1.880e+04 2.700     11.520   
""",
 "rmgPyKinetics": Arrhenius(A=(18800, 'cm^3/(mol*s)'), n=2.7, Ea=(11520, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2o + oh <=> hoch2o',
 "chemkinKinetics": """
ch2o+oh=hoch2o                                      4.500e+15 -1.100    0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.5e+15, 'cm^3/(mol*s)'), n=-1.1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'hoch2o <=> hocho + h',
 "chemkinKinetics": """
hoch2o=hocho+h                                      1.000e+14 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'hocho <=> co + h2o',
 "chemkinKinetics": """
hocho=co+h2o                                        2.450e+12 0.000     60.470   
""",
 "rmgPyKinetics": Arrhenius(A=(2.45e+12, 's^-1'), n=0, Ea=(60470, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hocho <=> co2 + h2',
 "chemkinKinetics": """
hocho=co2+h2                                        2.950e+09 0.000     48.520   
""",
 "rmgPyKinetics": Arrhenius(A=(2.95e+09, 's^-1'), n=0, Ea=(48520, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['1,3_Insertion_CO2',  ],
},

{
 "reaction": 'ocho + ho2 <=> hocho + o2',
 "chemkinKinetics": """
ocho+ho2=hocho+o2                                   3.500e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(3.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hocho + oh => h2o + co2 + h',
 "chemkinKinetics": """
hocho+oh=>h2o+co2+h                                 2.620e+06 2.060     0.916    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.62e+06, 'cm^3/(mol*s)'),
    n = 2.06,
    Ea = (916, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hocho + oh => h2o + co + oh',
 "chemkinKinetics": """
hocho+oh=>h2o+co+oh                                 1.850e+07 1.510     -0.962   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.85e+07, 'cm^3/(mol*s)'),
    n = 1.51,
    Ea = (-962, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hocho + h => h2 + co2 + h',
 "chemkinKinetics": """
hocho+h=>h2+co2+h                                   4.240e+06 2.100     4.868    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.24e+06, 'cm^3/(mol*s)'),
    n = 2.1,
    Ea = (4868, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hocho + h => h2 + co + oh',
 "chemkinKinetics": """
hocho+h=>h2+co+oh                                   6.030e+13 -0.350    2.988    
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.03e+13, 'cm^3/(mol*s)'),
    n = -0.35,
    Ea = (2988, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hocho + ch3 => ch4 + co + oh',
 "chemkinKinetics": """
hocho+ch3=>ch4+co+oh                                3.900e-07 5.800     2.200    
""",
 "rmgPyKinetics": Arrhenius(A=(3.9e-07, 'cm^3/(mol*s)'), n=5.8, Ea=(2200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ocho + h2o2 <=> hocho + ho2',
 "chemkinKinetics": """
ocho+h2o2=hocho+ho2                                 2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hocho + ho2 => h2o2 + co + oh',
 "chemkinKinetics": """
hocho+ho2=>h2o2+co+oh                               1.000e+12 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hocho + o => co + oh + oh',
 "chemkinKinetics": """
hocho+o=>co+oh+oh                                   1.770e+18 -1.900    2.975    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.77e+18, 'cm^3/(mol*s)'),
    n = -1.9,
    Ea = (2975, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2o + ocho <=> hocho + hco',
 "chemkinKinetics": """
ch2o+ocho=hocho+hco                                 5.600e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3o <=> ch2o + h',
 "chemkinKinetics": """
ch3o(+M)=ch2o+h(+M)                                 6.800e+13 0.000     26.170   
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ 
    LOW/ 1.867e+25 -3.000    24.307   /
    TROE/ 9.000e-01 2.5e+03   1.3e+03   1e+99    /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(6.8e+13, 's^-1'), n=0, Ea=(26170, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.867e+25, 'cm^3/(mol*s)'),
        n = -3,
        Ea = (24307, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.9,
    T3 = (2500, 'K'),
    T1 = (1300, 'K'),
    T2 = (1e+99, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3o + o2 <=> ch2o + ho2',
 "chemkinKinetics": """
ch3o+o2=ch2o+ho2                                    4.380e-19 9.500     -5.501   
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.38e-19, 'cm^3/(mol*s)'),
    n = 9.5,
    Ea = (-5501, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch2o + ch3o <=> ch3oh + hco',
 "chemkinKinetics": """
ch2o+ch3o=ch3oh+hco                                 6.620e+11 0.000     2.294    
""",
 "rmgPyKinetics": Arrhenius(A=(6.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(2294, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3 + ch3oh <=> ch4 + ch3o',
 "chemkinKinetics": """
ch3+ch3oh=ch4+ch3o                                  1.440e+01 3.100     6.935    
""",
 "rmgPyKinetics": Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6935, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3o + ch3 <=> ch2o + ch4',
 "chemkinKinetics": """
ch3o+ch3=ch2o+ch4                                   1.200e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3o + h <=> ch2o + h2',
 "chemkinKinetics": """
ch3o+h=ch2o+h2                                      2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3o + ho2 <=> ch2o + h2o2',
 "chemkinKinetics": """
ch3o+ho2=ch2o+h2o2                                  3.010e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch2o + h <=> ch2oh',
 "chemkinKinetics": """
ch2o+h(+M)=ch2oh(+M)                                5.400e+11 0.454     3.600    
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ 
    LOW/ 1.270e+32 -4.820    6.530    /
    TROE/ 7.187e-01 103       1.29e+03  4.16e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (5.4e+11, 'cm^3/(mol*s)'),
        n = 0.454,
        Ea = (3600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (1.27e+32, 'cm^6/(mol^2*s)'),
        n = -4.82,
        Ea = (6530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.7187,
    T3 = (103, 'K'),
    T1 = (1291, 'K'),
    T2 = (4160, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2oh + o2 <=> ch2o + ho2',
 "chemkinKinetics": """
ch2oh+o2=ch2o+ho2                                   1.510e+15 -1.000    0.000    
DUPLICATE
""",
 "rmgPyKinetics": Arrhenius(A=(1.51e+15, 'cm^3/(mol*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch2oh + o2 <=> ch2o + ho2',
 "chemkinKinetics": """
ch2oh+o2=ch2o+ho2                                   2.410e+14 0.000     5.017    
DUPLICATE
""",
 "rmgPyKinetics": Arrhenius(A=(2.41e+14, 'cm^3/(mol*s)'), n=0, Ea=(5017, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch2oh + h <=> ch2o + h2',
 "chemkinKinetics": """
ch2oh+h=ch2o+h2                                     6.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch2oh + ho2 <=> ch2o + h2o2',
 "chemkinKinetics": """
ch2oh+ho2=ch2o+h2o2                                 1.200e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch2oh + hco <=> ch2o + ch2o',
 "chemkinKinetics": """
ch2oh+hco=ch2o+ch2o                                 1.800e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch2oh + ch3o <=> ch2o + ch3oh',
 "chemkinKinetics": """
ch2oh+ch3o=ch2o+ch3oh                               2.400e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3oh + hco <=> ch2oh + ch2o',
 "chemkinKinetics": """
ch3oh+hco=ch2oh+ch2o                                9.630e+03 2.900     13.110   
""",
 "rmgPyKinetics": Arrhenius(A=(9630, 'cm^3/(mol*s)'), n=2.9, Ea=(13110, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'oh + ch2oh <=> h2o + ch2o',
 "chemkinKinetics": """
oh+ch2oh=h2o+ch2o                                   2.400e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'o + ch2oh <=> oh + ch2o',
 "chemkinKinetics": """
o+ch2oh=oh+ch2o                                     4.200e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch2oh + ch2oh <=> ch2o + ch3oh',
 "chemkinKinetics": """
ch2oh+ch2oh=ch2o+ch3oh                              3.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch2oh + ho2 <=> hoch2o + oh',
 "chemkinKinetics": """
ch2oh+ho2=hoch2o+oh                                 1.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ch2o + ho2 <=> och2o2h',
 "chemkinKinetics": """
ch2o+ho2=och2o2h                                    1.500e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'och2o2h <=> hoch2o2',
 "chemkinKinetics": """
och2o2h=hoch2o2                                     3.000e+11 0.000     8.600    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(8600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'hoch2o2 + ho2 <=> hoch2o2h + o2',
 "chemkinKinetics": """
hoch2o2+ho2=hoch2o2h+o2                             3.500e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(3.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoch2o + oh <=> hoch2o2h',
 "chemkinKinetics": """
hoch2o+oh=hoch2o2h                                  1.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3oh <=> ch3 + oh',
 "chemkinKinetics": """
ch3oh(+M)=ch3+oh(+M)                                2.084e+18 -0.615    92.541   

    LOW/ 1.500e+43 -6.995    97.992   /
    TROE/ -4.748e-01 3.56e+04  1.12e+03  9.02e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(2.084e+18, 's^-1'), n=-0.615, Ea=(92540.6, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.5e+43, 'cm^3/(mol*s)'),
        n = -6.99452,
        Ea = (97992.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = -0.4748,
    T3 = (35578.5, 'K'),
    T1 = (1116.46, 'K'),
    T2 = (9023, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3oh <=> ch2(s) + h2o',
 "chemkinKinetics": """
ch3oh(+M)=ch2(s)+h2o(+M)                            3.121e+18 -1.017    91.712   

    LOW/ 1.430e+47 -8.227    99.417   /
    TROE/ 2.545e+00 3.29e+03  4.73e+04  4.71e+04 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(3.121e+18, 's^-1'), n=-1.017, Ea=(91712, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.43e+47, 'cm^3/(mol*s)'),
        n = -8.22668,
        Ea = (99417.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 2.545,
    T3 = (3289.78, 'K'),
    T1 = (47315.6, 'K'),
    T2 = (47110, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3oh <=> ch2oh + h',
 "chemkinKinetics": """
ch3oh(+M)=ch2oh+h(+M)                               7.896e-03 5.038     84.467   

    LOW/ 3.390e+42 -7.244    105.230  /
    TROE/ -7.391e+01 3.71e+04  4.15e+04  5.22e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(0.007896, 's^-1'), n=5.038, Ea=(84467.4, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (3.39e+42, 'cm^3/(mol*s)'),
        n = -7.24388,
        Ea = (105230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = -73.91,
    T3 = (37053.8, 'K'),
    T1 = (41496.4, 'K'),
    T2 = (5220, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3oh + h <=> ch2oh + h2',
 "chemkinKinetics": """
ch3oh+h=ch2oh+h2                                    3.070e+05 2.550     5.440    
""",
 "rmgPyKinetics": Arrhenius(A=(307000, 'cm^3/(mol*s)'), n=2.55, Ea=(5440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + h <=> ch3o + h2',
 "chemkinKinetics": """
ch3oh+h=ch3o+h2                                     1.990e+05 2.560     10.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (199000, 'cm^3/(mol*s)'),
    n = 2.56,
    Ea = (10300, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + o <=> ch2oh + oh',
 "chemkinKinetics": """
ch3oh+o=ch2oh+oh                                    3.880e+05 2.500     3.080    
""",
 "rmgPyKinetics": Arrhenius(A=(388000, 'cm^3/(mol*s)'), n=2.5, Ea=(3080, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + oh <=> ch2oh + h2o',
 "chemkinKinetics": """
ch3oh+oh=ch2oh+h2o                                  3.080e+04 2.650     -0.807   
""",
 "rmgPyKinetics": Arrhenius(
    A = (30800, 'cm^3/(mol*s)'),
    n = 2.65,
    Ea = (-806.7, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + oh <=> ch3o + h2o',
 "chemkinKinetics": """
ch3oh+oh=ch3o+h2o                                   1.500e+02 3.030     -0.763   
""",
 "rmgPyKinetics": Arrhenius(A=(150, 'cm^3/(mol*s)'), n=3.03, Ea=(-763, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + o2 <=> ch2oh + ho2',
 "chemkinKinetics": """
ch3oh+o2=ch2oh+ho2                                  2.050e+13 0.000     44.900   
""",
 "rmgPyKinetics": Arrhenius(A=(2.05e+13, 'cm^3/(mol*s)'), n=0, Ea=(44900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + ho2 <=> ch2oh + h2o2',
 "chemkinKinetics": """
ch3oh+ho2=ch2oh+h2o2                                1.080e+04 2.550     10.530   
""",
 "rmgPyKinetics": Arrhenius(A=(10800, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + ch3 <=> ch2oh + ch4',
 "chemkinKinetics": """
ch3oh+ch3=ch2oh+ch4                                 3.190e+01 3.170     7.172    
""",
 "rmgPyKinetics": Arrhenius(A=(31.9, 'cm^3/(mol*s)'), n=3.17, Ea=(7172, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3o + ch3oh <=> ch2oh + ch3oh',
 "chemkinKinetics": """
ch3o+ch3oh=ch2oh+ch3oh                              3.000e+11 0.000     4.074    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(4074, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3o + ch3o <=> ch3oh + ch2o',
 "chemkinKinetics": """
ch3o+ch3o=ch3oh+ch2o                                6.030e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3 + h <=> ch4',
 "chemkinKinetics": """
ch3+h(+M)=ch4(+M)                                   6.350e+15 -0.630    0.383    
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ he/0.70/ 
    LOW/ 2.477e+33 -4.760    2.440    /
    TROE/ 7.830e-01 74        2.94e+03  6.96e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (6.35e+15, 'cm^3/(mol*s)'),
        n = -0.63,
        Ea = (383, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (2.477e+33, 'cm^6/(mol^2*s)'),
        n = -4.76,
        Ea = (2440, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.783,
    T3 = (74, 'K'),
    T1 = (2941, 'K'),
    T2 = (6964, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.7,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch4 + h <=> ch3 + h2',
 "chemkinKinetics": """
ch4+h=ch3+h2                                        6.140e+05 2.500     9.587    
""",
 "rmgPyKinetics": Arrhenius(A=(614000, 'cm^3/(mol*s)'), n=2.5, Ea=(9587, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch4 + oh <=> ch3 + h2o',
 "chemkinKinetics": """
ch4+oh=ch3+h2o                                      5.830e+04 2.600     2.190    
""",
 "rmgPyKinetics": Arrhenius(A=(58300, 'cm^3/(mol*s)'), n=2.6, Ea=(2190, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch4 + o <=> ch3 + oh',
 "chemkinKinetics": """
ch4+o=ch3+oh                                        1.020e+09 1.500     8.600    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.02e+09, 'cm^3/(mol*s)'),
    n = 1.5,
    Ea = (8600, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch4 + ho2 <=> ch3 + h2o2',
 "chemkinKinetics": """
ch4+ho2=ch3+h2o2                                    1.130e+01 3.740     21.010   
""",
 "rmgPyKinetics": Arrhenius(A=(11.3, 'cm^3/(mol*s)'), n=3.74, Ea=(21010, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch4 + ch2 <=> ch3 + ch3',
 "chemkinKinetics": """
ch4+ch2=ch3+ch3                                     2.460e+06 2.000     8.270    
""",
 "rmgPyKinetics": Arrhenius(A=(2.46e+06, 'cm^3/(mol*s)'), n=2, Ea=(8270, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3 + oh <=> ch2(s) + h2o',
 "chemkinKinetics": """
ch3+oh(+M)=ch2(s)+h2o(+M)                           2.394e-03 4.096     -1.242   

    LOW/ 1.128e+15 -0.633    -0.493   /
    TROE/ 2.122e+00 838       2.33e+03  4.43e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (0.002394, 'cm^3/(mol*s)'),
        n = 4.096,
        Ea = (-1241.88, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (1.128e+15, 'cm^6/(mol^2*s)'),
        n = -0.63327,
        Ea = (-493.156, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 2.122,
    T3 = (837.667, 'K'),
    T1 = (2326.05, 'K'),
    T2 = (4432, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3 + oh <=> ch2o + h2',
 "chemkinKinetics": """
ch3+oh(+M)=ch2o+h2(+M)                              5.880e-14 6.721     -3.022   

    LOW/ 2.823e+05 1.469     -3.271   /
    TROE/ 1.671e+00 435       2.93e+03  3.92e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (5.88e-14, 'cm^3/(mol*s)'),
        n = 6.721,
        Ea = (-3022.23, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (282320, 'cm^6/(mol^2*s)'),
        n = 1.46878,
        Ea = (-3270.56, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 1.671,
    T3 = (434.782, 'K'),
    T1 = (2934.21, 'K'),
    T2 = (3919, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3 + oh <=> ch2oh + h',
 "chemkinKinetics": """
ch3+oh(+M)=ch2oh+h(+M)                              5.860e-06 5.009     1.886    

    LOW/ 6.580e+09 0.996     3.191    /
    TROE/ 1.349e+00 612       2.3e+03   4.41e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (5.86e-06, 'cm^3/(mol*s)'),
        n = 5.009,
        Ea = (1886.46, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (6.58e+09, 'cm^6/(mol^2*s)'),
        n = 0.996,
        Ea = (3191.12, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 1.349,
    T3 = (612.15, 'K'),
    T1 = (2296.27, 'K'),
    T2 = (4411, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3 + oh <=> h + ch3o',
 "chemkinKinetics": """
ch3+oh(+M)=h+ch3o(+M)                               1.780e-46 18.590    -0.027   

    LOW/ 1.200e+09 1.014     11.948   /
    TROE/ 2.897e+00 1.87e+03  3.32e+03  3.68e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (1.78e-46, 'cm^3/(mol*s)'),
        n = 18.59,
        Ea = (-27.4138, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (1.2e+09, 'cm^6/(mol^2*s)'),
        n = 1.014,
        Ea = (11947.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 2.897,
    T3 = (1873.28, 'K'),
    T1 = (3323.16, 'K'),
    T2 = (3675, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ch3 + oh <=> hcoh + h2',
 "chemkinKinetics": """
ch3+oh(+M)=hcoh+h2(+M)                              3.000e-11 6.225     -3.126   

    LOW/ 6.390e+08 0.825     -3.098   /
    TROE/ 2.386e+00 806       2.2e+03   4.44e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (3e-11, 'cm^3/(mol*s)'),
        n = 6.225,
        Ea = (-3125.55, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (6.39e+08, 'cm^6/(mol^2*s)'),
        n = 0.82548,
        Ea = (-3097.96, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 2.386,
    T3 = (806.021, 'K'),
    T1 = (2201.7, 'K'),
    T2 = (4440, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hcoh + oh <=> hco + h2o',
 "chemkinKinetics": """
hcoh+oh=hco+h2o                                     2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hcoh + h <=> ch2o + h',
 "chemkinKinetics": """
hcoh+h=ch2o+h                                       2.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hcoh + o <=> co2 + h + h',
 "chemkinKinetics": """
hcoh+o=co2+h+h                                      5.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hcoh + o <=> co + oh + h',
 "chemkinKinetics": """
hcoh+o=co+oh+h                                      3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hcoh + o2 <=> co2 + h + oh',
 "chemkinKinetics": """
hcoh+o2=co2+h+oh                                    5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hcoh + o2 <=> co2 + h2o',
 "chemkinKinetics": """
hcoh+o2=co2+h2o                                     3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3 + ho2 <=> ch3o + oh',
 "chemkinKinetics": """
ch3+ho2=ch3o+oh                                     1.000e+12 0.269     -0.688   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+12, 'cm^3/(mol*s)'),
    n = 0.269,
    Ea = (-687.5, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ch3 + ho2 <=> ch4 + o2',
 "chemkinKinetics": """
ch3+ho2=ch4+o2                                      1.160e+05 2.230     -3.022   
""",
 "rmgPyKinetics": Arrhenius(
    A = (116000, 'cm^3/(mol*s)'),
    n = 2.23,
    Ea = (-3022, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3 + o <=> ch2o + h',
 "chemkinKinetics": """
ch3+o=ch2o+h                                        5.540e+13 0.050     -0.136   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.54e+13, 'cm^3/(mol*s)'),
    n = 0.05,
    Ea = (-136, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3 + o2 <=> ch3o + o',
 "chemkinKinetics": """
ch3+o2=ch3o+o                                       7.546e+12 0.000     28.320   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.546e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (28320, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3 + o2 <=> ch2o + oh',
 "chemkinKinetics": """
ch3+o2=ch2o+oh                                      2.641e+00 3.283     8.105    
""",
 "rmgPyKinetics": Arrhenius(A=(2.641, 'cm^3/(mol*s)'), n=3.283, Ea=(8105, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3 + o2 <=> ch3o2',
 "chemkinKinetics": """
ch3+o2(+M)=ch3o2(+M)                                7.812e+09 0.900     0.000    

    LOW/ 6.850e+24 -3.000    0.000    /
    TROE/ 6.000e-01 1e+03     70        1.7e+03  /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(7.812e+09, 'cm^3/(mol*s)'), n=0.9, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(A=(6.85e+24, 'cm^6/(mol^2*s)'), n=-3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    alpha = 0.6,
    T3 = (1000, 'K'),
    T1 = (70, 'K'),
    T2 = (1700, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3o2 + ch2o <=> ch3o2h + hco',
 "chemkinKinetics": """
ch3o2+ch2o=ch3o2h+hco                               1.990e+12 0.000     11.660   
""",
 "rmgPyKinetics": Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch4 + ch3o2 <=> ch3 + ch3o2h',
 "chemkinKinetics": """
ch4+ch3o2=ch3+ch3o2h                                6.400e-01 3.770     17.810   
""",
 "rmgPyKinetics": Arrhenius(A=(0.64, 'cm^3/(mol*s)'), n=3.77, Ea=(17810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + ch3o2 <=> ch2oh + ch3o2h',
 "chemkinKinetics": """
ch3oh+ch3o2=ch2oh+ch3o2h                            1.810e+12 0.000     13.710   
""",
 "rmgPyKinetics": Arrhenius(A=(1.81e+12, 'cm^3/(mol*s)'), n=0, Ea=(13710, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + ch3 <=> ch3o + ch3o',
 "chemkinKinetics": """
ch3o2+ch3=ch3o+ch3o                                 2.540e+12 0.000     -1.411   
""",
 "rmgPyKinetics": Arrhenius(A=(2.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + ho2 <=> ch3o2h + o2',
 "chemkinKinetics": """
ch3o2+ho2=ch3o2h+o2                                 2.470e+11 0.000     -1.570   
""",
 "rmgPyKinetics": Arrhenius(A=(2.47e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1570, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + ch3o2 => ch2o + ch3oh + o2',
 "chemkinKinetics": """
ch3o2+ch3o2=>ch2o+ch3oh+o2                          3.110e+14 -1.610    -1.051   
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.11e+14, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (-1051, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3o2 + ch3o2 => o2 + ch3o + ch3o',
 "chemkinKinetics": """
ch3o2+ch3o2=>o2+ch3o+ch3o                           1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ch3o2 + h <=> ch3o + oh',
 "chemkinKinetics": """
ch3o2+h=ch3o+oh                                     9.600e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + o <=> ch3o + o2',
 "chemkinKinetics": """
ch3o2+o=ch3o+o2                                     3.600e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3o2 + oh <=> ch3oh + o2',
 "chemkinKinetics": """
ch3o2+oh=ch3oh+o2                                   6.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3o2h <=> ch3o + oh',
 "chemkinKinetics": """
ch3o2h=ch3o+oh                                      6.310e+14 0.000     42.300   
""",
 "rmgPyKinetics": Arrhenius(A=(6.31e+14, 's^-1'), n=0, Ea=(42300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch2(s) + n2 <=> ch2 + n2',
 "chemkinKinetics": """
ch2(s)+n2=ch2+n2                                    1.500e+13 0.000     0.600    
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2(s) + ar <=> ch2 + ar',
 "chemkinKinetics": """
ch2(s)+ar=ch2+ar                                    9.000e+12 0.000     0.600    
""",
 "rmgPyKinetics": Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2(s) + h <=> ch + h2',
 "chemkinKinetics": """
ch2(s)+h=ch+h2                                      3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2(s) + o <=> co + h2',
 "chemkinKinetics": """
ch2(s)+o=co+h2                                      1.500e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2(s) + o <=> hco + h',
 "chemkinKinetics": """
ch2(s)+o=hco+h                                      1.500e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2(s) + oh <=> ch2o + h',
 "chemkinKinetics": """
ch2(s)+oh=ch2o+h                                    3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2(s) + h2 <=> ch3 + h',
 "chemkinKinetics": """
ch2(s)+h2=ch3+h                                     7.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2(s) + o2 <=> ch2 + o2',
 "chemkinKinetics": """
ch2(s)+o2=ch2+o2                                    1.500e+13 0.000     0.600    
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2(s) + h2o <=> ch2 + h2o',
 "chemkinKinetics": """
ch2(s)+h2o=ch2+h2o                                  3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2(s) + co <=> ch2 + co',
 "chemkinKinetics": """
ch2(s)+co=ch2+co                                    9.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2(s) + co2 <=> ch2 + co2',
 "chemkinKinetics": """
ch2(s)+co2=ch2+co2                                  7.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2(s) + co2 <=> ch2o + co',
 "chemkinKinetics": """
ch2(s)+co2=ch2o+co                                  1.400e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2 + h <=> ch3',
 "chemkinKinetics": """
ch2+h(+M)=ch3(+M)                                   2.500e+16 -0.800    0.000    
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ he/0.70/ 
    LOW/ 3.200e+27 -3.140    1.230    /
    TROE/ 6.800e-01 78        2e+03     5.59e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(2.5e+16, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (3.2e+27, 'cm^6/(mol^2*s)'),
        n = -3.14,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.68,
    T3 = (78, 'K'),
    T1 = (1995, 'K'),
    T2 = (5590, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.7,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2 + o2 <=> ch2o + o',
 "chemkinKinetics": """
ch2+o2=ch2o+o                                       1.260e+06 2.420     1.604    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.26e+06, 'cm^3/(mol*s)'),
    n = 2.4202,
    Ea = (1604, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2 + o2 <=> co2 + h2',
 "chemkinKinetics": """
ch2+o2=co2+h2                                       2.050e+09 0.993     -0.269   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.05e+09, 'cm^3/(mol*s)'),
    n = 0.9929,
    Ea = (-269.4, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2 + o => co + h + h',
 "chemkinKinetics": """
ch2+o=>co+h+h                                       5.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2 + h <=> ch + h2',
 "chemkinKinetics": """
ch2+h=ch+h2                                         1.000e+18 -1.560    0.000    
DUPLICATE
""",
 "rmgPyKinetics": Arrhenius(A=(1e+18, 'cm^3/(mol*s)'), n=-1.56, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2 + oh <=> ch + h2o',
 "chemkinKinetics": """
ch2+oh=ch+h2o                                       1.130e+07 2.000     3.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.13e+07, 'cm^3/(mol*s)'), n=2, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch + o2 <=> hco + o',
 "chemkinKinetics": """
ch+o2=hco+o                                         3.300e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c + oh <=> co + h',
 "chemkinKinetics": """
c+oh=co+h                                           5.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c + o2 <=> co + o',
 "chemkinKinetics": """
c+o2=co+o                                           5.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch + h <=> c + h2',
 "chemkinKinetics": """
ch+h=c+h2                                           1.100e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch + o <=> co + h',
 "chemkinKinetics": """
ch+o=co+h                                           5.700e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch + oh <=> hco + h',
 "chemkinKinetics": """
ch+oh=hco+h                                         3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2 + h <=> ch + h2',
 "chemkinKinetics": """
ch2+h=ch+h2                                         2.700e+11 0.670     25.700   
DUPLICATE
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.7e+11, 'cm^3/(mol*s)'),
    n = 0.67,
    Ea = (25700, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch + h2o <=> h + ch2o',
 "chemkinKinetics": """
ch+h2o=h+ch2o                                       1.713e+13 0.000     -0.755   
""",
 "rmgPyKinetics": Arrhenius(A=(1.713e+13, 'cm^3/(mol*s)'), n=0, Ea=(-755, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch + co2 <=> hco + co',
 "chemkinKinetics": """
ch+co2=hco+co                                       1.700e+12 0.000     0.685    
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(685, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3 + ch3 <=> c2h6',
 "chemkinKinetics": """
ch3+ch3(+M)=c2h6(+M)                                2.277e+15 -0.690    0.175    
co2/3.00/ co/2.00/ h2o/5.00/ 
    LOW/ 8.054e+31 -3.750    0.982    /
    TROE/ 0.000e+00 570       0         1e+30    /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (2.277e+15, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (174.86, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (8.054e+31, 'cm^6/(mol^2*s)'),
        n = -3.75,
        Ea = (981.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    T3 = (570, 'K'),
    T1 = (0, 'K'),
    T2 = (1e+30, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 2,
        Molecule(SMILES='O=C=O'): 3,
        Molecule(SMILES='O'): 5,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h5 + h <=> c2h6',
 "chemkinKinetics": """
c2h5+h(+M)=c2h6(+M)                                 5.210e+17 -0.990    1.580    
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ he/0.70/ 
    LOW/ 1.990e+41 -7.080    6.685    /
    TROE/ 8.420e-01 125       2.22e+03  6.88e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (5.21e+17, 'cm^3/(mol*s)'),
        n = -0.99,
        Ea = (1580, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (1.99e+41, 'cm^6/(mol^2*s)'),
        n = -7.08,
        Ea = (6685, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.842,
    T3 = (125, 'K'),
    T1 = (2219, 'K'),
    T2 = (6882, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.7,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h6 + h <=> c2h5 + h2',
 "chemkinKinetics": """
c2h6+h=c2h5+h2                                      1.150e+08 1.900     7.530    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.15e+08, 'cm^3/(mol*s)'),
    n = 1.9,
    Ea = (7530, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h6 + o <=> c2h5 + oh',
 "chemkinKinetics": """
c2h6+o=c2h5+oh                                      3.550e+06 2.400     5.830    
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.55e+06, 'cm^3/(mol*s)'),
    n = 2.4,
    Ea = (5830, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h6 + oh <=> c2h5 + h2o',
 "chemkinKinetics": """
c2h6+oh=c2h5+h2o                                    1.480e+07 1.900     0.950    
""",
 "rmgPyKinetics": Arrhenius(A=(1.48e+07, 'cm^3/(mol*s)'), n=1.9, Ea=(950, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h6 + o2 <=> c2h5 + ho2',
 "chemkinKinetics": """
c2h6+o2=c2h5+ho2                                    6.030e+13 0.000     51.870   
""",
 "rmgPyKinetics": Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(51870, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h6 + ch3 <=> c2h5 + ch4',
 "chemkinKinetics": """
c2h6+ch3=c2h5+ch4                                   5.480e-01 4.000     8.280    
""",
 "rmgPyKinetics": Arrhenius(A=(0.548, 'cm^3/(mol*s)'), n=4, Ea=(8280, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h6 + ho2 <=> c2h5 + h2o2',
 "chemkinKinetics": """
c2h6+ho2=c2h5+h2o2                                  3.460e+01 3.610     16.920   
""",
 "rmgPyKinetics": Arrhenius(A=(34.6, 'cm^3/(mol*s)'), n=3.61, Ea=(16920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h6 + ch3o2 <=> c2h5 + ch3o2h',
 "chemkinKinetics": """
c2h6+ch3o2=c2h5+ch3o2h                              1.940e+01 3.640     17.100   
""",
 "rmgPyKinetics": Arrhenius(A=(19.4, 'cm^3/(mol*s)'), n=3.64, Ea=(17100, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h6 + ch3o <=> c2h5 + ch3oh',
 "chemkinKinetics": """
c2h6+ch3o=c2h5+ch3oh                                2.410e+11 0.000     7.090    
""",
 "rmgPyKinetics": Arrhenius(A=(2.41e+11, 'cm^3/(mol*s)'), n=0, Ea=(7090, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h6 + ch <=> c2h5 + ch2',
 "chemkinKinetics": """
c2h6+ch=c2h5+ch2                                    1.100e+14 0.000     -0.260   
""",
 "rmgPyKinetics": Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(-260, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2(s) + c2h6 <=> ch3 + c2h5',
 "chemkinKinetics": """
ch2(s)+c2h6=ch3+c2h5                                1.200e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + h <=> c2h5',
 "chemkinKinetics": """
c2h4+h(+M)=c2h5(+M)                                 5.270e+09 1.183     1.273    
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ 
    LOW/ 2.027e+40 -6.642    5.769    /
    TROE/ 9.760e-01 9.99e+09  384       3.29e+09 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (5.27e+09, 'cm^3/(mol*s)'),
        n = 1.183,
        Ea = (1272.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (2.027e+40, 'cm^6/(mol^2*s)'),
        n = -6.642,
        Ea = (5769, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.976,
    T3 = (9.99e+09, 'K'),
    T1 = (384, 'K'),
    T2 = (3.29e+09, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'h2 + ch3o2 <=> h + ch3o2h',
 "chemkinKinetics": """
h2+ch3o2=h+ch3o2h                                   1.500e+14 0.000     26.030   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h2 + c2h5o2 <=> h + c2h5o2h',
 "chemkinKinetics": """
h2+c2h5o2=h+c2h5o2h                                 1.500e+14 0.000     26.030   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + c2h4 <=> c2h5 + c2h3',
 "chemkinKinetics": """
c2h4+c2h4=c2h5+c2h3                                 4.820e+14 0.000     71.530   
""",
 "rmgPyKinetics": Arrhenius(A=(4.82e+14, 'cm^3/(mol*s)'), n=0, Ea=(71530, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3 + c2h5 <=> ch4 + c2h4',
 "chemkinKinetics": """
ch3+c2h5=ch4+c2h4                                   1.180e+04 2.450     -2.921   
""",
 "rmgPyKinetics": Arrhenius(A=(11800, 'cm^3/(mol*s)'), n=2.45, Ea=(-2921, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3 + ch3 <=> c2h5 + h',
 "chemkinKinetics": """
ch3+ch3(+M)=c2h5+h(+M)                              3.802e-07 4.838     7.710    

    LOW/ 4.989e+12 0.099     10.600   /
""",
 "rmgPyKinetics": Lindemann(
    arrheniusHigh = Arrhenius(
        A = (3.802e-07, 'cm^3/(mol*s)'),
        n = 4.838,
        Ea = (7710, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (4.989e+12, 'cm^6/(mol^2*s)'),
        n = 0.099,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    efficiencies = {},
    comment = 'Warning: SRI parameters from chemkin file ignored on import. ',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h5 + h <=> c2h4 + h2',
 "chemkinKinetics": """
c2h5+h=c2h4+h2                                      2.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h5 + o <=> ch3cho + h',
 "chemkinKinetics": """
c2h5+o=ch3cho+h                                     1.100e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h5 + ho2 <=> c2h5o + oh',
 "chemkinKinetics": """
c2h5+ho2=c2h5o+oh                                   1.100e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + c2h5 <=> ch3o + c2h5o',
 "chemkinKinetics": """
ch3o2+c2h5=ch3o+c2h5o                               8.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c2h5o + o2 <=> ch3cho + ho2',
 "chemkinKinetics": """
c2h5o+o2=ch3cho+ho2                                 4.280e+10 0.000     1.097    
""",
 "rmgPyKinetics": Arrhenius(A=(4.28e+10, 'cm^3/(mol*s)'), n=0, Ea=(1097, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3 + ch2o <=> c2h5o',
 "chemkinKinetics": """
ch3+ch2o=c2h5o                                      3.000e+11 0.000     6.336    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(6336, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3cho + h <=> c2h5o',
 "chemkinKinetics": """
ch3cho+h=c2h5o                                      4.610e+07 1.710     7.090    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.61e+07, 'cm^3/(mol*s)'),
    n = 1.71,
    Ea = (7090, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h5o2 + ch2o <=> c2h5o2h + hco',
 "chemkinKinetics": """
c2h5o2+ch2o=c2h5o2h+hco                             1.990e+12 0.000     11.660   
""",
 "rmgPyKinetics": Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch4 + c2h5o2 <=> ch3 + c2h5o2h',
 "chemkinKinetics": """
ch4+c2h5o2=ch3+c2h5o2h                              1.810e+11 0.000     18.480   
""",
 "rmgPyKinetics": Arrhenius(A=(1.81e+11, 'cm^3/(mol*s)'), n=0, Ea=(18480, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + c2h5o2 <=> ch2oh + c2h5o2h',
 "chemkinKinetics": """
ch3oh+c2h5o2=ch2oh+c2h5o2h                          1.810e+12 0.000     13.710   
""",
 "rmgPyKinetics": Arrhenius(A=(1.81e+12, 'cm^3/(mol*s)'), n=0, Ea=(13710, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5o2 + ho2 <=> c2h5o2h + o2',
 "chemkinKinetics": """
c2h5o2+ho2=c2h5o2h+o2                               1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h6 + c2h5o2 <=> c2h5 + c2h5o2h',
 "chemkinKinetics": """
c2h6+c2h5o2=c2h5+c2h5o2h                            8.600e+00 3.760     17.200   
""",
 "rmgPyKinetics": Arrhenius(A=(8.6, 'cm^3/(mol*s)'), n=3.76, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5o2h <=> c2h5o + oh',
 "chemkinKinetics": """
c2h5o2h=c2h5o+oh                                    6.310e+14 0.000     42.300   
""",
 "rmgPyKinetics": Arrhenius(A=(6.31e+14, 's^-1'), n=0, Ea=(42300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h5 + o2 <=> c2h5o2',
 "chemkinKinetics": """
c2h5+o2=c2h5o2                                      1.000e+00 0.000     0.000    
    PLOG/ 0.040     3.398e+53 -13.900   9.279    /
    PLOG/ 1.000     9.362e+59 -15.280   14.240   /
    PLOG/ 10.000    1.262e+60 -14.910   16.240   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.04, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (3.398e+53, 'cm^3/(mol*s)'),
            n = -13.9,
            Ea = (9279, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (9.362e+59, 'cm^3/(mol*s)'),
            n = -15.28,
            Ea = (14240, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.262e+60, 'cm^3/(mol*s)'),
            n = -14.91,
            Ea = (16240, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h5 + o2 <=> c2h4o2h',
 "chemkinKinetics": """
c2h5+o2=c2h4o2h                                     1.000e+00 0.000     0.000    
    PLOG/ 0.040     2.103e+34 -9.010    5.444    /
    PLOG/ 1.000     4.884e+33 -8.310    7.710    /
    PLOG/ 10.000    1.705e+45 -11.490   14.590   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.04, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (2.103e+34, 'cm^3/(mol*s)'),
            n = -9.01,
            Ea = (5444, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.884e+33, 'cm^3/(mol*s)'),
            n = -8.31,
            Ea = (7710, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.705e+45, 'cm^3/(mol*s)'),
            n = -11.49,
            Ea = (14590, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h5 + o2 <=> c2h4 + ho2',
 "chemkinKinetics": """
c2h5+o2=c2h4+ho2                                    1.000e+00 0.000     0.000    
    PLOG/ 0.040     2.094e+09 0.490     -0.391   /
    PLOG/ 1.000     1.843e+07 1.130     -0.721   /
    PLOG/ 10.000    7.561e+14 -1.010    4.749    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.04, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (2.094e+09, 'cm^3/(mol*s)'),
            n = 0.49,
            Ea = (-391.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.843e+07, 'cm^3/(mol*s)'),
            n = 1.13,
            Ea = (-720.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (7.561e+14, 'cm^3/(mol*s)'),
            n = -1.01,
            Ea = (4749, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h5 + o2 <=> c2h4 + ho2',
 "chemkinKinetics": """
c2h5+o2=c2h4+ho2                                    6.609e+00 3.510     14.160   
""",
 "rmgPyKinetics": Arrhenius(A=(6.609, 'cm^3/(mol*s)'), n=3.51, Ea=(14160, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h5 + o2 <=> c2h4o1-2 + oh',
 "chemkinKinetics": """
c2h5+o2=c2h4o1-2+oh                                 1.000e+00 0.000     0.000    
    PLOG/ 0.040     1.303e+03 1.930     -0.503   /
    PLOG/ 1.000     2.438e+02 2.180     -0.062   /
    PLOG/ 10.000    4.621e+09 0.150     5.409    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.04, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(1303, 'cm^3/(mol*s)'), n=1.93, Ea=(-502.7, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(
            A = (243.8, 'cm^3/(mol*s)'),
            n = 2.18,
            Ea = (-62.49, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.621e+09, 'cm^3/(mol*s)'),
            n = 0.15,
            Ea = (5409, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h5 + o2 <=> ch3cho + oh',
 "chemkinKinetics": """
c2h5+o2=ch3cho+oh                                   1.000e+00 0.000     0.000    
    PLOG/ 0.040     4.908e-06 4.760     0.254    /
    PLOG/ 1.000     6.803e-02 3.570     2.643    /
    PLOG/ 10.000    8.265e+02 2.410     5.285    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.04, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (4.908e-06, 'cm^3/(mol*s)'),
            n = 4.76,
            Ea = (254.3, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (0.06803, 'cm^3/(mol*s)'),
            n = 3.57,
            Ea = (2643, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(A=(826.5, 'cm^3/(mol*s)'), n=2.41, Ea=(5285, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4o2h <=> c2h5o2',
 "chemkinKinetics": """
c2h4o2h=c2h5o2                                      1.000e+00 0.000     0.000    
    PLOG/ 0.040     2.653e-16 6.960     2.396    /
    PLOG/ 1.000     1.064e+41 -10.100   26.030   /
    PLOG/ 10.000    1.203e+36 -8.130    27.020   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.04, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(2.653e-16, 's^-1'), n=6.96, Ea=(2396, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.064e+41, 's^-1'), n=-10.1, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.203e+36, 's^-1'), n=-8.13, Ea=(27020, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c2h5o2 <=> ch3cho + oh',
 "chemkinKinetics": """
c2h5o2=ch3cho+oh                                    1.000e+00 0.000     0.000    
    PLOG/ 0.040     1.237e+35 -9.420    36.360   /
    PLOG/ 1.000     1.687e+36 -9.220    38.700   /
    PLOG/ 10.000    2.520e+41 -10.200   43.710   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.04, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(1.237e+35, 's^-1'), n=-9.42, Ea=(36360, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.687e+36, 's^-1'), n=-9.22, Ea=(38700, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.52e+41, 's^-1'), n=-10.2, Ea=(43710, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h5o2 <=> c2h4 + ho2',
 "chemkinKinetics": """
c2h5o2=c2h4+ho2                                     1.000e+00 0.000     0.000    
    PLOG/ 0.040     1.782e+32 -7.100    32.840   /
    PLOG/ 1.000     2.701e+37 -8.470    35.840   /
    PLOG/ 10.000    1.980e+38 -8.460    37.900   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.04, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(1.782e+32, 's^-1'), n=-7.1, Ea=(32840, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.701e+37, 's^-1'), n=-8.47, Ea=(35840, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.98e+38, 's^-1'), n=-8.46, Ea=(37900, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'c2h5o2 <=> c2h4o1-2 + oh',
 "chemkinKinetics": """
c2h5o2=c2h4o1-2+oh                                  1.000e+00 0.000     0.000    
    PLOG/ 0.040     5.778e+45 -11.900   4.112    /
    PLOG/ 1.000     1.916e+43 -10.750   42.400   /
    PLOG/ 10.000    3.965e+43 -10.460   45.580   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.04, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(5.778e+45, 's^-1'), n=-11.9, Ea=(4112, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.916e+43, 's^-1'), n=-10.75, Ea=(42400, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(3.965e+43, 's^-1'), n=-10.46, Ea=(45580, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4o2h <=> c2h4o1-2 + oh',
 "chemkinKinetics": """
c2h4o2h=c2h4o1-2+oh                                 1.000e+00 0.000     0.000    
    PLOG/ 0.040     8.959e+38 -9.400    20.660   /
    PLOG/ 1.000     1.224e+37 -8.320    21.460   /
    PLOG/ 10.000    8.848e+30 -6.080    20.660   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.04, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(8.959e+38, 's^-1'), n=-9.4, Ea=(20660, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.224e+37, 's^-1'), n=-8.32, Ea=(21460, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(8.848e+30, 's^-1'), n=-6.08, Ea=(20660, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c2h4o2h <=> c2h4 + ho2',
 "chemkinKinetics": """
c2h4o2h=c2h4+ho2                                    1.000e+00 0.000     0.000    
    PLOG/ 0.040     3.918e+40 -10.200   22.250   /
    PLOG/ 1.000     6.825e+40 -9.610    23.840   /
    PLOG/ 10.000    3.980e+34 -7.250    23.250   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.04, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(3.918e+40, 's^-1'), n=-10.2, Ea=(22250, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(6.825e+40, 's^-1'), n=-9.61, Ea=(23840, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(3.98e+34, 's^-1'), n=-7.25, Ea=(23250, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h4o2h <=> ch3cho + oh',
 "chemkinKinetics": """
c2h4o2h=ch3cho+oh                                   1.000e+00 0.000     0.000    
    PLOG/ 0.040     5.819e+26 -7.970    20.860   /
    PLOG/ 1.000     5.520e+34 -9.880    26.230   /
    PLOG/ 10.000    1.188e+34 -9.020    29.210   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.04, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(5.819e+26, 's^-1'), n=-7.97, Ea=(20860, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.52e+34, 's^-1'), n=-9.88, Ea=(26230, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.188e+34, 's^-1'), n=-9.02, Ea=(29210, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4o1-2 <=> ch3 + hco',
 "chemkinKinetics": """
c2h4o1-2=ch3+hco                                    3.630e+13 0.000     57.200   
""",
 "rmgPyKinetics": Arrhenius(A=(3.63e+13, 's^-1'), n=0, Ea=(57200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4o1-2 <=> ch3cho',
 "chemkinKinetics": """
c2h4o1-2=ch3cho                                     7.407e+12 0.000     53.800   
""",
 "rmgPyKinetics": Arrhenius(A=(7.407e+12, 's^-1'), n=0, Ea=(53800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4o1-2 + oh <=> c2h3o1-2 + h2o',
 "chemkinKinetics": """
c2h4o1-2+oh=c2h3o1-2+h2o                            1.780e+13 0.000     3.610    
""",
 "rmgPyKinetics": Arrhenius(A=(1.78e+13, 'cm^3/(mol*s)'), n=0, Ea=(3610, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4o1-2 + h <=> c2h3o1-2 + h2',
 "chemkinKinetics": """
c2h4o1-2+h=c2h3o1-2+h2                              8.000e+13 0.000     9.680    
""",
 "rmgPyKinetics": Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(9680, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4o1-2 + ho2 <=> c2h3o1-2 + h2o2',
 "chemkinKinetics": """
c2h4o1-2+ho2=c2h3o1-2+h2o2                          1.130e+13 0.000     30.430   
""",
 "rmgPyKinetics": Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4o1-2 + ch3o2 <=> c2h3o1-2 + ch3o2h',
 "chemkinKinetics": """
c2h4o1-2+ch3o2=c2h3o1-2+ch3o2h                      1.130e+13 0.000     30.430   
""",
 "rmgPyKinetics": Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4o1-2 + c2h5o2 <=> c2h3o1-2 + c2h5o2h',
 "chemkinKinetics": """
c2h4o1-2+c2h5o2=c2h3o1-2+c2h5o2h                    1.130e+13 0.000     30.430   
""",
 "rmgPyKinetics": Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4o1-2 + ch3 <=> c2h3o1-2 + ch4',
 "chemkinKinetics": """
c2h4o1-2+ch3=c2h3o1-2+ch4                           1.070e+12 0.000     11.830   
""",
 "rmgPyKinetics": Arrhenius(A=(1.07e+12, 'cm^3/(mol*s)'), n=0, Ea=(11830, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4o1-2 + ch3o <=> c2h3o1-2 + ch3oh',
 "chemkinKinetics": """
c2h4o1-2+ch3o=c2h3o1-2+ch3oh                        1.200e+11 0.000     6.750    
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(6750, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3o1-2 <=> ch3co',
 "chemkinKinetics": """
c2h3o1-2=ch3co                                      8.500e+14 0.000     14.000   
""",
 "rmgPyKinetics": Arrhenius(A=(8.5e+14, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3o1-2 <=> ch2cho',
 "chemkinKinetics": """
c2h3o1-2=ch2cho                                     1.000e+14 0.000     14.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Intra_R_Add_Endocyclic',  ],
},

{
 "reaction": 'ch3cho <=> ch3 + hco',
 "chemkinKinetics": """
ch3cho(+M)=ch3+hco(+M)                              2.450e+22 -1.740    86.355   

    LOW/ 1.030e+59 -11.300   95.912   /
    TROE/ 2.490e-03 718       6.09      3.78e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(2.45e+22, 's^-1'), n=-1.74, Ea=(86355, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.02976e+59, 'cm^3/(mol*s)'),
        n = -11.3,
        Ea = (95912.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.00249,
    T3 = (718.119, 'K'),
    T1 = (6.08949, 'K'),
    T2 = (3780.02, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3cho <=> ch4 + co',
 "chemkinKinetics": """
ch3cho(+M)=ch4+co(+M)                               2.720e+21 -1.740    86.355   

    LOW/ 1.144e+58 -11.300   95.912   /
    TROE/ 2.490e-03 718       6.09      3.78e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(2.72e+21, 's^-1'), n=-1.74, Ea=(86355, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.14418e+58, 'cm^3/(mol*s)'),
        n = -11.3,
        Ea = (95912.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.00249,
    T3 = (718.119, 'K'),
    T1 = (6.08949, 'K'),
    T2 = (3780.02, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3cho + h <=> ch3co + h2',
 "chemkinKinetics": """
ch3cho+h=ch3co+h2                                   1.310e+05 2.580     1.220    
""",
 "rmgPyKinetics": Arrhenius(A=(131000, 'cm^3/(mol*s)'), n=2.58, Ea=(1220, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3cho + h <=> ch2cho + h2',
 "chemkinKinetics": """
ch3cho+h=ch2cho+h2                                  2.720e+03 3.100     5.210    
""",
 "rmgPyKinetics": Arrhenius(A=(2720, 'cm^3/(mol*s)'), n=3.1, Ea=(5210, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3cho + o <=> ch3co + oh',
 "chemkinKinetics": """
ch3cho+o=ch3co+oh                                   5.940e+12 0.000     1.868    
""",
 "rmgPyKinetics": Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3cho + oh <=> ch3co + h2o',
 "chemkinKinetics": """
ch3cho+oh=ch3co+h2o                                 3.370e+12 0.000     -0.619   
""",
 "rmgPyKinetics": Arrhenius(A=(3.37e+12, 'cm^3/(mol*s)'), n=0, Ea=(-619, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3cho + o2 <=> ch3co + ho2',
 "chemkinKinetics": """
ch3cho+o2=ch3co+ho2                                 3.010e+13 0.000     39.150   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(39150, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3cho + ch3 <=> ch3co + ch4',
 "chemkinKinetics": """
ch3cho+ch3=ch3co+ch4                                7.080e-04 4.580     1.966    
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.000708, 'cm^3/(mol*s)'),
    n = 4.58,
    Ea = (1966, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3cho + ho2 <=> ch3co + h2o2',
 "chemkinKinetics": """
ch3cho+ho2=ch3co+h2o2                               3.010e+12 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + ch3cho <=> ch3o2h + ch3co',
 "chemkinKinetics": """
ch3o2+ch3cho=ch3o2h+ch3co                           3.010e+12 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3cho + ch3co3 <=> ch3co + ch3co3h',
 "chemkinKinetics": """
ch3cho+ch3co3=ch3co+ch3co3h                         3.010e+12 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3cho + oh <=> ch3 + hocho',
 "chemkinKinetics": """
ch3cho+oh=ch3+hocho                                 3.000e+15 -1.076    0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+15, 'cm^3/(mol*s)'), n=-1.076, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3cho + oh <=> ch2cho + h2o',
 "chemkinKinetics": """
ch3cho+oh=ch2cho+h2o                                1.720e+05 2.400     0.815    
""",
 "rmgPyKinetics": Arrhenius(A=(172000, 'cm^3/(mol*s)'), n=2.4, Ea=(815, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3co <=> ch3 + co',
 "chemkinKinetics": """
ch3co(+M)=ch3+co(+M)                                1.070e+12 0.630     16.900   

    LOW/ 5.650e+18 -0.970    14.600   /
    TROE/ 6.290e-01 8.73e+09  5.52      7.6e+07  /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.07e+12, 's^-1'), n=0.63, Ea=(16900, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (5.65e+18, 'cm^3/(mol*s)'),
        n = -0.97,
        Ea = (14600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.629,
    T3 = (8.73e+09, 'K'),
    T1 = (5.52, 'K'),
    T2 = (7.6e+07, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3co + h <=> ch2co + h2',
 "chemkinKinetics": """
ch3co+h=ch2co+h2                                    2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3co + o <=> ch2co + oh',
 "chemkinKinetics": """
ch3co+o=ch2co+oh                                    2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3co + ch3 <=> ch2co + ch4',
 "chemkinKinetics": """
ch3co+ch3=ch2co+ch4                                 5.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3co + o2 <=> ch3co3',
 "chemkinKinetics": """
ch3co+o2=ch3co3                                     1.200e+11 0.000     -1.100   
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3co3 + ho2 <=> ch3co3h + o2',
 "chemkinKinetics": """
ch3co3+ho2=ch3co3h+o2                               1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h2o2 + ch3co3 <=> ho2 + ch3co3h',
 "chemkinKinetics": """
h2o2+ch3co3=ho2+ch3co3h                             2.410e+12 0.000     9.936    
""",
 "rmgPyKinetics": Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(9936, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch4 + ch3co3 <=> ch3 + ch3co3h',
 "chemkinKinetics": """
ch4+ch3co3=ch3+ch3co3h                              1.810e+11 0.000     18.480   
""",
 "rmgPyKinetics": Arrhenius(A=(1.81e+11, 'cm^3/(mol*s)'), n=0, Ea=(18480, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2o + ch3co3 <=> hco + ch3co3h',
 "chemkinKinetics": """
ch2o+ch3co3=hco+ch3co3h                             1.990e+12 0.000     11.660   
""",
 "rmgPyKinetics": Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h6 + ch3co3 <=> c2h5 + ch3co3h',
 "chemkinKinetics": """
c2h6+ch3co3=c2h5+ch3co3h                            1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3co3h <=> ch3co2 + oh',
 "chemkinKinetics": """
ch3co3h=ch3co2+oh                                   5.010e+14 0.000     40.150   
""",
 "rmgPyKinetics": Arrhenius(A=(5.01e+14, 's^-1'), n=0, Ea=(40150, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3co2 <=> ch3 + co2',
 "chemkinKinetics": """
ch3co2+M=ch3+co2+M                                  4.400e+15 0.000     10.500   

""",
 "rmgPyKinetics": ThirdBody(
    arrheniusLow = Arrhenius(A=(4.4e+15, 'cm^3/(mol*s)'), n=0, Ea=(10500, 'cal/mol'), T0=(1, 'K')),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2cho <=> ch2co + h',
 "chemkinKinetics": """
ch2cho(+M)=ch2co+h(+M)                              1.430e+15 -0.150    45.600   

    LOW/ 6.000e+29 -3.800    43.424   /
    TROE/ 9.850e-01 393       9.8e+09   5e+09    /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.43e+15, 's^-1'), n=-0.15, Ea=(45600, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (6e+29, 'cm^3/(mol*s)'),
        n = -3.8,
        Ea = (43423.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.985,
    T3 = (393, 'K'),
    T1 = (9.8e+09, 'K'),
    T2 = (5e+09, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2cho <=> ch3 + co',
 "chemkinKinetics": """
ch2cho(+M)=ch3+co(+M)                               2.930e+12 0.290     40.300   

    LOW/ 9.520e+33 -5.070    41.300   /
    TROE/ 7.130e-17 1.15e+03  4.99e+09  1.79e+09 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(2.93e+12, 's^-1'), n=0.29, Ea=(40300, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (9.52e+33, 'cm^3/(mol*s)'),
        n = -5.07,
        Ea = (41300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 7.13e-17,
    T3 = (1150, 'K'),
    T1 = (4.99e+09, 'K'),
    T2 = (1.79e+09, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2cho + o2 <=> o2ch2cho',
 "chemkinKinetics": """
ch2cho+o2=o2ch2cho                                  1.000e+00 0.000     0.000    
    PLOG/ 0.010     1.580e+77 -21.900   19.350   /
    PLOG/ 0.100     3.880e+69 -18.840   19.240   /
    PLOG/ 1.000     7.800e+59 -15.400   17.650   /
    PLOG/ 10.000    3.050e+50 -12.200   15.630   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.1, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (1.58e+77, 'cm^3/(mol*s)'),
            n = -21.9,
            Ea = (19350, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.88e+69, 'cm^3/(mol*s)'),
            n = -18.84,
            Ea = (19240, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (7.8e+59, 'cm^3/(mol*s)'),
            n = -15.4,
            Ea = (17650, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.05e+50, 'cm^3/(mol*s)'),
            n = -12.2,
            Ea = (15630, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2cho + o2 <=> ch2co + ho2',
 "chemkinKinetics": """
ch2cho+o2=ch2co+ho2                                 1.000e+00 0.000     0.000    
    PLOG/ 0.010     1.880e+05 2.370     23.730   /
    PLOG/ 0.100     1.880e+05 2.370     27.370   /
    PLOG/ 1.000     2.510e+05 2.330     23.800   /
    PLOG/ 10.000    7.050e+07 1.630     25.290   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.1, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (188000, 'cm^3/(mol*s)'),
            n = 2.37,
            Ea = (23730, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (188000, 'cm^3/(mol*s)'),
            n = 2.37,
            Ea = (27370, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (251000, 'cm^3/(mol*s)'),
            n = 2.33,
            Ea = (23800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (7.05e+07, 'cm^3/(mol*s)'),
            n = 1.63,
            Ea = (25290, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch2cho + o2 <=> ch2o + co + oh',
 "chemkinKinetics": """
ch2cho+o2=ch2o+co+oh                                1.000e+00 0.000     0.000    
    PLOG/ 0.010     2.680e+17 -1.840    6.530    /
    PLOG/ 0.100     1.520e+20 -2.580    8.980    /
    PLOG/ 1.000     1.650e+19 -2.220    10.340   /
    PLOG/ 10.000    8.953e+13 -0.600    10.120   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.1, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (2.68e+17, 'cm^3/(mol*s)'),
            n = -1.84,
            Ea = (6530, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.52e+20, 'cm^3/(mol*s)'),
            n = -2.58,
            Ea = (8980, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.65e+19, 'cm^3/(mol*s)'),
            n = -2.22,
            Ea = (10340, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (8.953e+13, 'cm^3/(mol*s)'),
            n = -0.6,
            Ea = (10120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2cho + o2 <=> ho2ch2co',
 "chemkinKinetics": """
ch2cho+o2=ho2ch2co                                  1.000e+00 0.000     0.000    
    PLOG/ 0.010     3.640e+65 -21.870   19.020   /
    PLOG/ 0.100     3.640e+58 -19.000   19.090   /
    PLOG/ 1.000     6.650e+48 -15.550   17.460   /
    PLOG/ 10.000    4.800e+38 -12.140   14.960   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.1, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (3.64e+65, 'cm^3/(mol*s)'),
            n = -21.87,
            Ea = (19020, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.64e+58, 'cm^3/(mol*s)'),
            n = -19,
            Ea = (19090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (6.65e+48, 'cm^3/(mol*s)'),
            n = -15.55,
            Ea = (17460, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.8e+38, 'cm^3/(mol*s)'),
            n = -12.14,
            Ea = (14960, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'o2ch2cho <=> ho2ch2co',
 "chemkinKinetics": """
o2ch2cho=ho2ch2co                                   1.000e+00 0.000     0.000    
    PLOG/ 0.010     8.270e+30 -6.650    24.500   /
    PLOG/ 0.100     1.730e+26 -4.990    23.760   /
    PLOG/ 1.000     9.030e+19 -2.920    22.170   /
    PLOG/ 10.000    1.430e+16 -1.670    21.210   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.1, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(8.27e+30, 's^-1'), n=-6.65, Ea=(24500, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.73e+26, 's^-1'), n=-4.99, Ea=(23760, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(9.03e+19, 's^-1'), n=-2.92, Ea=(22170, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.43e+16, 's^-1'), n=-1.67, Ea=(21210, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'o2ch2cho <=> ch2co + ho2',
 "chemkinKinetics": """
o2ch2cho=ch2co+ho2                                  1.000e+00 0.000     0.000    
    PLOG/ 0.010     2.050e+40 -13.310   52.150   /
    PLOG/ 0.100     5.720e+45 -14.000   52.200   /
    PLOG/ 1.000     4.160e+55 -15.760   55.080   /
    PLOG/ 10.000    1.120e+61 -16.040   60.010   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.1, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(2.05e+40, 's^-1'), n=-13.31, Ea=(52150, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.72e+45, 's^-1'), n=-14, Ea=(52200, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.16e+55, 's^-1'), n=-15.76, Ea=(55080, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.12e+61, 's^-1'), n=-16.04, Ea=(60010, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'ho2ch2co <=> co + ch2o + oh',
 "chemkinKinetics": """
ho2ch2co=co+ch2o+oh                                 1.000e+00 0.000     0.000    
    PLOG/ 0.010     2.360e+17 -2.950    8.100    /
    PLOG/ 0.100     2.380e+18 -2.950    8.100    /
    PLOG/ 1.000     2.510e+19 -2.950    8.110    /
    PLOG/ 10.000    4.160e+20 -3.020    8.240    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.1, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(2.36e+17, 's^-1'), n=-2.95, Ea=(8100, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.38e+18, 's^-1'), n=-2.95, Ea=(8100, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.51e+19, 's^-1'), n=-2.95, Ea=(8110, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.16e+20, 's^-1'), n=-3.02, Ea=(8240, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ho2ch2co <=> ch2co + ho2',
 "chemkinKinetics": """
ho2ch2co=ch2co+ho2                                  1.000e+00 0.000     0.000    
    PLOG/ 0.010     1.120e+07 -3.760    21.680   /
    PLOG/ 0.100     1.100e+08 -3.760    21.680   /
    PLOG/ 1.000     9.200e+08 -3.730    21.630   /
    PLOG/ 10.000    2.090e+09 -3.550    21.220   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.1, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(1.12e+07, 's^-1'), n=-3.76, Ea=(21680, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.1e+08, 's^-1'), n=-3.76, Ea=(21680, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(9.2e+08, 's^-1'), n=-3.73, Ea=(21630, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.09e+09, 's^-1'), n=-3.55, Ea=(21220, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2 + co <=> ch2co',
 "chemkinKinetics": """
ch2+co(+M)=ch2co(+M)                                8.100e+11 0.000     0.000    
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ he/0.70/ 
    LOW/ 2.690e+33 -5.110    7.095    /
    TROE/ 5.907e-01 275       1.23e+03  5.18e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(8.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (2.69e+33, 'cm^6/(mol^2*s)'),
        n = -5.11,
        Ea = (7095, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.5907,
    T3 = (275, 'K'),
    T1 = (1226, 'K'),
    T2 = (5185, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.7,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3co <=> ch2co + h',
 "chemkinKinetics": """
ch3co(+M)=ch2co+h(+M)                               9.413e+07 1.917     44.987   

    LOW/ 1.516e+51 -10.270   55.390   /
    TROE/ 6.009e-01 8.1e+09   668       5e+09    /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(9.413e+07, 's^-1'), n=1.9166, Ea=(44987.2, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.516e+51, 'cm^3/(mol*s)'),
        n = -10.27,
        Ea = (55390, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.600884,
    T3 = (8.10341e+09, 'K'),
    T1 = (667.669, 'K'),
    T2 = (5e+09, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2co + h <=> hcco + h2',
 "chemkinKinetics": """
ch2co+h=hcco+h2                                     1.401e+15 -0.171    8.783    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.40068e+15, 'cm^3/(mol*s)'),
    n = -0.17131,
    Ea = (8783.15, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2co + h <=> ch3 + co',
 "chemkinKinetics": """
ch2co+h=ch3+co                                      7.704e+13 -0.171    4.183    
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.70374e+13, 'cm^3/(mol*s)'),
    n = -0.17131,
    Ea = (4183.15, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2co + o <=> ch2 + co2',
 "chemkinKinetics": """
ch2co+o=ch2+co2                                     1.750e+12 0.000     1.350    
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+12, 'cm^3/(mol*s)'), n=0, Ea=(1350, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2co + o <=> hcco + oh',
 "chemkinKinetics": """
ch2co+o=hcco+oh                                     1.000e+13 0.000     8.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2co + oh <=> hcco + h2o',
 "chemkinKinetics": """
ch2co+oh=hcco+h2o                                   1.000e+13 0.000     2.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2co + oh <=> ch2oh + co',
 "chemkinKinetics": """
ch2co+oh=ch2oh+co                                   2.000e+12 0.000     -1.010   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2co + ch3 <=> c2h5 + co',
 "chemkinKinetics": """
ch2co+ch3=c2h5+co                                   4.769e+04 2.312     9.468    
""",
 "rmgPyKinetics": Arrhenius(
    A = (47690, 'cm^3/(mol*s)'),
    n = 2.31199,
    Ea = (9468, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2(s) + ch2co <=> c2h4 + co',
 "chemkinKinetics": """
ch2(s)+ch2co=c2h4+co                                1.600e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hcco + oh => h2 + co + co',
 "chemkinKinetics": """
hcco+oh=>h2+co+co                                   1.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hcco + o => h + co + co',
 "chemkinKinetics": """
hcco+o=>h+co+co                                     8.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hcco + h <=> ch2(s) + co',
 "chemkinKinetics": """
hcco+h=ch2(s)+co                                    1.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hcco + o2 => oh + co + co',
 "chemkinKinetics": """
hcco+o2=>oh+co+co                                   1.910e+11 -0.020    1.020    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.91e+11, 'cm^3/(mol*s)'),
    n = -0.02,
    Ea = (1020, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hcco + o2 => co2 + co + h',
 "chemkinKinetics": """
hcco+o2=>co2+co+h                                   4.780e+12 -0.142    1.150    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.78e+12, 'cm^3/(mol*s)'),
    n = -0.142,
    Ea = (1150, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch + co <=> hcco',
 "chemkinKinetics": """
ch+co+M=hcco+M                                      7.570e+22 -1.900    0.000    

""",
 "rmgPyKinetics": ThirdBody(
    arrheniusLow = Arrhenius(
        A = (7.57e+22, 'cm^6/(mol^2*s)'),
        n = -1.9,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    efficiencies = {},
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch + ch2o <=> h + ch2co',
 "chemkinKinetics": """
ch+ch2o=h+ch2co                                     9.460e+13 0.000     -0.515   
""",
 "rmgPyKinetics": Arrhenius(A=(9.46e+13, 'cm^3/(mol*s)'), n=0, Ea=(-515, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch + hcco <=> co + c2h2',
 "chemkinKinetics": """
ch+hcco=co+c2h2                                     5.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3 + h <=> c2h4',
 "chemkinKinetics": """
c2h3+h(+M)=c2h4(+M)                                 6.080e+12 0.270     0.280    
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ he/0.70/ 
    LOW/ 1.400e+30 -3.860    3.320    /
    TROE/ 7.820e-01 208       2.66e+03  6.1e+03  /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (6.08e+12, 'cm^3/(mol*s)'),
        n = 0.27,
        Ea = (280, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (1.4e+30, 'cm^6/(mol^2*s)'),
        n = -3.86,
        Ea = (3320, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.782,
    T3 = (207.5, 'K'),
    T1 = (2663, 'K'),
    T2 = (6095, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.7,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h4 <=> h2 + h2cc',
 "chemkinKinetics": """
c2h4(+M)=h2+h2cc(+M)                                8.000e+12 0.440     88.770   
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ 
    LOW/ 7.000e+50 -9.310    99.860   /
    TROE/ 7.345e-01 180       1.04e+03  5.42e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(8e+12, 's^-1'), n=0.44, Ea=(88770, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (7e+50, 'cm^3/(mol*s)'),
        n = -9.31,
        Ea = (99860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.7345,
    T3 = (180, 'K'),
    T1 = (1035, 'K'),
    T2 = (5417, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4 + h <=> c2h3 + h2',
 "chemkinKinetics": """
c2h4+h=c2h3+h2                                      5.070e+07 1.930     12.950   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.07e+07, 'cm^3/(mol*s)'),
    n = 1.93,
    Ea = (12950, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + o <=> ch3 + hco',
 "chemkinKinetics": """
c2h4+o=ch3+hco                                      6.775e+06 1.880     0.183    
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.775e+06, 'cm^3/(mol*s)'),
    n = 1.88,
    Ea = (183, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4 + o <=> ch2cho + h',
 "chemkinKinetics": """
c2h4+o=ch2cho+h                                     6.775e+06 1.880     0.183    
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.775e+06, 'cm^3/(mol*s)'),
    n = 1.88,
    Ea = (183, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4 + oh <=> c2h3 + h2o',
 "chemkinKinetics": """
c2h4+oh=c2h3+h2o                                    2.230e+04 2.745     2.216    
""",
 "rmgPyKinetics": Arrhenius(
    A = (22300, 'cm^3/(mol*s)'),
    n = 2.745,
    Ea = (2215.5, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + oh <=> ch3 + ch2o',
 "chemkinKinetics": """
c2h4+oh=ch3+ch2o                                    1.000e+00 0.000     0.000    
    PLOG/ 0.010     5.350e+00 2.920     -1.733   /
    PLOG/ 0.025     3.190e+01 2.710     -1.172   /
    PLOG/ 0.100     5.550e+02 2.360     -0.181   /
    PLOG/ 1.000     1.780e+05 1.680     2.061    /
    PLOG/ 10.000    2.370e+09 0.560     6.007    /
    PLOG/ 100.000   2.760e+13 -0.500    11.455   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.35, 'cm^3/(mol*s)'),
            n = 2.92,
            Ea = (-1732.66, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (31.9, 'cm^3/(mol*s)'),
            n = 2.71,
            Ea = (-1172.33, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (555, 'cm^3/(mol*s)'),
            n = 2.36,
            Ea = (-180.817, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (178000, 'cm^3/(mol*s)'),
            n = 1.68,
            Ea = (2060.52, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.37e+09, 'cm^3/(mol*s)'),
            n = 0.56,
            Ea = (6006.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.76e+13, 'cm^3/(mol*s)'),
            n = -0.5,
            Ea = (11455.1, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4 + oh <=> ch3cho + h',
 "chemkinKinetics": """
c2h4+oh=ch3cho+h                                    1.000e+00 0.000     0.000    
    PLOG/ 0.010     2.370e-07 5.300     -2.051   /
    PLOG/ 0.025     8.730e-05 4.570     -0.618   /
    PLOG/ 0.100     4.030e-01 3.540     1.882    /
    PLOG/ 1.000     2.380e-02 3.910     1.723    /
    PLOG/ 10.000    8.250e+08 1.010     10.507   /
    PLOG/ 100.000   6.800e+09 0.810     13.867   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (2.37e-07, 'cm^3/(mol*s)'),
            n = 5.3,
            Ea = (-2050.58, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (8.73e-05, 'cm^3/(mol*s)'),
            n = 4.57,
            Ea = (-617.957, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (0.403, 'cm^3/(mol*s)'),
            n = 3.54,
            Ea = (1881.69, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (0.0238, 'cm^3/(mol*s)'),
            n = 3.91,
            Ea = (1722.73, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (8.25e+08, 'cm^3/(mol*s)'),
            n = 1.01,
            Ea = (10507.3, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (6.8e+09, 'cm^3/(mol*s)'),
            n = 0.81,
            Ea = (13867.3, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4 + oh <=> c2h3oh + h',
 "chemkinKinetics": """
c2h4+oh=c2h3oh+h                                    1.000e+00 0.000     0.000    
    PLOG/ 0.010     1.040e+04 2.600     4.121    /
    PLOG/ 0.025     1.070e+04 2.600     4.129    /
    PLOG/ 0.100     1.520e+04 2.560     4.238    /
    PLOG/ 1.000     3.190e+05 2.190     5.256    /
    PLOG/ 10.000    1.940e+08 1.430     7.829    /
    PLOG/ 100.000   8.550e+10 0.750     11.491   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (10400, 'cm^3/(mol*s)'),
            n = 2.6,
            Ea = (4121.04, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (10700, 'cm^3/(mol*s)'),
            n = 2.6,
            Ea = (4128.99, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (15200, 'cm^3/(mol*s)'),
            n = 2.56,
            Ea = (4238.27, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (319000, 'cm^3/(mol*s)'),
            n = 2.19,
            Ea = (5255.61, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.94e+08, 'cm^3/(mol*s)'),
            n = 1.43,
            Ea = (7828.78, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (8.55e+10, 'cm^3/(mol*s)'),
            n = 0.75,
            Ea = (11490.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4 + oh <=> pc2h4oh',
 "chemkinKinetics": """
c2h4+oh=pc2h4oh                                     1.000e+00 0.000     0.000    
    PLOG/ 0.010     1.740e+43 -10.461   7.699    /
    PLOG/ 0.025     3.250e+37 -8.629    5.215    /
    PLOG/ 0.100     1.840e+35 -7.750    4.909    /
    PLOG/ 1.000     2.560e+36 -7.752    6.946    /
    PLOG/ 10.000    3.700e+33 -6.573    7.606    /
    PLOG/ 100.000   1.120e+26 -4.101    5.757    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (1.74e+43, 'cm^3/(mol*s)'),
            n = -10.4609,
            Ea = (7698.73, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.25e+37, 'cm^3/(mol*s)'),
            n = -8.62888,
            Ea = (5214.66, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.84e+35, 'cm^3/(mol*s)'),
            n = -7.75006,
            Ea = (4908.86, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.56e+36, 'cm^3/(mol*s)'),
            n = -7.75206,
            Ea = (6946.11, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.7e+33, 'cm^3/(mol*s)'),
            n = -6.57294,
            Ea = (7605.89, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.12e+26, 'cm^3/(mol*s)'),
            n = -4.10119,
            Ea = (5756.95, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h3oh + o2 <=> ch2cho + ho2',
 "chemkinKinetics": """
c2h3oh+o2=ch2cho+ho2                                5.310e+11 0.210     39.830   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.31e+11, 'cm^3/(mol*s)'),
    n = 0.21,
    Ea = (39830, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3oh + o <=> ch2cho + oh',
 "chemkinKinetics": """
c2h3oh+o=ch2cho+oh                                  1.875e+06 1.900     -0.860   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.875e+06, 'cm^3/(mol*s)'),
    n = 1.9,
    Ea = (-860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3oh + oh <=> ch2cho + h2o',
 "chemkinKinetics": """
c2h3oh+oh=ch2cho+h2o                                3.330e+09 1.100     0.541    
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.33e+09, 'cm^3/(mol*s)'),
    n = 1.1,
    Ea = (540.5, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3oh + ch3 <=> ch2cho + ch4',
 "chemkinKinetics": """
c2h3oh+ch3=ch2cho+ch4                               2.030e-08 5.900     1.052    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.03e-08, 'cm^3/(mol*s)'),
    n = 5.9,
    Ea = (1052, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3oh + ch3o2 <=> ch2cho + ch3o2h',
 "chemkinKinetics": """
c2h3oh+ch3o2=ch2cho+ch3o2h                          3.400e+03 2.500     8.922    
""",
 "rmgPyKinetics": Arrhenius(A=(3400, 'cm^3/(mol*s)'), n=2.5, Ea=(8922, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3oh + h <=> ch2cho + h2',
 "chemkinKinetics": """
c2h3oh+h=ch2cho+h2                                  1.480e+03 3.077     7.220    
""",
 "rmgPyKinetics": Arrhenius(A=(1480, 'cm^3/(mol*s)'), n=3.077, Ea=(7220, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3oh + h <=> c2h2oh + h2',
 "chemkinKinetics": """
c2h3oh+h=c2h2oh+h2                                  2.470e+07 2.030     15.200   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.47e+07, 'cm^3/(mol*s)'),
    n = 2.03,
    Ea = (15200, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3oh + h <=> pc2h4oh',
 "chemkinKinetics": """
c2h3oh+h=pc2h4oh                                    3.010e+08 1.577     3.670    
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.01e+08, 'cm^3/(mol*s)'),
    n = 1.577,
    Ea = (3670, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h3oh + ho2 <=> ch3cho + ho2',
 "chemkinKinetics": """
c2h3oh+ho2=ch3cho+ho2                               1.490e+05 1.670     6.810    
""",
 "rmgPyKinetics": Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3oh <=> ch3cho',
 "chemkinKinetics": """
c2h3oh=ch3cho                                       1.000e+00 0.000     0.000    
    PLOG/ 0.100     7.420e+46 -10.560   67.200   /
    PLOG/ 1.000     4.420e+42 -9.090    67.069   /
    PLOG/ 100.000   2.900e+27 -4.350    61.613   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(7.42e+46, 's^-1'), n=-10.56, Ea=(67200, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.42e+42, 's^-1'), n=-9.09, Ea=(67069.2, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.9e+27, 's^-1'), n=-4.35, Ea=(61612.9, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['ketoenol',  ],
},

{
 "reaction": 'c2h3oh <=> c2h3 + oh',
 "chemkinKinetics": """
c2h3oh=c2h3+oh                                      6.899e+21 -1.564    110.700  
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.899e+21, 's^-1'),
    n = -1.564,
    Ea = (110700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 2.410E+13 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h3oh <=> ch2cho + h',
 "chemkinKinetics": """
c2h3oh=ch2cho+h                                     3.643e+15 -0.397    95.390   
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.643e+15, 's^-1'),
    n = -0.397,
    Ea = (95390, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 2.400E+13 0.000 1.251E+04 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h4 + ch3 <=> c2h3 + ch4',
 "chemkinKinetics": """
c2h4+ch3=c2h3+ch4                                   6.620e+00 3.700     9.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.62, 'cm^3/(mol*s)'), n=3.7, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + o2 <=> c2h3 + ho2',
 "chemkinKinetics": """
c2h4+o2=c2h3+ho2                                    4.220e+13 0.000     57.623   
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.22e+13, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (57623.1, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + ch3o <=> c2h3 + ch3oh',
 "chemkinKinetics": """
c2h4+ch3o=c2h3+ch3oh                                1.200e+11 0.000     6.750    
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(6750, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + ch3o2 <=> c2h3 + ch3o2h',
 "chemkinKinetics": """
c2h4+ch3o2=c2h3+ch3o2h                              8.590e+00 3.754     27.132   
""",
 "rmgPyKinetics": Arrhenius(A=(8.59, 'cm^3/(mol*s)'), n=3.754, Ea=(27132, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + c2h5o2 <=> c2h3 + c2h5o2h',
 "chemkinKinetics": """
c2h4+c2h5o2=c2h3+c2h5o2h                            8.590e+00 3.754     27.132   
""",
 "rmgPyKinetics": Arrhenius(A=(8.59, 'cm^3/(mol*s)'), n=3.754, Ea=(27132, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + ch3co3 <=> c2h3 + ch3co3h',
 "chemkinKinetics": """
c2h4+ch3co3=c2h3+ch3co3h                            1.130e+13 0.000     30.430   
""",
 "rmgPyKinetics": Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + ch3o2 <=> c2h4o1-2 + ch3o',
 "chemkinKinetics": """
c2h4+ch3o2=c2h4o1-2+ch3o                            2.820e+12 0.000     17.110   
""",
 "rmgPyKinetics": Arrhenius(A=(2.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(17110, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4 + c2h5o2 <=> c2h4o1-2 + c2h5o',
 "chemkinKinetics": """
c2h4+c2h5o2=c2h4o1-2+c2h5o                          2.820e+12 0.000     17.110   
""",
 "rmgPyKinetics": Arrhenius(A=(2.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(17110, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4 + ho2 <=> c2h4o1-2 + oh',
 "chemkinKinetics": """
c2h4+ho2=c2h4o1-2+oh                                5.575e+11 0.000     17.190   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.575e+11, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17190, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch + ch4 <=> c2h4 + h',
 "chemkinKinetics": """
ch+ch4=c2h4+h                                       6.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2(s) + ch3 <=> c2h4 + h',
 "chemkinKinetics": """
ch2(s)+ch3=c2h4+h                                   2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + h <=> c2h3',
 "chemkinKinetics": """
c2h2+h(+M)=c2h3(+M)                                 1.710e+10 1.266     2.709    
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ he/0.70/ 
    LOW/ 6.346e+31 -4.664    3.780    /
    TROE/ 7.600e-01 1e+30     1e-30    /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (1.71e+10, 'cm^3/(mol*s)'),
        n = 1.266,
        Ea = (2709, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (6.346e+31, 'cm^6/(mol^2*s)'),
        n = -4.664,
        Ea = (3780, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.76,
    T3 = (1e+30, 'K'),
    T1 = (1e-30, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.7,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h3 + o2 <=> ch2o + hco',
 "chemkinKinetics": """
c2h3+o2=ch2o+hco                                    1.700e+29 -5.312    6.503    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.7e+29, 'cm^3/(mol*s)'),
    n = -5.312,
    Ea = (6503.11, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3 + o2 <=> ch2cho + o',
 "chemkinKinetics": """
c2h3+o2=ch2cho+o                                    7.000e+14 -0.611    5.262    
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+14, 'cm^3/(mol*s)'),
    n = -0.611,
    Ea = (5262.43, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3 + o2 => h + co + ch2o',
 "chemkinKinetics": """
c2h3+o2=>h+co+ch2o                                  5.190e+15 -1.260    3.313    
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.19e+15, 'cm^3/(mol*s)'),
    n = -1.26,
    Ea = (3312.62, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3 + c2h3 <=> ch4 + c2h2',
 "chemkinKinetics": """
ch3+c2h3=ch4+c2h2                                   3.920e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.92e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h3 + h <=> c2h2 + h2',
 "chemkinKinetics": """
c2h3+h=c2h2+h2                                      9.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h3 + h <=> h2cc + h2',
 "chemkinKinetics": """
c2h3+h=h2cc+h2                                      6.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3 + oh <=> c2h2 + h2o',
 "chemkinKinetics": """
c2h3+oh=c2h2+h2o                                    3.011e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.011e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h3 + c2h3 <=> c2h2 + c2h4',
 "chemkinKinetics": """
c2h3+c2h3=c2h2+c2h4                                 9.600e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(9.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h + h <=> c2h2',
 "chemkinKinetics": """
c2h+h(+M)=c2h2(+M)                                  1.000e+17 0.000     0.000    
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ he/0.70/ 
    LOW/ 3.750e+33 -4.800    1.900    /
    TROE/ 6.460e-01 132       1.32e+03  5.57e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (3.75e+33, 'cm^6/(mol^2*s)'),
        n = -4.8,
        Ea = (1900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.646,
    T3 = (132, 'K'),
    T1 = (1315, 'K'),
    T2 = (5566, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.7,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h2 <=> h2cc',
 "chemkinKinetics": """
c2h2(+M)=h2cc(+M)                                   8.000e+14 -0.520    50.750   
co2/2.00/ ch4/2.00/ c2h2/2.50/ co/1.50/ c2h4/2.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ 
    LOW/ 2.450e+15 -0.640    49.700   /
""",
 "rmgPyKinetics": Lindemann(
    arrheniusHigh = Arrhenius(A=(8e+14, 's^-1'), n=-0.52, Ea=(50750, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (2.45e+15, 'cm^3/(mol*s)'),
        n = -0.64,
        Ea = (49700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='C=C'): 2.5,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[H][H]'): 2,
        Molecule(SMILES='C#C'): 2.5,
    },
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + o <=> ch2 + co',
 "chemkinKinetics": """
c2h2+o=ch2+co                                       7.395e+08 1.280     2.472    
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.395e+08, 'cm^3/(mol*s)'),
    n = 1.28,
    Ea = (2472, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + o <=> hcco + h',
 "chemkinKinetics": """
c2h2+o=hcco+h                                       2.958e+09 1.280     2.472    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.958e+09, 'cm^3/(mol*s)'),
    n = 1.28,
    Ea = (2472, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + oh <=> c2h + h2o',
 "chemkinKinetics": """
c2h2+oh=c2h+h2o                                     2.632e+06 2.140     17.060   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.632e+06, 'cm^3/(mol*s)'),
    n = 2.14,
    Ea = (17060, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h2 + oh <=> hccoh + h',
 "chemkinKinetics": """
c2h2+oh=hccoh+h                                     1.000e+00 0.000     0.000    
    PLOG/ 0.010     2.800e+05 2.280     12.420   /
    PLOG/ 0.025     7.467e+05 2.160     12.550   /
    PLOG/ 0.100     1.776e+06 2.040     12.670   /
    PLOG/ 1.000     2.415e+06 2.000     12.710   /
    PLOG/ 10.000    3.210e+06 1.970     12.810   /
    PLOG/ 100.000   7.347e+06 1.890     13.600   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (280000, 'cm^3/(mol*s)'),
            n = 2.28,
            Ea = (12420, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (746700, 'cm^3/(mol*s)'),
            n = 2.16,
            Ea = (12550, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.776e+06, 'cm^3/(mol*s)'),
            n = 2.04,
            Ea = (12670, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.415e+06, 'cm^3/(mol*s)'),
            n = 2,
            Ea = (12710, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.21e+06, 'cm^3/(mol*s)'),
            n = 1.97,
            Ea = (12810, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (7.347e+06, 'cm^3/(mol*s)'),
            n = 1.89,
            Ea = (13600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + oh <=> ch2co + h',
 "chemkinKinetics": """
c2h2+oh=ch2co+h                                     1.000e+00 0.000     0.000    
    PLOG/ 0.010     1.578e+03 2.560     -0.845   /
    PLOG/ 0.025     1.518e+04 2.280     -0.292   /
    PLOG/ 0.100     3.017e+05 1.920     0.598    /
    PLOG/ 1.000     7.528e+06 1.550     2.106    /
    PLOG/ 10.000    5.101e+06 1.650     3.400    /
    PLOG/ 100.000   1.457e+04 2.450     4.477    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(1578, 'cm^3/(mol*s)'), n=2.56, Ea=(-844.5, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(
            A = (15180, 'cm^3/(mol*s)'),
            n = 2.28,
            Ea = (-292.1, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (301700, 'cm^3/(mol*s)'),
            n = 1.92,
            Ea = (598.1, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (7.528e+06, 'cm^3/(mol*s)'),
            n = 1.55,
            Ea = (2106, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.101e+06, 'cm^3/(mol*s)'),
            n = 1.65,
            Ea = (3400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(A=(14570, 'cm^3/(mol*s)'), n=2.45, Ea=(4477, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + oh <=> ch3 + co',
 "chemkinKinetics": """
c2h2+oh=ch3+co                                      1.000e+00 0.000     0.000    
    PLOG/ 0.010     4.757e+05 1.680     -0.330   /
    PLOG/ 0.025     4.372e+06 1.400     0.227    /
    PLOG/ 0.100     7.648e+07 1.050     1.115    /
    PLOG/ 1.000     1.277e+09 0.730     2.579    /
    PLOG/ 10.000    4.312e+08 0.920     3.736    /
    PLOG/ 100.000   8.250e+05 1.770     4.697    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (475700, 'cm^3/(mol*s)'),
            n = 1.68,
            Ea = (-329.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.372e+06, 'cm^3/(mol*s)'),
            n = 1.4,
            Ea = (226.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (7.648e+07, 'cm^3/(mol*s)'),
            n = 1.05,
            Ea = (1115, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.277e+09, 'cm^3/(mol*s)'),
            n = 0.73,
            Ea = (2579, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.312e+08, 'cm^3/(mol*s)'),
            n = 0.92,
            Ea = (3736, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(A=(825000, 'cm^3/(mol*s)'), n=1.77, Ea=(4697, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + oh <=> c2h2oh',
 "chemkinKinetics": """
c2h2+oh=c2h2oh                                      1.000e+00 0.000     0.000    
    PLOG/ 0.010     3.913e+32 -7.126    5.824    /
    PLOG/ 0.025     1.067e+32 -6.847    5.508    /
    PLOG/ 0.100     1.646e+32 -6.717    5.822    /
    PLOG/ 1.000     1.387e+31 -6.087    6.348    /
    PLOG/ 10.000    2.892e+29 -5.288    7.055    /
    PLOG/ 100.000   1.367e+25 -3.754    6.543    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (3.913e+32, 'cm^3/(mol*s)'),
            n = -7.126,
            Ea = (5824, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.067e+32, 'cm^3/(mol*s)'),
            n = -6.847,
            Ea = (5508, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.646e+32, 'cm^3/(mol*s)'),
            n = -6.717,
            Ea = (5822, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.387e+31, 'cm^3/(mol*s)'),
            n = -6.087,
            Ea = (6348, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.892e+29, 'cm^3/(mol*s)'),
            n = -5.288,
            Ea = (7055, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.367e+25, 'cm^3/(mol*s)'),
            n = -3.754,
            Ea = (6543, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h2 + hco <=> c2h3 + co',
 "chemkinKinetics": """
c2h2+hco=c2h3+co                                    1.000e+07 2.000     6.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h2 + ch2 <=> c3h3 + h',
 "chemkinKinetics": """
c2h2+ch2=c3h3+h                                     1.200e+13 0.000     6.620    
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(6620, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + ch2(s) <=> c3h3 + h',
 "chemkinKinetics": """
c2h2+ch2(s)=c3h3+h                                  2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + hcco <=> c3h3 + co',
 "chemkinKinetics": """
c2h2+hcco=c3h3+co                                   1.000e+11 0.000     3.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'h2cc + h <=> c2h2 + h',
 "chemkinKinetics": """
h2cc+h=c2h2+h                                       1.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'h2cc + oh <=> ch2co + h',
 "chemkinKinetics": """
h2cc+oh=ch2co+h                                     2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'h2cc + o2 <=> hco + hco',
 "chemkinKinetics": """
h2cc+o2=hco+hco                                     1.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'h + hccoh <=> h + ch2co',
 "chemkinKinetics": """
h+hccoh=h+ch2co                                     1.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h5oh <=> c2h4 + h2o',
 "chemkinKinetics": """
c2h5oh=c2h4+h2o                                     1.000e+00 0.000     0.000    
    PLOG/ 0.001     3.410e+59 -14.200   83.673   /
    PLOG/ 0.010     2.620e+57 -13.300   85.262   /
    PLOG/ 0.100     1.650e+52 -11.500   84.746   /
    PLOG/ 1.000     5.230e+43 -8.900    81.507   /
    PLOG/ 10.000    4.590e+32 -5.600    76.062   /
    PLOG/ 100.000   3.840e+20 -2.060    69.466   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(3.41e+59, 's^-1'), n=-14.2, Ea=(83672.6, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.62e+57, 's^-1'), n=-13.3, Ea=(85262.2, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.65e+52, 's^-1'), n=-11.5, Ea=(84745.6, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.23e+43, 's^-1'), n=-8.9, Ea=(81506.7, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.59e+32, 's^-1'), n=-5.6, Ea=(76062.4, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(3.84e+20, 's^-1'), n=-2.06, Ea=(69465.5, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['1,3_Insertion_ROR',  ],
},

{
 "reaction": 'c2h5oh <=> ch3 + ch2oh',
 "chemkinKinetics": """
c2h5oh=ch3+ch2oh                                    1.000e+00 0.000     0.000    
    PLOG/ 0.001     1.200e+54 -12.900   100.006  /
    PLOG/ 0.010     5.180e+59 -14.000   99.906   /
    PLOG/ 0.100     1.620e+66 -15.300   105.390  /
    PLOG/ 1.000     5.550e+64 -14.500   106.183  /
    PLOG/ 10.000    1.550e+58 -12.300   105.768  /
    PLOG/ 100.000   1.780e+47 -8.960    101.059  /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(1.2e+54, 's^-1'), n=-12.9, Ea=(100006, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.18e+59, 's^-1'), n=-14, Ea=(99906.4, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.62e+66, 's^-1'), n=-15.3, Ea=(105390, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.55e+64, 's^-1'), n=-14.5, Ea=(106183, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.55e+58, 's^-1'), n=-12.3, Ea=(105768, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.78e+47, 's^-1'), n=-8.96, Ea=(101059, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h5oh <=> c2h5 + oh',
 "chemkinKinetics": """
c2h5oh=c2h5+oh                                      1.000e+00 0.000     0.000    
    PLOG/ 0.001     8.100e+46 -11.300   111.053  /
    PLOG/ 0.010     1.860e+56 -13.500   107.238  /
    PLOG/ 0.100     4.650e+63 -15.000   109.623  /
    PLOG/ 1.000     4.460e+65 -14.900   112.345  /
    PLOG/ 10.000    2.790e+61 -13.400   113.080  /
    PLOG/ 100.000   6.170e+51 -10.300   109.941  /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(8.1e+46, 's^-1'), n=-11.3, Ea=(111053, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.86e+56, 's^-1'), n=-13.5, Ea=(107238, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.65e+63, 's^-1'), n=-15, Ea=(109623, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.46e+65, 's^-1'), n=-14.9, Ea=(112345, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.79e+61, 's^-1'), n=-13.4, Ea=(113080, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(6.17e+51, 's^-1'), n=-10.3, Ea=(109941, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h5oh + o2 <=> pc2h4oh + ho2',
 "chemkinKinetics": """
c2h5oh+o2=pc2h4oh+ho2                               2.000e+13 0.000     52.800   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(52800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + o2 <=> sc2h4oh + ho2',
 "chemkinKinetics": """
c2h5oh+o2=sc2h4oh+ho2                               1.500e+13 0.000     50.150   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(50150, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + h <=> sc2h4oh + h2',
 "chemkinKinetics": """
c2h5oh+h=sc2h4oh+h2                                 8.790e+04 2.680     2.910    
""",
 "rmgPyKinetics": Arrhenius(A=(87900, 'cm^3/(mol*s)'), n=2.68, Ea=(2910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + h <=> pc2h4oh + h2',
 "chemkinKinetics": """
c2h5oh+h=pc2h4oh+h2                                 5.310e+04 2.810     7.490    
""",
 "rmgPyKinetics": Arrhenius(A=(53100, 'cm^3/(mol*s)'), n=2.81, Ea=(7490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + h <=> c2h5o + h2',
 "chemkinKinetics": """
c2h5oh+h=c2h5o+h2                                   9.450e+02 3.140     8.701    
""",
 "rmgPyKinetics": Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701.07, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + oh <=> sc2h4oh + h2o',
 "chemkinKinetics": """
c2h5oh+oh=sc2h4oh+h2o                               7.170e+04 2.540     -1.534   
""",
 "rmgPyKinetics": Arrhenius(
    A = (71700, 'cm^3/(mol*s)'),
    n = 2.54,
    Ea = (-1533.96, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + oh <=> pc2h4oh + h2o',
 "chemkinKinetics": """
c2h5oh+oh=pc2h4oh+h2o                               5.700e+00 3.380     -2.394   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.7, 'cm^3/(mol*s)'),
    n = 3.38,
    Ea = (-2394.34, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + oh <=> c2h5o + h2o',
 "chemkinKinetics": """
c2h5oh+oh=c2h5o+h2o                                 5.810e-03 4.280     -3.560   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.00581, 'cm^3/(mol*s)'),
    n = 4.28,
    Ea = (-3560, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + ho2 <=> sc2h4oh + h2o2',
 "chemkinKinetics": """
c2h5oh+ho2=sc2h4oh+h2o2                             2.800e-02 4.320     8.530    
""",
 "rmgPyKinetics": Arrhenius(A=(0.028, 'cm^3/(mol*s)'), n=4.32, Ea=(8530, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + ho2 <=> pc2h4oh + h2o2',
 "chemkinKinetics": """
c2h5oh+ho2=pc2h4oh+h2o2                             9.040e-03 4.540     11.968   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.00904, 'cm^3/(mol*s)'),
    n = 4.54,
    Ea = (11967.9, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + ho2 <=> c2h5o + h2o2',
 "chemkinKinetics": """
c2h5oh+ho2=c2h5o+h2o2                               5.620e-03 4.120     17.400   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.00562, 'cm^3/(mol*s)'),
    n = 4.12,
    Ea = (17400, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + ch3o2 <=> pc2h4oh + ch3o2h',
 "chemkinKinetics": """
c2h5oh+ch3o2=pc2h4oh+ch3o2h                         1.230e+04 2.550     15.750   
""",
 "rmgPyKinetics": Arrhenius(A=(12300, 'cm^3/(mol*s)'), n=2.55, Ea=(15750, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + ch3o2 <=> sc2h4oh + ch3o2h',
 "chemkinKinetics": """
c2h5oh+ch3o2=sc2h4oh+ch3o2h                         8.200e+03 2.550     10.750   
""",
 "rmgPyKinetics": Arrhenius(A=(8200, 'cm^3/(mol*s)'), n=2.55, Ea=(10750, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + ch3o2 <=> c2h5o + ch3o2h',
 "chemkinKinetics": """
c2h5oh+ch3o2=c2h5o+ch3o2h                           2.500e+12 0.000     24.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + o <=> pc2h4oh + oh',
 "chemkinKinetics": """
c2h5oh+o=pc2h4oh+oh                                 9.690e+02 3.230     4.658    
""",
 "rmgPyKinetics": Arrhenius(A=(969, 'cm^3/(mol*s)'), n=3.23, Ea=(4658, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + o <=> sc2h4oh + oh',
 "chemkinKinetics": """
c2h5oh+o=sc2h4oh+oh                                 1.450e+05 2.470     0.876    
""",
 "rmgPyKinetics": Arrhenius(A=(145000, 'cm^3/(mol*s)'), n=2.47, Ea=(876, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + o <=> c2h5o + oh',
 "chemkinKinetics": """
c2h5oh+o=c2h5o+oh                                   1.460e-03 4.730     1.727    
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.00146, 'cm^3/(mol*s)'),
    n = 4.73,
    Ea = (1727, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + ch3 <=> pc2h4oh + ch4',
 "chemkinKinetics": """
c2h5oh+ch3=pc2h4oh+ch4                              3.300e+02 3.300     12.290   
""",
 "rmgPyKinetics": Arrhenius(A=(330, 'cm^3/(mol*s)'), n=3.3, Ea=(12290, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + ch3 <=> sc2h4oh + ch4',
 "chemkinKinetics": """
c2h5oh+ch3=sc2h4oh+ch4                              1.993e+01 3.370     7.634    
""",
 "rmgPyKinetics": Arrhenius(A=(19.93, 'cm^3/(mol*s)'), n=3.37, Ea=(7634, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + ch3 <=> c2h5o + ch4',
 "chemkinKinetics": """
c2h5oh+ch3=c2h5o+ch4                                2.035e+00 3.570     7.721    
""",
 "rmgPyKinetics": Arrhenius(A=(2.035, 'cm^3/(mol*s)'), n=3.57, Ea=(7721, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + c2h5 <=> pc2h4oh + c2h6',
 "chemkinKinetics": """
c2h5oh+c2h5=pc2h4oh+c2h6                            5.000e+10 0.000     13.400   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5oh + c2h5 <=> sc2h4oh + c2h6',
 "chemkinKinetics": """
c2h5oh+c2h5=sc2h4oh+c2h6                            5.000e+10 0.000     10.400   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc2h4oh <=> ch3cho + h',
 "chemkinKinetics": """
sc2h4oh=ch3cho+h                                    1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.690e+52 -13.380   45.049   /
    PLOG/ 0.010     3.290e+56 -14.120   48.129   /
    PLOG/ 0.100     8.580e+57 -14.160   50.743   /
    PLOG/ 1.000     5.360e+55 -13.150   51.886   /
    PLOG/ 10.000    1.660e+48 -10.640   50.297   /
    PLOG/ 20.000    8.260e+44 -9.590    49.218   /
    PLOG/ 50.000    1.010e+40 -8.060    47.439   /
    PLOG/ 100.000   1.100e+36 -6.840    45.899   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 20, 50, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(5.69e+52, 's^-1'), n=-13.38, Ea=(45049, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(3.29e+56, 's^-1'), n=-14.12, Ea=(48129, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(8.58e+57, 's^-1'), n=-14.16, Ea=(50743, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.36e+55, 's^-1'), n=-13.15, Ea=(51886, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.66e+48, 's^-1'), n=-10.64, Ea=(50297, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(8.26e+44, 's^-1'), n=-9.59, Ea=(49218, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.01e+40, 's^-1'), n=-8.06, Ea=(47439, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.1e+36, 's^-1'), n=-6.84, Ea=(45899, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'sc2h4oh <=> c2h3oh + h',
 "chemkinKinetics": """
sc2h4oh=c2h3oh+h                                    1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.400e+46 -11.630   44.323   /
    PLOG/ 0.010     1.210e+51 -12.550   47.240   /
    PLOG/ 0.100     2.870e+54 -13.150   50.702   /
    PLOG/ 1.000     3.790e+53 -12.510   52.560   /
    PLOG/ 10.000    6.330e+46 -10.200   51.441   /
    PLOG/ 20.000    3.870e+43 -9.170    50.440   /
    PLOG/ 50.000    5.080e+38 -7.650    48.713   /
    PLOG/ 100.000   5.120e+34 -6.410    47.182   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 20, 50, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(5.4e+46, 's^-1'), n=-11.63, Ea=(44323, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.21e+51, 's^-1'), n=-12.55, Ea=(47240, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.87e+54, 's^-1'), n=-13.15, Ea=(50702, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(3.79e+53, 's^-1'), n=-12.51, Ea=(52560, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(6.33e+46, 's^-1'), n=-10.2, Ea=(51441, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(3.87e+43, 's^-1'), n=-9.17, Ea=(50440, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.08e+38, 's^-1'), n=-7.65, Ea=(48713, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.12e+34, 's^-1'), n=-6.41, Ea=(47182, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'sc2h4oh <=> c2h5o',
 "chemkinKinetics": """
sc2h4oh=c2h5o                                       1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.480e+45 -11.630   44.328   /
    PLOG/ 0.010     2.540e+49 -12.370   46.445   /
    PLOG/ 0.100     1.650e+54 -13.400   50.330   /
    PLOG/ 1.000     1.810e+55 -13.310   53.132   /
    PLOG/ 10.000    4.580e+49 -11.320   52.714   /
    PLOG/ 20.000    4.110e+46 -10.330   51.834   /
    PLOG/ 50.000    6.680e+41 -8.830    50.202   /
    PLOG/ 100.000   6.540e+37 -7.580    48.697   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 20, 50, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(5.48e+45, 's^-1'), n=-11.63, Ea=(44328, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.54e+49, 's^-1'), n=-12.37, Ea=(46445, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.65e+54, 's^-1'), n=-13.4, Ea=(50330, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.81e+55, 's^-1'), n=-13.31, Ea=(53132, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.58e+49, 's^-1'), n=-11.32, Ea=(52714, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.11e+46, 's^-1'), n=-10.33, Ea=(51834, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(6.68e+41, 's^-1'), n=-8.83, Ea=(50202, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(6.54e+37, 's^-1'), n=-7.58, Ea=(48697, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc2h4oh <=> pc2h4oh',
 "chemkinKinetics": """
sc2h4oh=pc2h4oh                                     1.000e+00 0.000     0.000    
    PLOG/ 0.001     2.650e+36 -8.860    51.019   /
    PLOG/ 0.010     3.560e+37 -8.890    51.114   /
    PLOG/ 0.100     4.140e+39 -9.190    51.912   /
    PLOG/ 1.000     5.820e+44 -10.340   55.296   /
    PLOG/ 10.000    4.260e+48 -11.060   59.458   /
    PLOG/ 20.000    8.840e+47 -10.740   59.901   /
    PLOG/ 50.000    2.230e+45 -9.840    59.604   /
    PLOG/ 100.000   1.700e+42 -8.830    58.737   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 20, 50, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(2.65e+36, 's^-1'), n=-8.86, Ea=(51019, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(3.56e+37, 's^-1'), n=-8.89, Ea=(51114, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.14e+39, 's^-1'), n=-9.19, Ea=(51912, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.82e+44, 's^-1'), n=-10.34, Ea=(55296, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.26e+48, 's^-1'), n=-11.06, Ea=(59458, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(8.84e+47, 's^-1'), n=-10.74, Ea=(59901, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.23e+45, 's^-1'), n=-9.84, Ea=(59604, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.7e+42, 's^-1'), n=-8.83, Ea=(58737, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'o2c2h4oh <=> pc2h4oh + o2',
 "chemkinKinetics": """
o2c2h4oh=pc2h4oh+o2                                 3.900e+16 -1.000    30.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3.9e+16, 's^-1'), n=-1, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'o2c2h4oh => oh + ch2o + ch2o',
 "chemkinKinetics": """
o2c2h4oh=>oh+ch2o+ch2o                              3.125e+09 0.000     18.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.125e+09, 's^-1'), n=0, Ea=(18900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products3',  ],
},

{
 "reaction": 'sc2h4oh + o2 <=> ch3cho + ho2',
 "chemkinKinetics": """
sc2h4oh+o2=ch3cho+ho2                               1.000e+00 0.000     0.000    
    PLOG/ 0.010     5.260e+17 -1.637    0.838    /
    PLOG/ 0.100     5.260e+17 -1.637    0.838    /
    PLOG/ 1.000     5.280e+17 -1.638    0.839    /
    PLOG/ 10.000    1.540e+18 -1.771    1.120    /
    PLOG/ 100.000   3.780e+20 -2.429    3.090    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.28e+17, 'cm^3/(mol*s)'),
            n = -1.638,
            Ea = (839, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.54e+18, 'cm^3/(mol*s)'),
            n = -1.771,
            Ea = (1120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+20, 'cm^3/(mol*s)'),
            n = -2.429,
            Ea = (3090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'sc2h4oh + o2 <=> c2h3oh + ho2',
 "chemkinKinetics": """
sc2h4oh+o2=c2h3oh+ho2                               1.000e+00 0.000     0.000    
    PLOG/ 0.010     5.120e+02 2.496     -0.414   /
    PLOG/ 0.100     5.330e+02 2.490     -0.402   /
    PLOG/ 1.000     7.620e+02 2.446     -0.296   /
    PLOG/ 10.000    8.920e+03 2.146     0.470    /
    PLOG/ 100.000   4.380e+05 1.699     2.330    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(512, 'cm^3/(mol*s)'), n=2.496, Ea=(-414, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(533, 'cm^3/(mol*s)'), n=2.49, Ea=(-402, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(762, 'cm^3/(mol*s)'), n=2.446, Ea=(-296, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(8920, 'cm^3/(mol*s)'), n=2.146, Ea=(470, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(
            A = (438000, 'cm^3/(mol*s)'),
            n = 1.699,
            Ea = (2330, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3coch3 <=> ch3co + ch3',
 "chemkinKinetics": """
ch3coch3(+M)=ch3co+ch3(+M)                          7.108e+21 -1.570    84.680   

    LOW/ 7.013e+89 -20.380   107.150  /
    TROE/ 8.630e-01 1e+10     416       3.29e+09 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(7.108e+21, 's^-1'), n=-1.57, Ea=(84680, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (7.013e+89, 'cm^3/(mol*s)'),
        n = -20.38,
        Ea = (107150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.863,
    T3 = (1e+10, 'K'),
    T1 = (416.4, 'K'),
    T2 = (3.29e+09, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3coch3 + oh <=> ch3coch2 + h2o',
 "chemkinKinetics": """
ch3coch3+oh=ch3coch2+h2o                            1.250e+05 2.483     0.445    
""",
 "rmgPyKinetics": Arrhenius(A=(125000, 'cm^3/(mol*s)'), n=2.483, Ea=(445, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3coch3 + h <=> ch3coch2 + h2',
 "chemkinKinetics": """
ch3coch3+h=ch3coch2+h2                              9.800e+05 2.430     5.160    
""",
 "rmgPyKinetics": Arrhenius(A=(980000, 'cm^3/(mol*s)'), n=2.43, Ea=(5160, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3coch3 + o <=> ch3coch2 + oh',
 "chemkinKinetics": """
ch3coch3+o=ch3coch2+oh                              5.130e+11 0.211     4.890    
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.13e+11, 'cm^3/(mol*s)'),
    n = 0.211,
    Ea = (4890, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3coch3 + ch3 <=> ch3coch2 + ch4',
 "chemkinKinetics": """
ch3coch3+ch3=ch3coch2+ch4                           3.960e+11 0.000     9.784    
""",
 "rmgPyKinetics": Arrhenius(A=(3.96e+11, 'cm^3/(mol*s)'), n=0, Ea=(9784, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3coch3 + ch3o <=> ch3coch2 + ch3oh',
 "chemkinKinetics": """
ch3coch3+ch3o=ch3coch2+ch3oh                        4.340e+11 0.000     6.460    
""",
 "rmgPyKinetics": Arrhenius(A=(4.34e+11, 'cm^3/(mol*s)'), n=0, Ea=(6460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3coch3 + o2 <=> ch3coch2 + ho2',
 "chemkinKinetics": """
ch3coch3+o2=ch3coch2+ho2                            6.030e+13 0.000     48.500   
""",
 "rmgPyKinetics": Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(48500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3coch3 + ho2 <=> ch3coch2 + h2o2',
 "chemkinKinetics": """
ch3coch3+ho2=ch3coch2+h2o2                          1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3coch3 + ch3o2 <=> ch3coch2 + ch3o2h',
 "chemkinKinetics": """
ch3coch3+ch3o2=ch3coch2+ch3o2h                      1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2co + ch3 <=> ch3coch2',
 "chemkinKinetics": """
ch2co+ch3=ch3coch2                                  1.760e+04 2.480     6.130    
""",
 "rmgPyKinetics": Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3coch2 + o2 <=> ch3coch2o2',
 "chemkinKinetics": """
ch3coch2+o2=ch3coch2o2                              1.200e+11 0.000     -1.100   
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3coch3 + ch3coch2o2 <=> ch3coch2 + c3ket21',
 "chemkinKinetics": """
ch3coch3+ch3coch2o2=ch3coch2+c3ket21                1.000e+11 0.000     5.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2o + ch3coch2o2 <=> hco + c3ket21',
 "chemkinKinetics": """
ch2o+ch3coch2o2=hco+c3ket21                         1.288e+11 0.000     9.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.288e+11, 'cm^3/(mol*s)'), n=0, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ho2 + ch3coch2o2 <=> c3ket21 + o2',
 "chemkinKinetics": """
ho2+ch3coch2o2=c3ket21+o2                           1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3 + hco <=> c2h3cho',
 "chemkinKinetics": """
c2h3+hco=c2h3cho                                    1.810e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h3cho + h <=> c2h3co + h2',
 "chemkinKinetics": """
c2h3cho+h=c2h3co+h2                                 1.340e+13 0.000     3.300    
""",
 "rmgPyKinetics": Arrhenius(A=(1.34e+13, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3cho + o <=> c2h3co + oh',
 "chemkinKinetics": """
c2h3cho+o=c2h3co+oh                                 5.940e+12 0.000     1.868    
""",
 "rmgPyKinetics": Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3cho + oh <=> c2h3co + h2o',
 "chemkinKinetics": """
c2h3cho+oh=c2h3co+h2o                               9.240e+06 1.500     -0.962   
""",
 "rmgPyKinetics": Arrhenius(
    A = (9.24e+06, 'cm^3/(mol*s)'),
    n = 1.5,
    Ea = (-962, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3cho + o2 <=> c2h3co + ho2',
 "chemkinKinetics": """
c2h3cho+o2=c2h3co+ho2                               1.005e+13 0.000     40.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.005e+13, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (40700, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3cho + ho2 <=> c2h3co + h2o2',
 "chemkinKinetics": """
c2h3cho+ho2=c2h3co+h2o2                             3.010e+12 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3cho + ch3 <=> c2h3co + ch4',
 "chemkinKinetics": """
c2h3cho+ch3=c2h3co+ch4                              2.608e+06 1.780     5.911    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.608e+06, 'cm^3/(mol*s)'),
    n = 1.78,
    Ea = (5911, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3cho + c2h3 <=> c2h3co + c2h4',
 "chemkinKinetics": """
c2h3cho+c2h3=c2h3co+c2h4                            1.740e+12 0.000     8.440    
""",
 "rmgPyKinetics": Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3cho + ch3o <=> c2h3co + ch3oh',
 "chemkinKinetics": """
c2h3cho+ch3o=c2h3co+ch3oh                           1.000e+12 0.000     3.300    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3cho + ch3o2 <=> c2h3co + ch3o2h',
 "chemkinKinetics": """
c2h3cho+ch3o2=c2h3co+ch3o2h                         3.010e+12 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3 + co <=> c2h3co',
 "chemkinKinetics": """
c2h3+co=c2h3co                                      1.510e+11 0.000     4.810    
""",
 "rmgPyKinetics": Arrhenius(A=(1.51e+11, 'cm^3/(mol*s)'), n=0, Ea=(4810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h5 + hco <=> c2h5cho',
 "chemkinKinetics": """
c2h5+hco=c2h5cho                                    1.810e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h5cho + h <=> c2h5co + h2',
 "chemkinKinetics": """
c2h5cho+h=c2h5co+h2                                 4.000e+13 0.000     4.200    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + o <=> c2h5co + oh',
 "chemkinKinetics": """
c2h5cho+o=c2h5co+oh                                 5.000e+12 0.000     1.790    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1790, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + oh <=> c2h5co + h2o',
 "chemkinKinetics": """
c2h5cho+oh=c2h5co+h2o                               2.690e+10 0.760     -0.340   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.69e+10, 'cm^3/(mol*s)'),
    n = 0.76,
    Ea = (-340, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + ch3 <=> c2h5co + ch4',
 "chemkinKinetics": """
c2h5cho+ch3=c2h5co+ch4                              2.608e+06 1.780     5.911    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.608e+06, 'cm^3/(mol*s)'),
    n = 1.78,
    Ea = (5911, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + ho2 <=> c2h5co + h2o2',
 "chemkinKinetics": """
c2h5cho+ho2=c2h5co+h2o2                             2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + ch3o <=> c2h5co + ch3oh',
 "chemkinKinetics": """
c2h5cho+ch3o=c2h5co+ch3oh                           1.000e+12 0.000     3.300    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + ch3o2 <=> c2h5co + ch3o2h',
 "chemkinKinetics": """
c2h5cho+ch3o2=c2h5co+ch3o2h                         3.010e+12 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + c2h5 <=> c2h5co + c2h6',
 "chemkinKinetics": """
c2h5cho+c2h5=c2h5co+c2h6                            1.000e+12 0.000     8.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + c2h5o <=> c2h5co + c2h5oh',
 "chemkinKinetics": """
c2h5cho+c2h5o=c2h5co+c2h5oh                         6.026e+11 0.000     3.300    
""",
 "rmgPyKinetics": Arrhenius(A=(6.026e+11, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + c2h5o2 <=> c2h5co + c2h5o2h',
 "chemkinKinetics": """
c2h5cho+c2h5o2=c2h5co+c2h5o2h                       3.010e+12 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + o2 <=> c2h5co + ho2',
 "chemkinKinetics": """
c2h5cho+o2=c2h5co+ho2                               1.005e+13 0.000     40.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.005e+13, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (40700, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + ch3co3 <=> c2h5co + ch3co3h',
 "chemkinKinetics": """
c2h5cho+ch3co3=c2h5co+ch3co3h                       3.010e+12 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + c2h3 <=> c2h5co + c2h4',
 "chemkinKinetics": """
c2h5cho+c2h3=c2h5co+c2h4                            1.700e+12 0.000     8.440    
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5 + co <=> c2h5co',
 "chemkinKinetics": """
c2h5+co=c2h5co                                      1.510e+11 0.000     4.810    
""",
 "rmgPyKinetics": Arrhenius(A=(1.51e+11, 'cm^3/(mol*s)'), n=0, Ea=(4810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3och3 <=> ch3 + ch3o',
 "chemkinKinetics": """
ch3och3(+M)=ch3+ch3o(+M)                            4.380e+21 -1.570    83.890   

    LOW/ 7.520e+15 0.000     42.790   /
    TROE/ 4.540e-01 1e-30     2.51e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(4.38e+21, 's^-1'), n=-1.57, Ea=(83890, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(A=(7.52e+15, 'cm^3/(mol*s)'), n=0, Ea=(42790, 'cal/mol'), T0=(1, 'K')),
    alpha = 0.454,
    T3 = (1e-30, 'K'),
    T1 = (2510, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3och3 + oh <=> ch3och2 + h2o',
 "chemkinKinetics": """
ch3och3+oh=ch3och2+h2o                              6.324e+06 2.000     -0.652   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.324e+06, 'cm^3/(mol*s)'),
    n = 2,
    Ea = (-651.7, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och3 + h <=> ch3och2 + h2',
 "chemkinKinetics": """
ch3och3+h=ch3och2+h2                                7.721e+06 2.090     3.384    
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.721e+06, 'cm^3/(mol*s)'),
    n = 2.09,
    Ea = (3384, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och3 + o <=> ch3och2 + oh',
 "chemkinKinetics": """
ch3och3+o=ch3och2+oh                                7.750e+08 1.360     2.250    
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.75e+08, 'cm^3/(mol*s)'),
    n = 1.36,
    Ea = (2250, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och3 + ho2 <=> ch3och2 + h2o2',
 "chemkinKinetics": """
ch3och3+ho2=ch3och2+h2o2                            1.680e+13 0.000     17.690   
""",
 "rmgPyKinetics": Arrhenius(A=(1.68e+13, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och3 + ch3o2 <=> ch3och2 + ch3o2h',
 "chemkinKinetics": """
ch3och3+ch3o2=ch3och2+ch3o2h                        3.120e+02 3.120     13.190   
""",
 "rmgPyKinetics": Arrhenius(A=(312, 'cm^3/(mol*s)'), n=3.12, Ea=(13190, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och3 + ch3 <=> ch3och2 + ch4',
 "chemkinKinetics": """
ch3och3+ch3=ch3och2+ch4                             1.445e-06 5.730     5.700    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.445e-06, 'cm^3/(mol*s)'),
    n = 5.73,
    Ea = (5700, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och3 + o2 <=> ch3och2 + ho2',
 "chemkinKinetics": """
ch3och3+o2=ch3och2+ho2                              4.100e+13 0.000     44.910   
""",
 "rmgPyKinetics": Arrhenius(A=(4.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(44910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och3 + ch3o <=> ch3och2 + ch3oh',
 "chemkinKinetics": """
ch3och3+ch3o=ch3och2+ch3oh                          6.020e+11 0.000     4.074    
""",
 "rmgPyKinetics": Arrhenius(A=(6.02e+11, 'cm^3/(mol*s)'), n=0, Ea=(4074, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och3 + ch3och2o2 <=> ch3och2 + ch3och2o2h',
 "chemkinKinetics": """
ch3och3+ch3och2o2=ch3och2+ch3och2o2h                5.000e+12 0.000     17.690   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och3 + o2cho <=> ch3och2 + ho2cho',
 "chemkinKinetics": """
ch3och3+o2cho=ch3och2+ho2cho                        4.425e+04 2.600     13.910   
""",
 "rmgPyKinetics": Arrhenius(A=(44250, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och3 + ocho <=> ch3och2 + hocho',
 "chemkinKinetics": """
ch3och3+ocho=ch3och2+hocho                          1.000e+13 0.000     17.690   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och2 <=> ch2o + ch3',
 "chemkinKinetics": """
ch3och2=ch2o+ch3                                    1.600e+13 0.000     25.500   
""",
 "rmgPyKinetics": Arrhenius(A=(1.6e+13, 's^-1'), n=0, Ea=(25500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3och2 + ch3o <=> ch3och3 + ch2o',
 "chemkinKinetics": """
ch3och2+ch3o=ch3och3+ch2o                           2.410e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3och2 + ch2o <=> ch3och3 + hco',
 "chemkinKinetics": """
ch3och2+ch2o=ch3och3+hco                            5.490e+03 2.800     5.862    
""",
 "rmgPyKinetics": Arrhenius(A=(5490, 'cm^3/(mol*s)'), n=2.8, Ea=(5862, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och2 + ch3cho <=> ch3och3 + ch3co',
 "chemkinKinetics": """
ch3och2+ch3cho=ch3och3+ch3co                        1.260e+12 0.000     8.499    
""",
 "rmgPyKinetics": Arrhenius(A=(1.26e+12, 'cm^3/(mol*s)'), n=0, Ea=(8499, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och2 + o2 <=> ch3och2o2',
 "chemkinKinetics": """
ch3och2+o2=ch3och2o2                                2.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3och2o2 + ch2o <=> ch3och2o2h + hco',
 "chemkinKinetics": """
ch3och2o2+ch2o=ch3och2o2h+hco                       1.000e+12 0.000     11.660   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och2o2 + ch3cho <=> ch3och2o2h + ch3co',
 "chemkinKinetics": """
ch3och2o2+ch3cho=ch3och2o2h+ch3co                   2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3och2o2 + ch3och2o2 => o2 + ch3och2o + ch3och2o',
 "chemkinKinetics": """
ch3och2o2+ch3och2o2=>o2+ch3och2o+ch3och2o           1.547e+23 -4.500    0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.547e+23, 'cm^3/(mol*s)'), n=-4.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ch3och2o + oh <=> ch3och2o2h',
 "chemkinKinetics": """
ch3och2o+oh=ch3och2o2h                              2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3o + ch2o <=> ch3och2o',
 "chemkinKinetics": """
ch3o+ch2o=ch3och2o                                  1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3och2o + o2 <=> ch3ocho + ho2',
 "chemkinKinetics": """
ch3och2o+o2=ch3ocho+ho2                             5.000e+10 0.000     0.500    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ch3ocho + h <=> ch3och2o',
 "chemkinKinetics": """
ch3ocho+h=ch3och2o                                  1.000e+13 0.000     7.838    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(7838, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3och2o2 <=> ch2och2o2h',
 "chemkinKinetics": """
ch3och2o2=ch2och2o2h                                6.000e+10 0.000     21.580   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+10, 's^-1'), n=0, Ea=(21580, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ch2och2o2h => oh + ch2o + ch2o',
 "chemkinKinetics": """
ch2och2o2h=>oh+ch2o+ch2o                            1.500e+13 0.000     19.760   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+13, 's^-1'), n=0, Ea=(19760, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'ch2och2o2h + o2 <=> o2ch2och2o2h',
 "chemkinKinetics": """
ch2och2o2h+o2=o2ch2och2o2h                          7.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'o2ch2och2o2h <=> ho2ch2ocho + oh',
 "chemkinKinetics": """
o2ch2och2o2h=ho2ch2ocho+oh                          4.000e+10 0.000     18.580   
""",
 "rmgPyKinetics": Arrhenius(A=(4e+10, 's^-1'), n=0, Ea=(18580, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ho2ch2ocho <=> och2ocho + oh',
 "chemkinKinetics": """
ho2ch2ocho=och2ocho+oh                              2.000e+16 0.000     41.500   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+16, 's^-1'), n=0, Ea=(41500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch2o + ocho <=> och2ocho',
 "chemkinKinetics": """
ch2o+ocho=och2ocho                                  1.250e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.25e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'och2ocho <=> hoch2oco',
 "chemkinKinetics": """
och2ocho=hoch2oco                                   1.000e+11 0.000     14.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'hoch2o + co <=> hoch2oco',
 "chemkinKinetics": """
hoch2o+co=hoch2oco                                  1.500e+11 0.000     4.800    
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2oh + co2 <=> hoch2oco',
 "chemkinKinetics": """
ch2oh+co2=hoch2oco                                  1.500e+11 0.000     35.720   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(35720, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2ocho + h <=> ch3ocho',
 "chemkinKinetics": """
ch2ocho+h=ch3ocho                                   1.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3oco + h <=> ch3ocho',
 "chemkinKinetics": """
ch3oco+h=ch3ocho                                    1.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3ocho <=> ch3oh + co',
 "chemkinKinetics": """
ch3ocho(+M)=ch3oh+co(+M)                            1.000e+14 0.000     62.500   

    LOW/ 6.143e+60 -12.070   75.400   /
    TROE/ 7.800e-01 8.28e+09  439       6.7e+08  /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(62500, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (6.143e+60, 'cm^3/(mol*s)'),
        n = -12.07,
        Ea = (75400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.78,
    T3 = (8.28e+09, 'K'),
    T1 = (438.9, 'K'),
    T2 = (6.7e+08, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3o + hco <=> ch3ocho',
 "chemkinKinetics": """
ch3o+hco=ch3ocho                                    3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3 + ocho <=> ch3ocho',
 "chemkinKinetics": """
ch3+ocho=ch3ocho                                    1.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3ocho + o2 <=> ch3oco + ho2',
 "chemkinKinetics": """
ch3ocho+o2=ch3oco+ho2                               1.000e+13 0.000     49.700   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(49700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + o2 <=> ch2ocho + ho2',
 "chemkinKinetics": """
ch3ocho+o2=ch2ocho+ho2                              2.050e+13 0.000     52.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.05e+13, 'cm^3/(mol*s)'), n=0, Ea=(52000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + oh <=> ch3oco + h2o',
 "chemkinKinetics": """
ch3ocho+oh=ch3oco+h2o                               1.580e+07 1.800     0.934    
""",
 "rmgPyKinetics": Arrhenius(A=(1.58e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(934, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + oh <=> ch2ocho + h2o',
 "chemkinKinetics": """
ch3ocho+oh=ch2ocho+h2o                              5.270e+09 0.970     1.586    
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.27e+09, 'cm^3/(mol*s)'),
    n = 0.97,
    Ea = (1586, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + ho2 <=> ch3oco + h2o2',
 "chemkinKinetics": """
ch3ocho+ho2=ch3oco+h2o2                             4.820e+03 2.600     13.910   
""",
 "rmgPyKinetics": Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + ho2 <=> ch2ocho + h2o2',
 "chemkinKinetics": """
ch3ocho+ho2=ch2ocho+h2o2                            2.380e+04 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + o <=> ch3oco + oh',
 "chemkinKinetics": """
ch3ocho+o=ch3oco+oh                                 2.755e+05 2.450     2.830    
""",
 "rmgPyKinetics": Arrhenius(A=(275500, 'cm^3/(mol*s)'), n=2.45, Ea=(2830, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + o <=> ch2ocho + oh',
 "chemkinKinetics": """
ch3ocho+o=ch2ocho+oh                                9.800e+05 2.430     4.750    
""",
 "rmgPyKinetics": Arrhenius(A=(980000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + h <=> ch3oco + h2',
 "chemkinKinetics": """
ch3ocho+h=ch3oco+h2                                 6.500e+05 2.400     4.471    
""",
 "rmgPyKinetics": Arrhenius(A=(650000, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + h <=> ch2ocho + h2',
 "chemkinKinetics": """
ch3ocho+h=ch2ocho+h2                                6.650e+05 2.540     6.756    
""",
 "rmgPyKinetics": Arrhenius(A=(665000, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + ch3 <=> ch3oco + ch4',
 "chemkinKinetics": """
ch3ocho+ch3=ch3oco+ch4                              7.550e-01 3.460     5.481    
""",
 "rmgPyKinetics": Arrhenius(A=(0.755, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + ch3 <=> ch2ocho + ch4',
 "chemkinKinetics": """
ch3ocho+ch3=ch2ocho+ch4                             4.520e-01 3.650     7.154    
""",
 "rmgPyKinetics": Arrhenius(A=(0.452, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + ch3o <=> ch3oco + ch3oh',
 "chemkinKinetics": """
ch3ocho+ch3o=ch3oco+ch3oh                           5.480e+11 0.000     5.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5.48e+11, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + ch3o <=> ch2ocho + ch3oh',
 "chemkinKinetics": """
ch3ocho+ch3o=ch2ocho+ch3oh                          2.170e+11 0.000     6.458    
""",
 "rmgPyKinetics": Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + ch3o2 <=> ch3oco + ch3o2h',
 "chemkinKinetics": """
ch3ocho+ch3o2=ch3oco+ch3o2h                         4.820e+03 2.600     13.910   
""",
 "rmgPyKinetics": Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + ch3o2 <=> ch2ocho + ch3o2h',
 "chemkinKinetics": """
ch3ocho+ch3o2=ch2ocho+ch3o2h                        2.380e+04 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + hco <=> ch3oco + ch2o',
 "chemkinKinetics": """
ch3ocho+hco=ch3oco+ch2o                             5.400e+06 1.900     17.010   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.4e+06, 'cm^3/(mol*s)'),
    n = 1.9,
    Ea = (17010, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3ocho + hco <=> ch2ocho + ch2o',
 "chemkinKinetics": """
ch3ocho+hco=ch2ocho+ch2o                            1.025e+05 2.500     18.430   
""",
 "rmgPyKinetics": Arrhenius(A=(102500, 'cm^3/(mol*s)'), n=2.5, Ea=(18430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oco <=> ch2ocho',
 "chemkinKinetics": """
ch3oco=ch2ocho                                      1.629e+12 -0.180    40.670   
""",
 "rmgPyKinetics": Arrhenius(A=(1.629e+12, 's^-1'), n=-0.18, Ea=(40670, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ch3 + co2 <=> ch3oco',
 "chemkinKinetics": """
ch3+co2=ch3oco                                      4.760e+07 1.540     34.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.76e+07, 'cm^3/(mol*s)'),
    n = 1.54,
    Ea = (34700, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3o + co <=> ch3oco',
 "chemkinKinetics": """
ch3o+co=ch3oco                                      1.550e+06 2.020     5.730    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.55e+06, 'cm^3/(mol*s)'),
    n = 2.02,
    Ea = (5730, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2o + hco <=> ch2ocho',
 "chemkinKinetics": """
ch2o+hco=ch2ocho                                    1.500e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h8 <=> ch3 + c2h5',
 "chemkinKinetics": """
c3h8(+M)=ch3+c2h5(+M)                               1.290e+37 -5.840    97.380   
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ he/0.70/ 
    LOW/ 5.640e+74 -15.740   98.714   /
    TROE/ 3.100e-01 50        3e+03     9e+03    /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.29e+37, 's^-1'), n=-5.84, Ea=(97380, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (5.64e+74, 'cm^3/(mol*s)'),
        n = -15.74,
        Ea = (98714, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.31,
    T3 = (50, 'K'),
    T1 = (3000, 'K'),
    T2 = (9000, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[He]'): 0.7,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'nc3h7 + h <=> c3h8',
 "chemkinKinetics": """
nc3h7+h=c3h8                                        1.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic3h7 + h <=> c3h8',
 "chemkinKinetics": """
ic3h7+h=c3h8                                        1.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h8 + o2 <=> ic3h7 + ho2',
 "chemkinKinetics": """
c3h8+o2=ic3h7+ho2                                   2.000e+13 0.000     49.640   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49640, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + o2 <=> nc3h7 + ho2',
 "chemkinKinetics": """
c3h8+o2=nc3h7+ho2                                   6.000e+13 0.000     52.290   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52290, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h + c3h8 <=> h2 + ic3h7',
 "chemkinKinetics": """
h+c3h8=h2+ic3h7                                     1.300e+06 2.400     4.471    
""",
 "rmgPyKinetics": Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h + c3h8 <=> h2 + nc3h7',
 "chemkinKinetics": """
h+c3h8=h2+nc3h7                                     3.490e+05 2.690     6.450    
""",
 "rmgPyKinetics": Arrhenius(A=(349000, 'cm^3/(mol*s)'), n=2.69, Ea=(6450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + o <=> ic3h7 + oh',
 "chemkinKinetics": """
c3h8+o=ic3h7+oh                                     5.490e+05 2.500     3.140    
""",
 "rmgPyKinetics": Arrhenius(A=(549000, 'cm^3/(mol*s)'), n=2.5, Ea=(3140, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + o <=> nc3h7 + oh',
 "chemkinKinetics": """
c3h8+o=nc3h7+oh                                     3.710e+06 2.400     5.505    
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.71e+06, 'cm^3/(mol*s)'),
    n = 2.4,
    Ea = (5505, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + oh <=> nc3h7 + h2o',
 "chemkinKinetics": """
c3h8+oh=nc3h7+h2o                                   1.054e+10 0.970     1.586    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.054e+10, 'cm^3/(mol*s)'),
    n = 0.97,
    Ea = (1586, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + oh <=> ic3h7 + h2o',
 "chemkinKinetics": """
c3h8+oh=ic3h7+h2o                                   4.670e+07 1.610     -0.035   
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.67e+07, 'cm^3/(mol*s)'),
    n = 1.61,
    Ea = (-35, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + ho2 <=> ic3h7 + h2o2',
 "chemkinKinetics": """
c3h8+ho2=ic3h7+h2o2                                 6.320e+01 3.370     13.720   
""",
 "rmgPyKinetics": Arrhenius(A=(63.2, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + ho2 <=> nc3h7 + h2o2',
 "chemkinKinetics": """
c3h8+ho2=nc3h7+h2o2                                 4.080e+01 3.590     17.160   
""",
 "rmgPyKinetics": Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3 + c3h8 <=> ch4 + ic3h7',
 "chemkinKinetics": """
ch3+c3h8=ch4+ic3h7                                  6.400e+04 2.170     7.520    
""",
 "rmgPyKinetics": Arrhenius(A=(64000, 'cm^3/(mol*s)'), n=2.17, Ea=(7520, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3 + c3h8 <=> ch4 + nc3h7',
 "chemkinKinetics": """
ch3+c3h8=ch4+nc3h7                                  9.040e-01 3.650     7.154    
""",
 "rmgPyKinetics": Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7 + c3h8 <=> nc3h7 + c3h8',
 "chemkinKinetics": """
ic3h7+c3h8=nc3h7+c3h8                               3.000e+10 0.000     12.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(12900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3 + c3h8 <=> c2h4 + ic3h7',
 "chemkinKinetics": """
c2h3+c3h8=c2h4+ic3h7                                1.000e+11 0.000     10.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3 + c3h8 <=> c2h4 + nc3h7',
 "chemkinKinetics": """
c2h3+c3h8=c2h4+nc3h7                                1.000e+11 0.000     10.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5 + c3h8 <=> c2h6 + ic3h7',
 "chemkinKinetics": """
c2h5+c3h8=c2h6+ic3h7                                1.000e+11 0.000     10.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5 + c3h8 <=> c2h6 + nc3h7',
 "chemkinKinetics": """
c2h5+c3h8=c2h6+nc3h7                                1.000e+11 0.000     10.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + c3h5-a <=> nc3h7 + c3h6',
 "chemkinKinetics": """
c3h8+c3h5-a=nc3h7+c3h6                              7.940e+11 0.000     20.500   
""",
 "rmgPyKinetics": Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + c3h5-a <=> ic3h7 + c3h6',
 "chemkinKinetics": """
c3h8+c3h5-a=ic3h7+c3h6                              7.940e+11 0.000     16.200   
""",
 "rmgPyKinetics": Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(16200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + ch3o <=> nc3h7 + ch3oh',
 "chemkinKinetics": """
c3h8+ch3o=nc3h7+ch3oh                               3.000e+11 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + ch3o <=> ic3h7 + ch3oh',
 "chemkinKinetics": """
c3h8+ch3o=ic3h7+ch3oh                               3.000e+11 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + c3h8 <=> ch3o2h + nc3h7',
 "chemkinKinetics": """
ch3o2+c3h8=ch3o2h+nc3h7                             1.386e+00 3.970     18.280   
""",
 "rmgPyKinetics": Arrhenius(A=(1.386, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + c3h8 <=> ch3o2h + ic3h7',
 "chemkinKinetics": """
ch3o2+c3h8=ch3o2h+ic3h7                             1.019e+01 3.580     14.810   
""",
 "rmgPyKinetics": Arrhenius(A=(10.19, 'cm^3/(mol*s)'), n=3.58, Ea=(14810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5o2 + c3h8 <=> c2h5o2h + nc3h7',
 "chemkinKinetics": """
c2h5o2+c3h8=c2h5o2h+nc3h7                           1.386e+00 3.970     18.280   
""",
 "rmgPyKinetics": Arrhenius(A=(1.386, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5o2 + c3h8 <=> c2h5o2h + ic3h7',
 "chemkinKinetics": """
c2h5o2+c3h8=c2h5o2h+ic3h7                           1.019e+01 3.580     14.810   
""",
 "rmgPyKinetics": Arrhenius(A=(10.19, 'cm^3/(mol*s)'), n=3.58, Ea=(14810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + c3h8 <=> nc3h7o2h + nc3h7',
 "chemkinKinetics": """
nc3h7o2+c3h8=nc3h7o2h+nc3h7                         1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + c3h8 <=> nc3h7o2h + ic3h7',
 "chemkinKinetics": """
nc3h7o2+c3h8=nc3h7o2h+ic3h7                         2.000e+12 0.000     17.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + c3h8 <=> ic3h7o2h + nc3h7',
 "chemkinKinetics": """
ic3h7o2+c3h8=ic3h7o2h+nc3h7                         1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + c3h8 <=> ic3h7o2h + ic3h7',
 "chemkinKinetics": """
ic3h7o2+c3h8=ic3h7o2h+ic3h7                         2.000e+12 0.000     17.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + ch3co3 <=> ic3h7 + ch3co3h',
 "chemkinKinetics": """
c3h8+ch3co3=ic3h7+ch3co3h                           2.000e+12 0.000     17.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + ch3co3 <=> nc3h7 + ch3co3h',
 "chemkinKinetics": """
c3h8+ch3co3=nc3h7+ch3co3h                           1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + o2cho <=> nc3h7 + ho2cho',
 "chemkinKinetics": """
c3h8+o2cho=nc3h7+ho2cho                             5.520e+04 2.550     16.480   
""",
 "rmgPyKinetics": Arrhenius(A=(55200, 'cm^3/(mol*s)'), n=2.55, Ea=(16480, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h8 + o2cho <=> ic3h7 + ho2cho',
 "chemkinKinetics": """
c3h8+o2cho=ic3h7+ho2cho                             1.475e+04 2.600     13.910   
""",
 "rmgPyKinetics": Arrhenius(A=(14750, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h + c3h6 <=> ic3h7',
 "chemkinKinetics": """
h+c3h6=ic3h7                                        4.240e+11 0.510     1.230    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.24e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (1230, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h7 + h <=> c2h5 + ch3',
 "chemkinKinetics": """
ic3h7+h=c2h5+ch3                                    2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic3h7 + o2 <=> c3h6 + ho2',
 "chemkinKinetics": """
ic3h7+o2=c3h6+ho2                                   4.500e-19 0.000     5.020    
""",
 "rmgPyKinetics": Arrhenius(A=(4.5e-19, 'cm^3/(mol*s)'), n=0, Ea=(5020, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic3h7 + oh <=> c3h6 + h2o',
 "chemkinKinetics": """
ic3h7+oh=c3h6+h2o                                   2.410e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic3h7 + o <=> ch3coch3 + h',
 "chemkinKinetics": """
ic3h7+o=ch3coch3+h                                  4.818e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.818e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic3h7 + o <=> ch3cho + ch3',
 "chemkinKinetics": """
ic3h7+o=ch3cho+ch3                                  4.818e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.818e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3 + c2h4 <=> nc3h7',
 "chemkinKinetics": """
ch3+c2h4=nc3h7                                      1.760e+04 2.480     6.130    
""",
 "rmgPyKinetics": Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'h + c3h6 <=> nc3h7',
 "chemkinKinetics": """
h+c3h6=nc3h7                                        2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'nc3h7 + o2 <=> c3h6 + ho2',
 "chemkinKinetics": """
nc3h7+o2=c3h6+ho2                                   3.000e-19 0.000     3.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e-19, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h5cho + nc3h7 <=> c2h5co + c3h8',
 "chemkinKinetics": """
c2h5cho+nc3h7=c2h5co+c3h8                           1.700e+12 0.000     8.440    
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + ic3h7 <=> c2h5co + c3h8',
 "chemkinKinetics": """
c2h5cho+ic3h7=c2h5co+c3h8                           1.700e+12 0.000     8.440    
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5cho + c3h5-a <=> c2h5co + c3h6',
 "chemkinKinetics": """
c2h5cho+c3h5-a=c2h5co+c3h6                          1.700e+12 0.000     8.440    
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3 + ch3 <=> c3h6',
 "chemkinKinetics": """
c2h3+ch3(+M)=c3h6(+M)                               2.500e+13 0.000     0.000    

    LOW/ 4.270e+58 -11.940   9.770    /
    TROE/ 1.750e-01 1.34e+03  6e+04     1.01e+04 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (4.27e+58, 'cm^6/(mol^2*s)'),
        n = -11.94,
        Ea = (9769.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.175,
    T3 = (1340.6, 'K'),
    T1 = (60000, 'K'),
    T2 = (10140, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h5-a + h <=> c3h6',
 "chemkinKinetics": """
c3h5-a+h(+M)=c3h6(+M)                               2.000e+14 0.000     0.000    
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ 
    LOW/ 1.330e+60 -12.000   5.968    /
    TROE/ 2.000e-02 1.1e+03   1.1e+03   6.86e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.33e+60, 'cm^6/(mol^2*s)'),
        n = -12,
        Ea = (5967.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.02,
    T3 = (1096.6, 'K'),
    T1 = (1096.6, 'K'),
    T2 = (6859.5, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h6 <=> c3h5-s + h',
 "chemkinKinetics": """
c3h6=c3h5-s+h                                       7.710e+69 -16.090   140.000  
""",
 "rmgPyKinetics": Arrhenius(A=(7.71e+69, 's^-1'), n=-16.09, Ea=(140000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h6 <=> c3h5-t + h',
 "chemkinKinetics": """
c3h6=c3h5-t+h                                       5.620e+71 -16.580   139.300  
""",
 "rmgPyKinetics": Arrhenius(A=(5.62e+71, 's^-1'), n=-16.58, Ea=(139300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h6 + o <=> c2h5 + hco',
 "chemkinKinetics": """
c3h6+o=c2h5+hco                                     1.580e+07 1.760     -1.216   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.58e+07, 'cm^3/(mol*s)'),
    n = 1.76,
    Ea = (-1216, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6 + o => ch2co + ch3 + h',
 "chemkinKinetics": """
c3h6+o=>ch2co+ch3+h                                 2.500e+07 1.760     0.076    
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6 + o => ch3chco + h + h',
 "chemkinKinetics": """
c3h6+o=>ch3chco+h+h                                 2.500e+07 1.760     0.076    
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6 + o <=> c3h5-a + oh',
 "chemkinKinetics": """
c3h6+o=c3h5-a+oh                                    5.240e+11 0.700     5.884    
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.24e+11, 'cm^3/(mol*s)'),
    n = 0.7,
    Ea = (5884, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + o <=> c3h5-s + oh',
 "chemkinKinetics": """
c3h6+o=c3h5-s+oh                                    1.200e+11 0.700     8.959    
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0.7, Ea=(8959, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + o <=> c3h5-t + oh',
 "chemkinKinetics": """
c3h6+o=c3h5-t+oh                                    6.030e+10 0.700     7.632    
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.03e+10, 'cm^3/(mol*s)'),
    n = 0.7,
    Ea = (7632, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + oh <=> c3h5-a + h2o',
 "chemkinKinetics": """
c3h6+oh=c3h5-a+h2o                                  1.970e+06 2.200     0.540    
""",
 "rmgPyKinetics": Arrhenius(A=(1.97e+06, 'cm^3/(mol*s)'), n=2.2, Ea=(540, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + oh <=> c3h5-s + h2o',
 "chemkinKinetics": """
c3h6+oh=c3h5-s+h2o                                  2.110e+06 2.000     2.778    
""",
 "rmgPyKinetics": Arrhenius(A=(2.11e+06, 'cm^3/(mol*s)'), n=2, Ea=(2778, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + oh <=> c3h5-t + h2o',
 "chemkinKinetics": """
c3h6+oh=c3h5-t+h2o                                  1.110e+06 2.000     1.451    
""",
 "rmgPyKinetics": Arrhenius(A=(1.11e+06, 'cm^3/(mol*s)'), n=2, Ea=(1451, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + ho2 <=> c3h5-a + h2o2',
 "chemkinKinetics": """
c3h6+ho2=c3h5-a+h2o2                                2.700e+04 2.500     12.340   
""",
 "rmgPyKinetics": Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + ho2 <=> c3h5-s + h2o2',
 "chemkinKinetics": """
c3h6+ho2=c3h5-s+h2o2                                1.800e+04 2.500     27.620   
""",
 "rmgPyKinetics": Arrhenius(A=(18000, 'cm^3/(mol*s)'), n=2.5, Ea=(27620, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + ho2 <=> c3h5-t + h2o2',
 "chemkinKinetics": """
c3h6+ho2=c3h5-t+h2o2                                9.000e+03 2.500     23.590   
""",
 "rmgPyKinetics": Arrhenius(A=(9000, 'cm^3/(mol*s)'), n=2.5, Ea=(23590, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + h <=> c3h5-a + h2',
 "chemkinKinetics": """
c3h6+h=c3h5-a+h2                                    1.730e+05 2.500     2.492    
""",
 "rmgPyKinetics": Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + h <=> c3h5-s + h2',
 "chemkinKinetics": """
c3h6+h=c3h5-s+h2                                    8.040e+05 2.500     12.280   
""",
 "rmgPyKinetics": Arrhenius(A=(804000, 'cm^3/(mol*s)'), n=2.5, Ea=(12280, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + h <=> c3h5-t + h2',
 "chemkinKinetics": """
c3h6+h=c3h5-t+h2                                    4.050e+05 2.500     9.794    
""",
 "rmgPyKinetics": Arrhenius(A=(405000, 'cm^3/(mol*s)'), n=2.5, Ea=(9794, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + h <=> c2h4 + ch3',
 "chemkinKinetics": """
c3h6+h=c2h4+ch3                                     1.000e+00 0.000     0.000    
    PLOG/ 0.100     8.800e+16 -1.050    6.461    /
    PLOG/ 1.000     8.000e+21 -2.390    11.180   /
    PLOG/ 10.000    3.300e+24 -3.040    15.610   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (8.8e+16, 'cm^3/(mol*s)'),
            n = -1.05,
            Ea = (6461, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (8e+21, 'cm^3/(mol*s)'),
            n = -2.39,
            Ea = (11180, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.3e+24, 'cm^3/(mol*s)'),
            n = -3.04,
            Ea = (15610, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6 + o2 <=> c3h5-a + ho2',
 "chemkinKinetics": """
c3h6+o2=c3h5-a+ho2                                  4.000e+12 0.000     39.900   
""",
 "rmgPyKinetics": Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + o2 <=> c3h5-s + ho2',
 "chemkinKinetics": """
c3h6+o2=c3h5-s+ho2                                  2.000e+12 0.000     62.900   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(62900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + o2 <=> c3h5-t + ho2',
 "chemkinKinetics": """
c3h6+o2=c3h5-t+ho2                                  1.400e+12 0.000     60.700   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(60700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + ch3 <=> c3h5-a + ch4',
 "chemkinKinetics": """
c3h6+ch3=c3h5-a+ch4                                 2.210e+00 3.500     5.675    
""",
 "rmgPyKinetics": Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + ch3 <=> c3h5-s + ch4',
 "chemkinKinetics": """
c3h6+ch3=c3h5-s+ch4                                 1.348e+00 3.500     12.850   
""",
 "rmgPyKinetics": Arrhenius(A=(1.348, 'cm^3/(mol*s)'), n=3.5, Ea=(12850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + ch3 <=> c3h5-t + ch4',
 "chemkinKinetics": """
c3h6+ch3=c3h5-t+ch4                                 8.400e-01 3.500     11.660   
""",
 "rmgPyKinetics": Arrhenius(A=(0.84, 'cm^3/(mol*s)'), n=3.5, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + c2h5 <=> c3h5-a + c2h6',
 "chemkinKinetics": """
c3h6+c2h5=c3h5-a+c2h6                               1.000e+11 0.000     9.800    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + ch3co3 <=> c3h5-a + ch3co3h',
 "chemkinKinetics": """
c3h6+ch3co3=c3h5-a+ch3co3h                          3.240e+11 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + ch3o2 <=> c3h5-a + ch3o2h',
 "chemkinKinetics": """
c3h6+ch3o2=c3h5-a+ch3o2h                            3.240e+11 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + ho2 <=> c3h6o1-2 + oh',
 "chemkinKinetics": """
c3h6+ho2=c3h6o1-2+oh                                1.290e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.29e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6 + c2h5o2 <=> c3h5-a + c2h5o2h',
 "chemkinKinetics": """
c3h6+c2h5o2=c3h5-a+c2h5o2h                          3.240e+11 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + nc3h7o2 <=> c3h5-a + nc3h7o2h',
 "chemkinKinetics": """
c3h6+nc3h7o2=c3h5-a+nc3h7o2h                        3.240e+11 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + ic3h7o2 <=> c3h5-a + ic3h7o2h',
 "chemkinKinetics": """
c3h6+ic3h7o2=c3h5-a+ic3h7o2h                        3.240e+11 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + oh <=> c3h6oh',
 "chemkinKinetics": """
c3h6+oh=c3h6oh                                      9.930e+11 0.000     -0.960   
""",
 "rmgPyKinetics": Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6oh + o2 <=> hoc3h6o2',
 "chemkinKinetics": """
c3h6oh+o2=hoc3h6o2                                  1.200e+11 0.000     -1.100   
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'hoc3h6o2 => ch3cho + ch2o + oh',
 "chemkinKinetics": """
hoc3h6o2=>ch3cho+ch2o+oh                            1.250e+10 0.000     18.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(18900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + ch3 <=> c3h5-a',
 "chemkinKinetics": """
c2h2+ch3=c3h5-a                                     1.000e+00 0.000     0.000    
    PLOG/ 0.100     8.200e+53 -13.320   33.200   /
    PLOG/ 1.000     2.680e+53 -12.820   35.730   /
    PLOG/ 2.000     3.640e+52 -12.460   36.127   /
    PLOG/ 5.000     1.040e+51 -11.890   36.476   /
    PLOG/ 10.000    4.400e+49 -11.400   36.700   /
    PLOG/ 100.000   3.800e+44 -9.630    37.600   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (8.2e+53, 'cm^3/(mol*s)'),
            n = -13.32,
            Ea = (33200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.68e+53, 'cm^3/(mol*s)'),
            n = -12.82,
            Ea = (35730, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.64e+52, 'cm^3/(mol*s)'),
            n = -12.46,
            Ea = (36127, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.04e+51, 'cm^3/(mol*s)'),
            n = -11.89,
            Ea = (36476, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.4e+49, 'cm^3/(mol*s)'),
            n = -11.4,
            Ea = (36700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.8e+44, 'cm^3/(mol*s)'),
            n = -9.63,
            Ea = (37600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-a + h <=> c3h5-a',
 "chemkinKinetics": """
c3h4-a+h=c3h5-a                                     1.000e+00 0.000     0.000    
    PLOG/ 0.100     9.600e+61 -14.670   26.000   /
    PLOG/ 1.000     1.520e+59 -13.540   26.949   /
    PLOG/ 2.000     3.780e+57 -12.980   26.785   /
    PLOG/ 5.000     7.340e+54 -12.090   26.187   /
    PLOG/ 10.000    2.400e+52 -11.300   25.400   /
    PLOG/ 100.000   6.900e+41 -8.060    21.300   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (9.6e+61, 'cm^3/(mol*s)'),
            n = -14.67,
            Ea = (26000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.52e+59, 'cm^3/(mol*s)'),
            n = -13.54,
            Ea = (26949, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+57, 'cm^3/(mol*s)'),
            n = -12.98,
            Ea = (26785, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (7.34e+54, 'cm^3/(mol*s)'),
            n = -12.09,
            Ea = (26187, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.4e+52, 'cm^3/(mol*s)'),
            n = -11.3,
            Ea = (25400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (6.9e+41, 'cm^3/(mol*s)'),
            n = -8.06,
            Ea = (21300, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h5-a + ho2 <=> c3h5o + oh',
 "chemkinKinetics": """
c3h5-a+ho2=c3h5o+oh                                 7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c3h5-a + ch3o2 <=> c3h5o + ch3o',
 "chemkinKinetics": """
c3h5-a+ch3o2=c3h5o+ch3o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c3h5-a + h <=> c3h4-a + h2',
 "chemkinKinetics": """
c3h5-a+h=c3h4-a+h2                                  1.232e+03 3.035     2.582    
""",
 "rmgPyKinetics": Arrhenius(A=(1232, 'cm^3/(mol*s)'), n=3.035, Ea=(2582, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-a + o <=> c2h3cho + h',
 "chemkinKinetics": """
c3h5-a+o=c2h3cho+h                                  6.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-a + oh => c2h3cho + h + h',
 "chemkinKinetics": """
c3h5-a+oh=>c2h3cho+h+h                              1.000e+00 0.000     0.000    
    PLOG/ 0.100     5.300e+37 -6.710    29.306   /
    PLOG/ 1.000     4.200e+32 -5.160    30.126   /
    PLOG/ 10.000    1.600e+20 -1.560    26.330   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.3e+37, 'cm^3/(mol*s)'),
            n = -6.71,
            Ea = (29306, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.2e+32, 'cm^3/(mol*s)'),
            n = -5.16,
            Ea = (30126, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.6e+20, 'cm^3/(mol*s)'),
            n = -1.56,
            Ea = (26330, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-a + oh <=> c3h4-a + h2o',
 "chemkinKinetics": """
c3h5-a+oh=c3h4-a+h2o                                6.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-a + ch3 <=> c3h4-a + ch4',
 "chemkinKinetics": """
c3h5-a+ch3=c3h4-a+ch4                               3.000e+12 -0.320    -0.131   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=-0.32, Ea=(-131, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-a + c2h5 <=> c2h6 + c3h4-a',
 "chemkinKinetics": """
c3h5-a+c2h5=c2h6+c3h4-a                             4.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-a + c2h5 <=> c2h4 + c3h6',
 "chemkinKinetics": """
c3h5-a+c2h5=c2h4+c3h6                               4.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-a + c2h3 <=> c2h4 + c3h4-a',
 "chemkinKinetics": """
c3h5-a+c2h3=c2h4+c3h4-a                             1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-a + c3h5-a <=> c3h4-a + c3h6',
 "chemkinKinetics": """
c3h5-a+c3h5-a=c3h4-a+c3h6                           8.430e+10 0.000     -0.262   
""",
 "rmgPyKinetics": Arrhenius(A=(8.43e+10, 'cm^3/(mol*s)'), n=0, Ea=(-262, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-a + o2 <=> c3h4-a + ho2',
 "chemkinKinetics": """
c3h5-a+o2=c3h4-a+ho2                                1.000e+00 0.000     0.000    
    PLOG/ 1.000     4.990e+15 -1.400    22.428   /
    PLOG/ 10.000    2.180e+21 -2.850    30.755   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (4.99e+15, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (22428, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.18e+21, 'cm^3/(mol*s)'),
            n = -2.85,
            Ea = (30755, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-a + o2 <=> ch3co + ch2o',
 "chemkinKinetics": """
c3h5-a+o2=ch3co+ch2o                                1.000e+00 0.000     0.000    
    PLOG/ 1.000     1.190e+15 -1.010    20.128   /
    PLOG/ 10.000    7.140e+15 -1.210    21.046   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (1.19e+15, 'cm^3/(mol*s)'),
            n = -1.01,
            Ea = (20128, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (7.14e+15, 'cm^3/(mol*s)'),
            n = -1.21,
            Ea = (21046, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-a + o2 <=> c2h3cho + oh',
 "chemkinKinetics": """
c3h5-a+o2=c2h3cho+oh                                1.000e+00 0.000     0.000    
    PLOG/ 1.000     1.820e+13 -0.410    22.859   /
    PLOG/ 10.000    2.470e+13 -0.450    23.017   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (1.82e+13, 'cm^3/(mol*s)'),
            n = -0.41,
            Ea = (22859, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.47e+13, 'cm^3/(mol*s)'),
            n = -0.45,
            Ea = (23017, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-a + hco <=> c3h6 + co',
 "chemkinKinetics": """
c3h5-a+hco=c3h6+co                                  6.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3 + ch3 <=> c3h5-a + h',
 "chemkinKinetics": """
c2h3+ch3=c3h5-a+h                                   1.500e+24 -2.830    18.618   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.5e+24, 'cm^3/(mol*s)'),
    n = -2.83,
    Ea = (18618, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-a <=> c3h5-t',
 "chemkinKinetics": """
c3h5-a=c3h5-t                                       1.000e+00 0.000     0.000    
    PLOG/ 0.100     3.900e+59 -15.420   75.400   /
    PLOG/ 1.000     7.060e+56 -14.080   75.868   /
    PLOG/ 2.000     4.800e+55 -13.590   75.949   /
    PLOG/ 5.000     4.860e+53 -12.810   75.883   /
    PLOG/ 10.000    6.400e+51 -12.120   75.700   /
    PLOG/ 100.000   2.800e+43 -9.270    74.000   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(3.9e+59, 's^-1'), n=-15.42, Ea=(75400, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(7.06e+56, 's^-1'), n=-14.08, Ea=(75868, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.8e+55, 's^-1'), n=-13.59, Ea=(75949, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.86e+53, 's^-1'), n=-12.81, Ea=(75883, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(6.4e+51, 's^-1'), n=-12.12, Ea=(75700, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.8e+43, 's^-1'), n=-9.27, Ea=(74000, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c3h5-a <=> c3h5-s',
 "chemkinKinetics": """
c3h5-a=c3h5-s                                       1.000e+00 0.000     0.000    
    PLOG/ 0.100     1.300e+55 -14.530   73.800   /
    PLOG/ 1.000     5.000e+51 -13.020   73.300   /
    PLOG/ 10.000    9.700e+48 -11.730   73.700   /
    PLOG/ 100.000   4.860e+44 -9.840    73.400   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(1.3e+55, 's^-1'), n=-14.53, Ea=(73800, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5e+51, 's^-1'), n=-13.02, Ea=(73300, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(9.7e+48, 's^-1'), n=-11.73, Ea=(73700, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.86e+44, 's^-1'), n=-9.84, Ea=(73400, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c2h2 + ch3 <=> c3h5-s',
 "chemkinKinetics": """
c2h2+ch3=c3h5-s                                     1.000e+00 0.000     0.000    
    PLOG/ 0.100     1.400e+32 -7.140    10.000   /
    PLOG/ 1.000     3.200e+35 -7.760    13.300   /
    PLOG/ 10.000    2.400e+38 -8.210    17.100   /
    PLOG/ 100.000   1.400e+39 -8.060    20.200   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (1.4e+32, 'cm^3/(mol*s)'),
            n = -7.14,
            Ea = (10000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.2e+35, 'cm^3/(mol*s)'),
            n = -7.76,
            Ea = (13300, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.4e+38, 'cm^3/(mol*s)'),
            n = -8.21,
            Ea = (17100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.4e+39, 'cm^3/(mol*s)'),
            n = -8.06,
            Ea = (20200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h5-s + o2 <=> ch3cho + hco',
 "chemkinKinetics": """
c3h5-s+o2=ch3cho+hco                                1.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-s + h <=> c3h4-a + h2',
 "chemkinKinetics": """
c3h5-s+h=c3h4-a+h2                                  3.333e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.333e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-s + ch3 <=> c3h4-a + ch4',
 "chemkinKinetics": """
c3h5-s+ch3=c3h4-a+ch4                               1.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + ch3 <=> c3h5-t',
 "chemkinKinetics": """
c2h2+ch3=c3h5-t                                     1.000e+00 0.000     0.000    
    PLOG/ 0.100     6.800e+20 -4.160    18.000   /
    PLOG/ 1.000     4.990e+22 -4.390    18.850   /
    PLOG/ 2.000     6.000e+23 -4.600    19.571   /
    PLOG/ 5.000     7.310e+25 -5.060    21.150   /
    PLOG/ 10.000    9.300e+27 -5.550    22.900   /
    PLOG/ 100.000   3.800e+36 -7.580    31.300   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (6.8e+20, 'cm^3/(mol*s)'),
            n = -4.16,
            Ea = (18000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.99e+22, 'cm^3/(mol*s)'),
            n = -4.39,
            Ea = (18850, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(A=(6e+23, 'cm^3/(mol*s)'), n=-4.6, Ea=(19571, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(
            A = (7.31e+25, 'cm^3/(mol*s)'),
            n = -5.06,
            Ea = (21150, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (9.3e+27, 'cm^3/(mol*s)'),
            n = -5.55,
            Ea = (22900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.8e+36, 'cm^3/(mol*s)'),
            n = -7.58,
            Ea = (31300, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-a + h <=> c3h5-t',
 "chemkinKinetics": """
c3h4-a+h=c3h5-t                                     1.000e+00 0.000     0.000    
    PLOG/ 0.100     9.200e+38 -8.650    7.000    /
    PLOG/ 1.000     9.460e+42 -9.430    11.190   /
    PLOG/ 2.000     8.470e+43 -9.590    12.462   /
    PLOG/ 5.000     6.980e+44 -9.700    14.032   /
    PLOG/ 10.000    1.500e+45 -9.690    15.100   /
    PLOG/ 100.000   1.800e+43 -8.780    16.800   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (9.2e+38, 'cm^3/(mol*s)'),
            n = -8.65,
            Ea = (7000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (9.46e+42, 'cm^3/(mol*s)'),
            n = -9.43,
            Ea = (11190, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (8.47e+43, 'cm^3/(mol*s)'),
            n = -9.59,
            Ea = (12462, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (6.98e+44, 'cm^3/(mol*s)'),
            n = -9.7,
            Ea = (14032, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.5e+45, 'cm^3/(mol*s)'),
            n = -9.69,
            Ea = (15100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.8e+43, 'cm^3/(mol*s)'),
            n = -8.78,
            Ea = (16800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h4-p + h <=> c3h5-t',
 "chemkinKinetics": """
c3h4-p+h=c3h5-t                                     1.000e+00 0.000     0.000    
    PLOG/ 0.100     4.600e+44 -10.210   10.200   /
    PLOG/ 1.000     1.660e+47 -10.580   13.690   /
    PLOG/ 2.000     5.040e+47 -10.610   14.707   /
    PLOG/ 5.000     9.620e+47 -10.550   15.910   /
    PLOG/ 10.000    7.000e+47 -10.400   16.600   /
    PLOG/ 100.000   3.200e+44 -9.110    17.400   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (4.6e+44, 'cm^3/(mol*s)'),
            n = -10.21,
            Ea = (10200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.66e+47, 'cm^3/(mol*s)'),
            n = -10.58,
            Ea = (13690, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.04e+47, 'cm^3/(mol*s)'),
            n = -10.61,
            Ea = (14707, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (9.62e+47, 'cm^3/(mol*s)'),
            n = -10.55,
            Ea = (15910, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (7e+47, 'cm^3/(mol*s)'),
            n = -10.4,
            Ea = (16600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.2e+44, 'cm^3/(mol*s)'),
            n = -9.11,
            Ea = (17400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h5-s + h <=> c3h4-p + h2',
 "chemkinKinetics": """
c3h5-s+h=c3h4-p+h2                                  3.340e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-s + o <=> c2h4 + hco',
 "chemkinKinetics": """
c3h5-s+o=c2h4+hco                                   6.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-s + oh => c2h4 + hco + h',
 "chemkinKinetics": """
c3h5-s+oh=>c2h4+hco+h                               5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-s + ho2 => c2h4 + hco + oh',
 "chemkinKinetics": """
c3h5-s+ho2=>c2h4+hco+oh                             2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-s + hco <=> c3h6 + co',
 "chemkinKinetics": """
c3h5-s+hco=c3h6+co                                  9.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h5-s + ch3 <=> c3h4-p + ch4',
 "chemkinKinetics": """
c3h5-s+ch3=c3h4-p+ch4                               1.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-t <=> c3h5-s',
 "chemkinKinetics": """
c3h5-t=c3h5-s                                       1.000e+00 0.000     0.000    
    PLOG/ 0.100     1.600e+44 -12.160   52.200   /
    PLOG/ 1.000     1.500e+48 -12.710   53.900   /
    PLOG/ 10.000    5.100e+52 -13.370   57.200   /
    PLOG/ 100.000   5.800e+51 -12.430   59.200   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(1.6e+44, 's^-1'), n=-12.16, Ea=(52200, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.5e+48, 's^-1'), n=-12.71, Ea=(53900, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.1e+52, 's^-1'), n=-13.37, Ea=(57200, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.8e+51, 's^-1'), n=-12.43, Ea=(59200, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c3h4-a + h <=> c3h5-s',
 "chemkinKinetics": """
c3h4-a+h=c3h5-s                                     1.000e+00 0.000     0.000    
    PLOG/ 0.100     1.100e+30 -6.520    15.200   /
    PLOG/ 1.000     5.400e+29 -6.090    16.300   /
    PLOG/ 10.000    2.600e+31 -6.230    18.700   /
    PLOG/ 100.000   3.200e+31 -5.880    21.500   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (1.1e+30, 'cm^3/(mol*s)'),
            n = -6.52,
            Ea = (15200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.4e+29, 'cm^3/(mol*s)'),
            n = -6.09,
            Ea = (16300, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.6e+31, 'cm^3/(mol*s)'),
            n = -6.23,
            Ea = (18700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.2e+31, 'cm^3/(mol*s)'),
            n = -5.88,
            Ea = (21500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-a + c3h4-a <=> c3h5-a + c3h3',
 "chemkinKinetics": """
c3h4-a+c3h4-a=c3h5-a+c3h3                           5.000e+14 0.000     64.747   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+14, 'cm^3/(mol*s)'), n=0, Ea=(64746.7, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-t + o2 <=> c3h4-a + ho2',
 "chemkinKinetics": """
c3h5-t+o2=c3h4-a+ho2                                1.890e+30 -5.590    15.540   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.89e+30, 'cm^3/(mol*s)'),
    n = -5.59,
    Ea = (15540, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-t + o2 <=> ch3coch2 + o',
 "chemkinKinetics": """
c3h5-t+o2=ch3coch2+o                                3.810e+17 -1.360    5.580    
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.81e+17, 'cm^3/(mol*s)'),
    n = -1.36,
    Ea = (5580, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-t + o2 <=> ch3co + ch2o',
 "chemkinKinetics": """
c3h5-t+o2=ch3co+ch2o                                1.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-t + h <=> c3h4-p + h2',
 "chemkinKinetics": """
c3h5-t+h=c3h4-p+h2                                  3.340e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-t + ch3 <=> c3h4-p + ch4',
 "chemkinKinetics": """
c3h5-t+ch3=c3h4-p+ch4                               1.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c3h5-t + o <=> ch3 + ch2co',
 "chemkinKinetics": """
c3h5-t+o=ch3+ch2co                                  6.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-t + oh => ch3 + ch2co + h',
 "chemkinKinetics": """
c3h5-t+oh=>ch3+ch2co+h                              5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-t + ho2 => ch3 + ch2co + oh',
 "chemkinKinetics": """
c3h5-t+ho2=>ch3+ch2co+oh                            2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h5-t + hco <=> c3h6 + co',
 "chemkinKinetics": """
c3h5-t+hco=c3h6+co                                  9.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-p <=> c3h4-a',
 "chemkinKinetics": """
c3h4-p=c3h4-a                                       1.000e+00 0.000     0.000    
    PLOG/ 0.100     6.400e+61 -14.590   88.200   /
    PLOG/ 0.400     5.810e+62 -14.630   91.211   /
    PLOG/ 1.000     5.150e+60 -13.930   91.117   /
    PLOG/ 2.000     7.640e+59 -13.590   91.817   /
    PLOG/ 5.000     3.120e+58 -13.070   92.680   /
    PLOG/ 10.000    1.900e+57 -12.620   93.300   /
    PLOG/ 100.000   1.400e+52 -10.860   95.400   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 0.4, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(6.4e+61, 's^-1'), n=-14.59, Ea=(88200, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.81e+62, 's^-1'), n=-14.63, Ea=(91211, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.15e+60, 's^-1'), n=-13.93, Ea=(91117, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(7.64e+59, 's^-1'), n=-13.59, Ea=(91817, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(3.12e+58, 's^-1'), n=-13.07, Ea=(92680, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.9e+57, 's^-1'), n=-12.62, Ea=(93300, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.4e+52, 's^-1'), n=-10.86, Ea=(95400, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h3 + ho2 <=> c3h4-a + o2',
 "chemkinKinetics": """
c3h3+ho2=c3h4-a+o2                                  3.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-a + ho2 => ch2co + ch2 + oh',
 "chemkinKinetics": """
c3h4-a+ho2=>ch2co+ch2+oh                            4.000e+12 0.000     19.000   
""",
 "rmgPyKinetics": Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-a + oh <=> ch2co + ch3',
 "chemkinKinetics": """
c3h4-a+oh=ch2co+ch3                                 3.120e+12 0.000     -0.397   
""",
 "rmgPyKinetics": Arrhenius(A=(3.12e+12, 'cm^3/(mol*s)'), n=0, Ea=(-397, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-a + oh <=> c3h3 + h2o',
 "chemkinKinetics": """
c3h4-a+oh=c3h3+h2o                                  5.300e+06 2.000     2.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-a + o <=> c2h4 + co',
 "chemkinKinetics": """
c3h4-a+o=c2h4+co                                    2.000e+07 1.800     1.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-a + o <=> c2h2 + ch2o',
 "chemkinKinetics": """
c3h4-a+o=c2h2+ch2o                                  3.000e-03 4.610     -4.243   
""",
 "rmgPyKinetics": Arrhenius(A=(0.003, 'cm^3/(mol*s)'), n=4.61, Ea=(-4243, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-a + h <=> c3h3 + h2',
 "chemkinKinetics": """
c3h4-a+h=c3h3+h2                                    1.300e+06 2.000     5.500    
""",
 "rmgPyKinetics": Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(5500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-a + ch3 <=> c3h3 + ch4',
 "chemkinKinetics": """
c3h4-a+ch3=c3h3+ch4                                 1.300e+12 0.000     7.700    
""",
 "rmgPyKinetics": Arrhenius(A=(1.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-a + c3h5-a <=> c3h3 + c3h6',
 "chemkinKinetics": """
c3h4-a+c3h5-a=c3h3+c3h6                             2.000e+11 0.000     7.700    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-a + c2h <=> c2h2 + c3h3',
 "chemkinKinetics": """
c3h4-a+c2h=c2h2+c3h3                                1.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-p <=> cc3h4',
 "chemkinKinetics": """
c3h4-p=cc3h4                                        1.000e+00 0.000     0.000    
    PLOG/ 0.100     3.400e+46 -10.970   68.900   /
    PLOG/ 0.400     2.840e+45 -10.450   69.284   /
    PLOG/ 1.000     1.200e+44 -9.920    69.250   /
    PLOG/ 2.000     5.470e+42 -9.430    69.089   /
    PLOG/ 5.000     3.920e+40 -8.690    68.706   /
    PLOG/ 10.000    5.300e+38 -8.060    68.300   /
    PLOG/ 100.000   2.800e+31 -5.690    66.400   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 0.4, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(3.4e+46, 's^-1'), n=-10.97, Ea=(68900, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.84e+45, 's^-1'), n=-10.45, Ea=(69284, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.2e+44, 's^-1'), n=-9.92, Ea=(69250, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.47e+42, 's^-1'), n=-9.43, Ea=(69089, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(3.92e+40, 's^-1'), n=-8.69, Ea=(68706, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(5.3e+38, 's^-1'), n=-8.06, Ea=(68300, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2.8e+31, 's^-1'), n=-5.69, Ea=(66400, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-p + h <=> c3h4-a + h',
 "chemkinKinetics": """
c3h4-p+h=c3h4-a+h                                   1.000e+00 0.000     0.000    
    PLOG/ 0.100     2.300e+15 -0.260    7.600    /
    PLOG/ 1.000     6.270e+17 -0.910    10.079   /
    PLOG/ 2.000     1.500e+18 -1.000    10.756   /
    PLOG/ 5.000     1.930e+18 -1.010    11.523   /
    PLOG/ 10.000    3.100e+22 -2.180    14.800   /
    PLOG/ 100.000   6.400e+27 -3.580    21.200   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (2.3e+15, 'cm^3/(mol*s)'),
            n = -0.26,
            Ea = (7600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (6.27e+17, 'cm^3/(mol*s)'),
            n = -0.91,
            Ea = (10079, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(A=(1.5e+18, 'cm^3/(mol*s)'), n=-1, Ea=(10756, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(
            A = (1.93e+18, 'cm^3/(mol*s)'),
            n = -1.01,
            Ea = (11523, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.1e+22, 'cm^3/(mol*s)'),
            n = -2.18,
            Ea = (14800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (6.4e+27, 'cm^3/(mol*s)'),
            n = -3.58,
            Ea = (21200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-p + h <=> c3h5-s',
 "chemkinKinetics": """
c3h4-p+h=c3h5-s                                     1.000e+00 0.000     0.000    
    PLOG/ 0.100     1.000e+25 -5.000    1.800    /
    PLOG/ 1.000     5.500e+28 -5.740    4.300    /
    PLOG/ 10.000    1.000e+34 -6.880    8.900    /
    PLOG/ 100.000   9.700e+37 -7.630    13.800   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(1e+25, 'cm^3/(mol*s)'), n=-5, Ea=(1800, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(
            A = (5.5e+28, 'cm^3/(mol*s)'),
            n = -5.74,
            Ea = (4300, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(A=(1e+34, 'cm^3/(mol*s)'), n=-6.88, Ea=(8900, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(
            A = (9.7e+37, 'cm^3/(mol*s)'),
            n = -7.63,
            Ea = (13800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h4-p + h <=> c3h5-a',
 "chemkinKinetics": """
c3h4-p+h=c3h5-a                                     1.000e+00 0.000     0.000    
    PLOG/ 0.100     1.100e+60 -14.560   28.100   /
    PLOG/ 1.000     4.910e+60 -14.370   31.644   /
    PLOG/ 2.000     3.040e+60 -14.190   32.642   /
    PLOG/ 5.000     9.020e+59 -13.890   33.953   /
    PLOG/ 10.000    2.200e+59 -13.610   34.900   /
    PLOG/ 100.000   1.600e+55 -12.070   37.500   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (1.1e+60, 'cm^3/(mol*s)'),
            n = -14.56,
            Ea = (28100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.91e+60, 'cm^3/(mol*s)'),
            n = -14.37,
            Ea = (31644, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.04e+60, 'cm^3/(mol*s)'),
            n = -14.19,
            Ea = (32642, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (9.02e+59, 'cm^3/(mol*s)'),
            n = -13.89,
            Ea = (33953, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.2e+59, 'cm^3/(mol*s)'),
            n = -13.61,
            Ea = (34900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.6e+55, 'cm^3/(mol*s)'),
            n = -12.07,
            Ea = (37500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-p + h <=> c3h3 + h2',
 "chemkinKinetics": """
c3h4-p+h=c3h3+h2                                    1.300e+06 2.000     5.500    
""",
 "rmgPyKinetics": Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(5500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-p + c3h3 <=> c3h4-a + c3h3',
 "chemkinKinetics": """
c3h4-p+c3h3=c3h4-a+c3h3                             6.140e+06 1.740     10.450   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.14e+06, 'cm^3/(mol*s)'),
    n = 1.74,
    Ea = (10450, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-p + o <=> hcco + ch3',
 "chemkinKinetics": """
c3h4-p+o=hcco+ch3                                   7.300e+12 0.000     2.250    
""",
 "rmgPyKinetics": Arrhenius(A=(7.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-p + o <=> c2h4 + co',
 "chemkinKinetics": """
c3h4-p+o=c2h4+co                                    1.000e+13 0.000     2.250    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-p + oh <=> c3h3 + h2o',
 "chemkinKinetics": """
c3h4-p+oh=c3h3+h2o                                  1.000e+06 2.000     0.100    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+06, 'cm^3/(mol*s)'), n=2, Ea=(100, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-p + c2h <=> c2h2 + c3h3',
 "chemkinKinetics": """
c3h4-p+c2h=c2h2+c3h3                                1.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-p + ch3 <=> c3h3 + ch4',
 "chemkinKinetics": """
c3h4-p+ch3=c3h3+ch4                                 1.800e+12 0.000     7.700    
""",
 "rmgPyKinetics": Arrhenius(A=(1.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h2 + ch3 <=> c3h4-p + h',
 "chemkinKinetics": """
c2h2+ch3=c3h4-p+h                                   1.000e+00 0.000     0.000    
    PLOG/ 0.100     4.500e+06 1.860     11.600   /
    PLOG/ 1.000     2.560e+09 1.100     13.644   /
    PLOG/ 2.000     2.070e+10 0.850     14.415   /
    PLOG/ 5.000     2.510e+11 0.560     15.453   /
    PLOG/ 10.000    1.100e+12 0.390     16.200   /
    PLOG/ 100.000   2.100e+12 0.370     18.100   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (4.5e+06, 'cm^3/(mol*s)'),
            n = 1.86,
            Ea = (11600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.56e+09, 'cm^3/(mol*s)'),
            n = 1.1,
            Ea = (13644, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.07e+10, 'cm^3/(mol*s)'),
            n = 0.85,
            Ea = (14415, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.51e+11, 'cm^3/(mol*s)'),
            n = 0.56,
            Ea = (15453, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.1e+12, 'cm^3/(mol*s)'),
            n = 0.39,
            Ea = (16200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.1e+12, 'cm^3/(mol*s)'),
            n = 0.37,
            Ea = (18100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'cc3h4 <=> c3h4-a',
 "chemkinKinetics": """
cc3h4=c3h4-a                                        1.000e+00 0.000     0.000    
    PLOG/ 0.100     2.300e+39 -8.810    47.800   /
    PLOG/ 0.400     7.590e+40 -9.070    48.831   /
    PLOG/ 1.000     4.890e+41 -9.170    49.594   /
    PLOG/ 2.000     8.810e+41 -9.150    50.073   /
    PLOG/ 5.000     4.330e+41 -8.930    50.475   /
    PLOG/ 10.000    7.200e+40 -8.600    50.600   /
    PLOG/ 100.000   1.600e+35 -6.640    49.500   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 0.4, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(A=(2.3e+39, 's^-1'), n=-8.81, Ea=(47800, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(7.59e+40, 's^-1'), n=-9.07, Ea=(48831, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.89e+41, 's^-1'), n=-9.17, Ea=(49594, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(8.81e+41, 's^-1'), n=-9.15, Ea=(50073, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.33e+41, 's^-1'), n=-8.93, Ea=(50475, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(7.2e+40, 's^-1'), n=-8.6, Ea=(50600, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.6e+35, 's^-1'), n=-6.64, Ea=(49500, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h3 + h <=> c3h4-p',
 "chemkinKinetics": """
c3h3+h=c3h4-p                                       1.500e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h3 + h <=> c3h4-a',
 "chemkinKinetics": """
c3h3+h=c3h4-a                                       2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h + ch3 <=> c3h4-p',
 "chemkinKinetics": """
c2h+ch3=c3h4-p                                      8.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h3 + ho2 <=> c3h4-p + o2',
 "chemkinKinetics": """
c3h3+ho2=c3h4-p+o2                                  2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-p + ho2 => c2h4 + co + oh',
 "chemkinKinetics": """
c3h4-p+ho2=>c2h4+co+oh                              3.000e+12 0.000     19.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-p + oh <=> ch2co + ch3',
 "chemkinKinetics": """
c3h4-p+oh=ch2co+ch3                                 5.000e-04 4.500     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(0.0005, 'cm^3/(mol*s)'), n=4.5, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-p + o <=> c2h3 + hco',
 "chemkinKinetics": """
c3h4-p+o=c2h3+hco                                   3.200e+12 0.000     2.010    
""",
 "rmgPyKinetics": Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(2010, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-p + o <=> c3h3 + oh',
 "chemkinKinetics": """
c3h4-p+o=c3h3+oh                                    7.650e+08 1.500     8.600    
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.65e+08, 'cm^3/(mol*s)'),
    n = 1.5,
    Ea = (8600, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-p + c2h3 <=> c3h3 + c2h4',
 "chemkinKinetics": """
c3h4-p+c2h3=c3h3+c2h4                               1.000e+12 0.000     7.700    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-p + c3h5-a <=> c3h3 + c3h6',
 "chemkinKinetics": """
c3h4-p+c3h5-a=c3h3+c3h6                             1.000e+12 0.000     7.700    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h3 + o <=> ch2o + c2h',
 "chemkinKinetics": """
c3h3+o=ch2o+c2h                                     2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h3 + o2 <=> ch2co + hco',
 "chemkinKinetics": """
c3h3+o2=ch2co+hco                                   3.000e+10 0.000     2.868    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2868, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h3 + ho2 => oh + co + c2h3',
 "chemkinKinetics": """
c3h3+ho2=>oh+co+c2h3                                8.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h3 + hco <=> c3h4-a + co',
 "chemkinKinetics": """
c3h3+hco=c3h4-a+co                                  2.500e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h3 + hco <=> c3h4-p + co',
 "chemkinKinetics": """
c3h3+hco=c3h4-p+co                                  2.500e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5 + c2h <=> c3h3 + ch3',
 "chemkinKinetics": """
c2h5+c2h=c3h3+ch3                                   1.810e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-a + ho2 => c2h4 + co + oh',
 "chemkinKinetics": """
c3h4-a+ho2=>c2h4+co+oh                              1.000e+12 0.000     14.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-a + ho2 <=> c3h3 + h2o2',
 "chemkinKinetics": """
c3h4-a+ho2=c3h3+h2o2                                3.000e+13 0.000     14.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h2 + ch3 <=> c3h4-a + h',
 "chemkinKinetics": """
c2h2+ch3=c3h4-a+h                                   1.000e+00 0.000     0.000    
    PLOG/ 0.100     2.400e+09 0.910     20.700   /
    PLOG/ 1.000     5.140e+09 0.860     22.153   /
    PLOG/ 2.000     1.330e+10 0.750     22.811   /
    PLOG/ 5.000     9.200e+10 0.540     23.950   /
    PLOG/ 10.000    5.100e+11 0.350     25.000   /
    PLOG/ 100.000   7.300e+12 0.110     28.500   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (2.4e+09, 'cm^3/(mol*s)'),
            n = 0.91,
            Ea = (20700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.14e+09, 'cm^3/(mol*s)'),
            n = 0.86,
            Ea = (22153, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.33e+10, 'cm^3/(mol*s)'),
            n = 0.75,
            Ea = (22811, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (9.2e+10, 'cm^3/(mol*s)'),
            n = 0.54,
            Ea = (23950, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.1e+11, 'cm^3/(mol*s)'),
            n = 0.35,
            Ea = (25000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (7.3e+12, 'cm^3/(mol*s)'),
            n = 0.11,
            Ea = (28500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chco + oh <=> c2h5 + co2',
 "chemkinKinetics": """
ch3chco+oh=c2h5+co2                                 1.730e+12 0.000     -1.010   
""",
 "rmgPyKinetics": Arrhenius(A=(1.73e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chco + oh <=> sc2h4oh + co',
 "chemkinKinetics": """
ch3chco+oh=sc2h4oh+co                               2.000e+12 0.000     -1.010   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chco + h <=> c2h5 + co',
 "chemkinKinetics": """
ch3chco+h=c2h5+co                                   4.400e+12 0.000     1.459    
""",
 "rmgPyKinetics": Arrhenius(A=(4.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(1459, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chco + o <=> ch3cho + co',
 "chemkinKinetics": """
ch3chco+o=ch3cho+co                                 3.200e+12 0.000     -0.437   
""",
 "rmgPyKinetics": Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'nc3h7 + ho2 <=> nc3h7o + oh',
 "chemkinKinetics": """
nc3h7+ho2=nc3h7o+oh                                 7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic3h7 + ho2 <=> ic3h7o + oh',
 "chemkinKinetics": """
ic3h7+ho2=ic3h7o+oh                                 7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + nc3h7 <=> ch3o + nc3h7o',
 "chemkinKinetics": """
ch3o2+nc3h7=ch3o+nc3h7o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + ic3h7 <=> ch3o + ic3h7o',
 "chemkinKinetics": """
ch3o2+ic3h7=ch3o+ic3h7o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'nc3h7 + o2 <=> nc3h7o2',
 "chemkinKinetics": """
nc3h7+o2=nc3h7o2                                    4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic3h7 + o2 <=> ic3h7o2',
 "chemkinKinetics": """
ic3h7+o2=ic3h7o2                                    7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'nc3h7o2 + ch2o <=> nc3h7o2h + hco',
 "chemkinKinetics": """
nc3h7o2+ch2o=nc3h7o2h+hco                           5.600e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + ch3cho <=> nc3h7o2h + ch3co',
 "chemkinKinetics": """
nc3h7o2+ch3cho=nc3h7o2h+ch3co                       2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + ch2o <=> ic3h7o2h + hco',
 "chemkinKinetics": """
ic3h7o2+ch2o=ic3h7o2h+hco                           5.600e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + ch3cho <=> ic3h7o2h + ch3co',
 "chemkinKinetics": """
ic3h7o2+ch3cho=ic3h7o2h+ch3co                       2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + ho2 <=> nc3h7o2h + o2',
 "chemkinKinetics": """
nc3h7o2+ho2=nc3h7o2h+o2                             1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + ho2 <=> ic3h7o2h + o2',
 "chemkinKinetics": """
ic3h7o2+ho2=ic3h7o2h+o2                             1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + nc3h7o2 <=> c2h3 + nc3h7o2h',
 "chemkinKinetics": """
c2h4+nc3h7o2=c2h3+nc3h7o2h                          1.130e+13 0.000     30.430   
""",
 "rmgPyKinetics": Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + ic3h7o2 <=> c2h3 + ic3h7o2h',
 "chemkinKinetics": """
c2h4+ic3h7o2=c2h3+ic3h7o2h                          1.130e+13 0.000     30.430   
""",
 "rmgPyKinetics": Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + nc3h7o2 <=> ch2oh + nc3h7o2h',
 "chemkinKinetics": """
ch3oh+nc3h7o2=ch2oh+nc3h7o2h                        6.300e+12 0.000     19.360   
""",
 "rmgPyKinetics": Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + ic3h7o2 <=> ch2oh + ic3h7o2h',
 "chemkinKinetics": """
ch3oh+ic3h7o2=ch2oh+ic3h7o2h                        6.300e+12 0.000     19.360   
""",
 "rmgPyKinetics": Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3cho + nc3h7o2 <=> c2h3co + nc3h7o2h',
 "chemkinKinetics": """
c2h3cho+nc3h7o2=c2h3co+nc3h7o2h                     2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3cho + ic3h7o2 <=> c2h3co + ic3h7o2h',
 "chemkinKinetics": """
c2h3cho+ic3h7o2=c2h3co+ic3h7o2h                     2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch4 + nc3h7o2 <=> ch3 + nc3h7o2h',
 "chemkinKinetics": """
ch4+nc3h7o2=ch3+nc3h7o2h                            1.120e+13 0.000     24.640   
""",
 "rmgPyKinetics": Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch4 + ic3h7o2 <=> ch3 + ic3h7o2h',
 "chemkinKinetics": """
ch4+ic3h7o2=ch3+ic3h7o2h                            1.120e+13 0.000     24.640   
""",
 "rmgPyKinetics": Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + ch3o2 => nc3h7o + ch3o + o2',
 "chemkinKinetics": """
nc3h7o2+ch3o2=>nc3h7o+ch3o+o2                       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic3h7o2 + ch3o2 => ic3h7o + ch3o + o2',
 "chemkinKinetics": """
ic3h7o2+ch3o2=>ic3h7o+ch3o+o2                       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'h2 + nc3h7o2 <=> h + nc3h7o2h',
 "chemkinKinetics": """
h2+nc3h7o2=h+nc3h7o2h                               3.010e+13 0.000     26.030   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h2 + ic3h7o2 <=> h + ic3h7o2h',
 "chemkinKinetics": """
h2+ic3h7o2=h+ic3h7o2h                               3.010e+13 0.000     26.030   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + c2h6 <=> ic3h7o2h + c2h5',
 "chemkinKinetics": """
ic3h7o2+c2h6=ic3h7o2h+c2h5                          1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + c2h6 <=> nc3h7o2h + c2h5',
 "chemkinKinetics": """
nc3h7o2+c2h6=nc3h7o2h+c2h5                          1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + c2h5cho <=> ic3h7o2h + c2h5co',
 "chemkinKinetics": """
ic3h7o2+c2h5cho=ic3h7o2h+c2h5co                     2.000e+11 0.000     9.500    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + c2h5cho <=> nc3h7o2h + c2h5co',
 "chemkinKinetics": """
nc3h7o2+c2h5cho=nc3h7o2h+c2h5co                     2.000e+11 0.000     9.500    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + ch3co3 => ic3h7o + ch3co2 + o2',
 "chemkinKinetics": """
ic3h7o2+ch3co3=>ic3h7o+ch3co2+o2                    1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'nc3h7o2 + ch3co3 => nc3h7o + ch3co2 + o2',
 "chemkinKinetics": """
nc3h7o2+ch3co3=>nc3h7o+ch3co2+o2                    1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic3h7o2 + c2h5o2 => ic3h7o + c2h5o + o2',
 "chemkinKinetics": """
ic3h7o2+c2h5o2=>ic3h7o+c2h5o+o2                     1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'nc3h7o2 + c2h5o2 => nc3h7o + c2h5o + o2',
 "chemkinKinetics": """
nc3h7o2+c2h5o2=>nc3h7o+c2h5o+o2                     1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic3h7o2 + ic3h7o2 => o2 + ic3h7o + ic3h7o',
 "chemkinKinetics": """
ic3h7o2+ic3h7o2=>o2+ic3h7o+ic3h7o                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'nc3h7o2 + nc3h7o2 => o2 + nc3h7o + nc3h7o',
 "chemkinKinetics": """
nc3h7o2+nc3h7o2=>o2+nc3h7o+nc3h7o                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic3h7o2 + nc3h7o2 => ic3h7o + nc3h7o + o2',
 "chemkinKinetics": """
ic3h7o2+nc3h7o2=>ic3h7o+nc3h7o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic3h7o2 + ch3 <=> ic3h7o + ch3o',
 "chemkinKinetics": """
ic3h7o2+ch3=ic3h7o+ch3o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + c2h5 <=> ic3h7o + c2h5o',
 "chemkinKinetics": """
ic3h7o2+c2h5=ic3h7o+c2h5o                           7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + ic3h7 <=> ic3h7o + ic3h7o',
 "chemkinKinetics": """
ic3h7o2+ic3h7=ic3h7o+ic3h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + nc3h7 <=> ic3h7o + nc3h7o',
 "chemkinKinetics": """
ic3h7o2+nc3h7=ic3h7o+nc3h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + c3h5-a <=> ic3h7o + c3h5o',
 "chemkinKinetics": """
ic3h7o2+c3h5-a=ic3h7o+c3h5o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + ch3 <=> nc3h7o + ch3o',
 "chemkinKinetics": """
nc3h7o2+ch3=nc3h7o+ch3o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + c2h5 <=> nc3h7o + c2h5o',
 "chemkinKinetics": """
nc3h7o2+c2h5=nc3h7o+c2h5o                           7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + ic3h7 <=> nc3h7o + ic3h7o',
 "chemkinKinetics": """
nc3h7o2+ic3h7=nc3h7o+ic3h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + nc3h7 <=> nc3h7o + nc3h7o',
 "chemkinKinetics": """
nc3h7o2+nc3h7=nc3h7o+nc3h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + c3h5-a <=> nc3h7o + c3h5o',
 "chemkinKinetics": """
nc3h7o2+c3h5-a=nc3h7o+c3h5o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2h <=> nc3h7o + oh',
 "chemkinKinetics": """
nc3h7o2h=nc3h7o+oh                                  1.500e+16 0.000     42.500   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic3h7o + oh <=> ic3h7o2h',
 "chemkinKinetics": """
ic3h7o+oh=ic3h7o2h                                  1.000e+15 -0.800    0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+15, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h5 + ch2o <=> nc3h7o',
 "chemkinKinetics": """
c2h5+ch2o=nc3h7o                                    1.000e+11 0.000     3.496    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(3496, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h5cho + h <=> nc3h7o',
 "chemkinKinetics": """
c2h5cho+h=nc3h7o                                    4.000e+12 0.000     6.260    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(6260, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3 + ch3cho <=> ic3h7o',
 "chemkinKinetics": """
ch3+ch3cho=ic3h7o                                   1.000e+11 0.000     9.256    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9256, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3coch3 + h <=> ic3h7o',
 "chemkinKinetics": """
ch3coch3+h=ic3h7o                                   2.000e+12 0.000     7.270    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(7270, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h7o + o2 <=> ch3coch3 + ho2',
 "chemkinKinetics": """
ic3h7o+o2=ch3coch3+ho2                              9.090e+09 0.000     0.390    
""",
 "rmgPyKinetics": Arrhenius(A=(9.09e+09, 'cm^3/(mol*s)'), n=0, Ea=(390, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'nc3h7o2 <=> c3h6ooh1-2',
 "chemkinKinetics": """
nc3h7o2=c3h6ooh1-2                                  6.000e+11 0.000     26.850   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(26850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'nc3h7o2 <=> c3h6ooh1-3',
 "chemkinKinetics": """
nc3h7o2=c3h6ooh1-3                                  1.125e+11 0.000     24.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1.125e+11, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic3h7o2 <=> c3h6ooh2-1',
 "chemkinKinetics": """
ic3h7o2=c3h6ooh2-1                                  1.800e+12 0.000     29.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1.8e+12, 's^-1'), n=0, Ea=(29400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic3h7o2 <=> c3h6ooh2-2',
 "chemkinKinetics": """
ic3h7o2=c3h6ooh2-2                                  1.230e+35 -6.960    48.880   
""",
 "rmgPyKinetics": Arrhenius(A=(1.23e+35, 's^-1'), n=-6.96, Ea=(48880, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c3h6ooh1-2 <=> c3h6o1-2 + oh',
 "chemkinKinetics": """
c3h6ooh1-2=c3h6o1-2+oh                              6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c3h6ooh1-3 <=> c3h6o1-3 + oh',
 "chemkinKinetics": """
c3h6ooh1-3=c3h6o1-3+oh                              7.500e+10 0.000     15.250   
""",
 "rmgPyKinetics": Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c3h6ooh2-1 <=> c3h6o1-2 + oh',
 "chemkinKinetics": """
c3h6ooh2-1=c3h6o1-2+oh                              6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c3h6 + ho2 <=> c3h6ooh1-2',
 "chemkinKinetics": """
c3h6+ho2=c3h6ooh1-2                                 1.000e+11 0.000     11.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h6 + ho2 <=> c3h6ooh2-1',
 "chemkinKinetics": """
c3h6+ho2=c3h6ooh2-1                                 1.000e+11 0.000     11.750   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11750, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h6ooh1-3 => oh + ch2o + c2h4',
 "chemkinKinetics": """
c3h6ooh1-3=>oh+ch2o+c2h4                            3.035e+15 -0.790    27.400   
""",
 "rmgPyKinetics": Arrhenius(A=(3.035e+15, 's^-1'), n=-0.79, Ea=(27400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'c3h6ooh2-1 <=> c2h3ooh + ch3',
 "chemkinKinetics": """
c3h6ooh2-1=c2h3ooh+ch3                              6.540e+27 -5.140    38.320   
""",
 "rmgPyKinetics": Arrhenius(A=(6.54e+27, 's^-1'), n=-5.14, Ea=(38320, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h6ooh1-2 => c2h4 + ch2o + oh',
 "chemkinKinetics": """
c3h6ooh1-2=>c2h4+ch2o+oh                            1.310e+33 -7.010    48.120   
""",
 "rmgPyKinetics": Arrhenius(A=(1.31e+33, 's^-1'), n=-7.01, Ea=(48120, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6ooh2-2 <=> ch3coch3 + oh',
 "chemkinKinetics": """
c3h6ooh2-2=ch3coch3+oh                              9.000e+14 0.000     1.500    
""",
 "rmgPyKinetics": Arrhenius(A=(9e+14, 's^-1'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h6ooh1-2 + o2 <=> c3h6ooh1-2o2',
 "chemkinKinetics": """
c3h6ooh1-2+o2=c3h6ooh1-2o2                          5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h6ooh1-3 + o2 <=> c3h6ooh1-3o2',
 "chemkinKinetics": """
c3h6ooh1-3+o2=c3h6ooh1-3o2                          4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h6ooh2-1 + o2 <=> c3h6ooh2-1o2',
 "chemkinKinetics": """
c3h6ooh2-1+o2=c3h6ooh2-1o2                          4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h6ooh1-2o2 <=> c3ket12 + oh',
 "chemkinKinetics": """
c3h6ooh1-2o2=c3ket12+oh                             6.000e+11 0.000     26.400   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(26400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c3h6ooh1-3o2 <=> c3ket13 + oh',
 "chemkinKinetics": """
c3h6ooh1-3o2=c3ket13+oh                             7.500e+10 0.000     21.400   
""",
 "rmgPyKinetics": Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(21400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c3h6ooh2-1o2 <=> c3ket21 + oh',
 "chemkinKinetics": """
c3h6ooh2-1o2=c3ket21+oh                             3.000e+11 0.000     23.850   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(23850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c3h6ooh2-1o2 <=> c3h51-2,3ooh',
 "chemkinKinetics": """
c3h6ooh2-1o2=c3h51-2,3ooh                           1.125e+11 0.000     24.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1.125e+11, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c3h6ooh1-2o2 <=> c3h51-2,3ooh',
 "chemkinKinetics": """
c3h6ooh1-2o2=c3h51-2,3ooh                           9.000e+11 0.000     29.400   
""",
 "rmgPyKinetics": Arrhenius(A=(9e+11, 's^-1'), n=0, Ea=(29400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c3h51-2,3ooh <=> ac3h5ooh + ho2',
 "chemkinKinetics": """
c3h51-2,3ooh=ac3h5ooh+ho2                           2.560e+13 -0.490    17.770   
""",
 "rmgPyKinetics": Arrhenius(A=(2.56e+13, 's^-1'), n=-0.49, Ea=(17770, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h6ooh1-3o2 <=> c3h52-1,3ooh',
 "chemkinKinetics": """
c3h6ooh1-3o2=c3h52-1,3ooh                           6.000e+11 0.000     26.850   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(26850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c3h52-1,3ooh <=> ac3h5ooh + ho2',
 "chemkinKinetics": """
c3h52-1,3ooh=ac3h5ooh+ho2                           1.150e+14 -0.630    17.250   
""",
 "rmgPyKinetics": Arrhenius(A=(1.15e+14, 's^-1'), n=-0.63, Ea=(17250, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3ket12 => ch3cho + hco + oh',
 "chemkinKinetics": """
c3ket12=>ch3cho+hco+oh                              9.450e+15 0.000     43.000   
""",
 "rmgPyKinetics": Arrhenius(A=(9.45e+15, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products1',  ],
},

{
 "reaction": 'c3ket13 => ch2o + ch2cho + oh',
 "chemkinKinetics": """
c3ket13=>ch2o+ch2cho+oh                             1.000e+16 0.000     43.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products1', 'Fake_3products1', 'Fake_3products1',  ],
},

{
 "reaction": 'c3ket21 => ch2o + ch3co + oh',
 "chemkinKinetics": """
c3ket21=>ch2o+ch3co+oh                              1.000e+16 0.000     43.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products1',  ],
},

{
 "reaction": 'c3h5o + oh <=> ac3h5ooh',
 "chemkinKinetics": """
c3h5o+oh=ac3h5ooh                                   2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h5o <=> c2h3cho + h',
 "chemkinKinetics": """
c3h5o=c2h3cho+h                                     1.000e+14 0.000     29.100   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(29100, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h3 + ch2o <=> c3h5o',
 "chemkinKinetics": """
c2h3+ch2o=c3h5o                                     1.500e+11 0.000     10.600   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(10600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h5o + o2 <=> c2h3cho + ho2',
 "chemkinKinetics": """
c3h5o+o2=c2h3cho+ho2                                1.000e+12 0.000     6.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h3ooh <=> ch2cho + oh',
 "chemkinKinetics": """
c2h3ooh=ch2cho+oh                                   8.400e+14 0.000     43.000   
""",
 "rmgPyKinetics": Arrhenius(A=(8.4e+14, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h6o1-2 <=> c2h4 + ch2o',
 "chemkinKinetics": """
c3h6o1-2=c2h4+ch2o                                  6.000e+14 0.000     60.000   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+14, 's^-1'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6o1-2 + oh => ch2o + c2h3 + h2o',
 "chemkinKinetics": """
c3h6o1-2+oh=>ch2o+c2h3+h2o                          5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6o1-2 + h => ch2o + c2h3 + h2',
 "chemkinKinetics": """
c3h6o1-2+h=>ch2o+c2h3+h2                            2.630e+07 2.000     5.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.63e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6o1-2 + o => ch2o + c2h3 + oh',
 "chemkinKinetics": """
c3h6o1-2+o=>ch2o+c2h3+oh                            8.430e+13 0.000     5.200    
""",
 "rmgPyKinetics": Arrhenius(A=(8.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6o1-2 + ho2 => ch2o + c2h3 + h2o2',
 "chemkinKinetics": """
c3h6o1-2+ho2=>ch2o+c2h3+h2o2                        1.000e+13 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6o1-2 + ch3o2 => ch2o + c2h3 + ch3o2h',
 "chemkinKinetics": """
c3h6o1-2+ch3o2=>ch2o+c2h3+ch3o2h                    1.000e+13 0.000     19.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6o1-2 + ch3 => ch2o + c2h3 + ch4',
 "chemkinKinetics": """
c3h6o1-2+ch3=>ch2o+c2h3+ch4                         2.000e+11 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6o1-3 <=> c2h4 + ch2o',
 "chemkinKinetics": """
c3h6o1-3=c2h4+ch2o                                  6.000e+14 0.000     60.000   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+14, 's^-1'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['2+2_cycloaddition_Cd',  ],
},

{
 "reaction": 'c3h6o1-3 + oh => ch2o + c2h3 + h2o',
 "chemkinKinetics": """
c3h6o1-3+oh=>ch2o+c2h3+h2o                          5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6o1-3 + o => ch2o + c2h3 + oh',
 "chemkinKinetics": """
c3h6o1-3+o=>ch2o+c2h3+oh                            8.430e+13 0.000     5.200    
""",
 "rmgPyKinetics": Arrhenius(A=(8.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6o1-3 + h => ch2o + c2h3 + h2',
 "chemkinKinetics": """
c3h6o1-3+h=>ch2o+c2h3+h2                            2.630e+07 2.000     5.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.63e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6o1-3 + ch3o2 => ch2o + c2h3 + ch3o2h',
 "chemkinKinetics": """
c3h6o1-3+ch3o2=>ch2o+c2h3+ch3o2h                    1.000e+13 0.000     19.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6o1-3 + ho2 => ch2o + c2h3 + h2o2',
 "chemkinKinetics": """
c3h6o1-3+ho2=>ch2o+c2h3+h2o2                        1.000e+13 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6o1-3 + ch3 => ch2o + c2h3 + ch4',
 "chemkinKinetics": """
c3h6o1-3+ch3=>ch2o+c2h3+ch4                         2.000e+11 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic3h7o2 <=> c3h6 + ho2',
 "chemkinKinetics": """
ic3h7o2=c3h6+ho2                                    1.196e+43 -9.430    41.530   
""",
 "rmgPyKinetics": Arrhenius(A=(1.196e+43, 's^-1'), n=-9.43, Ea=(41530, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'nc3h7o2 <=> c3h6 + ho2',
 "chemkinKinetics": """
nc3h7o2=c3h6+ho2                                    4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'c4h10 <=> c2h5 + c2h5',
 "chemkinKinetics": """
c4h10(+M)=c2h5+c2h5(+M)                             1.355e+37 -6.036    92.929   

    LOW/ 4.720e+18 0.000     49.578   /
    TROE/ 7.998e-02 1e-20     3.24e+04  4.86e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.3554e+37, 's^-1'), n=-6.036, Ea=(92929, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(A=(4.72e+18, 'cm^3/(mol*s)'), n=0, Ea=(49578, 'cal/mol'), T0=(1, 'K')),
    alpha = 0.079982,
    T3 = (1e-20, 'K'),
    T1 = (32428, 'K'),
    T2 = (4858.2, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h10 <=> nc3h7 + ch3',
 "chemkinKinetics": """
c4h10(+M)=nc3h7+ch3(+M)                             6.600e+52 -10.626   100.330  

    LOW/ 5.340e+17 0.000     42.959   /
    TROE/ 9.502e-02 1e-20     5.35e+03  4.33e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (6.5998e+52, 's^-1'),
        n = -10.626,
        Ea = (100330, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(A=(5.34e+17, 'cm^3/(mol*s)'), n=0, Ea=(42959, 'cal/mol'), T0=(1, 'K')),
    alpha = 0.095015,
    T3 = (1e-20, 'K'),
    T1 = (5347.6, 'K'),
    T2 = (4325.6, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'pc4h9 + h <=> c4h10',
 "chemkinKinetics": """
pc4h9+h=c4h10                                       3.610e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.61e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9 + h <=> c4h10',
 "chemkinKinetics": """
sc4h9+h=c4h10                                       3.610e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.61e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h10 + o2 <=> pc4h9 + ho2',
 "chemkinKinetics": """
c4h10+o2=pc4h9+ho2                                  6.000e+13 0.000     52.340   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + o2 <=> sc4h9 + ho2',
 "chemkinKinetics": """
c4h10+o2=sc4h9+ho2                                  4.000e+13 0.000     49.800   
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + c3h5-a <=> pc4h9 + c3h6',
 "chemkinKinetics": """
c4h10+c3h5-a=pc4h9+c3h6                             7.940e+11 0.000     20.500   
""",
 "rmgPyKinetics": Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + c3h5-a <=> sc4h9 + c3h6',
 "chemkinKinetics": """
c4h10+c3h5-a=sc4h9+c3h6                             3.160e+11 0.000     16.400   
""",
 "rmgPyKinetics": Arrhenius(A=(3.16e+11, 'cm^3/(mol*s)'), n=0, Ea=(16400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + c2h5 <=> pc4h9 + c2h6',
 "chemkinKinetics": """
c4h10+c2h5=pc4h9+c2h6                               1.580e+11 0.000     12.300   
""",
 "rmgPyKinetics": Arrhenius(A=(1.58e+11, 'cm^3/(mol*s)'), n=0, Ea=(12300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + c2h5 <=> sc4h9 + c2h6',
 "chemkinKinetics": """
c4h10+c2h5=sc4h9+c2h6                               1.000e+11 0.000     10.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + c2h3 <=> pc4h9 + c2h4',
 "chemkinKinetics": """
c4h10+c2h3=pc4h9+c2h4                               1.000e+12 0.000     18.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + c2h3 <=> sc4h9 + c2h4',
 "chemkinKinetics": """
c4h10+c2h3=sc4h9+c2h4                               8.000e+11 0.000     16.800   
""",
 "rmgPyKinetics": Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(16800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + ch3 <=> pc4h9 + ch4',
 "chemkinKinetics": """
c4h10+ch3=pc4h9+ch4                                 9.040e-01 3.650     7.154    
""",
 "rmgPyKinetics": Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + ch3 <=> sc4h9 + ch4',
 "chemkinKinetics": """
c4h10+ch3=sc4h9+ch4                                 3.020e+00 3.460     5.481    
""",
 "rmgPyKinetics": Arrhenius(A=(3.02, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + h <=> pc4h9 + h2',
 "chemkinKinetics": """
c4h10+h=pc4h9+h2                                    3.490e+05 2.690     6.450    
""",
 "rmgPyKinetics": Arrhenius(A=(349000, 'cm^3/(mol*s)'), n=2.69, Ea=(6450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + h <=> sc4h9 + h2',
 "chemkinKinetics": """
c4h10+h=sc4h9+h2                                    2.600e+06 2.400     4.471    
""",
 "rmgPyKinetics": Arrhenius(A=(2.6e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + oh <=> pc4h9 + h2o',
 "chemkinKinetics": """
c4h10+oh=pc4h9+h2o                                  1.054e+10 0.970     1.586    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.054e+10, 'cm^3/(mol*s)'),
    n = 0.97,
    Ea = (1586, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + oh <=> sc4h9 + h2o',
 "chemkinKinetics": """
c4h10+oh=sc4h9+h2o                                  9.340e+07 1.610     -0.035   
""",
 "rmgPyKinetics": Arrhenius(
    A = (9.34e+07, 'cm^3/(mol*s)'),
    n = 1.61,
    Ea = (-35, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + o <=> pc4h9 + oh',
 "chemkinKinetics": """
c4h10+o=pc4h9+oh                                    1.130e+14 0.000     7.850    
""",
 "rmgPyKinetics": Arrhenius(A=(1.13e+14, 'cm^3/(mol*s)'), n=0, Ea=(7850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + o <=> sc4h9 + oh',
 "chemkinKinetics": """
c4h10+o=sc4h9+oh                                    5.620e+13 0.000     5.200    
""",
 "rmgPyKinetics": Arrhenius(A=(5.62e+13, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + ho2 <=> pc4h9 + h2o2',
 "chemkinKinetics": """
c4h10+ho2=pc4h9+h2o2                                4.080e+01 3.590     17.160   
""",
 "rmgPyKinetics": Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + ho2 <=> sc4h9 + h2o2',
 "chemkinKinetics": """
c4h10+ho2=sc4h9+h2o2                                1.264e+02 3.370     13.720   
""",
 "rmgPyKinetics": Arrhenius(A=(126.4, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + ch3o <=> pc4h9 + ch3oh',
 "chemkinKinetics": """
c4h10+ch3o=pc4h9+ch3oh                              3.000e+11 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + ch3o <=> sc4h9 + ch3oh',
 "chemkinKinetics": """
c4h10+ch3o=sc4h9+ch3oh                              6.000e+11 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + c2h5o <=> pc4h9 + c2h5oh',
 "chemkinKinetics": """
c4h10+c2h5o=pc4h9+c2h5oh                            3.000e+11 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + c2h5o <=> sc4h9 + c2h5oh',
 "chemkinKinetics": """
c4h10+c2h5o=sc4h9+c2h5oh                            6.000e+11 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + pc4h9 <=> sc4h9 + c4h10',
 "chemkinKinetics": """
c4h10+pc4h9=sc4h9+c4h10                             1.000e+11 0.000     10.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + ch3co3 <=> pc4h9 + ch3co3h',
 "chemkinKinetics": """
c4h10+ch3co3=pc4h9+ch3co3h                          1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + ch3co3 <=> sc4h9 + ch3co3h',
 "chemkinKinetics": """
c4h10+ch3co3=sc4h9+ch3co3h                          1.120e+13 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + o2cho <=> pc4h9 + ho2cho',
 "chemkinKinetics": """
c4h10+o2cho=pc4h9+ho2cho                            1.680e+13 0.000     20.440   
""",
 "rmgPyKinetics": Arrhenius(A=(1.68e+13, 'cm^3/(mol*s)'), n=0, Ea=(20440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h10 + o2cho <=> sc4h9 + ho2cho',
 "chemkinKinetics": """
c4h10+o2cho=sc4h9+ho2cho                            1.120e+13 0.000     17.690   
""",
 "rmgPyKinetics": Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + c4h10 <=> ch3o2h + pc4h9',
 "chemkinKinetics": """
ch3o2+c4h10=ch3o2h+pc4h9                            1.386e+00 3.970     18.280   
""",
 "rmgPyKinetics": Arrhenius(A=(1.386, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + c4h10 <=> ch3o2h + sc4h9',
 "chemkinKinetics": """
ch3o2+c4h10=ch3o2h+sc4h9                            2.037e+01 3.580     14.810   
""",
 "rmgPyKinetics": Arrhenius(A=(20.37, 'cm^3/(mol*s)'), n=3.58, Ea=(14810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5o2 + c4h10 <=> c2h5o2h + pc4h9',
 "chemkinKinetics": """
c2h5o2+c4h10=c2h5o2h+pc4h9                          4.080e+01 3.590     17.160   
""",
 "rmgPyKinetics": Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5o2 + c4h10 <=> c2h5o2h + sc4h9',
 "chemkinKinetics": """
c2h5o2+c4h10=c2h5o2h+sc4h9                          1.264e+02 3.370     13.720   
""",
 "rmgPyKinetics": Arrhenius(A=(126.4, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + c4h10 <=> nc3h7o2h + pc4h9',
 "chemkinKinetics": """
nc3h7o2+c4h10=nc3h7o2h+pc4h9                        1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + c4h10 <=> nc3h7o2h + sc4h9',
 "chemkinKinetics": """
nc3h7o2+c4h10=nc3h7o2h+sc4h9                        1.120e+13 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + c4h10 <=> ic3h7o2h + pc4h9',
 "chemkinKinetics": """
ic3h7o2+c4h10=ic3h7o2h+pc4h9                        1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + c4h10 <=> ic3h7o2h + sc4h9',
 "chemkinKinetics": """
ic3h7o2+c4h10=ic3h7o2h+sc4h9                        1.120e+13 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + c3h8 <=> pc4h9o2h + nc3h7',
 "chemkinKinetics": """
pc4h9o2+c3h8=pc4h9o2h+nc3h7                         1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + c3h8 <=> pc4h9o2h + ic3h7',
 "chemkinKinetics": """
pc4h9o2+c3h8=pc4h9o2h+ic3h7                         2.000e+12 0.000     17.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + c4h10 <=> pc4h9o2h + pc4h9',
 "chemkinKinetics": """
pc4h9o2+c4h10=pc4h9o2h+pc4h9                        1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + c4h10 <=> pc4h9o2h + sc4h9',
 "chemkinKinetics": """
pc4h9o2+c4h10=pc4h9o2h+sc4h9                        1.120e+13 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + c3h8 <=> sc4h9o2h + nc3h7',
 "chemkinKinetics": """
sc4h9o2+c3h8=sc4h9o2h+nc3h7                         1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + c3h8 <=> sc4h9o2h + ic3h7',
 "chemkinKinetics": """
sc4h9o2+c3h8=sc4h9o2h+ic3h7                         2.000e+12 0.000     17.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + c4h10 <=> sc4h9o2h + pc4h9',
 "chemkinKinetics": """
sc4h9o2+c4h10=sc4h9o2h+pc4h9                        1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + c4h10 <=> sc4h9o2h + sc4h9',
 "chemkinKinetics": """
sc4h9o2+c4h10=sc4h9o2h+sc4h9                        1.120e+13 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'pc4h9 <=> sc4h9',
 "chemkinKinetics": """
pc4h9=sc4h9                                         3.560e+10 0.880     37.300   
DUPLICATE
""",
 "rmgPyKinetics": Arrhenius(A=(3.56e+10, 's^-1'), n=0.88, Ea=(37300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'pc4h9 <=> sc4h9',
 "chemkinKinetics": """
pc4h9=sc4h9                                         3.800e+10 0.670     36.600   
DUPLICATE
""",
 "rmgPyKinetics": Arrhenius(A=(3.8e+10, 's^-1'), n=0.67, Ea=(36600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c2h5 + c2h4 <=> pc4h9',
 "chemkinKinetics": """
c2h5+c2h4=pc4h9                                     1.320e+04 2.480     6.130    
""",
 "rmgPyKinetics": Arrhenius(A=(13200, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h6 + ch3 <=> sc4h9',
 "chemkinKinetics": """
c3h6+ch3=sc4h9                                      1.760e+04 2.480     6.130    
""",
 "rmgPyKinetics": Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h8-1 + h <=> pc4h9',
 "chemkinKinetics": """
c4h8-1+h=pc4h9                                      2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h8-2 + h <=> sc4h9',
 "chemkinKinetics": """
c4h8-2+h=sc4h9                                      2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h8-1 + h <=> sc4h9',
 "chemkinKinetics": """
c4h8-1+h=sc4h9                                      4.240e+11 0.510     1.230    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.24e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (1230, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'pc4h9 + o2 <=> c4h8-1 + ho2',
 "chemkinKinetics": """
pc4h9+o2=c4h8-1+ho2                                 8.370e-01 3.590     11.960   
""",
 "rmgPyKinetics": Arrhenius(A=(0.837, 'cm^3/(mol*s)'), n=3.59, Ea=(11960, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'sc4h9 + o2 <=> c4h8-1 + ho2',
 "chemkinKinetics": """
sc4h9+o2=c4h8-1+ho2                                 5.350e-01 3.710     9.322    
""",
 "rmgPyKinetics": Arrhenius(A=(0.535, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'sc4h9 + o2 <=> c4h8-2 + ho2',
 "chemkinKinetics": """
sc4h9+o2=c4h8-2+ho2                                 1.070e+00 3.710     9.322    
""",
 "rmgPyKinetics": Arrhenius(A=(1.07, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h3 + c2h5 <=> c4h8-1',
 "chemkinKinetics": """
c2h3+c2h5=c4h8-1                                    9.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c3h5-a + ch3 <=> c4h8-1',
 "chemkinKinetics": """
c3h5-a+ch3(+M)=c4h8-1(+M)                           1.000e+14 -0.320    -0.262   
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ 
    LOW/ 3.910e+60 -12.810   6.250    /
    TROE/ 1.040e-01 1.61e+03  6e+04     6.12e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (-262.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (3.91e+60, 'cm^6/(mol^2*s)'),
        n = -12.81,
        Ea = (6250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.104,
    T3 = (1606, 'K'),
    T1 = (60000, 'K'),
    T2 = (6118.4, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'h + c4h71-3 <=> c4h8-1',
 "chemkinKinetics": """
h+c4h71-3=c4h8-1                                    5.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8-1 + o2 <=> c4h71-3 + ho2',
 "chemkinKinetics": """
c4h8-1+o2=c4h71-3+ho2                               2.000e+13 0.000     37.190   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + o <=> c4h71-3 + oh',
 "chemkinKinetics": """
c4h8-1+o=c4h71-3+oh                                 1.750e+11 0.700     5.884    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.75e+11, 'cm^3/(mol*s)'),
    n = 0.7,
    Ea = (5884, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-2 + o <=> c4h71-3 + oh',
 "chemkinKinetics": """
c4h8-2+o=c4h71-3+oh                                 2.190e+11 0.810     7.550    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.19e+11, 'cm^3/(mol*s)'),
    n = 0.81,
    Ea = (7550, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + h <=> c4h71-3 + h2',
 "chemkinKinetics": """
c4h8-1+h=c4h71-3+h2                                 1.730e+05 2.500     2.492    
""",
 "rmgPyKinetics": Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + h <=> c4h71-4 + h2',
 "chemkinKinetics": """
c4h8-1+h=c4h71-4+h2                                 6.651e+05 2.540     6.756    
""",
 "rmgPyKinetics": Arrhenius(A=(665100, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + oh <=> c4h71-1 + h2o',
 "chemkinKinetics": """
c4h8-1+oh=c4h71-1+h2o                               9.000e+05 2.000     2.500    
""",
 "rmgPyKinetics": Arrhenius(A=(900000, 'cm^3/(mol*s)'), n=2, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + oh <=> c4h71-2 + h2o',
 "chemkinKinetics": """
c4h8-1+oh=c4h71-2+h2o                               2.220e+06 2.000     1.451    
""",
 "rmgPyKinetics": Arrhenius(A=(2.22e+06, 'cm^3/(mol*s)'), n=2, Ea=(1451, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + oh <=> c4h71-3 + h2o',
 "chemkinKinetics": """
c4h8-1+oh=c4h71-3+h2o                               3.120e+06 2.000     -0.298   
""",
 "rmgPyKinetics": Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + oh <=> c4h71-4 + h2o',
 "chemkinKinetics": """
c4h8-1+oh=c4h71-4+h2o                               5.270e+09 0.970     1.586    
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.27e+09, 'cm^3/(mol*s)'),
    n = 0.97,
    Ea = (1586, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + ch3 <=> c4h71-3 + ch4',
 "chemkinKinetics": """
c4h8-1+ch3=c4h71-3+ch4                              2.210e+00 3.500     5.675    
""",
 "rmgPyKinetics": Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + ch3 <=> c4h71-4 + ch4',
 "chemkinKinetics": """
c4h8-1+ch3=c4h71-4+ch4                              4.520e-01 3.650     7.154    
""",
 "rmgPyKinetics": Arrhenius(A=(0.452, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + ho2 <=> c4h71-3 + h2o2',
 "chemkinKinetics": """
c4h8-1+ho2=c4h71-3+h2o2                             2.700e+04 0.700     5.884    
""",
 "rmgPyKinetics": Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=0.7, Ea=(5884, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + ho2 <=> c4h71-4 + h2o2',
 "chemkinKinetics": """
c4h8-1+ho2=c4h71-4+h2o2                             2.380e+03 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(2380, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + ch3o2 <=> c4h71-3 + ch3o2h',
 "chemkinKinetics": """
c4h8-1+ch3o2=c4h71-3+ch3o2h                         2.700e+04 0.700     5.884    
""",
 "rmgPyKinetics": Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=0.7, Ea=(5884, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + ch3o2 <=> c4h71-4 + ch3o2h',
 "chemkinKinetics": """
c4h8-1+ch3o2=c4h71-4+ch3o2h                         2.380e+03 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(2380, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + ch3o <=> c4h71-3 + ch3oh',
 "chemkinKinetics": """
c4h8-1+ch3o=c4h71-3+ch3oh                           4.000e+01 2.900     8.609    
""",
 "rmgPyKinetics": Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + ch3o <=> c4h71-4 + ch3oh',
 "chemkinKinetics": """
c4h8-1+ch3o=c4h71-4+ch3oh                           2.170e+11 0.000     6.458    
""",
 "rmgPyKinetics": Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + ch3co3 <=> c4h71-3 + ch3co3h',
 "chemkinKinetics": """
c4h8-1+ch3co3=c4h71-3+ch3co3h                       1.000e+11 0.000     8.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + c3h5-a <=> c4h71-3 + c3h6',
 "chemkinKinetics": """
c4h8-1+c3h5-a=c4h71-3+c3h6                          7.900e+10 0.000     12.400   
""",
 "rmgPyKinetics": Arrhenius(A=(7.9e+10, 'cm^3/(mol*s)'), n=0, Ea=(12400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h71-3 + c4h71-3 <=> c4h8-1 + c4h6',
 "chemkinKinetics": """
c4h71-3+c4h71-3=c4h8-1+c4h6                         1.600e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h8-1 + c2h5o2 <=> c4h71-3 + c2h5o2h',
 "chemkinKinetics": """
c4h8-1+c2h5o2=c4h71-3+c2h5o2h                       1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + nc3h7o2 <=> c4h71-3 + nc3h7o2h',
 "chemkinKinetics": """
c4h8-1+nc3h7o2=c4h71-3+nc3h7o2h                     1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + ic3h7o2 <=> c4h71-3 + ic3h7o2h',
 "chemkinKinetics": """
c4h8-1+ic3h7o2=c4h71-3+ic3h7o2h                     1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + pc4h9o2 <=> c4h71-3 + pc4h9o2h',
 "chemkinKinetics": """
c4h8-1+pc4h9o2=c4h71-3+pc4h9o2h                     1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + sc4h9o2 <=> c4h71-3 + sc4h9o2h',
 "chemkinKinetics": """
c4h8-1+sc4h9o2=c4h71-3+sc4h9o2h                     1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + ch3o2 <=> c4h8o1-2 + ch3o',
 "chemkinKinetics": """
c4h8-1+ch3o2=c4h8o1-2+ch3o                          1.000e+12 0.000     14.340   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(14340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'h + c4h71-3 <=> c4h8-2',
 "chemkinKinetics": """
h+c4h71-3=c4h8-2                                    5.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8-2 + o2 <=> c4h71-3 + ho2',
 "chemkinKinetics": """
c4h8-2+o2=c4h71-3+ho2                               4.000e+13 0.000     39.390   
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(39390, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-2 + h <=> c4h71-3 + h2',
 "chemkinKinetics": """
c4h8-2+h=c4h71-3+h2                                 4.440e+04 2.810     4.414    
""",
 "rmgPyKinetics": Arrhenius(A=(44400, 'cm^3/(mol*s)'), n=2.81, Ea=(4414, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-2 + oh <=> c4h71-3 + h2o',
 "chemkinKinetics": """
c4h8-2+oh=c4h71-3+h2o                               5.100e+08 1.400     1.250    
""",
 "rmgPyKinetics": Arrhenius(A=(5.1e+08, 'cm^3/(mol*s)'), n=1.4, Ea=(1250, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-2 + ch3 <=> c4h71-3 + ch4',
 "chemkinKinetics": """
c4h8-2+ch3=c4h71-3+ch4                              7.140e+00 3.570     7.642    
""",
 "rmgPyKinetics": Arrhenius(A=(7.14, 'cm^3/(mol*s)'), n=3.57, Ea=(7642, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-2 + ho2 <=> c4h71-3 + h2o2',
 "chemkinKinetics": """
c4h8-2+ho2=c4h71-3+h2o2                             5.940e+04 2.570     16.140   
""",
 "rmgPyKinetics": Arrhenius(A=(59400, 'cm^3/(mol*s)'), n=2.57, Ea=(16140, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-2 + ch3o2 <=> c4h71-3 + ch3o2h',
 "chemkinKinetics": """
c4h8-2+ch3o2=c4h71-3+ch3o2h                         5.940e+04 2.570     16.140   
""",
 "rmgPyKinetics": Arrhenius(A=(59400, 'cm^3/(mol*s)'), n=2.57, Ea=(16140, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-2 + ch3o <=> c4h71-3 + ch3oh',
 "chemkinKinetics": """
c4h8-2+ch3o=c4h71-3+ch3oh                           1.800e+01 2.950     11.990   
""",
 "rmgPyKinetics": Arrhenius(A=(18, 'cm^3/(mol*s)'), n=2.95, Ea=(11990, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-2 + c2h5o2 <=> c4h71-3 + c2h5o2h',
 "chemkinKinetics": """
c4h8-2+c2h5o2=c4h71-3+c2h5o2h                       3.200e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-2 + nc3h7o2 <=> c4h71-3 + nc3h7o2h',
 "chemkinKinetics": """
c4h8-2+nc3h7o2=c4h71-3+nc3h7o2h                     3.200e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-2 + ic3h7o2 <=> c4h71-3 + ic3h7o2h',
 "chemkinKinetics": """
c4h8-2+ic3h7o2=c4h71-3+ic3h7o2h                     3.200e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-2 + pc4h9o2 <=> c4h71-3 + pc4h9o2h',
 "chemkinKinetics": """
c4h8-2+pc4h9o2=c4h71-3+pc4h9o2h                     3.200e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-2 + sc4h9o2 <=> c4h71-3 + sc4h9o2h',
 "chemkinKinetics": """
c4h8-2+sc4h9o2=c4h71-3+sc4h9o2h                     3.200e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8-1 + ho2 <=> c4h8o1-2 + oh',
 "chemkinKinetics": """
c4h8-1+ho2=c4h8o1-2+oh                              1.000e+12 0.000     14.340   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(14340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8-2 + ho2 <=> c4h8o2-3 + oh',
 "chemkinKinetics": """
c4h8-2+ho2=c4h8o2-3+oh                              5.620e+11 0.000     12.310   
""",
 "rmgPyKinetics": Arrhenius(A=(5.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(12310, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8-2 + ch3o2 <=> c4h8o2-3 + ch3o',
 "chemkinKinetics": """
c4h8-2+ch3o2=c4h8o2-3+ch3o                          5.620e+11 0.000     12.310   
""",
 "rmgPyKinetics": Arrhenius(A=(5.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(12310, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + c2h5 <=> c4h71-1',
 "chemkinKinetics": """
c2h2+c2h5=c4h71-1                                   2.000e+11 0.000     7.800    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h4-a + ch3 <=> c4h71-2',
 "chemkinKinetics": """
c3h4-a+ch3=c4h71-2                                  2.000e+11 0.000     7.800    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h4 + c2h3 <=> c4h71-4',
 "chemkinKinetics": """
c2h4+c2h3=c4h71-4                                   2.000e+11 0.000     7.800    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h4-p + ch3 <=> c4h72-2',
 "chemkinKinetics": """
c3h4-p+ch3=c4h72-2                                  1.000e+11 0.000     7.800    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h6 + h <=> c4h71-3',
 "chemkinKinetics": """
c4h6+h=c4h71-3                                      4.000e+13 0.000     1.300    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(1300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h71-3 + c2h5 <=> c4h8-1 + c2h4',
 "chemkinKinetics": """
c4h71-3+c2h5=c4h8-1+c2h4                            2.590e+12 0.000     -0.131   
""",
 "rmgPyKinetics": Arrhenius(A=(2.59e+12, 'cm^3/(mol*s)'), n=0, Ea=(-131, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h71-3 + ch3o <=> c4h8-1 + ch2o',
 "chemkinKinetics": """
c4h71-3+ch3o=c4h8-1+ch2o                            2.410e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h71-3 + o <=> c2h3cho + ch3',
 "chemkinKinetics": """
c4h71-3+o=c2h3cho+ch3                               6.030e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h71-3 + ho2 <=> c4h7o + oh',
 "chemkinKinetics": """
c4h71-3+ho2=c4h7o+oh                                9.640e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(9.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h71-3 + ch3o2 <=> c4h7o + ch3o',
 "chemkinKinetics": """
c4h71-3+ch3o2=c4h7o+ch3o                            9.640e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(9.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c3h5-a + c4h71-3 <=> c3h6 + c4h6',
 "chemkinKinetics": """
c3h5-a+c4h71-3=c3h6+c4h6                            6.310e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6.31e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h71-3 + o2 <=> c4h6 + ho2',
 "chemkinKinetics": """
c4h71-3+o2=c4h6+ho2                                 1.000e+09 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'h + c4h71-3 <=> c4h6 + h2',
 "chemkinKinetics": """
h+c4h71-3=c4h6+h2                                   3.160e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.16e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h5 + c4h71-3 <=> c4h6 + c2h6',
 "chemkinKinetics": """
c2h5+c4h71-3=c4h6+c2h6                              3.980e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h3 + c4h71-3 <=> c2h4 + c4h6',
 "chemkinKinetics": """
c2h3+c4h71-3=c2h4+c4h6                              3.980e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h71-3 + c2h5o2 <=> c4h7o + c2h5o',
 "chemkinKinetics": """
c4h71-3+c2h5o2=c4h7o+c2h5o                          3.800e+12 0.000     -1.200   
""",
 "rmgPyKinetics": Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + c4h71-3 <=> ic3h7o + c4h7o',
 "chemkinKinetics": """
ic3h7o2+c4h71-3=ic3h7o+c4h7o                        3.800e+12 0.000     -1.200   
""",
 "rmgPyKinetics": Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + c4h71-3 <=> nc3h7o + c4h7o',
 "chemkinKinetics": """
nc3h7o2+c4h71-3=nc3h7o+c4h7o                        3.800e+12 0.000     -1.200   
""",
 "rmgPyKinetics": Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h7o <=> ch3cho + c2h3',
 "chemkinKinetics": """
c4h7o=ch3cho+c2h3                                   7.940e+14 0.000     19.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7.94e+14, 's^-1'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7o <=> c2h3cho + ch3',
 "chemkinKinetics": """
c4h7o=c2h3cho+ch3                                   7.940e+14 0.000     19.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7.94e+14, 's^-1'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h6 <=> c4h5-i + h',
 "chemkinKinetics": """
c4h6=c4h5-i+h                                       5.700e+36 -6.270    112.353  
""",
 "rmgPyKinetics": Arrhenius(A=(5.7e+36, 's^-1'), n=-6.27, Ea=(112353, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h6 <=> c4h5-n + h',
 "chemkinKinetics": """
c4h6=c4h5-n+h                                       5.300e+44 -8.620    123.608  
""",
 "rmgPyKinetics": Arrhenius(A=(5.3e+44, 's^-1'), n=-8.62, Ea=(123608, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h6 <=> c4h4 + h2',
 "chemkinKinetics": """
c4h6=c4h4+h2                                        2.500e+15 0.000     94.700   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+15, 's^-1'), n=0, Ea=(94700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6 + h <=> c4h5-n + h2',
 "chemkinKinetics": """
c4h6+h=c4h5-n+h2                                    1.330e+06 2.530     12.240   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.33e+06, 'cm^3/(mol*s)'),
    n = 2.53,
    Ea = (12240, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h6 + h <=> c4h5-i + h2',
 "chemkinKinetics": """
c4h6+h=c4h5-i+h2                                    6.650e+05 2.530     9.240    
""",
 "rmgPyKinetics": Arrhenius(A=(665000, 'cm^3/(mol*s)'), n=2.53, Ea=(9240, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h6 + h <=> c2h4 + c2h3',
 "chemkinKinetics": """
c4h6+h=c2h4+c2h3                                    1.000e+00 0.000     0.000    
    PLOG/ 1.000     1.460e+30 -4.340    21.647   /
    PLOG/ 10.000    5.450e+30 -4.510    21.877   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (1.46e+30, 'cm^3/(mol*s)'),
            n = -4.34,
            Ea = (21647, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.45e+30, 'cm^3/(mol*s)'),
            n = -4.51,
            Ea = (21877, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6 + h <=> c3h4-p + ch3',
 "chemkinKinetics": """
c4h6+h=c3h4-p+ch3                                   2.000e+12 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6 + h <=> c3h4-a + ch3',
 "chemkinKinetics": """
c4h6+h=c3h4-a+ch3                                   2.000e+12 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6 + o <=> c4h5-n + oh',
 "chemkinKinetics": """
c4h6+o=c4h5-n+oh                                    7.500e+06 1.900     3.740    
""",
 "rmgPyKinetics": Arrhenius(A=(7.5e+06, 'cm^3/(mol*s)'), n=1.9, Ea=(3740, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h6 + o <=> c4h5-i + oh',
 "chemkinKinetics": """
c4h6+o=c4h5-i+oh                                    7.500e+06 1.900     3.740    
""",
 "rmgPyKinetics": Arrhenius(A=(7.5e+06, 'cm^3/(mol*s)'), n=1.9, Ea=(3740, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h6 + o <=> c2h2 + c2h4o1-2',
 "chemkinKinetics": """
c4h6+o=c2h2+c2h4o1-2                                1.000e+08 1.450     -0.860   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+08, 'cm^3/(mol*s)'), n=1.45, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6 + o <=> ch3chchco + h',
 "chemkinKinetics": """
c4h6+o=ch3chchco+h                                  5.000e+07 1.450     -0.860   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+07, 'cm^3/(mol*s)'), n=1.45, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6 + o <=> ch2chchcho + h',
 "chemkinKinetics": """
c4h6+o=ch2chchcho+h                                 4.500e+08 1.450     -0.860   
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.5e+08, 'cm^3/(mol*s)'),
    n = 1.45,
    Ea = (-860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6 + oh <=> c4h5-n + h2o',
 "chemkinKinetics": """
c4h6+oh=c4h5-n+h2o                                  6.200e+06 2.000     3.430    
""",
 "rmgPyKinetics": Arrhenius(A=(6.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(3430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h6 + oh <=> c4h5-i + h2o',
 "chemkinKinetics": """
c4h6+oh=c4h5-i+h2o                                  3.100e+06 2.000     0.430    
""",
 "rmgPyKinetics": Arrhenius(A=(3.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h6 + ho2 <=> c4h6o25 + oh',
 "chemkinKinetics": """
c4h6+ho2=c4h6o25+oh                                 1.200e+12 0.000     14.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6 + ho2 <=> c2h3choch2 + oh',
 "chemkinKinetics": """
c4h6+ho2=c2h3choch2+oh                              4.800e+12 0.000     14.000   
""",
 "rmgPyKinetics": Arrhenius(A=(4.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6 + ch3 <=> c4h5-n + ch4',
 "chemkinKinetics": """
c4h6+ch3=c4h5-n+ch4                                 2.000e+14 0.000     22.800   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(22800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h6 + ch3 <=> c4h5-i + ch4',
 "chemkinKinetics": """
c4h6+ch3=c4h5-i+ch4                                 1.000e+14 0.000     19.800   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(19800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h6 + c2h3 <=> c4h5-n + c2h4',
 "chemkinKinetics": """
c4h6+c2h3=c4h5-n+c2h4                               5.000e+13 0.000     22.800   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(22800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h6 + c2h3 <=> c4h5-i + c2h4',
 "chemkinKinetics": """
c4h6+c2h3=c4h5-i+c2h4                               2.500e+13 0.000     19.800   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(19800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h6 + c3h3 <=> c4h5-n + c3h4-a',
 "chemkinKinetics": """
c4h6+c3h3=c4h5-n+c3h4-a                             1.000e+13 0.000     22.500   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(22500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6 + c3h3 <=> c4h5-i + c3h4-a',
 "chemkinKinetics": """
c4h6+c3h3=c4h5-i+c3h4-a                             5.000e+12 0.000     19.500   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6 + c3h5-a <=> c4h5-n + c3h6',
 "chemkinKinetics": """
c4h6+c3h5-a=c4h5-n+c3h6                             1.000e+13 0.000     22.500   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(22500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h6 + c3h5-a <=> c4h5-i + c3h6',
 "chemkinKinetics": """
c4h6+c3h5-a=c4h5-i+c3h6                             5.000e+12 0.000     19.500   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h71-4 <=> c4h6 + h',
 "chemkinKinetics": """
c4h71-4=c4h6+h                                      1.000e+00 0.000     0.000    
    PLOG/ 1.000     2.480e+53 -12.300   52.000   /
    PLOG/ 10.000    1.850e+48 -10.500   51.770   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(2.48e+53, 's^-1'), n=-12.3, Ea=(52000, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.85e+48, 's^-1'), n=-10.5, Ea=(51770, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h3 + c2h2 <=> c4h4 + h',
 "chemkinKinetics": """
c2h3+c2h2=c4h4+h                                    1.000e+00 0.000     0.000    
    PLOG/ 0.013     7.200e+13 -0.480    6.100    /
    PLOG/ 0.026     5.000e+14 -0.710    6.700    /
    PLOG/ 0.120     4.600e+16 -1.250    8.400    /
    PLOG/ 1.000     2.000e+18 -1.680    10.600   /
    PLOG/ 10.000    4.900e+16 -1.130    11.800   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (7.2e+13, 'cm^3/(mol*s)'),
            n = -0.48,
            Ea = (6100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(A=(5e+14, 'cm^3/(mol*s)'), n=-0.71, Ea=(6700, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(
            A = (4.6e+16, 'cm^3/(mol*s)'),
            n = -1.25,
            Ea = (8400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2e+18, 'cm^3/(mol*s)'),
            n = -1.68,
            Ea = (10600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.9e+16, 'cm^3/(mol*s)'),
            n = -1.13,
            Ea = (11800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3 + c2h2 <=> c4h5-n',
 "chemkinKinetics": """
c2h3+c2h2=c4h5-n                                    1.000e+00 0.000     0.000    
    PLOG/ 0.013     1.100e+31 -7.140    5.600    /
    PLOG/ 0.026     1.100e+32 -7.330    6.200    /
    PLOG/ 0.120     2.400e+31 -6.950    5.600    /
    PLOG/ 1.000     9.300e+38 -8.760    12.000   /
    PLOG/ 10.000    8.100e+37 -8.090    13.400   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (1.1e+31, 'cm^3/(mol*s)'),
            n = -7.14,
            Ea = (5600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.1e+32, 'cm^3/(mol*s)'),
            n = -7.33,
            Ea = (6200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.4e+31, 'cm^3/(mol*s)'),
            n = -6.95,
            Ea = (5600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (9.3e+38, 'cm^3/(mol*s)'),
            n = -8.76,
            Ea = (12000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (8.1e+37, 'cm^3/(mol*s)'),
            n = -8.09,
            Ea = (13400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h3 + c2h2 <=> c4h5-i',
 "chemkinKinetics": """
c2h3+c2h2=c4h5-i                                    1.000e+00 0.000     0.000    
    PLOG/ 0.013     5.000e+34 -8.420    7.900    /
    PLOG/ 0.026     2.100e+36 -8.780    9.100    /
    PLOG/ 0.120     1.000e+37 -8.770    9.800    /
    PLOG/ 1.000     1.600e+46 -10.980   18.600   /
    PLOG/ 10.000    5.100e+53 -12.640   28.800   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(5e+34, 'cm^3/(mol*s)'), n=-8.42, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(
            A = (2.1e+36, 'cm^3/(mol*s)'),
            n = -8.78,
            Ea = (9100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(A=(1e+37, 'cm^3/(mol*s)'), n=-8.77, Ea=(9800, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(
            A = (1.6e+46, 'cm^3/(mol*s)'),
            n = -10.98,
            Ea = (18600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.1e+53, 'cm^3/(mol*s)'),
            n = -12.64,
            Ea = (28800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3 + c2h3 <=> c4h6',
 "chemkinKinetics": """
c2h3+c2h3=c4h6                                      1.000e+00 0.000     0.000    
    PLOG/ 0.026     7.000e+57 -13.820   17.629   /
    PLOG/ 0.120     1.500e+52 -11.970   16.056   /
    PLOG/ 1.000     1.500e+42 -8.840    12.483   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.0263, 0.12, 1], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (7e+57, 'cm^3/(mol*s)'),
            n = -13.82,
            Ea = (17629, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.5e+52, 'cm^3/(mol*s)'),
            n = -11.97,
            Ea = (16056, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.5e+42, 'cm^3/(mol*s)'),
            n = -8.84,
            Ea = (12483, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c2h3 + c2h3 <=> c4h5-i + h',
 "chemkinKinetics": """
c2h3+c2h3=c4h5-i+h                                  1.000e+00 0.000     0.000    
    PLOG/ 0.026     1.500e+30 -4.950    12.958   /
    PLOG/ 0.120     7.200e+28 -4.490    14.273   /
    PLOG/ 1.000     1.200e+22 -2.440    13.654   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.0263, 0.12, 1], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (1.5e+30, 'cm^3/(mol*s)'),
            n = -4.95,
            Ea = (12958, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (7.2e+28, 'cm^3/(mol*s)'),
            n = -4.49,
            Ea = (14273, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.2e+22, 'cm^3/(mol*s)'),
            n = -2.44,
            Ea = (13654, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3 + c2h3 <=> c4h5-n + h',
 "chemkinKinetics": """
c2h3+c2h3=c4h5-n+h                                  1.000e+00 0.000     0.000    
    PLOG/ 0.026     1.100e+24 -3.280    12.395   /
    PLOG/ 0.120     4.600e+24 -3.380    14.650   /
    PLOG/ 1.000     2.400e+20 -2.040    15.361   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.0263, 0.12, 1], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (1.1e+24, 'cm^3/(mol*s)'),
            n = -3.28,
            Ea = (12395, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.6e+24, 'cm^3/(mol*s)'),
            n = -3.38,
            Ea = (14650, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.4e+20, 'cm^3/(mol*s)'),
            n = -2.04,
            Ea = (15361, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h5-n <=> c4h5-i',
 "chemkinKinetics": """
c4h5-n=c4h5-i                                       1.000e+00 0.000     0.000    
    PLOG/ 0.013     2.400e+60 -16.080   47.500   /
    PLOG/ 0.026     1.300e+62 -16.380   49.600   /
    PLOG/ 0.120     4.900e+66 -17.260   55.400   /
    PLOG/ 1.000     1.500e+67 -16.890   59.100   /
    PLOG/ 10.000    2.000e+60 -14.460   58.600   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(A=(2.4e+60, 's^-1'), n=-16.08, Ea=(47500, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.3e+62, 's^-1'), n=-16.38, Ea=(49600, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(4.9e+66, 's^-1'), n=-17.26, Ea=(55400, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(1.5e+67, 's^-1'), n=-16.89, Ea=(59100, 'cal/mol'), T0=(1, 'K')),
        Arrhenius(A=(2e+60, 's^-1'), n=-14.46, Ea=(58600, 'cal/mol'), T0=(1, 'K')),
    ],
),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h5-n + h <=> c4h5-i + h',
 "chemkinKinetics": """
c4h5-n+h=c4h5-i+h                                   3.100e+26 -3.350    17.423   
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.1e+26, 'cm^3/(mol*s)'),
    n = -3.35,
    Ea = (17423, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h5-n + h <=> c4h4 + h2',
 "chemkinKinetics": """
c4h5-n+h=c4h4+h2                                    1.500e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h5-n + oh <=> c4h4 + h2o',
 "chemkinKinetics": """
c4h5-n+oh=c4h4+h2o                                  2.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h5-n + hco <=> c4h6 + co',
 "chemkinKinetics": """
c4h5-n+hco=c4h6+co                                  5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h5-n + ho2 => c2h3 + ch2co + oh',
 "chemkinKinetics": """
c4h5-n+ho2=>c2h3+ch2co+oh                           6.600e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h5-n + h2o2 <=> c4h6 + ho2',
 "chemkinKinetics": """
c4h5-n+h2o2=c4h6+ho2                                1.210e+10 0.000     -0.596   
""",
 "rmgPyKinetics": Arrhenius(A=(1.21e+10, 'cm^3/(mol*s)'), n=0, Ea=(-596, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h5-n + ho2 <=> c4h6 + o2',
 "chemkinKinetics": """
c4h5-n+ho2=c4h6+o2                                  6.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h5-n + o2 <=> ch2chchcho + o',
 "chemkinKinetics": """
c4h5-n+o2=ch2chchcho+o                              3.000e+11 0.290     0.011    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0.29, Ea=(11, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h5-n + o2 <=> hco + c2h3cho',
 "chemkinKinetics": """
c4h5-n+o2=hco+c2h3cho                               9.200e+16 -1.390    1.010    
""",
 "rmgPyKinetics": Arrhenius(
    A = (9.2e+16, 'cm^3/(mol*s)'),
    n = -1.39,
    Ea = (1010, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h5-i + h <=> c4h4 + h2',
 "chemkinKinetics": """
c4h5-i+h=c4h4+h2                                    3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h5-i + h <=> c3h3 + ch3',
 "chemkinKinetics": """
c4h5-i+h=c3h3+ch3                                   2.000e+13 0.000     2.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h5-i + oh <=> c4h4 + h2o',
 "chemkinKinetics": """
c4h5-i+oh=c4h4+h2o                                  4.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h5-i + hco <=> c4h6 + co',
 "chemkinKinetics": """
c4h5-i+hco=c4h6+co                                  5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h5-i + ho2 <=> c4h6 + o2',
 "chemkinKinetics": """
c4h5-i+ho2=c4h6+o2                                  6.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h5-i + ho2 => c2h3 + ch2co + oh',
 "chemkinKinetics": """
c4h5-i+ho2=>c2h3+ch2co+oh                           6.600e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h5-i + h2o2 <=> c4h6 + ho2',
 "chemkinKinetics": """
c4h5-i+h2o2=c4h6+ho2                                1.210e+10 0.000     -0.596   
""",
 "rmgPyKinetics": Arrhenius(A=(1.21e+10, 'cm^3/(mol*s)'), n=0, Ea=(-596, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h5-i + o2 <=> ch2co + ch2cho',
 "chemkinKinetics": """
c4h5-i+o2=ch2co+ch2cho                              2.160e+10 0.000     2.500    
""",
 "rmgPyKinetics": Arrhenius(A=(2.16e+10, 'cm^3/(mol*s)'), n=0, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h5-2 <=> c4h5-i',
 "chemkinKinetics": """
c4h5-2=c4h5-i                                       1.500e+67 -16.890   59.100   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+67, 's^-1'), n=-16.89, Ea=(59100, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h5-2 + h <=> c4h5-i + h',
 "chemkinKinetics": """
c4h5-2+h=c4h5-i+h                                   3.100e+26 -3.350    17.423   
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.1e+26, 'cm^3/(mol*s)'),
    n = -3.35,
    Ea = (17423, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h5-2 + ho2 => oh + c2h2 + ch3co',
 "chemkinKinetics": """
c4h5-2+ho2=>oh+c2h2+ch3co                           8.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h5-2 + o2 <=> ch3co + ch2co',
 "chemkinKinetics": """
c4h5-2+o2=ch3co+ch2co                               2.160e+10 0.000     2.500    
""",
 "rmgPyKinetics": Arrhenius(A=(2.16e+10, 'cm^3/(mol*s)'), n=0, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h612 <=> c4h5-i + h',
 "chemkinKinetics": """
c4h612=c4h5-i+h                                     4.200e+15 0.000     92.600   
""",
 "rmgPyKinetics": Arrhenius(A=(4.2e+15, 's^-1'), n=0, Ea=(92600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h612 + h <=> c4h6 + h',
 "chemkinKinetics": """
c4h612+h=c4h6+h                                     2.000e+13 0.000     4.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h612 + h <=> c4h5-i + h2',
 "chemkinKinetics": """
c4h612+h=c4h5-i+h2                                  1.700e+05 2.500     2.490    
""",
 "rmgPyKinetics": Arrhenius(A=(170000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h612 + h <=> c3h4-a + ch3',
 "chemkinKinetics": """
c4h612+h=c3h4-a+ch3                                 2.000e+13 0.000     2.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h612 + h <=> c3h4-p + ch3',
 "chemkinKinetics": """
c4h612+h=c3h4-p+ch3                                 2.000e+13 0.000     2.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h612 + ch3 <=> c4h5-i + ch4',
 "chemkinKinetics": """
c4h612+ch3=c4h5-i+ch4                               7.000e+13 0.000     18.500   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(18500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h612 + o <=> ch2co + c2h4',
 "chemkinKinetics": """
c4h612+o=ch2co+c2h4                                 1.200e+08 1.650     0.327    
""",
 "rmgPyKinetics": Arrhenius(A=(1.2e+08, 'cm^3/(mol*s)'), n=1.65, Ea=(327, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h612 + o <=> c4h5-i + oh',
 "chemkinKinetics": """
c4h612+o=c4h5-i+oh                                  1.800e+11 0.700     5.880    
""",
 "rmgPyKinetics": Arrhenius(A=(1.8e+11, 'cm^3/(mol*s)'), n=0.7, Ea=(5880, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h612 + oh <=> c4h5-i + h2o',
 "chemkinKinetics": """
c4h612+oh=c4h5-i+h2o                                3.100e+06 2.000     -0.298   
""",
 "rmgPyKinetics": Arrhenius(A=(3.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h612 <=> c4h6',
 "chemkinKinetics": """
c4h612=c4h6                                         3.000e+13 0.000     65.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 's^-1'), n=0, Ea=(65000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6-2 <=> c4h6',
 "chemkinKinetics": """
c4h6-2=c4h6                                         3.000e+13 0.000     65.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 's^-1'), n=0, Ea=(65000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6-2 <=> c4h612',
 "chemkinKinetics": """
c4h6-2=c4h612                                       3.000e+13 0.000     67.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 's^-1'), n=0, Ea=(67000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6-2 + h <=> c4h612 + h',
 "chemkinKinetics": """
c4h6-2+h=c4h612+h                                   2.000e+13 0.000     4.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6-2 + h <=> c4h5-2 + h2',
 "chemkinKinetics": """
c4h6-2+h=c4h5-2+h2                                  3.400e+05 2.500     2.490    
""",
 "rmgPyKinetics": Arrhenius(A=(340000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h6-2 + h <=> ch3 + c3h4-p',
 "chemkinKinetics": """
c4h6-2+h=ch3+c3h4-p                                 2.600e+05 2.500     1.000    
""",
 "rmgPyKinetics": Arrhenius(A=(260000, 'cm^3/(mol*s)'), n=2.5, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6-2 <=> h + c4h5-2',
 "chemkinKinetics": """
c4h6-2=h+c4h5-2                                     5.000e+15 0.000     87.300   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+15, 's^-1'), n=0, Ea=(87300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h6-2 + ch3 <=> c4h5-2 + ch4',
 "chemkinKinetics": """
c4h6-2+ch3=c4h5-2+ch4                               1.400e+14 0.000     18.500   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+14, 'cm^3/(mol*s)'), n=0, Ea=(18500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3choch2 <=> c4h6o23',
 "chemkinKinetics": """
c2h3choch2=c4h6o23                                  2.000e+14 0.000     50.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+14, 's^-1'), n=0, Ea=(50600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Birad_recombination',  ],
},

{
 "reaction": 'c4h6o23 <=> ch3chchcho',
 "chemkinKinetics": """
c4h6o23=ch3chchcho                                  1.950e+13 0.000     49.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1.95e+13, 's^-1'), n=0, Ea=(49400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6o23 <=> c2h4 + ch2co',
 "chemkinKinetics": """
c4h6o23=c2h4+ch2co                                  5.750e+15 0.000     69.300   
""",
 "rmgPyKinetics": Arrhenius(A=(5.75e+15, 's^-1'), n=0, Ea=(69300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6o23 <=> c2h2 + c2h4o1-2',
 "chemkinKinetics": """
c4h6o23=c2h2+c2h4o1-2                               1.000e+16 0.000     75.800   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(75800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6o25 <=> c4h4o + h2',
 "chemkinKinetics": """
c4h6o25=c4h4o+h2                                    5.300e+12 0.000     48.500   
""",
 "rmgPyKinetics": Arrhenius(A=(5.3e+12, 's^-1'), n=0, Ea=(48500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h4o <=> co + c3h4-p',
 "chemkinKinetics": """
c4h4o=co+c3h4-p                                     1.780e+15 0.000     77.500   
""",
 "rmgPyKinetics": Arrhenius(A=(1.78e+15, 's^-1'), n=0, Ea=(77500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h4o <=> c2h2 + ch2co',
 "chemkinKinetics": """
c4h4o=c2h2+ch2co                                    5.010e+14 0.000     77.500   
""",
 "rmgPyKinetics": Arrhenius(A=(5.01e+14, 's^-1'), n=0, Ea=(77500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chchcho <=> c3h6 + co',
 "chemkinKinetics": """
ch3chchcho=c3h6+co                                  3.900e+14 0.000     69.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3.9e+14, 's^-1'), n=0, Ea=(69000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chchcho + h <=> ch2chchcho + h2',
 "chemkinKinetics": """
ch3chchcho+h=ch2chchcho+h2                          1.700e+05 2.500     2.490    
""",
 "rmgPyKinetics": Arrhenius(A=(170000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3chchcho + h <=> ch3chchco + h2',
 "chemkinKinetics": """
ch3chchcho+h=ch3chchco+h2                           1.000e+05 2.500     2.490    
""",
 "rmgPyKinetics": Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3chchcho + h <=> ch3 + c2h3cho',
 "chemkinKinetics": """
ch3chchcho+h=ch3+c2h3cho                            4.000e+21 -2.390    11.180   
""",
 "rmgPyKinetics": Arrhenius(
    A = (4e+21, 'cm^3/(mol*s)'),
    n = -2.39,
    Ea = (11180, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chchcho + h <=> c3h6 + hco',
 "chemkinKinetics": """
ch3chchcho+h=c3h6+hco                               4.000e+21 -2.390    11.180   
""",
 "rmgPyKinetics": Arrhenius(
    A = (4e+21, 'cm^3/(mol*s)'),
    n = -2.39,
    Ea = (11180, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chchcho + ch3 <=> ch2chchcho + ch4',
 "chemkinKinetics": """
ch3chchcho+ch3=ch2chchcho+ch4                       2.100e+00 3.500     5.675    
""",
 "rmgPyKinetics": Arrhenius(A=(2.1, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3chchcho + ch3 <=> ch3chchco + ch4',
 "chemkinKinetics": """
ch3chchcho+ch3=ch3chchco+ch4                        1.100e+00 3.500     5.675    
""",
 "rmgPyKinetics": Arrhenius(A=(1.1, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3chchcho + c2h3 <=> ch2chchcho + c2h4',
 "chemkinKinetics": """
ch3chchcho+c2h3=ch2chchcho+c2h4                     2.210e+00 3.500     4.682    
""",
 "rmgPyKinetics": Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(4682, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3chchcho + c2h3 <=> ch3chchco + c2h4',
 "chemkinKinetics": """
ch3chchcho+c2h3=ch3chchco+c2h4                      1.110e+00 3.500     4.682    
""",
 "rmgPyKinetics": Arrhenius(A=(1.11, 'cm^3/(mol*s)'), n=3.5, Ea=(4682, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3chchco <=> c3h5-s + co',
 "chemkinKinetics": """
ch3chchco=c3h5-s+co                                 1.000e+14 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chchco + h <=> ch3chchcho',
 "chemkinKinetics": """
ch3chchco+h=ch3chchcho                              1.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch2chchcho <=> c3h5-a + co',
 "chemkinKinetics": """
ch2chchcho=c3h5-a+co                                1.000e+14 0.000     25.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2chchcho + h <=> ch3chchcho',
 "chemkinKinetics": """
ch2chchcho+h=ch3chchcho                             1.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h4 + h <=> c4h5-n',
 "chemkinKinetics": """
c4h4+h=c4h5-n                                       1.000e+00 0.000     0.000    
    PLOG/ 0.013     1.200e+51 -12.570   12.300   /
    PLOG/ 0.026     4.200e+50 -12.340   12.500   /
    PLOG/ 0.120     1.100e+50 -11.940   13.400   /
    PLOG/ 1.000     1.300e+51 -11.920   16.500   /
    PLOG/ 10.000    6.200e+45 -10.080   15.800   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (1.2e+51, 'cm^3/(mol*s)'),
            n = -12.57,
            Ea = (12300, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.2e+50, 'cm^3/(mol*s)'),
            n = -12.34,
            Ea = (12500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.1e+50, 'cm^3/(mol*s)'),
            n = -11.94,
            Ea = (13400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.3e+51, 'cm^3/(mol*s)'),
            n = -11.92,
            Ea = (16500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (6.2e+45, 'cm^3/(mol*s)'),
            n = -10.08,
            Ea = (15800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h4 + h <=> c4h5-i',
 "chemkinKinetics": """
c4h4+h=c4h5-i                                       1.000e+00 0.000     0.000    
    PLOG/ 0.013     6.100e+53 -13.190   14.200   /
    PLOG/ 0.026     9.600e+52 -12.850   14.300   /
    PLOG/ 0.120     2.100e+52 -12.440   15.500   /
    PLOG/ 1.000     4.900e+51 -11.920   17.700   /
    PLOG/ 10.000    1.500e+48 -10.580   18.800   /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (6.1e+53, 'cm^3/(mol*s)'),
            n = -13.19,
            Ea = (14200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (9.6e+52, 'cm^3/(mol*s)'),
            n = -12.85,
            Ea = (14300, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (2.1e+52, 'cm^3/(mol*s)'),
            n = -12.44,
            Ea = (15500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (4.9e+51, 'cm^3/(mol*s)'),
            n = -11.92,
            Ea = (17700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.5e+48, 'cm^3/(mol*s)'),
            n = -10.58,
            Ea = (18800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h4 + h <=> c4h3-n + h2',
 "chemkinKinetics": """
c4h4+h=c4h3-n+h2                                    6.650e+05 2.530     12.240   
""",
 "rmgPyKinetics": Arrhenius(
    A = (665000, 'cm^3/(mol*s)'),
    n = 2.53,
    Ea = (12240, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h4 + h <=> c4h3-i + h2',
 "chemkinKinetics": """
c4h4+h=c4h3-i+h2                                    3.330e+05 2.530     9.240    
""",
 "rmgPyKinetics": Arrhenius(A=(333000, 'cm^3/(mol*s)'), n=2.53, Ea=(9240, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h4 + oh <=> c4h3-n + h2o',
 "chemkinKinetics": """
c4h4+oh=c4h3-n+h2o                                  3.100e+07 2.000     3.430    
""",
 "rmgPyKinetics": Arrhenius(A=(3.1e+07, 'cm^3/(mol*s)'), n=2, Ea=(3430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h4 + oh <=> c4h3-i + h2o',
 "chemkinKinetics": """
c4h4+oh=c4h3-i+h2o                                  1.550e+07 2.000     0.430    
""",
 "rmgPyKinetics": Arrhenius(A=(1.55e+07, 'cm^3/(mol*s)'), n=2, Ea=(430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h4 + o <=> c3h3 + hco',
 "chemkinKinetics": """
c4h4+o=c3h3+hco                                     6.000e+08 1.450     -0.860   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+08, 'cm^3/(mol*s)'), n=1.45, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h3 + hcco <=> c4h4 + co',
 "chemkinKinetics": """
c3h3+hcco=c4h4+co                                   2.500e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h3 + ch <=> c4h3-i + h',
 "chemkinKinetics": """
c3h3+ch=c4h3-i+h                                    5.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h3 + ch2 <=> c4h4 + h',
 "chemkinKinetics": """
c3h3+ch2=c4h4+h                                     5.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h3 + ch3 <=> c4h612',
 "chemkinKinetics": """
c3h3+ch3(+M)=c4h612(+M)                             1.500e+12 0.000     0.000    
co2/2.00/ ch4/2.00/ co/1.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ ar/0.70/ 
    LOW/ 2.600e+57 -11.940   9.770    /
    TROE/ 1.750e-01 1.34e+03  6e+04     9.77e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (2.6e+57, 'cm^6/(mol^2*s)'),
        n = -11.94,
        Ea = (9770, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.175,
    T3 = (1340.6, 'K'),
    T1 = (60000, 'K'),
    T2 = (9769.8, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='[Ar]'): 0.7,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[H][H]'): 2,
    },
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + c2h <=> c4h3-n',
 "chemkinKinetics": """
c2h2+c2h(+M)=c4h3-n(+M)                             8.300e+10 0.899     -0.363   
co2/2.00/ ch4/2.00/ c2h2/2.50/ co/1.50/ c2h4/2.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ 
    LOW/ 1.240e+31 -4.718    1.871    /
    TROE/ 1.000e+00 100       5.61e+03  1.34e+04 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (8.3e+10, 'cm^3/(mol*s)'),
        n = 0.899,
        Ea = (-363, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (1.24e+31, 'cm^6/(mol^2*s)'),
        n = -4.718,
        Ea = (1871, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 1,
    T3 = (100, 'K'),
    T1 = (5613, 'K'),
    T2 = (13387, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='C=C'): 2.5,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[H][H]'): 2,
        Molecule(SMILES='C#C'): 2.5,
    },
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h3-n <=> c4h3-i',
 "chemkinKinetics": """
c4h3-n=c4h3-i                                       4.100e+43 -9.490    53.000   
""",
 "rmgPyKinetics": Arrhenius(A=(4.1e+43, 's^-1'), n=-9.49, Ea=(53000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h3-n + h <=> c4h3-i + h',
 "chemkinKinetics": """
c4h3-n+h=c4h3-i+h                                   2.500e+20 -1.670    10.800   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+20, 'cm^3/(mol*s)'),
    n = -1.67,
    Ea = (10800, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h3-n + h <=> c2h2 + h2cc',
 "chemkinKinetics": """
c4h3-n+h=c2h2+h2cc                                  6.300e+25 -3.340    10.014   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.3e+25, 'cm^3/(mol*s)'),
    n = -3.34,
    Ea = (10014, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h3-n + h <=> c4h4',
 "chemkinKinetics": """
c4h3-n+h=c4h4                                       2.000e+47 -10.260   13.070   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2e+47, 'cm^3/(mol*s)'),
    n = -10.26,
    Ea = (13070, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h3-n + h <=> c4h2 + h2',
 "chemkinKinetics": """
c4h3-n+h=c4h2+h2                                    3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h3-n + oh <=> c4h2 + h2o',
 "chemkinKinetics": """
c4h3-n+oh=c4h2+h2o                                  2.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c2h2 + c2h <=> c4h3-i',
 "chemkinKinetics": """
c2h2+c2h(+M)=c4h3-i(+M)                             8.300e+10 0.899     -0.363   
co2/2.00/ ch4/2.00/ c2h2/2.50/ co/1.50/ c2h4/2.50/ c2h6/3.00/ h2o/6.00/ h2/2.00/ 
    LOW/ 1.240e+31 -4.718    1.871    /
    TROE/ 1.000e+00 100       5.61e+03  1.34e+04 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (8.3e+10, 'cm^3/(mol*s)'),
        n = 0.899,
        Ea = (-363, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (1.24e+31, 'cm^6/(mol^2*s)'),
        n = -4.718,
        Ea = (1871, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 1,
    T3 = (100, 'K'),
    T1 = (5613, 'K'),
    T2 = (13387, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='C=C'): 2.5,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[H][H]'): 2,
        Molecule(SMILES='C#C'): 2.5,
    },
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h3-i + h <=> c2h2 + h2cc',
 "chemkinKinetics": """
c4h3-i+h=c2h2+h2cc                                  2.800e+23 -2.550    10.780   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.8e+23, 'cm^3/(mol*s)'),
    n = -2.55,
    Ea = (10780, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h3-i + h <=> c4h4',
 "chemkinKinetics": """
c4h3-i+h=c4h4                                       3.400e+43 -9.010    12.120   
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.4e+43, 'cm^3/(mol*s)'),
    n = -9.01,
    Ea = (12120, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h3-i + h <=> c4h2 + h2',
 "chemkinKinetics": """
c4h3-i+h=c4h2+h2                                    6.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h3-i + oh <=> c4h2 + h2o',
 "chemkinKinetics": """
c4h3-i+oh=c4h2+h2o                                  4.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h3-i + o2 <=> hcco + ch2co',
 "chemkinKinetics": """
c4h3-i+o2=hcco+ch2co                                7.860e+16 -1.800    0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.86e+16, 'cm^3/(mol*s)'), n=-1.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h3-i + ch2 <=> c3h4-a + c2h',
 "chemkinKinetics": """
c4h3-i+ch2=c3h4-a+c2h                               2.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h2 + c2h <=> c4h2 + h',
 "chemkinKinetics": """
c2h2+c2h=c4h2+h                                     9.600e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h2 + h <=> c4h3-n',
 "chemkinKinetics": """
c4h2+h=c4h3-n                                       1.100e+42 -8.720    15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.1e+42, 'cm^3/(mol*s)'),
    n = -8.72,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h2 + h <=> c4h3-i',
 "chemkinKinetics": """
c4h2+h=c4h3-i                                       1.100e+30 -4.920    10.800   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.1e+30, 'cm^3/(mol*s)'),
    n = -4.92,
    Ea = (10800, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h2 + oh <=> h2c4o + h',
 "chemkinKinetics": """
c4h2+oh=h2c4o+h                                     6.600e+12 0.000     -0.410   
""",
 "rmgPyKinetics": Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(-410, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'h2c4o + h <=> c2h2 + hcco',
 "chemkinKinetics": """
h2c4o+h=c2h2+hcco                                   5.000e+13 0.000     3.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'h2c4o + oh <=> ch2co + hcco',
 "chemkinKinetics": """
h2c4o+oh=ch2co+hcco                                 1.000e+07 2.000     2.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'h2cc + c2h2 <=> c4h4',
 "chemkinKinetics": """
h2cc+c2h2(+M)=c4h4(+M)                              3.500e+05 2.055     -2.400   
co2/2.00/ ch4/2.00/ c2h2/3.00/ co/1.50/ c2h4/3.00/ c2h6/3.00/ h2o/6.00/ h2/2.00/ 
    LOW/ 1.400e+60 -12.599   7.417    /
    TROE/ 9.800e-01 56        580       4.16e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(
        A = (350000, 'cm^3/(mol*s)'),
        n = 2.055,
        Ea = (-2400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    arrheniusLow = Arrhenius(
        A = (1.4e+60, 'cm^6/(mol^2*s)'),
        n = -12.599,
        Ea = (7417, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.98,
    T3 = (56, 'K'),
    T1 = (580, 'K'),
    T2 = (4164, 'K'),
    efficiencies = {
        Molecule(SMILES='[C]=O'): 1.5,
        Molecule(SMILES='CC'): 3,
        Molecule(SMILES='O'): 6,
        Molecule(SMILES='C=C'): 3,
        Molecule(SMILES='O=C=O'): 2,
        Molecule(SMILES='C'): 2,
        Molecule(SMILES='[H][H]'): 2,
        Molecule(SMILES='C#C'): 3,
    },
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'h2cc + c2h4 <=> c4h6',
 "chemkinKinetics": """
h2cc+c2h4=c4h6                                      1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-2 + oh => ch2o + c3h5-a + h2o',
 "chemkinKinetics": """
c4h8o1-2+oh=>ch2o+c3h5-a+h2o                        5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-2 + h => ch2o + c3h5-a + h2',
 "chemkinKinetics": """
c4h8o1-2+h=>ch2o+c3h5-a+h2                          5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-2 + o => ch2o + c3h5-a + oh',
 "chemkinKinetics": """
c4h8o1-2+o=>ch2o+c3h5-a+oh                          5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-2 + ho2 => ch2o + c3h5-a + h2o2',
 "chemkinKinetics": """
c4h8o1-2+ho2=>ch2o+c3h5-a+h2o2                      1.000e+13 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-2 + ch3o2 => ch2o + c3h5-a + ch3o2h',
 "chemkinKinetics": """
c4h8o1-2+ch3o2=>ch2o+c3h5-a+ch3o2h                  1.000e+13 0.000     19.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-2 + ch3 => ch2o + c3h5-a + ch4',
 "chemkinKinetics": """
c4h8o1-2+ch3=>ch2o+c3h5-a+ch4                       2.000e+11 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-3 + oh => ch2o + c3h5-a + h2o',
 "chemkinKinetics": """
c4h8o1-3+oh=>ch2o+c3h5-a+h2o                        5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-3 + h => ch2o + c3h5-a + h2',
 "chemkinKinetics": """
c4h8o1-3+h=>ch2o+c3h5-a+h2                          5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-3 + o => ch2o + c3h5-a + oh',
 "chemkinKinetics": """
c4h8o1-3+o=>ch2o+c3h5-a+oh                          5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-3 + ho2 => ch2o + c3h5-a + h2o2',
 "chemkinKinetics": """
c4h8o1-3+ho2=>ch2o+c3h5-a+h2o2                      1.000e+13 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-3 + ch3o2 => ch2o + c3h5-a + ch3o2h',
 "chemkinKinetics": """
c4h8o1-3+ch3o2=>ch2o+c3h5-a+ch3o2h                  1.000e+13 0.000     19.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-3 + ch3 => ch2o + c3h5-a + ch4',
 "chemkinKinetics": """
c4h8o1-3+ch3=>ch2o+c3h5-a+ch4                       2.000e+11 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-4 + oh => ch2o + c3h5-a + h2o',
 "chemkinKinetics": """
c4h8o1-4+oh=>ch2o+c3h5-a+h2o                        5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-4 + h => ch2o + c3h5-a + h2',
 "chemkinKinetics": """
c4h8o1-4+h=>ch2o+c3h5-a+h2                          5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-4 + o => ch2o + c3h5-a + oh',
 "chemkinKinetics": """
c4h8o1-4+o=>ch2o+c3h5-a+oh                          5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-4 + ho2 => ch2o + c3h5-a + h2o2',
 "chemkinKinetics": """
c4h8o1-4+ho2=>ch2o+c3h5-a+h2o2                      1.000e+13 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-4 + ch3o2 => ch2o + c3h5-a + ch3o2h',
 "chemkinKinetics": """
c4h8o1-4+ch3o2=>ch2o+c3h5-a+ch3o2h                  1.000e+13 0.000     19.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o1-4 + ch3 => ch2o + c3h5-a + ch4',
 "chemkinKinetics": """
c4h8o1-4+ch3=>ch2o+c3h5-a+ch4                       2.000e+11 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o2-3 + oh => ch2o + c3h5-a + h2o',
 "chemkinKinetics": """
c4h8o2-3+oh=>ch2o+c3h5-a+h2o                        5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o2-3 + h => ch2o + c3h5-a + h2',
 "chemkinKinetics": """
c4h8o2-3+h=>ch2o+c3h5-a+h2                          5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o2-3 + o => ch2o + c3h5-a + oh',
 "chemkinKinetics": """
c4h8o2-3+o=>ch2o+c3h5-a+oh                          5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o2-3 + ho2 => ch2o + c3h5-a + h2o2',
 "chemkinKinetics": """
c4h8o2-3+ho2=>ch2o+c3h5-a+h2o2                      1.000e+13 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o2-3 + ch3o2 => ch2o + c3h5-a + ch3o2h',
 "chemkinKinetics": """
c4h8o2-3+ch3o2=>ch2o+c3h5-a+ch3o2h                  1.000e+13 0.000     19.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h8o2-3 + ch3 => ch2o + c3h5-a + ch4',
 "chemkinKinetics": """
c4h8o2-3+ch3=>ch2o+c3h5-a+ch4                       2.000e+11 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'pc4h9o2 <=> pc4h9 + o2',
 "chemkinKinetics": """
pc4h9o2=pc4h9+o2                                    2.849e+20 -1.642    35.930   
""",
 "rmgPyKinetics": Arrhenius(A=(2.849e+20, 's^-1'), n=-1.642, Ea=(35930, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9o2 <=> sc4h9 + o2',
 "chemkinKinetics": """
sc4h9o2=sc4h9+o2                                    4.329e+22 -2.216    38.160   
""",
 "rmgPyKinetics": Arrhenius(A=(4.329e+22, 's^-1'), n=-2.216, Ea=(38160, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9o2 + ch2o <=> sc4h9o2h + hco',
 "chemkinKinetics": """
sc4h9o2+ch2o=sc4h9o2h+hco                           5.600e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + ch3cho <=> sc4h9o2h + ch3co',
 "chemkinKinetics": """
sc4h9o2+ch3cho=sc4h9o2h+ch3co                       2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + ho2 <=> sc4h9o2h + o2',
 "chemkinKinetics": """
sc4h9o2+ho2=sc4h9o2h+o2                             1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + pc4h9 <=> ic3h7o + pc4h9o',
 "chemkinKinetics": """
ic3h7o2+pc4h9=ic3h7o+pc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + sc4h9 <=> ic3h7o + sc4h9o',
 "chemkinKinetics": """
ic3h7o2+sc4h9=ic3h7o+sc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + pc4h9 <=> nc3h7o + pc4h9o',
 "chemkinKinetics": """
nc3h7o2+pc4h9=nc3h7o+pc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + sc4h9 <=> nc3h7o + sc4h9o',
 "chemkinKinetics": """
nc3h7o2+sc4h9=nc3h7o+sc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + sc4h9o2 => o2 + sc4h9o + sc4h9o',
 "chemkinKinetics": """
sc4h9o2+sc4h9o2=>o2+sc4h9o+sc4h9o                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h9o2 + nc3h7o2 => sc4h9o + nc3h7o + o2',
 "chemkinKinetics": """
sc4h9o2+nc3h7o2=>sc4h9o+nc3h7o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h9o2 + ic3h7o2 => sc4h9o + ic3h7o + o2',
 "chemkinKinetics": """
sc4h9o2+ic3h7o2=>sc4h9o+ic3h7o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h9o2 + c2h5o2 => sc4h9o + c2h5o + o2',
 "chemkinKinetics": """
sc4h9o2+c2h5o2=>sc4h9o+c2h5o+o2                     1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h9o2 + ch3o2 => sc4h9o + ch3o + o2',
 "chemkinKinetics": """
sc4h9o2+ch3o2=>sc4h9o+ch3o+o2                       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h9o2 + ch3co3 => sc4h9o + ch3co2 + o2',
 "chemkinKinetics": """
sc4h9o2+ch3co3=>sc4h9o+ch3co2+o2                    1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'h2 + pc4h9o2 <=> h + pc4h9o2h',
 "chemkinKinetics": """
h2+pc4h9o2=h+pc4h9o2h                               3.010e+13 0.000     26.030   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h2 + sc4h9o2 <=> h + sc4h9o2h',
 "chemkinKinetics": """
h2+sc4h9o2=h+sc4h9o2h                               3.010e+13 0.000     26.030   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h6 + pc4h9o2 <=> c2h5 + pc4h9o2h',
 "chemkinKinetics": """
c2h6+pc4h9o2=c2h5+pc4h9o2h                          1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h6 + sc4h9o2 <=> c2h5 + sc4h9o2h',
 "chemkinKinetics": """
c2h6+sc4h9o2=c2h5+sc4h9o2h                          1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + c2h5cho <=> pc4h9o2h + c2h5co',
 "chemkinKinetics": """
pc4h9o2+c2h5cho=pc4h9o2h+c2h5co                     2.000e+11 0.000     9.500    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + c2h5cho <=> sc4h9o2h + c2h5co',
 "chemkinKinetics": """
sc4h9o2+c2h5cho=sc4h9o2h+c2h5co                     2.000e+11 0.000     9.500    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + ch3 <=> sc4h9o + ch3o',
 "chemkinKinetics": """
sc4h9o2+ch3=sc4h9o+ch3o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + c2h5 <=> sc4h9o + c2h5o',
 "chemkinKinetics": """
sc4h9o2+c2h5=sc4h9o+c2h5o                           7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + ic3h7 <=> sc4h9o + ic3h7o',
 "chemkinKinetics": """
sc4h9o2+ic3h7=sc4h9o+ic3h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + nc3h7 <=> sc4h9o + nc3h7o',
 "chemkinKinetics": """
sc4h9o2+nc3h7=sc4h9o+nc3h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + pc4h9 <=> sc4h9o + pc4h9o',
 "chemkinKinetics": """
sc4h9o2+pc4h9=sc4h9o+pc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + sc4h9 <=> sc4h9o + sc4h9o',
 "chemkinKinetics": """
sc4h9o2+sc4h9=sc4h9o+sc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + c3h5-a <=> sc4h9o + c3h5o',
 "chemkinKinetics": """
sc4h9o2+c3h5-a=sc4h9o+c3h5o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + ch2o <=> pc4h9o2h + hco',
 "chemkinKinetics": """
pc4h9o2+ch2o=pc4h9o2h+hco                           5.600e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + ch3cho <=> pc4h9o2h + ch3co',
 "chemkinKinetics": """
pc4h9o2+ch3cho=pc4h9o2h+ch3co                       2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + ho2 <=> pc4h9o2h + o2',
 "chemkinKinetics": """
pc4h9o2+ho2=pc4h9o2h+o2                             1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + pc4h9o2 <=> c3h5-a + pc4h9o2h',
 "chemkinKinetics": """
c3h6+pc4h9o2=c3h5-a+pc4h9o2h                        3.240e+11 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h6 + sc4h9o2 <=> c3h5-a + sc4h9o2h',
 "chemkinKinetics": """
c3h6+sc4h9o2=c3h5-a+sc4h9o2h                        3.240e+11 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + pc4h9o2 <=> c2h3 + pc4h9o2h',
 "chemkinKinetics": """
c2h4+pc4h9o2=c2h3+pc4h9o2h                          1.130e+13 0.000     30.430   
""",
 "rmgPyKinetics": Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h4 + sc4h9o2 <=> c2h3 + sc4h9o2h',
 "chemkinKinetics": """
c2h4+sc4h9o2=c2h3+sc4h9o2h                          1.130e+13 0.000     30.430   
""",
 "rmgPyKinetics": Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + pc4h9o2 <=> ch2oh + pc4h9o2h',
 "chemkinKinetics": """
ch3oh+pc4h9o2=ch2oh+pc4h9o2h                        6.300e+12 0.000     19.360   
""",
 "rmgPyKinetics": Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3oh + sc4h9o2 <=> ch2oh + sc4h9o2h',
 "chemkinKinetics": """
ch3oh+sc4h9o2=ch2oh+sc4h9o2h                        6.300e+12 0.000     19.360   
""",
 "rmgPyKinetics": Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3cho + pc4h9o2 <=> c2h3co + pc4h9o2h',
 "chemkinKinetics": """
c2h3cho+pc4h9o2=c2h3co+pc4h9o2h                     2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3cho + sc4h9o2 <=> c2h3co + sc4h9o2h',
 "chemkinKinetics": """
c2h3cho+sc4h9o2=c2h3co+sc4h9o2h                     2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch4 + pc4h9o2 <=> ch3 + pc4h9o2h',
 "chemkinKinetics": """
ch4+pc4h9o2=ch3+pc4h9o2h                            1.120e+13 0.000     24.640   
""",
 "rmgPyKinetics": Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch4 + sc4h9o2 <=> ch3 + sc4h9o2h',
 "chemkinKinetics": """
ch4+sc4h9o2=ch3+sc4h9o2h                            1.120e+13 0.000     24.640   
""",
 "rmgPyKinetics": Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h71-3 + pc4h9o2 <=> c4h7o + pc4h9o',
 "chemkinKinetics": """
c4h71-3+pc4h9o2=c4h7o+pc4h9o                        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h71-3 + sc4h9o2 <=> c4h7o + sc4h9o',
 "chemkinKinetics": """
c4h71-3+sc4h9o2=c4h7o+sc4h9o                        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'h2o2 + pc4h9o2 <=> ho2 + pc4h9o2h',
 "chemkinKinetics": """
h2o2+pc4h9o2=ho2+pc4h9o2h                           2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h2o2 + sc4h9o2 <=> ho2 + sc4h9o2h',
 "chemkinKinetics": """
h2o2+sc4h9o2=ho2+sc4h9o2h                           2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + pc4h9o2 => o2 + pc4h9o + pc4h9o',
 "chemkinKinetics": """
pc4h9o2+pc4h9o2=>o2+pc4h9o+pc4h9o                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'pc4h9o2 + sc4h9o2 => pc4h9o + sc4h9o + o2',
 "chemkinKinetics": """
pc4h9o2+sc4h9o2=>pc4h9o+sc4h9o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'pc4h9o2 + nc3h7o2 => pc4h9o + nc3h7o + o2',
 "chemkinKinetics": """
pc4h9o2+nc3h7o2=>pc4h9o+nc3h7o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'pc4h9o2 + ic3h7o2 => pc4h9o + ic3h7o + o2',
 "chemkinKinetics": """
pc4h9o2+ic3h7o2=>pc4h9o+ic3h7o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'pc4h9o2 + c2h5o2 => pc4h9o + c2h5o + o2',
 "chemkinKinetics": """
pc4h9o2+c2h5o2=>pc4h9o+c2h5o+o2                     1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'pc4h9o2 + ch3o2 => pc4h9o + ch3o + o2',
 "chemkinKinetics": """
pc4h9o2+ch3o2=>pc4h9o+ch3o+o2                       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'pc4h9o2 + ch3co3 => pc4h9o + ch3co2 + o2',
 "chemkinKinetics": """
pc4h9o2+ch3co3=>pc4h9o+ch3co2+o2                    1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'pc4h9o2 + ch3 <=> pc4h9o + ch3o',
 "chemkinKinetics": """
pc4h9o2+ch3=pc4h9o+ch3o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + c2h5 <=> pc4h9o + c2h5o',
 "chemkinKinetics": """
pc4h9o2+c2h5=pc4h9o+c2h5o                           7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + ic3h7 <=> pc4h9o + ic3h7o',
 "chemkinKinetics": """
pc4h9o2+ic3h7=pc4h9o+ic3h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + nc3h7 <=> pc4h9o + nc3h7o',
 "chemkinKinetics": """
pc4h9o2+nc3h7=pc4h9o+nc3h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + pc4h9 <=> pc4h9o + pc4h9o',
 "chemkinKinetics": """
pc4h9o2+pc4h9=pc4h9o+pc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + sc4h9 <=> pc4h9o + sc4h9o',
 "chemkinKinetics": """
pc4h9o2+sc4h9=pc4h9o+sc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + c3h5-a <=> pc4h9o + c3h5o',
 "chemkinKinetics": """
pc4h9o2+c3h5-a=pc4h9o+c3h5o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'pc4h9 + ho2 <=> pc4h9o + oh',
 "chemkinKinetics": """
pc4h9+ho2=pc4h9o+oh                                 7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h9 + ho2 <=> sc4h9o + oh',
 "chemkinKinetics": """
sc4h9+ho2=sc4h9o+oh                                 7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + pc4h9 <=> ch3o + pc4h9o',
 "chemkinKinetics": """
ch3o2+pc4h9=ch3o+pc4h9o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + sc4h9 <=> ch3o + sc4h9o',
 "chemkinKinetics": """
ch3o2+sc4h9=ch3o+sc4h9o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2h <=> pc4h9o + oh',
 "chemkinKinetics": """
pc4h9o2h=pc4h9o+oh                                  1.500e+16 0.000     42.500   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9o + oh <=> sc4h9o2h',
 "chemkinKinetics": """
sc4h9o+oh=sc4h9o2h                                  1.000e+15 -0.800    0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+15, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'nc3h7 + ch2o <=> pc4h9o',
 "chemkinKinetics": """
nc3h7+ch2o=pc4h9o                                   5.000e+10 0.000     3.457    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(3457, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3 + c2h5cho <=> sc4h9o',
 "chemkinKinetics": """
ch3+c2h5cho=sc4h9o                                  5.000e+10 0.000     9.043    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(9043, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h5 + ch3cho <=> sc4h9o',
 "chemkinKinetics": """
c2h5+ch3cho=sc4h9o                                  3.330e+10 0.000     6.397    
""",
 "rmgPyKinetics": Arrhenius(A=(3.33e+10, 'cm^3/(mol*s)'), n=0, Ea=(6397, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'pc4h9o2 <=> c4h8ooh1-2',
 "chemkinKinetics": """
pc4h9o2=c4h8ooh1-2                                  2.000e+11 0.000     31.850   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(31850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'pc4h9o2 <=> c4h8ooh1-3',
 "chemkinKinetics": """
pc4h9o2=c4h8ooh1-3                                  2.500e+10 0.000     20.850   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(20850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'pc4h9o2 <=> c4h8ooh1-4',
 "chemkinKinetics": """
pc4h9o2=c4h8ooh1-4                                  4.688e+09 0.000     22.350   
""",
 "rmgPyKinetics": Arrhenius(A=(4.688e+09, 's^-1'), n=0, Ea=(22350, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h9o2 <=> c4h8ooh2-1',
 "chemkinKinetics": """
sc4h9o2=c4h8ooh2-1                                  3.000e+11 0.000     34.500   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(34500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h9o2 <=> c4h8ooh2-3',
 "chemkinKinetics": """
sc4h9o2=c4h8ooh2-3                                  2.000e+11 0.000     31.850   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(31850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h9o2 <=> c4h8ooh2-4',
 "chemkinKinetics": """
sc4h9o2=c4h8ooh2-4                                  3.750e+10 0.000     24.400   
""",
 "rmgPyKinetics": Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'pc4h9o2 <=> c4h8-1 + ho2',
 "chemkinKinetics": """
pc4h9o2=c4h8-1+ho2                                  4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'sc4h9o2 <=> c4h8-1 + ho2',
 "chemkinKinetics": """
sc4h9o2=c4h8-1+ho2                                  5.980e+42 -9.430    41.530   
""",
 "rmgPyKinetics": Arrhenius(A=(5.98e+42, 's^-1'), n=-9.43, Ea=(41530, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'sc4h9o2 <=> c4h8-2 + ho2',
 "chemkinKinetics": """
sc4h9o2=c4h8-2+ho2                                  4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'c4h8-1 + ho2 <=> c4h8ooh1-2',
 "chemkinKinetics": """
c4h8-1+ho2=c4h8ooh1-2                               1.000e+11 0.000     11.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h8-1 + ho2 <=> c4h8ooh2-1',
 "chemkinKinetics": """
c4h8-1+ho2=c4h8ooh2-1                               1.000e+11 0.000     11.750   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11750, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h8-2 + ho2 <=> c4h8ooh2-3',
 "chemkinKinetics": """
c4h8-2+ho2=c4h8ooh2-3                               1.000e+11 0.000     11.750   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11750, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h8ooh1-2 <=> c4h8o1-2 + oh',
 "chemkinKinetics": """
c4h8ooh1-2=c4h8o1-2+oh                              1.380e+12 0.000     15.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.38e+12, 's^-1'), n=0, Ea=(15900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h8ooh1-3 <=> c4h8o1-3 + oh',
 "chemkinKinetics": """
c4h8ooh1-3=c4h8o1-3+oh                              2.040e+11 0.000     19.500   
""",
 "rmgPyKinetics": Arrhenius(A=(2.04e+11, 's^-1'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h8ooh1-4 <=> c4h8o1-4 + oh',
 "chemkinKinetics": """
c4h8ooh1-4=c4h8o1-4+oh                              5.130e+10 0.000     14.800   
""",
 "rmgPyKinetics": Arrhenius(A=(5.13e+10, 's^-1'), n=0, Ea=(14800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h8ooh2-1 <=> c4h8o1-2 + oh',
 "chemkinKinetics": """
c4h8ooh2-1=c4h8o1-2+oh                              3.980e+12 0.000     17.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3.98e+12, 's^-1'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h8ooh2-3 <=> c4h8o2-3 + oh',
 "chemkinKinetics": """
c4h8ooh2-3=c4h8o2-3+oh                              1.380e+12 0.000     15.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.38e+12, 's^-1'), n=0, Ea=(15900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h8ooh2-4 <=> c4h8o1-3 + oh',
 "chemkinKinetics": """
c4h8ooh2-4=c4h8o1-3+oh                              4.470e+11 0.000     21.900   
""",
 "rmgPyKinetics": Arrhenius(A=(4.47e+11, 's^-1'), n=0, Ea=(21900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h8ooh1-1 <=> nc3h7cho + oh',
 "chemkinKinetics": """
c4h8ooh1-1=nc3h7cho+oh                              9.000e+14 0.000     1.500    
""",
 "rmgPyKinetics": Arrhenius(A=(9e+14, 's^-1'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h8ooh2-2 <=> c2h5coch3 + oh',
 "chemkinKinetics": """
c4h8ooh2-2=c2h5coch3+oh                             9.000e+14 0.000     1.500    
""",
 "rmgPyKinetics": Arrhenius(A=(9e+14, 's^-1'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h8ooh1-3 => oh + ch2o + c3h6',
 "chemkinKinetics": """
c4h8ooh1-3=>oh+ch2o+c3h6                            6.635e+13 -0.160    29.900   
""",
 "rmgPyKinetics": Arrhenius(A=(6.635e+13, 's^-1'), n=-0.16, Ea=(29900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'c4h8ooh2-4 => oh + ch3cho + c2h4',
 "chemkinKinetics": """
c4h8ooh2-4=>oh+ch3cho+c2h4                          1.945e+18 -1.630    26.790   
""",
 "rmgPyKinetics": Arrhenius(A=(1.945e+18, 's^-1'), n=-1.63, Ea=(26790, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'c4h8ooh1-2 + o2 <=> c4h8ooh1-2o2',
 "chemkinKinetics": """
c4h8ooh1-2+o2=c4h8ooh1-2o2                          7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8ooh1-3 + o2 <=> c4h8ooh1-3o2',
 "chemkinKinetics": """
c4h8ooh1-3+o2=c4h8ooh1-3o2                          7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8ooh1-4 + o2 <=> c4h8ooh1-4o2',
 "chemkinKinetics": """
c4h8ooh1-4+o2=c4h8ooh1-4o2                          4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8ooh2-1 + o2 <=> c4h8ooh2-1o2',
 "chemkinKinetics": """
c4h8ooh2-1+o2=c4h8ooh2-1o2                          4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8ooh2-3 + o2 <=> c4h8ooh2-3o2',
 "chemkinKinetics": """
c4h8ooh2-3+o2=c4h8ooh2-3o2                          7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8ooh2-4 + o2 <=> c4h8ooh2-4o2',
 "chemkinKinetics": """
c4h8ooh2-4+o2=c4h8ooh2-4o2                          4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8ooh1-2o2 <=> nc4ket12 + oh',
 "chemkinKinetics": """
c4h8ooh1-2o2=nc4ket12+oh                            2.000e+11 0.000     31.500   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(31500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h8ooh1-3o2 <=> nc4ket13 + oh',
 "chemkinKinetics": """
c4h8ooh1-3o2=nc4ket13+oh                            2.500e+10 0.000     21.400   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h8ooh1-4o2 <=> nc4ket14 + oh',
 "chemkinKinetics": """
c4h8ooh1-4o2=nc4ket14+oh                            3.125e+09 0.000     19.350   
""",
 "rmgPyKinetics": Arrhenius(A=(3.125e+09, 's^-1'), n=0, Ea=(19350, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h8ooh2-1o2 <=> nc4ket21 + oh',
 "chemkinKinetics": """
c4h8ooh2-1o2=nc4ket21+oh                            1.000e+11 0.000     28.850   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(28850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h8ooh2-3o2 <=> nc4ket23 + oh',
 "chemkinKinetics": """
c4h8ooh2-3o2=nc4ket23+oh                            1.000e+11 0.000     28.850   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(28850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h8ooh2-4o2 <=> nc4ket24 + oh',
 "chemkinKinetics": """
c4h8ooh2-4o2=nc4ket24+oh                            1.250e+10 0.000     17.850   
""",
 "rmgPyKinetics": Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(17850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'nc4ket12 => c2h5cho + hco + oh',
 "chemkinKinetics": """
nc4ket12=>c2h5cho+hco+oh                            1.050e+16 0.000     41.600   
""",
 "rmgPyKinetics": Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products1',  ],
},

{
 "reaction": 'nc4ket13 => ch3cho + ch2cho + oh',
 "chemkinKinetics": """
nc4ket13=>ch3cho+ch2cho+oh                          1.050e+16 0.000     41.600   
""",
 "rmgPyKinetics": Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products1', 'Fake_3products1', 'Fake_3products1',  ],
},

{
 "reaction": 'nc4ket14 => ch2ch2cho + ch2o + oh',
 "chemkinKinetics": """
nc4ket14=>ch2ch2cho+ch2o+oh                         1.500e+16 0.000     42.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products1', 'Fake_3products1', 'Fake_3products1',  ],
},

{
 "reaction": 'nc4ket21 => ch2o + c2h5co + oh',
 "chemkinKinetics": """
nc4ket21=>ch2o+c2h5co+oh                            1.500e+16 0.000     42.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products1',  ],
},

{
 "reaction": 'nc4ket23 => ch3cho + ch3co + oh',
 "chemkinKinetics": """
nc4ket23=>ch3cho+ch3co+oh                           1.050e+16 0.000     41.600   
""",
 "rmgPyKinetics": Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products1',  ],
},

{
 "reaction": 'nc4ket24 => ch2o + ch3coch2 + oh',
 "chemkinKinetics": """
nc4ket24=>ch2o+ch3coch2+oh                          1.500e+16 0.000     42.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products1', 'Fake_3products1', 'Fake_3products1',  ],
},

{
 "reaction": 'c2h5coch3 + oh <=> ch2ch2coch3 + h2o',
 "chemkinKinetics": """
c2h5coch3+oh=ch2ch2coch3+h2o                        7.550e+09 0.970     1.586    
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.55e+09, 'cm^3/(mol*s)'),
    n = 0.97,
    Ea = (1586, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + oh <=> ch3chcoch3 + h2o',
 "chemkinKinetics": """
c2h5coch3+oh=ch3chcoch3+h2o                         8.450e+11 0.000     -0.228   
""",
 "rmgPyKinetics": Arrhenius(A=(8.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(-228, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + oh <=> c2h5coch2 + h2o',
 "chemkinKinetics": """
c2h5coch3+oh=c2h5coch2+h2o                          5.100e+11 0.000     1.192    
""",
 "rmgPyKinetics": Arrhenius(A=(5.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(1192, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + ho2 <=> ch2ch2coch3 + h2o2',
 "chemkinKinetics": """
c2h5coch3+ho2=ch2ch2coch3+h2o2                      2.380e+04 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + ho2 <=> ch3chcoch3 + h2o2',
 "chemkinKinetics": """
c2h5coch3+ho2=ch3chcoch3+h2o2                       2.000e+11 0.000     8.698    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(8698, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + ho2 <=> c2h5coch2 + h2o2',
 "chemkinKinetics": """
c2h5coch3+ho2=c2h5coch2+h2o2                        2.380e+04 2.550     14.690   
""",
 "rmgPyKinetics": Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(14690, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + o <=> ch2ch2coch3 + oh',
 "chemkinKinetics": """
c2h5coch3+o=ch2ch2coch3+oh                          2.250e+13 0.000     7.700    
""",
 "rmgPyKinetics": Arrhenius(A=(2.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + o <=> ch3chcoch3 + oh',
 "chemkinKinetics": """
c2h5coch3+o=ch3chcoch3+oh                           3.070e+13 0.000     3.400    
""",
 "rmgPyKinetics": Arrhenius(A=(3.07e+13, 'cm^3/(mol*s)'), n=0, Ea=(3400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + o <=> c2h5coch2 + oh',
 "chemkinKinetics": """
c2h5coch3+o=c2h5coch2+oh                            5.000e+12 0.000     5.962    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(5962, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + h <=> ch2ch2coch3 + h2',
 "chemkinKinetics": """
c2h5coch3+h=ch2ch2coch3+h2                          9.160e+06 2.000     7.700    
""",
 "rmgPyKinetics": Arrhenius(A=(9.16e+06, 'cm^3/(mol*s)'), n=2, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + h <=> ch3chcoch3 + h2',
 "chemkinKinetics": """
c2h5coch3+h=ch3chcoch3+h2                           4.460e+06 2.000     3.200    
""",
 "rmgPyKinetics": Arrhenius(A=(4.46e+06, 'cm^3/(mol*s)'), n=2, Ea=(3200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + h <=> c2h5coch2 + h2',
 "chemkinKinetics": """
c2h5coch3+h=c2h5coch2+h2                            9.300e+12 0.000     6.357    
""",
 "rmgPyKinetics": Arrhenius(A=(9.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(6357, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + o2 <=> ch2ch2coch3 + ho2',
 "chemkinKinetics": """
c2h5coch3+o2=ch2ch2coch3+ho2                        2.050e+13 0.000     51.310   
""",
 "rmgPyKinetics": Arrhenius(A=(2.05e+13, 'cm^3/(mol*s)'), n=0, Ea=(51310, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + o2 <=> ch3chcoch3 + ho2',
 "chemkinKinetics": """
c2h5coch3+o2=ch3chcoch3+ho2                         1.550e+13 0.000     41.970   
""",
 "rmgPyKinetics": Arrhenius(A=(1.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(41970, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + o2 <=> c2h5coch2 + ho2',
 "chemkinKinetics": """
c2h5coch3+o2=c2h5coch2+ho2                          2.050e+13 0.000     49.150   
""",
 "rmgPyKinetics": Arrhenius(A=(2.05e+13, 'cm^3/(mol*s)'), n=0, Ea=(49150, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + ch3 <=> ch2ch2coch3 + ch4',
 "chemkinKinetics": """
c2h5coch3+ch3=ch2ch2coch3+ch4                       3.190e+01 3.170     7.172    
""",
 "rmgPyKinetics": Arrhenius(A=(31.9, 'cm^3/(mol*s)'), n=3.17, Ea=(7172, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + ch3 <=> ch3chcoch3 + ch4',
 "chemkinKinetics": """
c2h5coch3+ch3=ch3chcoch3+ch4                        1.740e+00 3.460     3.680    
""",
 "rmgPyKinetics": Arrhenius(A=(1.74, 'cm^3/(mol*s)'), n=3.46, Ea=(3680, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + ch3 <=> c2h5coch2 + ch4',
 "chemkinKinetics": """
c2h5coch3+ch3=c2h5coch2+ch4                         1.620e+11 0.000     9.630    
""",
 "rmgPyKinetics": Arrhenius(A=(1.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(9630, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + ch3o <=> ch2ch2coch3 + ch3oh',
 "chemkinKinetics": """
c2h5coch3+ch3o=ch2ch2coch3+ch3oh                    2.170e+11 0.000     6.460    
""",
 "rmgPyKinetics": Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + ch3o <=> ch3chcoch3 + ch3oh',
 "chemkinKinetics": """
c2h5coch3+ch3o=ch3chcoch3+ch3oh                     1.450e+11 0.000     2.771    
""",
 "rmgPyKinetics": Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(2771, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + ch3o <=> c2h5coch2 + ch3oh',
 "chemkinKinetics": """
c2h5coch3+ch3o=c2h5coch2+ch3oh                      2.170e+11 0.000     4.660    
""",
 "rmgPyKinetics": Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(4660, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + ch3o2 <=> ch2ch2coch3 + ch3o2h',
 "chemkinKinetics": """
c2h5coch3+ch3o2=ch2ch2coch3+ch3o2h                  3.010e+12 0.000     19.380   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(19380, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + ch3o2 <=> ch3chcoch3 + ch3o2h',
 "chemkinKinetics": """
c2h5coch3+ch3o2=ch3chcoch3+ch3o2h                   2.000e+12 0.000     15.250   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + ch3o2 <=> c2h5coch2 + ch3o2h',
 "chemkinKinetics": """
c2h5coch3+ch3o2=c2h5coch2+ch3o2h                    3.010e+12 0.000     17.580   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(17580, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + c2h3 <=> ch2ch2coch3 + c2h4',
 "chemkinKinetics": """
c2h5coch3+c2h3=ch2ch2coch3+c2h4                     5.000e+11 0.000     10.400   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + c2h3 <=> ch3chcoch3 + c2h4',
 "chemkinKinetics": """
c2h5coch3+c2h3=ch3chcoch3+c2h4                      3.000e+11 0.000     3.400    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(3400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + c2h3 <=> c2h5coch2 + c2h4',
 "chemkinKinetics": """
c2h5coch3+c2h3=c2h5coch2+c2h4                       6.150e+10 0.000     4.278    
""",
 "rmgPyKinetics": Arrhenius(A=(6.15e+10, 'cm^3/(mol*s)'), n=0, Ea=(4278, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + c2h5 <=> ch2ch2coch3 + c2h6',
 "chemkinKinetics": """
c2h5coch3+c2h5=ch2ch2coch3+c2h6                     5.000e+10 0.000     13.400   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + c2h5 <=> ch3chcoch3 + c2h6',
 "chemkinKinetics": """
c2h5coch3+c2h5=ch3chcoch3+c2h6                      3.000e+10 0.000     8.600    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(8600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h5coch3 + c2h5 <=> c2h5coch2 + c2h6',
 "chemkinKinetics": """
c2h5coch3+c2h5=c2h5coch2+c2h6                       5.000e+10 0.000     11.600   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(11600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch3chcoch3 + o2 <=> ch3choococh3',
 "chemkinKinetics": """
ch3chcoch3+o2=ch3choococh3                          1.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3choococh3 <=> ch2choohcoch3',
 "chemkinKinetics": """
ch3choococh3=ch2choohcoch3                          8.900e+12 0.000     29.700   
""",
 "rmgPyKinetics": Arrhenius(A=(8.9e+12, 's^-1'), n=0, Ea=(29700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c2h3coch3 + ho2 <=> ch2choohcoch3',
 "chemkinKinetics": """
c2h3coch3+ho2=ch2choohcoch3                         7.000e+10 0.000     7.800    
""",
 "rmgPyKinetics": Arrhenius(A=(7e+10, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2ch2cho <=> c2h4 + hco',
 "chemkinKinetics": """
ch2ch2cho=c2h4+hco                                  3.127e+13 -0.520    24.590   
""",
 "rmgPyKinetics": Arrhenius(A=(3.127e+13, 's^-1'), n=-0.52, Ea=(24590, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2ch2coch3 <=> c2h4 + ch3co',
 "chemkinKinetics": """
ch2ch2coch3=c2h4+ch3co                              1.000e+14 0.000     18.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h5coch2 <=> ch2co + c2h5',
 "chemkinKinetics": """
c2h5coch2=ch2co+c2h5                                1.000e+14 0.000     35.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(35000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h3coch3 + h <=> ch3chcoch3',
 "chemkinKinetics": """
c2h3coch3+h=ch3chcoch3                              5.000e+12 0.000     1.200    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3chco + ch3 <=> ch3chcoch3',
 "chemkinKinetics": """
ch3chco+ch3=ch3chcoch3                              1.230e+11 0.000     7.800    
""",
 "rmgPyKinetics": Arrhenius(A=(1.23e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'nc3h7cho + o2 <=> nc3h7co + ho2',
 "chemkinKinetics": """
nc3h7cho+o2=nc3h7co+ho2                             1.200e+05 2.500     37.560   
""",
 "rmgPyKinetics": Arrhenius(A=(120000, 'cm^3/(mol*s)'), n=2.5, Ea=(37560, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + oh <=> nc3h7co + h2o',
 "chemkinKinetics": """
nc3h7cho+oh=nc3h7co+h2o                             2.000e+06 1.800     -1.300   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+06, 'cm^3/(mol*s)'), n=1.8, Ea=(-1300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + h <=> nc3h7co + h2',
 "chemkinKinetics": """
nc3h7cho+h=nc3h7co+h2                               4.140e+09 1.120     2.320    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.14e+09, 'cm^3/(mol*s)'),
    n = 1.12,
    Ea = (2320, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + o <=> nc3h7co + oh',
 "chemkinKinetics": """
nc3h7cho+o=nc3h7co+oh                               5.940e+12 0.000     1.868    
""",
 "rmgPyKinetics": Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + ho2 <=> nc3h7co + h2o2',
 "chemkinKinetics": """
nc3h7cho+ho2=nc3h7co+h2o2                           4.090e+04 2.500     10.200   
""",
 "rmgPyKinetics": Arrhenius(A=(40900, 'cm^3/(mol*s)'), n=2.5, Ea=(10200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + ch3 <=> nc3h7co + ch4',
 "chemkinKinetics": """
nc3h7cho+ch3=nc3h7co+ch4                            2.890e-03 4.620     3.210    
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.00289, 'cm^3/(mol*s)'),
    n = 4.62,
    Ea = (3210, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + ch3o <=> nc3h7co + ch3oh',
 "chemkinKinetics": """
nc3h7cho+ch3o=nc3h7co+ch3oh                         1.000e+12 0.000     3.300    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + ch3o2 <=> nc3h7co + ch3o2h',
 "chemkinKinetics": """
nc3h7cho+ch3o2=nc3h7co+ch3o2h                       4.090e+04 2.500     10.200   
""",
 "rmgPyKinetics": Arrhenius(A=(40900, 'cm^3/(mol*s)'), n=2.5, Ea=(10200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + oh <=> c3h6cho-1 + h2o',
 "chemkinKinetics": """
nc3h7cho+oh=c3h6cho-1+h2o                           5.280e+09 0.970     1.586    
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.28e+09, 'cm^3/(mol*s)'),
    n = 0.97,
    Ea = (1586, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + oh <=> c3h6cho-2 + h2o',
 "chemkinKinetics": """
nc3h7cho+oh=c3h6cho-2+h2o                           4.680e+07 1.610     -0.035   
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.68e+07, 'cm^3/(mol*s)'),
    n = 1.61,
    Ea = (-35, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + oh <=> c3h6cho-3 + h2o',
 "chemkinKinetics": """
nc3h7cho+oh=c3h6cho-3+h2o                           5.520e+02 3.120     -1.176   
""",
 "rmgPyKinetics": Arrhenius(A=(552, 'cm^3/(mol*s)'), n=3.12, Ea=(-1176, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + ho2 <=> c3h6cho-1 + h2o2',
 "chemkinKinetics": """
nc3h7cho+ho2=c3h6cho-1+h2o2                         2.379e+04 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(23790, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + ho2 <=> c3h6cho-2 + h2o2',
 "chemkinKinetics": """
nc3h7cho+ho2=c3h6cho-2+h2o2                         9.640e+03 2.600     13.910   
""",
 "rmgPyKinetics": Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + ho2 <=> c3h6cho-3 + h2o2',
 "chemkinKinetics": """
nc3h7cho+ho2=c3h6cho-3+h2o2                         3.440e+12 0.050     17.880   
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.44e+12, 'cm^3/(mol*s)'),
    n = 0.05,
    Ea = (17880, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + ch3o2 <=> c3h6cho-1 + ch3o2h',
 "chemkinKinetics": """
nc3h7cho+ch3o2=c3h6cho-1+ch3o2h                     2.379e+04 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(23790, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + ch3o2 <=> c3h6cho-2 + ch3o2h',
 "chemkinKinetics": """
nc3h7cho+ch3o2=c3h6cho-2+ch3o2h                     9.640e+03 2.600     13.910   
""",
 "rmgPyKinetics": Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7cho + ch3o2 <=> c3h6cho-3 + ch3o2h',
 "chemkinKinetics": """
nc3h7cho+ch3o2=c3h6cho-3+ch3o2h                     3.440e+12 0.050     17.880   
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.44e+12, 'cm^3/(mol*s)'),
    n = 0.05,
    Ea = (17880, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7co <=> nc3h7 + co',
 "chemkinKinetics": """
nc3h7co=nc3h7+co                                    1.000e+11 0.000     9.600    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(9600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6cho-1 <=> c2h4 + ch2cho',
 "chemkinKinetics": """
c3h6cho-1=c2h4+ch2cho                               7.400e+11 0.000     21.970   
""",
 "rmgPyKinetics": Arrhenius(A=(7.4e+11, 's^-1'), n=0, Ea=(21970, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h5chco + h <=> c3h6cho-3',
 "chemkinKinetics": """
c2h5chco+h=c3h6cho-3                                5.000e+12 0.000     1.200    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h3cho + ch3 <=> c3h6cho-3',
 "chemkinKinetics": """
c2h3cho+ch3=c3h6cho-3                               1.230e+11 0.000     7.800    
""",
 "rmgPyKinetics": Arrhenius(A=(1.23e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'sc3h5cho + h <=> c3h6cho-2',
 "chemkinKinetics": """
sc3h5cho+h=c3h6cho-2                                5.000e+12 0.000     2.900    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(2900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h6 + hco <=> c3h6cho-2',
 "chemkinKinetics": """
c3h6+hco=c3h6cho-2                                  1.000e+11 0.000     6.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h5chco + oh <=> nc3h7 + co2',
 "chemkinKinetics": """
c2h5chco+oh=nc3h7+co2                               3.730e+12 0.000     -1.010   
""",
 "rmgPyKinetics": Arrhenius(A=(3.73e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h5chco + h <=> nc3h7 + co',
 "chemkinKinetics": """
c2h5chco+h=nc3h7+co                                 4.400e+12 0.000     1.459    
""",
 "rmgPyKinetics": Arrhenius(A=(4.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(1459, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h5chco + o <=> c3h6 + co2',
 "chemkinKinetics": """
c2h5chco+o=c3h6+co2                                 3.200e+12 0.000     -0.437   
""",
 "rmgPyKinetics": Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc3h5cho + oh <=> sc3h5co + h2o',
 "chemkinKinetics": """
sc3h5cho+oh=sc3h5co+h2o                             2.690e+10 0.760     -0.340   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.69e+10, 'cm^3/(mol*s)'),
    n = 0.76,
    Ea = (-340, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h5-s + co <=> sc3h5co',
 "chemkinKinetics": """
c3h5-s+co=sc3h5co                                   5.000e+12 0.000     8.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc3h5cho + ho2 <=> sc3h5co + h2o2',
 "chemkinKinetics": """
sc3h5cho+ho2=sc3h5co+h2o2                           1.000e+12 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc3h5cho + ch3 <=> sc3h5co + ch4',
 "chemkinKinetics": """
sc3h5cho+ch3=sc3h5co+ch4                            3.980e+12 0.000     8.700    
""",
 "rmgPyKinetics": Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(8700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc3h5cho + o <=> sc3h5co + oh',
 "chemkinKinetics": """
sc3h5cho+o=sc3h5co+oh                               7.180e+12 0.000     1.389    
""",
 "rmgPyKinetics": Arrhenius(A=(7.18e+12, 'cm^3/(mol*s)'), n=0, Ea=(1389, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc3h5cho + o2 <=> sc3h5co + ho2',
 "chemkinKinetics": """
sc3h5cho+o2=sc3h5co+ho2                             4.000e+13 0.000     37.600   
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(37600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc3h5cho + h <=> sc3h5co + h2',
 "chemkinKinetics": """
sc3h5cho+h=sc3h5co+h2                               2.600e+12 0.000     2.600    
""",
 "rmgPyKinetics": Arrhenius(A=(2.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3coch3 + oh <=> ch3cho + ch3co',
 "chemkinKinetics": """
c2h3coch3+oh=ch3cho+ch3co                           1.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3coch3 + oh => ch2co + c2h3 + h2o',
 "chemkinKinetics": """
c2h3coch3+oh=>ch2co+c2h3+h2o                        5.100e+11 0.000     1.192    
""",
 "rmgPyKinetics": Arrhenius(A=(5.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(1192, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3coch3 + ho2 => ch2cho + ch3co + oh',
 "chemkinKinetics": """
c2h3coch3+ho2=>ch2cho+ch3co+oh                      6.030e+09 0.000     7.949    
""",
 "rmgPyKinetics": Arrhenius(A=(6.03e+09, 'cm^3/(mol*s)'), n=0, Ea=(7949, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3coch3 + ho2 => ch2co + c2h3 + h2o2',
 "chemkinKinetics": """
c2h3coch3+ho2=>ch2co+c2h3+h2o2                      8.500e+12 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(8.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3coch3 + ch3o2 => ch2cho + ch3co + ch3o',
 "chemkinKinetics": """
c2h3coch3+ch3o2=>ch2cho+ch3co+ch3o                  3.970e+11 0.000     17.050   
""",
 "rmgPyKinetics": Arrhenius(A=(3.97e+11, 'cm^3/(mol*s)'), n=0, Ea=(17050, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3coch3 + ch3o2 => ch2co + c2h3 + ch3o2h',
 "chemkinKinetics": """
c2h3coch3+ch3o2=>ch2co+c2h3+ch3o2h                  3.010e+12 0.000     17.580   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(17580, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h10 <=> ch3 + ic3h7',
 "chemkinKinetics": """
ic4h10(+M)=ch3+ic3h7(+M)                            2.520e+31 -4.102    91.495   

    LOW/ 2.410e+19 0.000     52.576   /
    TROE/ 3.662e-01 815       60.8      1e+20    /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(2.5203e+31, 's^-1'), n=-4.102, Ea=(91495, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(A=(2.41e+19, 'cm^3/(mol*s)'), n=0, Ea=(52576, 'cal/mol'), T0=(1, 'K')),
    alpha = 0.3662,
    T3 = (815.3, 'K'),
    T1 = (60.786, 'K'),
    T2 = (1e+20, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h10 <=> tc4h9 + h',
 "chemkinKinetics": """
ic4h10=tc4h9+h                                      2.510e+98 -23.810   145.300  
""",
 "rmgPyKinetics": Arrhenius(A=(2.51e+98, 's^-1'), n=-23.81, Ea=(145300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h10 <=> ic4h9 + h',
 "chemkinKinetics": """
ic4h10=ic4h9+h                                      9.850e+95 -23.110   147.600  
""",
 "rmgPyKinetics": Arrhenius(A=(9.85e+95, 's^-1'), n=-23.11, Ea=(147600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h10 + h <=> tc4h9 + h2',
 "chemkinKinetics": """
ic4h10+h=tc4h9+h2                                   6.020e+05 2.400     2.583    
""",
 "rmgPyKinetics": Arrhenius(A=(602000, 'cm^3/(mol*s)'), n=2.4, Ea=(2583, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + h <=> ic4h9 + h2',
 "chemkinKinetics": """
ic4h10+h=ic4h9+h2                                   1.810e+06 2.540     6.756    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.81e+06, 'cm^3/(mol*s)'),
    n = 2.54,
    Ea = (6756, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ch3 <=> tc4h9 + ch4',
 "chemkinKinetics": """
ic4h10+ch3=tc4h9+ch4                                9.040e-01 3.460     4.598    
""",
 "rmgPyKinetics": Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.46, Ea=(4598, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ch3 <=> ic4h9 + ch4',
 "chemkinKinetics": """
ic4h10+ch3=ic4h9+ch4                                1.360e+00 3.650     7.154    
""",
 "rmgPyKinetics": Arrhenius(A=(1.36, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + oh <=> tc4h9 + h2o',
 "chemkinKinetics": """
ic4h10+oh=tc4h9+h2o                                 2.925e+04 2.531     -1.659   
""",
 "rmgPyKinetics": Arrhenius(
    A = (29250, 'cm^3/(mol*s)'),
    n = 2.531,
    Ea = (-1659, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + oh <=> ic4h9 + h2o',
 "chemkinKinetics": """
ic4h10+oh=ic4h9+h2o                                 6.654e+04 2.665     -0.169   
""",
 "rmgPyKinetics": Arrhenius(
    A = (66540, 'cm^3/(mol*s)'),
    n = 2.665,
    Ea = (-168.9, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + c2h5 <=> ic4h9 + c2h6',
 "chemkinKinetics": """
ic4h10+c2h5=ic4h9+c2h6                              1.510e+12 0.000     10.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1.51e+12, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + c2h5 <=> tc4h9 + c2h6',
 "chemkinKinetics": """
ic4h10+c2h5=tc4h9+c2h6                              1.000e+11 0.000     7.900    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ho2 <=> ic4h9 + h2o2',
 "chemkinKinetics": """
ic4h10+ho2=ic4h9+h2o2                               6.120e+01 3.590     17.160   
""",
 "rmgPyKinetics": Arrhenius(A=(61.2, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ho2 <=> tc4h9 + h2o2',
 "chemkinKinetics": """
ic4h10+ho2=tc4h9+h2o2                               4.332e+02 3.010     12.090   
""",
 "rmgPyKinetics": Arrhenius(A=(433.2, 'cm^3/(mol*s)'), n=3.01, Ea=(12090, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + o <=> tc4h9 + oh',
 "chemkinKinetics": """
ic4h10+o=tc4h9+oh                                   1.968e+05 2.402     1.150    
""",
 "rmgPyKinetics": Arrhenius(
    A = (196800, 'cm^3/(mol*s)'),
    n = 2.402,
    Ea = (1150, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + o <=> ic4h9 + oh',
 "chemkinKinetics": """
ic4h10+o=ic4h9+oh                                   4.046e+07 2.034     5.136    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.046e+07, 'cm^3/(mol*s)'),
    n = 2.034,
    Ea = (5136, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ch3o <=> ic4h9 + ch3oh',
 "chemkinKinetics": """
ic4h10+ch3o=ic4h9+ch3oh                             4.800e+11 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ch3o <=> tc4h9 + ch3oh',
 "chemkinKinetics": """
ic4h10+ch3o=tc4h9+ch3oh                             1.900e+10 0.000     2.800    
""",
 "rmgPyKinetics": Arrhenius(A=(1.9e+10, 'cm^3/(mol*s)'), n=0, Ea=(2800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + o2 <=> ic4h9 + ho2',
 "chemkinKinetics": """
ic4h10+o2=ic4h9+ho2                                 9.000e+13 0.000     52.290   
""",
 "rmgPyKinetics": Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(52290, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + o2 <=> tc4h9 + ho2',
 "chemkinKinetics": """
ic4h10+o2=tc4h9+ho2                                 1.000e+13 0.000     48.200   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(48200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ch3o2 <=> ic4h9 + ch3o2h',
 "chemkinKinetics": """
ic4h10+ch3o2=ic4h9+ch3o2h                           2.079e+00 3.970     18.280   
""",
 "rmgPyKinetics": Arrhenius(A=(2.079, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + c2h5o2 <=> ic4h9 + c2h5o2h',
 "chemkinKinetics": """
ic4h10+c2h5o2=ic4h9+c2h5o2h                         2.550e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ch3co3 <=> ic4h9 + ch3co3h',
 "chemkinKinetics": """
ic4h10+ch3co3=ic4h9+ch3co3h                         2.550e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + nc3h7o2 <=> ic4h9 + nc3h7o2h',
 "chemkinKinetics": """
ic4h10+nc3h7o2=ic4h9+nc3h7o2h                       2.550e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ic3h7o2 <=> ic4h9 + ic3h7o2h',
 "chemkinKinetics": """
ic4h10+ic3h7o2=ic4h9+ic3h7o2h                       2.550e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ic4h9o2 <=> ic4h9 + ic4h9o2h',
 "chemkinKinetics": """
ic4h10+ic4h9o2=ic4h9+ic4h9o2h                       2.550e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + tc4h9o2 <=> ic4h9 + tc4h9o2h',
 "chemkinKinetics": """
ic4h10+tc4h9o2=ic4h9+tc4h9o2h                       2.550e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + o2cho <=> ic4h9 + ho2cho',
 "chemkinKinetics": """
ic4h10+o2cho=ic4h9+ho2cho                           2.520e+13 0.000     20.440   
""",
 "rmgPyKinetics": Arrhenius(A=(2.52e+13, 'cm^3/(mol*s)'), n=0, Ea=(20440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + o2cho <=> tc4h9 + ho2cho',
 "chemkinKinetics": """
ic4h10+o2cho=tc4h9+ho2cho                           2.800e+12 0.000     16.010   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16010, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + sc4h9o2 <=> ic4h9 + sc4h9o2h',
 "chemkinKinetics": """
ic4h10+sc4h9o2=ic4h9+sc4h9o2h                       2.250e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(2.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + sc4h9o2 <=> tc4h9 + sc4h9o2h',
 "chemkinKinetics": """
ic4h10+sc4h9o2=tc4h9+sc4h9o2h                       2.800e+12 0.000     16.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + pc4h9o2 <=> ic4h9 + pc4h9o2h',
 "chemkinKinetics": """
ic4h10+pc4h9o2=ic4h9+pc4h9o2h                       2.250e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(2.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + pc4h9o2 <=> tc4h9 + pc4h9o2h',
 "chemkinKinetics": """
ic4h10+pc4h9o2=tc4h9+pc4h9o2h                       2.800e+12 0.000     16.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ch3o2 <=> tc4h9 + ch3o2h',
 "chemkinKinetics": """
ic4h10+ch3o2=tc4h9+ch3o2h                           1.366e+02 3.120     13.190   
""",
 "rmgPyKinetics": Arrhenius(A=(136.6, 'cm^3/(mol*s)'), n=3.12, Ea=(13190, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + c2h5o2 <=> tc4h9 + c2h5o2h',
 "chemkinKinetics": """
ic4h10+c2h5o2=tc4h9+c2h5o2h                         2.800e+12 0.000     16.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ch3co3 <=> tc4h9 + ch3co3h',
 "chemkinKinetics": """
ic4h10+ch3co3=tc4h9+ch3co3h                         2.800e+12 0.000     16.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + nc3h7o2 <=> tc4h9 + nc3h7o2h',
 "chemkinKinetics": """
ic4h10+nc3h7o2=tc4h9+nc3h7o2h                       2.800e+12 0.000     16.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ic3h7o2 <=> tc4h9 + ic3h7o2h',
 "chemkinKinetics": """
ic4h10+ic3h7o2=tc4h9+ic3h7o2h                       2.800e+12 0.000     16.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ic4h9o2 <=> tc4h9 + ic4h9o2h',
 "chemkinKinetics": """
ic4h10+ic4h9o2=tc4h9+ic4h9o2h                       2.800e+12 0.000     16.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + tc4h9o2 <=> tc4h9 + tc4h9o2h',
 "chemkinKinetics": """
ic4h10+tc4h9o2=tc4h9+tc4h9o2h                       2.800e+12 0.000     16.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h10 + ic4h9 <=> tc4h9 + ic4h10',
 "chemkinKinetics": """
ic4h10+ic4h9=tc4h9+ic4h10                           2.500e+10 0.000     7.900    
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9 + ho2 <=> ic4h9o + oh',
 "chemkinKinetics": """
ic4h9+ho2=ic4h9o+oh                                 7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h9 + ho2 <=> tc4h9o + oh',
 "chemkinKinetics": """
tc4h9+ho2=tc4h9o+oh                                 7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + ic4h9 <=> ch3o + ic4h9o',
 "chemkinKinetics": """
ch3o2+ic4h9=ch3o+ic4h9o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ch3o2 + tc4h9 <=> ch3o + tc4h9o',
 "chemkinKinetics": """
ch3o2+tc4h9=ch3o+tc4h9o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9 <=> tc4h9',
 "chemkinKinetics": """
ic4h9=tc4h9                                         3.560e+10 0.880     34.600   
""",
 "rmgPyKinetics": Arrhenius(A=(3.56e+10, 's^-1'), n=0.88, Ea=(34600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h8 + h <=> ic4h9',
 "chemkinKinetics": """
ic4h8+h=ic4h9                                       6.250e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.25e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h6 + ch3 <=> ic4h9',
 "chemkinKinetics": """
c3h6+ch3=ic4h9                                      1.890e+03 2.670     6.850    
""",
 "rmgPyKinetics": Arrhenius(A=(1890, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'h + ic4h8 <=> tc4h9',
 "chemkinKinetics": """
h+ic4h8=tc4h9                                       1.060e+12 0.510     1.230    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.06e+12, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (1230, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'tc4h9 + o2 <=> ic4h8 + ho2',
 "chemkinKinetics": """
tc4h9+o2=ic4h8+ho2                                  8.370e-01 3.590     11.960   
""",
 "rmgPyKinetics": Arrhenius(A=(0.837, 'cm^3/(mol*s)'), n=3.59, Ea=(11960, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h9 + o2 <=> ic4h8 + ho2',
 "chemkinKinetics": """
ic4h9+o2=ic4h8+ho2                                  1.070e+00 3.710     9.322    
""",
 "rmgPyKinetics": Arrhenius(A=(1.07, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'nc3h7o2 + ic4h9 <=> nc3h7o + ic4h9o',
 "chemkinKinetics": """
nc3h7o2+ic4h9=nc3h7o+ic4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + tc4h9 <=> nc3h7o + tc4h9o',
 "chemkinKinetics": """
nc3h7o2+tc4h9=nc3h7o+tc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + ic4h7 <=> nc3h7o + ic4h7o',
 "chemkinKinetics": """
nc3h7o2+ic4h7=nc3h7o+ic4h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + ic4h9 <=> sc4h9o + ic4h9o',
 "chemkinKinetics": """
sc4h9o2+ic4h9=sc4h9o+ic4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + tc4h9 <=> sc4h9o + tc4h9o',
 "chemkinKinetics": """
sc4h9o2+tc4h9=sc4h9o+tc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + ic4h9 <=> pc4h9o + ic4h9o',
 "chemkinKinetics": """
pc4h9o2+ic4h9=pc4h9o+ic4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + tc4h9 <=> pc4h9o + tc4h9o',
 "chemkinKinetics": """
pc4h9o2+tc4h9=pc4h9o+tc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + ic4h7 <=> pc4h9o + ic4h7o',
 "chemkinKinetics": """
pc4h9o2+ic4h7=pc4h9o+ic4h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + ic4h7 <=> sc4h9o + ic4h7o',
 "chemkinKinetics": """
sc4h9o2+ic4h7=sc4h9o+ic4h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9 + o2 <=> ic4h9o2',
 "chemkinKinetics": """
ic4h9+o2=ic4h9o2                                    2.260e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.26e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'tc4h9 + o2 <=> tc4h9o2',
 "chemkinKinetics": """
tc4h9+o2=tc4h9o2                                    1.410e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h9o2 + c4h10 <=> ic4h9o2h + sc4h9',
 "chemkinKinetics": """
ic4h9o2+c4h10=ic4h9o2h+sc4h9                        1.120e+13 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c4h10 <=> tc4h9o2h + sc4h9',
 "chemkinKinetics": """
tc4h9o2+c4h10=tc4h9o2h+sc4h9                        1.120e+13 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c4h10 <=> ic4h9o2h + pc4h9',
 "chemkinKinetics": """
ic4h9o2+c4h10=ic4h9o2h+pc4h9                        1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c4h10 <=> tc4h9o2h + pc4h9',
 "chemkinKinetics": """
tc4h9o2+c4h10=tc4h9o2h+pc4h9                        1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + ic4h9 <=> ic3h7o + ic4h9o',
 "chemkinKinetics": """
ic3h7o2+ic4h9=ic3h7o+ic4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + tc4h9 <=> ic3h7o + tc4h9o',
 "chemkinKinetics": """
ic3h7o2+tc4h9=ic3h7o+tc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + ic4h7 <=> ic3h7o + ic4h7o',
 "chemkinKinetics": """
ic3h7o2+ic4h7=ic3h7o+ic4h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c3h6 <=> ic4h9o2h + c3h5-a',
 "chemkinKinetics": """
ic4h9o2+c3h6=ic4h9o2h+c3h5-a                        3.240e+11 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c3h6 <=> tc4h9o2h + c3h5-a',
 "chemkinKinetics": """
tc4h9o2+c3h6=tc4h9o2h+c3h5-a                        3.240e+11 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + ic4h8 <=> ic4h9o2h + ic4h7',
 "chemkinKinetics": """
ic4h9o2+ic4h8=ic4h9o2h+ic4h7                        1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + ic4h8 <=> tc4h9o2h + ic4h7',
 "chemkinKinetics": """
tc4h9o2+ic4h8=tc4h9o2h+ic4h7                        1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'pc4h9o2 + ic4h8 <=> pc4h9o2h + ic4h7',
 "chemkinKinetics": """
pc4h9o2+ic4h8=pc4h9o2h+ic4h7                        1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9o2 + ic4h8 <=> sc4h9o2h + ic4h7',
 "chemkinKinetics": """
sc4h9o2+ic4h8=sc4h9o2h+ic4h7                        1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7o2 + ic4h8 <=> ic3h7o2h + ic4h7',
 "chemkinKinetics": """
ic3h7o2+ic4h8=ic3h7o2h+ic4h7                        1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc3h7o2 + ic4h8 <=> nc3h7o2h + ic4h7',
 "chemkinKinetics": """
nc3h7o2+ic4h8=nc3h7o2h+ic4h7                        1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c4h8-1 <=> ic4h9o2h + c4h71-3',
 "chemkinKinetics": """
ic4h9o2+c4h8-1=ic4h9o2h+c4h71-3                     1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c4h8-1 <=> tc4h9o2h + c4h71-3',
 "chemkinKinetics": """
tc4h9o2+c4h8-1=tc4h9o2h+c4h71-3                     1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c4h8-2 <=> ic4h9o2h + c4h71-3',
 "chemkinKinetics": """
ic4h9o2+c4h8-2=ic4h9o2h+c4h71-3                     1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c4h8-2 <=> tc4h9o2h + c4h71-3',
 "chemkinKinetics": """
tc4h9o2+c4h8-2=tc4h9o2h+c4h71-3                     1.400e+12 0.000     14.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'cc4h8o + oh => ch2o + c3h5-a + h2o',
 "chemkinKinetics": """
cc4h8o+oh=>ch2o+c3h5-a+h2o                          5.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'cc4h8o + h => ch2o + c3h5-a + h2',
 "chemkinKinetics": """
cc4h8o+h=>ch2o+c3h5-a+h2                            3.510e+07 2.000     5.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3.51e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'cc4h8o + o => ch2o + c3h5-a + oh',
 "chemkinKinetics": """
cc4h8o+o=>ch2o+c3h5-a+oh                            1.124e+14 0.000     5.200    
""",
 "rmgPyKinetics": Arrhenius(A=(1.124e+14, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'cc4h8o + ho2 => ch2o + c3h5-a + h2o2',
 "chemkinKinetics": """
cc4h8o+ho2=>ch2o+c3h5-a+h2o2                        1.000e+13 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'cc4h8o + ch3o2 => ch2o + c3h5-a + ch3o2h',
 "chemkinKinetics": """
cc4h8o+ch3o2=>ch2o+c3h5-a+ch3o2h                    1.000e+13 0.000     19.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'cc4h8o + ch3 => ch2o + c3h5-a + ch4',
 "chemkinKinetics": """
cc4h8o+ch3=>ch2o+c3h5-a+ch4                         2.000e+11 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h4 + tc4h9o2 <=> c2h3 + tc4h9o2h',
 "chemkinKinetics": """
c2h4+tc4h9o2=c2h3+tc4h9o2h                          8.590e+00 3.754     27.132   
""",
 "rmgPyKinetics": Arrhenius(A=(8.59, 'cm^3/(mol*s)'), n=3.754, Ea=(27132, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + ch4 <=> tc4h9o2h + ch3',
 "chemkinKinetics": """
tc4h9o2+ch4=tc4h9o2h+ch3                            1.130e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h2 + tc4h9o2 <=> h + tc4h9o2h',
 "chemkinKinetics": """
h2+tc4h9o2=h+tc4h9o2h                               3.010e+13 0.000     26.030   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c2h6 <=> tc4h9o2h + c2h5',
 "chemkinKinetics": """
tc4h9o2+c2h6=tc4h9o2h+c2h5                          1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c3h8 <=> tc4h9o2h + ic3h7',
 "chemkinKinetics": """
tc4h9o2+c3h8=tc4h9o2h+ic3h7                         2.000e+12 0.000     17.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c3h8 <=> tc4h9o2h + nc3h7',
 "chemkinKinetics": """
tc4h9o2+c3h8=tc4h9o2h+nc3h7                         1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + ch3oh <=> tc4h9o2h + ch2oh',
 "chemkinKinetics": """
tc4h9o2+ch3oh=tc4h9o2h+ch2oh                        6.300e+12 0.000     19.360   
""",
 "rmgPyKinetics": Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c2h5oh <=> tc4h9o2h + pc2h4oh',
 "chemkinKinetics": """
tc4h9o2+c2h5oh=tc4h9o2h+pc2h4oh                     6.300e+12 0.000     19.360   
""",
 "rmgPyKinetics": Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c2h5oh <=> tc4h9o2h + sc2h4oh',
 "chemkinKinetics": """
tc4h9o2+c2h5oh=tc4h9o2h+sc2h4oh                     4.200e+12 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(4.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + ch3cho <=> ic4h9o2h + ch3co',
 "chemkinKinetics": """
ic4h9o2+ch3cho=ic4h9o2h+ch3co                       2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + ch3cho <=> tc4h9o2h + ch3co',
 "chemkinKinetics": """
tc4h9o2+ch3cho=tc4h9o2h+ch3co                       2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c2h3cho <=> ic4h9o2h + c2h3co',
 "chemkinKinetics": """
ic4h9o2+c2h3cho=ic4h9o2h+c2h3co                     2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c2h3cho <=> tc4h9o2h + c2h3co',
 "chemkinKinetics": """
tc4h9o2+c2h3cho=tc4h9o2h+c2h3co                     2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c2h5cho <=> ic4h9o2h + c2h5co',
 "chemkinKinetics": """
ic4h9o2+c2h5cho=ic4h9o2h+c2h5co                     2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c2h5cho <=> tc4h9o2h + c2h5co',
 "chemkinKinetics": """
tc4h9o2+c2h5cho=tc4h9o2h+c2h5co                     2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + ho2 <=> ic4h9o2h + o2',
 "chemkinKinetics": """
ic4h9o2+ho2=ic4h9o2h+o2                             1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + ho2 <=> tc4h9o2h + o2',
 "chemkinKinetics": """
tc4h9o2+ho2=tc4h9o2h+o2                             1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + h2o2 <=> ic4h9o2h + ho2',
 "chemkinKinetics": """
ic4h9o2+h2o2=ic4h9o2h+ho2                           2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + h2o2 <=> tc4h9o2h + ho2',
 "chemkinKinetics": """
tc4h9o2+h2o2=tc4h9o2h+ho2                           2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + ch2o <=> ic4h9o2h + hco',
 "chemkinKinetics": """
ic4h9o2+ch2o=ic4h9o2h+hco                           1.300e+11 0.000     9.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.3e+11, 'cm^3/(mol*s)'), n=0, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + ch2o <=> tc4h9o2h + hco',
 "chemkinKinetics": """
tc4h9o2+ch2o=tc4h9o2h+hco                           1.300e+11 0.000     9.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.3e+11, 'cm^3/(mol*s)'), n=0, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + ch3o2 => ic4h9o + ch3o + o2',
 "chemkinKinetics": """
ic4h9o2+ch3o2=>ic4h9o+ch3o+o2                       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'tc4h9o2 + ch3o2 => tc4h9o + ch3o + o2',
 "chemkinKinetics": """
tc4h9o2+ch3o2=>tc4h9o+ch3o+o2                       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h9o2 + c2h5o2 => ic4h9o + c2h5o + o2',
 "chemkinKinetics": """
ic4h9o2+c2h5o2=>ic4h9o+c2h5o+o2                     1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'tc4h9o2 + c2h5o2 => tc4h9o + c2h5o + o2',
 "chemkinKinetics": """
tc4h9o2+c2h5o2=>tc4h9o+c2h5o+o2                     1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h9o2 + ch3co3 => ic4h9o + ch3co2 + o2',
 "chemkinKinetics": """
ic4h9o2+ch3co3=>ic4h9o+ch3co2+o2                    1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'tc4h9o2 + ch3co3 => tc4h9o + ch3co2 + o2',
 "chemkinKinetics": """
tc4h9o2+ch3co3=>tc4h9o+ch3co2+o2                    1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h9o2 + ic4h9o2 => o2 + ic4h9o + ic4h9o',
 "chemkinKinetics": """
ic4h9o2+ic4h9o2=>o2+ic4h9o+ic4h9o                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h9o2 + tc4h9o2 => ic4h9o + tc4h9o + o2',
 "chemkinKinetics": """
ic4h9o2+tc4h9o2=>ic4h9o+tc4h9o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'tc4h9o2 + tc4h9o2 => o2 + tc4h9o + tc4h9o',
 "chemkinKinetics": """
tc4h9o2+tc4h9o2=>o2+tc4h9o+tc4h9o                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h9o2 + pc4h9o2 => ic4h9o + pc4h9o + o2',
 "chemkinKinetics": """
ic4h9o2+pc4h9o2=>ic4h9o+pc4h9o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'tc4h9o2 + pc4h9o2 => tc4h9o + pc4h9o + o2',
 "chemkinKinetics": """
tc4h9o2+pc4h9o2=>tc4h9o+pc4h9o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h9o2 + sc4h9o2 => ic4h9o + sc4h9o + o2',
 "chemkinKinetics": """
ic4h9o2+sc4h9o2=>ic4h9o+sc4h9o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'tc4h9o2 + sc4h9o2 => tc4h9o + sc4h9o + o2',
 "chemkinKinetics": """
tc4h9o2+sc4h9o2=>tc4h9o+sc4h9o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h9o2 + nc3h7o2 => ic4h9o + nc3h7o + o2',
 "chemkinKinetics": """
ic4h9o2+nc3h7o2=>ic4h9o+nc3h7o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'tc4h9o2 + nc3h7o2 => tc4h9o + nc3h7o + o2',
 "chemkinKinetics": """
tc4h9o2+nc3h7o2=>tc4h9o+nc3h7o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h9o2 + ic3h7o2 => ic4h9o + ic3h7o + o2',
 "chemkinKinetics": """
ic4h9o2+ic3h7o2=>ic4h9o+ic3h7o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'tc4h9o2 + ic3h7o2 => tc4h9o + ic3h7o + o2',
 "chemkinKinetics": """
tc4h9o2+ic3h7o2=>tc4h9o+ic3h7o+o2                   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h9o2 + ho2 => ic4h9o + oh + o2',
 "chemkinKinetics": """
ic4h9o2+ho2=>ic4h9o+oh+o2                           1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'tc4h9o2 + ho2 => tc4h9o + oh + o2',
 "chemkinKinetics": """
tc4h9o2+ho2=>tc4h9o+oh+o2                           1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h9o2 + ch3 <=> ic4h9o + ch3o',
 "chemkinKinetics": """
ic4h9o2+ch3=ic4h9o+ch3o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c2h5 <=> ic4h9o + c2h5o',
 "chemkinKinetics": """
ic4h9o2+c2h5=ic4h9o+c2h5o                           7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + ic3h7 <=> ic4h9o + ic3h7o',
 "chemkinKinetics": """
ic4h9o2+ic3h7=ic4h9o+ic3h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + nc3h7 <=> ic4h9o + nc3h7o',
 "chemkinKinetics": """
ic4h9o2+nc3h7=ic4h9o+nc3h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + pc4h9 <=> ic4h9o + pc4h9o',
 "chemkinKinetics": """
ic4h9o2+pc4h9=ic4h9o+pc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + sc4h9 <=> ic4h9o + sc4h9o',
 "chemkinKinetics": """
ic4h9o2+sc4h9=ic4h9o+sc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + ic4h9 <=> ic4h9o + ic4h9o',
 "chemkinKinetics": """
ic4h9o2+ic4h9=ic4h9o+ic4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + tc4h9 <=> ic4h9o + tc4h9o',
 "chemkinKinetics": """
ic4h9o2+tc4h9=ic4h9o+tc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c3h5-a <=> ic4h9o + c3h5o',
 "chemkinKinetics": """
ic4h9o2+c3h5-a=ic4h9o+c3h5o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c4h71-3 <=> ic4h9o + c4h7o',
 "chemkinKinetics": """
ic4h9o2+c4h71-3=ic4h9o+c4h7o                        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + ic4h7 <=> ic4h9o + ic4h7o',
 "chemkinKinetics": """
ic4h9o2+ic4h7=ic4h9o+ic4h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + ch3 <=> tc4h9o + ch3o',
 "chemkinKinetics": """
tc4h9o2+ch3=tc4h9o+ch3o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c2h5 <=> tc4h9o + c2h5o',
 "chemkinKinetics": """
tc4h9o2+c2h5=tc4h9o+c2h5o                           7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + ic3h7 <=> tc4h9o + ic3h7o',
 "chemkinKinetics": """
tc4h9o2+ic3h7=tc4h9o+ic3h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + nc3h7 <=> tc4h9o + nc3h7o',
 "chemkinKinetics": """
tc4h9o2+nc3h7=tc4h9o+nc3h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + pc4h9 <=> tc4h9o + pc4h9o',
 "chemkinKinetics": """
tc4h9o2+pc4h9=tc4h9o+pc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + sc4h9 <=> tc4h9o + sc4h9o',
 "chemkinKinetics": """
tc4h9o2+sc4h9=tc4h9o+sc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + ic4h9 <=> tc4h9o + ic4h9o',
 "chemkinKinetics": """
tc4h9o2+ic4h9=tc4h9o+ic4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + tc4h9 <=> tc4h9o + tc4h9o',
 "chemkinKinetics": """
tc4h9o2+tc4h9=tc4h9o+tc4h9o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c3h5-a <=> tc4h9o + c3h5o',
 "chemkinKinetics": """
tc4h9o2+c3h5-a=tc4h9o+c3h5o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + c4h71-3 <=> tc4h9o + c4h7o',
 "chemkinKinetics": """
tc4h9o2+c4h71-3=tc4h9o+c4h7o                        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h9o2 + ic4h7 <=> tc4h9o + ic4h7o',
 "chemkinKinetics": """
tc4h9o2+ic4h7=tc4h9o+ic4h7o                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c2h4 <=> ic4h9o2h + c2h3',
 "chemkinKinetics": """
ic4h9o2+c2h4=ic4h9o2h+c2h3                          2.000e+11 0.000     6.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + ch4 <=> ic4h9o2h + ch3',
 "chemkinKinetics": """
ic4h9o2+ch4=ic4h9o2h+ch3                            1.130e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'h2 + ic4h9o2 <=> h + ic4h9o2h',
 "chemkinKinetics": """
h2+ic4h9o2=h+ic4h9o2h                               3.010e+13 0.000     26.030   
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c2h6 <=> ic4h9o2h + c2h5',
 "chemkinKinetics": """
ic4h9o2+c2h6=ic4h9o2h+c2h5                          1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c3h8 <=> ic4h9o2h + ic3h7',
 "chemkinKinetics": """
ic4h9o2+c3h8=ic4h9o2h+ic3h7                         2.000e+12 0.000     17.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c3h8 <=> ic4h9o2h + nc3h7',
 "chemkinKinetics": """
ic4h9o2+c3h8=ic4h9o2h+nc3h7                         1.700e+13 0.000     20.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + ch3oh <=> ic4h9o2h + ch2oh',
 "chemkinKinetics": """
ic4h9o2+ch3oh=ic4h9o2h+ch2oh                        6.300e+12 0.000     19.360   
""",
 "rmgPyKinetics": Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c2h5oh <=> ic4h9o2h + pc2h4oh',
 "chemkinKinetics": """
ic4h9o2+c2h5oh=ic4h9o2h+pc2h4oh                     6.300e+12 0.000     19.360   
""",
 "rmgPyKinetics": Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2 + c2h5oh <=> ic4h9o2h + sc2h4oh',
 "chemkinKinetics": """
ic4h9o2+c2h5oh=ic4h9o2h+sc2h4oh                     4.200e+12 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(4.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9o2h <=> ic4h9o + oh',
 "chemkinKinetics": """
ic4h9o2h=ic4h9o+oh                                  1.500e+16 0.000     42.500   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'tc4h9o2h <=> tc4h9o + oh',
 "chemkinKinetics": """
tc4h9o2h=tc4h9o+oh                                  5.950e+15 0.000     42.540   
""",
 "rmgPyKinetics": Arrhenius(A=(5.95e+15, 's^-1'), n=0, Ea=(42540, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h9o + ho2 <=> ic3h7cho + h2o2',
 "chemkinKinetics": """
ic4h9o+ho2=ic3h7cho+h2o2                            1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h9o + oh <=> ic3h7cho + h2o',
 "chemkinKinetics": """
ic4h9o+oh=ic3h7cho+h2o                              1.810e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h9o + ch3 <=> ic3h7cho + ch4',
 "chemkinKinetics": """
ic4h9o+ch3=ic3h7cho+ch4                             2.400e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h9o + o <=> ic3h7cho + oh',
 "chemkinKinetics": """
ic4h9o+o=ic3h7cho+oh                                6.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h9o + h <=> ic3h7cho + h2',
 "chemkinKinetics": """
ic4h9o+h=ic3h7cho+h2                                1.990e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.99e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic3h7cho + h <=> ic4h9o',
 "chemkinKinetics": """
ic3h7cho+h=ic4h9o                                   1.000e+12 0.000     5.860    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2o + ic3h7 <=> ic4h9o',
 "chemkinKinetics": """
ch2o+ic3h7=ic4h9o                                   5.000e+10 0.000     2.330    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(2330, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3coch3 + ch3 <=> tc4h9o',
 "chemkinKinetics": """
ch3coch3+ch3=tc4h9o                                 1.500e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h9o + o2 <=> ic3h7cho + ho2',
 "chemkinKinetics": """
ic4h9o+o2=ic3h7cho+ho2                              1.930e+11 0.000     1.660    
""",
 "rmgPyKinetics": Arrhenius(A=(1.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(1660, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'tc4h9o + o2 <=> ic4h8o + ho2',
 "chemkinKinetics": """
tc4h9o+o2=ic4h8o+ho2                                8.100e+11 0.000     4.700    
""",
 "rmgPyKinetics": Arrhenius(A=(8.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(4700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h8o <=> ic3h7cho',
 "chemkinKinetics": """
ic4h8o=ic3h7cho                                     4.180e+13 0.000     52.720   
""",
 "rmgPyKinetics": Arrhenius(A=(4.18e+13, 's^-1'), n=0, Ea=(52720, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Intra_Disproportionation',  ],
},

{
 "reaction": 'ic4h8o + oh <=> ic3h6cho + h2o',
 "chemkinKinetics": """
ic4h8o+oh=ic3h6cho+h2o                              1.250e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.25e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h8o + h <=> ic3h6cho + h2',
 "chemkinKinetics": """
ic4h8o+h=ic3h6cho+h2                                1.250e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.25e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h8o + ho2 <=> ic3h6cho + h2o2',
 "chemkinKinetics": """
ic4h8o+ho2=ic3h6cho+h2o2                            2.500e+12 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h8o + ch3o2 <=> ic3h6cho + ch3o2h',
 "chemkinKinetics": """
ic4h8o+ch3o2=ic3h6cho+ch3o2h                        2.500e+12 0.000     19.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h8o + ch3 <=> ic3h6cho + ch4',
 "chemkinKinetics": """
ic4h8o+ch3=ic3h6cho+ch4                             5.000e+10 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h8o + o <=> ic3h6cho + oh',
 "chemkinKinetics": """
ic4h8o+o=ic3h6cho+oh                                1.250e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.25e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'tc3h6cho + h <=> ic3h7cho',
 "chemkinKinetics": """
tc3h6cho+h=ic3h7cho                                 2.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic3h7 + hco <=> ic3h7cho',
 "chemkinKinetics": """
ic3h7+hco=ic3h7cho                                  1.810e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic3h7cho + ho2 <=> ic3h7co + h2o2',
 "chemkinKinetics": """
ic3h7cho+ho2=ic3h7co+h2o2                           3.000e+12 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7cho + ho2 <=> tc3h6cho + h2o2',
 "chemkinKinetics": """
ic3h7cho+ho2=tc3h6cho+h2o2                          8.000e+10 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(8e+10, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7cho + ch3 <=> ic3h7co + ch4',
 "chemkinKinetics": """
ic3h7cho+ch3=ic3h7co+ch4                            3.980e+12 0.000     8.700    
""",
 "rmgPyKinetics": Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(8700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7cho + o <=> ic3h7co + oh',
 "chemkinKinetics": """
ic3h7cho+o=ic3h7co+oh                               7.180e+12 0.000     1.389    
""",
 "rmgPyKinetics": Arrhenius(A=(7.18e+12, 'cm^3/(mol*s)'), n=0, Ea=(1389, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7cho + o2 <=> ic3h7co + ho2',
 "chemkinKinetics": """
ic3h7cho+o2=ic3h7co+ho2                             4.000e+13 0.000     37.600   
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(37600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7cho + oh <=> ic3h7co + h2o',
 "chemkinKinetics": """
ic3h7cho+oh=ic3h7co+h2o                             2.690e+10 0.760     -0.340   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.69e+10, 'cm^3/(mol*s)'),
    n = 0.76,
    Ea = (-340, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7cho + oh <=> tc3h6cho + h2o',
 "chemkinKinetics": """
ic3h7cho+oh=tc3h6cho+h2o                            1.684e+12 0.000     -0.781   
""",
 "rmgPyKinetics": Arrhenius(A=(1.684e+12, 'cm^3/(mol*s)'), n=0, Ea=(-781, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7cho + h <=> ic3h7co + h2',
 "chemkinKinetics": """
ic3h7cho+h=ic3h7co+h2                               2.600e+12 0.000     2.600    
""",
 "rmgPyKinetics": Arrhenius(A=(2.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7cho + oh <=> ic3h6cho + h2o',
 "chemkinKinetics": """
ic3h7cho+oh=ic3h6cho+h2o                            3.120e+06 2.000     -0.298   
""",
 "rmgPyKinetics": Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7cho + ho2 <=> ic3h6cho + h2o2',
 "chemkinKinetics": """
ic3h7cho+ho2=ic3h6cho+h2o2                          2.740e+04 2.550     15.500   
""",
 "rmgPyKinetics": Arrhenius(A=(27400, 'cm^3/(mol*s)'), n=2.55, Ea=(15500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7cho + ch3o2 <=> ic3h6cho + ch3o2h',
 "chemkinKinetics": """
ic3h7cho+ch3o2=ic3h6cho+ch3o2h                      4.760e+04 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(47600, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h7 + co <=> ic3h7co',
 "chemkinKinetics": """
ic3h7+co=ic3h7co                                    1.500e+11 0.000     4.810    
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6 + hco <=> ic3h6cho',
 "chemkinKinetics": """
c3h6+hco=ic3h6cho                                   1.000e+11 0.000     7.800    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h3cho + ch3 <=> ic3h6cho',
 "chemkinKinetics": """
c2h3cho+ch3=ic3h6cho                                1.000e+11 0.000     7.800    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h9o2 <=> ic4h8o2h-i',
 "chemkinKinetics": """
ic4h9o2=ic4h8o2h-i                                  7.500e+10 0.000     24.400   
""",
 "rmgPyKinetics": Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'tc4h9o2 <=> tc4h8o2h-i',
 "chemkinKinetics": """
tc4h9o2=tc4h8o2h-i                                  9.000e+11 0.000     34.500   
""",
 "rmgPyKinetics": Arrhenius(A=(9e+11, 's^-1'), n=0, Ea=(34500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h9o2 <=> ic4h8o2h-t',
 "chemkinKinetics": """
ic4h9o2=ic4h8o2h-t                                  1.000e+11 0.000     29.200   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(29200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h9o2 <=> ic4h8 + ho2',
 "chemkinKinetics": """
ic4h9o2=ic4h8+ho2                                   2.265e+35 -7.220    39.490   
""",
 "rmgPyKinetics": Arrhenius(A=(2.265e+35, 's^-1'), n=-7.22, Ea=(39490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'tc4h9o2 <=> ic4h8 + ho2',
 "chemkinKinetics": """
tc4h9o2=ic4h8+ho2                                   7.612e+42 -9.410    41.490   
""",
 "rmgPyKinetics": Arrhenius(A=(7.612e+42, 's^-1'), n=-9.41, Ea=(41490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'ic4h8o2h-i + o2 <=> ic4h8ooh-io2',
 "chemkinKinetics": """
ic4h8o2h-i+o2=ic4h8ooh-io2                          2.260e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.26e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'tc4h8o2h-i + o2 <=> tc4h8ooh-io2',
 "chemkinKinetics": """
tc4h8o2h-i+o2=tc4h8ooh-io2                          2.260e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.26e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h8o2h-t + o2 <=> ic4h8ooh-to2',
 "chemkinKinetics": """
ic4h8o2h-t+o2=ic4h8ooh-to2                          1.410e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h8ooh-io2 <=> ic4ketii + oh',
 "chemkinKinetics": """
ic4h8ooh-io2=ic4ketii+oh                            5.000e+10 0.000     21.400   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+10, 's^-1'), n=0, Ea=(21400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'ic4h8ooh-to2 <=> ic4ketit + oh',
 "chemkinKinetics": """
ic4h8ooh-to2=ic4ketit+oh                            4.000e+11 0.000     31.500   
""",
 "rmgPyKinetics": Arrhenius(A=(4e+11, 's^-1'), n=0, Ea=(31500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'tc4h8ooh-io2 <=> tic4h7q2-i',
 "chemkinKinetics": """
tc4h8ooh-io2=tic4h7q2-i                             7.500e+10 0.000     24.400   
""",
 "rmgPyKinetics": Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h7ooh + ho2 <=> tic4h7q2-i',
 "chemkinKinetics": """
ic4h7ooh+ho2=tic4h7q2-i                             1.000e+11 0.000     10.600   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h8ooh-io2 <=> iic4h7q2-i',
 "chemkinKinetics": """
ic4h8ooh-io2=iic4h7q2-i                             3.750e+10 0.000     24.400   
""",
 "rmgPyKinetics": Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h8ooh-io2 <=> iic4h7q2-t',
 "chemkinKinetics": """
ic4h8ooh-io2=iic4h7q2-t                             1.000e+11 0.000     29.200   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(29200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h8ooh-to2 <=> tic4h7q2-i',
 "chemkinKinetics": """
ic4h8ooh-to2=tic4h7q2-i                             6.000e+11 0.000     34.500   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(34500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ac3h5ooh + ch2o2h <=> iic4h7q2-i',
 "chemkinKinetics": """
ac3h5ooh+ch2o2h=iic4h7q2-i                          8.500e+10 0.000     10.600   
""",
 "rmgPyKinetics": Arrhenius(A=(8.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h7ooh + ho2 <=> iic4h7q2-t',
 "chemkinKinetics": """
ic4h7ooh+ho2=iic4h7q2-t                             1.000e+11 0.000     7.800    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2o2h <=> ch2o + oh',
 "chemkinKinetics": """
ch2o2h=ch2o+oh                                      9.000e+14 0.000     1.500    
""",
 "rmgPyKinetics": Arrhenius(A=(9e+14, 's^-1'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4ketii => ch2o + c2h5co + oh',
 "chemkinKinetics": """
ic4ketii=>ch2o+c2h5co+oh                            1.500e+16 0.000     42.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4ketit => ch3coch3 + hco + oh',
 "chemkinKinetics": """
ic4ketit=>ch3coch3+hco+oh                           9.500e+15 0.000     42.540   
""",
 "rmgPyKinetics": Arrhenius(A=(9.5e+15, 's^-1'), n=0, Ea=(42540, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products1',  ],
},

{
 "reaction": 'ic4h8 + ho2 <=> tc4h8o2h-i',
 "chemkinKinetics": """
ic4h8+ho2=tc4h8o2h-i                                3.970e+11 0.000     12.620   
""",
 "rmgPyKinetics": Arrhenius(A=(3.97e+11, 'cm^3/(mol*s)'), n=0, Ea=(12620, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h8 + ho2 <=> ic4h8o2h-t',
 "chemkinKinetics": """
ic4h8+ho2=ic4h8o2h-t                                3.970e+11 0.000     12.620   
""",
 "rmgPyKinetics": Arrhenius(A=(3.97e+11, 'cm^3/(mol*s)'), n=0, Ea=(12620, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h8o2h-i <=> cc4h8o + oh',
 "chemkinKinetics": """
ic4h8o2h-i=cc4h8o+oh                                4.470e+11 0.000     21.900   
""",
 "rmgPyKinetics": Arrhenius(A=(4.47e+11, 's^-1'), n=0, Ea=(21900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'ic4h8o2h-t <=> ic4h8o + oh',
 "chemkinKinetics": """
ic4h8o2h-t=ic4h8o+oh                                3.090e+12 0.000     13.400   
""",
 "rmgPyKinetics": Arrhenius(A=(3.09e+12, 's^-1'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'tc4h8o2h-i <=> ic4h8o + oh',
 "chemkinKinetics": """
tc4h8o2h-i=ic4h8o+oh                                3.980e+12 0.000     17.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3.98e+12, 's^-1'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h8o2h-i => oh + ch2o + c3h6',
 "chemkinKinetics": """
ic4h8o2h-i=>oh+ch2o+c3h6                            8.451e+15 -0.680    29.170   
""",
 "rmgPyKinetics": Arrhenius(A=(8.451e+15, 's^-1'), n=-0.68, Ea=(29170, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'ic4h8 <=> c3h5-t + ch3',
 "chemkinKinetics": """
ic4h8=c3h5-t+ch3                                    1.920e+66 -14.220   128.100  
""",
 "rmgPyKinetics": Arrhenius(A=(1.92e+66, 's^-1'), n=-14.22, Ea=(128100, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h8 <=> ic4h7 + h',
 "chemkinKinetics": """
ic4h8=ic4h7+h                                       3.070e+55 -11.490   114.300  
""",
 "rmgPyKinetics": Arrhenius(A=(3.07e+55, 's^-1'), n=-11.49, Ea=(114300, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h8 + h <=> c3h6 + ch3',
 "chemkinKinetics": """
ic4h8+h=c3h6+ch3                                    5.680e+33 -5.720    20.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.68e+33, 'cm^3/(mol*s)'),
    n = -5.72,
    Ea = (20000, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h8 + h <=> ic4h7 + h2',
 "chemkinKinetics": """
ic4h8+h=ic4h7+h2                                    3.400e+05 2.500     2.492    
""",
 "rmgPyKinetics": Arrhenius(A=(340000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8 + o => ch2co + ch3 + ch3',
 "chemkinKinetics": """
ic4h8+o=>ch2co+ch3+ch3                              3.330e+07 1.760     0.076    
""",
 "rmgPyKinetics": Arrhenius(A=(3.33e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h8 + o => ic3h6co + h + h',
 "chemkinKinetics": """
ic4h8+o=>ic3h6co+h+h                                1.660e+07 1.760     0.076    
""",
 "rmgPyKinetics": Arrhenius(A=(1.66e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h8 + o <=> ic4h7 + oh',
 "chemkinKinetics": """
ic4h8+o=ic4h7+oh                                    1.206e+11 0.700     7.633    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.206e+11, 'cm^3/(mol*s)'),
    n = 0.7,
    Ea = (7633, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8 + ch3 <=> ic4h7 + ch4',
 "chemkinKinetics": """
ic4h8+ch3=ic4h7+ch4                                 4.420e+00 3.500     5.675    
""",
 "rmgPyKinetics": Arrhenius(A=(4.42, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8 + ho2 <=> ic4h7 + h2o2',
 "chemkinKinetics": """
ic4h8+ho2=ic4h7+h2o2                                1.928e+04 2.600     13.910   
""",
 "rmgPyKinetics": Arrhenius(A=(19280, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8 + o2cho <=> ic4h7 + ho2cho',
 "chemkinKinetics": """
ic4h8+o2cho=ic4h7+ho2cho                            1.928e+04 2.600     13.910   
""",
 "rmgPyKinetics": Arrhenius(A=(19280, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8 + o2 <=> ic4h7 + ho2',
 "chemkinKinetics": """
ic4h8+o2=ic4h7+ho2                                  6.000e+12 0.000     39.900   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8 + c3h5-a <=> ic4h7 + c3h6',
 "chemkinKinetics": """
ic4h8+c3h5-a=ic4h7+c3h6                             7.940e+11 0.000     20.500   
""",
 "rmgPyKinetics": Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8 + c3h5-s <=> ic4h7 + c3h6',
 "chemkinKinetics": """
ic4h8+c3h5-s=ic4h7+c3h6                             7.940e+11 0.000     20.500   
""",
 "rmgPyKinetics": Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8 + c3h5-t <=> ic4h7 + c3h6',
 "chemkinKinetics": """
ic4h8+c3h5-t=ic4h7+c3h6                             7.940e+11 0.000     20.500   
""",
 "rmgPyKinetics": Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8 + oh <=> ic4h7 + h2o',
 "chemkinKinetics": """
ic4h8+oh=ic4h7+h2o                                  5.200e+06 2.000     -0.298   
""",
 "rmgPyKinetics": Arrhenius(A=(5.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8 + o <=> ic3h7 + hco',
 "chemkinKinetics": """
ic4h8+o=ic3h7+hco                                   1.580e+07 1.760     -1.216   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.58e+07, 'cm^3/(mol*s)'),
    n = 1.76,
    Ea = (-1216, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h8 + ch3o2 <=> ic4h7 + ch3o2h',
 "chemkinKinetics": """
ic4h8+ch3o2=ic4h7+ch3o2h                            1.928e+04 2.600     13.910   
""",
 "rmgPyKinetics": Arrhenius(A=(19280, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8 + ho2 <=> ic4h8o + oh',
 "chemkinKinetics": """
ic4h8+ho2=ic4h8o+oh                                 1.290e+12 0.000     13.340   
""",
 "rmgPyKinetics": Arrhenius(A=(1.29e+12, 'cm^3/(mol*s)'), n=0, Ea=(13340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7 + o2 <=> ic3h5cho + oh',
 "chemkinKinetics": """
ic4h7+o2=ic3h5cho+oh                                2.470e+13 -0.450    23.020   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.47e+13, 'cm^3/(mol*s)'),
    n = -0.45,
    Ea = (23020, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7 + o2 <=> ch3coch2 + ch2o',
 "chemkinKinetics": """
ic4h7+o2=ch3coch2+ch2o                              7.140e+15 -1.210    21.050   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.14e+15, 'cm^3/(mol*s)'),
    n = -1.21,
    Ea = (21050, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7 + o2 => c3h4-a + ch2o + oh',
 "chemkinKinetics": """
ic4h7+o2=>c3h4-a+ch2o+oh                            7.290e+29 -5.710    21.450   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.29e+29, 'cm^3/(mol*s)'),
    n = -5.71,
    Ea = (21450, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7 + o <=> ic3h5cho + h',
 "chemkinKinetics": """
ic4h7+o=ic3h5cho+h                                  6.030e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7 <=> c3h4-a + ch3',
 "chemkinKinetics": """
ic4h7=c3h4-a+ch3                                    1.230e+47 -9.740    74.260   
""",
 "rmgPyKinetics": Arrhenius(A=(1.23e+47, 's^-1'), n=-9.74, Ea=(74260, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3o2 + ic4h7 <=> ch3o + ic4h7o',
 "chemkinKinetics": """
ch3o2+ic4h7=ch3o+ic4h7o                             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h7 + ho2 <=> ic4h7o + oh',
 "chemkinKinetics": """
ic4h7+ho2=ic4h7o+oh                                 7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c3h5-t + ch2o <=> ic4h7o',
 "chemkinKinetics": """
c3h5-t+ch2o=ic4h7o                                  1.000e+11 0.000     12.600   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(12600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h7o <=> ic4h6oh',
 "chemkinKinetics": """
ic4h7o=ic4h6oh                                      1.391e+11 0.000     15.600   
""",
 "rmgPyKinetics": Arrhenius(A=(1.391e+11, 's^-1'), n=0, Ea=(15600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h7o <=> ic3h5cho + h',
 "chemkinKinetics": """
ic4h7o=ic3h5cho+h                                   5.000e+13 0.000     29.100   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 's^-1'), n=0, Ea=(29100, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h6oh + h2 <=> ic4h7oh + h',
 "chemkinKinetics": """
ic4h6oh+h2=ic4h7oh+h                                2.160e+04 2.380     18.990   
""",
 "rmgPyKinetics": Arrhenius(A=(21600, 'cm^3/(mol*s)'), n=2.38, Ea=(18990, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h7oh + o2 <=> ic4h6oh + ho2',
 "chemkinKinetics": """
ic4h7oh+o2=ic4h6oh+ho2                              6.000e+13 0.000     39.900   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h6oh + ch2o <=> ic4h7oh + hco',
 "chemkinKinetics": """
ic4h6oh+ch2o=ic4h7oh+hco                            6.300e+08 1.900     18.190   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.3e+08, 'cm^3/(mol*s)'),
    n = 1.9,
    Ea = (18190, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h6oh + ic4h8 <=> ic4h7oh + ic4h7',
 "chemkinKinetics": """
ic4h6oh+ic4h8=ic4h7oh+ic4h7                         4.700e+02 3.300     19.840   
""",
 "rmgPyKinetics": Arrhenius(A=(470, 'cm^3/(mol*s)'), n=3.3, Ea=(19840, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h6oh + h <=> ic4h7oh',
 "chemkinKinetics": """
ic4h6oh+h=ic4h7oh                                   1.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h6oh + h2o2 <=> ic4h7oh + ho2',
 "chemkinKinetics": """
ic4h6oh+h2o2=ic4h7oh+ho2                            7.830e+05 2.050     13.580   
""",
 "rmgPyKinetics": Arrhenius(
    A = (783000, 'cm^3/(mol*s)'),
    n = 2.05,
    Ea = (13580, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h4-a + ch2oh <=> ic4h6oh',
 "chemkinKinetics": """
c3h4-a+ch2oh=ic4h6oh                                1.000e+11 0.000     9.200    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h7o + o2 <=> ic3h5cho + ho2',
 "chemkinKinetics": """
ic4h7o+o2=ic3h5cho+ho2                              3.000e+10 0.000     1.649    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(1649, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h7o + ho2 <=> ic3h5cho + h2o2',
 "chemkinKinetics": """
ic4h7o+ho2=ic3h5cho+h2o2                            3.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h7o + ch3 <=> ic3h5cho + ch4',
 "chemkinKinetics": """
ic4h7o+ch3=ic3h5cho+ch4                             2.400e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h7o + o <=> ic3h5cho + oh',
 "chemkinKinetics": """
ic4h7o+o=ic3h5cho+oh                                6.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h7o + oh <=> ic3h5cho + h2o',
 "chemkinKinetics": """
ic4h7o+oh=ic3h5cho+h2o                              1.810e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h7o + h <=> ic3h5cho + h2',
 "chemkinKinetics": """
ic4h7o+h=ic3h5cho+h2                                1.990e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.99e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic3h5cho + oh <=> ic3h5co + h2o',
 "chemkinKinetics": """
ic3h5cho+oh=ic3h5co+h2o                             2.690e+10 0.760     -0.340   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.69e+10, 'cm^3/(mol*s)'),
    n = 0.76,
    Ea = (-340, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h5cho + ho2 <=> ic3h5co + h2o2',
 "chemkinKinetics": """
ic3h5cho+ho2=ic3h5co+h2o2                           1.000e+12 0.000     11.920   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h5cho + ch3 <=> ic3h5co + ch4',
 "chemkinKinetics": """
ic3h5cho+ch3=ic3h5co+ch4                            3.980e+12 0.000     8.700    
""",
 "rmgPyKinetics": Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(8700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h5cho + o <=> ic3h5co + oh',
 "chemkinKinetics": """
ic3h5cho+o=ic3h5co+oh                               7.180e+12 0.000     1.389    
""",
 "rmgPyKinetics": Arrhenius(A=(7.18e+12, 'cm^3/(mol*s)'), n=0, Ea=(1389, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h5cho + o2 <=> ic3h5co + ho2',
 "chemkinKinetics": """
ic3h5cho+o2=ic3h5co+ho2                             2.000e+13 0.000     40.700   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(40700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h5cho + h <=> ic3h5co + h2',
 "chemkinKinetics": """
ic3h5cho+h=ic3h5co+h2                               2.600e+12 0.000     2.600    
""",
 "rmgPyKinetics": Arrhenius(A=(2.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h5co <=> c3h5-t + co',
 "chemkinKinetics": """
ic3h5co=c3h5-t+co                                   1.278e+20 -1.890    34.460   
""",
 "rmgPyKinetics": Arrhenius(A=(1.278e+20, 's^-1'), n=-1.89, Ea=(34460, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'tc3h6ocho + oh <=> tc3h6cho + ho2',
 "chemkinKinetics": """
tc3h6ocho+oh=tc3h6cho+ho2                           2.018e+17 -1.200    21.010   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.018e+17, 'cm^3/(mol*s)'),
    n = -1.2,
    Ea = (21010, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc3h6ocho <=> ch3coch3 + hco',
 "chemkinKinetics": """
tc3h6ocho=ch3coch3+hco                              3.980e+13 0.000     9.700    
""",
 "rmgPyKinetics": Arrhenius(A=(3.98e+13, 's^-1'), n=0, Ea=(9700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h5cho + h <=> tc3h6cho',
 "chemkinKinetics": """
ic3h5cho+h=tc3h6cho                                 1.300e+13 0.000     1.200    
""",
 "rmgPyKinetics": Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(1200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h6co + h <=> tc3h6cho',
 "chemkinKinetics": """
ic3h6co+h=tc3h6cho                                  1.300e+13 0.000     4.800    
""",
 "rmgPyKinetics": Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(4800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'tc3h6cho + h2 <=> ic3h7cho + h',
 "chemkinKinetics": """
tc3h6cho+h2=ic3h7cho+h                              2.160e+05 2.380     18.990   
""",
 "rmgPyKinetics": Arrhenius(
    A = (216000, 'cm^3/(mol*s)'),
    n = 2.38,
    Ea = (18990, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h7o + oh <=> ic4h7ooh',
 "chemkinKinetics": """
ic4h7o+oh=ic4h7ooh                                  1.000e+11 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h7o + h <=> ic4h7oh',
 "chemkinKinetics": """
ic4h7o+h=ic4h7oh                                    4.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h7oh + h <=> ic4h8oh',
 "chemkinKinetics": """
ic4h7oh+h=ic4h8oh                                   1.000e+13 0.000     1.200    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(1200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h7o + h2 <=> ic4h7oh + h',
 "chemkinKinetics": """
ic4h7o+h2=ic4h7oh+h                                 9.050e+06 2.000     17.830   
""",
 "rmgPyKinetics": Arrhenius(A=(9.05e+06, 'cm^3/(mol*s)'), n=2, Ea=(17830, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h7 + oh <=> ic4h7oh',
 "chemkinKinetics": """
ic4h7+oh=ic4h7oh                                    3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h7oh + hco <=> ic4h7o + ch2o',
 "chemkinKinetics": """
ic4h7oh+hco=ic4h7o+ch2o                             3.020e+11 0.000     18.160   
""",
 "rmgPyKinetics": Arrhenius(A=(3.02e+11, 'cm^3/(mol*s)'), n=0, Ea=(18160, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc3h6cho + ch2o <=> ic3h7cho + hco',
 "chemkinKinetics": """
tc3h6cho+ch2o=ic3h7cho+hco                          2.520e+08 1.900     18.190   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.52e+08, 'cm^3/(mol*s)'),
    n = 1.9,
    Ea = (18190, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc3h6cho + ic4h8 <=> ic3h7cho + ic4h7',
 "chemkinKinetics": """
tc3h6cho+ic4h8=ic3h7cho+ic4h7                       4.700e+02 3.300     19.840   
""",
 "rmgPyKinetics": Arrhenius(A=(470, 'cm^3/(mol*s)'), n=3.3, Ea=(19840, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic3h6co + oh <=> ic3h7 + co2',
 "chemkinKinetics": """
ic3h6co+oh=ic3h7+co2                                1.730e+12 0.000     -1.010   
""",
 "rmgPyKinetics": Arrhenius(A=(1.73e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'tc3h6cho + oh <=> tc3h6ohcho',
 "chemkinKinetics": """
tc3h6cho+oh=tc3h6ohcho                              5.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'tc3h6oh + hco <=> tc3h6ohcho',
 "chemkinKinetics": """
tc3h6oh+hco=tc3h6ohcho                              1.810e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3coch3 + h <=> tc3h6oh',
 "chemkinKinetics": """
ch3coch3+h=tc3h6oh                                  8.000e+12 0.000     9.500    
""",
 "rmgPyKinetics": Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h5oh + h <=> tc3h6oh',
 "chemkinKinetics": """
ic3h5oh+h=tc3h6oh                                   6.250e+11 0.510     4.020    
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.25e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (4020, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h5-t + oh <=> ic3h5oh',
 "chemkinKinetics": """
c3h5-t+oh=ic3h5oh                                   5.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'tc3h6cho + o2 <=> tc3h6o2cho',
 "chemkinKinetics": """
tc3h6cho+o2=tc3h6o2cho                              1.990e+17 -2.100    0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.99e+17, 'cm^3/(mol*s)'), n=-2.1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'tc3h6o2cho <=> ic3h5o2hcho',
 "chemkinKinetics": """
tc3h6o2cho=ic3h5o2hcho                              6.000e+11 0.000     29.880   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(29880, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'tc3h6o2cho <=> tc3h6o2hco',
 "chemkinKinetics": """
tc3h6o2cho=tc3h6o2hco                               1.000e+11 0.000     25.750   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25750, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic3h5cho + ho2 <=> ic3h5o2hcho',
 "chemkinKinetics": """
ic3h5cho+ho2=ic3h5o2hcho                            2.230e+11 0.000     10.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.23e+11, 'cm^3/(mol*s)'), n=0, Ea=(10600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'tc3h6o2hco => ch3coch3 + co + oh',
 "chemkinKinetics": """
tc3h6o2hco=>ch3coch3+co+oh                          4.244e+18 -1.430    4.800    
""",
 "rmgPyKinetics": Arrhenius(A=(4.244e+18, 's^-1'), n=-1.43, Ea=(4800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'tc3h6oh + o2 <=> ch3coch3 + ho2',
 "chemkinKinetics": """
tc3h6oh+o2=ch3coch3+ho2                             2.230e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.23e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic3h6co + oh <=> tc3h6oh + co',
 "chemkinKinetics": """
ic3h6co+oh=tc3h6oh+co                               2.000e+12 0.000     -1.010   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'tc3h6cho + ho2 <=> ic3h7cho + o2',
 "chemkinKinetics": """
tc3h6cho+ho2=ic3h7cho+o2                            3.675e+12 0.000     1.310    
""",
 "rmgPyKinetics": Arrhenius(A=(3.675e+12, 'cm^3/(mol*s)'), n=0, Ea=(1310, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc3h6cho + ch3 <=> ic3h5cho + ch4',
 "chemkinKinetics": """
tc3h6cho+ch3=ic3h5cho+ch4                           3.010e+12 -0.320    -0.131   
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.01e+12, 'cm^3/(mol*s)'),
    n = -0.32,
    Ea = (-131, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'tc4h8cho <=> ic3h5cho + ch3',
 "chemkinKinetics": """
tc4h8cho=ic3h5cho+ch3                               1.000e+13 0.000     26.290   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(26290, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'tc4h8cho <=> ic4h8 + hco',
 "chemkinKinetics": """
tc4h8cho=ic4h8+hco                                  8.520e+12 0.000     20.090   
""",
 "rmgPyKinetics": Arrhenius(A=(8.52e+12, 's^-1'), n=0, Ea=(20090, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'tc4h8cho + o2 <=> o2c4h8cho',
 "chemkinKinetics": """
tc4h8cho+o2=o2c4h8cho                               2.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'o2c4h8cho <=> o2hc4h8co',
 "chemkinKinetics": """
o2c4h8cho=o2hc4h8co                                 2.160e+11 0.000     15.360   
""",
 "rmgPyKinetics": Arrhenius(A=(2.16e+11, 's^-1'), n=0, Ea=(15360, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h8o2h-t + co <=> o2hc4h8co',
 "chemkinKinetics": """
ic4h8o2h-t+co=o2hc4h8co                             1.500e+11 0.000     4.809    
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4809, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7o + ic4h8 <=> ic4h7oh + ic4h7',
 "chemkinKinetics": """
ic4h7o+ic4h8=ic4h7oh+ic4h7                          2.700e+11 0.000     4.000    
""",
 "rmgPyKinetics": Arrhenius(A=(2.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h6oh + ho2 => ch2cch2oh + ch2o + oh',
 "chemkinKinetics": """
ic4h6oh+ho2=>ch2cch2oh+ch2o+oh                      1.446e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.446e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h8 + ch2cch2oh <=> ic4h7 + c3h5oh',
 "chemkinKinetics": """
ic4h8+ch2cch2oh=ic4h7+c3h5oh                        7.940e+11 0.000     20.500   
""",
 "rmgPyKinetics": Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2cch2oh + h2o2 <=> c3h5oh + ho2',
 "chemkinKinetics": """
ch2cch2oh+h2o2=c3h5oh+ho2                           3.010e+09 0.000     2.583    
""",
 "rmgPyKinetics": Arrhenius(A=(3.01e+09, 'cm^3/(mol*s)'), n=0, Ea=(2583, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h5oh + oh <=> ch2cch2oh + h2o',
 "chemkinKinetics": """
c3h5oh+oh=ch2cch2oh+h2o                             5.060e+12 0.000     5.960    
""",
 "rmgPyKinetics": Arrhenius(A=(5.06e+12, 'cm^3/(mol*s)'), n=0, Ea=(5960, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h5oh + h <=> ch2cch2oh + h2',
 "chemkinKinetics": """
c3h5oh+h=ch2cch2oh+h2                               3.900e+05 2.500     5.821    
""",
 "rmgPyKinetics": Arrhenius(A=(390000, 'cm^3/(mol*s)'), n=2.5, Ea=(5821, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h5oh + o2 <=> ch2cch2oh + ho2',
 "chemkinKinetics": """
c3h5oh+o2=ch2cch2oh+ho2                             4.000e+13 0.000     60.690   
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(60690, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h5oh + ch3 <=> ch2cch2oh + ch4',
 "chemkinKinetics": """
c3h5oh+ch3=ch2cch2oh+ch4                            2.400e+11 0.000     8.030    
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+11, 'cm^3/(mol*s)'), n=0, Ea=(8030, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ch2cch2oh + ch3 <=> ic4h7oh',
 "chemkinKinetics": """
ch2cch2oh+ch3=ic4h7oh                               3.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch2cch2oh + h <=> c3h5oh',
 "chemkinKinetics": """
ch2cch2oh+h=c3h5oh                                  1.000e+14 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch2cch2oh + o2 => ch2oh + co + ch2o',
 "chemkinKinetics": """
ch2cch2oh+o2=>ch2oh+co+ch2o                         4.335e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.335e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch2cch2oh <=> c2h2 + ch2oh',
 "chemkinKinetics": """
ch2cch2oh=c2h2+ch2oh                                2.163e+40 -8.310    45.110   
""",
 "rmgPyKinetics": Arrhenius(A=(2.163e+40, 's^-1'), n=-8.31, Ea=(45110, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h4-a + oh <=> ch2cch2oh',
 "chemkinKinetics": """
c3h4-a+oh=ch2cch2oh                                 8.500e+12 0.000     2.000    
""",
 "rmgPyKinetics": Arrhenius(A=(8.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'nc4h9oh <=> ch3 + c3h6oh',
 "chemkinKinetics": """
nc4h9oh(+M)=ch3+c3h6oh(+M)                          3.790e+24 -2.230    88.070   

    LOW/ 1.782e+60 -12.280   83.980   /
    TROE/ 2.352e-01 724       5e+09     5e+09    /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(3.79e+24, 's^-1'), n=-2.23, Ea=(88070, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.782e+60, 'cm^3/(mol*s)'),
        n = -12.28,
        Ea = (83980, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.2352,
    T3 = (724, 'K'),
    T1 = (5e+09, 'K'),
    T2 = (5e+09, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'nc4h9oh <=> c2h5 + pc2h4oh',
 "chemkinKinetics": """
nc4h9oh(+M)=c2h5+pc2h4oh(+M)                        5.530e+24 -2.230    89.010   

    LOW/ 6.632e+59 -12.130   84.720   /
    TROE/ 2.438e-01 744       5e+09     5e+09    /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(5.53e+24, 's^-1'), n=-2.23, Ea=(89010, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (6.632e+59, 'cm^3/(mol*s)'),
        n = -12.13,
        Ea = (84720, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.2438,
    T3 = (744.06, 'K'),
    T1 = (5e+09, 'K'),
    T2 = (5e+09, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'nc4h9oh <=> nc3h7 + ch2oh',
 "chemkinKinetics": """
nc4h9oh(+M)=nc3h7+ch2oh(+M)                         3.020e+23 -1.880    85.710   

    LOW/ 1.416e+59 -11.930   83.980   /
    TROE/ 7.646e-01 8.34e+09  725       8.21e+09 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(3.02e+23, 's^-1'), n=-1.88, Ea=(85710, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.416e+59, 'cm^3/(mol*s)'),
        n = -11.93,
        Ea = (83980, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.7646,
    T3 = (8.344e+09, 'K'),
    T1 = (724.8, 'K'),
    T2 = (8.214e+09, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'nc4h9oh <=> oh + pc4h9',
 "chemkinKinetics": """
nc4h9oh(+M)=oh+pc4h9(+M)                            6.330e+20 -1.370    94.930   

    LOW/ 6.902e+51 -10.210   89.200   /
    TROE/ 7.030e-01 9.88e+09  635       1.79e+09 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(6.33e+20, 's^-1'), n=-1.37, Ea=(94930, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (6.902e+51, 'cm^3/(mol*s)'),
        n = -10.21,
        Ea = (89200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.703,
    T3 = (9.882e+09, 'K'),
    T1 = (634.68, 'K'),
    T2 = (1.786e+09, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'nc4h9oh <=> h + pc4h9o',
 "chemkinKinetics": """
nc4h9oh(+M)=h+pc4h9o(+M)                            6.040e+14 0.100     103.800  

    LOW/ 2.408e+39 -7.030    95.960   /
    TROE/ 3.865e-01 565       4.44e+09  6.71e+09 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(6.04e+14, 's^-1'), n=0.1, Ea=(103800, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (2.408e+39, 'cm^3/(mol*s)'),
        n = -7.03,
        Ea = (95960, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.3865,
    T3 = (564.91, 'K'),
    T1 = (4.438e+09, 'K'),
    T2 = (6.71e+09, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'nc4h9oh <=> c4h8-1 + h2o',
 "chemkinKinetics": """
nc4h9oh(+M)=c4h8-1+h2o(+M)                          3.520e+13 0.000     67.230   

    LOW/ 1.690e+75 -17.040   64.750   /
    TROE/ 8.000e-02 1         9.92e+09  9.92e+09 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(3.52e+13, 's^-1'), n=0, Ea=(67230, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.69e+75, 'cm^3/(mol*s)'),
        n = -17.04,
        Ea = (64750, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.08,
    T3 = (1, 'K'),
    T1 = (9.924e+09, 'K'),
    T2 = (9.924e+09, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['1,3_Insertion_ROR',  ],
},

{
 "reaction": 'h + c4h8oh-1 <=> nc4h9oh',
 "chemkinKinetics": """
h+c4h8oh-1=nc4h9oh                                  4.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'h + c4h8oh-2 <=> nc4h9oh',
 "chemkinKinetics": """
h+c4h8oh-2=nc4h9oh                                  4.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'h + c4h8oh-3 <=> nc4h9oh',
 "chemkinKinetics": """
h+c4h8oh-3=nc4h9oh                                  4.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'h + c4h8oh-4 <=> nc4h9oh',
 "chemkinKinetics": """
h+c4h8oh-4=nc4h9oh                                  4.000e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'nc4h9oh + h <=> c4h8oh-4 + h2',
 "chemkinKinetics": """
nc4h9oh+h=c4h8oh-4+h2                               6.660e+05 2.540     6.756    
""",
 "rmgPyKinetics": Arrhenius(A=(666000, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + h <=> c4h8oh-3 + h2',
 "chemkinKinetics": """
nc4h9oh+h=c4h8oh-3+h2                               1.300e+06 2.400     4.471    
""",
 "rmgPyKinetics": Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + h <=> c4h8oh-2 + h2',
 "chemkinKinetics": """
nc4h9oh+h=c4h8oh-2+h2                               1.080e+05 2.690     4.440    
""",
 "rmgPyKinetics": Arrhenius(A=(108000, 'cm^3/(mol*s)'), n=2.69, Ea=(4440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + h <=> c4h8oh-1 + h2',
 "chemkinKinetics": """
nc4h9oh+h=c4h8oh-1+h2                               8.789e+04 2.680     2.915    
""",
 "rmgPyKinetics": Arrhenius(A=(87890, 'cm^3/(mol*s)'), n=2.68, Ea=(2915, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + h <=> pc4h9o + h2',
 "chemkinKinetics": """
nc4h9oh+h=pc4h9o+h2                                 9.450e+02 3.140     8.701    
""",
 "rmgPyKinetics": Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + oh <=> c4h8oh-4 + h2o',
 "chemkinKinetics": """
nc4h9oh+oh=c4h8oh-4+h2o                             5.280e+09 0.970     1.586    
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.28e+09, 'cm^3/(mol*s)'),
    n = 0.97,
    Ea = (1586, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + oh <=> c4h8oh-3 + h2o',
 "chemkinKinetics": """
nc4h9oh+oh=c4h8oh-3+h2o                             1.141e+03 2.870     -2.926   
""",
 "rmgPyKinetics": Arrhenius(A=(1141, 'cm^3/(mol*s)'), n=2.87, Ea=(-2926, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + oh <=> c4h8oh-2 + h2o',
 "chemkinKinetics": """
nc4h9oh+oh=c4h8oh-2+h2o                             1.540e+00 3.700     -3.736   
""",
 "rmgPyKinetics": Arrhenius(A=(1.54, 'cm^3/(mol*s)'), n=3.7, Ea=(-3736, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + oh <=> c4h8oh-1 + h2o',
 "chemkinKinetics": """
nc4h9oh+oh=c4h8oh-1+h2o                             3.610e+03 2.890     -2.291   
""",
 "rmgPyKinetics": Arrhenius(A=(3610, 'cm^3/(mol*s)'), n=2.89, Ea=(-2291, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + oh <=> pc4h9o + h2o',
 "chemkinKinetics": """
nc4h9oh+oh=pc4h9o+h2o                               5.880e+02 2.820     -0.585   
""",
 "rmgPyKinetics": Arrhenius(A=(588, 'cm^3/(mol*s)'), n=2.82, Ea=(-585, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + o <=> c4h8oh-4 + oh',
 "chemkinKinetics": """
nc4h9oh+o=c4h8oh-4+oh                               9.810e+05 2.430     4.750    
""",
 "rmgPyKinetics": Arrhenius(A=(981000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + o <=> c4h8oh-3 + oh',
 "chemkinKinetics": """
nc4h9oh+o=c4h8oh-3+oh                               5.520e+05 2.450     2.830    
""",
 "rmgPyKinetics": Arrhenius(A=(552000, 'cm^3/(mol*s)'), n=2.45, Ea=(2830, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + o <=> c4h8oh-2 + oh',
 "chemkinKinetics": """
nc4h9oh+o=c4h8oh-2+oh                               1.440e+05 2.610     3.029    
""",
 "rmgPyKinetics": Arrhenius(A=(144000, 'cm^3/(mol*s)'), n=2.61, Ea=(3029, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + o <=> c4h8oh-1 + oh',
 "chemkinKinetics": """
nc4h9oh+o=c4h8oh-1+oh                               1.450e+05 2.470     0.876    
""",
 "rmgPyKinetics": Arrhenius(A=(145000, 'cm^3/(mol*s)'), n=2.47, Ea=(876, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + o <=> pc4h9o + oh',
 "chemkinKinetics": """
nc4h9oh+o=pc4h9o+oh                                 1.460e-03 4.730     1.727    
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.00146, 'cm^3/(mol*s)'),
    n = 4.73,
    Ea = (1727, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + o2 <=> ho2 + c4h8oh-4',
 "chemkinKinetics": """
nc4h9oh+o2=ho2+c4h8oh-4                             3.000e+13 0.000     52.340   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + o2 <=> ho2 + c4h8oh-3',
 "chemkinKinetics": """
nc4h9oh+o2=ho2+c4h8oh-3                             2.000e+13 0.000     49.800   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + o2 <=> ho2 + c4h8oh-2',
 "chemkinKinetics": """
nc4h9oh+o2=ho2+c4h8oh-2                             2.000e+13 0.000     49.800   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + o2 <=> ho2 + c4h8oh-1',
 "chemkinKinetics": """
nc4h9oh+o2=ho2+c4h8oh-1                             2.000e+13 0.000     46.800   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(46800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + o2 <=> ho2 + pc4h9o',
 "chemkinKinetics": """
nc4h9oh+o2=ho2+pc4h9o                               1.000e+13 0.000     56.340   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(56340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ho2 <=> c4h8oh-4 + h2o2',
 "chemkinKinetics": """
nc4h9oh+ho2=c4h8oh-4+h2o2                           8.800e-02 4.310     17.270   
""",
 "rmgPyKinetics": Arrhenius(A=(0.088, 'cm^3/(mol*s)'), n=4.31, Ea=(17270, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ho2 <=> c4h8oh-3 + h2o2',
 "chemkinKinetics": """
nc4h9oh+ho2=c4h8oh-3+h2o2                           2.760e-04 4.760     11.850   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.000276, 'cm^3/(mol*s)'),
    n = 4.76,
    Ea = (11850, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ho2 <=> c4h8oh-2 + h2o2',
 "chemkinKinetics": """
nc4h9oh+ho2=c4h8oh-2+h2o2                           7.510e-03 4.520     14.710   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.00751, 'cm^3/(mol*s)'),
    n = 4.52,
    Ea = (14710, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ho2 <=> c4h8oh-1 + h2o2',
 "chemkinKinetics": """
nc4h9oh+ho2=c4h8oh-1+h2o2                           3.500e-05 5.260     8.268    
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.5e-05, 'cm^3/(mol*s)'),
    n = 5.26,
    Ea = (8268, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ho2 <=> pc4h9o + h2o2',
 "chemkinKinetics": """
nc4h9oh+ho2=pc4h9o+h2o2                             6.470e-07 5.300     10.530   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.47e-07, 'cm^3/(mol*s)'),
    n = 5.3,
    Ea = (10530, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3 <=> c4h8oh-4 + ch4',
 "chemkinKinetics": """
nc4h9oh+ch3=c4h8oh-4+ch4                            4.530e-01 3.650     7.154    
""",
 "rmgPyKinetics": Arrhenius(A=(0.453, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3 <=> c4h8oh-3 + ch4',
 "chemkinKinetics": """
nc4h9oh+ch3=c4h8oh-3+ch4                            1.510e+00 3.460     5.481    
""",
 "rmgPyKinetics": Arrhenius(A=(1.51, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3 <=> c4h8oh-2 + ch4',
 "chemkinKinetics": """
nc4h9oh+ch3=c4h8oh-2+ch4                            8.020e+00 3.230     6.461    
""",
 "rmgPyKinetics": Arrhenius(A=(8.02, 'cm^3/(mol*s)'), n=3.23, Ea=(6461, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3 <=> c4h8oh-1 + ch4',
 "chemkinKinetics": """
nc4h9oh+ch3=c4h8oh-1+ch4                            1.993e+01 3.370     7.634    
""",
 "rmgPyKinetics": Arrhenius(A=(19.93, 'cm^3/(mol*s)'), n=3.37, Ea=(7634, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3 <=> pc4h9o + ch4',
 "chemkinKinetics": """
nc4h9oh+ch3=pc4h9o+ch4                              1.020e+00 3.570     8.221    
""",
 "rmgPyKinetics": Arrhenius(A=(1.02, 'cm^3/(mol*s)'), n=3.57, Ea=(8221, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + hco <=> c4h8oh-4 + ch2o',
 "chemkinKinetics": """
nc4h9oh+hco=c4h8oh-4+ch2o                           1.020e+05 2.500     18.440   
""",
 "rmgPyKinetics": Arrhenius(A=(102000, 'cm^3/(mol*s)'), n=2.5, Ea=(18440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + hco <=> c4h8oh-3 + ch2o',
 "chemkinKinetics": """
nc4h9oh+hco=c4h8oh-3+ch2o                           1.090e+07 1.900     17.010   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.09e+07, 'cm^3/(mol*s)'),
    n = 1.9,
    Ea = (17010, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + hco <=> c4h8oh-2 + ch2o',
 "chemkinKinetics": """
nc4h9oh+hco=c4h8oh-2+ch2o                           5.160e+05 2.250     16.760   
""",
 "rmgPyKinetics": Arrhenius(
    A = (516000, 'cm^3/(mol*s)'),
    n = 2.25,
    Ea = (16760, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + hco <=> c4h8oh-1 + ch2o',
 "chemkinKinetics": """
nc4h9oh+hco=c4h8oh-1+ch2o                           1.000e+07 1.900     17.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=1.9, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + hco <=> pc4h9o + ch2o',
 "chemkinKinetics": """
nc4h9oh+hco=pc4h9o+ch2o                             3.400e+04 2.500     13.500   
""",
 "rmgPyKinetics": Arrhenius(A=(34000, 'cm^3/(mol*s)'), n=2.5, Ea=(13500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch2oh <=> c4h8oh-4 + ch3oh',
 "chemkinKinetics": """
nc4h9oh+ch2oh=c4h8oh-4+ch3oh                        1.010e+02 2.950     13.970   
""",
 "rmgPyKinetics": Arrhenius(A=(101, 'cm^3/(mol*s)'), n=2.95, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch2oh <=> c4h8oh-3 + ch3oh',
 "chemkinKinetics": """
nc4h9oh+ch2oh=c4h8oh-3+ch3oh                        6.020e+01 2.950     11.980   
""",
 "rmgPyKinetics": Arrhenius(A=(60.2, 'cm^3/(mol*s)'), n=2.95, Ea=(11980, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch2oh <=> c4h8oh-2 + ch3oh',
 "chemkinKinetics": """
nc4h9oh+ch2oh=c4h8oh-2+ch3oh                        1.530e+01 3.110     12.210   
""",
 "rmgPyKinetics": Arrhenius(A=(15.3, 'cm^3/(mol*s)'), n=3.11, Ea=(12210, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch2oh <=> c4h8oh-1 + ch3oh',
 "chemkinKinetics": """
nc4h9oh+ch2oh=c4h8oh-1+ch3oh                        6.000e+01 2.950     12.000   
""",
 "rmgPyKinetics": Arrhenius(A=(60, 'cm^3/(mol*s)'), n=2.95, Ea=(12000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch2oh <=> pc4h9o + ch3oh',
 "chemkinKinetics": """
nc4h9oh+ch2oh=pc4h9o+ch3oh                          1.200e+02 2.760     10.800   
""",
 "rmgPyKinetics": Arrhenius(A=(120, 'cm^3/(mol*s)'), n=2.76, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3o <=> c4h8oh-4 + ch3oh',
 "chemkinKinetics": """
nc4h9oh+ch3o=c4h8oh-4+ch3oh                         2.170e+11 0.000     6.458    
""",
 "rmgPyKinetics": Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3o <=> c4h8oh-3 + ch3oh',
 "chemkinKinetics": """
nc4h9oh+ch3o=c4h8oh-3+ch3oh                         1.450e+11 0.000     4.571    
""",
 "rmgPyKinetics": Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(4571, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3o <=> c4h8oh-2 + ch3oh',
 "chemkinKinetics": """
nc4h9oh+ch3o=c4h8oh-2+ch3oh                         3.020e+10 0.180     4.703    
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.02e+10, 'cm^3/(mol*s)'),
    n = 0.18,
    Ea = (4703, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3o <=> c4h8oh-1 + ch3oh',
 "chemkinKinetics": """
nc4h9oh+ch3o=c4h8oh-1+ch3oh                         1.500e+11 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3o <=> pc4h9o + ch3oh',
 "chemkinKinetics": """
nc4h9oh+ch3o=pc4h9o+ch3oh                           2.300e+10 0.000     2.900    
""",
 "rmgPyKinetics": Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3o2 <=> c4h8oh-4 + ch3o2h',
 "chemkinKinetics": """
nc4h9oh+ch3o2=c4h8oh-4+ch3o2h                       2.380e+04 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3o2 <=> c4h8oh-3 + ch3o2h',
 "chemkinKinetics": """
nc4h9oh+ch3o2=c4h8oh-3+ch3o2h                       9.640e+03 2.600     13.910   
""",
 "rmgPyKinetics": Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3o2 <=> c4h8oh-2 + ch3o2h',
 "chemkinKinetics": """
nc4h9oh+ch3o2=c4h8oh-2+ch3o2h                       1.580e+03 2.810     14.050   
""",
 "rmgPyKinetics": Arrhenius(A=(1580, 'cm^3/(mol*s)'), n=2.81, Ea=(14050, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3o2 <=> c4h8oh-1 + ch3o2h',
 "chemkinKinetics": """
nc4h9oh+ch3o2=c4h8oh-1+ch3o2h                       3.000e+12 0.000     17.500   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(17500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + ch3o2 <=> pc4h9o + ch3o2h',
 "chemkinKinetics": """
nc4h9oh+ch3o2=pc4h9o+ch3o2h                         1.500e+12 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + c2h5 <=> c4h8oh-4 + c2h6',
 "chemkinKinetics": """
nc4h9oh+c2h5=c4h8oh-4+c2h6                          5.010e+10 0.000     13.400   
""",
 "rmgPyKinetics": Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + c2h5 <=> c4h8oh-3 + c2h6',
 "chemkinKinetics": """
nc4h9oh+c2h5=c4h8oh-3+c2h6                          5.010e+10 0.000     10.400   
""",
 "rmgPyKinetics": Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + c2h5 <=> c4h8oh-2 + c2h6',
 "chemkinKinetics": """
nc4h9oh+c2h5=c4h8oh-2+c2h6                          5.010e+10 0.000     10.400   
""",
 "rmgPyKinetics": Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + c2h5 <=> c4h8oh-1 + c2h6',
 "chemkinKinetics": """
nc4h9oh+c2h5=c4h8oh-1+c2h6                          2.010e+11 0.000     7.900    
""",
 "rmgPyKinetics": Arrhenius(A=(2.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'nc4h9oh + c2h5 <=> pc4h9o + c2h6',
 "chemkinKinetics": """
nc4h9oh+c2h5=pc4h9o+c2h6                            1.670e+10 0.000     13.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1.67e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c2h3oh + c2h5 <=> c4h8oh-1',
 "chemkinKinetics": """
c2h3oh+c2h5=c4h8oh-1                                8.800e+03 2.480     6.130    
""",
 "rmgPyKinetics": Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'nc3h7cho + h <=> c4h8oh-1',
 "chemkinKinetics": """
nc3h7cho+h=c4h8oh-1                                 8.000e+12 0.000     9.500    
""",
 "rmgPyKinetics": Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh1-1 + h <=> c4h8oh-1',
 "chemkinKinetics": """
c4h7oh1-1+h=c4h8oh-1                                2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h8-1 + oh <=> c4h8oh-2',
 "chemkinKinetics": """
c4h8-1+oh=c4h8oh-2                                  9.930e+11 0.000     -0.960   
""",
 "rmgPyKinetics": Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h5oh + ch3 <=> c4h8oh-2',
 "chemkinKinetics": """
c3h5oh+ch3=c4h8oh-2                                 1.760e+04 2.480     6.130    
""",
 "rmgPyKinetics": Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'h + c4h7oh2-1 <=> c4h8oh-2',
 "chemkinKinetics": """
h+c4h7oh2-1=c4h8oh-2                                2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'h + c4h7oh1-1 <=> c4h8oh-2',
 "chemkinKinetics": """
h+c4h7oh1-1=c4h8oh-2                                2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h6 + ch2oh <=> c4h8oh-3',
 "chemkinKinetics": """
c3h6+ch2oh=c4h8oh-3                                 8.800e+03 2.480     6.130    
""",
 "rmgPyKinetics": Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh1-4 + h <=> c4h8oh-3',
 "chemkinKinetics": """
c4h7oh1-4+h=c4h8oh-3                                4.240e+11 0.510     1.230    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.24e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (1230, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh2-1 + h <=> c4h8oh-3',
 "chemkinKinetics": """
c4h7oh2-1+h=c4h8oh-3                                2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h4 + pc2h4oh <=> c4h8oh-4',
 "chemkinKinetics": """
c2h4+pc2h4oh=c4h8oh-4                               8.800e+03 2.480     6.130    
""",
 "rmgPyKinetics": Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond', '1,3_Insertion_ROR',  ],
},

{
 "reaction": 'h + c4h7oh1-4 <=> c4h8oh-4',
 "chemkinKinetics": """
h+c4h7oh1-4=c4h8oh-4                                2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'h + nc3h7cho <=> pc4h9o',
 "chemkinKinetics": """
h+nc3h7cho=pc4h9o                                   1.000e+12 0.000     5.860    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'pc4h9o <=> c4h8oh-4',
 "chemkinKinetics": """
pc4h9o=c4h8oh-4                                     1.320e-01 3.632     2.689    
""",
 "rmgPyKinetics": Arrhenius(A=(0.132, 's^-1'), n=3.632, Ea=(2689, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'pc4h9o <=> c4h8oh-3',
 "chemkinKinetics": """
pc4h9o=c4h8oh-3                                     5.320e-10 6.204     6.710    
""",
 "rmgPyKinetics": Arrhenius(A=(5.32e-10, 's^-1'), n=6.204, Ea=(6710, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-4 <=> c4h8oh-1',
 "chemkinKinetics": """
c4h8oh-4=c4h8oh-1                                   3.300e-19 8.638     5.268    
""",
 "rmgPyKinetics": Arrhenius(A=(3.3e-19, 's^-1'), n=8.638, Ea=(5268, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h7oh1-3 + h <=> c4h6oh1-32 + h2',
 "chemkinKinetics": """
c4h7oh1-3+h=c4h6oh1-32+h2                           3.376e+05 2.360     0.207    
""",
 "rmgPyKinetics": Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-3 + o <=> c4h6oh1-32 + oh',
 "chemkinKinetics": """
c4h7oh1-3+o=c4h6oh1-32+oh                           9.590e+12 0.000     1.967    
""",
 "rmgPyKinetics": Arrhenius(A=(9.59e+12, 'cm^3/(mol*s)'), n=0, Ea=(1967, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-3 + oh <=> c4h6oh1-32 + h2o',
 "chemkinKinetics": """
c4h7oh1-3+oh=c4h6oh1-32+h2o                         2.764e+04 2.640     -1.919   
""",
 "rmgPyKinetics": Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-3 + ch3 <=> c4h6oh1-32 + ch4',
 "chemkinKinetics": """
c4h7oh1-3+ch3=c4h6oh1-32+ch4                        3.690e+00 3.310     4.002    
""",
 "rmgPyKinetics": Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-3 + ho2 <=> c4h6oh1-32 + h2o2',
 "chemkinKinetics": """
c4h7oh1-3+ho2=c4h6oh1-32+h2o2                       4.820e+03 2.550     10.530   
""",
 "rmgPyKinetics": Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-3 + ch3o2 <=> c4h6oh1-32 + ch3o2h',
 "chemkinKinetics": """
c4h7oh1-3+ch3o2=c4h6oh1-32+ch3o2h                   4.820e+03 2.550     10.530   
""",
 "rmgPyKinetics": Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-3 + ch3o <=> c4h6oh1-32 + ch3oh',
 "chemkinKinetics": """
c4h7oh1-3+ch3o=c4h6oh1-32+ch3oh                     4.000e+01 2.900     8.609    
""",
 "rmgPyKinetics": Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-1 + h <=> c4h6oh1-32 + h2',
 "chemkinKinetics": """
c4h7oh2-1+h=c4h6oh1-32+h2                           1.730e+05 2.500     2.492    
""",
 "rmgPyKinetics": Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-1 + o <=> c4h6oh1-32 + oh',
 "chemkinKinetics": """
c4h7oh2-1+o=c4h6oh1-32+oh                           5.240e+11 0.700     5.884    
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.24e+11, 'cm^3/(mol*s)'),
    n = 0.7,
    Ea = (5884, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-1 + oh <=> c4h6oh1-32 + h2o',
 "chemkinKinetics": """
c4h7oh2-1+oh=c4h6oh1-32+h2o                         3.120e+06 2.000     -0.298   
""",
 "rmgPyKinetics": Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-1 + ch3 <=> c4h6oh1-32 + ch4',
 "chemkinKinetics": """
c4h7oh2-1+ch3=c4h6oh1-32+ch4                        3.690e+00 3.310     4.002    
""",
 "rmgPyKinetics": Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-1 + ho2 <=> c4h6oh1-32 + h2o2',
 "chemkinKinetics": """
c4h7oh2-1+ho2=c4h6oh1-32+h2o2                       2.700e+04 2.500     12.340   
""",
 "rmgPyKinetics": Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-1 + ch3o2 <=> c4h6oh1-32 + ch3o2h',
 "chemkinKinetics": """
c4h7oh2-1+ch3o2=c4h6oh1-32+ch3o2h                   2.700e+04 2.500     12.340   
""",
 "rmgPyKinetics": Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-4 + h <=> c4h6oh1-32 + h2',
 "chemkinKinetics": """
c4h7oh1-4+h=c4h6oh1-32+h2                           3.376e+05 2.360     0.207    
""",
 "rmgPyKinetics": Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-4 + o <=> c4h6oh1-32 + oh',
 "chemkinKinetics": """
c4h7oh1-4+o=c4h6oh1-32+oh                           9.590e+12 0.000     1.967    
""",
 "rmgPyKinetics": Arrhenius(A=(9.59e+12, 'cm^3/(mol*s)'), n=0, Ea=(1967, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-4 + oh <=> c4h6oh1-32 + h2o',
 "chemkinKinetics": """
c4h7oh1-4+oh=c4h6oh1-32+h2o                         2.764e+04 2.640     -1.919   
""",
 "rmgPyKinetics": Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-4 + ch3 <=> c4h6oh1-32 + ch4',
 "chemkinKinetics": """
c4h7oh1-4+ch3=c4h6oh1-32+ch4                        3.690e+00 3.310     4.002    
""",
 "rmgPyKinetics": Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-4 + ho2 <=> c4h6oh1-32 + h2o2',
 "chemkinKinetics": """
c4h7oh1-4+ho2=c4h6oh1-32+h2o2                       4.820e+03 2.550     10.530   
""",
 "rmgPyKinetics": Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-4 + ch3o2 <=> c4h6oh1-32 + ch3o2h',
 "chemkinKinetics": """
c4h7oh1-4+ch3o2=c4h6oh1-32+ch3o2h                   4.820e+03 2.550     10.530   
""",
 "rmgPyKinetics": Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-4 + ch3o <=> c4h6oh1-32 + ch3oh',
 "chemkinKinetics": """
c4h7oh1-4+ch3o=c4h6oh1-32+ch3oh                     4.000e+01 2.900     8.609    
""",
 "rmgPyKinetics": Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-2 + h <=> c4h6oh1-32 + h2',
 "chemkinKinetics": """
c4h7oh2-2+h=c4h6oh1-32+h2                           1.730e+05 2.500     2.492    
""",
 "rmgPyKinetics": Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh2-2 + o <=> c4h6oh1-32 + oh',
 "chemkinKinetics": """
c4h7oh2-2+o=c4h6oh1-32+oh                           5.240e+11 0.700     5.884    
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.24e+11, 'cm^3/(mol*s)'),
    n = 0.7,
    Ea = (5884, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh2-2 + oh <=> c4h6oh1-32 + h2o',
 "chemkinKinetics": """
c4h7oh2-2+oh=c4h6oh1-32+h2o                         3.120e+06 2.000     -0.298   
""",
 "rmgPyKinetics": Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh2-2 + ch3 <=> c4h6oh1-32 + ch4',
 "chemkinKinetics": """
c4h7oh2-2+ch3=c4h6oh1-32+ch4                        3.690e+00 3.310     4.002    
""",
 "rmgPyKinetics": Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh2-2 + ho2 <=> c4h6oh1-32 + h2o2',
 "chemkinKinetics": """
c4h7oh2-2+ho2=c4h6oh1-32+h2o2                       2.700e+04 2.500     12.340   
""",
 "rmgPyKinetics": Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh2-2 + ch3o2 <=> c4h6oh1-32 + ch3o2h',
 "chemkinKinetics": """
c4h7oh2-2+ch3o2=c4h6oh1-32+ch3o2h                   2.700e+04 2.500     12.340   
""",
 "rmgPyKinetics": Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-2 + h <=> c4h6oh1-32 + h2',
 "chemkinKinetics": """
c4h7oh1-2+h=c4h6oh1-32+h2                           1.730e+05 2.500     2.492    
""",
 "rmgPyKinetics": Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-2 + o <=> c4h6oh1-32 + oh',
 "chemkinKinetics": """
c4h7oh1-2+o=c4h6oh1-32+oh                           5.240e+11 0.700     5.884    
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.24e+11, 'cm^3/(mol*s)'),
    n = 0.7,
    Ea = (5884, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-2 + oh <=> c4h6oh1-32 + h2o',
 "chemkinKinetics": """
c4h7oh1-2+oh=c4h6oh1-32+h2o                         3.120e+06 2.000     -0.298   
""",
 "rmgPyKinetics": Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-2 + ch3 <=> c4h6oh1-32 + ch4',
 "chemkinKinetics": """
c4h7oh1-2+ch3=c4h6oh1-32+ch4                        3.690e+00 3.310     4.002    
""",
 "rmgPyKinetics": Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-2 + ho2 <=> c4h6oh1-32 + h2o2',
 "chemkinKinetics": """
c4h7oh1-2+ho2=c4h6oh1-32+h2o2                       2.700e+04 2.500     12.340   
""",
 "rmgPyKinetics": Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-2 + ch3o2 <=> c4h6oh1-32 + ch3o2h',
 "chemkinKinetics": """
c4h7oh1-2+ch3o2=c4h6oh1-32+ch3o2h                   2.700e+04 2.500     12.340   
""",
 "rmgPyKinetics": Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-1 + h <=> c4h6oh1-13 + h2',
 "chemkinKinetics": """
c4h7oh1-1+h=c4h6oh1-13+h2                           3.376e+05 2.360     0.207    
""",
 "rmgPyKinetics": Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-1 + o <=> c4h6oh1-13 + oh',
 "chemkinKinetics": """
c4h7oh1-1+o=c4h6oh1-13+oh                           9.590e+12 0.000     1.967    
""",
 "rmgPyKinetics": Arrhenius(A=(9.59e+12, 'cm^3/(mol*s)'), n=0, Ea=(1967, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-1 + oh <=> c4h6oh1-13 + h2o',
 "chemkinKinetics": """
c4h7oh1-1+oh=c4h6oh1-13+h2o                         2.764e+04 2.640     -1.919   
""",
 "rmgPyKinetics": Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-1 + ch3 <=> c4h6oh1-13 + ch4',
 "chemkinKinetics": """
c4h7oh1-1+ch3=c4h6oh1-13+ch4                        3.690e+00 3.310     4.002    
""",
 "rmgPyKinetics": Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-1 + ho2 <=> c4h6oh1-13 + h2o2',
 "chemkinKinetics": """
c4h7oh1-1+ho2=c4h6oh1-13+h2o2                       4.820e+03 2.550     10.530   
""",
 "rmgPyKinetics": Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-1 + ch3o2 <=> c4h6oh1-13 + ch3o2h',
 "chemkinKinetics": """
c4h7oh1-1+ch3o2=c4h6oh1-13+ch3o2h                   4.820e+03 2.550     10.530   
""",
 "rmgPyKinetics": Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-1 + ch3o <=> c4h6oh1-13 + ch3oh',
 "chemkinKinetics": """
c4h7oh1-1+ch3o=c4h6oh1-13+ch3oh                     4.000e+01 2.900     8.609    
""",
 "rmgPyKinetics": Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-1 + ho2 <=> nc3h7cho + ho2',
 "chemkinKinetics": """
c4h7oh1-1+ho2=nc3h7cho+ho2                          1.490e+05 1.670     6.810    
""",
 "rmgPyKinetics": Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-2 + ho2 <=> c2h5coch3 + ho2',
 "chemkinKinetics": """
c4h7oh1-2+ho2=c2h5coch3+ho2                         1.490e+05 1.670     6.810    
""",
 "rmgPyKinetics": Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-2 + ho2 <=> c2h5coch3 + ho2',
 "chemkinKinetics": """
c4h7oh2-2+ho2=c2h5coch3+ho2                         1.490e+05 1.670     6.810    
""",
 "rmgPyKinetics": Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chchoh + ho2 <=> c2h5cho + ho2',
 "chemkinKinetics": """
ch3chchoh+ho2=c2h5cho+ho2                           1.490e+05 1.670     6.810    
""",
 "rmgPyKinetics": Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic3h5oh + ho2 <=> ch3coch3 + ho2',
 "chemkinKinetics": """
ic3h5oh+ho2=ch3coch3+ho2                            1.490e+05 1.670     6.810    
""",
 "rmgPyKinetics": Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c2h3oh + hocho <=> ch3cho + hocho',
 "chemkinKinetics": """
c2h3oh+hocho=ch3cho+hocho                           2.810e-02 3.286     -4.509   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.0281, 'cm^3/(mol*s)'),
    n = 3.286,
    Ea = (-4509, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV / 7.04E+04  1.209  556 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-1 + hocho <=> nc3h7cho + hocho',
 "chemkinKinetics": """
c4h7oh1-1+hocho=nc3h7cho+hocho                      2.810e-02 3.286     -4.509   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.0281, 'cm^3/(mol*s)'),
    n = 3.286,
    Ea = (-4509, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV / 7.04E+04  1.209  556 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-2 + hocho <=> c2h5coch3 + hocho',
 "chemkinKinetics": """
c4h7oh1-2+hocho=c2h5coch3+hocho                     2.810e-02 3.286     -4.509   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.0281, 'cm^3/(mol*s)'),
    n = 3.286,
    Ea = (-4509, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV / 7.04E+04  1.209  556 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-2 + hocho <=> c2h5coch3 + hocho',
 "chemkinKinetics": """
c4h7oh2-2+hocho=c2h5coch3+hocho                     2.810e-02 3.286     -4.509   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.0281, 'cm^3/(mol*s)'),
    n = 3.286,
    Ea = (-4509, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV / 7.04E+04  1.209  556 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chchoh + hocho <=> c2h5cho + hocho',
 "chemkinKinetics": """
ch3chchoh+hocho=c2h5cho+hocho                       2.810e-02 3.286     -4.509   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.0281, 'cm^3/(mol*s)'),
    n = 3.286,
    Ea = (-4509, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV / 7.04E+04  1.209  556 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic3h5oh + hocho <=> ch3coch3 + hocho',
 "chemkinKinetics": """
ic3h5oh+hocho=ch3coch3+hocho                        2.810e-02 3.286     -4.509   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.0281, 'cm^3/(mol*s)'),
    n = 3.286,
    Ea = (-4509, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV / 7.04E+04  1.209  556 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chchoh <=> c2h5cho',
 "chemkinKinetics": """
ch3chchoh=c2h5cho                                   8.590e+11 0.318     55.900   
""",
 "rmgPyKinetics": Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['ketoenol',  ],
},

{
 "reaction": 'ic3h5oh <=> ch3coch3',
 "chemkinKinetics": """
ic3h5oh=ch3coch3                                    8.590e+11 0.318     55.900   
""",
 "rmgPyKinetics": Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['ketoenol',  ],
},

{
 "reaction": 'c4h7oh1-1 <=> nc3h7cho',
 "chemkinKinetics": """
c4h7oh1-1=nc3h7cho                                  8.590e+11 0.318     55.900   
""",
 "rmgPyKinetics": Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['ketoenol',  ],
},

{
 "reaction": 'c4h7oh2-1 <=> c2h5coch3',
 "chemkinKinetics": """
c4h7oh2-1=c2h5coch3                                 8.590e+11 0.318     55.900   
""",
 "rmgPyKinetics": Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-2 <=> c2h5coch3',
 "chemkinKinetics": """
c4h7oh2-2=c2h5coch3                                 8.590e+11 0.318     55.900   
""",
 "rmgPyKinetics": Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['ketoenol',  ],
},

{
 "reaction": 'ic3h6choh <=> ic3h7cho',
 "chemkinKinetics": """
ic3h6choh=ic3h7cho                                  8.590e+11 0.318     55.900   
""",
 "rmgPyKinetics": Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['ketoenol',  ],
},

{
 "reaction": 'c4h7oh1-3 + o2 <=> c4h6oh1-32 + ho2',
 "chemkinKinetics": """
c4h7oh1-3+o2=c4h6oh1-32+ho2                         6.000e+12 0.000     37.190   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-1 + o2 <=> c4h6oh1-32 + ho2',
 "chemkinKinetics": """
c4h7oh2-1+o2=c4h6oh1-32+ho2                         6.000e+12 0.000     37.190   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-4 + o2 <=> c4h6oh1-32 + ho2',
 "chemkinKinetics": """
c4h7oh1-4+o2=c4h6oh1-32+ho2                         6.000e+12 0.000     37.190   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-2 + o2 <=> c4h6oh1-32 + ho2',
 "chemkinKinetics": """
c4h7oh2-2+o2=c4h6oh1-32+ho2                         6.000e+12 0.000     37.190   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-2 + o2 <=> c4h6oh1-32 + ho2',
 "chemkinKinetics": """
c4h7oh1-2+o2=c4h6oh1-32+ho2                         4.000e+12 0.000     39.900   
""",
 "rmgPyKinetics": Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h7oh1-1 + o2 <=> c4h6oh1-13 + ho2',
 "chemkinKinetics": """
c4h7oh1-1+o2=c4h6oh1-13+ho2                         4.000e+12 0.000     37.190   
""",
 "rmgPyKinetics": Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c3h5oh + h <=> c2h4 + ch2oh',
 "chemkinKinetics": """
c3h5oh+h=c2h4+ch2oh                                 6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic3h5oh + h <=> c2h3oh + ch3',
 "chemkinKinetics": """
ic3h5oh+h=c2h3oh+ch3                                6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic3h5oh + h <=> c3h6 + oh',
 "chemkinKinetics": """
ic3h5oh+h=c3h6+oh                                   6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chchoh + h <=> c2h3oh + ch3',
 "chemkinKinetics": """
ch3chchoh+h=c2h3oh+ch3                              6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3chchoh + h <=> c3h6 + oh',
 "chemkinKinetics": """
ch3chchoh+h=c3h6+oh                                 6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic3h6choh + h <=> ch3chchoh + ch3',
 "chemkinKinetics": """
ic3h6choh+h=ch3chchoh+ch3                           6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic3h6choh + h <=> ic4h8 + oh',
 "chemkinKinetics": """
ic3h6choh+h=ic4h8+oh                                6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-1 + h <=> c4h8-1 + oh',
 "chemkinKinetics": """
c4h7oh1-1+h=c4h8-1+oh                               6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-1 + h <=> c2h3oh + c2h5',
 "chemkinKinetics": """
c4h7oh1-1+h=c2h3oh+c2h5                             6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-2 + h <=> c4h8-1 + oh',
 "chemkinKinetics": """
c4h7oh1-2+h=c4h8-1+oh                               6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-2 + h <=> c2h3oh + c2h5',
 "chemkinKinetics": """
c4h7oh1-2+h=c2h3oh+c2h5                             6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-2 + h <=> ic3h5oh + ch3',
 "chemkinKinetics": """
c4h7oh2-2+h=ic3h5oh+ch3                             6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-2 + h <=> c4h8-2 + oh',
 "chemkinKinetics": """
c4h7oh2-2+h=c4h8-2+oh                               6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-2 + h <=> ch3chchoh + ch3',
 "chemkinKinetics": """
c4h7oh2-2+h=ch3chchoh+ch3                           6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic3h5ch2oh + h <=> ch3 + c3h5oh',
 "chemkinKinetics": """
ic3h5ch2oh+h=ch3+c3h5oh                             6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-3 + h <=> c2h4 + sc2h4oh',
 "chemkinKinetics": """
c4h7oh1-3+h=c2h4+sc2h4oh                            6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-4 + h <=> c2h4 + pc2h4oh',
 "chemkinKinetics": """
c4h7oh1-4+h=c2h4+pc2h4oh                            6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-1 + h <=> c3h6 + ch2oh',
 "chemkinKinetics": """
c4h7oh2-1+h=c3h6+ch2oh                              6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-1 + h <=> c4h8-2 + oh',
 "chemkinKinetics": """
c4h7oh2-1+h=c4h8-2+oh                               6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh2-1 + h <=> ch3chchoh + ch3',
 "chemkinKinetics": """
c4h7oh2-1+h=ch3chchoh+ch3                           6.260e+13 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6oh1-32 <=> c4h6 + oh',
 "chemkinKinetics": """
c4h6oh1-32=c4h6+oh                                  7.035e+16 -1.012    36.070   
""",
 "rmgPyKinetics": Arrhenius(A=(7.035e+16, 's^-1'), n=-1.012, Ea=(36070, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h6oh1-13 <=> c4h5oh-13 + h',
 "chemkinKinetics": """
c4h6oh1-13=c4h5oh-13+h                              7.722e+12 0.488     43.940   
""",
 "rmgPyKinetics": Arrhenius(A=(7.722e+12, 's^-1'), n=0.488, Ea=(43940, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c3h6 + oh <=> ic3h6oh',
 "chemkinKinetics": """
c3h6+oh=ic3h6oh                                     2.920e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.92e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h3oh + ch3 <=> ic3h6oh',
 "chemkinKinetics": """
c2h3oh+ch3=ic3h6oh                                  1.890e+03 2.670     6.850    
""",
 "rmgPyKinetics": Arrhenius(A=(1890, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h5oh + h <=> ic3h6oh',
 "chemkinKinetics": """
ic3h5oh+h=ic3h6oh                                   6.250e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.25e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h5cho + h <=> c3h6oh-1',
 "chemkinKinetics": """
c2h5cho+h=c3h6oh-1                                  4.240e+11 0.510     1.230    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.24e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (1230, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3chchoh + h <=> c3h6oh-1',
 "chemkinKinetics": """
ch3chchoh+h=c3h6oh-1                                2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3 + c2h3oh <=> c3h6oh-1',
 "chemkinKinetics": """
ch3+c2h3oh=c3h6oh-1                                 1.760e+04 2.480     6.130    
""",
 "rmgPyKinetics": Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c3h6 + oh <=> c3h6oh-2',
 "chemkinKinetics": """
c3h6+oh=c3h6oh-2                                    4.950e+11 0.000     -0.960   
""",
 "rmgPyKinetics": Arrhenius(A=(4.95e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'h + ch3chchoh <=> c3h6oh-2',
 "chemkinKinetics": """
h+ch3chchoh=c3h6oh-2                                2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'h + c3h5oh <=> c3h6oh-2',
 "chemkinKinetics": """
h+c3h5oh=c3h6oh-2                                   4.240e+11 0.510     1.230    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.24e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (1230, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh1-3 <=> c4h71-3 + oh',
 "chemkinKinetics": """
c4h7oh1-3=c4h71-3+oh                                2.367e+20 -1.189    94.340   
""",
 "rmgPyKinetics": Arrhenius(A=(2.367e+20, 's^-1'), n=-1.189, Ea=(94340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh1-3 <=> c2h3 + sc2h4oh',
 "chemkinKinetics": """
c4h7oh1-3=c2h3+sc2h4oh                              6.644e+19 -1.132    74.590   
""",
 "rmgPyKinetics": Arrhenius(A=(6.644e+19, 's^-1'), n=-1.132, Ea=(74590, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh2-1 <=> c4h71-3 + oh',
 "chemkinKinetics": """
c4h7oh2-1=c4h71-3+oh                                2.367e+20 -1.189    94.340   
""",
 "rmgPyKinetics": Arrhenius(A=(2.367e+20, 's^-1'), n=-1.189, Ea=(94340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh2-1 <=> c3h5-a + ch2oh',
 "chemkinKinetics": """
c4h7oh2-1=c3h5-a+ch2oh                              6.644e+19 -1.132    74.590   
""",
 "rmgPyKinetics": Arrhenius(A=(6.644e+19, 's^-1'), n=-1.132, Ea=(74590, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-4 <=> c4h71-4 + oh',
 "chemkinKinetics": """
c4h7oh1-4=c4h71-4+oh                                2.367e+20 -1.189    94.340   
""",
 "rmgPyKinetics": Arrhenius(A=(2.367e+20, 's^-1'), n=-1.189, Ea=(94340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh1-4 <=> c2h3 + pc2h4oh',
 "chemkinKinetics": """
c4h7oh1-4=c2h3+pc2h4oh                              6.644e+19 -1.132    74.590   
""",
 "rmgPyKinetics": Arrhenius(A=(6.644e+19, 's^-1'), n=-1.132, Ea=(74590, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh2-2 <=> c4h72-2 + oh',
 "chemkinKinetics": """
c4h7oh2-2=c4h72-2+oh                                2.367e+20 -1.189    94.340   
""",
 "rmgPyKinetics": Arrhenius(A=(2.367e+20, 's^-1'), n=-1.189, Ea=(94340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh1-2 <=> c4h71-2 + oh',
 "chemkinKinetics": """
c4h7oh1-2=c4h71-2+oh                                5.887e+19 -0.956    95.950   
""",
 "rmgPyKinetics": Arrhenius(A=(5.887e+19, 's^-1'), n=-0.956, Ea=(95950, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh1-2 <=> c2h5 + ch2cho',
 "chemkinKinetics": """
c4h7oh1-2=c2h5+ch2cho                               2.214e+22 -1.576    97.520   
""",
 "rmgPyKinetics": Arrhenius(A=(2.214e+22, 's^-1'), n=-1.576, Ea=(97520, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-1 <=> c2h5 + ch2cho',
 "chemkinKinetics": """
c4h7oh1-1=c2h5+ch2cho                               2.214e+22 -1.576    97.520   
""",
 "rmgPyKinetics": Arrhenius(A=(2.214e+22, 's^-1'), n=-1.576, Ea=(97520, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh1-1 <=> c4h71-1 + oh',
 "chemkinKinetics": """
c4h7oh1-1=c4h71-1+oh                                5.887e+19 -0.956    95.950   
""",
 "rmgPyKinetics": Arrhenius(A=(5.887e+19, 's^-1'), n=-0.956, Ea=(95950, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h5oh-13 <=> c4h5-n + oh',
 "chemkinKinetics": """
c4h5oh-13=c4h5-n+oh                                 5.610e+21 -1.612    106.000  
""",
 "rmgPyKinetics": Arrhenius(A=(5.61e+21, 's^-1'), n=-1.612, Ea=(106000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h5oh-13 <=> c2h3 + ch2cho',
 "chemkinKinetics": """
c4h5oh-13=c2h3+ch2cho                               2.816e+24 -2.381    90.130   
""",
 "rmgPyKinetics": Arrhenius(A=(2.816e+24, 's^-1'), n=-2.381, Ea=(90130, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'tc4h9oh <=> ch3 + tc3h6oh',
 "chemkinKinetics": """
tc4h9oh(+M)=ch3+tc3h6oh(+M)                         6.310e+16 0.000     81.277   

    LOW/ 9.821e+74 -16.121   92.918   /
    TROE/ 4.087e-01 1.1e+03   490       2.85e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(6.31e+16, 's^-1'), n=0, Ea=(81277, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (9.8207e+74, 'cm^3/(mol*s)'),
        n = -16.121,
        Ea = (92918, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.40865,
    T3 = (1104.3, 'K'),
    T1 = (490, 'K'),
    T2 = (2851.9, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'tc4h9oh <=> oh + tc4h9',
 "chemkinKinetics": """
tc4h9oh(+M)=oh+tc4h9(+M)                            1.200e+24 -2.130    97.281   

    LOW/ 4.529e+74 -16.275   107.810  /
    TROE/ 3.679e-01 469       2.91e+12  3.67e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.2e+24, 's^-1'), n=-2.13, Ea=(97281, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (4.5291e+74, 'cm^3/(mol*s)'),
        n = -16.275,
        Ea = (107810, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.36787,
    T3 = (469.09, 'K'),
    T1 = (2.9117e+12, 'K'),
    T2 = (3672.8, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'tc4h9oh <=> h + tc4h9o',
 "chemkinKinetics": """
tc4h9oh(+M)=h+tc4h9o(+M)                            1.100e+15 0.028     105.150  

    LOW/ 5.444e+61 -13.089   114.690  /
    TROE/ 3.033e-01 516       3.96e+07  2.39e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.1e+15, 's^-1'), n=0.028, Ea=(105150, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (5.4443e+61, 'cm^3/(mol*s)'),
        n = -13.089,
        Ea = (114690, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.30333,
    T3 = (515.66, 'K'),
    T1 = (3.9578e+07, 'K'),
    T2 = (2386.5, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'tc4h9oh <=> h + tc4h8oh',
 "chemkinKinetics": """
tc4h9oh(+M)=h+tc4h8oh(+M)                           1.300e+18 -0.449    104.460  

    LOW/ 1.542e+65 -13.668   114.110  /
    TROE/ 3.211e-01 507       8e+06     2.54e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.3e+18, 's^-1'), n=-0.449, Ea=(104460, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.542e+65, 'cm^3/(mol*s)'),
        n = -13.668,
        Ea = (114110, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.32112,
    T3 = (507.26, 'K'),
    T1 = (7.9992e+06, 'K'),
    T2 = (2535.1, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'tc4h9oh <=> h2o + ic4h8',
 "chemkinKinetics": """
tc4h9oh(+M)=h2o+ic4h8(+M)                           1.480e+14 0.000     64.200   

    LOW/ 5.871e+95 -22.630   79.171   /
    TROE/ 3.268e-05 333       1.41e+10  3.82e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.48e+14, 's^-1'), n=0, Ea=(64200, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (5.8705e+95, 'cm^3/(mol*s)'),
        n = -22.63,
        Ea = (79171, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 3.2677e-05,
    T3 = (332.6, 'K'),
    T1 = (1.4141e+10, 'K'),
    T2 = (3823.8, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['1,3_Insertion_ROR',  ],
},

{
 "reaction": 'sc4h9oh <=> ch3 + ic3h6oh',
 "chemkinKinetics": """
sc4h9oh(+M)=ch3+ic3h6oh(+M)                         1.100e+26 -2.815    92.354   

    LOW/ 1.532e+84 -19.166   104.670  /
    TROE/ 4.255e-02 278       3.36e+06  2.19e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.1e+26, 's^-1'), n=-2.815, Ea=(92354, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.5323e+84, 'cm^3/(mol*s)'),
        n = -19.166,
        Ea = (104670, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.042546,
    T3 = (277.51, 'K'),
    T1 = (3.3602e+06, 'K'),
    T2 = (2193.4, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9oh <=> c2h5 + sc2h4oh',
 "chemkinKinetics": """
sc4h9oh(+M)=c2h5+sc2h4oh(+M)                        1.728e+26 -2.720    86.207   

    LOW/ 1.677e+89 -20.364   99.453   /
    TROE/ 5.585e-03 358       4.93e+07  2.48e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.728e+26, 's^-1'), n=-2.72, Ea=(86207, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.6771e+89, 'cm^3/(mol*s)'),
        n = -20.364,
        Ea = (99453, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.0055845,
    T3 = (358.2, 'K'),
    T1 = (4.9325e+07, 'K'),
    T2 = (2476.1, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9oh <=> ch3 + c3h6oh-1',
 "chemkinKinetics": """
sc4h9oh(+M)=ch3+c3h6oh-1(+M)                        8.500e+24 -2.530    88.444   

    LOW/ 9.912e+85 -19.664   101.200  /
    TROE/ 3.993e-01 217       466       2.28e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(8.5e+24, 's^-1'), n=-2.53, Ea=(88444, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (9.9116e+85, 'cm^3/(mol*s)'),
        n = -19.664,
        Ea = (101200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.39928,
    T3 = (217.47, 'K'),
    T1 = (465.57, 'K'),
    T2 = (2284.1, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9oh <=> oh + sc4h9',
 "chemkinKinetics": """
sc4h9oh(+M)=oh+sc4h9(+M)                            6.430e+22 -1.865    96.229   

    LOW/ 1.902e+78 -17.503   108.350  /
    TROE/ 8.677e-05 293       1.97e+04  1.67e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(6.43e+22, 's^-1'), n=-1.865, Ea=(96229, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.9022e+78, 'cm^3/(mol*s)'),
        n = -17.503,
        Ea = (108350, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 8.6766e-05,
    T3 = (293.41, 'K'),
    T1 = (19749, 'K'),
    T2 = (1674.6, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9oh <=> h + sc4h8ohm',
 "chemkinKinetics": """
sc4h9oh(+M)=h+sc4h8ohm(+M)                          1.330e+16 0.017     102.430  

    LOW/ 5.218e+66 -14.289   113.840  /
    TROE/ 8.936e-02 337       7.84e+09  1.66e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.33e+16, 's^-1'), n=0.017, Ea=(102430, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (5.218e+66, 'cm^3/(mol*s)'),
        n = -14.289,
        Ea = (113840, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.089358,
    T3 = (336.51, 'K'),
    T1 = (7.8352e+09, 'K'),
    T2 = (1663.2, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9oh <=> h + sc4h8oh-1',
 "chemkinKinetics": """
sc4h9oh(+M)=h+sc4h8oh-1(+M)                         8.860e+18 -0.818    94.238   

    LOW/ 6.424e+75 -16.831   106.460  /
    TROE/ 1.090e-01 86.8      5.71e+09  2.44e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(8.86e+18, 's^-1'), n=-0.818, Ea=(94238, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (6.4242e+75, 'cm^3/(mol*s)'),
        n = -16.831,
        Ea = (106460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.10896,
    T3 = (86.767, 'K'),
    T1 = (5.7087e+09, 'K'),
    T2 = (2439.2, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9oh <=> h + sc4h8oh-2',
 "chemkinKinetics": """
sc4h9oh(+M)=h+sc4h8oh-2(+M)                         3.630e+20 -1.323    102.100  

    LOW/ 2.706e+71 -15.706   113.570  /
    TROE/ 1.803e-01 274       1.08e+07  2.15e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(3.63e+20, 's^-1'), n=-1.323, Ea=(102100, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (2.7063e+71, 'cm^3/(mol*s)'),
        n = -15.706,
        Ea = (113570, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.18033,
    T3 = (274.39, 'K'),
    T1 = (1.0791e+07, 'K'),
    T2 = (2148, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9oh <=> h + sc4h8oh-3',
 "chemkinKinetics": """
sc4h9oh(+M)=h+sc4h8oh-3(+M)                         1.310e+16 0.018     101.830  

    LOW/ 1.741e+67 -14.434   113.350  /
    TROE/ 1.605e-01 286       1.54e+06  2.06e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.31e+16, 's^-1'), n=0.018, Ea=(101830, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.7414e+67, 'cm^3/(mol*s)'),
        n = -14.434,
        Ea = (113350, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.16051,
    T3 = (285.87, 'K'),
    T1 = (1.5444e+06, 'K'),
    T2 = (2057.6, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9oh <=> h + sc4h9o',
 "chemkinKinetics": """
sc4h9oh(+M)=h+sc4h9o(+M)                            2.200e+14 0.245     104.850  

    LOW/ 8.597e+62 -13.509   115.890  /
    TROE/ 4.882e-01 27.2      2.1e+10   2.25e+06 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(2.2e+14, 's^-1'), n=0.245, Ea=(104850, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (8.597e+62, 'cm^3/(mol*s)'),
        n = -13.509,
        Ea = (115890, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.48822,
    T3 = (27.191, 'K'),
    T1 = (2.1032e+10, 'K'),
    T2 = (2.2461e+06, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h9oh <=> h2o + c4h8-1',
 "chemkinKinetics": """
sc4h9oh(+M)=h2o+c4h8-1(+M)                          5.000e+13 0.000     67.960   

    LOW/ 4.821e+94 -22.464   83.529   /
    TROE/ 2.825e-04 362       1.29e+04  4.49e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(5e+13, 's^-1'), n=0, Ea=(67960, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (4.8206e+94, 'cm^3/(mol*s)'),
        n = -22.464,
        Ea = (83529, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.00028246,
    T3 = (361.97, 'K'),
    T1 = (12873, 'K'),
    T2 = (4491, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['1,3_Insertion_ROR',  ],
},

{
 "reaction": 'sc4h9oh <=> h2o + c4h8-2',
 "chemkinKinetics": """
sc4h9oh(+M)=h2o+c4h8-2(+M)                          3.500e+13 0.000     65.900   

    LOW/ 4.627e+101 -24.473   83.466   /
    TROE/ 2.946e-03 293       5.21e+10  5.08e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(3.5e+13, 's^-1'), n=0, Ea=(65900, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (4.6273e+101, 'cm^3/(mol*s)'),
        n = -24.473,
        Ea = (83466, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.0029457,
    T3 = (293.4, 'K'),
    T1 = (5.2057e+10, 'K'),
    T2 = (5081.2, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['1,3_Insertion_ROR',  ],
},

{
 "reaction": 'ic4h9oh <=> ic3h7 + ch2oh',
 "chemkinKinetics": """
ic4h9oh(+M)=ic3h7+ch2oh(+M)                         3.250e+25 -2.413    87.976   

    LOW/ 1.233e+73 -15.724   92.616   /
    TROE/ 1.342e-01 775       4.01e+07  4.43e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(3.25e+25, 's^-1'), n=-2.413, Ea=(87976, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.2327e+73, 'cm^3/(mol*s)'),
        n = -15.724,
        Ea = (92616, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.13423,
    T3 = (775.39, 'K'),
    T1 = (4.0069e+07, 'K'),
    T2 = (4428.1, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h9oh <=> c3h6oh-2 + ch3',
 "chemkinKinetics": """
ic4h9oh(+M)=c3h6oh-2+ch3(+M)                        4.000e+27 -3.110    92.179   

    LOW/ 4.046e+66 -14.122   90.777   /
    TROE/ 1.442e-01 836       4.85e+06  4.55e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(4e+27, 's^-1'), n=-3.11, Ea=(92179, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (4.0463e+66, 'cm^3/(mol*s)'),
        n = -14.122,
        Ea = (90777, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.14416,
    T3 = (835.91, 'K'),
    T1 = (4.8482e+06, 'K'),
    T2 = (4547.3, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h9oh <=> oh + ic4h9',
 "chemkinKinetics": """
ic4h9oh(+M)=oh+ic4h9(+M)                            1.400e+21 -1.481    94.894   

    LOW/ 2.087e+55 -11.191   90.431   /
    TROE/ 5.447e-04 1.13e+03  1.68e+10  3.64e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.4e+21, 's^-1'), n=-1.481, Ea=(94894, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (2.0872e+55, 'cm^3/(mol*s)'),
        n = -11.191,
        Ea = (90431, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.00054471,
    T3 = (1125.4, 'K'),
    T1 = (1.6818e+10, 'K'),
    T2 = (3635.2, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h9oh <=> ic4h8oh-1 + h',
 "chemkinKinetics": """
ic4h9oh(+M)=ic4h8oh-1+h(+M)                         5.680e+16 -0.297    95.908   

    LOW/ 1.890e+49 -9.561    90.472   /
    TROE/ 2.095e-05 1.16e+03  1.68e+10  3.7e+03  /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(5.68e+16, 's^-1'), n=-0.297, Ea=(95908, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.8895e+49, 'cm^3/(mol*s)'),
        n = -9.561,
        Ea = (90472, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 2.0948e-05,
    T3 = (1164.2, 'K'),
    T1 = (1.6818e+10, 'K'),
    T2 = (3704.9, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h9oh <=> ic4h8oh-2 + h',
 "chemkinKinetics": """
ic4h9oh(+M)=ic4h8oh-2+h(+M)                         1.700e+17 -0.467    98.199   

    LOW/ 2.478e+46 -8.823    90.945   /
    TROE/ 1.459e-01 1.03e+03  1.07e+11  5.13e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.7e+17, 's^-1'), n=-0.467, Ea=(98199, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (2.4779e+46, 'cm^3/(mol*s)'),
        n = -8.823,
        Ea = (90945, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.14595,
    T3 = (1034, 'K'),
    T1 = (1.0695e+11, 'K'),
    T2 = (5129.2, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h9oh <=> ic4h8oh-3 + h',
 "chemkinKinetics": """
ic4h9oh(+M)=ic4h8oh-3+h(+M)                         5.000e+17 -0.462    102.490  

    LOW/ 3.317e+41 -7.365    92.821   /
    TROE/ 2.707e-01 2.74e+03  129       9.66e+03 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(5e+17, 's^-1'), n=-0.462, Ea=(102490, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (3.3167e+41, 'cm^3/(mol*s)'),
        n = -7.365,
        Ea = (92821, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.27069,
    T3 = (2741.9, 'K'),
    T1 = (128.72, 'K'),
    T2 = (9656.2, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h9oh <=> ic4h9o + h',
 "chemkinKinetics": """
ic4h9oh(+M)=ic4h9o+h(+M)                            1.200e+15 0.016     105.180  

    LOW/ 1.494e+36 -6.144    94.567   /
    TROE/ 4.999e-01 6.21e+03  666       2.9e+06  /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(1.2e+15, 's^-1'), n=0.016, Ea=(105180, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (1.4939e+36, 'cm^3/(mol*s)'),
        n = -6.144,
        Ea = (94567, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.49994,
    T3 = (6209.6, 'K'),
    T1 = (665.5, 'K'),
    T2 = (2.9e+06, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h9oh <=> h2o + ic4h8',
 "chemkinKinetics": """
ic4h9oh(+M)=h2o+ic4h8(+M)                           4.560e+13 0.000     64.970   

    LOW/ 6.097e+101 -23.781   106.720  /
    TROE/ 2.018e-01 1.29e+03  1.28e+03  6.79e+04 /
""",
 "rmgPyKinetics": Troe(
    arrheniusHigh = Arrhenius(A=(4.56e+13, 's^-1'), n=0, Ea=(64970, 'cal/mol'), T0=(1, 'K')),
    arrheniusLow = Arrhenius(
        A = (6.0967e+101, 'cm^3/(mol*s)'),
        n = -23.781,
        Ea = (106720, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    alpha = 0.20182,
    T3 = (1286.4, 'K'),
    T1 = (1282.4, 'K'),
    T2 = (67921, 'K'),
    efficiencies = {},
),
 "possibleReactionFamilies": ['1,3_Insertion_ROR',  ],
},

{
 "reaction": 'tc4h9oh + h <=> tc4h9o + h2',
 "chemkinKinetics": """
tc4h9oh+h=tc4h9o+h2                                 9.450e+02 3.140     8.701    
""",
 "rmgPyKinetics": Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + h <=> tc4h8oh + h2',
 "chemkinKinetics": """
tc4h9oh+h=tc4h8oh+h2                                1.998e+06 2.540     6.756    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.998e+06, 'cm^3/(mol*s)'),
    n = 2.54,
    Ea = (6756, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + oh <=> tc4h9o + h2o',
 "chemkinKinetics": """
tc4h9oh+oh=tc4h9o+h2o                               5.880e+02 2.820     -0.585   
""",
 "rmgPyKinetics": Arrhenius(A=(588, 'cm^3/(mol*s)'), n=2.82, Ea=(-585, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + oh <=> tc4h8oh + h2o',
 "chemkinKinetics": """
tc4h9oh+oh=tc4h8oh+h2o                              6.930e+00 3.700     -2.416   
""",
 "rmgPyKinetics": Arrhenius(A=(6.93, 'cm^3/(mol*s)'), n=3.7, Ea=(-2416, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + o <=> tc4h9o + oh',
 "chemkinKinetics": """
tc4h9oh+o=tc4h9o+oh                                 1.460e-03 4.730     1.727    
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.00146, 'cm^3/(mol*s)'),
    n = 4.73,
    Ea = (1727, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + o <=> tc4h8oh + oh',
 "chemkinKinetics": """
tc4h9oh+o=tc4h8oh+oh                                2.943e+06 2.430     4.750    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.943e+06, 'cm^3/(mol*s)'),
    n = 2.43,
    Ea = (4750, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + ho2 <=> tc4h9o + h2o2',
 "chemkinKinetics": """
tc4h9oh+ho2=tc4h9o+h2o2                             6.470e-07 5.300     10.530   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.47e-07, 'cm^3/(mol*s)'),
    n = 5.3,
    Ea = (10530, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + ho2 <=> tc4h8oh + h2o2',
 "chemkinKinetics": """
tc4h9oh+ho2=tc4h8oh+h2o2                            7.140e+04 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(71400, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + ch3 <=> tc4h9o + ch4',
 "chemkinKinetics": """
tc4h9oh+ch3=tc4h9o+ch4                              1.020e+00 3.570     8.221    
""",
 "rmgPyKinetics": Arrhenius(A=(1.02, 'cm^3/(mol*s)'), n=3.57, Ea=(8221, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + ch3 <=> tc4h8oh + ch4',
 "chemkinKinetics": """
tc4h9oh+ch3=tc4h8oh+ch4                             1.359e+00 3.650     9.154    
""",
 "rmgPyKinetics": Arrhenius(A=(1.359, 'cm^3/(mol*s)'), n=3.65, Ea=(9154, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + ch3o <=> tc4h9o + ch3oh',
 "chemkinKinetics": """
tc4h9oh+ch3o=tc4h9o+ch3oh                           2.300e+10 0.000     2.900    
""",
 "rmgPyKinetics": Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + ch3o <=> tc4h8oh + ch3oh',
 "chemkinKinetics": """
tc4h9oh+ch3o=tc4h8oh+ch3oh                          6.510e+11 0.000     8.458    
""",
 "rmgPyKinetics": Arrhenius(A=(6.51e+11, 'cm^3/(mol*s)'), n=0, Ea=(8458, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + hco <=> tc4h9o + ch2o',
 "chemkinKinetics": """
tc4h9oh+hco=tc4h9o+ch2o                             3.400e+04 2.500     13.500   
""",
 "rmgPyKinetics": Arrhenius(A=(34000, 'cm^3/(mol*s)'), n=2.5, Ea=(13500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + hco <=> tc4h8oh + ch2o',
 "chemkinKinetics": """
tc4h9oh+hco=tc4h8oh+ch2o                            3.060e+05 2.500     18.440   
""",
 "rmgPyKinetics": Arrhenius(A=(306000, 'cm^3/(mol*s)'), n=2.5, Ea=(18440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + ch2oh <=> tc4h9o + ch3oh',
 "chemkinKinetics": """
tc4h9oh+ch2oh=tc4h9o+ch3oh                          1.200e+02 2.760     10.800   
""",
 "rmgPyKinetics": Arrhenius(A=(120, 'cm^3/(mol*s)'), n=2.76, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + ch2oh <=> tc4h8oh + ch3oh',
 "chemkinKinetics": """
tc4h9oh+ch2oh=tc4h8oh+ch3oh                         3.030e+02 2.950     13.970   
""",
 "rmgPyKinetics": Arrhenius(A=(303, 'cm^3/(mol*s)'), n=2.95, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + ch3o2 <=> tc4h9o + ch3o2h',
 "chemkinKinetics": """
tc4h9oh+ch3o2=tc4h9o+ch3o2h                         1.680e-02 4.120     16.730   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.0168, 'cm^3/(mol*s)'),
    n = 4.12,
    Ea = (16730, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + ch3o2 <=> tc4h8oh + ch3o2h',
 "chemkinKinetics": """
tc4h9oh+ch3o2=tc4h8oh+ch3o2h                        7.140e+04 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(71400, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + c2h5 <=> tc4h9o + c2h6',
 "chemkinKinetics": """
tc4h9oh+c2h5=tc4h9o+c2h6                            1.670e+10 0.000     13.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1.67e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + c2h5 <=> tc4h8oh + c2h6',
 "chemkinKinetics": """
tc4h9oh+c2h5=tc4h8oh+c2h6                           1.503e+11 0.000     13.400   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.503e+11, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (13400, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + o2 <=> ho2 + tc4h8oh',
 "chemkinKinetics": """
tc4h9oh+o2=ho2+tc4h8oh                              6.000e+13 0.000     52.340   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h9oh + o2 <=> ho2 + tc4h9o',
 "chemkinKinetics": """
tc4h9oh+o2=ho2+tc4h9o                               1.000e+13 0.000     56.340   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(56340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + h <=> sc4h9o + h2',
 "chemkinKinetics": """
sc4h9oh+h=sc4h9o+h2                                 9.450e+02 3.140     8.701    
""",
 "rmgPyKinetics": Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + h <=> sc4h8ohm + h2',
 "chemkinKinetics": """
sc4h9oh+h=sc4h8ohm+h2                               6.660e+05 2.540     6.756    
""",
 "rmgPyKinetics": Arrhenius(A=(666000, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + h <=> sc4h8oh-3 + h2',
 "chemkinKinetics": """
sc4h9oh+h=sc4h8oh-3+h2                              6.660e+05 2.540     6.756    
""",
 "rmgPyKinetics": Arrhenius(A=(666000, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + h <=> sc4h8oh-2 + h2',
 "chemkinKinetics": """
sc4h9oh+h=sc4h8oh-2+h2                              1.080e+05 2.690     4.440    
""",
 "rmgPyKinetics": Arrhenius(A=(108000, 'cm^3/(mol*s)'), n=2.69, Ea=(4440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + h <=> sc4h8oh-1 + h2',
 "chemkinKinetics": """
sc4h9oh+h=sc4h8oh-1+h2                              4.395e+04 2.680     2.915    
""",
 "rmgPyKinetics": Arrhenius(A=(43950, 'cm^3/(mol*s)'), n=2.68, Ea=(2915, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + oh <=> sc4h9o + h2o',
 "chemkinKinetics": """
sc4h9oh+oh=sc4h9o+h2o                               5.880e+02 2.820     -0.585   
""",
 "rmgPyKinetics": Arrhenius(A=(588, 'cm^3/(mol*s)'), n=2.82, Ea=(-585, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + oh <=> sc4h8ohm + h2o',
 "chemkinKinetics": """
sc4h9oh+oh=sc4h8ohm+h2o                             2.310e+00 3.700     -2.946   
""",
 "rmgPyKinetics": Arrhenius(A=(2.31, 'cm^3/(mol*s)'), n=3.7, Ea=(-2946, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + oh <=> sc4h8oh-3 + h2o',
 "chemkinKinetics": """
sc4h9oh+oh=sc4h8oh-3+h2o                            5.170e+06 1.806     0.012    
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.17e+06, 'cm^3/(mol*s)'),
    n = 1.806,
    Ea = (12.48, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + oh <=> sc4h8oh-2 + h2o',
 "chemkinKinetics": """
sc4h9oh+oh=sc4h8oh-2+h2o                            1.540e+00 3.700     -3.736   
""",
 "rmgPyKinetics": Arrhenius(A=(1.54, 'cm^3/(mol*s)'), n=3.7, Ea=(-3736, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + oh <=> sc4h8oh-1 + h2o',
 "chemkinKinetics": """
sc4h9oh+oh=sc4h8oh-1+h2o                            1.805e+03 2.890     -2.611   
""",
 "rmgPyKinetics": Arrhenius(A=(1805, 'cm^3/(mol*s)'), n=2.89, Ea=(-2611, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + o <=> sc4h9o + oh',
 "chemkinKinetics": """
sc4h9oh+o=sc4h9o+oh                                 1.460e-03 4.730     1.727    
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.00146, 'cm^3/(mol*s)'),
    n = 4.73,
    Ea = (1727, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + o <=> sc4h8ohm + oh',
 "chemkinKinetics": """
sc4h9oh+o=sc4h8ohm+oh                               9.810e+05 2.430     4.750    
""",
 "rmgPyKinetics": Arrhenius(A=(981000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + o <=> sc4h8oh-3 + oh',
 "chemkinKinetics": """
sc4h9oh+o=sc4h8oh-3+oh                              9.810e+05 2.430     4.750    
""",
 "rmgPyKinetics": Arrhenius(A=(981000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + o <=> sc4h8oh-2 + oh',
 "chemkinKinetics": """
sc4h9oh+o=sc4h8oh-2+oh                              1.440e+05 2.610     3.029    
""",
 "rmgPyKinetics": Arrhenius(A=(144000, 'cm^3/(mol*s)'), n=2.61, Ea=(3029, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + o <=> sc4h8oh-1 + oh',
 "chemkinKinetics": """
sc4h9oh+o=sc4h8oh-1+oh                              7.250e+04 2.470     0.876    
""",
 "rmgPyKinetics": Arrhenius(A=(72500, 'cm^3/(mol*s)'), n=2.47, Ea=(876, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ho2 <=> sc4h9o + h2o2',
 "chemkinKinetics": """
sc4h9oh+ho2=sc4h9o+h2o2                             6.470e-07 5.300     10.530   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.47e-07, 'cm^3/(mol*s)'),
    n = 5.3,
    Ea = (10530, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ho2 <=> sc4h8ohm + h2o2',
 "chemkinKinetics": """
sc4h9oh+ho2=sc4h8ohm+h2o2                           1.130e-02 4.520     13.850   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.0113, 'cm^3/(mol*s)'),
    n = 4.52,
    Ea = (13850, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ho2 <=> sc4h8oh-3 + h2o2',
 "chemkinKinetics": """
sc4h9oh+ho2=sc4h8oh-3+h2o2                          4.140e-04 4.760     15.050   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.000414, 'cm^3/(mol*s)'),
    n = 4.76,
    Ea = (15050, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ho2 <=> sc4h8oh-2 + h2o2',
 "chemkinKinetics": """
sc4h9oh+ho2=sc4h8oh-2+h2o2                          7.510e-03 4.520     14.710   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.00751, 'cm^3/(mol*s)'),
    n = 4.52,
    Ea = (14710, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ho2 <=> sc4h8oh-1 + h2o2',
 "chemkinKinetics": """
sc4h9oh+ho2=sc4h8oh-1+h2o2                          1.250e-05 5.260     7.468    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.25e-05, 'cm^3/(mol*s)'),
    n = 5.26,
    Ea = (7468, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3 <=> sc4h9o + ch4',
 "chemkinKinetics": """
sc4h9oh+ch3=sc4h9o+ch4                              1.020e+00 3.570     8.221    
""",
 "rmgPyKinetics": Arrhenius(A=(1.02, 'cm^3/(mol*s)'), n=3.57, Ea=(8221, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3 <=> sc4h8ohm + ch4',
 "chemkinKinetics": """
sc4h9oh+ch3=sc4h8ohm+ch4                            4.530e-01 3.650     7.154    
""",
 "rmgPyKinetics": Arrhenius(A=(0.453, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3 <=> sc4h8oh-3 + ch4',
 "chemkinKinetics": """
sc4h9oh+ch3=sc4h8oh-3+ch4                           4.530e-01 3.650     7.154    
""",
 "rmgPyKinetics": Arrhenius(A=(0.453, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3 <=> sc4h8oh-2 + ch4',
 "chemkinKinetics": """
sc4h9oh+ch3=sc4h8oh-2+ch4                           8.020e+00 3.230     6.461    
""",
 "rmgPyKinetics": Arrhenius(A=(8.02, 'cm^3/(mol*s)'), n=3.23, Ea=(6461, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3 <=> sc4h8oh-1 + ch4',
 "chemkinKinetics": """
sc4h9oh+ch3=sc4h8oh-1+ch4                           9.965e+00 3.370     7.634    
""",
 "rmgPyKinetics": Arrhenius(A=(9.965, 'cm^3/(mol*s)'), n=3.37, Ea=(7634, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + hco <=> sc4h9o + ch2o',
 "chemkinKinetics": """
sc4h9oh+hco=sc4h9o+ch2o                             3.400e+04 2.500     13.500   
""",
 "rmgPyKinetics": Arrhenius(A=(34000, 'cm^3/(mol*s)'), n=2.5, Ea=(13500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + hco <=> sc4h8ohm + ch2o',
 "chemkinKinetics": """
sc4h9oh+hco=sc4h8ohm+ch2o                           1.020e+05 2.500     18.440   
""",
 "rmgPyKinetics": Arrhenius(A=(102000, 'cm^3/(mol*s)'), n=2.5, Ea=(18440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + hco <=> sc4h8oh-3 + ch2o',
 "chemkinKinetics": """
sc4h9oh+hco=sc4h8oh-3+ch2o                          1.020e+05 2.500     18.440   
""",
 "rmgPyKinetics": Arrhenius(A=(102000, 'cm^3/(mol*s)'), n=2.5, Ea=(18440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + hco <=> sc4h8oh-2 + ch2o',
 "chemkinKinetics": """
sc4h9oh+hco=sc4h8oh-2+ch2o                          5.160e+05 2.250     16.760   
""",
 "rmgPyKinetics": Arrhenius(
    A = (516000, 'cm^3/(mol*s)'),
    n = 2.25,
    Ea = (16760, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + hco <=> sc4h8oh-1 + ch2o',
 "chemkinKinetics": """
sc4h9oh+hco=sc4h8oh-1+ch2o                          5.000e+06 1.900     17.000   
""",
 "rmgPyKinetics": Arrhenius(A=(5e+06, 'cm^3/(mol*s)'), n=1.9, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch2oh <=> sc4h9o + ch3oh',
 "chemkinKinetics": """
sc4h9oh+ch2oh=sc4h9o+ch3oh                          1.200e+02 2.760     10.800   
""",
 "rmgPyKinetics": Arrhenius(A=(120, 'cm^3/(mol*s)'), n=2.76, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch2oh <=> sc4h8ohm + ch3oh',
 "chemkinKinetics": """
sc4h9oh+ch2oh=sc4h8ohm+ch3oh                        1.010e+01 2.950     13.970   
""",
 "rmgPyKinetics": Arrhenius(A=(10.1, 'cm^3/(mol*s)'), n=2.95, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch2oh <=> sc4h8oh-3 + ch3oh',
 "chemkinKinetics": """
sc4h9oh+ch2oh=sc4h8oh-3+ch3oh                       1.010e+01 2.950     13.970   
""",
 "rmgPyKinetics": Arrhenius(A=(10.1, 'cm^3/(mol*s)'), n=2.95, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch2oh <=> sc4h8oh-2 + ch3oh',
 "chemkinKinetics": """
sc4h9oh+ch2oh=sc4h8oh-2+ch3oh                       1.530e+01 3.110     12.210   
""",
 "rmgPyKinetics": Arrhenius(A=(15.3, 'cm^3/(mol*s)'), n=3.11, Ea=(12210, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch2oh <=> sc4h8oh-1 + ch3oh',
 "chemkinKinetics": """
sc4h9oh+ch2oh=sc4h8oh-1+ch3oh                       3.000e+01 2.950     12.000   
""",
 "rmgPyKinetics": Arrhenius(A=(30, 'cm^3/(mol*s)'), n=2.95, Ea=(12000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3o <=> sc4h9o + ch3oh',
 "chemkinKinetics": """
sc4h9oh+ch3o=sc4h9o+ch3oh                           2.300e+10 0.000     2.900    
""",
 "rmgPyKinetics": Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3o <=> sc4h8ohm + ch3oh',
 "chemkinKinetics": """
sc4h9oh+ch3o=sc4h8ohm+ch3oh                         2.170e+11 0.000     6.458    
""",
 "rmgPyKinetics": Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3o <=> sc4h8oh-3 + ch3oh',
 "chemkinKinetics": """
sc4h9oh+ch3o=sc4h8oh-3+ch3oh                        2.170e+11 0.000     6.458    
""",
 "rmgPyKinetics": Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3o <=> sc4h8oh-2 + ch3oh',
 "chemkinKinetics": """
sc4h9oh+ch3o=sc4h8oh-2+ch3oh                        3.020e+10 0.180     4.703    
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.02e+10, 'cm^3/(mol*s)'),
    n = 0.18,
    Ea = (4703, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3o <=> sc4h8oh-1 + ch3oh',
 "chemkinKinetics": """
sc4h9oh+ch3o=sc4h8oh-1+ch3oh                        7.500e+10 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(7.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3o2 <=> sc4h9o + ch3o2h',
 "chemkinKinetics": """
sc4h9oh+ch3o2=sc4h9o+ch3o2h                         1.500e+12 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3o2 <=> sc4h8ohm + ch3o2h',
 "chemkinKinetics": """
sc4h9oh+ch3o2=sc4h8ohm+ch3o2h                       2.380e+04 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3o2 <=> sc4h8oh-3 + ch3o2h',
 "chemkinKinetics": """
sc4h9oh+ch3o2=sc4h8oh-3+ch3o2h                      2.380e+04 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3o2 <=> sc4h8oh-2 + ch3o2h',
 "chemkinKinetics": """
sc4h9oh+ch3o2=sc4h8oh-2+ch3o2h                      1.580e+03 2.810     14.050   
""",
 "rmgPyKinetics": Arrhenius(A=(1580, 'cm^3/(mol*s)'), n=2.81, Ea=(14050, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + ch3o2 <=> sc4h8oh-1 + ch3o2h',
 "chemkinKinetics": """
sc4h9oh+ch3o2=sc4h8oh-1+ch3o2h                      1.500e+12 0.000     17.500   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + c2h5 <=> sc4h9o + c2h6',
 "chemkinKinetics": """
sc4h9oh+c2h5=sc4h9o+c2h6                            1.670e+10 0.000     13.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1.67e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + c2h5 <=> sc4h8ohm + c2h6',
 "chemkinKinetics": """
sc4h9oh+c2h5=sc4h8ohm+c2h6                          5.010e+10 0.000     13.400   
""",
 "rmgPyKinetics": Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + c2h5 <=> sc4h8oh-3 + c2h6',
 "chemkinKinetics": """
sc4h9oh+c2h5=sc4h8oh-3+c2h6                         5.010e+10 0.000     13.400   
""",
 "rmgPyKinetics": Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + c2h5 <=> sc4h8oh-2 + c2h6',
 "chemkinKinetics": """
sc4h9oh+c2h5=sc4h8oh-2+c2h6                         5.010e+10 0.000     10.400   
""",
 "rmgPyKinetics": Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + c2h5 <=> sc4h8oh-1 + c2h6',
 "chemkinKinetics": """
sc4h9oh+c2h5=sc4h8oh-1+c2h6                         1.010e+11 0.000     7.900    
""",
 "rmgPyKinetics": Arrhenius(A=(1.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + o2 <=> ho2 + sc4h8ohm',
 "chemkinKinetics": """
sc4h9oh+o2=ho2+sc4h8ohm                             3.000e+13 0.000     52.340   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + o2 <=> ho2 + sc4h8oh-3',
 "chemkinKinetics": """
sc4h9oh+o2=ho2+sc4h8oh-3                            3.000e+13 0.000     52.340   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + o2 <=> ho2 + sc4h8oh-2',
 "chemkinKinetics": """
sc4h9oh+o2=ho2+sc4h8oh-2                            2.000e+13 0.000     49.800   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + o2 <=> ho2 + sc4h8oh-1',
 "chemkinKinetics": """
sc4h9oh+o2=ho2+sc4h8oh-1                            1.000e+13 0.000     46.800   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(46800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h9oh + o2 <=> ho2 + sc4h9o',
 "chemkinKinetics": """
sc4h9oh+o2=ho2+sc4h9o                               1.000e+13 0.000     56.340   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(56340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + h <=> ic4h9o + h2',
 "chemkinKinetics": """
ic4h9oh+h=ic4h9o+h2                                 9.450e+02 3.140     8.701    
""",
 "rmgPyKinetics": Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + h <=> ic4h8oh-3 + h2',
 "chemkinKinetics": """
ic4h9oh+h=ic4h8oh-3+h2                              1.332e+06 2.540     6.756    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.332e+06, 'cm^3/(mol*s)'),
    n = 2.54,
    Ea = (6756, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + h <=> ic4h8oh-2 + h2',
 "chemkinKinetics": """
ic4h9oh+h=ic4h8oh-2+h2                              6.500e+05 2.400     4.471    
""",
 "rmgPyKinetics": Arrhenius(A=(650000, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + h <=> ic4h8oh-1 + h2',
 "chemkinKinetics": """
ic4h9oh+h=ic4h8oh-1+h2                              8.789e+04 2.680     2.915    
""",
 "rmgPyKinetics": Arrhenius(A=(87890, 'cm^3/(mol*s)'), n=2.68, Ea=(2915, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + oh <=> ic4h9o + h2o',
 "chemkinKinetics": """
ic4h9oh+oh=ic4h9o+h2o                               5.880e+02 2.820     -0.585   
""",
 "rmgPyKinetics": Arrhenius(A=(588, 'cm^3/(mol*s)'), n=2.82, Ea=(-585, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + oh <=> ic4h8oh-3 + h2o',
 "chemkinKinetics": """
ic4h9oh+oh=ic4h8oh-3+h2o                            7.670e+06 1.843     -0.148   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.67e+06, 'cm^3/(mol*s)'),
    n = 1.843,
    Ea = (-147.7, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + oh <=> ic4h8oh-2 + h2o',
 "chemkinKinetics": """
ic4h9oh+oh=ic4h8oh-2+h2o                            7.700e-01 3.700     -4.940   
""",
 "rmgPyKinetics": Arrhenius(A=(0.77, 'cm^3/(mol*s)'), n=3.7, Ea=(-4940, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + oh <=> ic4h8oh-1 + h2o',
 "chemkinKinetics": """
ic4h9oh+oh=ic4h8oh-1+h2o                            3.610e+03 2.890     -2.331   
""",
 "rmgPyKinetics": Arrhenius(A=(3610, 'cm^3/(mol*s)'), n=2.89, Ea=(-2331, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + o <=> ic4h9o + oh',
 "chemkinKinetics": """
ic4h9oh+o=ic4h9o+oh                                 1.460e-03 4.730     1.727    
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.00146, 'cm^3/(mol*s)'),
    n = 4.73,
    Ea = (1727, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + o <=> ic4h8oh-3 + oh',
 "chemkinKinetics": """
ic4h9oh+o=ic4h8oh-3+oh                              1.962e+06 2.430     4.750    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.962e+06, 'cm^3/(mol*s)'),
    n = 2.43,
    Ea = (4750, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + o <=> ic4h8oh-2 + oh',
 "chemkinKinetics": """
ic4h9oh+o=ic4h8oh-2+oh                              2.760e+05 2.450     2.830    
""",
 "rmgPyKinetics": Arrhenius(A=(276000, 'cm^3/(mol*s)'), n=2.45, Ea=(2830, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + o <=> ic4h8oh-1 + oh',
 "chemkinKinetics": """
ic4h9oh+o=ic4h8oh-1+oh                              7.250e+04 2.470     0.876    
""",
 "rmgPyKinetics": Arrhenius(A=(72500, 'cm^3/(mol*s)'), n=2.47, Ea=(876, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ho2 <=> ic4h9o + h2o2',
 "chemkinKinetics": """
ic4h9oh+ho2=ic4h9o+h2o2                             6.470e-07 5.300     10.530   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.47e-07, 'cm^3/(mol*s)'),
    n = 5.3,
    Ea = (10530, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ho2 <=> ic4h8oh-3 + h2o2',
 "chemkinKinetics": """
ic4h9oh+ho2=ic4h8oh-3+h2o2                          4.140e-04 4.760     14.850   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.000414, 'cm^3/(mol*s)'),
    n = 4.76,
    Ea = (14850, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ho2 <=> ic4h8oh-2 + h2o2',
 "chemkinKinetics": """
ic4h9oh+ho2=ic4h8oh-2+h2o2                          3.760e-03 4.520     11.710   
""",
 "rmgPyKinetics": Arrhenius(
    A = (0.00376, 'cm^3/(mol*s)'),
    n = 4.52,
    Ea = (11710, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ho2 <=> ic4h8oh-1 + h2o2',
 "chemkinKinetics": """
ic4h9oh+ho2=ic4h8oh-1+h2o2                          3.500e-05 5.260     8.668    
""",
 "rmgPyKinetics": Arrhenius(
    A = (3.5e-05, 'cm^3/(mol*s)'),
    n = 5.26,
    Ea = (8668, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch3 <=> ic4h9o + ch4',
 "chemkinKinetics": """
ic4h9oh+ch3=ic4h9o+ch4                              1.020e+00 3.570     8.221    
""",
 "rmgPyKinetics": Arrhenius(A=(1.02, 'cm^3/(mol*s)'), n=3.57, Ea=(8221, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch3 <=> ic4h8oh-3 + ch4',
 "chemkinKinetics": """
ic4h9oh+ch3=ic4h8oh-3+ch4                           9.060e-01 3.650     7.154    
""",
 "rmgPyKinetics": Arrhenius(A=(0.906, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch3 <=> ic4h8oh-2 + ch4',
 "chemkinKinetics": """
ic4h9oh+ch3=ic4h8oh-2+ch4                           7.550e-01 3.460     5.481    
""",
 "rmgPyKinetics": Arrhenius(A=(0.755, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch3 <=> ic4h8oh-1 + ch4',
 "chemkinKinetics": """
ic4h9oh+ch3=ic4h8oh-1+ch4                           1.993e+01 3.370     7.634    
""",
 "rmgPyKinetics": Arrhenius(A=(19.93, 'cm^3/(mol*s)'), n=3.37, Ea=(7634, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + hco <=> ic4h9o + ch2o',
 "chemkinKinetics": """
ic4h9oh+hco=ic4h9o+ch2o                             3.400e+04 2.500     13.500   
""",
 "rmgPyKinetics": Arrhenius(A=(34000, 'cm^3/(mol*s)'), n=2.5, Ea=(13500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + hco <=> ic4h8oh-3 + ch2o',
 "chemkinKinetics": """
ic4h9oh+hco=ic4h8oh-3+ch2o                          2.040e+05 2.500     18.440   
""",
 "rmgPyKinetics": Arrhenius(A=(204000, 'cm^3/(mol*s)'), n=2.5, Ea=(18440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + hco <=> ic4h8oh-2 + ch2o',
 "chemkinKinetics": """
ic4h9oh+hco=ic4h8oh-2+ch2o                          5.450e+06 1.900     17.010   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5.45e+06, 'cm^3/(mol*s)'),
    n = 1.9,
    Ea = (17010, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + hco <=> ic4h8oh-1 + ch2o',
 "chemkinKinetics": """
ic4h9oh+hco=ic4h8oh-1+ch2o                          1.000e+07 1.900     17.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=1.9, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch2oh <=> ic4h9o + ch3oh',
 "chemkinKinetics": """
ic4h9oh+ch2oh=ic4h9o+ch3oh                          1.200e+02 2.760     10.800   
""",
 "rmgPyKinetics": Arrhenius(A=(120, 'cm^3/(mol*s)'), n=2.76, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch2oh <=> ic4h8oh-3 + ch3oh',
 "chemkinKinetics": """
ic4h9oh+ch2oh=ic4h8oh-3+ch3oh                       2.020e+02 2.950     13.970   
""",
 "rmgPyKinetics": Arrhenius(A=(202, 'cm^3/(mol*s)'), n=2.95, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch2oh <=> ic4h8oh-2 + ch3oh',
 "chemkinKinetics": """
ic4h9oh+ch2oh=ic4h8oh-2+ch3oh                       3.010e+01 2.950     11.980   
""",
 "rmgPyKinetics": Arrhenius(A=(30.1, 'cm^3/(mol*s)'), n=2.95, Ea=(11980, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch2oh <=> ic4h8oh-1 + ch3oh',
 "chemkinKinetics": """
ic4h9oh+ch2oh=ic4h8oh-1+ch3oh                       6.000e+01 2.950     12.000   
""",
 "rmgPyKinetics": Arrhenius(A=(60, 'cm^3/(mol*s)'), n=2.95, Ea=(12000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch3o <=> ic4h9o + ch3oh',
 "chemkinKinetics": """
ic4h9oh+ch3o=ic4h9o+ch3oh                           2.300e+10 0.000     2.900    
""",
 "rmgPyKinetics": Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch3o <=> ic4h8oh-3 + ch3oh',
 "chemkinKinetics": """
ic4h9oh+ch3o=ic4h8oh-3+ch3oh                        4.340e+11 0.000     6.458    
""",
 "rmgPyKinetics": Arrhenius(A=(4.34e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch3o <=> ic4h8oh-2 + ch3oh',
 "chemkinKinetics": """
ic4h9oh+ch3o=ic4h8oh-2+ch3oh                        7.250e+10 0.000     4.571    
""",
 "rmgPyKinetics": Arrhenius(A=(7.25e+10, 'cm^3/(mol*s)'), n=0, Ea=(4571, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch3o <=> ic4h8oh-1 + ch3oh',
 "chemkinKinetics": """
ic4h9oh+ch3o=ic4h8oh-1+ch3oh                        7.500e+10 0.000     4.500    
""",
 "rmgPyKinetics": Arrhenius(A=(7.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch3o2 <=> ic4h9o + ch3o2h',
 "chemkinKinetics": """
ic4h9oh+ch3o2=ic4h9o+ch3o2h                         1.500e+12 0.000     15.000   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch3o2 <=> ic4h8oh-3 + ch3o2h',
 "chemkinKinetics": """
ic4h9oh+ch3o2=ic4h8oh-3+ch3o2h                      4.760e+04 2.550     16.490   
""",
 "rmgPyKinetics": Arrhenius(A=(47600, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch3o2 <=> ic4h8oh-2 + ch3o2h',
 "chemkinKinetics": """
ic4h9oh+ch3o2=ic4h8oh-2+ch3o2h                      4.820e+03 2.600     13.910   
""",
 "rmgPyKinetics": Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + ch3o2 <=> ic4h8oh-1 + ch3o2h',
 "chemkinKinetics": """
ic4h9oh+ch3o2=ic4h8oh-1+ch3o2h                      1.500e+12 0.000     17.500   
""",
 "rmgPyKinetics": Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + c2h5 <=> ic4h9o + c2h6',
 "chemkinKinetics": """
ic4h9oh+c2h5=ic4h9o+c2h6                            1.670e+10 0.000     13.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1.67e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + c2h5 <=> ic4h8oh-3 + c2h6',
 "chemkinKinetics": """
ic4h9oh+c2h5=ic4h8oh-3+c2h6                         1.000e+11 0.000     13.400   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + c2h5 <=> ic4h8oh-2 + c2h6',
 "chemkinKinetics": """
ic4h9oh+c2h5=ic4h8oh-2+c2h6                         1.010e+11 0.000     7.900    
""",
 "rmgPyKinetics": Arrhenius(A=(1.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + c2h5 <=> ic4h8oh-1 + c2h6',
 "chemkinKinetics": """
ic4h9oh+c2h5=ic4h8oh-1+c2h6                         2.010e+11 0.000     7.900    
""",
 "rmgPyKinetics": Arrhenius(A=(2.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + o2 <=> ho2 + ic4h8oh-3',
 "chemkinKinetics": """
ic4h9oh+o2=ho2+ic4h8oh-3                            6.000e+13 0.000     52.340   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + o2 <=> ho2 + ic4h8oh-2',
 "chemkinKinetics": """
ic4h9oh+o2=ho2+ic4h8oh-2                            2.000e+13 0.000     48.200   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(48200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + o2 <=> ho2 + ic4h8oh-1',
 "chemkinKinetics": """
ic4h9oh+o2=ho2+ic4h8oh-1                            2.000e+13 0.000     46.800   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(46800, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h9oh + o2 <=> ho2 + ic4h9o',
 "chemkinKinetics": """
ic4h9oh+o2=ho2+ic4h9o                               1.000e+13 0.000     56.340   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(56340, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8 + oh <=> tc4h8oh',
 "chemkinKinetics": """
ic4h8+oh=tc4h8oh                                    9.930e+11 0.000     -0.960   
""",
 "rmgPyKinetics": Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h5oh + ch3 <=> tc4h8oh',
 "chemkinKinetics": """
ic3h5oh+ch3=tc4h8oh                                 1.300e+03 2.480     8.520    
""",
 "rmgPyKinetics": Arrhenius(A=(1300, 'cm^3/(mol*s)'), n=2.48, Ea=(8520, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3chchoh + ch3 <=> ic4h8oh-1',
 "chemkinKinetics": """
ch3chchoh+ch3=ic4h8oh-1                             1.890e+03 2.670     6.850    
""",
 "rmgPyKinetics": Arrhenius(A=(1890, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h6choh + h <=> ic4h8oh-1',
 "chemkinKinetics": """
ic3h6choh+h=ic4h8oh-1                               6.250e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.25e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h7cho + h <=> ic4h8oh-1',
 "chemkinKinetics": """
ic3h7cho+h=ic4h8oh-1                                8.000e+12 0.000     9.500    
""",
 "rmgPyKinetics": Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h5ch2oh + h <=> ic4h8oh-2',
 "chemkinKinetics": """
ic3h5ch2oh+h=ic4h8oh-2                              1.060e+12 0.510     1.230    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.06e+12, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (1230, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h6choh + h <=> ic4h8oh-2',
 "chemkinKinetics": """
ic3h6choh+h=ic4h8oh-2                               2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h8 + oh <=> ic4h8oh-2',
 "chemkinKinetics": """
ic4h8+oh=ic4h8oh-2                                  9.930e+11 0.000     -0.960   
""",
 "rmgPyKinetics": Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2oh + c3h6 <=> ic4h8oh-3',
 "chemkinKinetics": """
ch2oh+c3h6=ic4h8oh-3                                9.450e+02 2.670     6.850    
""",
 "rmgPyKinetics": Arrhenius(A=(945, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3 + c3h5oh <=> ic4h8oh-3',
 "chemkinKinetics": """
ch3+c3h5oh=ic4h8oh-3                                1.890e+03 2.670     6.850    
""",
 "rmgPyKinetics": Arrhenius(A=(1890, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h5ch2oh + h <=> ic4h8oh-3',
 "chemkinKinetics": """
ic3h5ch2oh+h=ic4h8oh-3                              6.250e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (6.25e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'h + c4h7oh1-2 <=> sc4h8ohm',
 "chemkinKinetics": """
h+c4h7oh1-2=sc4h8ohm                                2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'oh + c4h8-1 <=> sc4h8ohm',
 "chemkinKinetics": """
oh+c4h8-1=sc4h8ohm                                  9.930e+11 0.000     -0.960   
""",
 "rmgPyKinetics": Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h3oh + c2h5 <=> sc4h8ohm',
 "chemkinKinetics": """
c2h3oh+c2h5=sc4h8ohm                                8.800e+03 2.480     6.130    
""",
 "rmgPyKinetics": Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh1-2 + h <=> sc4h8oh-1',
 "chemkinKinetics": """
c4h7oh1-2+h=sc4h8oh-1                               4.240e+11 0.510     1.230    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.24e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (1230, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h5coch3 + h <=> sc4h8oh-1',
 "chemkinKinetics": """
c2h5coch3+h=sc4h8oh-1                               8.000e+12 0.000     9.500    
""",
 "rmgPyKinetics": Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh2-2 + h <=> sc4h8oh-1',
 "chemkinKinetics": """
c4h7oh2-2+h=sc4h8oh-1                               2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3 + ic3h5oh <=> sc4h8oh-1',
 "chemkinKinetics": """
ch3+ic3h5oh=sc4h8oh-1                               1.760e+04 2.480     6.130    
""",
 "rmgPyKinetics": Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3chchoh + ch3 <=> sc4h8oh-2',
 "chemkinKinetics": """
ch3chchoh+ch3=sc4h8oh-2                             1.890e+03 2.670     6.850    
""",
 "rmgPyKinetics": Arrhenius(A=(1890, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh2-2 + h <=> sc4h8oh-2',
 "chemkinKinetics": """
c4h7oh2-2+h=sc4h8oh-2                               2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h8-2 + oh <=> sc4h8oh-2',
 "chemkinKinetics": """
c4h8-2+oh=sc4h8oh-2                                 9.930e+11 0.000     -0.960   
""",
 "rmgPyKinetics": Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh1-3 + h <=> sc4h8oh-2',
 "chemkinKinetics": """
c4h7oh1-3+h=sc4h8oh-2                               4.240e+11 0.510     1.230    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.24e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (1230, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh1-3 + h <=> sc4h8oh-3',
 "chemkinKinetics": """
c4h7oh1-3+h=sc4h8oh-3                               2.500e+11 0.510     2.620    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+11, 'cm^3/(mol*s)'),
    n = 0.51,
    Ea = (2620, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'sc2h4oh + c2h4 <=> sc4h8oh-3',
 "chemkinKinetics": """
sc2h4oh+c2h4=sc4h8oh-3                              9.450e+02 2.670     6.850    
""",
 "rmgPyKinetics": Arrhenius(A=(945, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'sc4h9o <=> sc4h8oh-3',
 "chemkinKinetics": """
sc4h9o=sc4h8oh-3                                    2.300e-16 8.112     4.449    
""",
 "rmgPyKinetics": Arrhenius(A=(2.3e-16, 's^-1'), n=8.112, Ea=(4449, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h9o <=> ic4h8oh-3',
 "chemkinKinetics": """
ic4h9o=ic4h8oh-3                                    1.590e-15 7.838     4.655    
""",
 "rmgPyKinetics": Arrhenius(A=(1.59e-15, 's^-1'), n=7.838, Ea=(4655, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-1 + o2 <=> nc3h7cho + ho2',
 "chemkinKinetics": """
c4h8oh-1+o2=nc3h7cho+ho2                            1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.260e+17 -1.637    0.838    /
    PLOG/ 0.010     5.260e+17 -1.637    0.838    /
    PLOG/ 0.100     5.260e+17 -1.637    0.838    /
    PLOG/ 1.000     5.280e+17 -1.638    0.839    /
    PLOG/ 10.000    1.540e+18 -1.771    1.120    /
    PLOG/ 100.000   3.780e+20 -2.429    3.090    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.28e+17, 'cm^3/(mol*s)'),
            n = -1.638,
            Ea = (839, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.54e+18, 'cm^3/(mol*s)'),
            n = -1.771,
            Ea = (1120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+20, 'cm^3/(mol*s)'),
            n = -2.429,
            Ea = (3090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h8oh-1 + o2 <=> ic3h7cho + ho2',
 "chemkinKinetics": """
ic4h8oh-1+o2=ic3h7cho+ho2                           1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.260e+17 -1.637    0.838    /
    PLOG/ 0.010     5.260e+17 -1.637    0.838    /
    PLOG/ 0.100     5.260e+17 -1.637    0.838    /
    PLOG/ 1.000     5.280e+17 -1.638    0.839    /
    PLOG/ 10.000    1.540e+18 -1.771    1.120    /
    PLOG/ 100.000   3.780e+20 -2.429    3.090    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.28e+17, 'cm^3/(mol*s)'),
            n = -1.638,
            Ea = (839, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.54e+18, 'cm^3/(mol*s)'),
            n = -1.771,
            Ea = (1120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+20, 'cm^3/(mol*s)'),
            n = -2.429,
            Ea = (3090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'sc4h8oh-1 + o2 <=> c2h5coch3 + ho2',
 "chemkinKinetics": """
sc4h8oh-1+o2=c2h5coch3+ho2                          1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.260e+17 -1.637    0.838    /
    PLOG/ 0.010     5.260e+17 -1.637    0.838    /
    PLOG/ 0.100     5.260e+17 -1.637    0.838    /
    PLOG/ 1.000     5.280e+17 -1.638    0.839    /
    PLOG/ 10.000    1.540e+18 -1.771    1.120    /
    PLOG/ 100.000   3.780e+20 -2.429    3.090    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.28e+17, 'cm^3/(mol*s)'),
            n = -1.638,
            Ea = (839, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.54e+18, 'cm^3/(mol*s)'),
            n = -1.771,
            Ea = (1120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+20, 'cm^3/(mol*s)'),
            n = -2.429,
            Ea = (3090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h8oh-1 + o2 <=> c4h8oh-1o2',
 "chemkinKinetics": """
c4h8oh-1+o2=c4h8oh-1o2                              1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8oh-2 + o2 <=> c4h8oh-2o2',
 "chemkinKinetics": """
c4h8oh-2+o2=c4h8oh-2o2                              7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8oh-3 + o2 <=> c4h8oh-3o2',
 "chemkinKinetics": """
c4h8oh-3+o2=c4h8oh-3o2                              7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8oh-4 + o2 <=> c4h8oh-4o2',
 "chemkinKinetics": """
c4h8oh-4+o2=c4h8oh-4o2                              4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8oh-1 + c4h8oh-1o2 <=> c4h8oh-1o + c4h8oh-1o',
 "chemkinKinetics": """
c4h8oh-1+c4h8oh-1o2=c4h8oh-1o+c4h8oh-1o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-1 + c4h8oh-2o2 <=> c4h8oh-1o + c4h8oh-2o',
 "chemkinKinetics": """
c4h8oh-1+c4h8oh-2o2=c4h8oh-1o+c4h8oh-2o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-1 + c4h8oh-3o2 <=> c4h8oh-1o + c4h8oh-3o',
 "chemkinKinetics": """
c4h8oh-1+c4h8oh-3o2=c4h8oh-1o+c4h8oh-3o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-1 + c4h8oh-4o2 <=> c4h8oh-1o + c4h8oh-4o',
 "chemkinKinetics": """
c4h8oh-1+c4h8oh-4o2=c4h8oh-1o+c4h8oh-4o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-2 + c4h8oh-1o2 <=> c4h8oh-2o + c4h8oh-1o',
 "chemkinKinetics": """
c4h8oh-2+c4h8oh-1o2=c4h8oh-2o+c4h8oh-1o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-2 + c4h8oh-2o2 <=> c4h8oh-2o + c4h8oh-2o',
 "chemkinKinetics": """
c4h8oh-2+c4h8oh-2o2=c4h8oh-2o+c4h8oh-2o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-2 + c4h8oh-3o2 <=> c4h8oh-2o + c4h8oh-3o',
 "chemkinKinetics": """
c4h8oh-2+c4h8oh-3o2=c4h8oh-2o+c4h8oh-3o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-2 + c4h8oh-4o2 <=> c4h8oh-2o + c4h8oh-4o',
 "chemkinKinetics": """
c4h8oh-2+c4h8oh-4o2=c4h8oh-2o+c4h8oh-4o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-3 + c4h8oh-1o2 <=> c4h8oh-3o + c4h8oh-1o',
 "chemkinKinetics": """
c4h8oh-3+c4h8oh-1o2=c4h8oh-3o+c4h8oh-1o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-3 + c4h8oh-2o2 <=> c4h8oh-3o + c4h8oh-2o',
 "chemkinKinetics": """
c4h8oh-3+c4h8oh-2o2=c4h8oh-3o+c4h8oh-2o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-3 + c4h8oh-3o2 <=> c4h8oh-3o + c4h8oh-3o',
 "chemkinKinetics": """
c4h8oh-3+c4h8oh-3o2=c4h8oh-3o+c4h8oh-3o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-3 + c4h8oh-4o2 <=> c4h8oh-3o + c4h8oh-4o',
 "chemkinKinetics": """
c4h8oh-3+c4h8oh-4o2=c4h8oh-3o+c4h8oh-4o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-4 + c4h8oh-1o2 <=> c4h8oh-4o + c4h8oh-1o',
 "chemkinKinetics": """
c4h8oh-4+c4h8oh-1o2=c4h8oh-4o+c4h8oh-1o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-4 + c4h8oh-2o2 <=> c4h8oh-4o + c4h8oh-2o',
 "chemkinKinetics": """
c4h8oh-4+c4h8oh-2o2=c4h8oh-4o+c4h8oh-2o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-4 + c4h8oh-3o2 <=> c4h8oh-4o + c4h8oh-3o',
 "chemkinKinetics": """
c4h8oh-4+c4h8oh-3o2=c4h8oh-4o+c4h8oh-3o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-4 + c4h8oh-4o2 <=> c4h8oh-4o + c4h8oh-4o',
 "chemkinKinetics": """
c4h8oh-4+c4h8oh-4o2=c4h8oh-4o+c4h8oh-4o             7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-1 + ho2 <=> c4h8oh-1o + oh',
 "chemkinKinetics": """
c4h8oh-1+ho2=c4h8oh-1o+oh                           7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-2 + ho2 <=> c4h8oh-2o + oh',
 "chemkinKinetics": """
c4h8oh-2+ho2=c4h8oh-2o+oh                           7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-3 + ho2 <=> c4h8oh-3o + oh',
 "chemkinKinetics": """
c4h8oh-3+ho2=c4h8oh-3o+oh                           7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-4 + ho2 <=> c4h8oh-4o + oh',
 "chemkinKinetics": """
c4h8oh-4+ho2=c4h8oh-4o+oh                           7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-1 + ch3o2 <=> c4h8oh-1o + ch3o',
 "chemkinKinetics": """
c4h8oh-1+ch3o2=c4h8oh-1o+ch3o                       7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-2 + ch3o2 <=> c4h8oh-2o + ch3o',
 "chemkinKinetics": """
c4h8oh-2+ch3o2=c4h8oh-2o+ch3o                       7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-3 + ch3o2 <=> c4h8oh-3o + ch3o',
 "chemkinKinetics": """
c4h8oh-3+ch3o2=c4h8oh-3o+ch3o                       7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-4 + ch3o2 <=> c4h8oh-4o + ch3o',
 "chemkinKinetics": """
c4h8oh-4+ch3o2=c4h8oh-4o+ch3o                       7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-1o2 <=> c4h7oh-1ooh-2',
 "chemkinKinetics": """
c4h8oh-1o2=c4h7oh-1ooh-2                            2.000e+11 0.000     28.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(28450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-1o2 <=> c4h7oh-1ooh-3',
 "chemkinKinetics": """
c4h8oh-1o2=c4h7oh-1ooh-3                            2.500e+10 0.000     20.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(20450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-1o2 <=> c4h7oh-1ooh-4',
 "chemkinKinetics": """
c4h8oh-1o2=c4h7oh-1ooh-4                            4.688e+09 0.000     21.950   
""",
 "rmgPyKinetics": Arrhenius(A=(4.688e+09, 's^-1'), n=0, Ea=(21950, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-2o2 => c2h5cho + ch2o + oh',
 "chemkinKinetics": """
c4h8oh-2o2=>c2h5cho+ch2o+oh                         2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products3',  ],
},

{
 "reaction": 'c4h8oh-2o2 <=> c4h7oh-2ooh-4',
 "chemkinKinetics": """
c4h8oh-2o2=c4h7oh-2ooh-4                            3.750e+10 0.000     24.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-2o2 <=> c4h7oh-2ooh-3',
 "chemkinKinetics": """
c4h8oh-2o2=c4h7oh-2ooh-3                            2.000e+11 0.000     26.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-2o2 <=> c4h7oh-2ooh-1',
 "chemkinKinetics": """
c4h8oh-2o2=c4h7oh-2ooh-1                            2.000e+11 0.000     24.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(24450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-3o2 <=> c4h7oh-3ooh-1',
 "chemkinKinetics": """
c4h8oh-3o2=c4h7oh-3ooh-1                            2.500e+10 0.000     18.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(18450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-3o2 <=> c4h7oh-3ooh-4',
 "chemkinKinetics": """
c4h8oh-3o2=c4h7oh-3ooh-4                            3.000e+11 0.000     29.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(29000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-3o2 <=> c4h7oh-3ooh-2',
 "chemkinKinetics": """
c4h8oh-3o2=c4h7oh-3ooh-2                            2.000e+11 0.000     28.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(28450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-4o2 <=> c4h7oh-4ooh-3',
 "chemkinKinetics": """
c4h8oh-4o2=c4h7oh-4ooh-3                            2.000e+11 0.000     26.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-4o2 <=> c4h7oh-4ooh-2',
 "chemkinKinetics": """
c4h8oh-4o2=c4h7oh-4ooh-2                            2.500e+10 0.000     22.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(22450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-4o2 <=> c4h7oh-4ooh-1',
 "chemkinKinetics": """
c4h8oh-4o2=c4h7oh-4ooh-1                            3.120e+09 0.000     16.650   
""",
 "rmgPyKinetics": Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(16650, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'c4h8oh-1o2 <=> c4h7oh1-1 + ho2',
 "chemkinKinetics": """
c4h8oh-1o2=c4h7oh1-1+ho2                            4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'c4h8oh-2o2 <=> c4h7oh1-1 + ho2',
 "chemkinKinetics": """
c4h8oh-2o2=c4h7oh1-1+ho2                            4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'c4h8oh-2o2 <=> c4h7oh2-1 + ho2',
 "chemkinKinetics": """
c4h8oh-2o2=c4h7oh2-1+ho2                            4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'c4h8oh-3o2 <=> ho2 + c4h7oh2-1',
 "chemkinKinetics": """
c4h8oh-3o2=ho2+c4h7oh2-1                            4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'c4h8oh-3o2 <=> c4h7oh1-4 + ho2',
 "chemkinKinetics": """
c4h8oh-3o2=c4h7oh1-4+ho2                            4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'c4h8oh-4o2 <=> ho2 + c4h7oh1-4',
 "chemkinKinetics": """
c4h8oh-4o2=ho2+c4h7oh1-4                            4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'c4h8oh-1o2 + ho2 <=> c4h8oh-1o2h + o2',
 "chemkinKinetics": """
c4h8oh-1o2+ho2=c4h8oh-1o2h+o2                       1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-2o2 + ho2 <=> c4h8oh-2o2h + o2',
 "chemkinKinetics": """
c4h8oh-2o2+ho2=c4h8oh-2o2h+o2                       1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-3o2 + ho2 <=> c4h8oh-3o2h + o2',
 "chemkinKinetics": """
c4h8oh-3o2+ho2=c4h8oh-3o2h+o2                       1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-4o2 + ho2 <=> c4h8oh-4o2h + o2',
 "chemkinKinetics": """
c4h8oh-4o2+ho2=c4h8oh-4o2h+o2                       1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-1o2 + h2o2 <=> c4h8oh-1o2h + ho2',
 "chemkinKinetics": """
c4h8oh-1o2+h2o2=c4h8oh-1o2h+ho2                     2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-2o2 + h2o2 <=> c4h8oh-2o2h + ho2',
 "chemkinKinetics": """
c4h8oh-2o2+h2o2=c4h8oh-2o2h+ho2                     2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-3o2 + h2o2 <=> c4h8oh-3o2h + ho2',
 "chemkinKinetics": """
c4h8oh-3o2+h2o2=c4h8oh-3o2h+ho2                     2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-4o2 + h2o2 <=> c4h8oh-4o2h + ho2',
 "chemkinKinetics": """
c4h8oh-4o2+h2o2=c4h8oh-4o2h+ho2                     2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'c4h8oh-1o2 + ch3o2 => c4h8oh-1o + ch3o + o2',
 "chemkinKinetics": """
c4h8oh-1o2+ch3o2=>c4h8oh-1o+ch3o+o2                 1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-2o2 + ch3o2 => c4h8oh-2o + ch3o + o2',
 "chemkinKinetics": """
c4h8oh-2o2+ch3o2=>c4h8oh-2o+ch3o+o2                 1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-3o2 + ch3o2 => c4h8oh-3o + ch3o + o2',
 "chemkinKinetics": """
c4h8oh-3o2+ch3o2=>c4h8oh-3o+ch3o+o2                 1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-4o2 + ch3o2 => c4h8oh-4o + ch3o + o2',
 "chemkinKinetics": """
c4h8oh-4o2+ch3o2=>c4h8oh-4o+ch3o+o2                 1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-1o2 + c4h8oh-1o2 => c4h8oh-1o + c4h8oh-1o + o2',
 "chemkinKinetics": """
c4h8oh-1o2+c4h8oh-1o2=>c4h8oh-1o+c4h8oh-1o+o2       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-1o2 + c4h8oh-2o2 => c4h8oh-1o + c4h8oh-2o + o2',
 "chemkinKinetics": """
c4h8oh-1o2+c4h8oh-2o2=>c4h8oh-1o+c4h8oh-2o+o2       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-1o2 + c4h8oh-3o2 => c4h8oh-1o + c4h8oh-3o + o2',
 "chemkinKinetics": """
c4h8oh-1o2+c4h8oh-3o2=>c4h8oh-1o+c4h8oh-3o+o2       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-1o2 + c4h8oh-4o2 => c4h8oh-1o + c4h8oh-4o + o2',
 "chemkinKinetics": """
c4h8oh-1o2+c4h8oh-4o2=>c4h8oh-1o+c4h8oh-4o+o2       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-2o2 + c4h8oh-2o2 => c4h8oh-2o + c4h8oh-2o + o2',
 "chemkinKinetics": """
c4h8oh-2o2+c4h8oh-2o2=>c4h8oh-2o+c4h8oh-2o+o2       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-2o2 + c4h8oh-3o2 => c4h8oh-2o + c4h8oh-3o + o2',
 "chemkinKinetics": """
c4h8oh-2o2+c4h8oh-3o2=>c4h8oh-2o+c4h8oh-3o+o2       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-2o2 + c4h8oh-4o2 => c4h8oh-2o + c4h8oh-4o + o2',
 "chemkinKinetics": """
c4h8oh-2o2+c4h8oh-4o2=>c4h8oh-2o+c4h8oh-4o+o2       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-3o2 + c4h8oh-3o2 => c4h8oh-3o + c4h8oh-3o + o2',
 "chemkinKinetics": """
c4h8oh-3o2+c4h8oh-3o2=>c4h8oh-3o+c4h8oh-3o+o2       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-3o2 + c4h8oh-4o2 => c4h8oh-3o + c4h8oh-4o + o2',
 "chemkinKinetics": """
c4h8oh-3o2+c4h8oh-4o2=>c4h8oh-3o+c4h8oh-4o+o2       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-4o2 + c4h8oh-4o2 => c4h8oh-4o + c4h8oh-4o + o2',
 "chemkinKinetics": """
c4h8oh-4o2+c4h8oh-4o2=>c4h8oh-4o+c4h8oh-4o+o2       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'c4h8oh-1o2h => c4h8oh-1o + oh',
 "chemkinKinetics": """
c4h8oh-1o2h=>c4h8oh-1o+oh                           1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8oh-2o2h => c4h8oh-2o + oh',
 "chemkinKinetics": """
c4h8oh-2o2h=>c4h8oh-2o+oh                           1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8oh-3o2h => c4h8oh-3o + oh',
 "chemkinKinetics": """
c4h8oh-3o2h=>c4h8oh-3o+oh                           1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h8oh-4o2h => c4h8oh-4o + oh',
 "chemkinKinetics": """
c4h8oh-4o2h=>c4h8oh-4o+oh                           1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'hocho + nc3h7 <=> c4h8oh-1o',
 "chemkinKinetics": """
hocho+nc3h7=c4h8oh-1o                               1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c2h5cho + ch2oh <=> c4h8oh-2o',
 "chemkinKinetics": """
c2h5cho+ch2oh=c4h8oh-2o                             1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3cho + pc2h4oh <=> c4h8oh-3o',
 "chemkinKinetics": """
ch3cho+pc2h4oh=c4h8oh-3o                            1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2o + c3h6oh-1 <=> c4h8oh-4o',
 "chemkinKinetics": """
ch2o+c3h6oh-1=c4h8oh-4o                             1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh-1ooh-2 => c4h7oho1-2 + oh',
 "chemkinKinetics": """
c4h7oh-1ooh-2=>c4h7oho1-2+oh                        6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh-1ooh-3 => c4h7oho1-3 + oh',
 "chemkinKinetics": """
c4h7oh-1ooh-3=>c4h7oho1-3+oh                        7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h7oh-1ooh-4 => c4h7oho1-4 + oh',
 "chemkinKinetics": """
c4h7oh-1ooh-4=>c4h7oho1-4+oh                        9.380e+09 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (9.38e+09, 's^-1'),
    n = 0,
    Ea = (7000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h7oh-2ooh-1 => c4h7oho1-2 + oh',
 "chemkinKinetics": """
c4h7oh-2ooh-1=>c4h7oho1-2+oh                        6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oh-2ooh-3 => c4h7oho2-3 + oh',
 "chemkinKinetics": """
c4h7oh-2ooh-3=>c4h7oho2-3+oh                        7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h7oh-2ooh-4 => c4h7oho2-4 + oh',
 "chemkinKinetics": """
c4h7oh-2ooh-4=>c4h7oho2-4+oh                        7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h7oh-3ooh-1 => c4h7oho1-3 + oh',
 "chemkinKinetics": """
c4h7oh-3ooh-1=>c4h7oho1-3+oh                        7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h7oh-3ooh-2 => c4h7oho2-3 + oh',
 "chemkinKinetics": """
c4h7oh-3ooh-2=>c4h7oho2-3+oh                        6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h7oh-3ooh-4 => c4h7oho3-4 + oh',
 "chemkinKinetics": """
c4h7oh-3ooh-4=>c4h7oho3-4+oh                        6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h7oh-4ooh-1 => c4h7oho1-4 + oh',
 "chemkinKinetics": """
c4h7oh-4ooh-1=>c4h7oho1-4+oh                        9.380e+09 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (9.38e+09, 's^-1'),
    n = 0,
    Ea = (7000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h7oh-4ooh-2 => c4h7oho2-4 + oh',
 "chemkinKinetics": """
c4h7oh-4ooh-2=>c4h7oho2-4+oh                        7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h7oh-4ooh-3 => c4h7oho3-4 + oh',
 "chemkinKinetics": """
c4h7oh-4ooh-3=>c4h7oho3-4+oh                        6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h7oh1-1 + ho2 <=> c4h7oh-1ooh-2',
 "chemkinKinetics": """
c4h7oh1-1+ho2=c4h7oh-1ooh-2                         1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh1-1 + ho2 <=> c4h7oh-2ooh-1',
 "chemkinKinetics": """
c4h7oh1-1+ho2=c4h7oh-2ooh-1                         1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh2-1 + ho2 <=> c4h7oh-2ooh-3',
 "chemkinKinetics": """
c4h7oh2-1+ho2=c4h7oh-2ooh-3                         1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh2-1 + ho2 <=> c4h7oh-3ooh-2',
 "chemkinKinetics": """
c4h7oh2-1+ho2=c4h7oh-3ooh-2                         1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh1-4 + ho2 <=> c4h7oh-3ooh-4',
 "chemkinKinetics": """
c4h7oh1-4+ho2=c4h7oh-3ooh-4                         1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh1-4 + ho2 <=> c4h7oh-4ooh-3',
 "chemkinKinetics": """
c4h7oh1-4+ho2=c4h7oh-4ooh-3                         1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh-1ooh-3 => oh + hocho + c3h6',
 "chemkinKinetics": """
c4h7oh-1ooh-3=>oh+hocho+c3h6                        1.000e+13 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+13, 's^-1'),
    n = 0,
    Ea = (30000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'c4h7oh-2ooh-4 => oh + hoch2cho + c2h4',
 "chemkinKinetics": """
c4h7oh-2ooh-4=>oh+hoch2cho+c2h4                     1.000e+13 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+13, 's^-1'),
    n = 0,
    Ea = (30000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'c4h7oh-3ooh-1 => oh + ch3cho + c2h3oh',
 "chemkinKinetics": """
c4h7oh-3ooh-1=>oh+ch3cho+c2h3oh                     1.000e+13 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+13, 's^-1'),
    n = 0,
    Ea = (30000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'c4h7oh-4ooh-2 => oh + ch2o + c3h5oh',
 "chemkinKinetics": """
c4h7oh-4ooh-2=>oh+ch2o+c3h5oh                       1.000e+13 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+13, 's^-1'),
    n = 0,
    Ea = (30000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'c4h7oh-2ooh-1 + o2 <=> nc4ket12 + ho2',
 "chemkinKinetics": """
c4h7oh-2ooh-1+o2=nc4ket12+ho2                       1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.260e+17 -1.637    0.838    /
    PLOG/ 0.010     5.260e+17 -1.637    0.838    /
    PLOG/ 0.100     5.260e+17 -1.637    0.838    /
    PLOG/ 1.000     5.280e+17 -1.638    0.839    /
    PLOG/ 10.000    1.540e+18 -1.771    1.120    /
    PLOG/ 100.000   3.780e+20 -2.429    3.090    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.28e+17, 'cm^3/(mol*s)'),
            n = -1.638,
            Ea = (839, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.54e+18, 'cm^3/(mol*s)'),
            n = -1.771,
            Ea = (1120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+20, 'cm^3/(mol*s)'),
            n = -2.429,
            Ea = (3090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h7oh-3ooh-1 + o2 <=> nc4ket13 + ho2',
 "chemkinKinetics": """
c4h7oh-3ooh-1+o2=nc4ket13+ho2                       1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.260e+17 -1.637    0.838    /
    PLOG/ 0.010     5.260e+17 -1.637    0.838    /
    PLOG/ 0.100     5.260e+17 -1.637    0.838    /
    PLOG/ 1.000     5.280e+17 -1.638    0.839    /
    PLOG/ 10.000    1.540e+18 -1.771    1.120    /
    PLOG/ 100.000   3.780e+20 -2.429    3.090    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.28e+17, 'cm^3/(mol*s)'),
            n = -1.638,
            Ea = (839, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.54e+18, 'cm^3/(mol*s)'),
            n = -1.771,
            Ea = (1120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+20, 'cm^3/(mol*s)'),
            n = -2.429,
            Ea = (3090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h7oh-4ooh-1 + o2 <=> nc4ket14 + ho2',
 "chemkinKinetics": """
c4h7oh-4ooh-1+o2=nc4ket14+ho2                       1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.260e+17 -1.637    0.838    /
    PLOG/ 0.010     5.260e+17 -1.637    0.838    /
    PLOG/ 0.100     5.260e+17 -1.637    0.838    /
    PLOG/ 1.000     5.280e+17 -1.638    0.839    /
    PLOG/ 10.000    1.540e+18 -1.771    1.120    /
    PLOG/ 100.000   3.780e+20 -2.429    3.090    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.28e+17, 'cm^3/(mol*s)'),
            n = -1.638,
            Ea = (839, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.54e+18, 'cm^3/(mol*s)'),
            n = -1.771,
            Ea = (1120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+20, 'cm^3/(mol*s)'),
            n = -2.429,
            Ea = (3090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'c4h7oh-1ooh-2 + o2 <=> c4h7oh-1ooh-2o2',
 "chemkinKinetics": """
c4h7oh-1ooh-2+o2=c4h7oh-1ooh-2o2                    7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh-1ooh-3 + o2 <=> c4h7oh-1ooh-3o2',
 "chemkinKinetics": """
c4h7oh-1ooh-3+o2=c4h7oh-1ooh-3o2                    7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh-1ooh-4 + o2 <=> c4h7oh-1ooh-4o2',
 "chemkinKinetics": """
c4h7oh-1ooh-4+o2=c4h7oh-1ooh-4o2                    4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh-2ooh-1 + o2 <=> c4h7oh-2ooh-1o2',
 "chemkinKinetics": """
c4h7oh-2ooh-1+o2=c4h7oh-2ooh-1o2                    1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh-2ooh-3 + o2 <=> c4h7oh-2ooh-3o2',
 "chemkinKinetics": """
c4h7oh-2ooh-3+o2=c4h7oh-2ooh-3o2                    7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh-2ooh-4 + o2 <=> c4h7oh-2ooh-4o2',
 "chemkinKinetics": """
c4h7oh-2ooh-4+o2=c4h7oh-2ooh-4o2                    4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh-3ooh-1 + o2 <=> c4h7oh-3ooh-1o2',
 "chemkinKinetics": """
c4h7oh-3ooh-1+o2=c4h7oh-3ooh-1o2                    1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh-3ooh-2 + o2 <=> c4h7oh-3ooh-2o2',
 "chemkinKinetics": """
c4h7oh-3ooh-2+o2=c4h7oh-3ooh-2o2                    7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh-3ooh-4 + o2 <=> c4h7oh-3ooh-4o2',
 "chemkinKinetics": """
c4h7oh-3ooh-4+o2=c4h7oh-3ooh-4o2                    4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh-4ooh-1 + o2 <=> c4h7oh-4ooh-1o2',
 "chemkinKinetics": """
c4h7oh-4ooh-1+o2=c4h7oh-4ooh-1o2                    1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh-4ooh-2 + o2 <=> c4h7oh-4ooh-2o2',
 "chemkinKinetics": """
c4h7oh-4ooh-2+o2=c4h7oh-4ooh-2o2                    7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh-4ooh-3 + o2 <=> c4h7oh-4ooh-3o2',
 "chemkinKinetics": """
c4h7oh-4ooh-3+o2=c4h7oh-4ooh-3o2                    7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'c4h7oh-1ooh-2o2 => c2h5cho + ho2cho + oh',
 "chemkinKinetics": """
c4h7oh-1ooh-2o2=>c2h5cho+ho2cho+oh                  2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products3',  ],
},

{
 "reaction": 'c4h7oh-3ooh-2o2 => c3ket12 + ch2o + oh',
 "chemkinKinetics": """
c4h7oh-3ooh-2o2=>c3ket12+ch2o+oh                    2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products3',  ],
},

{
 "reaction": 'c4h7oh-4ooh-2o2 => c3ket13 + ch2o + oh',
 "chemkinKinetics": """
c4h7oh-4ooh-2o2=>c3ket13+ch2o+oh                    2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products3',  ],
},

{
 "reaction": 'c4h7oh-1ooh-2o2 <=> c4ohket1-2 + oh',
 "chemkinKinetics": """
c4h7oh-1ooh-2o2=c4ohket1-2+oh                       1.000e+11 0.000     21.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(21450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h7oh-1ooh-3o2 <=> c4ohket1-3 + oh',
 "chemkinKinetics": """
c4h7oh-1ooh-3o2=c4ohket1-3+oh                       1.250e+10 0.000     15.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(15450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h7oh-1ooh-4o2 <=> c4ohket1-4 + oh',
 "chemkinKinetics": """
c4h7oh-1ooh-4o2=c4ohket1-4+oh                       1.560e+09 0.000     13.650   
""",
 "rmgPyKinetics": Arrhenius(A=(1.56e+09, 's^-1'), n=0, Ea=(13650, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h7oh-2ooh-1o2 <=> c4ohket2-1 + oh',
 "chemkinKinetics": """
c4h7oh-2ooh-1o2=c4ohket2-1+oh                       1.000e+11 0.000     25.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h7oh-2ooh-3o2 <=> c4ohket2-3 + oh',
 "chemkinKinetics": """
c4h7oh-2ooh-3o2=c4ohket2-3+oh                       1.000e+11 0.000     25.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h7oh-2ooh-4o2 <=> c4ohket2-4 + oh',
 "chemkinKinetics": """
c4h7oh-2ooh-4o2=c4ohket2-4+oh                       1.250e+10 0.000     19.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(19450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h7oh-3ooh-1o2 <=> c4ohket3-1 + oh',
 "chemkinKinetics": """
c4h7oh-3ooh-1o2=c4ohket3-1+oh                       1.250e+10 0.000     17.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(17450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h7oh-3ooh-2o2 <=> c4ohket3-2 + oh',
 "chemkinKinetics": """
c4h7oh-3ooh-2o2=c4ohket3-2+oh                       1.000e+11 0.000     23.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(23450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h7oh-3ooh-4o2 <=> c4ohket3-4 + oh',
 "chemkinKinetics": """
c4h7oh-3ooh-4o2=c4ohket3-4+oh                       1.000e+11 0.000     23.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(23450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h7oh-4ooh-1o2 <=> c4ohket4-1 + oh',
 "chemkinKinetics": """
c4h7oh-4ooh-1o2=c4ohket4-1+oh                       3.120e+09 0.000     18.950   
""",
 "rmgPyKinetics": Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(18950, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h7oh-4ooh-2o2 <=> c4ohket4-2 + oh',
 "chemkinKinetics": """
c4h7oh-4ooh-2o2=c4ohket4-2+oh                       2.500e+10 0.000     21.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4h7oh-4ooh-3o2 <=> c4ohket4-3 + oh',
 "chemkinKinetics": """
c4h7oh-4ooh-3o2=c4ohket4-3+oh                       2.000e+11 0.000     26.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'c4ohket1-2 => oh + ocho + c2h5cho',
 "chemkinKinetics": """
c4ohket1-2=>oh+ocho+c2h5cho                         1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4ohket1-3 => oh + ch2ocho + ch3cho',
 "chemkinKinetics": """
c4ohket1-3=>oh+ch2ocho+ch3cho                       1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4ohket1-4 => oh + c2h4 + ocho + ch2o',
 "chemkinKinetics": """
c4ohket1-4=>oh+c2h4+ocho+ch2o                       1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4ohket2-1 => oh + hocho + c2h5co',
 "chemkinKinetics": """
c4ohket2-1=>oh+hocho+c2h5co                         1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products1',  ],
},

{
 "reaction": 'c4ohket2-3 => oh + hoch2co + ch3cho',
 "chemkinKinetics": """
c4ohket2-3=>oh+hoch2co+ch3cho                       1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products1',  ],
},

{
 "reaction": 'c4ohket2-4 => oh + ch2co + ch2oh + ch2o',
 "chemkinKinetics": """
c4ohket2-4=>oh+ch2co+ch2oh+ch2o                     1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4ohket3-1 => oh + hocho + ch3coch2',
 "chemkinKinetics": """
c4ohket3-1=>oh+hocho+ch3coch2                       1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products1', 'Fake_3products1', 'Fake_3products1',  ],
},

{
 "reaction": 'c4ohket3-2 => oh + hoch2cho + ch3co',
 "chemkinKinetics": """
c4ohket3-2=>oh+hoch2cho+ch3co                       1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products1',  ],
},

{
 "reaction": 'c4ohket3-4 => oh + hoc2h4co + ch2o',
 "chemkinKinetics": """
c4ohket3-4=>oh+hoc2h4co+ch2o                        1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products1',  ],
},

{
 "reaction": 'c4ohket4-1 => oh + hocho + ch2ch2cho',
 "chemkinKinetics": """
c4ohket4-1=>oh+hocho+ch2ch2cho                      1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products1', 'Fake_3products1', 'Fake_3products1',  ],
},

{
 "reaction": 'c4ohket4-2 => oh + hoch2cho + ch2cho',
 "chemkinKinetics": """
c4ohket4-2=>oh+hoch2cho+ch2cho                      1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products1', 'Fake_3products1', 'Fake_3products1',  ],
},

{
 "reaction": 'c4ohket4-3 => oh + hoc2h4cho + hco',
 "chemkinKinetics": """
c4ohket4-3=>oh+hoc2h4cho+hco                        1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products1',  ],
},

{
 "reaction": 'c4h7oho1-2 + oh => c3h5-s + hocho + h2o',
 "chemkinKinetics": """
c4h7oho1-2+oh=>c3h5-s+hocho+h2o                     2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oho1-3 + oh => c3h5-a + hocho + h2o',
 "chemkinKinetics": """
c4h7oho1-3+oh=>c3h5-a+hocho+h2o                     2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oho1-4 + oh => c3h5-a + hocho + h2o',
 "chemkinKinetics": """
c4h7oho1-4+oh=>c3h5-a+hocho+h2o                     2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oho2-3 + oh => c2h3cho + ch2oh + h2o',
 "chemkinKinetics": """
c4h7oho2-3+oh=>c2h3cho+ch2oh+h2o                    2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oho2-4 + oh => c2h3cho + ch2oh + h2o',
 "chemkinKinetics": """
c4h7oho2-4+oh=>c2h3cho+ch2oh+h2o                    2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oho3-4 + oh => pc2h4oh + ch2co + h2o',
 "chemkinKinetics": """
c4h7oho3-4+oh=>pc2h4oh+ch2co+h2o                    2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oho1-2 + ho2 => c3h5-s + hocho + h2o2',
 "chemkinKinetics": """
c4h7oho1-2+ho2=>c3h5-s+hocho+h2o2                   5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oho1-3 + ho2 => c3h5-a + hocho + h2o2',
 "chemkinKinetics": """
c4h7oho1-3+ho2=>c3h5-a+hocho+h2o2                   5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oho1-4 + ho2 => c3h5-a + hocho + h2o2',
 "chemkinKinetics": """
c4h7oho1-4+ho2=>c3h5-a+hocho+h2o2                   5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oho2-3 + ho2 => c2h3cho + ch2oh + h2o2',
 "chemkinKinetics": """
c4h7oho2-3+ho2=>c2h3cho+ch2oh+h2o2                  5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oho2-4 + ho2 => c2h3cho + ch2oh + h2o2',
 "chemkinKinetics": """
c4h7oho2-4+ho2=>c2h3cho+ch2oh+h2o2                  5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'c4h7oho3-4 + ho2 => pc2h4oh + ch2co + h2o2',
 "chemkinKinetics": """
c4h7oho3-4+ho2=>pc2h4oh+ch2co+h2o2                  5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hoch2cho + o2 <=> hoch2co + ho2',
 "chemkinKinetics": """
hoch2cho+o2=hoch2co+ho2                             2.000e+13 0.500     42.200   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0.5, Ea=(42200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoch2cho + oh <=> hoch2co + h2o',
 "chemkinKinetics": """
hoch2cho+oh=hoch2co+h2o                             2.690e+10 0.760     -0.340   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.69e+10, 'cm^3/(mol*s)'),
    n = 0.76,
    Ea = (-340, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoch2cho + h <=> hoch2co + h2',
 "chemkinKinetics": """
hoch2cho+h=hoch2co+h2                               4.000e+13 0.000     4.200    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoch2cho + o <=> hoch2co + oh',
 "chemkinKinetics": """
hoch2cho+o=hoch2co+oh                               5.000e+12 0.000     1.790    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1790, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoch2cho + ho2 <=> hoch2co + h2o2',
 "chemkinKinetics": """
hoch2cho+ho2=hoch2co+h2o2                           2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoch2cho + ch3 <=> hoch2co + ch4',
 "chemkinKinetics": """
hoch2cho+ch3=hoch2co+ch4                            1.700e+12 0.000     8.440    
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoch2cho + ch3o <=> hoch2co + ch3oh',
 "chemkinKinetics": """
hoch2cho+ch3o=hoch2co+ch3oh                         1.150e+11 0.000     1.280    
""",
 "rmgPyKinetics": Arrhenius(A=(1.15e+11, 'cm^3/(mol*s)'), n=0, Ea=(1280, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoch2cho + ch3o2 <=> hoch2co + ch3o2h',
 "chemkinKinetics": """
hoch2cho+ch3o2=hoch2co+ch3o2h                       1.000e+12 0.000     9.500    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoch2co <=> ch2oh + co',
 "chemkinKinetics": """
hoch2co=ch2oh+co                                    1.000e+11 0.000     9.600    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(9600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'hoc2h4cho + o2 <=> hoc2h4co + ho2',
 "chemkinKinetics": """
hoc2h4cho+o2=hoc2h4co+ho2                           2.000e+13 0.500     42.200   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0.5, Ea=(42200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoc2h4cho + oh <=> hoc2h4co + h2o',
 "chemkinKinetics": """
hoc2h4cho+oh=hoc2h4co+h2o                           2.690e+10 0.760     -0.340   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.69e+10, 'cm^3/(mol*s)'),
    n = 0.76,
    Ea = (-340, 'cal/mol'),
    T0 = (1, 'K'),
),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoc2h4cho + h <=> hoc2h4co + h2',
 "chemkinKinetics": """
hoc2h4cho+h=hoc2h4co+h2                             4.000e+13 0.000     4.200    
""",
 "rmgPyKinetics": Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4200, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoc2h4cho + o <=> hoc2h4co + oh',
 "chemkinKinetics": """
hoc2h4cho+o=hoc2h4co+oh                             5.000e+12 0.000     1.790    
""",
 "rmgPyKinetics": Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1790, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoc2h4cho + ho2 <=> hoc2h4co + h2o2',
 "chemkinKinetics": """
hoc2h4cho+ho2=hoc2h4co+h2o2                         2.800e+12 0.000     13.600   
""",
 "rmgPyKinetics": Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoc2h4cho + ch3 <=> hoc2h4co + ch4',
 "chemkinKinetics": """
hoc2h4cho+ch3=hoc2h4co+ch4                          1.700e+12 0.000     8.440    
""",
 "rmgPyKinetics": Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoc2h4cho + ch3o <=> hoc2h4co + ch3oh',
 "chemkinKinetics": """
hoc2h4cho+ch3o=hoc2h4co+ch3oh                       1.150e+11 0.000     1.280    
""",
 "rmgPyKinetics": Arrhenius(A=(1.15e+11, 'cm^3/(mol*s)'), n=0, Ea=(1280, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoc2h4cho + ch3o2 <=> hoc2h4co + ch3o2h',
 "chemkinKinetics": """
hoc2h4cho+ch3o2=hoc2h4co+ch3o2h                     1.000e+12 0.000     9.500    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'hoc2h4co <=> pc2h4oh + co',
 "chemkinKinetics": """
hoc2h4co=pc2h4oh+co                                 1.000e+11 0.000     9.600    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(9600, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h8oh-1 + o2 <=> ic4h8oh-1o2',
 "chemkinKinetics": """
ic4h8oh-1+o2=ic4h8oh-1o2                            1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h8oh-2 + o2 <=> ic4h8oh-2o2',
 "chemkinKinetics": """
ic4h8oh-2+o2=ic4h8oh-2o2                            1.410e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h8oh-3 + o2 <=> ic4h8oh-3o2',
 "chemkinKinetics": """
ic4h8oh-3+o2=ic4h8oh-3o2                            4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h8oh-1 + ic4h8oh-1o2 <=> ic4h8oh-1o + ic4h8oh-1o',
 "chemkinKinetics": """
ic4h8oh-1+ic4h8oh-1o2=ic4h8oh-1o+ic4h8oh-1o         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-1 + ic4h8oh-2o2 <=> ic4h8oh-1o + ic4h8oh-2o',
 "chemkinKinetics": """
ic4h8oh-1+ic4h8oh-2o2=ic4h8oh-1o+ic4h8oh-2o         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-1 + ic4h8oh-3o2 <=> ic4h8oh-1o + ic4h8oh-3o',
 "chemkinKinetics": """
ic4h8oh-1+ic4h8oh-3o2=ic4h8oh-1o+ic4h8oh-3o         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-2 + ic4h8oh-1o2 <=> ic4h8oh-2o + ic4h8oh-1o',
 "chemkinKinetics": """
ic4h8oh-2+ic4h8oh-1o2=ic4h8oh-2o+ic4h8oh-1o         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-2 + ic4h8oh-2o2 <=> ic4h8oh-2o + ic4h8oh-2o',
 "chemkinKinetics": """
ic4h8oh-2+ic4h8oh-2o2=ic4h8oh-2o+ic4h8oh-2o         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-2 + ic4h8oh-3o2 <=> ic4h8oh-2o + ic4h8oh-3o',
 "chemkinKinetics": """
ic4h8oh-2+ic4h8oh-3o2=ic4h8oh-2o+ic4h8oh-3o         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-3 + ic4h8oh-1o2 <=> ic4h8oh-3o + ic4h8oh-1o',
 "chemkinKinetics": """
ic4h8oh-3+ic4h8oh-1o2=ic4h8oh-3o+ic4h8oh-1o         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-3 + ic4h8oh-2o2 <=> ic4h8oh-3o + ic4h8oh-2o',
 "chemkinKinetics": """
ic4h8oh-3+ic4h8oh-2o2=ic4h8oh-3o+ic4h8oh-2o         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-3 + ic4h8oh-3o2 <=> ic4h8oh-3o + ic4h8oh-3o',
 "chemkinKinetics": """
ic4h8oh-3+ic4h8oh-3o2=ic4h8oh-3o+ic4h8oh-3o         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-1 + ho2 <=> ic4h8oh-1o + oh',
 "chemkinKinetics": """
ic4h8oh-1+ho2=ic4h8oh-1o+oh                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-2 + ho2 <=> ic4h8oh-2o + oh',
 "chemkinKinetics": """
ic4h8oh-2+ho2=ic4h8oh-2o+oh                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-3 + ho2 <=> ic4h8oh-3o + oh',
 "chemkinKinetics": """
ic4h8oh-3+ho2=ic4h8oh-3o+oh                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-1 + ch3o2 <=> ic4h8oh-1o + ch3o',
 "chemkinKinetics": """
ic4h8oh-1+ch3o2=ic4h8oh-1o+ch3o                     7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-2 + ch3o2 <=> ic4h8oh-2o + ch3o',
 "chemkinKinetics": """
ic4h8oh-2+ch3o2=ic4h8oh-2o+ch3o                     7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-3 + ch3o2 <=> ic4h8oh-3o + ch3o',
 "chemkinKinetics": """
ic4h8oh-3+ch3o2=ic4h8oh-3o+ch3o                     7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-1o2 <=> ic4h7oh-1ooh-2',
 "chemkinKinetics": """
ic4h8oh-1o2=ic4h7oh-1ooh-2                          1.000e+11 0.000     25.700   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h8oh-1o2 <=> ic4h7oh-1ooh-3',
 "chemkinKinetics": """
ic4h8oh-1o2=ic4h7oh-1ooh-3                          7.500e+10 0.000     24.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h8oh-2o2 => ch3coch3 + ch2o + oh',
 "chemkinKinetics": """
ic4h8oh-2o2=>ch3coch3+ch2o+oh                       2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products3',  ],
},

{
 "reaction": 'ic4h8oh-2o2 <=> ic4h7oh-2ooh-3',
 "chemkinKinetics": """
ic4h8oh-2o2=ic4h7oh-2ooh-3                          6.000e+11 0.000     29.000   
""",
 "rmgPyKinetics": Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(29000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h8oh-2o2 <=> ic4h7oh-2ooh-1',
 "chemkinKinetics": """
ic4h8oh-2o2=ic4h7oh-2ooh-1                          2.000e+11 0.000     25.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(25450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h8oh-3o2 <=> ic4h7oh-3ooh-1',
 "chemkinKinetics": """
ic4h8oh-3o2=ic4h7oh-3ooh-1                          2.500e+10 0.000     19.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(19450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h8oh-3o2 <=> ic4h7oh-3ooh-3',
 "chemkinKinetics": """
ic4h8oh-3o2=ic4h7oh-3ooh-3                          3.750e+10 0.000     24.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h8oh-3o2 <=> ic4h7oh-3ooh-2',
 "chemkinKinetics": """
ic4h8oh-3o2=ic4h7oh-3ooh-2                          1.000e+11 0.000     25.700   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25700, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'ic4h8oh-1o2 <=> ic3h6choh + ho2',
 "chemkinKinetics": """
ic4h8oh-1o2=ic3h6choh+ho2                           4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'ic4h8oh-2o2 <=> ic3h6choh + ho2',
 "chemkinKinetics": """
ic4h8oh-2o2=ic3h6choh+ho2                           4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'ic4h8oh-2o2 <=> ic3h5ch2oh + ho2',
 "chemkinKinetics": """
ic4h8oh-2o2=ic3h5ch2oh+ho2                          8.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(8.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'ic4h8oh-3o2 <=> ic3h5ch2oh + ho2',
 "chemkinKinetics": """
ic4h8oh-3o2=ic3h5ch2oh+ho2                          4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'ic4h8oh-1o2 + ho2 <=> ic4h8oh-1o2h + o2',
 "chemkinKinetics": """
ic4h8oh-1o2+ho2=ic4h8oh-1o2h+o2                     1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-2o2 + ho2 <=> ic4h8oh-2o2h + o2',
 "chemkinKinetics": """
ic4h8oh-2o2+ho2=ic4h8oh-2o2h+o2                     1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-3o2 + ho2 <=> ic4h8oh-3o2h + o2',
 "chemkinKinetics": """
ic4h8oh-3o2+ho2=ic4h8oh-3o2h+o2                     1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-1o2 + h2o2 <=> ic4h8oh-1o2h + ho2',
 "chemkinKinetics": """
ic4h8oh-1o2+h2o2=ic4h8oh-1o2h+ho2                   2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-2o2 + h2o2 <=> ic4h8oh-2o2h + ho2',
 "chemkinKinetics": """
ic4h8oh-2o2+h2o2=ic4h8oh-2o2h+ho2                   2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-3o2 + h2o2 <=> ic4h8oh-3o2h + ho2',
 "chemkinKinetics": """
ic4h8oh-3o2+h2o2=ic4h8oh-3o2h+ho2                   2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'ic4h8oh-1o2 + ch3o2 => ic4h8oh-1o + ch3o + o2',
 "chemkinKinetics": """
ic4h8oh-1o2+ch3o2=>ic4h8oh-1o+ch3o+o2               1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h8oh-2o2 + ch3o2 => ic4h8oh-2o + ch3o + o2',
 "chemkinKinetics": """
ic4h8oh-2o2+ch3o2=>ic4h8oh-2o+ch3o+o2               1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h8oh-3o2 + ch3o2 => ic4h8oh-3o + ch3o + o2',
 "chemkinKinetics": """
ic4h8oh-3o2+ch3o2=>ic4h8oh-3o+ch3o+o2               1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h8oh-1o2 + ic4h8oh-1o2 => ic4h8oh-1o + ic4h8oh-1o + o2',
 "chemkinKinetics": """
ic4h8oh-1o2+ic4h8oh-1o2=>ic4h8oh-1o+ic4h8oh-1o+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h8oh-1o2 + ic4h8oh-2o2 => ic4h8oh-1o + ic4h8oh-2o + o2',
 "chemkinKinetics": """
ic4h8oh-1o2+ic4h8oh-2o2=>ic4h8oh-1o+ic4h8oh-2o+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h8oh-1o2 + ic4h8oh-3o2 => ic4h8oh-1o + ic4h8oh-3o + o2',
 "chemkinKinetics": """
ic4h8oh-1o2+ic4h8oh-3o2=>ic4h8oh-1o+ic4h8oh-3o+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h8oh-2o2 + ic4h8oh-2o2 => ic4h8oh-2o + ic4h8oh-2o + o2',
 "chemkinKinetics": """
ic4h8oh-2o2+ic4h8oh-2o2=>ic4h8oh-2o+ic4h8oh-2o+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h8oh-2o2 + ic4h8oh-3o2 => ic4h8oh-2o + ic4h8oh-3o + o2',
 "chemkinKinetics": """
ic4h8oh-2o2+ic4h8oh-3o2=>ic4h8oh-2o+ic4h8oh-3o+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h8oh-3o2 + ic4h8oh-3o2 => ic4h8oh-3o + ic4h8oh-3o + o2',
 "chemkinKinetics": """
ic4h8oh-3o2+ic4h8oh-3o2=>ic4h8oh-3o+ic4h8oh-3o+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'ic4h8oh-1o2h => ic4h8oh-1o + oh',
 "chemkinKinetics": """
ic4h8oh-1o2h=>ic4h8oh-1o+oh                         1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h8oh-2o2h => ic4h8oh-2o + oh',
 "chemkinKinetics": """
ic4h8oh-2o2h=>ic4h8oh-2o+oh                         1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h8oh-3o2h => ic4h8oh-3o + oh',
 "chemkinKinetics": """
ic4h8oh-3o2h=>ic4h8oh-3o+oh                         1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'hocho + ic3h7 <=> ic4h8oh-1o',
 "chemkinKinetics": """
hocho+ic3h7=ic4h8oh-1o                              1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch3coch3 + ch2oh <=> ic4h8oh-2o',
 "chemkinKinetics": """
ch3coch3+ch2oh=ic4h8oh-2o                           1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2o + c3h6oh-2 <=> ic4h8oh-3o',
 "chemkinKinetics": """
ch2o+c3h6oh-2=ic4h8oh-3o                            1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h7oh-1ooh-2 => ic4h7oho1-2 + oh',
 "chemkinKinetics": """
ic4h7oh-1ooh-2=>ic4h7oho1-2+oh                      6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'ic4h7oh-1ooh-3 => ic4h7oho1-3 + oh',
 "chemkinKinetics": """
ic4h7oh-1ooh-3=>ic4h7oho1-3+oh                      7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'ic4h7oh-2ooh-1 => ic4h7oho1-2 + oh',
 "chemkinKinetics": """
ic4h7oh-2ooh-1=>ic4h7oho1-2+oh                      6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'ic4h7oh-2ooh-3 => ic4h7oho2-3 + oh',
 "chemkinKinetics": """
ic4h7oh-2ooh-3=>ic4h7oho2-3+oh                      7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'ic4h7oh-3ooh-1 => ic4h7oho1-3 + oh',
 "chemkinKinetics": """
ic4h7oh-3ooh-1=>ic4h7oho1-3+oh                      7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'ic4h7oh-3ooh-2 => ic4h7oho2-3 + oh',
 "chemkinKinetics": """
ic4h7oh-3ooh-2=>ic4h7oho2-3+oh                      6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'ic4h7oh-3ooh-3 => ic4h7oho3-3 + oh',
 "chemkinKinetics": """
ic4h7oh-3ooh-3=>ic4h7oho3-3+oh                      7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'ic3h6choh + ho2 <=> ic4h7oh-1ooh-2',
 "chemkinKinetics": """
ic3h6choh+ho2=ic4h7oh-1ooh-2                        1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h6choh + ho2 <=> ic4h7oh-2ooh-1',
 "chemkinKinetics": """
ic3h6choh+ho2=ic4h7oh-2ooh-1                        1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h5ch2oh + ho2 <=> ic4h7oh-2ooh-3',
 "chemkinKinetics": """
ic3h5ch2oh+ho2=ic4h7oh-2ooh-3                       1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic3h5ch2oh + ho2 <=> ic4h7oh-3ooh-2',
 "chemkinKinetics": """
ic3h5ch2oh+ho2=ic4h7oh-3ooh-2                       1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ic4h7oh-1ooh-3 => oh + hocho + c3h6',
 "chemkinKinetics": """
ic4h7oh-1ooh-3=>oh+hocho+c3h6                       1.000e+13 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+13, 's^-1'),
    n = 0,
    Ea = (30000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'ic4h7oh-3ooh-1 => oh + ch2o + c3h5oh',
 "chemkinKinetics": """
ic4h7oh-3ooh-1=>oh+ch2o+c3h5oh                      1.000e+13 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+13, 's^-1'),
    n = 0,
    Ea = (30000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7oh-3ooh-3 => oh + ch2o + c3h5oh',
 "chemkinKinetics": """
ic4h7oh-3ooh-3=>oh+ch2o+c3h5oh                      1.000e+13 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+13, 's^-1'),
    n = 0,
    Ea = (30000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'ic4h7oh-1ooh-2 + o2 <=> ic4h7oh-1ooh-2o2',
 "chemkinKinetics": """
ic4h7oh-1ooh-2+o2=ic4h7oh-1ooh-2o2                  1.410e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h7oh-1ooh-3 + o2 <=> ic4h7oh-1ooh-3o2',
 "chemkinKinetics": """
ic4h7oh-1ooh-3+o2=ic4h7oh-1ooh-3o2                  4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h7oh-2ooh-1 + o2 <=> ic4h7oh-2ooh-1o2',
 "chemkinKinetics": """
ic4h7oh-2ooh-1+o2=ic4h7oh-2ooh-1o2                  1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h7oh-2ooh-3 + o2 <=> ic4h7oh-2ooh-3o2',
 "chemkinKinetics": """
ic4h7oh-2ooh-3+o2=ic4h7oh-2ooh-3o2                  4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h7oh-3ooh-1 + o2 <=> ic4h7oh-3ooh-1o2',
 "chemkinKinetics": """
ic4h7oh-3ooh-1+o2=ic4h7oh-3ooh-1o2                  1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h7oh-3ooh-2 + o2 <=> ic4h7oh-3ooh-2o2',
 "chemkinKinetics": """
ic4h7oh-3ooh-2+o2=ic4h7oh-3ooh-2o2                  1.410e+13 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h7oh-3ooh-3 + o2 <=> ic4h7oh-3ooh-3o2',
 "chemkinKinetics": """
ic4h7oh-3ooh-3+o2=ic4h7oh-3ooh-3o2                  4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ic4h7oh-2ooh-1 + o2 <=> ic4ketit + ho2',
 "chemkinKinetics": """
ic4h7oh-2ooh-1+o2=ic4ketit+ho2                      1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.260e+17 -1.637    0.838    /
    PLOG/ 0.010     5.260e+17 -1.637    0.838    /
    PLOG/ 0.100     5.260e+17 -1.637    0.838    /
    PLOG/ 1.000     5.280e+17 -1.638    0.839    /
    PLOG/ 10.000    1.540e+18 -1.771    1.120    /
    PLOG/ 100.000   3.780e+20 -2.429    3.090    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.28e+17, 'cm^3/(mol*s)'),
            n = -1.638,
            Ea = (839, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.54e+18, 'cm^3/(mol*s)'),
            n = -1.771,
            Ea = (1120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+20, 'cm^3/(mol*s)'),
            n = -2.429,
            Ea = (3090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h7oh-3ooh-1 + o2 <=> ic4ketii + ho2',
 "chemkinKinetics": """
ic4h7oh-3ooh-1+o2=ic4ketii+ho2                      1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.260e+17 -1.637    0.838    /
    PLOG/ 0.010     5.260e+17 -1.637    0.838    /
    PLOG/ 0.100     5.260e+17 -1.637    0.838    /
    PLOG/ 1.000     5.280e+17 -1.638    0.839    /
    PLOG/ 10.000    1.540e+18 -1.771    1.120    /
    PLOG/ 100.000   3.780e+20 -2.429    3.090    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.28e+17, 'cm^3/(mol*s)'),
            n = -1.638,
            Ea = (839, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.54e+18, 'cm^3/(mol*s)'),
            n = -1.771,
            Ea = (1120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+20, 'cm^3/(mol*s)'),
            n = -2.429,
            Ea = (3090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'ic4h7oh-1ooh-2o2 => ch3coch3 + ho2cho + oh',
 "chemkinKinetics": """
ic4h7oh-1ooh-2o2=>ch3coch3+ho2cho+oh                2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products3',  ],
},

{
 "reaction": 'ic4h7oh-3ooh-2o2 => c3ket21 + ch2o + oh',
 "chemkinKinetics": """
ic4h7oh-3ooh-2o2=>c3ket21+ch2o+oh                   2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products3',  ],
},

{
 "reaction": 'ic4h7oh-1ooh-2o2 <=> ic4ohket1-2 + oh',
 "chemkinKinetics": """
ic4h7oh-1ooh-2o2=ic4ohket1-2+oh                     1.000e+11 0.000     22.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(22450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'ic4h7oh-1ooh-3o2 <=> ic4ohket1-3 + oh',
 "chemkinKinetics": """
ic4h7oh-1ooh-3o2=ic4ohket1-3+oh                     1.250e+10 0.000     16.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(16450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'ic4h7oh-2ooh-1o2 => ac3h5ooh + hocho + oh',
 "chemkinKinetics": """
ic4h7oh-2ooh-1o2=>ac3h5ooh+hocho+oh                 7.500e+10 0.000     24.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (24000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7oh-2ooh-3o2 => c3h4-a + ch2o + oh + oh + ho2',
 "chemkinKinetics": """
ic4h7oh-2ooh-3o2=>c3h4-a+ch2o+oh+oh+ho2             2.500e+10 0.000     19.450   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (19450, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7oh-3ooh-1o2 <=> ic4ohket3-1 + oh',
 "chemkinKinetics": """
ic4h7oh-3ooh-1o2=ic4ohket3-1+oh                     2.500e+10 0.000     21.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'ic4h7oh-3ooh-2o2 <=> ic4ohket3-2 + oh',
 "chemkinKinetics": """
ic4h7oh-3ooh-2o2=ic4ohket3-2+oh                     2.000e+11 0.000     26.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'ic4h7oh-3ooh-3o2 <=> ic4ohket3-3 + oh',
 "chemkinKinetics": """
ic4h7oh-3ooh-3o2=ic4ohket3-3+oh                     2.500e+10 0.000     21.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'ic4ohket1-2 => oh + ocho + ch3coch3',
 "chemkinKinetics": """
ic4ohket1-2=>oh+ocho+ch3coch3                       1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4ohket1-3 => oh + oh + ch3chco + ch2o',
 "chemkinKinetics": """
ic4ohket1-3=>oh+oh+ch3chco+ch2o                     1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4ohket3-1 => oh + hocho + ch2ch2cho',
 "chemkinKinetics": """
ic4ohket3-1=>oh+hocho+ch2ch2cho                     1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4ohket3-2 => oh + hoc2h4co + ch2o',
 "chemkinKinetics": """
ic4ohket3-2=>oh+hoc2h4co+ch2o                       1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4ohket3-3 => oh + hoc2h4cho + hco',
 "chemkinKinetics": """
ic4ohket3-3=>oh+hoc2h4cho+hco                       1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7oho1-2 + oh => c3h5-s + hocho + h2o',
 "chemkinKinetics": """
ic4h7oho1-2+oh=>c3h5-s+hocho+h2o                    2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7oho1-3 + oh => c3h5-a + hocho + h2o',
 "chemkinKinetics": """
ic4h7oho1-3+oh=>c3h5-a+hocho+h2o                    2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7oho2-3 + oh => ch2o + ch2cch2oh + h2o',
 "chemkinKinetics": """
ic4h7oho2-3+oh=>ch2o+ch2cch2oh+h2o                  2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7oho3-3 + oh => ch2o + ch2cch2oh + h2o',
 "chemkinKinetics": """
ic4h7oho3-3+oh=>ch2o+ch2cch2oh+h2o                  2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7oho1-2 + ho2 => c3h5-s + hocho + h2o2',
 "chemkinKinetics": """
ic4h7oho1-2+ho2=>c3h5-s+hocho+h2o2                  5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7oho1-3 + ho2 => c3h5-a + hocho + h2o2',
 "chemkinKinetics": """
ic4h7oho1-3+ho2=>c3h5-a+hocho+h2o2                  5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7oho2-3 + ho2 => ch2o + ch2cch2oh + h2o2',
 "chemkinKinetics": """
ic4h7oho2-3+ho2=>ch2o+ch2cch2oh+h2o2                5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ic4h7oho3-3 + ho2 => ch2o + ch2cch2oh + h2o2',
 "chemkinKinetics": """
ic4h7oho3-3+ho2=>ch2o+ch2cch2oh+h2o2                5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'tc4h8oh + o2 <=> tc4h8oh-o2',
 "chemkinKinetics": """
tc4h8oh+o2=tc4h8oh-o2                               4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.52e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV / 2.849E+20 -1.642 3.443E+04 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'tc4h8oh + tc4h8oh-o2 <=> tc4h8oh-o + tc4h8oh-o',
 "chemkinKinetics": """
tc4h8oh+tc4h8oh-o2=tc4h8oh-o+tc4h8oh-o              7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h8oh + ho2 <=> tc4h8oh-o + oh',
 "chemkinKinetics": """
tc4h8oh+ho2=tc4h8oh-o+oh                            7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h8oh + ch3o2 <=> tc4h8oh-o + ch3o',
 "chemkinKinetics": """
tc4h8oh+ch3o2=tc4h8oh-o+ch3o                        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'tc4h8oh-o2 <=> tc4h7oh-ooh',
 "chemkinKinetics": """
tc4h8oh-o2=tc4h7oh-ooh                              7.500e+10 0.000     27.000   
""",
 "rmgPyKinetics": Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(27000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'tc4h8oh-o2 => ch3coch3 + ch2o + oh',
 "chemkinKinetics": """
tc4h8oh-o2=>ch3coch3+ch2o+oh                        2.300e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.3e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products3',  ],
},

{
 "reaction": 'tc4h8oh-o2 => c3ket12 + ch3',
 "chemkinKinetics": """
tc4h8oh-o2=>c3ket12+ch3                             2.000e+09 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2e+09, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'tc4h8oh-o2 + ho2 <=> tc4h8oh-o2h + o2',
 "chemkinKinetics": """
tc4h8oh-o2+ho2=tc4h8oh-o2h+o2                       1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h8oh-o2 + h2o2 <=> tc4h8oh-o2h + ho2',
 "chemkinKinetics": """
tc4h8oh-o2+h2o2=tc4h8oh-o2h+ho2                     2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'tc4h8oh-o2 + ch3o2 => tc4h8oh-o + ch3o + o2',
 "chemkinKinetics": """
tc4h8oh-o2+ch3o2=>tc4h8oh-o+ch3o+o2                 1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'tc4h8oh-o2 + tc4h8oh-o2 => tc4h8oh-o + tc4h8oh-o + o2',
 "chemkinKinetics": """
tc4h8oh-o2+tc4h8oh-o2=>tc4h8oh-o+tc4h8oh-o+o2       1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'tc4h8oh-o2h => tc4h8oh-o + oh',
 "chemkinKinetics": """
tc4h8oh-o2h=>tc4h8oh-o+oh                           1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch2o + ic3h6oh <=> tc4h8oh-o',
 "chemkinKinetics": """
ch2o+ic3h6oh=tc4h8oh-o                              1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'tc4h7oh-ooh => tc4h7oho + oh',
 "chemkinKinetics": """
tc4h7oh-ooh=>tc4h7oho+oh                            7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'tc4h7oh-ooh => oh + ch2o + ic3h5oh',
 "chemkinKinetics": """
tc4h7oh-ooh=>oh+ch2o+ic3h5oh                        1.000e+13 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+13, 's^-1'),
    n = 0,
    Ea = (30000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'tc4h7oh-ooh + o2 <=> tc4h7oh-ooh-o2',
 "chemkinKinetics": """
tc4h7oh-ooh+o2=tc4h7oh-ooh-o2                       4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (4.52e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV / 2.849E+20 -1.642 3.443E+04 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'tc4h7oh-ooh-o2 => c3ket21 + ch2o + oh',
 "chemkinKinetics": """
tc4h7oh-ooh-o2=>c3ket21+ch2o+oh                     2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products3',  ],
},

{
 "reaction": 'tc4h7oh-ooh-o2 <=> tc4ohket + oh',
 "chemkinKinetics": """
tc4h7oh-ooh-o2=tc4ohket+oh                          2.500e+10 0.000     24.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'tc4ohket => oh + hoc2h4co + ch2o',
 "chemkinKinetics": """
tc4ohket=>oh+hoc2h4co+ch2o                          1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'tc4h7oho + oh => ch2o + ch2cch2oh + h2o',
 "chemkinKinetics": """
tc4h7oho+oh=>ch2o+ch2cch2oh+h2o                     2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'tc4h7oho + ho2 => ch2o + ch2cch2oh + h2o2',
 "chemkinKinetics": """
tc4h7oho+ho2=>ch2o+ch2cch2oh+h2o2                   5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h8oh-1 + o2 <=> sc4h8oh-1o2',
 "chemkinKinetics": """
sc4h8oh-1+o2=sc4h8oh-1o2                            1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h8oh-2 + o2 <=> sc4h8oh-2o2',
 "chemkinKinetics": """
sc4h8oh-2+o2=sc4h8oh-2o2                            7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h8oh-3 + o2 <=> sc4h8oh-3o2',
 "chemkinKinetics": """
sc4h8oh-3+o2=sc4h8oh-3o2                            4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h8ohm + o2 <=> sc4h8oh-mo2',
 "chemkinKinetics": """
sc4h8ohm+o2=sc4h8oh-mo2                             4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h8oh-1 + sc4h8oh-1o2 => sc4h8oh-1o + sc4h8oh-1o',
 "chemkinKinetics": """
sc4h8oh-1+sc4h8oh-1o2=>sc4h8oh-1o+sc4h8oh-1o        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-1 + sc4h8oh-2o2 => sc4h8oh-1o + sc4h8oh-2o',
 "chemkinKinetics": """
sc4h8oh-1+sc4h8oh-2o2=>sc4h8oh-1o+sc4h8oh-2o        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-1 + sc4h8oh-3o2 => sc4h8oh-1o + sc4h8oh-3o',
 "chemkinKinetics": """
sc4h8oh-1+sc4h8oh-3o2=>sc4h8oh-1o+sc4h8oh-3o        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-1 + sc4h8oh-mo2 => sc4h8oh-1o + sc4h8oh-mo',
 "chemkinKinetics": """
sc4h8oh-1+sc4h8oh-mo2=>sc4h8oh-1o+sc4h8oh-mo        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-2 + sc4h8oh-1o2 => sc4h8oh-2o + sc4h8oh-1o',
 "chemkinKinetics": """
sc4h8oh-2+sc4h8oh-1o2=>sc4h8oh-2o+sc4h8oh-1o        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-2 + sc4h8oh-2o2 => sc4h8oh-2o + sc4h8oh-2o',
 "chemkinKinetics": """
sc4h8oh-2+sc4h8oh-2o2=>sc4h8oh-2o+sc4h8oh-2o        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-2 + sc4h8oh-3o2 => sc4h8oh-2o + sc4h8oh-3o',
 "chemkinKinetics": """
sc4h8oh-2+sc4h8oh-3o2=>sc4h8oh-2o+sc4h8oh-3o        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-2 + sc4h8oh-mo2 => sc4h8oh-2o + sc4h8oh-mo',
 "chemkinKinetics": """
sc4h8oh-2+sc4h8oh-mo2=>sc4h8oh-2o+sc4h8oh-mo        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-3 + sc4h8oh-1o2 => sc4h8oh-3o + sc4h8oh-1o',
 "chemkinKinetics": """
sc4h8oh-3+sc4h8oh-1o2=>sc4h8oh-3o+sc4h8oh-1o        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-3 + sc4h8oh-2o2 => sc4h8oh-3o + sc4h8oh-2o',
 "chemkinKinetics": """
sc4h8oh-3+sc4h8oh-2o2=>sc4h8oh-3o+sc4h8oh-2o        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-3 + sc4h8oh-3o2 => sc4h8oh-3o + sc4h8oh-3o',
 "chemkinKinetics": """
sc4h8oh-3+sc4h8oh-3o2=>sc4h8oh-3o+sc4h8oh-3o        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-3 + sc4h8oh-mo2 => sc4h8oh-3o + sc4h8oh-mo',
 "chemkinKinetics": """
sc4h8oh-3+sc4h8oh-mo2=>sc4h8oh-3o+sc4h8oh-mo        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8ohm + sc4h8oh-1o2 => sc4h8oh-mo + sc4h8oh-1o',
 "chemkinKinetics": """
sc4h8ohm+sc4h8oh-1o2=>sc4h8oh-mo+sc4h8oh-1o         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8ohm + sc4h8oh-2o2 => sc4h8oh-mo + sc4h8oh-2o',
 "chemkinKinetics": """
sc4h8ohm+sc4h8oh-2o2=>sc4h8oh-mo+sc4h8oh-2o         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8ohm + sc4h8oh-3o2 => sc4h8oh-mo + sc4h8oh-3o',
 "chemkinKinetics": """
sc4h8ohm+sc4h8oh-3o2=>sc4h8oh-mo+sc4h8oh-3o         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8ohm + sc4h8oh-mo2 => sc4h8oh-mo + sc4h8oh-mo',
 "chemkinKinetics": """
sc4h8ohm+sc4h8oh-mo2=>sc4h8oh-mo+sc4h8oh-mo         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-1 + ho2 => sc4h8oh-1o + oh',
 "chemkinKinetics": """
sc4h8oh-1+ho2=>sc4h8oh-1o+oh                        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-2 + ho2 => sc4h8oh-2o + oh',
 "chemkinKinetics": """
sc4h8oh-2+ho2=>sc4h8oh-2o+oh                        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-3 + ho2 => sc4h8oh-3o + oh',
 "chemkinKinetics": """
sc4h8oh-3+ho2=>sc4h8oh-3o+oh                        7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8ohm + ho2 => sc4h8oh-mo + oh',
 "chemkinKinetics": """
sc4h8ohm+ho2=>sc4h8oh-mo+oh                         7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-1 + ch3o2 => sc4h8oh-1o + ch3o',
 "chemkinKinetics": """
sc4h8oh-1+ch3o2=>sc4h8oh-1o+ch3o                    7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-2 + ch3o2 => sc4h8oh-2o + ch3o',
 "chemkinKinetics": """
sc4h8oh-2+ch3o2=>sc4h8oh-2o+ch3o                    7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-3 + ch3o2 => sc4h8oh-3o + ch3o',
 "chemkinKinetics": """
sc4h8oh-3+ch3o2=>sc4h8oh-3o+ch3o                    7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8ohm + ch3o2 => sc4h8oh-mo + ch3o',
 "chemkinKinetics": """
sc4h8ohm+ch3o2=>sc4h8oh-mo+ch3o                     7.000e+12 0.000     -1.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (-1000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-1o2 <=> sc4h7oh-1ooh-2',
 "chemkinKinetics": """
sc4h8oh-1o2=sc4h7oh-1ooh-2                          2.000e+11 0.000     28.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(28450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h8oh-1o2 <=> sc4h7oh-1ooh-3',
 "chemkinKinetics": """
sc4h8oh-1o2=sc4h7oh-1ooh-3                          3.750e+10 0.000     24.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h8oh-1o2 <=> sc4h7oh-1ooh-m',
 "chemkinKinetics": """
sc4h8oh-1o2=sc4h7oh-1ooh-m                          3.000e+11 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h8oh-2o2 => ch3cho + ch3cho + oh',
 "chemkinKinetics": """
sc4h8oh-2o2=>ch3cho+ch3cho+oh                       2.300e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.3e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products3',  ],
},

{
 "reaction": 'sc4h8oh-2o2 => c3ket12 + ch3',
 "chemkinKinetics": """
sc4h8oh-2o2=>c3ket12+ch3                            2.000e+09 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2e+09, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h8oh-2o2 <=> sc4h7oh-2ooh-m',
 "chemkinKinetics": """
sc4h8oh-2o2=sc4h7oh-2ooh-m                          3.750e+10 0.000     25.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h8oh-2o2 <=> sc4h7oh-2ooh-3',
 "chemkinKinetics": """
sc4h8oh-2o2=sc4h7oh-2ooh-3                          3.000e+11 0.000     29.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(29000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h8oh-2o2 <=> sc4h7oh-2ooh-1',
 "chemkinKinetics": """
sc4h8oh-2o2=sc4h7oh-2ooh-1                          1.000e+11 0.000     24.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(24450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h8oh-3o2 <=> sc4h7oh-3ooh-1',
 "chemkinKinetics": """
sc4h8oh-3o2=sc4h7oh-3ooh-1                          1.250e+10 0.000     18.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(18450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h8oh-3o2 <=> sc4h7oh-3ooh-m',
 "chemkinKinetics": """
sc4h8oh-3o2=sc4h7oh-3ooh-m                          4.688e+09 0.000     22.950   
""",
 "rmgPyKinetics": Arrhenius(A=(4.688e+09, 's^-1'), n=0, Ea=(22950, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h8oh-3o2 <=> sc4h7oh-3ooh-2',
 "chemkinKinetics": """
sc4h8oh-3o2=sc4h7oh-3ooh-2                          2.000e+11 0.000     28.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(28450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h8oh-mo2 => c2h5cho + ch2o + oh',
 "chemkinKinetics": """
sc4h8oh-mo2=>c2h5cho+ch2o+oh                        2.300e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.3e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products3',  ],
},

{
 "reaction": 'sc4h8oh-mo2 => ch2o + hco + c2h5 + oh',
 "chemkinKinetics": """
sc4h8oh-mo2=>ch2o+hco+c2h5+oh                       2.000e+09 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2e+09, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h8oh-mo2 <=> sc4h7oh-mooh-3',
 "chemkinKinetics": """
sc4h8oh-mo2=sc4h7oh-mooh-3                          4.688e+09 0.000     21.950   
""",
 "rmgPyKinetics": Arrhenius(A=(4.688e+09, 's^-1'), n=0, Ea=(21950, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h8oh-mo2 <=> sc4h7oh-mooh-2',
 "chemkinKinetics": """
sc4h8oh-mo2=sc4h7oh-mooh-2                          2.500e+10 0.000     22.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(22450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h8oh-mo2 <=> sc4h7oh-mooh-1',
 "chemkinKinetics": """
sc4h8oh-mo2=sc4h7oh-mooh-1                          1.000e+11 0.000     24.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(24450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['intra_H_migration',  ],
},

{
 "reaction": 'sc4h8oh-1o2 <=> c4h7oh1-2 + ho2',
 "chemkinKinetics": """
sc4h8oh-1o2=c4h7oh1-2+ho2                           4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'sc4h8oh-1o2 <=> c4h7oh2-2 + ho2',
 "chemkinKinetics": """
sc4h8oh-1o2=c4h7oh2-2+ho2                           4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'sc4h8oh-2o2 <=> c4h7oh2-2 + ho2',
 "chemkinKinetics": """
sc4h8oh-2o2=c4h7oh2-2+ho2                           4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'sc4h8oh-2o2 <=> c4h7oh1-3 + ho2',
 "chemkinKinetics": """
sc4h8oh-2o2=c4h7oh1-3+ho2                           4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'sc4h8oh-3o2 <=> ho2 + c4h7oh1-3',
 "chemkinKinetics": """
sc4h8oh-3o2=ho2+c4h7oh1-3                           4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'sc4h8oh-mo2 <=> ho2 + c4h7oh1-2',
 "chemkinKinetics": """
sc4h8oh-mo2=ho2+c4h7oh1-2                           4.308e+36 -7.500    39.510   
""",
 "rmgPyKinetics": Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['HO2_Elimination_from_PeroxyRadical',  ],
},

{
 "reaction": 'sc4h8oh-1o2 + ho2 <=> sc4h8oh-1o2h + o2',
 "chemkinKinetics": """
sc4h8oh-1o2+ho2=sc4h8oh-1o2h+o2                     1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-2o2 + ho2 <=> sc4h8oh-2o2h + o2',
 "chemkinKinetics": """
sc4h8oh-2o2+ho2=sc4h8oh-2o2h+o2                     1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-3o2 + ho2 <=> sc4h8oh-3o2h + o2',
 "chemkinKinetics": """
sc4h8oh-3o2+ho2=sc4h8oh-3o2h+o2                     1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-mo2 + ho2 <=> sc4h8oh-mo2h + o2',
 "chemkinKinetics": """
sc4h8oh-mo2+ho2=sc4h8oh-mo2h+o2                     1.750e+10 0.000     -3.275   
""",
 "rmgPyKinetics": Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-1o2 + h2o2 <=> sc4h8oh-1o2h + ho2',
 "chemkinKinetics": """
sc4h8oh-1o2+h2o2=sc4h8oh-1o2h+ho2                   2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-2o2 + h2o2 <=> sc4h8oh-2o2h + ho2',
 "chemkinKinetics": """
sc4h8oh-2o2+h2o2=sc4h8oh-2o2h+ho2                   2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-3o2 + h2o2 <=> sc4h8oh-3o2h + ho2',
 "chemkinKinetics": """
sc4h8oh-3o2+h2o2=sc4h8oh-3o2h+ho2                   2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-mo2 + h2o2 <=> sc4h8oh-mo2h + ho2',
 "chemkinKinetics": """
sc4h8oh-mo2+h2o2=sc4h8oh-mo2h+ho2                   2.400e+12 0.000     10.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['H_Abstraction',  ],
},

{
 "reaction": 'sc4h8oh-1o2 + ch3o2 => sc4h8oh-1o + ch3o + o2',
 "chemkinKinetics": """
sc4h8oh-1o2+ch3o2=>sc4h8oh-1o+ch3o+o2               1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-2o2 + ch3o2 => sc4h8oh-2o + ch3o + o2',
 "chemkinKinetics": """
sc4h8oh-2o2+ch3o2=>sc4h8oh-2o+ch3o+o2               1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-3o2 + ch3o2 => sc4h8oh-3o + ch3o + o2',
 "chemkinKinetics": """
sc4h8oh-3o2+ch3o2=>sc4h8oh-3o+ch3o+o2               1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-mo2 + ch3o2 => sc4h8oh-mo + ch3o + o2',
 "chemkinKinetics": """
sc4h8oh-mo2+ch3o2=>sc4h8oh-mo+ch3o+o2               1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-1o2 + sc4h8oh-1o2 => sc4h8oh-1o + sc4h8oh-1o + o2',
 "chemkinKinetics": """
sc4h8oh-1o2+sc4h8oh-1o2=>sc4h8oh-1o+sc4h8oh-1o+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-1o2 + sc4h8oh-2o2 => sc4h8oh-1o + sc4h8oh-2o + o2',
 "chemkinKinetics": """
sc4h8oh-1o2+sc4h8oh-2o2=>sc4h8oh-1o+sc4h8oh-2o+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-1o2 + sc4h8oh-3o2 => sc4h8oh-1o + sc4h8oh-3o + o2',
 "chemkinKinetics": """
sc4h8oh-1o2+sc4h8oh-3o2=>sc4h8oh-1o+sc4h8oh-3o+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-1o2 + sc4h8oh-mo2 => sc4h8oh-1o + sc4h8oh-mo + o2',
 "chemkinKinetics": """
sc4h8oh-1o2+sc4h8oh-mo2=>sc4h8oh-1o+sc4h8oh-mo+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-2o2 + sc4h8oh-2o2 => sc4h8oh-2o + sc4h8oh-2o + o2',
 "chemkinKinetics": """
sc4h8oh-2o2+sc4h8oh-2o2=>sc4h8oh-2o+sc4h8oh-2o+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-2o2 + sc4h8oh-3o2 => sc4h8oh-2o + sc4h8oh-3o + o2',
 "chemkinKinetics": """
sc4h8oh-2o2+sc4h8oh-3o2=>sc4h8oh-2o+sc4h8oh-3o+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-2o2 + sc4h8oh-mo2 => sc4h8oh-2o + sc4h8oh-mo + o2',
 "chemkinKinetics": """
sc4h8oh-2o2+sc4h8oh-mo2=>sc4h8oh-2o+sc4h8oh-mo+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-3o2 + sc4h8oh-3o2 => sc4h8oh-3o + sc4h8oh-3o + o2',
 "chemkinKinetics": """
sc4h8oh-3o2+sc4h8oh-3o2=>sc4h8oh-3o+sc4h8oh-3o+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-3o2 + sc4h8oh-mo2 => sc4h8oh-3o + sc4h8oh-mo + o2',
 "chemkinKinetics": """
sc4h8oh-3o2+sc4h8oh-mo2=>sc4h8oh-3o+sc4h8oh-mo+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-mo2 + sc4h8oh-mo2 => sc4h8oh-mo + sc4h8oh-mo + o2',
 "chemkinKinetics": """
sc4h8oh-mo2+sc4h8oh-mo2=>sc4h8oh-mo+sc4h8oh-mo+o2   1.400e+16 -1.610    1.860    
""",
 "rmgPyKinetics": Arrhenius(
    A = (1.4e+16, 'cm^3/(mol*s)'),
    n = -1.61,
    Ea = (1860, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_O2_Elimination', 'Fake_O2_Elimination',  ],
},

{
 "reaction": 'sc4h8oh-1o2h => sc4h8oh-1o + oh',
 "chemkinKinetics": """
sc4h8oh-1o2h=>sc4h8oh-1o+oh                         1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h8oh-2o2h => sc4h8oh-2o + oh',
 "chemkinKinetics": """
sc4h8oh-2o2h=>sc4h8oh-2o+oh                         1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h8oh-3o2h => sc4h8oh-3o + oh',
 "chemkinKinetics": """
sc4h8oh-3o2h=>sc4h8oh-3o+oh                         1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h8oh-mo2h => sc4h8oh-mo + oh',
 "chemkinKinetics": """
sc4h8oh-mo2h=>sc4h8oh-mo+oh                         1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'ch3ocho + c2h5 <=> sc4h8oh-1o',
 "chemkinKinetics": """
ch3ocho+c2h5=sc4h8oh-1o                             1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'ch3cho + sc2h4oh <=> sc4h8oh-2o',
 "chemkinKinetics": """
ch3cho+sc2h4oh=sc4h8oh-2o                           1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2o + ic3h6oh <=> sc4h8oh-3o',
 "chemkinKinetics": """
ch2o+ic3h6oh=sc4h8oh-3o                             1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'ch2o + c3h6oh-1 <=> sc4h8oh-mo',
 "chemkinKinetics": """
ch2o+c3h6oh-1=sc4h8oh-mo                            1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'sc4h7oh-1ooh-2 => sc4h7oho1-2 + oh',
 "chemkinKinetics": """
sc4h7oh-1ooh-2=>sc4h7oho1-2+oh                      6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'sc4h7oh-1ooh-3 => sc4h7oho1-3 + oh',
 "chemkinKinetics": """
sc4h7oh-1ooh-3=>sc4h7oho1-3+oh                      7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-1ooh-m => sc4h7oho1-m + oh',
 "chemkinKinetics": """
sc4h7oh-1ooh-m=>sc4h7oho1-m+oh                      6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'sc4h7oh-2ooh-1 => sc4h7oho1-2 + oh',
 "chemkinKinetics": """
sc4h7oh-2ooh-1=>sc4h7oho1-2+oh                      6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'sc4h7oh-2ooh-3 => sc4h7oho2-3 + oh',
 "chemkinKinetics": """
sc4h7oh-2ooh-3=>sc4h7oho2-3+oh                      6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'sc4h7oh-2ooh-m => sc4h7oho2-m + oh',
 "chemkinKinetics": """
sc4h7oh-2ooh-m=>sc4h7oho2-m+oh                      7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'sc4h7oh-3ooh-1 => sc4h7oho1-3 + oh',
 "chemkinKinetics": """
sc4h7oh-3ooh-1=>sc4h7oho1-3+oh                      7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-3ooh-2 => sc4h7oho2-3 + oh',
 "chemkinKinetics": """
sc4h7oh-3ooh-2=>sc4h7oho2-3+oh                      6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'sc4h7oh-3ooh-m => sc4h7oho3-m + oh',
 "chemkinKinetics": """
sc4h7oh-3ooh-m=>sc4h7oho3-m+oh                      9.380e+09 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (9.38e+09, 's^-1'),
    n = 0,
    Ea = (7000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'sc4h7oh-mooh-1 => sc4h7oho1-m + oh',
 "chemkinKinetics": """
sc4h7oh-mooh-1=>sc4h7oho1-m+oh                      6.000e+11 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (6e+11, 's^-1'),
    n = 0,
    Ea = (22000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'sc4h7oh-mooh-2 => sc4h7oho2-m + oh',
 "chemkinKinetics": """
sc4h7oh-mooh-2=>sc4h7oho2-m+oh                      7.500e+10 0.000     15.300   
""",
 "rmgPyKinetics": Arrhenius(
    A = (7.5e+10, 's^-1'),
    n = 0,
    Ea = (15300, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'sc4h7oh-mooh-3 => sc4h7oho3-m + oh',
 "chemkinKinetics": """
sc4h7oh-mooh-3=>sc4h7oho3-m+oh                      9.380e+09 0.000     7.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (9.38e+09, 's^-1'),
    n = 0,
    Ea = (7000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV     /       0.00    0.00    0.00    /',
),
 "possibleReactionFamilies": ['Intra_R_Add_ExoTetCyclic', 'Cyclic_Ether_Formation',  ],
},

{
 "reaction": 'c4h7oh2-2 + ho2 => sc4h7oh-1ooh-2',
 "chemkinKinetics": """
c4h7oh2-2+ho2=>sc4h7oh-1ooh-2                       1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+11, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (11900, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh1-2 + ho2 => sc4h7oh-1ooh-m',
 "chemkinKinetics": """
c4h7oh1-2+ho2=>sc4h7oh-1ooh-m                       1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+11, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (11900, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh2-2 + ho2 => sc4h7oh-2ooh-1',
 "chemkinKinetics": """
c4h7oh2-2+ho2=>sc4h7oh-2ooh-1                       1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+11, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (11900, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh1-3 + ho2 => sc4h7oh-2ooh-3',
 "chemkinKinetics": """
c4h7oh1-3+ho2=>sc4h7oh-2ooh-3                       1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+11, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (11900, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh1-3 + ho2 => sc4h7oh-3ooh-2',
 "chemkinKinetics": """
c4h7oh1-3+ho2=>sc4h7oh-3ooh-2                       1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+11, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (11900, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['R_Addition_MultipleBond',  ],
},

{
 "reaction": 'c4h7oh2-2 + ho2 => sc4h7oh-mooh-1',
 "chemkinKinetics": """
c4h7oh2-2+ho2=>sc4h7oh-mooh-1                       1.000e+11 0.000     11.900   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+11, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (11900, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-1ooh-3 => oh + ch3ocho + c2h4',
 "chemkinKinetics": """
sc4h7oh-1ooh-3=>oh+ch3ocho+c2h4                     1.000e+13 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+13, 's^-1'),
    n = 0,
    Ea = (30000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-2ooh-m => oh + ch3cho + c2h3oh',
 "chemkinKinetics": """
sc4h7oh-2ooh-m=>oh+ch3cho+c2h3oh                    1.000e+13 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+13, 's^-1'),
    n = 0,
    Ea = (30000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'sc4h7oh-3ooh-1 => oh + ch2o + ic3h5oh',
 "chemkinKinetics": """
sc4h7oh-3ooh-1=>oh+ch2o+ic3h5oh                     1.000e+13 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+13, 's^-1'),
    n = 0,
    Ea = (30000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'sc4h7oh-mooh-2 => oh + ch2o + ch3chchoh',
 "chemkinKinetics": """
sc4h7oh-mooh-2=>oh+ch2o+ch3chchoh                   1.000e+13 0.000     30.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+13, 's^-1'),
    n = 0,
    Ea = (30000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": ['Fake_3products2',  ],
},

{
 "reaction": 'sc4h7oh-2ooh-1 + o2 <=> nc4ket23 + ho2',
 "chemkinKinetics": """
sc4h7oh-2ooh-1+o2=nc4ket23+ho2                      1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.260e+17 -1.637    0.838    /
    PLOG/ 0.010     5.260e+17 -1.637    0.838    /
    PLOG/ 0.100     5.260e+17 -1.637    0.838    /
    PLOG/ 1.000     5.280e+17 -1.638    0.839    /
    PLOG/ 10.000    1.540e+18 -1.771    1.120    /
    PLOG/ 100.000   3.780e+20 -2.429    3.090    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.28e+17, 'cm^3/(mol*s)'),
            n = -1.638,
            Ea = (839, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.54e+18, 'cm^3/(mol*s)'),
            n = -1.771,
            Ea = (1120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+20, 'cm^3/(mol*s)'),
            n = -2.429,
            Ea = (3090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'sc4h7oh-3ooh-1 + o2 <=> nc4ket24 + ho2',
 "chemkinKinetics": """
sc4h7oh-3ooh-1+o2=nc4ket24+ho2                      1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.260e+17 -1.637    0.838    /
    PLOG/ 0.010     5.260e+17 -1.637    0.838    /
    PLOG/ 0.100     5.260e+17 -1.637    0.838    /
    PLOG/ 1.000     5.280e+17 -1.638    0.839    /
    PLOG/ 10.000    1.540e+18 -1.771    1.120    /
    PLOG/ 100.000   3.780e+20 -2.429    3.090    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.28e+17, 'cm^3/(mol*s)'),
            n = -1.638,
            Ea = (839, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.54e+18, 'cm^3/(mol*s)'),
            n = -1.771,
            Ea = (1120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+20, 'cm^3/(mol*s)'),
            n = -2.429,
            Ea = (3090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'sc4h7oh-mooh-1 + o2 <=> nc4ket21 + ho2',
 "chemkinKinetics": """
sc4h7oh-mooh-1+o2=nc4ket21+ho2                      1.000e+00 0.000     0.000    
    PLOG/ 0.001     5.260e+17 -1.637    0.838    /
    PLOG/ 0.010     5.260e+17 -1.637    0.838    /
    PLOG/ 0.100     5.260e+17 -1.637    0.838    /
    PLOG/ 1.000     5.280e+17 -1.638    0.839    /
    PLOG/ 10.000    1.540e+18 -1.771    1.120    /
    PLOG/ 100.000   3.780e+20 -2.429    3.090    /
""",
 "rmgPyKinetics": PDepArrhenius(
    pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
    arrhenius = [
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.26e+17, 'cm^3/(mol*s)'),
            n = -1.637,
            Ea = (838, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (5.28e+17, 'cm^3/(mol*s)'),
            n = -1.638,
            Ea = (839, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (1.54e+18, 'cm^3/(mol*s)'),
            n = -1.771,
            Ea = (1120, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        Arrhenius(
            A = (3.78e+20, 'cm^3/(mol*s)'),
            n = -2.429,
            Ea = (3090, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ],
),
 "possibleReactionFamilies": ['Disproportionation',  ],
},

{
 "reaction": 'sc4h7oh-1ooh-2 + o2 <=> sc4h7oh-1ooh-2o2',
 "chemkinKinetics": """
sc4h7oh-1ooh-2+o2=sc4h7oh-1ooh-2o2                  7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h7oh-1ooh-3 + o2 <=> sc4h7oh-1ooh-3o2',
 "chemkinKinetics": """
sc4h7oh-1ooh-3+o2=sc4h7oh-1ooh-3o2                  4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h7oh-1ooh-m + o2 <=> sc4h7oh-1ooh-mo2',
 "chemkinKinetics": """
sc4h7oh-1ooh-m+o2=sc4h7oh-1ooh-mo2                  4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h7oh-2ooh-1 + o2 <=> sc4h7oh-2ooh-1o2',
 "chemkinKinetics": """
sc4h7oh-2ooh-1+o2=sc4h7oh-2ooh-1o2                  1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h7oh-2ooh-3 + o2 <=> sc4h7oh-2ooh-3o2',
 "chemkinKinetics": """
sc4h7oh-2ooh-3+o2=sc4h7oh-2ooh-3o2                  4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h7oh-2ooh-m + o2 <=> sc4h7oh-2ooh-mo2',
 "chemkinKinetics": """
sc4h7oh-2ooh-m+o2=sc4h7oh-2ooh-mo2                  4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h7oh-3ooh-1 + o2 <=> sc4h7oh-3ooh-1o2',
 "chemkinKinetics": """
sc4h7oh-3ooh-1+o2=sc4h7oh-3ooh-1o2                  1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h7oh-3ooh-2 + o2 <=> sc4h7oh-3ooh-2o2',
 "chemkinKinetics": """
sc4h7oh-3ooh-2+o2=sc4h7oh-3ooh-2o2                  7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h7oh-3ooh-m + o2 <=> sc4h7oh-3ooh-mo2',
 "chemkinKinetics": """
sc4h7oh-3ooh-m+o2=sc4h7oh-3ooh-mo2                  4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h7oh-mooh-1 + o2 <=> sc4h7oh-mooh-1o2',
 "chemkinKinetics": """
sc4h7oh-mooh-1+o2=sc4h7oh-mooh-1o2                  1.000e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h7oh-mooh-2 + o2 <=> sc4h7oh-mooh-2o2',
 "chemkinKinetics": """
sc4h7oh-mooh-2+o2=sc4h7oh-mooh-2o2                  7.540e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h7oh-mooh-3 + o2 <=> sc4h7oh-mooh-3o2',
 "chemkinKinetics": """
sc4h7oh-mooh-3+o2=sc4h7oh-mooh-3o2                  4.520e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['R_Recombination',  ],
},

{
 "reaction": 'sc4h7oh-1ooh-2o2 => ch3cho + co2 + ch3 + oh + oh',
 "chemkinKinetics": """
sc4h7oh-1ooh-2o2=>ch3cho+co2+ch3+oh+oh              2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-3ooh-2o2 => ch3cho + ch2o + hco + oh + oh',
 "chemkinKinetics": """
sc4h7oh-3ooh-2o2=>ch3cho+ch2o+hco+oh+oh             2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-mooh-2o2 <=> ch3cho + ch2o + hco + oh + oh',
 "chemkinKinetics": """
sc4h7oh-mooh-2o2=ch3cho+ch2o+hco+oh+oh              2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-1ooh-mo2 => ch3cho + co2 + ch3 + oh + oh',
 "chemkinKinetics": """
sc4h7oh-1ooh-mo2=>ch3cho+co2+ch3+oh+oh              2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-3ooh-mo2 => ch3cho + ch2o + hco + oh + oh',
 "chemkinKinetics": """
sc4h7oh-3ooh-mo2=>ch3cho+ch2o+hco+oh+oh             2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-2ooh-mo2 => ch3cho + ch2o + hco + oh + oh',
 "chemkinKinetics": """
sc4h7oh-2ooh-mo2=>ch3cho+ch2o+hco+oh+oh             2.500e+10 0.000     21.886   
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+10, 's^-1'),
    n = 0,
    Ea = (21886, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV/ 0.000E+00 0.000 0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-2ooh-1o2 <=> sc4ohket2-1 + oh',
 "chemkinKinetics": """
sc4h7oh-2ooh-1o2=sc4ohket2-1+oh                     1.000e+11 0.000     25.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'sc4h7oh-2ooh-3o2 <=> sc4ohket2-3 + oh',
 "chemkinKinetics": """
sc4h7oh-2ooh-3o2=sc4ohket2-3+oh                     1.000e+11 0.000     25.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'sc4h7oh-2ooh-mo2 <=> sc4ohket2-m + oh',
 "chemkinKinetics": """
sc4h7oh-2ooh-mo2=sc4ohket2-m+oh                     1.250e+10 0.000     19.450   
""",
 "rmgPyKinetics": Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(19450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'sc4h7oh-1ooh-2o2 <=> sc4ohket2-1 + oh',
 "chemkinKinetics": """
sc4h7oh-1ooh-2o2=sc4ohket2-1+oh                     3.750e+10 0.000     25.000   
""",
 "rmgPyKinetics": Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-1ooh-3o2 <=> sc4ohket2-3 + oh',
 "chemkinKinetics": """
sc4h7oh-1ooh-3o2=sc4ohket2-3+oh                     4.680e+09 0.000     22.950   
""",
 "rmgPyKinetics": Arrhenius(A=(4.68e+09, 's^-1'), n=0, Ea=(22950, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-1ooh-mo2 <=> sc4ohket2-m + oh',
 "chemkinKinetics": """
sc4h7oh-1ooh-mo2=sc4ohket2-m+oh                     2.500e+10 0.000     22.450   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(22450, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-3ooh-1o2 <=> sc4ohket3-1 + oh',
 "chemkinKinetics": """
sc4h7oh-3ooh-1o2=sc4ohket3-1+oh                     2.500e+10 0.000     21.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-3ooh-2o2 <=> sc4ohket3-2 + oh',
 "chemkinKinetics": """
sc4h7oh-3ooh-2o2=sc4ohket3-2+oh                     2.000e+11 0.000     26.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-3ooh-mo2 <=> sc4ohket3-m + oh',
 "chemkinKinetics": """
sc4h7oh-3ooh-mo2=sc4ohket3-m+oh                     3.120e+09 0.000     18.950   
""",
 "rmgPyKinetics": Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(18950, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'sc4h7oh-mooh-1o2 <=> sc4ohketm-1 + oh',
 "chemkinKinetics": """
sc4h7oh-mooh-1o2=sc4ohketm-1+oh                     2.000e+11 0.000     27.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(27000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'sc4h7oh-mooh-2o2 <=> sc4ohketm-2 + oh',
 "chemkinKinetics": """
sc4h7oh-mooh-2o2=sc4ohketm-2+oh                     2.500e+10 0.000     22.000   
""",
 "rmgPyKinetics": Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oh-mooh-3o2 <=> sc4ohketm-3 + oh',
 "chemkinKinetics": """
sc4h7oh-mooh-3o2=sc4ohketm-3+oh                     3.120e+09 0.000     19.950   
""",
 "rmgPyKinetics": Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(19950, 'cal/mol'), T0=(1, 'K')),
 "possibleReactionFamilies": ['Fake_Ketohydroperoxides',  ],
},

{
 "reaction": 'sc4ohket2-1 => oh + hocho + c2h5co',
 "chemkinKinetics": """
sc4ohket2-1=>oh+hocho+c2h5co                        1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4ohket2-3 => oh + hoch2co + ch3cho',
 "chemkinKinetics": """
sc4ohket2-3=>oh+hoch2co+ch3cho                      1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4ohket2-m => oh + ch2co + ch2oh + ch2o',
 "chemkinKinetics": """
sc4ohket2-m=>oh+ch2co+ch2oh+ch2o                    1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4ohket3-1 => oh + hocho + ch3coch2',
 "chemkinKinetics": """
sc4ohket3-1=>oh+hocho+ch3coch2                      1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4ohket3-2 => oh + hoch2cho + ch3co',
 "chemkinKinetics": """
sc4ohket3-2=>oh+hoch2cho+ch3co                      1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4ohket3-m => oh + hoc2h4co + ch2o',
 "chemkinKinetics": """
sc4ohket3-m=>oh+hoc2h4co+ch2o                       1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4ohketm-1 => oh + hocho + ch2ch2cho',
 "chemkinKinetics": """
sc4ohketm-1=>oh+hocho+ch2ch2cho                     1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4ohketm-2 => oh + hoch2cho + ch2cho',
 "chemkinKinetics": """
sc4ohketm-2=>oh+hoch2cho+ch2cho                     1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4ohketm-3 => oh + hoc2h4cho + hco',
 "chemkinKinetics": """
sc4ohketm-3=>oh+hoc2h4cho+hco                       1.000e+16 0.000     39.000   
""",
 "rmgPyKinetics": Arrhenius(
    A = (1e+16, 's^-1'),
    n = 0,
    Ea = (39000, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV /  0.000E+00  0.00  0.000E+00 /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oho1-2 + oh => c3h5-s + hocho + h2o',
 "chemkinKinetics": """
sc4h7oho1-2+oh=>c3h5-s+hocho+h2o                    2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oho1-3 + oh => c3h5-a + hocho + h2o',
 "chemkinKinetics": """
sc4h7oho1-3+oh=>c3h5-a+hocho+h2o                    2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oho1-m + oh => c3h5-a + hocho + h2o',
 "chemkinKinetics": """
sc4h7oho1-m+oh=>c3h5-a+hocho+h2o                    2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oho2-3 + oh => c2h3cho + ch2oh + h2o',
 "chemkinKinetics": """
sc4h7oho2-3+oh=>c2h3cho+ch2oh+h2o                   2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oho2-m + oh => c2h3cho + ch2oh + h2o',
 "chemkinKinetics": """
sc4h7oho2-m+oh=>c2h3cho+ch2oh+h2o                   2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oho3-m + oh => pc2h4oh + ch2co + h2o',
 "chemkinKinetics": """
sc4h7oho3-m+oh=>pc2h4oh+ch2co+h2o                   2.500e+12 0.000     0.000    
""",
 "rmgPyKinetics": Arrhenius(
    A = (2.5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (0, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oho1-2 + ho2 => c3h5-s + hocho + h2o2',
 "chemkinKinetics": """
sc4h7oho1-2+ho2=>c3h5-s+hocho+h2o2                  5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oho1-3 + ho2 => c3h5-a + hocho + h2o2',
 "chemkinKinetics": """
sc4h7oho1-3+ho2=>c3h5-a+hocho+h2o2                  5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oho1-m + ho2 => c3h5-a + hocho + h2o2',
 "chemkinKinetics": """
sc4h7oho1-m+ho2=>c3h5-a+hocho+h2o2                  5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oho2-3 + ho2 => c2h3cho + ch2oh + h2o2',
 "chemkinKinetics": """
sc4h7oho2-3+ho2=>c2h3cho+ch2oh+h2o2                 5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oho2-m + ho2 => c2h3cho + ch2oh + h2o2',
 "chemkinKinetics": """
sc4h7oho2-m+ho2=>c2h3cho+ch2oh+h2o2                 5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

{
 "reaction": 'sc4h7oho3-m + ho2 => pc2h4oh + ch2co + h2o2',
 "chemkinKinetics": """
sc4h7oho3-m+ho2=>pc2h4oh+ch2co+h2o2                 5.000e+12 0.000     17.700   
""",
 "rmgPyKinetics": Arrhenius(
    A = (5e+12, 'cm^3/(mol*s)'),
    n = 0,
    Ea = (17700, 'cal/mol'),
    T0 = (1, 'K'),
    comment = 'Chemkin file stated explicit reverse rate: REV  /  0.00E+00  0  0  /',
),
 "possibleReactionFamilies": [ ],
},

]
