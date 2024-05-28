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

export CUDA_VISIBLE_DEVICES=7

python -m train wandb=null experiment=hg38/akita_benchmark \
train.pretrained_model_path=/mnt/gemini/data2/zhenqiaosong/HyenaDNA/models/checkpoints/val/loss.ckpt \
train.test=True