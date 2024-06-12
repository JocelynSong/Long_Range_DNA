#!/bin/bash

python -m evaluate wandb=null experiment=hg38/enhancer_promoter_benchmark \
train.pretrained_model_path=enhancer_promoter/checkpoints/val/loss.ckpt \
train.test=True