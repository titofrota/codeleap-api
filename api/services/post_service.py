from api.models import Post

class PostService:
    @staticmethod
    def create_post(data):
        return Post.objects.create(**data)
    
    @staticmethod
    def update_post(id, data):
        return Post.objects.filter(id=id).update(**data)
    
    @staticmethod
    def delete_post(id):
        return Post.objects.filter(id=id).delete()
    
    @staticmethod
    def get_post_by_id(id):
        return Post.objects.get(id=id)
    
    @staticmethod
    def get_all_posts():
        return Post.objects.all()
    
