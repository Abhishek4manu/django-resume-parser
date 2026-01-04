from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .services.file_handler import save_temp_file, delete_file
from .services.text_extractor import extract_text
from .services.parser_engine import parse_resume_data


@csrf_exempt
def upload_resume(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    file = request.FILES.get("resume")
    if not file:
        return JsonResponse({"error": "No file uploaded"}, status=400)

    try:
        path = save_temp_file(file)
        text = extract_text(path)
        data = parse_resume_data(text)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    finally:
        delete_file(path)

    return JsonResponse({
        "success": True,
        "data": data
    })

