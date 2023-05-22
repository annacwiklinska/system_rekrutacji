from datetime import date


from rekrutacja.models import Uczelnia, KierunekStudiow

kierunki_studiow = [
        KierunekStudiow(
                nazwa='Filologia niemiecka',
                rok_akademicki='2023/2024',
                uczelnia_id=2,
                stopien='I stopień',
                tryb='stacjonarne'
        ),
        KierunekStudiow(
                nazwa='Informatyka',
                rok_akademicki='2023/2024',
                uczelnia_id=3,
                stopien='I stopień',
                tryb='stacjonarne'
        ),
        KierunekStudiow(
                nazwa='Ekonomia',
                rok_akademicki='2023/2024',
                uczelnia_id=4,
                stopien='I stopień',
                tryb='niestacjonarne'
        ),
        KierunekStudiow(
                nazwa='Prawo',
                rok_akademicki='2023/2024',
                uczelnia_id=5,
                stopien='jednolite',
                tryb='stacjonarne'
        ),
        KierunekStudiow(
                nazwa='Zarządzanie',
                rok_akademicki='2023/2024',
                uczelnia_id=6,
                stopien='II stopień',
                tryb='stacjonarne'
        ),
        KierunekStudiow(
                nazwa='Psychologia',
                rok_akademicki='2023/2024',
                uczelnia_id=7,
                stopien='jednolite',
                tryb='niestacjonarne'
        ),
        KierunekStudiow(
                nazwa='Inżynieria środowiska',
                rok_akademicki='2023/2024',
                uczelnia_id=2,
                stopien='II stopień',
                tryb='stacjonarne'
        ),
        KierunekStudiow(
                nazwa='Filologia angielska',
                rok_akademicki='2023/2024',
                uczelnia_id=3,
                stopien='II stopień',
                tryb='niestacjonarne'
        ),
        KierunekStudiow(
                nazwa='Filologia angielska',
                rok_akademicki='2023/2024',
                uczelnia_id=4,
                stopien='I stopień',
                tryb='niestacjonarne'
        ),
        KierunekStudiow(
                nazwa='Matematyka',
                rok_akademicki='2023/2024',
                uczelnia_id=7,
                stopien='I stopień',
                tryb='online'
        ),
        KierunekStudiow(
                nazwa='Fizyka',
                rok_akademicki='2023/2024',
                uczelnia_id=6,
                stopien='II stopień',
                tryb='hybrydowy'
        )
]


for x in kierunki_studiow:
        x.save()


