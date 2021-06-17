import pandas as pd

df = pd.read_csv('/media/mint/Barracuda/Datasets/CommonVoiceMozillaIta/cv-corpus-6.1-2020-12-11/it/train.tsv', sep='\t')

df.info()

by_id = df.groupby(['client_id'])['client_id'].count().nlargest(3)
print(by_id)

selected_id = by_id.index[0]
print('Selected', selected_id)

best_voice = df[df['client_id']==selected_id]
final = best_voice[['path', 'sentence']]
final['sentence2'] = final['sentence']
final['path'] = final['path'].apply(lambda x: x[:-4])
final.to_csv('/media/mint/Barracuda/Datasets/CommonVoiceMozillaIta/cv-corpus-6.1-2020-12-11/it/voice_best.csv', index=False, header=None, sep='|')

# head -n 1600 voice_best.csv > voice_best_train.csv
# tail -n 129 voice_best.csv > voice_best__val.csv