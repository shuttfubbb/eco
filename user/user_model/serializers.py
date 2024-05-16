from rest_framework import serializers
from .models import User, Fullname, Account, Address

class FullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullname
        fields = ['fname', 'lname']
    
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'password']
    
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['nohouse', 'street', 'district', 'city']

class UserSerializer(serializers.ModelSerializer):
    fullname = FullnameSerializer()
    account = AccountSerializer()
    address = AddressSerializer()
    class Meta:
        model = User
        fields = ['id', 'fullname', 'account', 'address', 'email', 'mobile', 'dob', 'position']
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class UserUpdateSerializer(serializers.ModelSerializer):
    fullname = FullnameSerializer()
    address = AddressSerializer()
    class Meta:
        model = User
        fields = ['fullname', 'address', 'mobile', 'dob']
    
    def update(self, instance, validated_data):
        # Xử lý cập nhật cho fullname
        fullname_data = validated_data.pop('fullname')
        fullname_obj = instance.fullname
        for key, value in fullname_data.items():
            setattr(fullname_obj, key, value)
        fullname_obj.save()
        
        # Xử lý cập nhật cho address
        address_data = validated_data.pop('address')
        address_obj = instance.address
        for key, value in address_data.items():
            setattr(address_obj, key, value)
        address_obj.save()

        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        # Kiểm tra mật khẩu mới và mật khẩu xác nhận có trùng nhau không
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Mật khẩu mới và mật khẩu xác nhận không trùng khớp."})
        return data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True) 

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        # Lấy ra account dựa trên username và password
        try:
            account = Account.objects.get(username=username, password=password)
        except Account.DoesNotExist:
            raise serializers.ValidationError('Invalid username or password.')

        # Kiểm tra xem có user nào liên kết với account này không và user đó có hoạt động không
        user = User.objects.filter(account=account, is_active=True).first()
        if not user:
            raise serializers.ValidationError('No active user found for these credentials.')

        # Nếu tất cả các điều kiện đều thỏa mãn, trả về thông tin user
        return user

