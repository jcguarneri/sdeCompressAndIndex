import arcpy

#compress the geodatabase
arcpy.Compress_management("C:\Users\GeoNexusAdmin\AppData\Roaming\ESRI\Desktop10.4\ArcCatalog\Connection to asteroid.sde")

try:
    
    #collect information on compress messages for log file
    cMessage = arcpy.GetMessages()
    cMessageCount = arcpy.GetMessageCount()
       
    #open log file and write compress message information
    logFile = open(r'C:\Users\GeoNexusAdmin\Desktop\compressLog.txt', 'wb')
    logFile.write('End Message:%s\nNumber of messages: %s'%(cMessage,cMessageCount)
                  
                  
    # set the workspace 
    arcpy.env.workspace = r"C:\Users\GeoNexusAdmin\AppData\Roaming\ESRI\Desktop10.4\ArcCatalog\Connection to asteroid.sde"
    workspace = arcpy.env.workspace
                  
    # Rebuild indexes and analyze the states and states_lineages system tables
    arcpy.RebuildIndexes_management(workspace, "SYSTEM", "ALL")

    arcpy.AnalyzeDatasets_management(workspace, "SYSTEM", "ANALYZE_BASE", "ANALYZE_DELTA", "ANALYZE_ARCHIVE")
    
    #write success confirmation to log file and save              
    logFile.write("\nSuccess!")
    logFile.close()             
                  
except:
    
    #collect messages from last run tool              
    messageText = arcpy.GetMessages()
    
    #open log file and write the messages and failure notice
    logFile = open(r'C:\Users\GeoNexusAdmin\Desktop\compressLog.txt', 'wb')
    logFile.write("Index failed")
    logFile.write(messageText)
    logFile.close()              
        

