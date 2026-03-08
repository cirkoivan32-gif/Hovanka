if (Test-Path ".env.local") {
    Get-Content ".env.local" | ForEach-Object {
        if ($_ -and -not $_.StartsWith("#")) {
            $name, $value = $_ -split "=", 2
            if ($name -and $value) {
                Set-Item -Path "Env:$name" -Value $value
            }
        }
    }
}

python manage.py migrate
python manage.py ensure_admin
python manage.py runserver 127.0.0.1:8000
