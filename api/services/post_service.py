from api.models import Post

class PostService:
    @staticmethod
    def create(data):
        return Post.objects.create(**data)
    
    @staticmethod
    def update(id, data):
        return Post.objects.filter(id=id).update(**data)
    
    @staticmethod
    def delete(id):
        return Post.objects.filter(id=id).delete()
    
    @staticmethod
    def get_post(id):
        return Post.objects.get(id=id)
    
    @staticmethod
    def get_all():
        return Post.objects.all()
    
