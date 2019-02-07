import json
from flask import Flask, request ,render_template
import subprocess

"""                                                                             
Clones repo, runs all tests as specified in ci.sh.                              
                                                                                
Input:                                                                          
    json_str - json formatted string of the pull request event payload                  
                                                                                
Output:                                                                         
    0 if all tests succeeded                                                    
    1 if compilation/static syntax check succeeds but tests fail                
    2 if compilation/static syntax check fails                                  
"""                                                                             
def repo_test(json_str):                                                        
    # get important stuff                                                       
    # payload = json.loads(json_str)                                              
    payload = json_str
    branch_name = payload["ref"]                        
    ssh_url = payload["repository"]["ssh_url"]                
    clone_url = payload["repository"]["clone_url"]            
    repo_name = payload["repository"]["name"]                 
                                                                                
    # clone repo, switch branch, run ci.sh, remove repo                         
    subprocess.run(["git", "clone", clone_url])                                 
    subprocess.run(["git", "-C", repo_name, "checkout", branch_name])           
    exit_code = subprocess.run(["sh", repo_name + "/ci.sh"]).returncode         
    subprocess.run(["rm", "-rf", repo_name])                                    
                                                                                
    return exit_code
