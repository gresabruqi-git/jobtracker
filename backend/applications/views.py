from django.db.models import Count
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import JobApplication
from .serializers import JobApplicationSerializer


class JobApplicationListCreateView(generics.ListCreateAPIView):
    serializer_class = JobApplicationSerializer

    def get_queryset(self):
        qs = self.request.user.applications.all()
        status_param = self.request.query_params.get('status')
        if status_param:
            qs = qs.filter(status=status_param)
        search = self.request.query_params.get('search')
        if search:
            qs = qs.filter(company_name__icontains=search.strip())
        return qs.order_by('-date_applied', '-id')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class JobApplicationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobApplicationSerializer

    def get_queryset(self):
        return self.request.user.applications.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    user = request.user
    total = user.applications.count()
    by_status = {value: 0 for value, _ in JobApplication.Status.choices}
    for row in user.applications.values('status').annotate(c=Count('id')):
        by_status[row['status']] = row['c']
    return Response({
        'total': total,
        'by_status': by_status,
    })
