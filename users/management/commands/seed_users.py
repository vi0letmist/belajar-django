from django.core.management.base import BaseCommand
from django.utils.timezone import now
import uuid

from users.models import User

class Command(BaseCommand):
    help = "Seed initial users"

    def handle(self, *args, **kwargs):
        users_data = [
            {
                "id": uuid.UUID("432336d0-51f7-4ac8-9675-8f7e5063ae43"),
                "fullname": "jetri 1",
                "username": "jetri",
                "email": "jetri@gmail.com",
                "password": "pbkdf2_sha256$870000$GLTLgIE0lMukWqTNchIojz$j/YpwUVjaSsQsiJNy1xiqxmUla3CMLBIekR6m7fEtso=",
                "last_login": "2024-12-26 15:34:15.583",
                "created_at": "2024-12-26 15:34:15.583",
                "updated_at": "2024-12-26 15:34:15.583",
                "role": "Admin",
            },
            {
                "id": uuid.UUID("8f2ce9f1-e5ee-4b67-959b-6c0e0386accf"),
                "fullname": "vi0letmist",
                "username": "vi0letmist",
                "email": "vi0letmist@gmail.com",
                "password": "pbkdf2_sha256$870000$1lpMP1pAUmpEMLRJ3fx0fH$2ElmXHr9gi6vplfmPrWLz+eBE+in5mJnogbmo025+jY=",
                "last_login": "2024-12-30 11:43:37.168",
                "created_at": "2024-12-30 11:43:37.168",
                "updated_at": "2024-12-30 11:43:37.168",
                "role": "Librarian",
            },
            {
                "id": uuid.UUID("94026233-8621-40f6-8eaa-4e47e77f77bf"),
                "fullname": "Alex Turner",
                "username": "alexturner",
                "email": "alexturner@gmail.com",
                "password": "pbkdf2_sha256$870000$QgneGLJJpOfDSMQEHIdXvF$tPs1mwRo/lNGEyV3VZDR3zDm/7ShfPiPUUTRhTuw5OI=",
                "last_login": "2025-01-15 15:20:24.748",
                "created_at": "2025-01-15 15:20:24.748",
                "updated_at": "2025-01-15 15:20:24.748",
                "role": "Member",
            },
            {
                "id": uuid.UUID("85cd72fc-571f-4a01-adad-586705ee469b"),
                "fullname": "Julian Casablancas",
                "username": "juliancasablancas",
                "email": "juliancasablancas@strokes.com",
                "password": "pbkdf2_sha256$870000$OFm8rxBhauFx1kzAfI2mRK$jOYMLd32R4+Bv33T2I+IfmVtXn/I8Zp6DHXy6cs8AEU=",
                "last_login": "2025-06-02 20:17:36.396",
                "created_at": "2025-06-02 20:17:36.396",
                "updated_at": "2025-06-02 20:17:36.396",
                "role": "Member",
            },
            {
                "id": uuid.UUID("3f845fc3-fb90-4afe-81cd-5bcd76a7cb51"),
                "fullname": "morissay",
                "username": "morrissay",
                "email": "morrissay@gmail.com",
                "password": "pbkdf2_sha256$870000$HDmf2kpDqjijXJNe8VKUTN$88jUpN1VTax+PNflChS/OQ2BKZPJYlSBNhfpHTGF3Zk=",
                "last_login": "2025-06-09 22:20:33.537",
                "created_at": "2025-06-09 22:20:33.538",
                "updated_at": "2025-06-09 22:20:33.538",
                "role": "Member",
            },
        ]

        for u in users_data:
            user, created = User.objects.update_or_create(
                id=u["id"],
                defaults={
                    "fullname": u["fullname"],
                    "username": u["username"],
                    "email": u["email"],
                    "password": u["password"],  # sudah hashed
                    "last_login": u["last_login"],
                    "created_at": u["created_at"],
                    "updated_at": u["updated_at"],
                    "role": u["role"],
                    "is_active": True,
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created user {user.username}")) # pylint: disable=no-member
            else:
                self.stdout.write(self.style.WARNING(f"Updated user {user.username}")) # pylint: disable=no-member

        self.stdout.write(self.style.SUCCESS("Users seeded successfully!")) # pylint: disable=no-member
