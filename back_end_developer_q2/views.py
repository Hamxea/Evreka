from django.http import JsonResponse
from django.shortcuts import render

from back_end_developer_q2.models import BinOperation


def collection_frequency_bin_operation(request):
    distinct = BinOperation.objects.all()
    results = [{
        "bin": str(row.bin.longitude) + "," + str(row.bin.latitude),
        "operation": row.operation.name,
        "collection_frequency": row.collection_frequency,
        "last_operation": row.last_operation
    } for row in distinct]

    results = JsonResponse(list(results), safe=False)

    return results
