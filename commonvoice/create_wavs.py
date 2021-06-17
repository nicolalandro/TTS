from os import path
from pydub import AudioSegment
import pandas as pd

df = pd.read_csv('/media/mint/Barracuda/Datasets/CommonVoiceMozillaIta/cv-corpus-6.1-2020-12-11/it/train.tsv', sep='\t')
by_id = df.groupby(['client_id'])['client_id'].count().nlargest(3)
selected_id = by_id.index[0]
best_voice = df[df['client_id']==selected_id]

base_path = '/media/mint/Barracuda/Datasets/CommonVoiceMozillaIta/cv-corpus-6.1-2020-12-11/it/clips'
out_base_path  = '/media/mint/Barracuda/Datasets/CommonVoiceMozillaIta/cv-corpus-6.1-2020-12-11/it/wavs'

for i, n in best_voice['path'].iteritems():
    src = path.join(base_path, n + '.mp3')
    dst = path.join(out_base_path, n + '.wav')
    print(n)
    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")