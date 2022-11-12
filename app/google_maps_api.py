import googlemaps

MAPS_API_KEY = 'AIzaSyDax7Rvk6BJ7Yum-JeFHbY6D5uMJ9c9ymc'

def geocode(address):
   try:
       gmaps = googlemaps.Client(key=MAPS_API_KEY)
       result = gmaps.geocode(address)
       lat = result[0]['geometry']['location']['lat']
       lng = result[0]['geometry']['location']['lng']

       return lat, lng
   except:
       return None, None

# 住所リストを読み込む
# 住所リストには　address というカラムが必須
filepaths = glob('address.xlsx')
filepath = filepaths[0]
df = pd.read_excel(filepath)

# 緯度経度データの取得
result = [] # 取得した緯度経度を入れておくリスト
for ad in tqdm(df['address']):
   result.append(geocode(ad))

# 取得したデータの保存
_df = pd.DataFrame(result, columns=['altitude', 'longitude'])
df = df.join(_df)
df.to_excel('address_with_altlong.xlsx', index=False)
