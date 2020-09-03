# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['dist/predict.py'],
             pathex=[],
             binaries=[],
             datas=[
                ('C:/Users/conta/AppData/Local/Programs/Python/Python37/Lib/site-packages/astor/VERSION', './astor'),
                ('C:/Users/conta/AppData/Local/Programs/Python/Python37/Lib/site-packages/tensorflow/lite/experimental/microfrontend/python/ops/_audio_microfrontend_op.so','tensorflow/lite/experimental/microfrontend/python/ops/')
             ],
             hiddenimports=["tensorflow.python.keras.engine.base_layer_v1", "tensorflow.python.ops.numpy_ops"],
             hookspath=["hooks"],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='predict',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='predict1',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
