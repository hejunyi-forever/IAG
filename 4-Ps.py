from util.chromosomeRearrangementPainting import plotChrsRearrangement

"""
Chromosomes painting for Gramineae in evolution history. 
result in outdutdata/Gramineae/plot
"""
## please use your path
path = 'D:/IAG'

# colors for target species chromosomes, Ancestor 4
colorlist = ['#990000','#FF6666','#FFB266','#CCCC00','#66FF66',
             '#006666','#003366','#B266FF']

block_length_file = path + '/input/Legume/blockindex.genenumber'
target_species_block_file = path + '/output/Legume/ancestor4/Ancestor4.block'
target_species_name = 'Ancestor4'
target_species_copy_number = 2

"""
Ancestor 4 -> P. sativum
"""
rearranged_species_block_file = path + '/input/Legume/Psativum.final.block'
rearranged_species_name = 'P.sativum'
rearranged_species_copy_number = 2

outdir = path + '/output/plot/4-Ps/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

