'''
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
'''

#append the existing file
wf = open('demo_file.txt','a')
wf.write("\nAnd now work with appending")
wf.close()

#using w
#open and read the file after the overwriting:
wf2 = open('demo_file.txt','w')
wf2.write("Deleted content \n new content")
wf2.close()
wf2 = open('demo_file.txt','r')
print(wf2.read())
wf2.close()