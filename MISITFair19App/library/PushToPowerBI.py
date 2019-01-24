import requests
from pygame import mixer
from datetime import datetime
import boto3

def PublishToPowerBI(object):
    API_ENDPOINT = "https://api.powerbi.com/beta/653bd3e1-36ff-4399-b0aa-f7e63a029597/datasets/2989ce29-4b55-4698-81d6-3ab7182830d3/rows?key=bJbpp%2B0uImFawmkWL%2FQuBeaHf04PYSb6Tv%2BYCRUAYkFlwiXePhsxw2bU%2FGf0UHH43JetPmNZxVQFzDyxpvG8OA%3D%3D"
    if object.Gender == 'Male':
        gender_logo = 'http://mis.digital:90/PBImages/MISITFAIR19/male.png'
    else:
        gender_logo = 'http://mis.digital:90/PBImages/MISITFAIR19/female.png'

    # if object.Emotion == 'Wow':
    #     emo_image = 'http://mis.digital:90/PBImages/MISITFAIR19/wow.png'
    # elif object.Emotion == 'Sad':
    #     emo_image = 'http://mis.digital:90/PBImages/MISITFAIR19/worst.png'

    currentDateTime = datetime.strftime(object.EntryDate, "%Y-%m-%dT%H:%M:%S%Z")
    output = '[{{ "Id": "{0}", "ImagePath": "{1}", "Gender": "{2}", "Age": "{3}", ' \
             '"Emotion-Calm": "{4}", "Emotion-Happy": "{5}", "Emotion-Surprised": "{6}", "EmotionSad": "{7}", "EntryDate": "{8}" }}]'\
            .format(object.Id, object.ImagePath, gender_logo, str(object.AgeLow) + '-' + str(object.AgeHigh),
                    object.EmotionCalm, object.EmotionHappy, object.EmotionSurprised, object.EmotionSad, currentDateTime)
    r = requests.post(url = API_ENDPOINT, data = output)


def PlayMusic(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

class AmazonServices:
    AWS_ACCESS_ID = 'AKIAICT7NC42AXAYHSIQ',
    AWS_SECRET_ACCESS_KEY = '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'
    S3FileDownloadLink = ''
    def __init__(self):
        pass

    def UploadToS3(self, bucketName, S3FileName, fileToUpload):
        try:
            print('Uploading')
            s3 = boto3.resource('s3', aws_access_key_id = 'AKIAICT7NC42AXAYHSIQ', aws_secret_access_key = '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')
            s3.Bucket(bucketName).put_object(Key=S3FileName, Body=fileToUpload)
            object_acl = s3.ObjectAcl(bucketName, S3FileName)
            response = object_acl.put(ACL='public-read')
            self.S3FileDownloadLink = 'https://s3.amazonaws.com/' + bucketName + '/' + S3FileName
            return self.S3FileDownloadLink

        except Exception as e:
            print('Exception Occured: ' + str(e))
            return 'Not Found'