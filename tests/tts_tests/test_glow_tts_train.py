import glob
import os
import shutil

from tests import get_device_id, get_tests_output_path, run_cli
from TTS.tts.configs import GlowTTSConfig

config_path = os.path.join(get_tests_output_path(), "test_model_config.json")
output_path = os.path.join(get_tests_output_path(), "train_outputs")


config = GlowTTSConfig(
    batch_size=8,
    eval_batch_size=8,
    num_loader_workers=0,
    num_val_loader_workers=0,
    text_cleaner="english_cleaners",
    use_phonemes=True,
    phoneme_language="zh-CN",
    phoneme_cache_path="tests/data/ljspeech/phoneme_cache/",
    run_eval=True,
    test_delay_epochs=-1,
    epochs=1,
    print_step=1,
    print_eval=True,
)
config.audio.do_trim_silence = True
config.audio.trim_db = 60
config.save_json(config_path)

# train the model for one epoch
command_train = (
    f"CUDA_VISIBLE_DEVICES='{get_device_id()}' python TTS/bin/train_glow_tts.py --config_path {config_path} "
    f"--coqpit.output_path {output_path} "
    "--coqpit.datasets.0.name ljspeech "
    "--coqpit.datasets.0.meta_file_train metadata.csv "
    "--coqpit.datasets.0.meta_file_val metadata.csv "
    "--coqpit.datasets.0.path tests/data/ljspeech "
    "--coqpit.datasets.0.meta_file_attn_mask tests/data/ljspeech/metadata_attn_mask.txt"
)
run_cli(command_train)

# Find latest folder
continue_path = max(glob.glob(os.path.join(output_path, "*/")), key=os.path.getmtime)

# restore the model and continue training for one more epoch
command_train = (
    f"CUDA_VISIBLE_DEVICES='{get_device_id()}' python TTS/bin/train_glow_tts.py --continue_path {continue_path} "
)
run_cli(command_train)
shutil.rmtree(continue_path)
