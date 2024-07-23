import os
import django
from django.core.files import File
from news.models import Category, News, User
from django.contrib.auth.hashers import make_password

# Django ayarlarını yükleyin
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bugun_ne_oldu.settings')
django.setup()

def load_dummy_data():
    # Kategorileri ekleyin

    agenda_category, created = Category.objects.get_or_create(
        id=1,
        defaults={'name': 'Gündem', 'description': 'Gündemle ilgili tüm haberler'}
    )
    tech_category, created = Category.objects.get_or_create(
        id=2,
        defaults={'name': 'Ekonomi', 'description': 'Ekonomi için tüm haberler'}
    )

    # Haberleri ekleyin
    news1, created = News.objects.get_or_create(
        id=1,
        defaults={
            'title': "İstanbul'da sıcaklıklar artmaya devam ediyor",
            'summary': "İstanbul'da, gece boyunca etkili olan sıcak hava ve yüksek nem oranı ilçelere göre değişirken, Ataşehir ve Ümraniye'de nem oranı yüzde 100'ü bularak rekor kırdı. Megakentte genel hava sıcaklığı sabahın ilk saatleri itibarıyla 26,7, hissedilen sıcaklık 30,3 derece ve nem oranı yüzde 85'i buldu",
            'content': "Detailed content about tech trends.",
            'category': tech_category,
            'publication_date': "2024-07-19T10:00:00Z"
        }
    )

   
    if created:
        with open('C:\\Users\\Eness\\Desktop\\bugun_ne_oldu\\news\\images\\istanbul.jpg', 'rb') as img_file:
            news1.image.save('istanbul.jpg', File(img_file), save=True)



    news2, created = News.objects.get_or_create(
        id=2,
        defaults={
            'title': "Etna Yanardağı'nda büyük patlama: Volkanik hareketlilik devam ediyor",
            'summary': "İtalya'nın Sicilya Adası'ndaki 3 bin 300 metre civarında yüksekliğe sahip olan Etna Yanardağı'nda son haftalarda devam eden volkanik hareketlilik dikkat çekiyor. Volkanik patlama sonucunda oluşan kül ve lav havadan görüntülendi",
            'content': "Detailed content about sports.",
            'category': agenda_category,
            'publication_date': "2024-07-18T11:00:00Z"
        }
    )

   
    if created:
        with open('C:/Users/Eness/Pictures/news_image_2.jpg', 'rb') as img_file:  # Gerçek dosya yolunu buraya girin
            news2.image.save('news_image_2.jpg', File(img_file), save=True)


    # Kullanıcıları ekleyin
    user1, created = User.objects.get_or_create(
        id=1,
        defaults={
            'name': "John Doe",
            'email': "john.doe@example.com",
            'password': make_password("password123"),
            'created_at': "2024-07-18T12:00:00Z"
        }
    )

    user2, created = User.objects.get_or_create(
        id=2,
        defaults={
            'name': "Jane Smith",
            'email': "jane.smith@example.com",
            'password': make_password("password456"),
            'created_at': "2024-07-18T13:00:00Z"
        }
    )

    print("Dummy veriler başarıyla yüklendi.")

if __name__ == '__main__':
    load_dummy_data()
