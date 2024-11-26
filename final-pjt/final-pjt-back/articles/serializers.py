from .models import Article, Comment, DepositComment, SavingComment
from rest_framework import serializers
from django.contrib.auth import get_user_model
from products.models import DepositProducts, SavingProducts

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# 게시글 조회/생성
class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'user')



# 댓글 조회/생성
class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    user = UserSerializer(read_only=True)
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'article', 'content', 'user')



# 단일 게시글 조회
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source="comment_set.count", read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


# 상품 후기 조회/생성 - deposit
class DepositCommentSerializer(serializers.ModelSerializer):
    class DepositProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = DepositProducts
            fields = ('fin_prdt_cd',)

    user = UserSerializer(read_only=True)
    deposit_products = DepositProductSerializer(read_only=True)

    class Meta:
        model = DepositComment
        fields = ('id', 'deposit_products', 'content', 'user')

# 상품 후기 조회/생성 - saving
class SavingCommentSerializer(serializers.ModelSerializer):
    class SavingProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = SavingProducts
            fields = ('fin_prdt_cd',)

    user = UserSerializer(read_only=True)
    saving_products = SavingProductSerializer(read_only=True)

    class Meta:
        model = SavingComment
        fields = ('id', 'saving_products', 'content', 'user')
