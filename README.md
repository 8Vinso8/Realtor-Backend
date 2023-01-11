# Realtor-Backend

Backend for Realtor Agency "Teplotrassa"

## API endpoints

- **`api/admin/`** - Admin panel
- **`api/users/`** - Get all users / create new one
  - **`api/users/<pk:int>/`** - to work with one user
- **`api/adverts/`** - Get all adverts / create new one
  - **`api/adverts/<pk:int>`** - to work with one advert
- **`api/auth/`** - all authentication related endpoints
  - api/auth/ ^users/$ [name='user-list']
  - api/auth/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
  - api/auth/ ^users/activation/$ [name='user-activation']
  - api/auth/ ^users/activation\.(?P<format>[a-z0-9]+)/?$ [name='user-activation']
  - api/auth/ ^users/me/$ [name='user-me']
  - api/auth/ ^users/me\.(?P<format>[a-z0-9]+)/?$ [name='user-me']
  - api/auth/ ^users/resend_activation/$ [name='user-resend-activation']
  - api/auth/ ^users/resend_activation\.(?P<format>[a-z0-9]+)/?$ [name='user-resend-activation']
  - api/auth/ ^users/reset_password/$ [name='user-reset-password']
  - api/auth/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password']
  - api/auth/ ^users/reset_password_confirm/$ [name='user-reset-password-confirm']
  - api/auth/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password-confirm']
  - api/auth/ ^users/reset_username/$ [name='user-reset-username']
  - api/auth/ ^users/reset_username\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username']
  - api/auth/ ^users/reset_username_confirm/$ [name='user-reset-username-confirm']
  - api/auth/ ^users/reset_username_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username-confirm']
  - api/auth/ ^users/set_password/$ [name='user-set-password']
  - api/auth/ ^users/set_password\.(?P<format>[a-z0-9]+)/?$ [name='user-set-password']
  - api/auth/ ^users/set_username/$ [name='user-set-username']
  - api/auth/ ^users/set_username\.(?P<format>[a-z0-9]+)/?$ [name='user-set-username']
  - api/auth/ ^users/(?P<id>[^/.]+)/$ [name='user-detail']
  - api/auth/ ^users/(?P<id>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
  - api/auth/ ^$ [name='api-root']
  - api/auth/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
  - api/auth/ ^token/login/?$ [name='login']
  - api/auth/ ^token/logout/?$ [name='logout']
