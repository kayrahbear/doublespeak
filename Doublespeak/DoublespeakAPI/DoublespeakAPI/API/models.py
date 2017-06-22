from django.db import models


class Candidate(models.Model):
    party_name_choices = (
        ('Democrat', 'Democrat'),
        ('Republican', 'Republican'),
    )
    election_year_choices = (
        ('1932', '1932'),
        ('1960', '1960'),
        ('1980', '1980'),
        ('2004', '2004'),
        ('2008', '2008'),
        ('2016', '2016'),
    )
    candidate_name = models.CharField(max_length=50)
    party_name = models.CharField(max_length=15, null=True, choices=party_name_choices)
    election_year = models.CharField(max_length=15, null=True, choices=election_year_choices)
    most_used_words = models.TextField()
    short_bio = models.TextField()

    def __str__(self):
        return self.candidate_name


class Sentiment(models.Model):
    candidate = models.ForeignKey(Candidate)
    positive_sentiment = models.IntegerField()
    negative_sentiment = models.IntegerField()
    sentiment_confidence = models.DecimalField(max_digits=4, decimal_places=2)


class WatsonEmotionalTone(models.Model):
    candidate = models.ForeignKey(Candidate)
    anger_tone = models.DecimalField(max_digits=4, decimal_places=2)
    disgust_tone = models.DecimalField(max_digits=4, decimal_places=2)
    fear_tone = models.DecimalField(max_digits=4, decimal_places=2)
    joy_tone = models.DecimalField(max_digits=4, decimal_places=2)
    sadness_tone = models.DecimalField(max_digits=4, decimal_places=2)


class WatsonPersonalityTone(models.Model):
    Candidate = models.ForeignKey(Candidate)
    openness_tone = models.DecimalField(max_digits=4, decimal_places=2)
    conscientiousness_tone = models.DecimalField(max_digits=4, decimal_places=2)
    extraversion_tone = models.DecimalField(max_digits=4, decimal_places=2)
    agreeableness_tone = models.DecimalField(max_digits=4, decimal_places=2)
    emotional_range_tone = models.DecimalField(max_digits=4, decimal_places=2)
