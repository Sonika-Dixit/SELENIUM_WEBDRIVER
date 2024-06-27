

l=['a','e','i','o','u']
with open('vowel_files.txt','r') as f:
    total_file_content=f.readlines()
    for i in total_file_content:
        print(i)
        for j in i:
            # print(j)
            if j in l:
                print(j)
                
                
        
