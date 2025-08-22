import uuid
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from datetime import datetime
from books.models import Book, Genre

class Command(BaseCommand):
    help = "Seed initial books and genres data"

    def handle(self, *args, **kwargs):
        # --- GENRES ---
        genres_data = [
            (1, 'Fiction'),
            (2, 'Non-Fiction'),
            (3, 'Poetry'),
            (4, 'Graphic Novels/Comics'),
            (5, 'Mystery/Thriller'),
            (6, 'Romance'),
            (7, 'Science Fiction'),
            (8, 'Fantasy'),
            (9, 'Horror'),
            (10, 'History'),
            (11, 'Science'),
            (12, 'Biography/Autobiography'),
            (13, 'Self-Help'),
            (14, 'Health & Wellness'),
            (15, 'Business & Economics'),
            (16, 'Psychology'),
            (17, 'Politics'),
            (18, 'Religion & Spirituality'),
            (19, 'Art & Photography'),
            (20, 'Humor'),
        ]
        for gid, name in genres_data:
            Genre.objects.get_or_create(id=gid, defaults={"name": name})

        # --- BOOKS ---
        books_data = [
            {
                "id": uuid.UUID("87561f47-4212-4e5c-a80d-584d937f6d76"),
                "title": "Hujan Bulan Juni: Novel",
                "author": "Sapardi Djoko Damono",
                "isbn": "9786029591545",
                "published_date": make_aware(datetime(2015, 6, 15)),
                "available_copies": 3,
                "cover": "book_covers/Hujan-Bulan-Juni-Sebuah-Novel_ckai0Z5.jpg",
                "language": "id",
                "pages": 144,
                "publisher": "Gramedia Pustaka Utama",
                "description": """Novel Hujan Bulan Juni mengisahkan tentang bagaimana mungkin seseorang mempunyai keinginan untuk mengurai kembali benang yang tidak terkira jumlahnya dalam selembar sapu tangan yang sudah ditenunnya sendiri.
                    Bagaimana mungkin seseorang dapat mendadak terbebas dari jaringan benang yang silang-menyilang, susun-bersusun, dan timpa-menimpa dengan rapi di selembar sapu tangan yang telah bertahun-tahun lamanya ditenun dengan sabar oleh jari-jemarinya sendiri, oleh ketabahannya sendiri, oleh tarikan dan hembusan nafasnya sendiri, oleh kesunyiannya sendiri, oleh kerinduannya sendiri, oleh rintik waktu dalam benaknya sendiri, oleh penghayatannya sendiri mengenai hubungan-hubungan pelik antara laki-laki dan perempuan yang tinggal di sebuah ruangan kedap suara yang bernama kasih sayang.""",
                "is_must_read": False,
                "genres": [1, 6],
            },
            {
                "id": uuid.UUID("86910230-7aa2-4821-beb8-a493410bdee4"),
                "title": "Animal Farm",
                "author": "George Orwell",
                "isbn": "9781943138425",
                "published_date": make_aware(datetime(2024, 5, 28, 17, 0, 0)),
                "available_copies": 2,
                "cover": "book_covers/animal-farm_george_orwell.jpg",
                "language": "en",
                "pages": 115,
                "publisher": "Aeons Classics",
                "description": """"Animal Farm is an allegorical and dystopian novella by George Orwell, first published in England on 17 August 1945. According to Orwell, the book reflects events leading up to the Russian Revolution of 1917 and then on into the Stalinist era of the Soviet Union. Orwell, a democratic socialist, was a critic of Joseph Stalin and hostile to Moscow-directed Stalinism, an attitude that was critically shaped by his experiences during the Spanish Civil War. The Soviet Union, he believed, had become a brutal dictatorship, built upon a cult of personality and enforced by a reigh of terror. In a letter to Yvonne Davet, Orwell described Animal Farm as a satirical tale against Stalin ('un conte satirique contre Staline'), and in his essay 'Why I Write' (1946), wrote that Animal Farm was the first book in which he tried, with full consciousness of what he was doing, 'to fuse political purpose and artistic purpose into one whole'. -- back cover.""",
                "is_must_read": False,
                "genres": [1],
            },
            {
                "id": uuid.UUID("42bb7a27-b2c0-4202-bbd8-5e4b2cdf6199"),
                "title": "The Road",
                "author": "Cormac McCarthy",
                "isbn": "9780307277923",
                "published_date": make_aware(datetime(2006, 3, 27, 17, 0, 0)),
                "available_copies": 12,
                "cover": "book_covers/the-road_cormac-mcCarthy.jpg",
                "language": "en",
                "pages": 287,
                "publisher": "Vintage International",
                "description": """The searing, post-apocalyptic novel about a father and son’s fight to survive.
                    A father and his son walk alone through burned America. Nothing moves in the ravaged landscape save the ash on the wind. It is cold enough to crack stones, and when the snow falls it is gray. The sky is dark. Their destination is the coast, although they don’t know what, if anything, awaits them there. They have nothing; just a pistol to defend themselves against the lawless bands that stalk the road, the clothes they are wearing, a cart of scavenged food—and each other.
                    The Road is the profoundly moving story of a journey. It boldly imagines a future in which no hope remains, but in which the father and his son, “each the other’s world entire,” are sustained by love. Awesome in the totality of its vision, it is an unflinching meditation on the worst and the best that we are capable of: ultimate destructiveness, desperate tenacity, and the tenderness that keeps two people alive in the face of total devastation.""",
                "is_must_read": False,
                "genres": [1],
            },
            {
                "id": uuid.UUID("ce951bd3-1e9a-4aa3-92fa-03039d206315"),
                "title": "Brave New World",
                "author": "Aldous Huxley",
                "isbn": "9783492116404",
                "published_date": make_aware(datetime(1932, 2, 3, 16, 40, 0)),
                "available_copies": 3,
                "cover": "book_covers/brave-new-world_aldous-huxley.jpg",
                "language": "en",
                "pages": 311,
                "publisher": "Chatto & Windus",
                "description": """Originally published in 1932, this outstanding work of literature is more crucial and relevant today than ever before. Cloning, feel-good drugs, antiaging programs, and total social control through politics, programming, and media -- has Aldous Huxley accurately predicted our future? With a storyteller's genius, he weaves these ethical controversies in a compelling narrative that dawns in the year 632 AF (After Ford, the deity). When Lenina and Bernard visit a savage reservation, we experience how Utopia can destroy humanity. A powerful work of speculative fiction that has enthralled and terrified readers for generations, Brave New World is both a warning to be heeded and thought-provoking yet satisfying entertainment.""",
                "is_must_read": True,
                "genres": [1],
            },
            {
                "id": uuid.UUID("1ac99d74-d8f5-4f1f-9424-cd34cfb4dd23"),
                "title": "A Happy Life",
                "author": "Seneca",
                "isbn": "9786232423831",
                "published_date": make_aware(datetime(2023, 6, 7, 0, 0, 0)),
                "available_copies": 20,
                "cover": "book_covers/a_happy_life_-_seneca_tK2mC01.png",
                "language": "id",
                "pages": 305,
                "publisher": "Noura Books",
                "description": """Kebahagiaan—paling sering dibicarakan, sekaligus paling sukar dipahami. Dalam keadaan buta dan tergesa-gesa, semua orang mengejar kebahagiaan tanpa arah, yang akhirnya hanya mendapatkan lelah.
                    A Happy Life, yang dirangkum dari kumpulan catatan dan surat-surat Lucius Annaeus Seneca, mengajak kita merenungi “apa tujuan kita”, kemudian “mana jalan terbaik untuk mencapainya”. Salah satu pemikir Romawi yang disebut sebagai paling cerdas di antara semua filsuf Stoa ini, mencoba menjawab dua pertanyaan tentang apa itu bahagia dan apa saja yang mendasarinya.
                    Pembaca era modern saat ini akan merasakan, betapa buah pikir Seneca tak pernah usang dan tetap relevan meski sudah dua milenium berselang sejak dituliskan.""",
                "is_must_read": False,
                "genres": [1, 13],
            },
            {
                "id": uuid.UUID("ee424991-1e86-4ee5-9133-8e3d19e2d40d"),
                "title": "The Catcher in the Rye",
                "author": "J.D. Salinger",
                "isbn": "9780316769488",
                "published_date": make_aware(datetime(1951, 7, 16, 0, 0, 0)),
                "available_copies": 10,
                "cover": "book_covers/a_catcher_in_the_rye_-_jd_salinger_BDxCmpI.jpg",
                "language": "en",
                "pages": 277,
                "publisher": "Back Bay Books",
                "description": """KStory of Holden Caufield with his idiosyncrasies, penetrating insight, confusion, sensitivity and negativism.""",
                "is_must_read": False,
                "genres": [1, 8],
            },
            {
                "id": uuid.UUID("22f04a6a-98db-4065-929d-f358d3dfd84c"),
                "title": "A Song of Ice and Fire: A Game of Thrones",
                "author": "George R.R. Martin",
                "isbn": "9780553588484",
                "published_date": make_aware(datetime(2005, 8, 1, 0, 0, 0)),
                "available_copies": 2,
                "cover": "book_covers/GOThcEng.jpg",
                "language": "en",
                "pages": 835,
                "publisher": "Bantam",
                "description": """A Game of Thrones is the inaugural novel in A Song of Ice and Fire, an epic series of fantasy novels crafted by the American author George R. R. Martin. Published on August 1, 1996, this novel introduces readers to the richly detailed world of Westeros and Essos, where political intrigue, power struggles, and magical elements intertwine.
                    The story unfolds through multiple perspectives, each chapter focusing on a different character, allowing readers to experience the narrative from various angles. This complex structure has become a hallmark of Martin's storytelling, immersing readers in the lives and motivations of a diverse cast.""",
                "is_must_read": False,
                "genres": [1, 7],
            },
            {
                "id": uuid.UUID("03d76750-9d99-47c2-acd8-4f300164abd9"),
                "title": "1984",
                "author": "George Orwell",
                "isbn": "9781782124207",
                "published_date": make_aware(datetime(1949, 6, 7, 16, 0, 0)),
                "available_copies": 2,
                "cover": "book_covers/1984_-_george_orwell2.jpg",
                "language": "en",
                "pages": 317,
                "publisher": "Arcturus",
                "description": """Nineteen Eighty-Four: A Novel, often referred to as 1984, is a dystopian social science fiction novel by the English novelist George Orwell (the pen name of Eric Arthur Blair). It was published on 8 June 1949 by Secker & Warburg as Orwell's ninth and final book completed in his lifetime. Thematically, Nineteen Eighty-Four centres on the consequences of totalitarianism, mass surveillance, and repressive regimentation of persons and behaviours within society. Orwell, himself a democratic socialist, modelled the authoritarian government in the novel after Stalinist Russia. More broadly, the novel examines the role of truth and facts within politics and the ways in which they are manipulated.""",
                "is_must_read": True,
                "genres": [1],
            },
            {
                "id": uuid.UUID("454beee4-a3eb-41f7-be6e-dbf8be3708e2"),
                "title": "Fahrenheit 451",
                "author": "Ray Bradbury",
                "isbn": "7435738236200",
                "published_date": make_aware(datetime(1953, 10, 18, 16, 30, 0)),
                "available_copies": 4,
                "cover": "book_covers/fahrenhait-451_ray-bradburry.jpg",
                "language": "en",
                "pages": 147,
                "publisher": "Ballantine Books",
                "description": """Fahrenheit 451 is a 1953 dystopian novel by American writer Ray Bradbury. Often regarded as one of his best works, the novel presents a future American society where books are outlawed and "firemen" burn any that are found. The book's tagline explains the title as "'the temperature at which book paper catches fire, and burns": the autoignition temperature of paper. The lead character, Guy Montag, is a fireman who becomes disillusioned with his role of censoring literature and destroying knowledge, eventually quitting his job and committing himself to the preservation of literary and cultural writings.
                    The novel has been the subject of interpretations focusing on the historical role of book burning in suppressing dissenting ideas for change. In a 1956 radio interview, Bradbury said that he wrote Fahrenheit 451 because of his concerns at the time (during the McCarthy era) about the threat of book burning in the United States. In later years, he described the book as a commentary on how mass media reduces interest in reading literature.
                    In 1954, Fahrenheit 451 won the American Academy of Arts and Letters Award in Literature and the Commonwealth Club of California Gold Medal. It later won the Prometheus "Hall of Fame" Award in 1984 and a "Retro" Hugo Award, one of a limited number of Best Novel Retro Hugos ever given, in 2004. Bradbury was honored with a Spoken Word Grammy nomination for his 1976 audiobook version.""",
                "is_must_read": True,
                "genres": [1],
            },
        ]

        for b in books_data:
            book, created = Book.objects.get_or_create(
                id=b["id"],
                defaults={
                    "title": b["title"],
                    "author": b["author"],
                    "isbn": b["isbn"],
                    "published_date": b["published_date"],
                    "available_copies": b["available_copies"],
                    "cover": b["cover"],
                    "language": b["language"],
                    "pages": b["pages"],
                    "publisher": b["publisher"],
                    "description": b["description"],
                    "is_must_read": b["is_must_read"],
                },
            )
            if created:
                book.genres.set(Genre.objects.filter(id__in=b["genres"]))

        self.stdout.write(self.style.SUCCESS("Books and genres seeded successfully"))  # pylint: disable=no-member