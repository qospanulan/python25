from blog.services.blog_service import BlogService
from blog.services.post_service import PostService

SERVICES = {}

"""
{
    "post_service": PostService (obj)
}

"""

def get_service(service_name: str):

    service = SERVICES.get(service_name)

    if not service:
        if service_name == "post_service":
            service = PostService()
        elif service_name == "blog_service":
            service = BlogService()
        else:
            raise Exception(f"service not found by name {service_name}")

        SERVICES[service_name] = service

    return service
