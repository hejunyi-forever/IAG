from models.MultiGGHPmodel import MultiCopyGGHPmodel
from models.MultiGMPmodel import MultiCopyGMPmodel
from util.calculatedCRBrateAndEstimationAccuracy import calculatedCRBrateAndEstimationAccuracy
from util.cutCircularChromosomes import cutCircularChromosomes

"""
Inferring ancestor species for Gramineae species. 
Ancestor 4: Multi-copy GGHP model, result in outdutdata/Gramineae/Ancestor4
Ancestor 3: Multi-copy GMP model, result in outdutdata/Gramineae/Ancestor3
Ancestor 2: Multi-copy GMP model, result in outdutdata/Gramineae/Ancestor2
Ancestor 1: Multi-copy GMP model, result in outdutdata/Gramineae/Ancestor1

"""
## please use your path
path = 'D:/IAG'

workdir = path + '/inputdata/Legue/'

"""
Inferring ancestor species for Gramineae species. 
Ancestor 3 using Multi-copy GMP model
"""
species_file_list = [workdir + 'Carietinum.final.block',
                     workdir + 'Ljaponicus.final.block',
                     workdir + 'Msativa.final.block',
                     workdir + 'Mtruncatula.final.block',
                     workdir + 'Oviciifolia.final.block',
                     workdir + 'Psativum.final.block']
guided_species_for_matching = workdir + 'Oviciifolia.final.block'
ancestor_target_copy_number = 2
outAncestor3dir = path + '/outputdata/Ancestor/'
ancestor_name = 'Ancestor'
MultiCopyGMPmodel(species_file_list, outAncestor3dir, guided_species_for_matching, ancestor_name, ancestor_target_copy_number)

# Evaluation
