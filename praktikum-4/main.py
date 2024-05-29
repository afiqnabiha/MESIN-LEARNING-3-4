import pandas as pd
import numpy as np
print("\n")

path = "./dataset/BL-Flickr-Images-Book.csv"
df = pd.read_csv(path)
arr = np.array(df)

print(df.loc[206].to_string())
print()
# print row 0 to 10th, col-1 to col -3
# print(df.loc[:9, ["Identifier", "Edition Statement", "Place of Publication"]])

# get 4th to 10th row 
# sample = df.loc[4:10, ["Edition Statement", "Place of Publication"]]
# print(f"\n {sample.to_string()}")
# with open("./file.txt", "w") as f:
#     f.write(sample.to_string())

# get df data type
print(f"\n{df.dtypes}")

# print 5 baris pertama
print(f"\n {df.head()}")

# membuat data frame baru dengan kolom yang sudah di filter
exclude_cols = ['Edition Statement', 
           'Corporate Author', 
           'Corporate Contributors', 
           'Former owner', 
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']

new_df = df.loc[:, [col for col in df.columns.values.tolist() if col not in exclude_cols]]
# tulis ke file biar mudah dibaca
# with open("./newdf.txt", "w", encoding="utf-8") as f:
#     f.write(new_df.iloc[:4].to_string())

# mengganti id menjadi kolom 'Identifier'
new_df = new_df.set_index('Identifier')
print("\n", new_df.head())

# merapikan format tgl publikasi
tgl_baru = new_df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
new_df['Date of Publication'] = pd.to_numeric(tgl_baru)
# with open("./newdate.txt", "w", encoding="utf-8") as f:
    # f.write(new_df.iloc[:14].to_string())

# merapikan format tempat publikasi
place = new_df['Place of Publication']
print(f'type of place: {type(place)}')
# with open("./place.txt", "w", encoding="utf-8") as f:
#     f.write(place.iloc[:14].to_string())
    
london = place.str.contains('London')
print(f'type of london: {type(london)}')
oxford = place.str.contains('Oxford')
nyc = place.str.contains('New York')

new_df['Place of Publication'] = np.where(
                                            london, 
                                            'London',
                                            np.where(
                                                        oxford, 
                                                        'Oxford', 
                                                        place.str.replace('-', ' ')
                                                    )
                                        )

print(f"\n {new_df.head()}")
print(f'type of df:\n {new_df.dtypes}')
print(f"publisher: \n{new_df['Publisher'].tolist()[:10]}")
print(f'\ndataset length: {len( new_df.index )}')
print(f'nan count: \n{new_df.isna().sum()}\n')

# drop rows with na
new_df = new_df.dropna(axis=0, how="any")
print(f'\ndataset length after rows dropped: {len(new_df)}')
print(f'nan after dropped: \n{new_df.isna().sum()}\n')
# print header
print(f'\n sample:\n {new_df.head()}')

new_df.to_csv("clean.csv", index=False)

print()