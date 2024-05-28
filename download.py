from boxsdk import OAuth2

client_id = "33605211995"
client_secret = ""
access_token = ""

oauth = OAuth2(client_id=client_id, client_secret=client_secret, access_token=access_token)
client = Client(oauth)

folder_id = "262082723696"
fold_path = "/mnt/taurus/data2/zhenqiaosong/HyenaDNA/data_long_range_dna"
folder = client.folder(folder_id=folder_id).get()

for item in folder.get_items():
    if isinstance(item, File):
        item.download_to(fold_path)