from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from .serializers import StudentRollNumberSlipSerializer, StudentRollNumberSlip


class StudentRollNumberSlipView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = StudentRollNumberSlipSerializer

    def get_queryset(self):
        if self.request.query_params:
            cnic_num = self.request.query_params.get("cnic_num")
            course_name = self.request.query_params.get("course_name")
            return StudentRollNumberSlip.objects.filter(
                student__cnic_number=cnic_num, course__name=course_name 
            )
        return StudentRollNumberSlip.objects.none()