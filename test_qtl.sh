#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=32GB
#SBATCH --error=err.txt
#SBATCH --output=train.txt
#SBATCH --partition=taurus
#SBATCH --gres=gpu:1
#SBATCH --time=7-0:0:0
#SBATCH --account=zhenqiaosong
#SBATCH --mail-type=fail
#SBATCH --mail-user=zhenqiao@ucsb.edu

export CUDA_VISIBLE_DEVICES=6

python -m train wandb=null experiment=hg38/enformer_benchmark \
train.pretrained_model_path=/mnt/taurus/data2/zhenqiaosong/HyenaDNA/enformer_QTL/checkpoints/val/loss.ckpt \
train.test=True