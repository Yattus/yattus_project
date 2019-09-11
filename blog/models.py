import os
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

#  from django.contrib.contenttypes.models import ContentType
#  from django.contrib.contenttypes.fields import GenericForeignKey
#  GenericRelation
# from django.utils import timezone

# Create your models here.


class Categorie(models.Model):
    """ table Article Categorie """
    nom = models.CharField(unique=True, max_length=50)
    slug = models.SlugField()
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            'slug',
            'parent',
        )  # forcé qu'ils soient unique
        verbose_name_plural = 'Categories'

    # we return the full_path for a categorie instance
    def __str__(self):
        full_path = [self.nom]
        cat = self.parent

        while cat is not None:
            full_path.append(cat.nom)
            cat = cat.parent

        return ' -> '.join(full_path[::-1])


#  Abstract table for Article and anothers docs like Commentaires
class Document(models.Model):
    """ Abstract table """
    auteur = models.CharField(max_length=40, unique=False)  # autor name
    contenu = models.TextField(unique=True, default='', null=False)
    date_post = models.DateTimeField(auto_now=True, auto_now_add=False,
                                     verbose_name="Date dernière modification")

    class Meta:
        abstract = True
        verbose_name_plural = "Documents"


# Renommé de nom de l'image de l'article
def rename_article_vue(instance, fichier):
    categorie = instance.categorie.__str__()
    categorie = categorie.replace("'", "").replace(" -> ",
                                                   "/").replace(' ', '_')
    return "blog/vue_articles/{0}/{1}".format(categorie,
                                              instance.titre)


class Article(Document):
    """ table Article """
    titre = models.CharField(unique=True, max_length=100)  # Titre de l'article
    introduction = models.TextField(
        unique=True, null=True, verbose_name='Intro')
    vue = models.ImageField(
        verbose_name="Image du post",
        default=False,
        upload_to=rename_article_vue)
    valide = models.NullBooleanField(default=True)
    slug = models.SlugField(unique=False)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    # date_post_update = models.DateTimeField(
    #     auto_now=False,
    #     auto_now_add=False,
    #     verbose_name="Dernière modification")

    class Meta:
        verbose_name_plural = "Articles"
        verbose_name = 'Article'
        ordering = ['categorie', 'date_post']

    def __str__(self):
        """ Name display in bd """
        return "TITRE: {0}, AUTEUR: {1}, CATEGORIE: {2}".format(self.titre,
                                                                self.auteur,
                                                                self.categorie)

    # we return a liste of links look like
    # [/a/b/c/d, /a/b/c, /a/b, /a]
    def get_cat_list(self):
        cat = self.categorie

        cat_list_link = []
        while cat is not None:
            cat_list_link.append(cat.slug)
            cat = cat.parent

        for i in range(len(cat_list_link) - 1):
            cat_list_link[i] = '/'.join(cat_list_link[-1:i - 1:-1])

        return cat_list_link[-1:0:-1]


#  class Commentaire(Document):
#  """ table Commentaire """
#  email = models.EmailField(null=False)
#  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#  object_id = models.PositiveIntegerField()
#  content_object = GenericForeignKey('content_type', 'object_id')
#
#  class Meta:
#  verbose_name = 'Commentaires'
#  ordering = ['content_type', 'date']
#
#  def __str__(self):
#  return self.auteur


# Signal de suppression du fichier(sujet) associer lorsqu'on efface un sujet
# signal who remove file's sujet if we deleted the sujet in base
@receiver(pre_delete, sender=Article)
def delete_vue_article(sender, instance, **kwargs):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Transform file name
    filename = instance.titre
    filename = filename.replace(' ', '_').replace("'", "")

    # Transform categorie name
    categorie = instance.categorie.__str__()
    categorie = categorie.replace("'", "").replace(" -> ",
                                                   "/").replace(' ', '_')

    os.chdir(path + '/media/blog/vue_articles/' + categorie)
    if os.path.isfile(filename):
        os.remove(filename)
    os.chdir(path)
