from util.calculateFissionsAndFusions import calculateFissionAndFussions

"""
Calculating Fissions and Fusions for Gramineae in evolution history. 
result in outdutdata/Gramineae
"""
## please use your path
path = 'D:/IAG'

outfile = path + '/output/ShufflingEvents/shufflingEvents.txt'
outfile = open(outfile,'w')


"""
Ancestor 1 -> Ancestor 2
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor1_block_sequence_dir = path + '/output/Legume/ancestor1/'

descendant_file = species_block_sequence_dir + 'ancestor2.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> Ancestor 2\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 1 -> Ancestor 6
"""
ancestor1_block_sequence_dir = path + '/output/Legume/ancestor1/'
ancestor6_block_sequence_dir = path + '/output/Legume/ancestor6/'

descendant_file = ancestor6_block_sequence_dir + 'Ancestor6.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> Ancestor 6\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 1 -> L. japonicus
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor1_block_sequence_dir = path + '/output/Legume/ancestor1/'

descendant_file = species_block_sequence_dir + 'Ljaponicus.final.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> L. japonicus\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 1 -> C. arietinum
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor1_block_sequence_dir = path + '/output/Legume/ancestor1/'

descendant_file = species_block_sequence_dir + 'Carietinum.final.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> C. arietinum\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
Ancestor 1 -> M. sativa
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor1_block_sequence_dir = path + '/output/Legume/ancestor1/'

descendant_file = species_block_sequence_dir + 'Msativa.final.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> M. sativa\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 1 -> M. truncatula
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor1_block_sequence_dir = path + '/output/Legume/ancestor1/'

descendant_file = species_block_sequence_dir + 'Mtruncatula.final.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> M. truncatula\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 1 -> O. viciifolia
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor1_block_sequence_dir = path + '/output/Legume/ancestor1/'

descendant_file = species_block_sequence_dir + 'Oviciifolia.final.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> O. viciifolia\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 1 -> P. sativum
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor1_block_sequence_dir = path + '/output/Legume/ancestor1/'

descendant_file = species_block_sequence_dir + 'Psativum.final.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> P. sativum\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')



"""
Ancestor 1 -> G. max
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor1_block_sequence_dir = path + '/output/Legume/ancestor1/'

descendant_file = species_block_sequence_dir + 'Gmax.final.block'
ancestor_file = ancestor1_block_sequence_dir + 'Ancestor1.block'

descendant_copy_number = 4
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor1_block_sequence_dir)
outfile.write('Ancestor 1 -> G. max\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 2 -> Ancestor 3
"""
ancestor3_block_sequence_dir = path + '/output/Legume/ancestor3/'
ancestor2_block_sequence_dir = path + '/output/Legume/ancestor2/'

descendant_file = ancestor3_block_sequence_dir + 'Ancestor3.block'
ancestor_file = ancestor2_block_sequence_dir + 'Ancestor2.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor2_block_sequence_dir)
outfile.write('Ancestor 2 -> Ancestor 3\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')



"""
Ancestor 2 -> C. arietinum
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor2_block_sequence_dir = path + '/output/Legume/ancestor2/'

descendant_file = species_block_sequence_dir + 'Carietinum.final.block'
ancestor_file = ancestor2_block_sequence_dir + 'Ancestor2.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor2_block_sequence_dir)
outfile.write('Ancestor 2 -> Carietinum\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 2 -> O. viciifolia
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor2_block_sequence_dir = path + '/output/Legume/ancestor2/'

descendant_file = species_block_sequence_dir + 'Oviciifolia.final.block'
ancestor_file = ancestor2_block_sequence_dir + 'Ancestor2.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor2_block_sequence_dir)
outfile.write('Ancestor 2 -> O. viciifolia\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
Ancestor 3 -> Ancestor 4
"""
ancestor4_block_sequence_dir = path + '/output/Legume/ancestor4/'
ancestor3_block_sequence_dir = path + '/output/Legume/ancestor3/'

descendant_file = ancestor4_block_sequence_dir + 'Ancestor4.block'
ancestor_file = ancestor3_block_sequence_dir + 'Ancestor3.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor3_block_sequence_dir)
outfile.write('Ancestor 3 -> Ancestor 4\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')



"""
Ancestor 3 -> C. arietinum
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor3_block_sequence_dir = path + '/output/Legume/ancestor3/'

descendant_file = species_block_sequence_dir + 'Carietinum.final.block'
ancestor_file = ancestor3_block_sequence_dir + 'Ancestor3.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor3_block_sequence_dir)
outfile.write('Ancestor 3 -> C. arietinum\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 4 -> Ancestor 5
"""
ancestor5_block_sequence_dir = path + '/output/Legume/ancestor5/'
ancestor4_block_sequence_dir = path + '/output/Legume/ancestor4/'

descendant_file = ancestor5_block_sequence_dir + 'Ancestor5.block'
ancestor_file = ancestor4_block_sequence_dir + 'Ancestor4.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor4_block_sequence_dir)

outfile.write('Ancestor 4 -> Ancestor 5\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 4 -> P. sativum
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor4_block_sequence_dir = path + '/output/Legume/ancestor4/'

descendant_file = species_block_sequence_dir + 'Psativum.final.block'
ancestor_file = ancestor4_block_sequence_dir + 'Ancestor4.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor4_block_sequence_dir)


outfile.write('Ancestor 4 -> P. sativum\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')

"""
Ancestor 5 -> M. sativa
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor5_block_sequence_dir = path + '/output/Legume/ancestor5/'

descendant_file = species_block_sequence_dir + 'Msativa.final.block'
ancestor_file = ancestor5_block_sequence_dir + 'Ancestor5.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor5_block_sequence_dir)


outfile.write('Ancestor 5 -> M. sativa\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
Ancestor 5 -> M. truncatula
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor5_block_sequence_dir = path + '/output/Legume/ancestor5/'

descendant_file = species_block_sequence_dir + 'Mtruncatula.final.block'
ancestor_file = ancestor5_block_sequence_dir + 'Ancestor5.block'

descendant_copy_number = 2
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor5_block_sequence_dir)


outfile.write('Ancestor 5 -> M. truncatula\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')


"""
Ancestor 6 -> G. max
"""
species_block_sequence_dir = path + '/input/Legume/'
ancestor6_block_sequence_dir = path + '/output/Legume/ancestor6/'

descendant_file = species_block_sequence_dir + 'Gmax.final.block'
ancestor_file = ancestor6_block_sequence_dir + 'Ancestor6.block'

descendant_copy_number = 4
ancestor_copy_number = 2

fissions,fusions = calculateFissionAndFussions(descendant_file,ancestor_file,
                                               descendant_copy_number,ancestor_copy_number,
                                               ancestor6_block_sequence_dir)


outfile.write('Ancestor 6 -> G. max\n' +
              'fissions: '+ str(fissions)+'\t' + 'fusions: '+str(fusions)+'\n')
outfile.close()
