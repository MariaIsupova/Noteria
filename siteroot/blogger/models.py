from django.db.models import *
# from django.contrib.auth.models import User
# from django.urls import reverse


class Blog(Model):
    # author = ForeignKey(User, on_delete=CASCADE)

    title = CharField(max_length=80)
    created_at = DateTimeField('creation timestamp', auto_now_add=True) # auto_now_add=True - автоматически добавлялось

    # def __str__(self):
    #     return '"%s" by @%s' % (self.title, self.author.username)
    #
    # def get_absolute_url(self):
    #     return reverse('blog_by_id', kwargs={'blog_id': self.id})
    #

class Post(Model):
    blog = ForeignKey(Blog, on_delete=CASCADE) # on_delete=CASCADE - удалится, если удалится родитель
    subject = CharField(max_length=80)
    text = TextField(max_length=4096)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)
    updated_at = DateTimeField('update timestamp', auto_now=True)

    #def is_modified(self):
    #     return (self.updated_at - self.created_at).total_seconds() >= 1
    # is_modified.boolean = True

    #def __str__(self):
        # return 'id:%s' % (self.id,)