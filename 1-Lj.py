from util.chromosomeRearrangementPainting import plotChrsRearrangement

"""
Chromosomes painting for Gramineae in evolution history. 
result in outdutdata/Gramineae/plot
"""
## please use your path
path = 'D:/IAG'

# colors for target species chromosomes, Ancestor 1
colorlist = ['#DF1159','#D8E3E7','#D5A1C5','#876818','#FB9968',
             '#000000','#A9A9A9']

block_length_file = path + '/input/Legume/blockindex.genenumber'
target_species_block_file = path + '/output/Legume/ancestor1/Ancestor1.block'
target_species_name = 'Ancestor1'
target_species_copy_number = 2

"""
Ancestor 1 -> L. japonicus
"""
rearranged_species_block_file = path + '/input/Legume/Ljaponicus.final.block'
rearranged_species_name = 'L.japonicus'
rearranged_species_copy_number = 2

outdir = path + '/output/plot/1-Lj/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

