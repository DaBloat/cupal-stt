from glob import glob
import os
import pandas as pd

# Checking the File
if 'data-open-voice' not in os.listdir():
    os.system("mkdir data-open-voice")
    os.system("mkdir data-open-voice/voices")
    os.system("mkdir data-open-voice/annotations")
else:
    print('file "data-open-voice" Already exists')

# Validation Paths
for main in glob('cv-corpus-*'):
    print(f"{main}:")
    print(f"    Total Records: {len(os.listdir(f'{main}/clips'))}")
    df = pd.read_csv(f'{main}/validated.tsv', sep='\t')
    print(f"    Validated Records: {len(df['path'].to_list())}")
    for file in df['path'].to_list():
        os.system(f'cp {main}/clips/{file} data-open-voice/voices/')
    os.system(f'cp {main}/validated.tsv data-open-voice/annotations/validated-{len(df['path'].to_list())}.tsv')
    
# Compile annotations
df = pd.DataFrame()
for annot in glob('data-open-voice/annotations/*'):
    an = pd.read_csv(annot, sep='\t')
    an = an[['path', 'sentence']]
    df = pd.concat([df, an])
    os.system(f'rm {annot}')
df['path'] = df['path'].apply(lambda x: f'data-open-voice/voices/{x}')
df.to_csv('data-open-voice/annotations/data.csv', index=False)