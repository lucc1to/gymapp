from django.core.management.base import BaseCommand

from exercises.models import Exercise

M = Exercise.Muscle
EXERCISES = [
    # Klatka
    ("Wyciskanie sztangi na ławce płaskiej", M.CHEST),
    ("Wyciskanie sztangi na ławce skośnej", M.CHEST),
    ("Wyciskanie hantli na ławce płaskiej", M.CHEST),
    ("Wyciskanie hantli na ławce skośnej", M.CHEST),
    ("Rozpiętki z hantlami", M.CHEST),
    ("Rozpiętki na bramie", M.CHEST),
    ("Butterfly (maszyna)", M.CHEST),
    ("Wyciskanie na maszynie", M.CHEST),
    ("Pompki", M.CHEST),
    ("Pompki na poręczach (dipy)", M.CHEST),
    # Plecy
    ("Martwy ciąg", M.BACK),
    ("Podciąganie nachwytem", M.BACK),
    ("Podciąganie podchwytem", M.BACK),
    ("Ściąganie drążka wyciągu górnego", M.BACK),
    ("Wiosłowanie sztangą w opadzie", M.BACK),
    ("Wiosłowanie hantlem jednorącz", M.BACK),
    ("Wiosłowanie na wyciągu dolnym", M.BACK),
    ("Wiosłowanie na maszynie", M.BACK),
    ("Pullover na wyciągu", M.BACK),
    ("Szrugsy z hantlami", M.BACK),
    # Barki
    ("Wyciskanie żołnierskie (OHP)", M.SHOULDERS),
    ("Wyciskanie hantli nad głowę siedząc", M.SHOULDERS),
    ("Wznosy hantli bokiem", M.SHOULDERS),
    ("Wznosy bokiem na wyciągu", M.SHOULDERS),
    ("Odwrotne rozpiętki", M.SHOULDERS),
    ("Face pull", M.SHOULDERS),
    ("Arnoldki", M.SHOULDERS),
    # Biceps
    ("Uginanie ramion ze sztangą", M.BICEPS),
    ("Uginanie ramion z hantlami", M.BICEPS),
    ("Uginanie młotkowe", M.BICEPS),
    ("Uginanie na modlitewniku", M.BICEPS),
    ("Uginanie ramion na wyciągu", M.BICEPS),
    # Triceps
    ("Prostowanie ramion na wyciągu", M.TRICEPS),
    ("Wyciskanie francuskie", M.TRICEPS),
    ("Wyciskanie sztangi wąsko", M.TRICEPS),
    ("Prostowanie ramienia nad głową z hantlem", M.TRICEPS),
    ("Pompki w podporze tyłem", M.TRICEPS),
    # Nogi
    ("Przysiad ze sztangą", M.LEGS),
    ("Przysiad bułgarski", M.LEGS),
    ("Wypychanie na suwnicy", M.LEGS),
    ("Hack przysiad", M.LEGS),
    ("Martwy ciąg rumuński", M.LEGS),
    ("Wyprosty nóg na maszynie", M.LEGS),
    ("Uginanie nóg na maszynie", M.LEGS),
    ("Wykroki z hantlami", M.LEGS),
    ("Hip thrust", M.LEGS),
    ("Wspięcia na palce", M.LEGS),
    # Brzuch
    ("Plank", M.ABS),
    ("Brzuszki", M.ABS),
    ("Unoszenie nóg w zwisie", M.ABS),
    ("Allahy (spięcia na wyciągu)", M.ABS),
    ("Russian twist", M.ABS),
]


class Command(BaseCommand):
    help = "Dodaje do bazy popularne ćwiczenia"

    def handle(self, *args, **options):
        added = 0
        for name, muscle in EXERCISES:
            _, created = Exercise.objects.get_or_create(
                name=name,
                defaults={"muscle": muscle},
            )
            if created:
                added += 1
        total = Exercise.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f"Dodano {added} nowych ćwiczeń. W bazie jest teraz {total} ćwiczeń."
            )
        )
