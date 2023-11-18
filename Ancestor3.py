from models.MultiGMPmodel import MultiCopyGMPmodel
from models.MultiGGHPmodel import MultiCopyGGHPmodel
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

workdir = path + '/input/Legume/'

"""
Inferring ancestor species for Gramineae species. 
Ancestor 6 using Multi-copy GMP model
"""
species_file_list = [workdir + 'Carietinum.final.block',
                     workdir + 'Ancestor4.block',
                     workdir + 'Oviciifolia.final.block']
guided_species_for_matching = workdir + 'Carietinum.final.block'
ancestor_target_copy_number = 2
outAncestor3dir = path + '/output/Legume/ancestor3/'
ancestor_name = 'Ancestor3'
MultiCopyGMPmodel(species_file_list, outAncestor3dir, guided_species_for_matching, ancestor_name, ancestor_target_copy_number)

# Evaluation
matching_target_file = workdir + 'Carietinum.final.block'
matching_target_copy_number = ancestor_target_copy_number
matching_target_name = 'C.arietinum'
speciesAndCopyList = [
    [workdir + 'Carietinum.final.block',ancestor_target_copy_number,'C.arietinum'],
    [workdir + 'Ancestor4.block',ancestor_target_copy_number,'Ancestor4'],
    [workdir + 'Oviciifolia.final.block',ancestor_target_copy_number,'O.viciifolia']
]

model_type = 'MultiCopyGMP'
calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outAncestor3dir, model_type)
