from googlesearch import search

f = open("searchfile.txt", "r")

for x in f: 
    query = 'url:scribd ' + x
    my_results_list = []

    for i in search(query,        
                    num = 10,     
                    start = 0,    
                    stop = None,  
                    pause = 2.0,  
                ):  
        
        my_results_list.append(i)
        outF = open("log.txt", "a")
        outF.write(i)
        outF.write("\n")
        print(i)

