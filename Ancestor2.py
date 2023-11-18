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
species_file_list = [workdir + 'Oviciifolia.final.block',
                     workdir + 'Ancestor3.block',
                     workdir + 'Ljaponicus.final.block']
guided_species_for_matching = workdir + 'Oviciifolia.final.block'
ancestor_target_copy_number = 2
outAncestor2dir = path + '/output/Legume/ancestor2/'
ancestor_name = 'Ancestor2'
MultiCopyGMPmodel(species_file_list, outAncestor2dir, guided_species_for_matching, ancestor_name, ancestor_target_copy_number)

# Evaluation
matching_target_file = workdir + 'Oviciifolia.final.block'
matching_target_copy_number = ancestor_target_copy_number
matching_target_name = 'O.viciifolia'
speciesAndCopyList = [
    [workdir + 'Oviciifolia.final.block',ancestor_target_copy_number,'O.viciifolia'],
    [workdir + 'Ancestor3.block',ancestor_target_copy_number,'Ancestor3'],
    [workdir + 'Ljaponicus.final.block',ancestor_target_copy_number,'L.japonicus']
]

model_type = 'MultiCopyGMP'
calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outAncestor2dir, model_type)
