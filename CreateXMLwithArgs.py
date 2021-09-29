def BasicxmlwithVariables(variableTo, variableFrom):                    #create funcion Basicxml with variables as additional information
    xml_content = ""                                                    
    xml_content += "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"       
    xml_content += "\n<note>"
    xml_content += "\n   <to>" + variableTo +"</to>"
    xml_content += "\n   <from>" + variableFrom +"</from>"
    xml_content += "\n   <heading>Reminder</heading>"
    xml_content += "\n   <body>Wake up 7:00 am on Saturday!</body>"
    xml_content += "\n</note>"
    return xml_content                  

toFile = BasicxmlwithVariables("Vivi", "Jose")

text_file = open("CreateXMLwithArgs.xml", "w")          
text_file.write(toFile)
text_file.close()