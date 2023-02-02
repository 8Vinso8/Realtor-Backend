# Realtor-Backend

Backend for Realtor Agency "Teplotrassa"

## API endpoints

- **`api/admin/`** - Admin panel

## Users 
- api/users/ - list of users, or create new
  - api/users/**id** - concrete user
   - id
   - url
   - username
   - email
   - phone
   - favorite_adverts - array of adverts (see below)
   - is_realtor - if realtor - then true, else - false


## Adverts
- api/adverts/ - list of adverts
- api/adverts/**id** - concrete advert
  - id
  - url
  - is_favorite - if user not logined - false always
  - owner - link for owner user
  - advert_type (Либо 'Квартира', либо 'Дом', либо 'Земельный участок')
  - city
  - street
  - latitude
  - longitude
  - address
  - floor - если это квартира то этаж, если это дом то кол-во этажей, а если участок то null :)
  - description
  - date - YYYY-MM-DD
  - image - array of image links
  - phone - cannot be changed(because user's field)
  - title 
  - GET Parameters(?)
    - filtering by fields | example: ?id=1&date=2022-10-10
    - favorite - if not null then adds/remove advert to favorite


- **`api/chat/`** -- Get all mesages
  - **`api/chat/<pk:int>`** mesage detail
- **`api/auth/`** - all authentication related endpoints
  - **`api/auth/token/login/`** - get auth token
  - **`api/auth/token/logout/`** - disable auth token (logout)
