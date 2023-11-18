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

"""
species_file_list = [workdir + 'Ancestor2.block',
                     workdir + 'Ljaponicus.final.block',
                     workdir + 'Ancestor6.block']
guided_species_for_matching = workdir + 'Ancestor2.block'
ancestor_target_copy_number = 2
outAncestor1dir = path + '/output/Legume/ancestor1/'
ancestor_name = 'Ancestor1'
MultiCopyGMPmodel(species_file_list, outAncestor1dir, guided_species_for_matching, ancestor_name, ancestor_target_copy_number)

# Evaluation
matching_target_file = workdir + 'Ancestor2.block'
matching_target_copy_number = ancestor_target_copy_number
matching_target_name = 'Ancestor2'
speciesAndCopyList = [
    [workdir + 'Ancestor2.block',ancestor_target_copy_number,'Ancestor2'],
    [workdir + 'Ljaponicus.final.block',ancestor_target_copy_number,'L.japonicus'],
    [workdir + 'Ancestor6.block',ancestor_target_copy_number,'Ancestor6']
]

model_type = 'MultiCopyGMP'
calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outAncestor1dir, model_type)
