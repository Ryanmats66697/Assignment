from django.db import models

class Rule(models.Model):
    """Model to store rules for the rule engine."""
    rule_string = models.CharField(max_length=255)

    def __str__(self):
        return self.rule_string

class UserProfile(models.Model):
    """Model to store user profiles with attributes for evaluation."""
    age = models.PositiveIntegerField()  # Ensure age cannot be negative
    income = models.FloatField()          # User income, allowing decimal values
    department = models.CharField(max_length=100)  # User department

    def __str__(self):
        return f"User(age={self.age}, income={self.income}, department={self.department})"

    class Meta:
        verbose_name_plural = "User Profiles"  # Plural name in admin panel
