import os
from rmgpy.molecule import Molecule

speciesList = """
H2              	InChI=1/H2/h1H
CO2             	InChI=1/CO2/c2-1-3
CO              	InChI=1/CO/c1-2
CH4             	InChI=1/CH4/h1H4
C2H4            	InChI=1/C2H4/c1-2/h1-2H2
C2H2            	InChI=1/C2H2/c1-2/h1-2H
C2H6            	InChI=1/C2H6/c1-2/h1-2H3
C3H6            	InChI=1/C3H6/c1-3-2/h3H,1H2,2H3
C3H8            	InChI=1/C3H8/c1-3-2/h3H2,1-2H3
C3H4-a           	InChI=1/C3H4/c1-3-2/h1-2H2
C3H-p           	InChI=1/C3H4/c1-3-2/h1H,2H3
CH3OH           	InChI=1/CH4O/c1-2/h2H,1H3
C4H8-1          	InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3
C4H6         	InChI=1/C4H6/c1-3-4-2/h3-4H,1-2H2
C4H10          	InChI=1/C4H10/c1-3-4-2/h3-4H2,1-2H3
C2H5OH         InChI=1/C2H6O/c1-2-3/h3H,2H2,1H3
C2H3            	InChI=1/C2H3/c1-2/h1H,2H2
CH2CO           	InChI=1/C2H2O/c1-2-3/h1H2
CH3CHO          	InChI=1/C2H4O/c1-2-3/h2H,1H3
H2O             	InChI=1/H2O/h1H2
CH2CHO          	InChI=1/C2H3O/c1-2-3/h2H,1H2
CH2O            	InChI=1/CH2O/c1-2/h1H2


C2H5            	InChI=1/C2H5/c1-2/h1H2,2H3
H               	InChI=1/H
O               	InChI=1/O
O2              	InChI=1/O2/c1-2
OH              	InChI=1/HO/h1H
HO2             	InChI=1/HO2/c1-2/h1H
H2O2            	InChI=1/H2O2/c1-2/h1-2H
C               	InChI=1/C
CH              	InChI=1/CH/h1H
CH2             	InChI=1/CH2/h1H2
CH2(S)          	InChI=1/CH2/h1H2
CH3             	InChI=1/CH3/h1H3
HCO             	InChI=1/CHO/c1-2/h1H
CH2OH           	InChI=1/CH3O/c1-2/h2H,1H2
CH3O            	InChI=1/CH3O/c1-2/h1H3
C2H             	InChI=1/C2H/c1-2/h1H
HCCO            	InChI=1/C2HO/c1-2-3/h1H
HCCOH           	InChI=1/C2H2O/c1-2-3/h1,3H

HOC2H4O2        	InChI=1/C2H5O3/c3-1-2-5-4/h3H,1-2H2
C3H2            	InChI=1/C3H2/c1-3-2/h1-2H
pC3H3           	InChI=1/C3H3/c1-3-2/h1H,2H2
C3H5-a           	InChI=1/C3H5/c1-3-2/h3H,1-2H2
C3H5-s           	InChI=1/C3H5/c1-3-2/h1H2,2H3
N2              	InChI=1/N2/c1-2
AR              	InChI=1/Ar
CH3CO           	InChI=1/C2H3O/c1-2-3/h1H3
C4H5           	    InChI=1/C4H5/c1-3-4-2/h1,3-4H,2H2


ho2cho
o2cho hocho ocho hoch2o2h hoch2o2
och2o2h hoch2o
ch3o2h ch3o2


ch3co3h ch3co3 ch3co2 c2h5o
pc2h4oh sc2h4oh o2c2h4oh c2h5o2h c2h5o2
c2h4o2h c2h4o1-2 c2h3o1-2 ch3coch3 ch3coch2
ch3coch2o2 ch3coch2o2h ch3coch2o c2h3cho c2h3co
c2h5cho c2h5co ch3och3 ch3och2 ch3och2o2
ch2och2o2h ch3och2o2h ch3och2o o2ch2och2o2h ho2ch2ocho
och2ocho hoch2oco ch3ocho ch3oco ch2ocho
he ic3h7 nc3h7
 c3h5-t
  c3h5o c3h6ooh1-2 c3h6ooh1-3
c3h6ooh2-1 c3h6ooh1-2o2 c3h6ooh1-3o2 c3h6ooh2-1o2 c3h6ooh2-2
nc3h7o2h ic3h7o2h nc3h7o2 ic3h7o2 nc3h7o
ic3h7o c3h6o1-2 c3h6o1-3 c3ket12 c3ket13
c3ket21 c3h51-2-3ooh c3h52-1-3ooh c3h6oh hoc3h6o2
ch3chco ac3h5ooh c2h3ooh
c4h8-2 pc4h9 sc4h9 c4h71-1 c4h71-2
c4h71-3 c4h71-4 c4h72-2  pc4h9o2h
sc4h9o2h pc4h9o2 sc4h9o2 pc4h9o sc4h9o
c4h7o c4h8o1-2 c4h8o1-3 c4h8o1-4 c4h8o2-3
pc4h8oh sc4h8oh c4h8oh-1o2 c4h8oh-2o2 c4h8ooh1-1
c4h8ooh1-2 c4h8ooh1-3 c4h8ooh1-4 c4h8ooh2-1 c4h8ooh2-2
c4h8ooh2-3 c4h8ooh2-4 c4h8ooh1-2o2 c4h8ooh1-3o2 c4h8ooh1-4o2
c4h8ooh2-1o2 c4h8ooh2-3o2 c4h8ooh2-4o2 nc4ket12 nc4ket13
nc4ket14 nc4ket21 nc4ket23 nc4ket24 c2h5coch3
c2h5coch2 ch2ch2coch3 ch3chcoch3 c2h3coch3 ch3choococh3
ch2choohcoch3 nc3h7cho nc3h7co c3h6cho-1 c3h6cho-2
c3h6cho-3 c2h5chco sc3h5cho sc3h5co ch2ch2cho
ic4h10 ic4h9 tc4h9 ic4h8 ic4h7
tc4h9o2 ic4h9o2 tc4h8o2h-i ic4h8o2h-i ic4h8o2h-t
ic4h8o cc4h8o ic4h9o tc4h9o ic4h9o2h
tc4h9o2h ic4h7o ic4h8oh io2c4h8oh ic3h7cho
tc3h6cho ic3h7co ic3h6cho tc4h8ooh-io2 ic4h8ooh-io2
ic4h8ooh-to2 ic4ketii ic4ketit ic4h7oh ic4h6oh
ic3h5cho ic3h5co tc3h6ocho ic3h6co ic4h7ooh
tc3h6ohcho tc3h6oh ic3h5oh tc3h6o2cho tc3h6o2hco
ic3h5o2hcho ch2cch2oh tc4h8cho o2c4h8cho o2hc4h8co
c3h5oh tic4h7q2-i iic4h7q2-t iic4h7q2-i ch2o2h


 c2h3oh
!
!  Added for charlie's mech
hcchoh
ch2coh
nc4h9oh    InChI=1S/C4H10O/c1-2-3-4-5/h5H,2-4H2,1H3
c4h8oh-1   InChI=1S/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3
c4h8oh-2   InChI=1S/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3
c4h8oh-3   InChI=1S/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3
c4h8oh-4   InChI=1S/C4H9O/c1-2-3-4-5/h5H,1-4H2
pc4h9o      InChI=1/C4H9O/c1-2-3-4-5/h2-4H2,1H3
c4h6oh1-32  InChI=1S/C4H7O/c1-3-4(2)5/h3,5H,2H2,1H3
c4h7oh1-1 InChI=1S/C4H8O/c1-2-3-4-5/h3-5H,2H2,1H3/b4-3-
c4h6oh1-13 InChI=1S/C4H7O/c1-2-3-4-5/h2-5H,1H3
c4h5oh-13  InChI=1S/C4H6O/c1-2-3-4-5/h2-5H,1H2/b4-3-
c4h7oh2-1 InChI=1S/C4H8O/c1-2-3-4-5/h2-3,5H,4H2,1H3/b3-2-
c4h7oh1-4 InChI=1S/C4H8O/c1-2-3-4-5/h2,5H,1,3-4H2
sc4h9oh  InChI=1S/C4H10O/c1-3-4(2)5/h4-5H,3H2,1-2H3
sc4h8ohm  InChI=1S/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3
sc4h8oh-1  InChI=1S/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3
sc4h8oh-2  InChI=1S/C4H9O/c1-3-4(2)5/h3-5H,1-2H3
sc4h8oh-3  InChI=1S/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3
sc4h9o       InChI=1S/C4H9O/c1-3-4(2)5/h4H,3H2,1-2H3
tc4h9oh      InChI=1S/C4H10O/c1-4(2,3)5/h5H,1-3H3
tc4h8oh      InChI=1S/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3
tc4h8o        InChI=1S/C4H9O/c1-4(2,3)5/h1-3H3
ic4h9oh     InChI=1S/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3
ic4h8oh-1  InChI=1S/C4H9O/c1-4(2)3-5/h3-5H,1-2H3
ic4h8oh-2  InChI=1S/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3
ic4h8oh-3  InChI=1S/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3
ic4h9o       InChI=1S/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3
ic3h6oh     InChI=1S/C3H7O/c1-3(2)4/h3-4H,1H2,2H3
c3h6oh-1   InChI=1S/C3H7O/c1-2-3-4/h3-4H,2H2,1H3
c4h7oh2-2   InChI=1S/C4H8O/c1-3-4(2)5/h3,5H,1-2H3/b4-3-
c4h7oh1-2   InChI=1S/C4H8O/c1-3-4(2)5/h5H,2-3H2,1H3
c4h7oh1-3   InChI=1S/C4H8O/c1-3-4(2)5/h3-5H,1H2,2H3
ch3chchoh   InChI=1S/C3H6O/c1-2-3-4/h2-4H,1H3/b3-2+
c3h6oh-2     InChI=1S/C3H7O/c1-2-3-4/h2,4H,3H2,1H3
c3h5oh        InChI=1S/C3H6O/c1-2-3-4/h2,4H,1,3H2
ic3h6choh   InChI=1S/C4H8O/c1-4(2)3-5/h3,5H,1-2H3
ic3h5ch2oh InChI=1S/C4H8O/c1-4(2)3-5/h5H,1,3H2,2H3
!
!  Added for charlie's mech
hcchoh
ch2coh
!
! Added for mani low T 1-butanol mech
c4h8oh-1o2    InChI=1S/C4H9O3/c1-2-3-4(5)7-6/h4-5H,2-3H2,1H3
c4h8oh-2o2    InChI=1S/C4H9O3/c1-2-4(3-5)7-6/h4-5H,2-3H2,1H3
c4h8oh-3o2      InChI=1S/C4H9O3/c1-4(7-6)2-3-5/h4-5H,2-3H2,1H3
c4h8oh-4o2      InChI=1S/C4H9O3/c5-3-1-2-4-7-6/h5H,1-4H2

!
c4h7oh-1ooh-2   InChI=1S/C4H9O3/c1-2-3-4(5)7-6/h3-6H,2H2,1H3
c4h7oh-1ooh-3   InChI=1S/C4H9O3/c1-2-3-4(5)7-6/h2,4-6H,3H2,1H3
c4h7oh-1ooh-4   InChI=1S/C4H9O3/c1-2-3-4(5)7-6/h4-6H,1-3H2
c4h7oh-2ooh-4     InChI=1S/C4H9O3/c1-2-4(3-5)7-6/h4-6H,1-3H2
c4h7oh-2ooh-3     InChI=1S/C4H9O3/c1-2-4(3-5)7-6/h2,4-6H,3H2,1H3
c4h7oh-2ooh-1     InChI=1S/C4H9O3/c1-2-4(3-5)7-6/h3-6H,2H2,1H3
c4h7oh-3ooh-1     InChI=1S/C4H9O3/c1-4(7-6)2-3-5/h3-6H,2H2,1H3
c4h7oh-3ooh-4     InChI=1S/C4H9O3/c1-4(7-6)2-3-5/h4-6H,1-3H2
c4h7oh-3ooh-2      InChI=1S/C4H9O3/c1-4(7-6)2-3-5/h2,4-6H,3H2,1H3
c4h7oh-4ooh-3      InChI=1S/C4H9O3/c5-3-1-2-4-7-6/h2,5-6H,1,3-4H2
c4h7oh-4ooh-2     InChI=1S/C4H9O3/c5-3-1-2-4-7-6/h1,5-6H,2-4H2
c4h7oh-4ooh-1     InChI=1S/C4H9O3/c5-3-1-2-4-7-6/h3,5-6H,1-2,4H2
!
c4h7oh-1ooh-2o2    InChI=1S/C4H9O5/c1-2-3(8-6)4(5)9-7/h3-5,7H,2H2,1H3
c4h7oh-1ooh-3o2    InChI=1S/C4H9O5/c1-3(8-6)2-4(5)9-7/h3-5,7H,2H2,1H3
c4h7oh-1ooh-4o2    InChI=1S/C4H9O5/c5-4(9-7)2-1-3-8-6/h4-5,7H,1-3H2
c4h7oh-2ooh-1o2    InChI=1S/C4H9O5/c1-2-3(8-6)4(5)9-7/h3-6H,2H2,1H3
c4h7oh-2ooh-3o2    InChI=1S/C4H9O5/c1-3(8-6)4(2-5)9-7/h3-5,7H,2H2,1H3
c4h7oh-2ooh-4o2    InChI=1S/C4H9O5/c5-3-4(9-7)1-2-8-6/h4-5,7H,1-3H2
c4h7oh-3ooh-1o2   InChI=1S/C4H9O5/c1-3(8-6)2-4(5)9-7/h3-6H,2H2,1H3
c4h7oh-3ooh-2o2   InChI=1S/C4H9O5/c1-3(8-6)4(2-5)9-7/h3-6H,2H2,1H3
c4h7oh-3ooh-4o2   InChI=1S/C4H9O5/c5-2-1-4(9-7)3-8-6/h4-5,7H,1-3H2
c4h7oh-4ooh-1o2   InChI=1S/C4H9O5/c5-4(9-7)2-1-3-8-6/h4-6H,1-3H2
c4h7oh-4ooh-2o2   InChI=1S/C4H9O5/c5-3-4(9-7)1-2-8-6/h4-6H,1-3H2
c4h7oh-4ooh-3o2   InChI=1S/C4H9O5/c5-2-1-4(9-7)3-8-6/h4-6H,1-3H2
!
c4ohket1-2  InChI=1S/C4H8O4/c1-2-3(8-7)4(5)6/h3,7H,2H2,1H3,(H,5,6)
c4ohket1-3  InChI=1S/C4H8O4/c1-3(8-7)2-4(5)6/h3,7H,2H2,1H3,(H,5,6)
c4ohket1-4  InChI=1S/C4H8O4/c5-4(6)2-1-3-8-7/h7H,1-3H2,(H,5,6)
c4ohket2-1  InChI=1S/C4H8O4/c1-2-3(5)4(6)8-7/h4,6-7H,2H2,1H3
c4ohket2-3  InChI=1S/C4H8O4/c1-3(8-7)4(6)2-5/h3,5,7H,2H2,1H3
c4ohket2-4  InChI=1S/C4H8O4/c5-3-4(6)1-2-8-7/h5,7H,1-3H2
c4ohket3-1  InChI=1S/C4H8O4/c1-3(5)2-4(6)8-7/h4,6-7H,2H2,1H3
c4ohket3-2  InChI=1S/C4H8O4/c1-3(6)4(2-5)8-7/h4-5,7H,2H2,1H3
c4ohket3-4  InChI=1S/C4H8O4/c5-2-1-4(6)3-8-7/h5,7H,1-3H2
c4ohket4-1  InChI=1S/C4H8O4/c5-3-1-2-4(6)8-7/h3-4,6-7H,1-2H2
c4ohket4-2  InChI=1S/C4H8O4/c5-2-1-4(3-6)8-7/h2,4,6-7H,1,3H2
c4ohket4-3  InChI=1S/C4H8O4/c5-2-1-4(3-6)8-7/h3-5,7H,1-2H2
!
c4h7oho1-2    InChI=1S/C4H8O2/c1-3-2-4(5)6-3/h3-5H,2H2,1H3/t3-,4+/m0/s1
c4h7oho1-3    InChI=1S/C4H8O2/c1-3-2-4(5)6-3/h3-5H,2H2,1H3/t3-,4+/m0/s1
c4h7oho1-4    InChI=1S/C4H8O2/c5-4-2-1-3-6-4/h4-5H,1-3H2/t4-/m1/s1
c4h7oho2-3    InChI=1S/C4H8O2/c1-3-4(2-5)6-3/h3-5H,2H2,1H3
c4h7oho2-4    InChI=1S/C4H8O2/c5-3-4-1-2-6-4/h4-5H,1-3H2
c4h7oho3-4    InChI=1S/C4H8O2/c5-2-1-4-3-6-4/h4-5H,1-3H2
!
c4h8oh-1o2h  InChI=1S/C4H10O3/c1-2-3-4(5)7-6/h4-6H,2-3H2,1H3
c4h8oh-2o2h  InChI=1S/C4H10O3/c1-2-4(3-5)7-6/h4-6H,2-3H2,1H3
c4h8oh-3o2h  InChI=1S/C4H10O3/c1-4(7-6)2-3-5/h4-6H,2-3H2,1H3
c4h8oh-4o2h  InChI=1S/C4H10O3/c5-3-1-2-4-7-6/h5-6H,1-4H2
!
c4h8oh-1o     InChI=1S/C4H9O2/c1-2-3-4(5)6/h4-5H,2-3H2,1H3
c4h8oh-2o     InChI=1S/C4H9O2/c1-2-4(6)3-5/h4-5H,2-3H2,1H3
c4h8oh-3o     InChI=1S/C4H9O2/c1-4(6)2-3-5/h4-5H,2-3H2,1H3
c4h8oh-4o     InChI=1S/C4H9O2/c5-3-1-2-4-6/h5H,1-4H2
!
hoch2cho    InChI=1S/C2H4O2/c3-1-2-4/h1,4H,2H2
hoch2co      InChI=1S/C2H3O2/c3-1-2-4/h3H,1H2
hoc2h4cho  InChI=1S/C3H6O2/c4-2-1-3-5/h2,5H,1,3H2
hoc2h4co    InChI=1S/C3H5O2/c4-2-1-3-5/h4H,1-2H2
!
! Added for mani low T iso-butanol mech

ic4h8oh-1o2    InChI=1S/C4H9O3/c1-3(2)4(5)7-6/h3-5H,1-2H3
ic4h8oh-2o2    InChI=1S/C4H9O3/c1-4(2,3-5)7-6/h5H,3H2,1-2H3
ic4h8oh-3o2    InChI=1S/C4H9O3/c1-4(2-5)3-7-6/h4-5H,2-3H2,1H3
!
ic4h7oh-1ooh-2   InChI=1S/C4H9O3/c1-3(2)4(5)7-6/h4-6H,1-2H3
ic4h7oh-1ooh-3   InChI=1S/C4H9O3/c1-3(2)4(5)7-6/h3-6H,1H2,2H3
ic4h7oh-2ooh-3   InChI=1S/C4H9O3/c1-4(2,3-5)7-6/h5-6H,1,3H2,2H3
ic4h7oh-2ooh-1   InChI=1S/C4H9O3/c1-4(2,3-5)7-6/h3,5-6H,1-2H3
ic4h7oh-3ooh-1   InChI=1S/C4H9O3/c1-4(2-5)3-7-6/h2,4-6H,3H2,1H3
ic4h7oh-3ooh-2   InChI=1S/C4H9O3/c1-4(2-5)3-7-6/h5-6H,2-3H2,1H3
ic4h7oh-3ooh-3   InChI=1S/C4H9O3/c1-4(2-5)3-7-6/h4-6H,1-3H2
!
ic4h7oh-1ooh-2o2  InChI=1S/C4H9O5/c1-4(2,9-7)3(5)8-6/h3,5-6H,1-2H3
ic4h7oh-1ooh-3o2  InChI=1S/C4H9O5/c1-3(2-8-6)4(5)9-7/h3-5,7H,2H2,1H3
ic4h7oh-2ooh-1o2   InChI=1S/C4H9O5/c1-4(2,9-7)3(5)8-6/h3,5,7H,1-2H3
ic4h7oh-2ooh-3o2   InChI=1S/C4H9O5/c1-4(2-5,9-7)3-8-6/h5,7H,2-3H2,1H3
ic4h7oh-3ooh-1o2   InChI=1S/C4H9O5/c1-3(2-8-6)4(5)9-7/h3-6H,2H2,1H3
ic4h7oh-3ooh-2o2   InChI=1S/C4H9O5/c1-4(2-5,9-7)3-8-6/h5-6H,2-3H2,1H3
ic4h7oh-3ooh-3o2   InChI=1S/C4H9O5/c5-1-4(2-8-6)3-9-7/h4-6H,1-3H2
!
ic4ohket1-2    InChI=1S/C4H8O4/c1-4(2,8-7)3(5)6/h7H,1-2H3,(H,5,6)
ic4ohket1-3    InChI=1S/C4H8O4/c1-3(2-8-7)4(5)6/h3,7H,2H2,1H3,(H,5,6)
ic4ohket3-1    InChI=1S/C4H8O4/c1-3(2-5)4(6)8-7/h2-4,6-7H,1H3
ic4ohket3-2    InChI=1S/C4H8O4/c1-4(2-5,3-6)8-7/h2,6-7H,3H2,1H3
ic4ohket3-3    InChI=1S/C4H8O4/c5-1-4(2-6)3-8-7/h1,4,6-7H,2-3H2
!
ic4h7oho1-2     InChI=1S/C4H8O2/c1-4(2)3(5)6-4/h3,5H,1-2H3
ic4h7oho1-3     InChI=1S/C4H8O2/c1-3-2-6-4(3)5/h3-5H,2H2,1H3
ic4h7oho2-3     InChI=1S/C4H8O2/c1-4(2-5)3-6-4/h5H,2-3H2,1H3
ic4h7oho3-3     InChI=1S/C4H8O2/c5-1-4-2-6-3-4/h4-5H,1-3H2
!
ic4h8oh-1o2h     InChI=1S/C4H10O3/c1-3(2)4(5)7-6/h3-6H,1-2H3
ic4h8oh-2o2h     InChI=1S/C4H10O3/c1-4(2,3-5)7-6/h5-6H,3H2,1-2H3
ic4h8oh-3o2h     InChI=1S/C4H10O3/c1-4(2-5)3-7-6/h4-6H,2-3H2,1H3
!
ic4h8oh-1o    InChI=1S/C4H9O2/c1-3(2)4(5)6/h3-5H,1-2H3
ic4h8oh-2o    InChI=1S/C4H9O2/c1-4(2,6)3-5/h5H,3H2,1-2H3
ic4h8oh-3o    InChI=1S/C4H9O2/c1-4(2-5)3-6/h4-5H,2-3H2,1H3

!
! Added for mani low T tert-butanol mech

tc4h8oh-o2       InChI=1S/C4H9O3/c1-4(2,5)3-7-6/h5H,3H2,1-2H3
!
tc4h7oh-ooh     InChI=1S/C4H9O3/c1-4(2,5)3-7-6/h5-6H,1,3H2,2H3
tc4h8o-ooh       InChI=1S/C4H9O3/c1-4(2,5)3-7-6/h6H,3H2,1-2H3
!
tc4h7oh-ooh-o2   InChI=1S/C4H9O5/c1-4(5,2-8-6)3-9-7/h5-6H,2-3H2,1H3
!
tc4ohket            InChI=1S/C4H8O4/c1-4(6,2-5)3-8-7/h2,6-7H,3H2,1H3
!
tc4h7oho           InChI=1S/C4H8O2/c1-4(5)2-6-3-4/h5H,2-3H2,1H3
!
tc4h8oh-o2h      InChI=1S/C4H10O3/c1-4(2,5)3-7-6/h5-6H,3H2,1-2H3
!
tc4h8oh-o          InChI=1S/C4H9O2/c1-4(2,6)3-5/h6H,3H2,1-2H3
!
!
! Added for mani low T 1-butanol mech

sc4h8oh-1o2    InChI=1S/C4H9O3/c1-3-4(2,5)7-6/h5H,3H2,1-2H3
sc4h8oh-2o2    InChI=1S/C4H9O3/c1-3(5)4(2)7-6/h3-5H,1-2H3
sc4h8oh-3o2    InChI=1S/C4H9O3/c1-4(5)2-3-7-6/h4-5H,2-3H2,1H3
sc4h8oh-mo2   InChI=1S/C4H9O3/c1-2-4(5)3-7-6/h4-5H,2-3H2,1H3
!
sc4h7oh-1ooh-2     InChI=1S/C4H9O3/c1-3-4(2,5)7-6/h3,5-6H,1-2H3
sc4h7oh-1ooh-3     InChI=1S/C4H9O3/c1-3-4(2,5)7-6/h5-6H,1,3H2,2H3
sc4h7oh-1ooh-m    InChI=1S/C4H9O3/c1-3-4(2,5)7-6/h5-6H,2-3H2,1H3
sc4h7oh-2ooh-m    InChI=1S/C4H9O3/c1-3(5)4(2)7-6/h3-6H,1H2,2H3
sc4h7oh-2ooh-3   InChI=1S/C4H9O3/c1-3(5)4(2)7-6/h3-6H,2H2,1H3
sc4h7oh-2ooh-1   InChI=1S/C4H9O3/c1-3(5)4(2)7-6/h4-6H,1-2H3
sc4h7oh-3ooh-1   InChI=1S/C4H9O3/c1-4(5)2-3-7-6/h5-6H,2-3H2,1H3
sc4h7oh-3ooh-m  InChI=1S/C4H9O3/c1-4(5)2-3-7-6/h4-6H,1-3H2
sc4h7oh-3ooh-2   InChI=1S/C4H9O3/c1-4(5)2-3-7-6/h2,4-6H,3H2,1H3
sc4h7oh-mooh-3  InChI=1S/C4H9O3/c1-2-4(5)3-7-6/h4-6H,1-3H2
sc4h7oh-mooh-2  InChI=1S/C4H9O3/c1-2-4(5)3-7-6/h2,4-6H,3H2,1H3
sc4h7oh-mooh-1  InChI=1S/C4H9O3/c1-2-4(5)3-7-6/h5-6H,2-3H2,1H3
!
sc4h7oh-1ooh-2o2    InChI=1S/C4H9O5/c1-3(8-6)4(2,5)9-7/h3,5,7H,1-2H3
sc4h7oh-1ooh-3o2    InChI=1S/C4H9O5/c1-4(5,9-7)2-3-8-6/h5,7H,2-3H2,1H3
sc4h7oh-1ooh-mo2   InChI=1S/C4H9O5/c1-2-4(5,9-7)3-8-6/h5,7H,2-3H2,1H3
sc4h7oh-2ooh-1o2    InChI=1S/C4H9O5/c1-3(8-6)4(2,5)9-7/h3,5-6H,1-2H3
sc4h7oh-2ooh-3o2    InChI=1S/C4H9O5/c1-3(5)4(9-7)2-8-6/h3-5,7H,2H2,1H3
sc4h7oh-2ooh-mo2   InChI=1S/C4H9O5/c1-3(9-7)4(5)2-8-6/h3-5,7H,2H2,1H3
sc4h7oh-3ooh-1o2    InChI=1S/C4H9O5/c1-4(5,9-7)2-3-8-6/h5-6H,2-3H2,1H3
sc4h7oh-3ooh-2o2    InChI=1S/C4H9O5/c1-3(5)4(9-7)2-8-6/h3-6H,2H2,1H3
sc4h7oh-3ooh-mo2   InChI=1S/C4H9O5/c5-4(3-9-7)1-2-8-6/h4-6H,1-3H2
sc4h7oh-mooh-1o2   InChI=1S/C4H9O5/c1-2-4(5,9-7)3-8-6/h5-6H,2-3H2,1H3
sc4h7oh-mooh-2o2   InChI=1S/C4H9O5/c1-3(9-7)4(5)2-8-6/h3-6H,2H2,1H3
sc4h7oh-mooh-3o2   InChI=1S/C4H9O5/c5-4(3-9-7)1-2-8-6/h4-5,7H,1-3H2
!
sc4ohket2-1     InChI=1S/C4H8O4/c1-3(5)4(2,6)8-7/h6-7H,1-2H3
sc4ohket2-3     InChI=1S/C4H8O4/c1-3(5)4(6)2-8-7/h3,5,7H,2H2,1H3
sc4ohket2-m    InChI=1S/C4H8O4/c1-3(5)4(6)2-8-7/h4,6-7H,2H2,1H3
sc4ohket3-1     InChI=1S/C4H8O4/c1-3(6)4(2-5)8-7/h2-4,6-7H,1H3
sc4ohket3-2      InChI=1S/C4H8O4/c1-4(6,8-7)2-3-5/h3,6-7H,2H2,1H3
sc4ohket3-m     InChI=1S/C4H8O4/c5-2-1-4(6)3-8-7/h2,4,6-7H,1,3H2
sc4ohketm-1     InChI=1S/C4H8O4/c1-2-4(6,3-5)8-7/h3,6-7H,2H2,1H3
sc4ohketm-2     InChI=1S/C4H8O4/c1-2-4(6,3-5)8-7/h3,6-7H,2H2,1H3
sc4ohketm-3     InChI=1S/C4H8O4/c5-3-4(6)1-2-8-7/h3-4,6-7H,1-2H2
!
sc4h7oho1-2     InChI=1S/C4H8O2/c1-3-4(2,5)6-3/h3,5H,1-2H3
sc4h7oho1-3     InChI=1S/C4H8O2/c1-3-4(2,5)6-3/h3,5H,1-2H3
sc4h7oho1-m    InChI=1S/C4H8O2/c1-2-4(5)3-6-4/h5H,2-3H2,1H3
sc4h7oho2-3     InChI=1S/C4H8O2/c1-3(5)4-2-6-4/h3-5H,2H2,1H3
sc4h7oho2-m    InChI=1S/C4H8O2/c1-3-4(5)2-6-3/h3-5H,2H2,1H3
sc4h7oho3-m    InChI=1S/C4H8O2/c5-4-1-2-6-3-4/h4-5H,1-3H2
!
sc4h8oh-1o2h   InChI=1S/C4H10O3/c1-3-4(2,5)7-6/h5-6H,3H2,1-2H3
sc4h8oh-2o2h   InChI=1S/C4H10O3/c1-3(5)4(2)7-6/h3-6H,1-2H3
sc4h8oh-3o2h   InChI=1S/C4H10O3/c1-4(5)2-3-7-6/h4-6H,2-3H2,1H3
sc4h8oh-mo2h  InChI=1S/C4H10O3/c1-2-4(5)3-7-6/h4-6H,2-3H2,1H3
!
sc4h8oh-1o    InChI=1S/C4H9O2/c1-3-4(2,5)6/h5H,3H2,1-2H3
sc4h8oh-2o    InChI=1S/C4H9O2/c1-3(5)4(2)6/h3-5H,1-2H3
sc4h8oh-3o    InChI=1S/C4H9O2/c1-4(6)2-3-5/h4,6H,2-3H2,1H3
sc4h8oh-mo   InChI=1S/C4H9O2/c1-2-4(6)3-5/h4,6H,2-3H2,1H3
!
!
"""
species = speciesList.split('\n')
newLines = []
for line in species:
    if 'InChI' in line:
        nickname, inchi = line.split()
        nickname = nickname.lower()
        try:
            mol = Molecule().fromInChI(inchi)
        except:
            import ipdb; ipdb.set_trace()

        try:
            newLine = nickname + '\t' + mol.toSMILES()
        except ValueError, e:
            if inchi=='InChI=1/C3H2/c1-3-2/h1-2H':
                newLine = nickname + '\t' + '[CH]C#C'
            else:
                print "Couldn't do {0} due to {1}".format(line, e.message)
        newLines.append(newLine)

input_string = '\n'.join(newLines)

with open('SMILES.txt', 'w') as smilesfile:
    smilesfile.write(input_string)
