from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(verbose_name='キャラクター', max_length=10)
    use = models.IntegerField(verbose_name='使用回数', default=0)
    max_dmg = models.IntegerField(verbose_name='最大ダメージ', default=0)
    champion = models.IntegerField(verbose_name='勝利数', default=0)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    weapon_kind = (('ar', 'ar'), ('smg', 'smg'), ('lmg', 'lmg'),('sr', 'sr'))
    bullet_kind = (('ライト', 'ライト'),
                   ('ヘビー', 'ヘビー'),
                   ('エナジー', 'エナジー'),
                   ('ショットガン', 'ショットガン'),
                   ('スナイパー','スナイパー'))

    name = models.CharField(verbose_name='名前', max_length=10)
    kind = models.CharField(verbose_name='武器種', max_length=10, choices=(weapon_kind))
    bullet = models.CharField(verbose_name='弾', max_length=10, choices=(bullet_kind))

    def __str__(self):
        return self.name


class Register(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    dmg = models.IntegerField(verbose_name='ダメージ', default=0)
    rank = models.IntegerField(verbose_name='順位', null=True, blank=True)
    mw = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='main_weapon', null=True, blank=True)
    sw = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='sub_weapon', null=True, blank=True)
    member1 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='member1', null=True, blank=True)
    member2 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='member2', null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.character