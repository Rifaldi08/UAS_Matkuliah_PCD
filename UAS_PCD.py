import cv2
import easyocr
import matplotlib.pyplot as plt

# Baca gambar
image_path = 'aeroc5.jpeg'  # Ganti dengan nama file kamu
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Jalankan OCR
reader = easyocr.Reader(['en'])
results = reader.readtext(gray)

# Tampilkan hasil
for (bbox, text, prob) in results:
    print(f"Teks Terdeteksi: {text} (Probabilitas: {prob:.2f})")
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(image, text, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

# Tampilkan gambar hasil deteksi
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()