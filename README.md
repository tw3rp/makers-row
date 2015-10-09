# makers-row
an epic parser
#Pre-requisites
- No installation required
- python (any version will do)
#How to run
-run "python parse.py <inputfile>"
example: python parse.py input.txt
# sample input
3
New York Embroidery Studio,Novelty Pom Pom,Sherry Accessories
Ace Binding Co,Dallas Bias Fabrics,Sherry Accessories
New York Embroidery Studio,Novelty Pom Pom,Pearl Trim & Textile
Baikal,Dallas Bias Fabrics,Novelty Pom Pom,Pearl Trim & Textile,Riva Jewelry Manufacturers
Ace Binding Co,Baikal,Pearl Trim & Textile
Ace Binding Co,Baikal,New York Embroidery Studio,Riva Jewelry Manufacturers,Sherry Accessories
New York Embroidery Studio,Novelty Pom Pom,Pearl Trim & Textile
Dallas Bias Fabrics,Novelty Pom Pom,Pearl Trim & Textile
Ace Binding Co,Baikal,New York Embroidery Studio
Ace Binding Co,New York Embroidery Studio,Riva Jewelry Manufacturers

#sample output
Ace Binding Co,Baikal                                                                                 │~
Ace Binding Co,New York Embroidery Studio                                                             │~
New York Embroidery Studio,Novelty Pom Pom                                                            │~
Novelty Pom Pom,Pearl Trim & Textile

#Details
-The function buildDict creates a dictionary of factories with all combinations and counts the
 occurances as new lines are fed into it 
-the sorting happens only if the conditions are met 
#algorithmic complexity
- The process is similiar to  map and reduce technique. It would run much faster if run on 
 hadoop map and reduce on a cluster for large objects. 
- It infact when tested on about a 260mb file it ran in about a minute.

#cheers ~tw3rp
