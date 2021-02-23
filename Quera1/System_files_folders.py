
import  os,sys,pprint
import glob

def combet(Sallib_format,Sajjand_format,path):
    def most_frequent(list):
        rapid_file=  max(set(list), key=list.count)
        return list.count(rapid_file) , rapid_file
    
    cheat_name = ''
    file_type = [] 
    files = []
    results = []

    msg1="Win normally!"
    msg2 = "Win you can win if you cheat on " 
    msg3 = 'Lose! you cant win this game '
    
    file_type.append(Sallib_format)
    file_type.append(Sajjand_format)
    
    print("Salib select : ",Sallib_format)
    print("Sajjad select: ", Sajjand_format)
    
    
    
    for type in file_type:
        count = len(glob.glob1(path,"*."+type))
        results.append (count)
        # print("Count of ", type,'files are : ',count)
        

    for r,d,f in os.walk(path):
        for file in f :
            files.append(file)
    
    
    counter,cheat_name,  = most_frequent(files)

    if   results[1] > results[0]:
        print(msg1) 
    elif  results[1]+ int(counter) > results[0] :
        print(msg2 + cheat_name)
    else:
        print(msg3)
        
    

path = "/home/hamid/Documents"
combet("pdf", "py", path)
