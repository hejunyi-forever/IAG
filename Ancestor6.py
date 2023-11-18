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
Ancestor 4 using Multi-copy GGHP model
"""
dup_child_file = workdir + 'Gmax.final.block'
outgroup_file = workdir + 'Ljaponicus.final.block'
outAncestor6dir = path + '/output/Legume/ancestor6/'
dup_copy_number = 4
out_copy_number = 2
ancestor_target_copy_number = 2
ancestor_name = 'Ancestor6'
MultiCopyGGHPmodel(dup_child_file, outgroup_file, outAncestor6dir,
                   ancestor_name, dup_copy_number, out_copy_number, ancestor_target_copy_number)

# speciesAndCopyList = [
#     [workdir + 'Zmays.final.block',dup_copy_number,'Z.mays'],
#     [workdir + 'Sbicolor.final.block',out_copy_number,'S.bicolor']
# ]
# cutCircularChromosomes(outAncestor4dir + 'Ancestor4.block',
#                        ancestor_target_copy_number,
#                        ancestor_name,speciesAndCopyList,outAncestor4dir)

# Evaluation
matching_target_file = workdir + 'Ljaponicus.final.block'
matching_target_copy_number = out_copy_number
matching_target_name = 'L.japonicus'

speciesAndCopyList = [
    [workdir + 'Gmax.final.block',dup_copy_number,'G.max'],
    [workdir + 'Ljaponicus.final.block',out_copy_number,'L.japonicus']
]

model_type = 'MultiCopyGGHP'

calculatedCRBrateAndEstimationAccuracy(matching_target_file, matching_target_copy_number, matching_target_name,
                                       speciesAndCopyList, outAncestor6dir, model_type)
