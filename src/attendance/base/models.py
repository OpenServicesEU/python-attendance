from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone


class Student(models.Model):
    matriculation = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return '{s.matriculation}'.format(s=self)


class Entry(models.Model):
    INCOMING = 'in'
    OUTGOING = 'out'
    DIRECTION_CHOICES = (
        (INCOMING, 'Incoming'),
        (OUTGOING, 'Outgoing'),
    )
    student = models.ForeignKey('Student')
    time = models.DateTimeField(auto_now_add=True)
    direction = models.CharField(
        max_length=4,
        choices=DIRECTION_CHOICES,
        default=INCOMING
    )
    auto = models.BooleanField(
        default=False
    )

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        if instance.auto:
            return
        try:
            l = sender.objects.filter(student=instance.student).latest('time')
            if l.direction == sender.INCOMING:
                if l.time.date() < timezone.now().date():
                    y = sender()
                    y.student = instance.student
                    y.direction = sender.OUTGOING
                    y.time = l.time.replace(
                        hour=16,
                        minute=0,
                        second=0,
                        microsecond=0
                    )
                    y.auto = True
                    y.save()
                else:
                    instance.direction = sender.OUTGOING
        except sender.DoesNotExist:
            pass

    def __str__(self):
        return '{s.student} @ {s.time}'.format(s=self)

pre_save.connect(
    Entry.pre_save,
    Entry,
    dispatch_uid='{p}.{n}'.format(p=Entry.__module__, n=Entry.__name__)
)
