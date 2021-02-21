# -*- coding:utf-8 -*-
"""
@author: 'teddy'
@file:serializers.py
@time: 2021/1/16 18:23
"""
from rest_framework import serializers

import accountapp.models

class AccountSerializer(serializers.ModelSerializer):
    # mount = serializers.IntegerField()
    class Meta:
        model = accountapp.models.Account
        fields = '__all__'