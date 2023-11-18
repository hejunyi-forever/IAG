from util.chromosomeRearrangementPainting import plotChrsRearrangement

"""
Chromosomes painting for Gramineae in evolution history. 
result in outdutdata/Gramineae/plot
"""
## please use your path
path = 'D:/IAG'

# colors for target species chromosomes, Ancestor 2
#Ancestor2color = ['#DF1159','#D8E3E7','#D5A1C5','#876818','#FB9968',
#             '#000000','#A9A9A9']


colorlist = ['#990000','#CC6600','#CCCC00','#D8E3E7','#006666',
             '#003366','#4C0099','#000000']

block_length_file = path + '/input/Legume/blockindex.genenumber'
target_species_block_file = path + '/output/Legume/ancestor2/Ancestor2.block'
target_species_name = 'Ancestor2'
target_species_copy_number = 2

"""
Ancestor 2 -> Ancestor 3
"""
rearranged_species_block_file = path + '/input/Legume/Ancestor3.block'
rearranged_species_name = 'Ancestor3'
rearranged_species_copy_number = 2

outdir = path + '/output/plot/2-3/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

