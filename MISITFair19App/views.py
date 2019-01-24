from django.shortcuts import render
from django.shortcuts import render
from django.conf import settings
import django_filters
from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route, list_route
from rest_framework.views import APIView
import os
from rest_framework.response import Response
from datetime import datetime
from .models import *
from rest_framework.reverse import reverse
from .serializer import RegisteredStgSerializer
from rest_framework.renderers import JSONRenderer
from django.core.files.storage import FileSystemStorage
import json
import datetime
import cv2
import argparse
import numpy as np
from .library.DetectObjectYOLO import *
from .library.PushToPowerBI import *
from datetime import datetime
from gtts import gTTS
from time import sleep


DetectedObjects = {}
Domain = "http://mis.digital:3006/"

class PiImageSave(viewsets.ModelViewSet):
    queryset = District.objects.all()
    role_class = RegisteredStgSerializer

    def create(self, request):
        print(request.build_absolute_uri)
        #myobj = gTTS(text='Hello Shakil, Akash, Kallol Vai', lang='en', slow=False)
        #myobj.save("PiImage/welcome_test.mp3")
        #os.system("mpg321 PiImage/welcome_test.mp3")
        dt = str(datetime.now())
        _datetime = datetime.now()
        datetime_str = _datetime.strftime("%Y-%m-%d-%H-%M-%S")
        fs = FileSystemStorage(location=settings.MEDIA_URL+'Fair/')
        productImage1 = request.FILES['uploaded_file']

        fs.save(datetime_str + "-" + productImage1.name, productImage1)

        response = {'StatusCode': '200', 'StatuasMessage': 'Success'}

        filename = Domain + 'PiImage/Fair/' + datetime_str + "-" + productImage1.name
        #output_filename, detected_objects = DetectFacesInImage('', filename, datetime_str + "-" + productImage1.name)
        #print(detected_objects)

        # if detected_objects['AnisUdDowla'] == 1:
        #     PlayMusic("PiImage/AnisUdDowla.mp3")
        #
        # elif detected_objects['DrArifDowla'] == 1:
        #     PlayMusic("PiImage/DrArifDowla.mp3")
        #
        # elif detected_objects['ShusmitaAnis'] == 1:
        #     PlayMusic("PiImage/ShusmitaAnis.mp3")
        #
        # elif detected_objects['MMohibuzZaman'] == 1:
        #     PlayMusic("PiImage/MMohibuzZaman.mp3")
        #
        # elif detected_objects['DrAnsary'] == 1:
        #     PlayMusic("PiImage/DrAnsary.mp3")
        #
        # else:
        #     PlayMusic("PiImage/General.mp3")

        client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id='AKIAICT7NC42AXAYHSIQ',
                              aws_secret_access_key='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')
        print(filename)
        #response = requests.get('http://mis.digital:3006/PiImage/Fair/' + datetime_str + "-" + productImage1.name)
        #response_content = response.content
		#io.open(file_path_dest,"r",encoding='ISO-8859-1')
        #rekognition_response = client.detect_faces(Image={'Bytes': response_content}, Attributes=['ALL'])

        # if rekognition_response is not None and len(rekognition_response['FaceDetails']) > 0:
        #     aws_rekog = rekognition_response['FaceDetails'][0]
        #     calm = aws_rekog['Emotions'][2]['Confidence']
        #     happy = aws_rekog['Emotions'][3]['Confidence']
        #     surprised = aws_rekog['Emotions'][4]['Confidence']
        #     sad = aws_rekog['Emotions'][5]['Confidence']
        #
        #     fairdata = FairEntryPoint(ImagePath=filename,
        #                         Gender=aws_rekog['Gender']['Value'], AgeLow=aws_rekog['AgeRange']['Low'],
        #                         AgeHigh=aws_rekog['AgeRange']['High'], EmotionCalm=float("{0:.2f}".format(calm)),
        #                           EmotionHappy=float("{0:.2f}".format(happy)),
        #                           EmotionSurprised=float("{0:.2f}".format(surprised)),
        #                           EmotionSad=float("{0:.2f}".format(sad)),
        #                           EntryDate = datetime.now())
        # else:
        fairdata = FairEntryPoint(ImagePath=filename,
                                  Gender='-', AgeLow=0,
                                  AgeHigh=0, EmotionCalm=0,
                                  EmotionHappy=0,
                                  EmotionSurprised=0,
                                  EmotionSad=0,
                                  EntryDate=datetime.now())

        fairdata.save(using='ACIFair')
        PublishToPowerBI(fairdata)
        return Response(response, content_type="application/json")





