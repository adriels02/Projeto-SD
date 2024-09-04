from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def send_notification(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get('email')
        message = data.get('message')

        # Validate email and message
        if not email or not message:
            return JsonResponse({"error": "Email and message are required."}, status=400)

        # Send Email
        try:
            send_mail(
                'Welcome!',
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            return JsonResponse({"error": f"Failed to send email: {str(e)}"}, status=500)

        return JsonResponse({"status": "success", "message": "Email notification sent successfully."})

    return JsonResponse({"error": "Invalid request method."}, status=400)
