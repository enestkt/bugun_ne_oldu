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
    categories = [
        {"id": 1, "name": "Gündem", "description": "Gündemle ilgili tüm haberler"},
        {"id": 2, "name": "Ekonomi", "description": "Ekonomi ile ilgili tüm haberler"},
        {"id": 3, "name": "Spor", "description": "Sporla ilgili tüm haberler"},
        {"id": 4, "name": "Magazin", "description": "Magazin ile ilgili tüm haberler"},
        {"id": 5, "name": "Dünya", "description": "Dünya ile ilgili tüm haberler"},
        {"id": 6, "name": "Teknoloji", "description": "Teknoloji ile ilgili tüm haberler"},
        {"id": 7, "name": "Sağlık", "description": "Sağlık ile ilgili tüm haberler"},
    ]

    for category in categories:
        Category.objects.get_or_create(
            id=category["id"],
            defaults={
                "name": category["name"],
                "description": category["description"]
            }
        )

    # Haberleri ekleyin
    news_list = [
        {
            "id": 1,
            "title": "İstanbul'da sıcaklıklar artmaya devam ediyor",
            "summary": "İstanbul'da, gece boyunca etkili olan sıcak hava ve yüksek nem oranı ilçelere göre değişirken, Ataşehir ve Ümraniye'de nem oranı yüzde 100'ü bularak rekor kırdı. Megakentte genel hava sıcaklığı sabahın ilk saatleri itibarıyla 26,7, hissedilen sıcaklık 30,3 derece ve nem oranı yüzde 85'i buldu",
            "content": "Detailed content about tech trends.",
            "image": "C:\Users\Eness\Desktop\bugun_ne_oldu\media\news\images\istanbul.jpg",
            "category_id": 1,
            "publication_date": "2024-07-19T10:00:00Z"
        },
        {
            "id": 2,
            "title": "Etna Yanardağı'nda büyük patlama: Volkanik hareketlilik devam ediyor",
            "summary": "İtalya'nın Sicilya Adası'ndaki 3 bin 300 metre civarında yüksekliğe sahip olan Etna Yanardağı'nda son haftalarda devam eden volkanik hareketlilik dikkat çekiyor. Volkanik patlama sonucunda oluşan kül ve lav havadan görüntülendi",
            "content": "Detailed content about sports.",
            "image": "C:\Users\Eness\Desktop\bugun_ne_oldu\media\news\images\photo.jpeg",
            "category_id": 2,
            "publication_date": "2024-07-18T11:00:00Z"
        },
        {
            "id": 3,
            "title": "Lorem ipsum",
            "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in tincidunt orci. Proin risus tellus, pretium ut sem nec, mollis placerat augue. Nullam non bibendum velit, non ultrices lacus. Proin molestie faucibus dapibus. Mauris accumsan auctor arcu, ac molestie est commodo vitae. Aliquam sed condimentum justo, ut elementum diam. Fusce augue nibh, malesuada ut nisi suscipit, tincidunt tempor magna.",
            "content": "Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque fringilla, ante rhoncus scelerisque tempor, magna magna pulvinar justo, eu pretium sapien diam quis ex. Quisque eu pulvinar tellus. Duis tempus tincidunt nibh, vitae commodo neque mollis quis. Pellentesque finibus lorem eget est feugiat, eget euismod sapien blandit. Aliquam sodales neque sapien, vitae luctus purus auctor sed. Duis tellus enim, commodo auctor dapibus ac, egestas molestie odio. Ut est ipsum, dignissim quis ultricies at, dapibus ac nunc. Etiam nisi neque, aliquet bibendum dolor consectetur, feugiat convallis ligula. Vestibulum imperdiet lorem libero, in blandit tortor vulputate id. Quisque nec arcu non leo molestie convallis eu a tortor. Vivamus tristique, odio vel pretium ullamcorper, elit libero malesuada purus, convallis ultrices lacus neque nec erat. Duis a metus mollis nisi tempus ultricies. Fusce molestie hendrerit dignissim. Sed felis ligula, rhoncus at ex ut, euismod ultricies felis..",
            "image": "C:\Users\Eness\Desktop\bugun_ne_oldu\media\news\images\photo1.jpg",
            "category_id": 3,
            "publication_date": "2024-07-18T11:00:00Z"
        },
        {
            "id": 4,
            "title": "Aliquam cursus, est non ultrices bibendum, eros dolor ultricies purus",
            "summary": " Donec eu lacus at mauris egestas faucibus. Duis nec cursus justo. Etiam eget urna et nunc porttitor finibus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Mauris facilisis mollis elit vel euismod. Proin convallis felis aliquam risus egestas tempus sed quis leo. Maecenas mollis, sapien sit amet dapibus pretium, odio ante blandit tortor, at facilisis ipsum diam at odio. Nam congue sem non laoreet posuere.",
            "content": "Detailed content about Vivamus molestie justo elit, id gravida augue malesuada eu. Fusce pellentesque aliquam nisl, ut ultrices nisl bibendum eget. Donec non viverra erat. Curabitur ac lectus id neque placerat bibendum. In nec porta purus. Sed eu nulla sapien. Fusce et metus sagittis, laoreet lacus id, pulvinar quam. Pellentesque fermentum vitae ligula nec sodales. Integer egestas efficitur arcu et tincidunt. Nunc tristique laoreet arcu in hendrerit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "C:\Users\Eness\Desktop\bugun_ne_oldu\media\news\images\photo3.jpg",
            "category_id": 4,
            "publication_date": "2024-07-18T11:00:00Z"
        },
        {
            "id": 5,
            "title": "Orci varius natoque penatibus et magnis dis parturient montes",
            "summary": " Nullam non bibendum velit, non ultrices lacus. Proin molestie faucibus dapibus. Mauris accumsan auctor arcu, ac molestie est commodo vitae. Aliquam sed condimentum justo, ut elementum diam. Fusce augue nibh, malesuada ut nisi suscipit, tincidunt tempor magna",
            "content": "Vivamus molestie justo elit, id gravida augue malesuada eu. Fusce pellentesque aliquam nisl, ut ultrices nisl bibendum eget. Donec non viverra erat. Curabitur ac lectus id neque placerat bibendum. In nec porta purus. Sed eu nulla sapien. Fusce et metus sagittis, laoreet lacus id, pulvinar quam. Pellentesque fermentum vitae ligula nec sodales. Integer egestas efficitur arcu et tincidunt. Nunc tristique laoreet arcu in hendrerit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "C:\Users\Eness\Desktop\bugun_ne_oldu\media\news\images\photo4.jpg",
            "category_id": 5,
            "publication_date": "2024-07-18T11:00:00Z"
        },
        {
            "id": 6,
            "title": "Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus",
            "summary": "Bro ipsum dolor sit amet groomer japan air dirtbag 360, rip hellflip hardtail betty titanium snake bite. Road rash Skate jib yard sale couloir ollie. Taco glove rigid rock-ectomy fully death cookies. Cornice avie butter, dirt drop north shore stoked liftie sucker hole grom reverse camber grip tape over the bars stunt method.",
            "content": "Detailed content about Pow afterbang schwag berm. Ripper hammer butter, frontside crank slash stoked wheelie drop hellflip steeps hammerhead euro sucker holePow afterbang schwag berm. Ripper hammer butter, frontside crank slash stoked wheelie drop hellflip steeps hammerhead euro sucker hole.",
            "image": "C:\Users\Eness\Desktop\bugun_ne_oldu\media\news\images\yanardag.jpeg",
            "category_id": 6,
            "publication_date": "2024-07-18T11:00:00Z"
        },
        {
            "id": 7,
            "title": "Pow afterbang schwag berm. Ripper hammer butter, frontside crank slash stoked wheelie drop hellflip steeps hammerhead euro sucker hole",
            "summary": "Sharkbite grind carve rock roll. Dirtbag shuttle couloir 360 manny huck huck 180. Liftie BB roadie, spin twin tip washboard skid lid hammerhead. Couloir wheelie gondy north shore huck, face plant dumbie skater dirtbag table top death cookies free ride taco helmet rail. Avie pocket corn snow dirt jump telegrapher cornice kerny frontside helluva nollie schwag tailgate bro groomer helluva bombhole powder dump pickstick down safety grab.",
            "content": "Detailed content about tech trends.",
            "image": "C:\Users\Eness\Desktop\bugun_ne_oldu\media\news\images\photo2.jpg",
            "category_id": 7,
            "publication_date": "2024-07-18T11:00:00Z"
        },
    ]

    for news in news_list:
        image_path = news.pop("image")
        news_instance, created = News.objects.get_or_create(
            id=news["id"],
            defaults=news
        )
        if created and image_path:
            with open(image_path, "rb") as image_file:
                news_instance.image.save(os.path.basename(image_path), File(image_file))

    # Kullanıcıları ekleyin
    users = [
        {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "password": make_password("password123"), "created_at": "2024-07-19T10:00:00Z"},
        {"id": 2, "name": "Jane Doe", "email": "jane.doe@example.com", "password": make_password("password123"), "created_at": "2024-07-19T10:00:00Z"},
    ]

    for user in users:
        User.objects.get_or_create(
            id=user["id"],
            defaults=user
        )

if __name__ == "__main__":
    load_dummy_data()
