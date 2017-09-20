import arcpy

# Process: Compress
arcpy.Compress_management("C:\Users\GeoNexusAdmin\AppData\Roaming\ESRI\Desktop10.4\ArcCatalog\Connection to asteroid.sde")

try:
    
    cMessage = arcpy.GetMessages()
    cMessageCount = arcpy.GetMessageCount()
       
    logFile = open(r'C:\Users\GeoNexusAdmin\Desktop\compressLog.txt', 'wb')
    logFile.write('End Message:%s\nNumber of messages: %s'%(cMessage,cMessageCount)
                  
                  
    # set the workspace 
    arcpy.env.workspace = r"C:\Users\GeoNexusAdmin\AppData\Roaming\ESRI\Desktop10.4\ArcCatalog\Connection to asteroid.sde"

    # Get the user name for the workspace
    # this assumes you are using database authentication.
    # OS authentication connection files do not have a 'user' property.
    userName = arcpy.Describe(arcpy.env.workspace).connectionProperties.user

    # Get a list of all the datasets the user has access to.
    # First, get all the stand alone tables, feature classes and rasters owned by the current user.
    dataList = arcpy.ListTables('*.' + userName + '.*') + arcpy.ListFeatureClasses('*.' + userName + '.*') + arcpy.ListRasters('*.' + userName + '.*')

    # Next, for feature datasets owned by the current user
    # get all of the featureclasses and add them to the master list.
    for dataset in arcpy.ListDatasets('*.' + userName + '.*'):
        dataList += arcpy.ListFeatureClasses(feature_dataset=dataset)

    # Execute rebuild indexes and analyze datasets
    # Note: to use the "SYSTEM" option, the user must be an administrator.

    workspace = r"C:\Users\GeoNexusAdmin\AppData\Roaming\ESRI\Desktop10.4\ArcCatalog\Connection to asteroid.sde"

    arcpy.RebuildIndexes_management(workspace, "NO_SYSTEM", dataList, "ALL")

    arcpy.AnalyzeDatasets_management(workspace, "NO_SYSTEM", dataList, "ANALYZE_BASE", "ANALYZE_DELTA", "ANALYZE_ARCHIVE")
    
    logFile.write("\nSuccess!")
    logFile.close()             
                  
except:
    messageText = arcpy.GetMessages()
    logFile = open(r'C:\Users\GeoNexusAdmin\Desktop\compressLog.txt', 'wb')
    logFile.write("Index failed")
    logFile.write(messageText)
    logFile.close()              
        

