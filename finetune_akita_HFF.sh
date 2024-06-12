#!/bin/bash

#
#export CUDA_VISIBLE_DEVICES=7
#export HYDRA_FULL_ERROR=1

python -m train wandb=null experiment=hg38/akita_benchmark \
train.pretrained_model_path=pretrained_models/weights.ckpt \
dataset.batch_size=1
