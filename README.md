# Simple creator of QR codes for Gazebo

### 1. Install requirements

```bash
>>> pip install -r requirements.txt
```

### 2. Run script

```bash
>>> python3 make_qr.py

Gazebo model name: model_name
QR encoded text: encoded
Width of QR code (empty for 0.33):
Successfully created!
```

### 3. Add to Gazebo

Move folder `output/qrmodel_name` to any Gazebo models folder, for example, `/home/user/model_editor_models/`
