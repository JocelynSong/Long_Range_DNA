import os 
import sys
import random
import torch
import torch.nn.functional as F

chr_list = ["chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10",
            "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19", "chr20",
            "chr21", "chr22", "chrX", "chrY"]


def extract_data_split(input_file, output_file):
    lines = open(input_file).readlines()
    data_dict = {"train": [], "valid": [], "test": []}
    for line in lines:
        items = line.strip().split()
        if items[0].strip() in chr_list:
            if items[0].strip() in ["chrX", "chrY"]:
                split = random.choice(["valid", "test"])
            else:
                split = "train"
            sample = items[: 3]
            if items[3].startswith("NM"):
                sample.extend("0")
            else:
                sample.extend("1")
            this_line = "\t".join(sample)
            data_dict[split].append(this_line)
    print(len(data_dict["train"]))
    print(len(data_dict["valid"]))
    print(len(data_dict["test"]))
    length = len(data_dict["train"]) + len(data_dict["valid"]) + len(data_dict["test"])
    sample_len = int(0.05 * length)
    train_samples = data_dict["train"]
    valid_samples = data_dict["valid"]
    test_samples = data_dict["test"]
    random.shuffle(train_samples)
    valid_len = sample_len - len(data_dict["valid"])
    test_len = sample_len - len(data_dict["test"])
    valid_samples.extend(train_samples[: valid_len])
    test_samples.extend(train_samples[valid_len: (valid_len + test_len)])
    train_samples = train_samples[valid_len + test_len: ]
    fw = open(output_file, "w", encoding="utf-8")
    for sample in train_samples:
        line = sample + "\t" + "train"
        fw.write(line + "\n")
    for sample in valid_samples:
        line = sample + "\t" + "valid"
        fw.write(line + "\n")
    for sample in valid_samples:
        line = sample + "\t" + "test"
        fw.write(line + "\n")
    fw.close()



if __name__ == "__main__":
    logits = torch.LongTensor([[0,1,0,0], [1,0,0,0]])
    a = F.gumbel_softmax(logits, tau=1, hard=False)
    print(a)
    exit(0)
    data_path = "/mnt/data2/zhenqiaosong/HyenaDNA/data"
    input_file = os.path.join(data_path, "hg38_refGene.bed")
    output_file = os.path.join(data_path, "hg38.human.bed")
    extract_data_split(input_file, output_file)
