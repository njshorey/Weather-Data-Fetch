#THIS IS AN EXAMPLE OF HOW TO EXTRACT VALUES FROM RB and BA pairs in png file output

value_input = 5.02567 #value to convert to RB format

xmax = 20.125 #from json file
xmin = -20.125 #from json file
div = 255 #from json file
a = (value_input-xmin)/(xmax-xmin)

#RG values
R = (div*a)//1
G = (div*a-R)*div//1
print("R:{0}, G:{1}".format(int(R),int(G)))

#extract
value_extracted = R*(xmax-xmin)/div + G*(xmax-xmin)/(div*div) + xmin
print("Orig:{0}, Extracted:{1}, Error:{2}%".format(value_input,round(value_extracted,5),round((value_extracted-value_input)/value_input,5)))