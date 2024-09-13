from rest_framework import serializers
from user.models import UserDetail, ticket

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required = True)

    class Meta:
        model = UserDetail
        fields = ['id', 'username', 'first_name', 'last_name', 'phone', 'email', 'street_address', 'province', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')  # Extract password
        user = UserDetail(**validated_data)        # Create the user instance
        user.set_password(password)                # Hash the password
        user.save()                                # Save the user instance
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
        
        
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket
        fields = '__all__'
        read_only_fields = ['created_by','created_on']

# class TicketSerializer(serializers.ModelSerializer):
#     created_by = serializers.SlugRelatedField(
#     queryset= UserDetail.objects.all(),
#     slug_field='email'  # Now using email instead of ID
# )
#     class Meta:
#         model = ticket
#         fields = ['id', 'ticket_number', 'ticket_type', 'ticket_category', 
#                   'description', 'budget', 'file_upload' ,'estimated_completion', 
#                   'created_on' , 'modified_on', 'created_by','ticket_state','comments',]
#         # fields = '__all__'


# class UserSignupSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, min_length=8)
    
#     class Meta:
#         model = UserDetail
#         # fields = '__all__'
#         fields = ['username', 'password']

#     def create(self, validated_data):
#         # Create a new user instance
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             password=validated_data['password'],
#             # street_address=validated_data['street_address'],
#             # city=validated_data['city'],
#             # province=validated_data['province']
#         )
#         return user