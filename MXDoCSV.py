# coding: utf-8
"""
Tool Name:  Average Nearest Neighbor
Source Name: NearestNeighbor.py
Version: ArcGIS 10.1
Author: ESRI

This tool performs the nearest neighbor measure of spatial clustering.
Given a set of features, it evaluates whether these features are more
or less clustered than we might expect by chance.  The nearest neighbor
approach involves:
(1) Measuring the distance between each feature and its nearest neighbor
(2) Calculating the mean nearest neighbor distance (observed)
(3) Calculating the mean nearest neighbor distance for theoretical random
    distribution (expected)
(4) Comparing the observed and expected by calculating a Z score for 
    their difference.
(5) Displaying the results of whether or not the Z Score is significant.
"""

################### Imports ########################
#Import modules...
import arcpy, os, fnmatch, csv

#User input variables...
mxddirectory ='C:\\Users\\svekhand\\Desktop\\MXDs\\Arc02\\' #arcpy.GetParameterAsText(0)
mxd_single = ''#arcpy.GetParameterAsText(1)
outputcsvlocation = 'C:\\Users\\svekhand\\Documents\\ArcGIS'#arcpy.GetParameterAsText(2)

#Create an empty list of ArcMap documents to process...
mxd_list=[]
#If a user defined a single mxd, add its path to the list...
if len(mxd_single) > 0:
    mxd_list.append(mxd_single)
#Otherwise walk through the input directory, adding paths for
#each .mxd file found to the list...
else:
    for dirpath in os.walk(mxddirectory): #os.walk returns \dirpath, dirnames, filenames)
        for filename in dirpath[2]:
            if fnmatch.fnmatch(filename, "*.mxd"):
                mxd_list.append(os.path.join(dirpath[0], filename))
        
        #Iterate the list of mxd paths and gather property values then  write to csv file...
if len(mxd_list) > 0:
  #Create the csv file...
  #with open('test.csv', 'wb') as csv_file:
   # writer = csv.DictWriter(csv_file, ['header1', 'header2'])
    with open('iti.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  #Write a header row to the csv file...
        spamwriter.writerow(["mxdpath", "layername"])
  #Iterate through the list of ArcMap Documents...
        for mxdpath in mxd_list:
            #mxdFile = os.path.join(root, file)
            mxdname = os.path.dirname(mxdpath)
            #assert (os.path.isfile(mxd)), gp.getIDMessage(89004,"InvaliMXDfilename")  
            arcpy.AddMessage("This statement reached 1")
            #arcpy.AddMessage("EXCEPTION: {0}".mxdname)
            try:
                mxd = arcpy.mapping.MapDocument(mxdpath)
                arcpy.AddMessage("This statement reached 2")
                #analysis = arcpy.mapping.AnalyzeForSD(mxd)
                #arcpy.AddMessage("This statement reached 3")
               #Iterate through the ArcMap Document layers...
                for layer in arcpy.mapping.ListLayers(mxd):
                    #print(layer.Name)
                    if layer.supports("DESCRIPTION"):
                        arcpy.AddMessage("This statement reached 3".format(layer))
                        layerattributes = [layer.description, layer.description]
                        #Write the attributes to the csv file...
                        spamwriter.writerow(layerattributes)
                #del mxd
            except Exception as e:
                arcpy.AddMessage("EXCEPTION: {0}".format(e))
         #del mxd
  #close the csv file to save it...
    #spamwriter.close()
#If no ArcMap Documents are in the list, then notify via an error message...
else:
    arcpy.AddError("No ArcMap Documents found. Please check your input \
    variables.")
