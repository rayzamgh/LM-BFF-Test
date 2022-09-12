from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  


upload_file_list = ['result/tmp/smsav-40/pytorch_model.bin',
                    'result/tmp/smsav-40/special_tokens_map.json',
                    'result/tmp/smsav-40/data_args.bin',
                    'result/tmp/smsav-40/model_args.bin',
                    'result/tmp/smsav-40/sentencepiece.bpe.model',
                    'result/tmp/smsav-40/training_args.bin',
                    'result/tmp/emotv-40/pytorch_model.bin',
                    'result/tmp/emotv-40/special_tokens_map.json',
                    'result/tmp/emotv-40/data_args.bin',
                    'result/tmp/emotv-40/model_args.bin',
                    'result/tmp/emotv-40/sentencepiece.bpe.model',
                    'result/tmp/emotv-40/training_args.bin']

for upload_file in upload_file_list:
	gfile = drive.CreateFile({
            'parents': [{'id': '1-64z_V4UkcmCITXre3dUpqOL8pmTcDuH'}],
            'title': upload_file}
        )
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.