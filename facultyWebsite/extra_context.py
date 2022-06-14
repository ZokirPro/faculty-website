from index.models import *
def context(request):
        return {
            'MainInfos': MainInfos.objects.first(),
            "e_resources":ResourceCategory.objects.all()
        }