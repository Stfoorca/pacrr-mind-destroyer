import os
import shutil
new_dir = '/home/pepe/Desktop/paccr-master/cosine/topic_doc_mat'
old_dir = '/home/pepe/Desktop/paccr-master/cosine/topic_doc_mat_kurwa'

#wchodzę w folder
    #biorę kolejne pliki
        #biorę nazwę pliku 01.py
        #przenoszę go do folderu 01.py
        #zmieniam jego nazwę na nazwę rodzica.py
        #przechodzę na kolejny plik
    #przechodzę na kolejny folder
print('STARTUJE!!!!')
#for dir in os.listdir(topic_dir):    
#    for file_dir in os.listdir(topic_dir + '/' + dir):
#        parentName = os.path.basename(dir)
#        prevName = os.path.basename(file_dir)
#        prevName=prevName[:-4]
#        print('{} {}'.format(parentName, prevName))
#        os.rename(topic_dir + '/' + parentName + '/' + file_dir, new_topic_dir +'/' + prevName + '/' + parentName + '.npy')



# os.mkdir(new_dir)

# for i in range(1, 16):
#     os.mkdir('{}/{}'.format(new_dir, i))

for direstory in os.listdir(old_dir):
    print('{}/{}'.format(old_dir, direstory))
    assert 1 == 0
    for fileN in os.listdir('{}/{}'.format(old_dir, direstory)):
        print(fileN)
        
        #shutil.copy("{}/{}/{}".format(old_dir, direstory ,file), "{}/{}/{}".format(new_dir, file[:-4], direstory))

# for direstory in os.listdir(topic_dir):
#     for file in os.listdir('{}/{}'.format(topic_dir, direstory)):
#         shutil.copy("{}/{}/{}".format(topic_dir, direstory ,file), "{}/{}/{}".format(new_topic_dir, file[:-4], direstory))

print('skonczylem :)')