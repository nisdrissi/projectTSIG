# -*- coding: cp1252 -*-
def fmeimporter(fmepath):
    import os,sys
    if not os.path.exists(os.path.join(fmepath,r"FME.app")):
        print("The dir seems not to be a FMEHOME : "+fmepath)
        return False
    
    print("Path seems to be a valid FMEHOME.")
    minor = sys.version_info.minor
    major = sys.version_info.major
    if major <> 2 or minor < 3 or minor > 7:
        print("Your Python version is not supported by FME : "+sys.version)
        return False
    os.environ["PATH"] = fmepath+";"+os.environ["PATH"]
    print("PATH environment variable adapted.")
    sys.path.insert(0,fmepath+r"\fmeobjects\python"+str(major)+str(minor))
    print("FME Python Module Path succesfully added.")
    return True


# correct the environment variables according FME_HOME
if fmeimporter(r"/Applications/FME2016.0"):
#if fmeimporter(r"/Library/FME 2016.0/fmeobjects/python27"):
    import fmeobjects
    print("Module fmeobjects successfully loaded!")
    session = fmeobjects.FMESession()
    print("Version : "+session.fmeVersion())
    print("Build # : "+str(session.fmeBuildNumber()))
    del(session)
