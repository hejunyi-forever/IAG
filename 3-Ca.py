from util.chromosomeRearrangementPainting import plotChrsRearrangement

"""
Chromosomes painting for Gramineae in evolution history. 
result in outdutdata/Gramineae/plot
"""
## please use your path
path = 'D:/IAG'

# colors for target species chromosomes, Ancestor 3
colorlist = ['#990000','#CC0000','#FF8000','#CCCC00','#006666',
             '#CC6600','#990099','#003366']

block_length_file = path + '/input/Legume/blockindex.genenumber'
target_species_block_file = path + '/output/Legume/ancestor3/Ancestor3.block'
target_species_name = 'Ancestor3'
target_species_copy_number = 2

"""
Ancestor 3 -> C. arietinum
"""
rearranged_species_block_file = path + '/input/Legume/Carietinum.final.block'
rearranged_species_name = 'C.arietinum'
rearranged_species_copy_number = 2

outdir = path + '/output/plot/3-Ca/'
plotChrsRearrangement(block_length_file,
                          rearranged_species_block_file,rearranged_species_name,rearranged_species_copy_number,
                          target_species_block_file,target_species_name,target_species_copy_number,
                          colorlist,outdir)

