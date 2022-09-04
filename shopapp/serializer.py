
class GroupSerializer(serializers.ModelSerializer): #serializers.ModelSerializer
    class Meta:
        model = Group
        fields = ['url', 'name']
