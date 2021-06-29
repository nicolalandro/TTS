# train for ita voice
Ita dataset for TTS:
* [Mozilla Common voice](https://commonvoice.mozilla.org/)
* [The M-AILABS Speech Dataset](https://www.caito.de/2019/01/the-m-ailabs-speech-dataset/)

## Train Guide for TTS model
* Train tacotron2 from common voice, select voice with more data

```
# download common voice
python commonvoice/analysis.py
# head -n 1600 voice_best.csv > voice_best_train.csv
# tail -n 129 voice_best.csv > voice_best_val.csv
python commonvoice/create_wavs.py
python TTS/bin/compute_statistics.py config_commonvoice_tactoron2.json scale_stats_common.npy --data_path media/mint/Barracuda/Datasets/CommonVoiceMozillaIta/cv-corpus-6.1-2020-12-11/it/wavs
CUDA_VISIBLE_DEVICES="0" python TTS/bin/train_tacotron.py --config_path config_commonvoice_tactoron2.json | tee training.log
# or start fine train from another model
CUDA_VISIBLE_DEVICES="0" python TTS/bin/train_tacotron.py --config_path config_commonvoice_tactoron2.json --restore_path out_commonvoice/commonvoice_best-June-17-2021_10+16PM-1e2713f7/best_model.pth.tar | tee training.log 
```

* Train GlowTTS on the same data

```
CUDA_VISIBLE_DEVICES="0" python TTS/bin/train_glow_tts.py --config_path config_commonvoice_glow_tts.json | tee training.log
```

## Train Guide for Vocoder
TODO

## Run server and use trained model
```
tts-server --model_path out_commonvoice/commonvoice_best-June-17-2021_10+16PM-1e2713f7/best_model.pth.tar --config_path config_commonvoice.json
firefox localhost:5002
```
