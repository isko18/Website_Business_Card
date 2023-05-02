from django.db import models

class Users(models.Model):
    profile_image = models.ImageField(
        upload_to="post_images/",
        verbose_name="Фотография"         
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Пользователь"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    phone_number = models.CharField(
        max_length=25,
        verbose_name="Номер"
    )
    age = models.IntegerField(
        verbose_name="Возраст"
    )
    instagram = models.URLField(
        verbose_name="instagram"
    )
    telegram = models.URLField(
        verbose_name="telegram"
    )

class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта" 
    )
    logo = models.ImageField(
        upload_to="logo",
        verbose_name="Логотип сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )

class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название" 
    )
    logo = models.ImageField(
        upload_to="about_image/",
        verbose_name="Фотография" 
    )  
    description = models.TextField(
        verbose_name="Описание "
    )
    created_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Дата создания"
    )

class Contact(models.Model):
    phone_number = models.CharField(
        max_length=25,
        verbose_name="Номер"
    )
    email = models.URLField(
        verbose_name="email"
    )   
    locate = models.CharField(
        max_length=255,
        verbose_name="Локация"
    )
    locate_url = models.URLField(
        verbose_name="Ссылка на локацию"
    )
    facebook_url = models.URLField(
        verbose_name="facebook"
    )
    youtube_url = models.URLField(
        verbose_name="youtube"
    )
