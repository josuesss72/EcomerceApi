# import io
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# from fastapi import UploadFile
# from PIL import Image

# path_credentials = 'C:/Users/Jafeth Sarmiento/Desktop/DESKTOP/JOSUE/BACKEND/PYTHON/FASTAPI/USERS/app/crendentials_module.json'

# def loginDrive():
#     gauth = GoogleAuth()
#     gauth.LoadCredentialsFile(path_credentials)

#     if gauth.access_token_expired:
#         gauth.Refresh()
#         gauth.SaveCredentialsFile(path_credentials)
#     else:
#         gauth.Authorize()
#     return GoogleDrive(gauth)

# def imgBytes(img_file: UploadFile):
#     # Convertir el archivo de imagen a bytes
#     image_bytes = io.BytesIO(img_file.file.read())
#     image = Image.open(image_bytes)
#     return image

# def uploadDriveImage(img_file: UploadFile, file_name: str):
#     try:
#         drive = loginDrive()
#         id_folder = '1aiEcZ9BS6uEr9TG77mZeMelLkYBvNiyb'

#         file_drive = drive.CreateFile({'title': file_name,'parents': [{'kind': 'drive#fileLink', 'id': id_folder}]}) 

#         # Convertir el archivo de imagen a bytes y guardarlo temporalmente
#         image = imgBytes(img_file)
#         image.save('../' + file_name + '.png')
#         image.close()

#         # Subir el archivo a Google Drive
#         file_drive.SetContentFile('../' + file_name + '.png')
#         file_drive.Upload()

#         #Hacer el archivo puplico
#         file_drive.InsertPermission({
#             'type': 'anyone',
#             'value': 'anyone',
#             'role': 'reader'
#         })

#         # Obtener el url publico del archivo
#         id_file = file_drive['embedLink']

#         return id_file
#     except Exception as e:
#         print('Error =>', str(e))
#         return False