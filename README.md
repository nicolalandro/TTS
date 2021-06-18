# train for ita voice
Train on Commonvoice

## Guide
```
# download common voice
python commonvoice/analysis.py
# head -n 1600 voice_best.csv > voice_best_train.csv
# tail -n 129 voice_best.csv > voice_best_val.csv
python commonvoice/create_wavs.py
python TTS/bin/compute_statistics.py config_commonvoice.json scale_stats_common.npy --data_path media/mint/Barracuda/Datasets/CommonVoiceMozillaIta/cv-corpus-6.1-2020-12-11/it/wavs
CUDA_VISIBLE_DEVICES="0" python TTS/bin/train_tacotron.py --config_path config_commonvoice.json | tee training.log
```