from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date
from django.contrib.auth.models import AnonymousUser
from .models import JobApplication
from .serializers import JobApplicationSerializer
from django.utils import timezone

class JobApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ['status']
    search_fields = ['company_name', 'job_title']
    ordering_fields = ['applied_date', 'follow_up_date']
    ordering = ['-applied_date']

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return JobApplication.objects.none()

        return JobApplication.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def reminders_today(self, request):
        today = timezone.localdate()
        jobs = self.get_queryset().filter(follow_up_date=today)
        serializer = self.get_serializer(jobs, many=True)
        return Response(serializer.data)
