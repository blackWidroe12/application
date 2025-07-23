# Create directories
$folders = @(
    "config\settings",
    "infrastructure\migrations",
    "infrastructure\models",
    "infrastructure\api",
    "utils"
)
foreach ($folder in $folders) {
    New-Item -Path "c:\Users\HP\mutare-rdc-backend\$folder" -ItemType Directory -Force
}

# Create files
$files = @(
    "config\settings\base.py",
    "config\settings\development.py",
    "config\settings\production.py",
    "config\urls.py",
    "config\asgi.py",
    "infrastructure\models\__init__.py",
    "infrastructure\models\core.py",
    "infrastructure\models\spatial.py",
    "infrastructure\models\user.py",
    "infrastructure\api\serializers.py",
    "infrastructure\api\viewsets.py",
    "infrastructure\api\filters.py",
    "infrastructure\api\routers.py",
    "infrastructure\tasks.py",
    "infrastructure\signals.py",
    "infrastructure\admin.py",
    "utils\gis.py",
    "utils\permissions.py",
    "utils\offline.py",
    "manage.py",
    "requirements.txt",
    "docker-compose.yml"
)
foreach ($file in $files) {
    New-Item -Path "c:\Users\HP\mutare-rdc-backend\$file" -ItemType File -Force
}
