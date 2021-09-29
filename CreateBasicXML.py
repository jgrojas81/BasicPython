def Basicxml ():                                                        #create funcion Basicxml
    xml_content = ""                                                    #create variable xml_content
    xml_content += "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"         #add content to variable 
    xml_content += "\n<note>"
    xml_content += "\n   <to>Tove</to>"
    xml_content += "\n   <from>Jani</from>"
    xml_content += "\n   <heading>Reminder</heading>"
    xml_content += "\n   <body>Wake up 7:00 am on Saturday!</body>"
    xml_content += "\n</note>"
    return xml_content                  

print( Basicxml() )