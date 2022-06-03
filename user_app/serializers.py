from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):

        password = self.validated_data.get('password')
        password2 = self.validated_data.get('password2')

        if password != password2:
            raise serializers.ValidationError('p1 and p2 should be same')

        if User.objects.filter(email=self.validated_data.get('email')).exists():
            raise serializers.ValidationError('email already exists!')

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account