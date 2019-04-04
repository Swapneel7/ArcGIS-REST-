#create a new sde connection

#List all featureclasses in a geodatabase, including any within feature datasets

import arcpy,os

from arcpy import env

arcpy.env.overwriteOutput = True

#arcpy.CreateDatabaseConnection_management(out_folder_path=".",
#                                          out_name="GIS winauth to gis-server.sde",
#                                          server="https://arc03.cc.vt.edu:6443/arcgis/admin/",
#                                          database_platform="POSTGRESQL",#Need to check this setting
#                                          instance="Oracle",
#                                          account_authentication="DATABASE_AUTH",#Not sure if its supported DBMS
#                                          username="svekhand_adm",
#                                          password="22a2626790c5f2004e4eb33d12a9d18a76df2f61",
#                                          database="gisdb",
#                                          version="sde")
#
#                                          
arcpy.CreateArcSDEConnectionFile_management(out_folder_path=r"C:\\Users\\svekhand\\Documents\\ArcGIS\\",
                                            out_name="mypostgres.sde",
                                            server="ARC03",
                                            #servicename= "SampleWorldCities"
                                            database="POSTGRESQL",#Need to check this setting
                                            account_authentication="DATABASE_AUTH",
                                            username="svekhand_adm",
                                            password="Kox8K+6}^=zPdCRS",
                                            save_username_password="SAVE_USERNAME",
                                            version="SDE.DEFAULT")