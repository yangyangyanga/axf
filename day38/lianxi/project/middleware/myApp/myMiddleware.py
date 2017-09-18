from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("process_request 中get参数为 = ", request.GET.get('a'))

    def process_view(self, request, view_func,view_args,view_kwargs):
        print("process_view 中get参数为 = ", request.GET.get('b'), view_func)

    def process_template_response(self,request,response):
        print("process_template_response 中get参数为 = ", request.GET.get('c'))
