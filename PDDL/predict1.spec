# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['predict.py'],
             pathex=['C:\\Users\\conta\\CVC\\ATP\\Mesulog\\KerasExeStrategies'],
             binaries=[],
             datas=[('venv/Lib/site-packages/astor/VERSION', './astor')],
             hiddenimports=['astor'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='predict',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
