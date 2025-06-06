import os
import pandas as pd
import requests
from tqdm import tqdm

# Parameters
csv_path = "../Datos/books.csv"        # path to your dataset
url_column = "image_url"                # column name containing the image URLs
output_folder = "../Datos/book_covers"           # folder to store downloaded images

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read the dataset
df = pd.read_csv(csv_path)

# create a book index mapping
idx2bookid = {i: id_ for i, id_ in enumerate(df.book_id)}
bookid2idx = {id_:i for i, id_ in enumerate(df.book_id)}

# Download images
for idx, url in tqdm(enumerate(df[url_column]), total=len(df), desc="Downloading images"):
    # si queremos guardar las imagenes con el idx del libro
    #idx = bookid2idx[df.book_id[idx]['book_id']] # Use the index from the mapping
    try:
        if isinstance(url, str) and url.startswith("http"):
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                ext = url.split('.')[-1].split('?')[0]  # handle .jpg or .jpg?param
                image_path = os.path.join(output_folder, f"book_{idx}.{ext}")
                with open(image_path, 'wb') as f:
                    f.write(response.content)
    except Exception as e:
        print(f"Failed to download image at index {idx}: {e}")
