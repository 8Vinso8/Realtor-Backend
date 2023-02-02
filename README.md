# Realtor-Backend

Backend for Realtor Agency "Teplotrassa"

## API endpoints

- **`api/admin/`** - Admin panel
- **`api/users/`** - Get all users / create new one
  - **`api/users/<pk:int>/`** - user detail
- **`api/adverts/`** - Get all adverts / create new one
  - **`api/adverts/<pk:int>`** - advert detail
- **`api/chat/`** -- Get all mesages
  - **`api/chat/<pk:int>`** mesage detail
- **`api/auth/`** - all authentication related endpoints
  - **`api/auth/token/login/`** - get auth token
  - **`api/auth/token/logout/`** - disable auth token (logout)
