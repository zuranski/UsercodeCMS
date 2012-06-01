def listAllFiles(readFiles, searchName, useMaxFiles=999999, firstFile=1):

# To facilitate the use of PoolSource.
# Define: readFiles = cms.untracked.vstring()
# Then do listOfFiles(readFiles, "mydir/fun*.root")
# and all the files found will be added to readFiles
# such that you can use them in:
# process.source = cms.Source ("PoolSource",fileNames = readFiles)
# To read a normal directory, mydir should be 'file:/opt/ppd/cms/users/tomalin/.../*.root'
# To read dcache it should be '/store/user/tomalini/.../*.root'
# To read castor, it should be 'rfio:/castor/.../"
# N.B. For castor, no wild-cards are allowed, so you should not specify *.root

# glob can't look at dcache area ...
#    import glob
#    files = glob.glob(searchName)

# Fragment of dcache directory name
    dcachename = '/pnfs/cms-pg/11'

    normalFileWords = searchName.split('file:')
    castorFileWords = searchName.split('rfio:')
    
# Note if is a normal file or castor file. If not, then must be dcache.
    isNormal = len(normalFileWords) > 1
    isCastor = len(castorFileWords) > 1
    isDcache = not (isNormal or isCastor)

    if isNormal:
        searchNameCor = normalFileWords[1]
        print "Looking at normal directory %s" %searchNameCor
    elif isCastor:
        searchNameCor = castorFileWords[1]
        print "Looking at normal directory %s" %searchNameCor        
    elif isDcache:
        searchNameCor = dcachename + searchName
        print "Looking at dcache directory %s" %searchNameCor
        print "This can be slow ..."
    
# List all files (including full path name)
    import os
    if isCastor:
       files = os.popen('rfdir ' + searchNameCor)
    else:
       # files = os.popen('find -noleaf -name ' + searchNameCor).readlines()
       files = os.popen('ls -1 ' + searchNameCor)

    ifile = 0
    iused = 0
    for f in files:
        ifile += 1
        if (ifile < firstFile): continue

        iused += 1
        if iused <= useMaxFiles:

            # Correct format to that expected by CMSSW PoolSource
            if isDcache:
                fcor = f.split(dcachename)
                line = fcor[1]
            elif isCastor:
                fcor = f.split(" ")
                line = "%s/%s" %(searchName, fcor[-1])
            elif isNormal:
                # File in normal directory
                line = "file:%s" %f
                
            # Remove annoying end-of-line character
            line = line.rstrip('\n')
            readFiles.append(line)

    if len(readFiles) > 0:
        print "Found ",len(readFiles)," in input file ",searchName
    else:
        print "ERROR: Found no files in input file ",searchName
        sys.exit("quitting")


def listAllFilesDBS(readFiles, dataset, useMaxFiles=999999, firstFile=1):

    # use dbs tool for getting file list
    import os
    command = "dbsql find file where dataset="+dataset
    commandOutput = os.popen(command).read().split()
    datasetFiles = [item for item in commandOutput if item.find('/store')==0]

    # add files to readFiles cms.pretty.variable and apply first file and max files options
    for datafile in datasetFiles[firstFile:]:
        readFiles.append(datafile)
        if len(readFiles) == useMaxFiles : break
