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
        
        
# class TicketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ticket
#         fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(
    queryset= UserDetail.objects.all(),
    slug_field='email'  # Now using email instead of ID
)
    class Meta:
        model = ticket
        fields = ['id', 'ticket_number', 'ticket_type', 'ticket_category', 'description', 'budget', 'file_upload' ,'estimated_completion', 'created_on' , 'modified_on', 'created_by']
        # fields = '__all__'
