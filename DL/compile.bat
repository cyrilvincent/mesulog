pyarmor o predict.py
pyinstaller --noconfirm predict.spec
copy mv*.dll dist\predict
md dist\predict\pytransform\platforms\windows\x86_64
copy dist\pytransform\_pytransform.dll dist\predict\pytransform\platforms\windows\x86_64
copy dist\pytransform\_pytransform.dll dist\predict

