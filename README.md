# Blurla

Fotoğraf yükle, yüzleri otomatik bulanıklaştırılmış halini geri al. Python, Flask ve OpenCV ile yapılmış küçük bir web uygulaması.

<!-- Buraya ekran görüntüsü ekleyebilirsin: ![Ekran görüntüsü](screenshot.png) -->

## Özellikler

- Tarayıcıdan fotoğraf yükleme ve önizleme
- Fotoğraftaki yüzleri otomatik tespit etme (OpenCV Haar Cascade)
- Her yüze boyutuna göre ayarlanan Gaussian blur uygulama
- Fotoğraflar diske kaydedilmez, sadece bellekte işlenir

## Kurulum

Python 3.9 veya üstü gerekir.

```bash
git clone https://github.com/mkeremeroglu/blurla.git
cd blurla
pip install -r requirements.txt
```

## Çalıştırma

```bash
python app.py
```

Ardından tarayıcıdan [http://127.0.0.1:5000](http://127.0.0.1:5000) adresini aç, bir fotoğraf seç ve **Blur At** butonuna bas.

## Proje yapısı

```
blurla/
├── app.py              # Flask uygulaması ve yüz blurlama kodu
├── requirements.txt
└── templates/
    └── index.html      # Yükleme sayfası
```

## Önemli not: OpenCV sürümü

Bu proje **OpenCV 4.x** ile çalışır. OpenCV 5.x sürümünde `CascadeClassifier` sınıfı kaldırıldığı için `requirements.txt` içinde `opencv-python<5` olarak sabitlenmiştir. Şu hatayı alırsan sürümün 5.x'e yükselmiş demektir:

```
AttributeError: module 'cv2' has no attribute 'CascadeClassifier'
```

Çözüm:

```bash
pip uninstall opencv-python -y
pip install "opencv-python<5"
```

## Sınırlamalar

- Haar Cascade, yandan bakan, eğik veya çok küçük yüzleri kaçırabilir. Bulunamayan yüzler bulanıklaştırılmaz, bu yüzden gizlilik amaçlı kullanımda sonucu kontrol et.
- Yükleme boyutu 10 MB ile sınırlıdır (`MAX_CONTENT_LENGTH` ile değiştirilebilir).

## Yapılacaklar

- [ ] Sonucu sayfada önce/sonra olarak gösterme
- [ ] İndirme butonu
- [ ] Blur şiddeti seçimi
- [ ] Pikselleştirme (mozaik) seçeneği
- [ ] Daha doğru yüz tespiti için DNN veya MediaPipe desteği
