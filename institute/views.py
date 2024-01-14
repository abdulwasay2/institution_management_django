from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from .serializers import CourseSerializer, Course


class CoursePublicView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.query_params:
            institute_id = self.request.query_params.get("institute_id")
            return Course.objects.filter(institute_id=institute_id)
        return Course.objects.all()