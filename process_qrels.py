import os

qrels = 'qrels'

def remove_column_qrels():
    with open(os.path.join('./', qrels), 'rt', encoding='utf-8') as f:
        for line in f:
            cols = line.split()
            if len(cols) > 1:
                yield cols[0:3] + [cols[4]]

if '__main__':
    file = open('./qrels.txt', 'w')
    for line in remove_column_qrels():
        file.write('\t '.join(line)+'\n')
    file.close()
