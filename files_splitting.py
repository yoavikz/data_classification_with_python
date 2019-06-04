print("Targil junior DS")
read_file=open("TrainDataset.csv",'r')
val_file=open("TrainValidation400.csv",'w')
new_train_file=open("Train_1000.csv",'w')
cnt=0
cnt_val=0
for line in (read_file):
    if cnt==0:
        val_file.write(line)
        new_train_file.write(line)
    elif cnt%3==0:
        if cnt_val<400:
            val_file.write(line)
            cnt_val+=1
        else:
            new_train_file.write(line)
    else:
        new_train_file.write(line)
    cnt+=1
        
read_file.close()
val_file.close()
new_train_file.close()
print("finished")
