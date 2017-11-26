from rest_framework import serializers
class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('id', 'text')

class FreelancerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('user','rating','url','photosrc','ratephr','bodytxt','country')