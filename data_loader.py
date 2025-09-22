import pandas as pd

# ID файла из ссылки
FILE_ID = "1tVFE3QrIMjPSVgiUF9jjUAywJhZIw3Vl"

# прямой URL для скачивания CSV
file_url = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

# читаем данные с пропуском строк с ошибками
raw_data = pd.read_csv(file_url)

# выводим первые 10 строк для проверки
print(raw_data.head(10))
