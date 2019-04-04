
# This example creates an SDE connection file.  This script MUST BE PLACED IN A
#  PATHNAME THAT HAS NO SPACES.  For example:
#    E:\SDE Connection File Example\Scripts   --> WRONG!
#    E:\SDEConnectionFileExample\Scripts      --> Right.
#
# The reasons for this are arcane and have to do with Java's unix roots.
#

import os, sys

# Routine to create an ArcSDE connection file.  Calls the Java class CreateSDEConnFile
#
def createSDEConnFile(connFilePath, sdeFileName, serverName, instance, database, \
                      userName, passwd, versionName, platformName, javaToolLocation):

    try:
        # The pathname to the output connection file CANNOT contain spaces.  Throw
        #  exception if it does.
        #
        if connFilePath.find(" ") > -1:
            raise Exception, "Output sde pathname cannot contain spaces"
        if javaToolLocation.find(" ") > -1:
            raise Exception, "Java class location cannot contain spaces"

        # Get JAVA_HOME and ARCGISHOME and test that they are set.  We don't test if
        #  the path actually exists.
        #
        arcHome = os.environ.get("ARCGISHOME")
        javaHome = os.environ.get("JAVA_HOME")	
        if not bool(arcHome):
            raise Exception, "System environment ARCGISHOME not set"
        if not bool (javaHome):
            raise Exception, "System environment JAVA_HOME not set"	

        javaHome = '"' + javaHome + os.sep + '"'

        # Construct the pathname to the java class, then construct the os command to execute the
        #  java class.  Since we're using command prompt syntax, we need 
        #  double quotes for windows pathnames.
        #
        if platformName == "Windows": 

            javaClassPath = arcHome + "java" + os.sep + "lib" + os.sep + r"arcobjects.jar;" + javaToolLocation 

            command = '"' + javaHome + "bin" + os.sep + "java -classpath" + " " + '"' + javaClassPath +\
                    '" '+ \
                    "CreateSDEConnFile.CreateSDEConnFile" + " " + connFilePath + " " +\
                    sdeFileName + " " + serverName + " " + instance + " " + userName + " " +\
                    passwd + " " + versionName + " " + database + '"'
            rv = os.system(command)

        else:
            javaClassPath = '"' + arcHome + "java" + os.sep + "lib" + \
                          os.sep + r"arcobjects.jar:" + javaToolLocation + '"'

            rv = os.system(javaHome + "bin" + os.sep + "java -client -Xss2m -classpath" + " " + \
                           javaClassPath + " " + "CreateSDEConnFile.CreateSDEConnFile" + " " + \
                           connFilePath + " " + sdeFileName + " " + serverName + " " + instance + " " + \
                           userName + " " + passwd + " " + versionName + " " + database)

        if rv:
            raise Exception, "Failure in external call to create " + sdeFileName

        # All clear.... return the connect file name.
        #
        return connFilePath + os.sep + sdeFileName

    except:
        raise Exception, "$PHU Warning Create of " + sdeFileName + " failed"


if __name__ == "__main__":

    # Get the pathname to this python script file.  The java class is found in the same
    #  location in a subfolder named "CreateSDEConnFile"
    #
    scriptPath = os.path.dirname(sys.argv[0]) 
    javaClassLocation = scriptPath + os.sep + "CreateSDEConnFile"

    # Set the output location for the sde connection file.  This can be 
    #  any existing folder on your system, but the pathname should not contain
    #  spaces.  In this case, we'll set it to the same location as our script 
    #  path since we know that has to exist.
    #
    outloc = scriptPath

    # Create the connection file
    #  Arguments:
    #    1 Folder where to create the connection file
    #    2 Name of connection file to create in outloc
    #    3 Name of SDE server
    #    4 Port number
    #    5 Database name
    #    6 Username
    #    7 Password
    #    8 Version
    #    9 Platform
    #   10 Pathname to the CreateSDEConnFile folder.  See above.
    #
    connfile = createSDEConnFile(outloc,\
                                 "toolbox.sde",\
                                 "gpserver",\
                                 "5151",\
                                 "none",\
                                 "toolbox",\
                                 "password",\
                                 "SDE.DEFAULT",\
                                 "Windows",\
                                 javaClassLocation)         

