from rest_framework import serializers

from .models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = (
            'id',
            'company_name',
            'position',
            'date_applied',
            'status',
            'notes',
        )
        read_only_fields = ('id',)
