from datetime import timedelta

from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from back_end_developer_q1.models import NavigationRecord


def last_points(request):
    distinct = NavigationRecord.objects.order_by('vehicle', '-datetime').distinct('vehicle')
    results = NavigationRecord.objects.filter(id__in=distinct).order_by('-datetime').annotate(
        vehicle_plate=F('vehicle__plate')).values('latitude', 'longitude', 'vehicle_plate', 'datetime')
    results = JsonResponse(list(results), safe=False)

    return results


def get_last_points(request):
    time_range_48hrs = timezone.now() - timedelta(hours=48)
    results = NavigationRecord.objects.filter(datetime__gte=time_range_48hrs).order_by('-datetime').annotate(
        vehicle_plate=F('vehicle__plate')).values('latitude', 'longitude', 'vehicle_plate', 'datetime')
    results = JsonResponse(list(results), safe=False)

    return results
