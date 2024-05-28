import numpy as np
from sklearn.metrics import roc_auc_score

preds, targets = [], []
lines = open("/mnt/gemini/data2/zhenqiaosong/HyenaDNA/models/output/result_qtl_mouse.txt").readlines()
for line in lines:
    items = line.strip().split()
    preds.append(float(items[0]))
    targets.append(float(items[1]))

print(roc_auc_score(targets, preds))