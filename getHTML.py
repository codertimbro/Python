    Gets HTML of a Web Page
    Python 3.6
    Tim Brown
    
    from requests_html import HTMLSession 
    r=session.get('<webpage>') #Goes out retrieves the web page 
    p=r.html.html               #Pulls HTML code
    
    Notes: It does not work for DOM COM and certificaiton sites. DOM COM sites you will need a timer to the code for the page to load or use render command.
    Certification sites you will need to include the code of 
