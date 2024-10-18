from django.db import models
import uuid

# Create your models here.
class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="asset name", max_length=100)
    description = models.TextField(verbose_name="asset description", max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # default representation
    def __str__(self):
        return self.name

    # representation for debugging
    def __repr__(self):
        return f"Asset(name='{self.name}', description='{self.description}', created_at={self.created_at})"


# Employee


# Lending