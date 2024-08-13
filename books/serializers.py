from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price',)



    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)


        # check title if it contains only alphabatical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitobni sarlavhasi harflardan tashkil topgan bolishi kerak"
                }
             )


        # check title and author form database exitstance
        if Book.objects.filter(title =title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitobni sarlavhasi va muallifi bir xil bolgan kitobni yuklay olmaysiz"
                }
            )

        return data


    # validate_price: Bunda alohida har bitta ozgaruvchimzga qiymatni bersak buladi
    def validate_price(self, price):
        if price < 0 or price > 99999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx notugri kiritilgan"
                }
            )








