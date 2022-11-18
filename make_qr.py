import pathlib
import pyqrcode


MODEL_NAME = input('Gazebo model name: ')
TEXT = input('QR encoded text: ')
WIDTH = input('Width of QR code (empty for 0.33): ')
try:
    WIDTH = float(WIDTH)
except ValueError:
    WIDTH = 0.33
MODEL_DIR = pathlib.Path(__file__).resolve().parent / 'output' / f'qr{MODEL_NAME}'
assert not MODEL_DIR.exists(), (
    f'This model ({MODEL_NAME}) is also created. Remove directory `output/qr{MODEL_NAME}` before!'
)
(MODEL_DIR / 'materials' / 'textures').mkdir(parents=True)
(MODEL_DIR / 'materials' / 'scripts').mkdir(parents=True)
pyqrcode.create(TEXT).png(MODEL_DIR / 'materials' / 'textures' / 'model.png', scale=1)
with open(MODEL_DIR / 'model.config', 'x') as config_file:
    config_file.write(
        '<?xml version="1.0"?>'
        '<model>'
        f'<name>qr{MODEL_NAME}</name>'
        '<version>1.0</version><sdf version="1.5">model.sdf</sdf>'
        '<author><name>QR code Generator script</name><email>me@mkme.ml</email></author>'
        f'<description>qr{MODEL_NAME}</description>'
        '</model>'
    )
with open(MODEL_DIR / 'model.sdf', 'x') as model_file:
    model_file.write(
        '<?xml version="1.0"?>'
        '<sdf version="1.5">'
        f'<model name="qr{MODEL_NAME}">'
        '<static>true</static>'
        f'<link name="qr{MODEL_NAME}_link">'
        '<pose>0 0 1e-3 0 0 1.5707963267948966</pose>'
        f'<visual name="visual_qr{MODEL_NAME}">'
        '<cast_shadows>false</cast_shadows>'
        f'<geometry><box><size>{WIDTH} {WIDTH} 1e-3</size></box></geometry>'
        '<material><script>'
        f'<uri>model://qr{MODEL_NAME}/materials/scripts</uri>'
        f'<uri>model://qr{MODEL_NAME}/materials/textures</uri>'
        f'<name>qr/qr{MODEL_NAME}</name>'
        '</script></material></visual></link></model></sdf>'
    )
with open(MODEL_DIR / 'materials' / 'scripts' / 'model.material', 'x') as material_file:
    material_file.write(
        'material qr/qr{MODEL_NAME}\n'
        '{\n'
        '\ttechnique\n'
        '\t{\n'
        '\t\tpass\n'
        '\t\t{\n'
        '\t\t\ttexture_unit\n'
        '\t\t\t{\n'
        '\t\t\t\ttexture model.png\n'
        '\t\t\t\tfiltering none\n'
        '\t\t\t\tscale 1.0 1.0\n'
        '\t\t\t}\n'
        '\t\t}\n'
        '\t}\n'
        '}'
    )
print('Successfully created!')
