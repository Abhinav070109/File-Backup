import os
import dropbox

class TransferData:
    
    def __init__(self,access_token):
        self.access_token = access_token
        
    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        for root,dirs,files in os.walk(file_from):
            
            for filename in files:
                localPath = os.path.join(root, filename)
                
                relative_path = os.path.relpath(localPath,file_from)
                dropBoxPath = os.path.join(file_to, relative_path)
                
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropBoxPath, mode=WriteMode('overwrite'))
                    
def main():
    access_token = 'es34yUQawTQAAAAAAAAAAfR3_py_bBIx0qCD4O5WDkZSLOoIBkR1-WA8HHTnG6Bl'
    transferData = TransferData(access_token)
    
    
    file_from = input("Enter the folder path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")
    
    transferData.upload_files(file_from,file_to)
    print('File Backed Up!!!')
    
main()