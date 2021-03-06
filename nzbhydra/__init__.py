from os.path import dirname, abspath

configFile = None
databaseFile = None

def getBasePath():
    try:
        basepath = dirname(dirname(abspath(__file__)))
    except NameError:  # We are the main py2exe script, not a module
        import sys
        basepath = dirname(abspath(sys.argv[0]))
    if "library.zip" in basepath:
        basepath = basepath[:basepath.find("library.zip")]
    return basepath