# Train
guide: https://tts.readthedocs.io/en/latest/tutorial_for_nervous_beginners.html

## Create stats file
```
python TTS/bin/compute_statistics.py MyFileAndConfig/config_maillabs_tacotron2.json scale_stats_maillabs.npy --data_path /media/mint/Barracuda/Datasets/MAIL_LABS_TTS/riccardo_fasol/wavs
```

## train vocoder
```
python TTS/bin/train_vocoder_gan.py --config_path MyFileAndConfig/config_maillabs_melgan.json
```

## train tts
```
python TTS/bin/train_tts.py --config_path MyFileAndConfig/config_maillabs_other.json
```

## run server
```
tts-server --model_path  out_maillabs/maillabs_best-June-30-2021_08+17AM-12c3cb9d/checkpoint_20000.pth.tar \
           --config_path MyFileAndConfig/config_maillabs_tacotron2.json \
           --vocoder_path out_maillabs/melgan-fasol-August-11-2021_09+55AM-12c3cb9d/checkpoint_30000.pth.tar \
           --vocoder_config_path MyFileAndConfig/config_maillabs_melgan.json
```
