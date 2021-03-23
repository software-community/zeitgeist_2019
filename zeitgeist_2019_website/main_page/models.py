from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from campus_ambassador.models import *
from main_page.methods import sendNotification

# Create your models here.


class Category(models.Model):
    
    CATEGORY_CHOICES = [
        ('Dance', 'Dance'),
        ('Dramatics', 'Dramatics'),
        ('Fine Arts', 'Fine Arts'),
        ('Gaming', 'Gaming'),
        ('Life Style', 'Life Style'),
        ('Literary', 'Literary'),
        ('Music', 'Music'),
        ('Photography', 'Photography'),
        ('Quizzing', 'Quizzing'),
        ('Video Making', 'Video Making'),
    ]
    name = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        null=False,
        blank=False,
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Categories'


class Subcategory(models.Model):

    name = models.CharField(max_length=40, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    

    def __str__(self):
        return str(self.name) + " - " + str(self.category)

    class Meta:
        verbose_name_plural = 'Subcategories'

class Cat(models.Model):
    category = models.CharField(blank=False, null=False,max_length=200)

    class Meta:
        verbose_name_plural = "Event Categories"

    def __str__(self):
        return str(self.category)

class SubCat(models.Model):
    category = models.ForeignKey(Cat, models.SET_NULL, blank=True, null=True)
    sub_category = models.CharField(blank=False, null=False,max_length=200)

    class Meta:
        verbose_name_plural = "Event Sub Categories"

    def __str__(self):
        return str(self.sub_category)

class Events(models.Model):
    serial = models.IntegerField(blank=False)
    category = models.ForeignKey(SubCat, models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=40, null=False, blank=False)
    code = models.CharField(max_length=20, null=False, blank=False, unique=True)
    EVENT_TYPE_CHOICES = [
        ('Solo', 'Solo'),
        ('Group', 'Group'),
    ]
    event_type = models.CharField(
        max_length=5,
        choices=EVENT_TYPE_CHOICES,
        null=False,
        blank=False,
    )
    rulebook = models.CharField(max_length=300)
    poster = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = 'Events List'
        
class Registration(models.Model):
    user_unique_id = models.CharField(blank=False, null=False,max_length=200)
    first_name = models.CharField(blank=False, null=False,max_length=200)
    last_name = models.CharField(blank=False, null=False,max_length=200)
    email = models.CharField(blank=False, null=False,max_length=200)
    college_name = models.CharField(blank=False, null=False,max_length=200)
    events=models.CharField(max_length=500)
    mobile = models.CharField(blank=False, null=False,max_length=15)

    class Meta:
        verbose_name_plural = "Registrations"

class Event(models.Model):

    name = models.CharField(max_length=40, null=False, blank=False)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    link_to_rulebook = models.URLField(max_length=300)
    participation_fees_per_person = models.IntegerField(blank=False)
    EVENT_TYPE_CHOICES = [
        ('Solo', 'Solo'),
        ('Group', 'Group'),
    ]
    event_type = models.CharField(
        max_length=5,
        choices=EVENT_TYPE_CHOICES,
        null=False,
        blank=False,
    )

    first_cash_prize = models.IntegerField(blank=False)
    second_cash_prize = models.IntegerField(blank=False)
    third_cash_prize = models.IntegerField(blank=False)
    first_goodies = models.IntegerField(blank=False)
    second_goodies = models.IntegerField(blank=False)
    third_goodies = models.IntegerField(blank=False)
    minimum_team_size = models.IntegerField(blank=False)
    maximum_team_size = models.IntegerField(blank=False)
    start_date_time = models.DateTimeField(blank=False)
    end_date_time = models.DateTimeField(blank=False)
    description = models.TextField(blank=False)
    venue = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name) + " - " + str(self.subcategory)


class Participant(models.Model):

    participating_user = models.OneToOneField(User, verbose_name='Participating User', on_delete=models.CASCADE, primary_key=True)
    participant_code = models.CharField(max_length=15, verbose_name='Participant Code', unique=True)
    name = models.CharField(verbose_name='Name', max_length=40, null=False, blank=False)
    college_name = models.CharField(max_length=200, verbose_name='College Name', null=False, blank=False)
    college_city = models.CharField(max_length=50, verbose_name='College City', null=False, blank=False)
    personal_address_with_pin_code = models.TextField(verbose_name='Personal Address with PIN Code', null=False, blank=False)
    contact_mobile_number = PhoneNumberField(null=False, blank=False, verbose_name='Contact Mobile Number', region='IN')
    whatsapp_mobile_number = PhoneNumberField(null=False, blank=False, verbose_name='WhatsApp Mobile Number', region='IN')
    birth_date = models.DateField(verbose_name='Birth Date (YYYY-MM-DD)', null=False, blank=False)
    referring_ca = models.ForeignKey(RegistrationDetails, verbose_name='CA Referral Code', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.participant_code)


class ParticipantHasPaid(models.Model):

    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    paid_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, default='-1')
    payment_request_id = models.CharField(max_length=100, default='-1')

    def __str__(self):
        return str(self.participant) + " - " + str(self.paid_event)

    class Meta:
        verbose_name_plural = 'Participant Has Paid'


class ParticipantHasParticipated(models.Model):

    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.participant) + " - " + str(self.event)

    class Meta:
        verbose_name_plural = 'Participant Has Participated'


class Team(models.Model):

    name = models.CharField(max_length=40, verbose_name='Team Name', null=False, blank=False)
    team_code = models.CharField(max_length=50, verbose_name='Team Code', unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    captain = models.ForeignKey(Participant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.team_code) + " - " + str(self.name)


class TeamHasMember(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(Participant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.team) + " - " + str(self.member)

    class Meta:
        verbose_name_plural = 'Team Has Member'


class Our_Sponsor(models.Model):

    name_of_photo_in_static_files = models.CharField(max_length=15, blank=False, null=False)
    link_to_sponsor = models.URLField(max_length=300)

    class Meta:
        verbose_name_plural = 'Our Sponsor'

class Media_Partner(models.Model):

    name_of_photo_in_static_files = models.CharField(max_length=15, blank=False, null=False)
    link_to_sponsor = models.URLField(max_length=300)

    class Meta:
        verbose_name_plural = 'Media Partner'


class Prev_Sponsor(models.Model):

    name_of_photo_in_static_files = models.CharField(max_length=15, blank=False, null=False)
    link_to_sponsor = models.URLField(max_length=300)

    class Meta:
        verbose_name_plural = 'Previous Sponsor'




class Support(models.Model):

    donating_user = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_amount = models.CharField(max_length=10)
    transaction_id = models.CharField(max_length=100, default='-1')
    payment_request_id = models.CharField(max_length=100, default='-1')

    def __str__(self):
        return str(self.donating_user.get_full_name()) + ' ' + str(self.donating_user.email)


class Notification(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        sendNotification(self.title, self.content)

class WebCounts(models.Model):

    count = models.IntegerField(blank=False, null=False)

    def increment():
        count = WebCounts.objects.first()
        count.count+=1
        count.save()
        return count.count

    class Meta:
        verbose_name_plural = 'Website Counts'