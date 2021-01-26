from django.conf import settings
from django.db import models
import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.auth.models import User


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""

        if not email:
            raise ValueError("Email must be a valid address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """ Creates and saves a new superuser """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """custome user model that uses email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"


class Subject(models.Model):
    """ saves subjects offered """

    SubjectId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SubjectName = models.CharField(max_length=100, blank=True)
    Abbreviation = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.SubjectName


class Term(models.Model):
    """ Saves periods in a year """

    TermId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TermName = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.TermName


class Group(models.Model):
    """ saves groups object """

    GroupId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    GroupName = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.GroupName


class Student(models.Model):
    """ students model that saves students """

    StudentId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    FirstName = models.CharField(max_length=100, blank=True)
    LastName = models.CharField(max_length=100, blank=True)
    ComChannel = models.CharField(max_length=100, blank=True)
    Groups = models.ManyToManyField(Group, related_name="groups_registered")
    Gender = models.CharField(
        max_length=10, choices=(("M", "Male"), ("F", "Female")), default="F"
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.FirstName


class Score(models.Model):
    """ Saves scores object for subjects taken by student"""

    ScoreId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Term = models.ForeignKey(Term, on_delete=models.CASCADE)
    score = models.IntegerField()
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.score


class Leader(models.Model):
    """Saves leaders objects of various groups """

    LeaderId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Group = models.ForeignKey(Group, on_delete=models.CASCADE)
    Position = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.Position