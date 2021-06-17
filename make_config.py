import json

from TTS.config import load_config

CONFIG = load_config('TTS/tts/configs/config.json')
CONFIG['datasets'][0]['path'] = '/media/mint/Barracuda/Datasets/LJSpeech-1.1/'  # set the target dataset to the LJSpeech
CONFIG['audio']['stats_path'] = None  # do not use mean and variance stats to normalizat spectrograms. Mean and variance stats need to be computed separately. 
CONFIG['output_path'] = './out'
with open('config.json', 'w') as fp:
    json.dump(CONFIG, fp)

