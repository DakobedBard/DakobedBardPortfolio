import subprocess
import sys

if __name__ == '__main__':
    subprocess.run('bash -c "source activate /home/mddarr/data/anaconda3/envs/kerasenv/ && python3 train_guitarset_model.py " ', shell=True)
