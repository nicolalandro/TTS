import os
import pandas as pd

base_path = '/media/mint/Barracuda/Datasets/MAIL_LABS_TTS/it_IT/by_book/male/riccardo_fasol'
out_base_path  = '/media/mint/Barracuda/Datasets/MAIL_LABS_TTS/riccardo_fasol'

wavs_output_folder = os.path.join(out_base_path, 'wavs')
os.system(f'mkdir -p {wavs_output_folder}')

csv_out = os.path.join(out_base_path, 'metadata.csv')
if os.path.exists(csv_out):
    os.system(f'rm {csv_out}')

folders = os.listdir(base_path)
for raw_f in folders:
    f = os.path.join(base_path, raw_f)
    if os.path.isdir(f):
        csv_file = os.path.join(f, 'metadata.csv')
        wav_folder = os.path.join(f, 'wavs')
        
        cp_command = f'cp -r "{wav_folder}"* "{out_base_path}"'
        print('[Copy]', cp_command)
        os.system(cp_command)

        cat_command = f'cat {csv_file} >> "{csv_out}"'
        print('[Cat]', cat_command)
        os.system(cat_command)
