from util.chromosomeRearrangementPainting import plotChrsRearrangement

"""
Chromosomes painting for Gramineae in evolution history. 
result in outdutdata/Gramineae/plot
"""
## please use your path
path = 'D:/IAG'

# colors for target species chromosomes, Ancestor 2
colorlist = ['#DF1159','#1E93C9','#26AF67','#D5A1C5','#EBCA6D',
             '#94B51E','#000000','#A9A9A9']

block_length_file = path + '/input/Legume/blockindex.genenumber'
target_species_block_file = path + '/output/Legume/ancestor3/Ancestor2.block'
target_species_name = 'Ancestor2'
target_species_copy_number = 2

"""
Ancestor 2 -> O. viciifolia
"""
rearranged_species_block_file = path + '/input/Legume/Oviciifolia.final.block'
rearranged_species_name = 'O.viciifolia'
rearranged_species_copy_number = 2

outdir = path + '/output/plot/2-Ov/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

