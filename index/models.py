from django.db import models
from django.utils.text import slugify
from django.urls import reverse



class Teacher(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="To'liq ismi")
    photo = models.ImageField(upload_to='teachers/photos/', blank=True, null=True, verbose_name='Foto')
    birth_date = models.DateField(blank=True, null=True, verbose_name="Tug'ilgan sanasi")
    death_date = models.DateField(blank=True, null=True, verbose_name="Vafot etgan sanasi")
    birth_place = models.CharField(max_length=255, verbose_name="Tug'ilgan joyi")
    profession = models.CharField(max_length=255, verbose_name="Kasbi / Cholg'u asbobi")
    biography = models.TextField(verbose_name="Biografiyasi")
    achievements = models.TextField(verbose_name="Yutuqlari", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"
        ordering = ['full_name']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.full_name)
            slug = base_slug
            n = 1
            while Teacher.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("teacher_detail", kwargs={'slug': self.slug})


# ✅ Новая модель — для макомов и композиций
class Meros(models.Model):
    RESOURCE_TYPES = [
        ('maqom', 'Maqom'),
        ('composition', 'Kompozitsiya'),
    ]

    title = models.CharField(max_length=255, verbose_name="Nom")
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='meroslar',
        verbose_name="Muallif (agar bo‘lsa)"
    )
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES, verbose_name="Turi")
    notes_file = models.FileField(upload_to='meros/notes/', blank=True, null=True, verbose_name="Nota fayli (PDF)")
    lyrics = models.TextField(blank=True, null=True, verbose_name="Matni / Tavsifi")
    youtube_link = models.URLField(blank=True, null=True, verbose_name="YouTube havolasi")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "Meros"
        verbose_name_plural = "Meroslar"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            n = 1
            while Meros.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("meros_detail", kwargs={'slug': self.slug})




class Makom(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Bolim(models.Model):  # Mushkilot / Nasr
    makom = models.ForeignKey(Makom, on_delete=models.CASCADE, related_name="bolimlar")
    name = models.CharField(max_length=50, choices=[
        ("mushkilot", "Mushkilot"),
        ("nasr", "Nasr"),
    ])
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + self.makom.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.makom.name} — {self.name}"


class Shoba(models.Model):  # только если Nasr
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE, related_name="shobalar")
    name = models.CharField(max_length=100)  # 1-guruh sho‘basi, 2-guruh sho‘basi
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + self.bolim.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.bolim} — {self.name}"


class Kuy(models.Model):
    shoba = models.ForeignKey(Shoba, on_delete=models.CASCADE, null=True, blank=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=150)
    notes = models.FileField(upload_to="notes/", blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)

    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

