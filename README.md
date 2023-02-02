# Realtor-Backend

Backend for Realtor Agency "Teplotrassa"

## API endpoints

- **`api/admin/`** - Admin panel
- **`api/users/`** - Get all users / create new one
  - **`api/users/<pk:int>/`** - user detail
## Adverts
- api/adverts/ - list of adverts
- api/adverts/**id** - concrete advert
  - id
  - url
  - owner - link for owner user
  - address
  - description
  - date - YYYY-MM-DD
  - image - array of image links
  - phone - cannot be changed(because user's field)
  - title 
  - GET Parameters(?)
    - filtering by fields | example: ?id=1&date=2022-10-10
    - favorite - if not null then adds/remove advert to favorite


  - **`api/adverts/<pk:int>`** - advert detail
- **`api/chat/`** -- Get all mesages
  - **`api/chat/<pk:int>`** mesage detail
- **`api/auth/`** - all authentication related endpoints
  - **`api/auth/token/login/`** - get auth token
  - **`api/auth/token/logout/`** - disable auth token (logout)
