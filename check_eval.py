import os

qrels = 'qrels'
dikt = dict()
def check_eval():
    for i in range(1, 16):
        dikt[str(i)] = dict()
        for j in range(-1, 3):
            dikt[str(i)][str(j)] = 0
    with open(os.path.join('./', qrels), 'rt', encoding='utf-8') as f:
        for line in f:
            cols = line.split()
            dikt[str(cols[0])][str(cols[3])] += 1
    return dikt


if '__main__':
    print(check_eval())
