from util.chromosomeRearrangementPainting import plotChrsRearrangement

"""
Chromosomes painting for Gramineae in evolution history. 
result in outdutdata/Gramineae/plot
"""
## please use your path
path = 'D:/IAG'

# colors for target species chromosomes, Ancestor 4
#['#990000','#CC0000','#FF8000','#CCCC00','',
#             '#CC6600','#990099','#003366']
colorlist = ['#990000','#FF6666','#FFB266','#CCCC00','#66FF66',
             '#006666','#003366','#B266FF']

block_length_file = path + '/input/Legume/blockindex.genenumber'
target_species_block_file = path + '/output/Legume/ancestor4/Ancestor4.block'
target_species_name = 'Ancestor4'
target_species_copy_number = 2

"""
Ancestor 4 -> Ancestor 5
"""
rearranged_species_block_file = path + '/input/Legume/Ancestor5.block'
rearranged_species_name = 'Ancestor5'
rearranged_species_copy_number = 2

outdir = path + '/output/plot/4-5/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

