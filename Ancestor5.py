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
species_file_list = [workdir + 'Msativa.final.block',
                     workdir + 'Mtruncatula.final.block',
                     workdir + 'Psativum.final.block']
guided_species_for_matching = workdir + 'Msativa.final.block'
ancestor_target_copy_number = 2
outAncestor5dir = path + '/output/Legume/ancestor5/'
ancestor_name = 'Ancestor5'
MultiCopyGMPmodel(species_file_list, outAncestor5dir, guided_species_for_matching, ancestor_name, ancestor_target_copy_number)

# Evaluation
matching_target_file = workdir + 'Msativa.final.block'
matching_target_copy_number = ancestor_target_copy_number
matching_target_name = 'M.sativa'
speciesAndCopyList = [
    [workdir + 'Msativa.final.block',ancestor_target_copy_number,'M.sativa'],
    [workdir + 'Mtruncatula.final.block',ancestor_target_copy_number,'M.truncatula'],
    [workdir + 'Psativum.final.block',ancestor_target_copy_number,'P.sativum']
]

model_type = 'MultiCopyGMP'
calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outAncestor5dir, model_type)
