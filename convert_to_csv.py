import os
import csv

# Kinetics-Dataset'teki val klasörünün yolu
train_directory = "/home/pc-3972/GSS/seyma2/VideoMamba/videomamba/video_sm/datasets/train"

# Etiketlerin bulunduğu dosyanın yolu (labels.txt)
labels_file = "/home/pc-3972/GSS/seyma2/VideoMamba/names.txt"

# Etiketleri dosyadan oku ve sayısal karşılıklarını oluştur
with open(labels_file, 'r') as file:
    labels = [line.strip() for line in file.readlines()]

# Etiketlerin sayısal karşılıklarını oluştur
label_dict = {label: idx for idx, label in enumerate(labels)}

# CSV dosyasını oluşturmak için dosya adı
csv_filename = "/home/pc-3972/GSS/seyma2/VideoMamba/videomamba/video_sm/datasets/train/test.csv"

# CSV dosyasını yazmak için açık
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # CSV başlıklarını yaz
    writer.writerow(["video_name", "label"])
    
    # 'train' klasöründeki tüm alt klasörleri döngüye al
    for label in os.listdir(train_directory):
        label_path = os.path.join(train_directory, label)
        
        # Eğer bu bir klasörse
        if os.path.isdir(label_path):
            # Klasördeki videoları al
            for video_file in os.listdir(label_path):
                # Videonun adı 'resized_' ile başlıyorsa
                if video_file.endswith(".mp4"):
                    # Yalnızca video adını al, yol yerine
                    video_path = os.path.join(label_path, video_file)
                    # Etiketin sayısal karşılığını CSV'ye yaz
                    writer.writerow([video_path, label_dict[label]])

print(f"CSV dosyası {csv_filename} başarıyla oluşturuldu.")

# import os

# # Kinetics-Dataset'teki val klasörünün yolu
# train_directory = "/home/pc-3972/GSS/seyma2/TimeSformer/timesformer/datasets/kinetics-dataset/val"

# # Etiketlerin bulunduğu dosyanın yolu (labels.txt)
# labels_file = "/home/pc-3972/GSS/seyma2/TimeSformer/names.txt"

# # Etiketleri dosyadan oku ve sayısal karşılıklarını oluştur
# with open(labels_file, 'r') as file:
#     labels = [line.strip() for line in file.readlines()]

# # Etiketlerin sayısal karşılıklarını oluştur
# label_dict = {label: idx for idx, label in enumerate(labels)}

# # CSV dosyasını oluşturmak için dosya adı
# csv_filename = "val.csv"

# # CSV dosyasını boşlukla ayırarak yazma işlemi
# with open(csv_filename, mode="w") as file:
#     # Başlık satırını yaz
#     file.write("video_name label\n")
    
#     # 'train' klasöründeki tüm alt klasörleri döngüye al
#     for label in os.listdir(train_directory):
#         label_path = os.path.join(train_directory, label)
        
#         # Eğer bu bir klasörse
#         if os.path.isdir(label_path):
#             # Klasördeki videoları al
#             for video_file in os.listdir(label_path):
#                 # Videonun adı 'resized_' ile başlıyorsa
#                 if video_file.startswith("resized_") and video_file.endswith(".mp4"):
#                     # Yalnızca video adını al, yol yerine
#                     video_path = os.path.join(label_path, video_file)
#                     # Etiketin sayısal karşılığını ve video yolunu boşlukla ayırarak yaz
#                     file.write(f"{video_path} {label_dict[label]}\n")

# print(f"CSV dosyası {csv_filename} başarıyla oluşturuldu.")
