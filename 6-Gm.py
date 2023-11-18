from util.chromosomeRearrangementPainting import plotChrsRearrangement

"""
Chromosomes painting for Gramineae in evolution history. 
result in outdutdata/Gramineae/plot
"""
## please use your path
path = 'D:/IAG'

# colors for target species chromosomes, Ancestor 6
#'#DF1159','#D8E3E7','#D5A1C5','#876818','#FB9968',
#             '#000000','#A9A9A9']
colorlist = ['#DF1159','#660000','#FF8000','#999900','#336600',
             '#006666','#330066','#660066','#99FF99','#CCCCFF','#A9A9A9']

block_length_file = path + '/input/Legume/blockindex.genenumber'
target_species_block_file = path + '/output/Legume/ancestor6/Ancestor6.block'
target_species_name = 'Ancestor6'
target_species_copy_number = 2

"""
Ancestor 6 -> G. max
"""
rearranged_species_block_file = path + '/input/Legume/Gmax.final.block'
rearranged_species_name = 'G.max'
rearranged_species_copy_number = 4

outdir = path + '/output/plot/6-Gm/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

