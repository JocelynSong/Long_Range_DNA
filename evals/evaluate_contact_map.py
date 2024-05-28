import numpy as np
import scipy.stats

preds, targets = [], []
lines = open("/mnt/gemini/data2/zhenqiaosong/HyenaDNA/models/output/result.txt").readlines()
for line in lines:
    items = line.strip().split()
    preds.append(float(items[0]))
    targets.append(float(items[1]))

print(scipy.stats.spearmanr(preds, targets)[0])