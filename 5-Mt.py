from util.chromosomeRearrangementPainting import plotChrsRearrangement

"""
Chromosomes painting for Gramineae in evolution history. 
result in outdutdata/Gramineae/plot
"""
## please use your path
path = 'D:/IAG'

# colors for target species chromosomes, Ancestor 5
colorlist = ['#990000','#FF6666','#6666FF','#CCCC00','#006666',
             '#FF3399','#B266FF','#003366']

block_length_file = path + '/input/Legume/blockindex.genenumber'
target_species_block_file = path + '/output/Legume/ancestor5/Ancestor5.block'
target_species_name = 'Ancestor5'
target_species_copy_number = 2

"""
Ancestor 5 -> M. truncatula
"""
rearranged_species_block_file = path + '/input/Legume/Mtruncatula.final.block'
rearranged_species_name = 'M.truncatula'
rearranged_species_copy_number = 2

outdir = path + '/output/plot/5-Mt/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

