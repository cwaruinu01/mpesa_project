from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . credentials import MpesaAccessToken, LipanaMpesaPpassword

from django.shortcuts import render,redirect
from django.contrib import messages


