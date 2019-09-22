Write to a File
Python 3.6
Tim Brown

 with open('drive/folder/out.txt', 'w',encode='utf-8') as f:                       # This is for char 
 with open('drive/folder/out.txt', 'wb') as f:                                     # This is for bytes, int, float 
 for link in job:                                                                  # For iteration
 jobs= link.text + '\n'                                                            # Adds new line and concat function 
 f.write(jobs)                                                                     # This writes to file 
 
