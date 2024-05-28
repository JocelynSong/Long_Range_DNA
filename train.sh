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

python -m train ++model.checkpoint_mixer=True ++model.checkpoint_mlp=True wandb=null \
experiment=hg38/hg38_hyena \
train.pretrained_model_path=/mnt/data2/zhenqiaosong/HyenaDNA/pretrained_models/weights.ckpt \
callbacks.model_checkpoint.every_n_train_steps=3000 \
model.n_layer=8 \
model.d_model=256 \
dataset.batch_size=1 \
train.global_batch_size=1 \
dataset.max_length=450000 \
optimizer.lr=6e-4 \
trainer.devices=1

#