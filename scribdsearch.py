from googlesearch import search

f = open("searchfile.txt", "r")

for x in f: 
    query = 'url:scribd ' + x
    my_results_list = []

    for i in search(query,        # The query you want to run
                    num = 10,     # Number of results per page
                    start = 0,    # First result to retrieve
                    stop = None,  # Last result to retrieve
                    pause = 2.0,  # Lapse between HTTP requests
                ):  
        
        my_results_list.append(i)
        outF = open("log.txt", "a")
        outF.write(i)
        outF.write("\n")
        print(i)

