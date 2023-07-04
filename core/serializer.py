from rest_framework import serializers
from .models import User, Organization, Shelf, ShelfReadings, AlertLogs


class UserSignUpSerializer(serializers.Serializer):
    email = serializers.CharField()
    phone = serializers.CharField()
    name = serializers.CharField()
    country_code = serializers.CharField()
    role = serializers.CharField()
    profile_picture = serializers.CharField()
    organization_name = serializers.CharField()

    def create(self, validated_data):
        email = validated_data.pop("email")
        phone = validated_data.pop("phone")
        name = validated_data.pop("name")
        country_code = validated_data.pop("country_code")
        role = validated_data.pop("role")
        profile_picture = validated_data.pop("profile_picture")
        organization_name = validated_data.pop("organization_name")
        org = Organization.objects.create(name=organization_name)

        user = User.objects.create(email=email, phone=phone, name=name, country_code=country_code, role=role, profile_picture=profile_picture, organization=org)
        user.save()
        return user

        def validate_email(self, value):
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError(
                    "user with this email_id already exists")
            return value

        def validate_phone(self, attrs):
            if User.objects.filter(phone=attrs).exists():
                raise serializers.ValidationError(
                    "user with this phone number already exits")
            return attrs

