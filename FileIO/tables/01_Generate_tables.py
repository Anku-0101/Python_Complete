
for i in range(2, 21):
    f_name = 'tableOf_' + str(i) +'.txt'
    file_ = open(f_name, 'w')
        
    for j in range(1, 11):
        val = str(i) + ' X ' + str(j) + ' = ' + str(i*j) + '\n'
        file_.write(val)
    
    file_.close()