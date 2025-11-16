# HTTPS Deployment Configuration Guide

This document provides instructions for configuring HTTPS and secure deployment for the Django application.

## Production Settings Configuration

### 1. Update Django Settings for Production

In `LibraryProject/settings.py`, update the following settings for production:

```python
# Production Security Settings
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# HTTPS Enforcement
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Secure Cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

# HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Additional Security Headers
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
```

## 2. Nginx Configuration Example

Create or update your Nginx configuration file:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    # SSL Configuration
    ssl_certificate /path/to/your/certificate.crt;
    ssl_certificate_key /path/to/your/private.key;
    
    # SSL Security Settings
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;

    # Security Headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    add_header X-Content-Type-Options nosniff always;
    add_header X-Frame-Options DENY always;
    add_header X-XSS-Protection "1; mode=block" always;

    # Static files
    location /static/ {
        alias /path/to/your/static/files/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Media files
    location /media/ {
        alias /path/to/your/media/files/;
        expires 1y;
        add_header Cache-Control "public";
    }

    # Django application
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 3. Apache Configuration Example

If using Apache, create or update your virtual host configuration:

```apache
<VirtualHost *:80>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com
    Redirect permanent / https://yourdomain.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com

    # SSL Configuration
    SSLEngine on
    SSLCertificateFile /path/to/your/certificate.crt
    SSLCertificateKeyFile /path/to/your/private.key
    SSLCertificateChainFile /path/to/your/chain.crt

    # SSL Security Settings
    SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1
    SSLCipherSuite ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305
    SSLHonorCipherOrder off
    SSLSessionTickets off

    # Security Headers
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
    Header always set X-Content-Type-Options nosniff
    Header always set X-Frame-Options DENY
    Header always set X-XSS-Protection "1; mode=block"

    # Static files
    Alias /static/ /path/to/your/static/files/
    <Directory /path/to/your/static/files/>
        Require all granted
        ExpiresActive On
        ExpiresDefault "access plus 1 year"
    </Directory>

    # Media files
    Alias /media/ /path/to/your/media/files/
    <Directory /path/to/your/media/files/>
        Require all granted
        ExpiresActive On
        ExpiresDefault "access plus 1 year"
    </Directory>

    # Django application
    ProxyPass /static/ !
    ProxyPass /media/ !
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/
    ProxyPreserveHost On
    ProxyAddHeaders On
</VirtualHost>
```

## 4. SSL Certificate Setup

### Using Let's Encrypt (Recommended)

1. **Install Certbot**:
   ```bash
   # Ubuntu/Debian
   sudo apt install certbot python3-certbot-nginx
   
   # CentOS/RHEL
   sudo yum install certbot python3-certbot-nginx
   ```

2. **Obtain Certificate**:
   ```bash
   sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
   ```

3. **Auto-renewal Setup**:
   ```bash
   sudo crontab -e
   # Add this line:
   0 12 * * * /usr/bin/certbot renew --quiet
   ```

### Using Commercial SSL Certificate

1. Generate a Certificate Signing Request (CSR)
2. Purchase SSL certificate from a trusted CA
3. Install the certificate files on your server
4. Update web server configuration with certificate paths

## 5. Environment Variables for Production

Create a `.env` file or use environment variables:

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost/dbname

# Security
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# SSL Settings
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## 6. Deployment Checklist

### Pre-deployment
- [ ] Update `settings.py` with production values
- [ ] Set up SSL certificates
- [ ] Configure web server (Nginx/Apache)
- [ ] Set up database (PostgreSQL recommended for production)
- [ ] Configure static file serving
- [ ] Set up media file handling

### Security Verification
- [ ] Test HTTPS redirect (HTTP → HTTPS)
- [ ] Verify SSL certificate validity
- [ ] Check security headers using tools like:
  - [SSL Labs SSL Test](https://www.ssllabs.com/ssltest/)
  - [Security Headers](https://securityheaders.com/)
- [ ] Test HSTS functionality
- [ ] Verify CSP headers are working
- [ ] Test permission-based access control

### Post-deployment
- [ ] Monitor SSL certificate expiration
- [ ] Set up automated certificate renewal
- [ ] Configure logging and monitoring
- [ ] Regular security updates
- [ ] Backup and recovery procedures

## 7. Security Testing Commands

### Test HTTPS Configuration
```bash
# Test SSL certificate
openssl s_client -connect yourdomain.com:443 -servername yourdomain.com

# Check security headers
curl -I https://yourdomain.com

# Test HSTS
curl -I https://yourdomain.com | grep -i strict-transport-security
```

### Test Django Security
```bash
# Run Django security check
python manage.py check --deploy

# Test with Django security middleware
python manage.py runserver --settings=LibraryProject.settings_production
```

## 8. Monitoring and Maintenance

### SSL Certificate Monitoring
- Set up alerts for certificate expiration
- Monitor certificate chain validity
- Regular security scans

### Application Security
- Regular dependency updates
- Security patch management
- Log monitoring for suspicious activity
- Regular penetration testing

This deployment configuration ensures that your Django application follows security best practices and provides secure HTTPS communication for all users.
