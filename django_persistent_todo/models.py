from django.db import models


class ToDoItem(models.Model):
    """ Items are associated with one another by list id. """
    list_id = models.IntegerField(db_index=True, blank=False)
    text = models.CharField(max_length=255, blank=False)
    order = models.IntegerField(blank=True, null=True)
    complete = models.BooleanField()

    def __unicode__(self):
        return self.text
