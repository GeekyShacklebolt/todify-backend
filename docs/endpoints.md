# Todify's API endpoints

# Authentication

## Register a user

```json
POST /api/auth/register
```

   Column    |       Type        | Nullable | Optional | Description 
-------------|-------------------|----------|----------|-------------
 username    | `string`          | not null | No       | Username of the User 
 email       | `string`          | not null | No       | Email address of the User 
 password    | `string`          | not null | No       | Password for the User
                                            
__Request__                                

```json
{
  "username": "GeekyShacklebolt",
  "email": "shiva+1@fueled.com",
  "password": "VerySafePassWord"
}
```

__Response__

Status: 201 Created

```json
{
    "id": "2a8dc6d6-d7d2-4f53-8e89-8f54951fbf14",
    "username": "GeekyShacklebolt",
    "email": "shiva+1@fueled.com",
    "first_name": "",
    "last_name": "",
    "avatar": null,
    "last_login": null,
    "created_at": "2020-11-04T15:37:37.589979Z"
}
```

# Current User Actions

## Get Profile

**User Schema**:

   Column    |       Type        | Nullable | Description 
-------------|-------------------|----------|-------------
 id          | `uuid`            | not null | UUID for the `UserObject`
 first_name  | `string`          | not null | First name of the User 
 last_name   | `string`          | not null | Last name of the User 
 email       | `string`          | not null | Email address of the User 
 username    | `string`          | not null | Username of the User 
 created_at  | `datetime`        | not null | Time at which the `UserObject` created 
 last_login  | `datetime`        |          | Time at which the user last logged in 
 avatar      | `string`          |          | URL of the image uploaded by the User 

```json
GET /api/me (requires authentication)
```

__Response__

Status: 200 OK

```json
{
    "id": "2a8dc6d6-d7d2-4f53-8e89-8f54951fbf14",
    "username": "GeekyShacklebolt",
    "email": "shiva+1@fueled.com",
    "first_name": "",
    "last_name": "",
    "avatar": null,
    "last_login": null,
    "created_at": "2020-11-04T15:37:37.589979Z"
}
```

## Change password

```
POST /api/me/password_change (requires authentication)
```

__Parameters__

Name             | Description
-----------------|-------------------------------------
current_password | Current password of the user.
new_password     | New password of the user.

__Request__

```json
{
    "current_password": "NotSoSafePassword",
    "new_password": "VerySafePassword0909"
}
```

__Response__

```
Status: 204 No-Content
```

**NOTE**:
- Error out in case "current_password" doesn't match

Status: 400 Bad Request

```
{
    "current_password": [
        "Incorrect current password!"
    ]
}
```

## Update profile

```json
PATCH /api/me (requires authentication)
```

__Parameter__

   Column    |       Type        | Nullable | Optional | Description
-------------|-------------------|----------|----------|-------------
 username    | `string`          | not null | Yes      | Username of the User
 email       | `string`          | not null | Yes      | Email of the User
 first_name  | `string`          | not null | Yes      | First name of the User
 last_name   | `string`          | not null | Yes      | Last name of the User
 avatar      | `string`          | not null | Yes      | URL of the image uploaded by the User

__Request__

```json
{
    "username": "GeekyyyShacklebolt",
    "email": "shiva+2@fueled.com",
    "first_name": "Shiva",
    "last_name": "Saxena",
    "avatar": null
}
```

__Response__

Status: 200 OK

```json
{
    "id": "2a8dc6d6-d7d2-4f53-8e89-8f54951fbf14",
    "username": "GeekyyyShacklebolt",
    "email": "shiva+2@fueled.com",
    "first_name": "Shiva",
    "last_name": "Saxena",
    "avatar": null,
    "last_login": null,
    "created_at": "2020-11-04T15:37:37.589979Z"
}
```

## Upload avatar

```json
POST /api/me/avatar_upload (requires authentication)
```

__Parameter__

   Column    |       Type        | Nullable | Optional | Description
-------------|-------------------|----------|----------|-------------
 avatar      | `string`          | not null | Yes      | URL of the image uploaded by the User

**NOTE**:
- Image will be uploaded as multipart data as a streaming HTTP request.

__Response__

Status: 201 Created

```json
{
    "id": "2a8dc6d6-d7d2-4f53-8e89-8f54951fbf14",
    "username": "GeekyyyShacklebolt",
    "email": "shiva+2@fueled.com",
    "first_name": "Shiva",
    "last_name": "Saxena",
    "avatar": "/.media/users/user/wYHeZ9B1QMylTJ7-82QLaQ.png",
    "last_login": null,
    "created_at": "2020-11-04T15:37:37.589979Z"
}
```

## Remove avatar

```json
DELETE /api/me/avatar_remove (requires authentication)
```

__Response__

Status: 204 No Content

## Delete user account

**NOTE**:
- A user can only delete its own account

```json
DELETE /api/me (requires authentication)
```

Status: 204 No Content

# Other User Actions

## List users

```json
GET /api/users
```

__Response__

Status: 200 OK

```json
{
    "count": 12,
    "next": "http://127.0.0.1:8000/api/users?page=2",
    "previous": null,
    "results": [
        {
            "id": "2a8dc6d6-d7d2-4f53-8e89-8f54951fbf14",
            "username": "GeekyyyShacklebolt",
            "email": "shiva+2@fueled.com",
            "first_name": "Shiva",
            "last_name": "Saxena",
            "avatar": "http://127.0.0.1:8000/.media/users/user/RlZCiYg0SSKvUdGR1SirZw.png",
            "last_login": "2020-11-04T12:56:02.229889Z",
            "created_at": "2020-11-04T15:37:37.589979Z"
        },
        {
            "id": "ba04f06d-8296-4c0b-a14e-f0b87671ed3d",
            "username": "akash",
            "email": "akash+1@test.com",
            "first_name": "",
            "last_name": "",
            "avatar": null,
            "last_login": "2020-11-04T12:56:02.229889Z",
            "created_at": "2020-11-04T12:56:02.229889Z"
        }
    ]
}
```

## Get profiles of a single User using id

```json
GET /api/users/:id
```

__Response__

Status: 200 OK

```json
{
    "id": "2a8dc6d6-d7d2-4f53-8e89-8f54951fbf14",
    "username": "GeekyyyShacklebolt",
    "email": "shiva+2@fueled.com",
    "first_name": "Shiva",
    "last_name": "Saxena",
    "avatar": "http://127.0.0.1:8000/.media/users/user/RlZCiYg0SSKvUdGR1SirZw.png",
    "last_login": null,
    "created_at": "2020-11-04T15:37:37.589979Z"
}
```

## Get profile of a single User using username

```json
GET /api/users?username=GeekyyyShacklebolt
```

__Response__

Status: 200 OK

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "2a8dc6d6-d7d2-4f53-8e89-8f54951fbf14",
            "username": "GeekyyyShacklebolt",
            "email": "shiva+2@fueled.com",
            "first_name": "Shiva",
            "last_name": "Saxena",
            "avatar": "http://127.0.0.1:8000/.media/users/user/RlZCiYg0SSKvUdGR1SirZw.png",
            "last_login": null,
            "created_at": "2020-11-04T15:37:37.589979Z"
        }
    ]
}
```

# Wishlist

## List wishlists of the current user

```json
GET /api/wishlists (requires authentication)
```

__Wishlist Schema__

   Column    |       Type        | Nullable | Description 
-------------|-------------------|----------|-------------
 id          | `uuid`            | not null | UUID for the `WishlistObject` 
 title       | `string`          | not null | Title of the Wishlsit 
 is_public   | `boolean`         | not null | Visibility of the wishlist
 created_at  | `datetime`        | not null | Time at which the `WishlistObject` created 
 modified_at | `datetime`        | not null | Time at which the `WishlistObject` modified 
 created_by  | `UserObject`      | not null | `UserObject` who created the wishlist 
 categories  | `Array`           |          | `Array` of `CategoryObjects`

__Response__

Status: 200 OK

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "e5ee9d28-c635-4ac3-8e3c-b79ad06615bd",
      "title": "Books To Read",
      "is_public": true, 
      "created_at": "2020-10-27T15:21:22.895341Z",
      "modified_at": "2020-10-27T15:21:22.895341Z",
      "created_by": {
        "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
        "first_name": "",
        "last_name": "",
        "photo": "http://example.com/media/users/01-0123/profile.png" 
      },
      "categories": [
        {
          "id": "12abcd28-c635-4ac3-8e3c-b79ad066abcd",
          "name": "comedy",
          "created_by": "123e9d28-c635-4ac3-8e3c-b79ad06000dff"
        }
      ]
    },
    {
      "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
      "title": "Movies",
      "is_public": true, 
      "created_at": "2020-10-27T15:21:22.895341Z",
      "modified_at": "2020-10-27T15:21:22.895341Z",
      "created_by": {
        "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
        "first_name": "",
        "last_name": "",
        "photo": "http://example.com/media/users/01-0123/profile.png" 
      },
     "categories": []
    }
  ]
}
```

## Get details of single wishlist

```json
GET /api/wishlists/:id (requires authentication)
```

**NOTE**:
- A user can get details of a wishlist if either s/he is the owner of it `created_by` or the wishlist is public `is_public=true`.

__Response__

Status: 200 OK

```json
{
  "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
  "title": "Movies",
  "is_public": true, 
  "created_at": "2020-10-27T15:21:22.895341Z",
  "modified_at": "2020-10-27T15:21:22.895341Z",
  "created_by": {
    "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
    "first_name": "",
    "last_name": "",
    "photo": "http://example.com/media/users/01-0123/profile.png" 
  },
  "categories": [
    {
      "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
      "name": "thriller",
      "created_by": "123e9d28-c635-4ac3-8e3c-b79ad06000dff"
    },
    {
      "id": "12abcd28-c635-4ac3-8e3c-b79ad066abcd",
      "name": "comedy",
      "created_by": "123e9d28-c635-4ac3-8e3c-b79ad06000dff"
    }
  ]
}
```

## Create a wishlist

```json
POST /api/wishlists (requires authentication)
```

**NOTE**:
  - No need to provide "created_by" field as it will be auto assigned from the backend.

__Parameters__

   Column    |       Type        | Nullable | Optional | Default | Description 
-------------|-------------------|----------|----------|---------|--------------
 title       | `string`          | not null | No       |         | Title of the Wishlsit 
 is_public   | `boolean`         | not null | Yes      | false   | Visibility of the wishlist

__Example__

```json
{
  "title": "Movies",
  "is_public": true
}
```

__Response__

Status: 201 Created

```json
{
  "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
  "title": "Movies",
  "is_public": true, 
  "created_at": "2020-10-27T15:21:22.895341Z",
  "modified_at": "2020-10-27T15:21:22.895341Z",
  "created_by": {
    "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
    "first_name": "",
    "last_name": "",
    "photo": "http://example.com/media/users/01-0123/profile.png" 
  },
  "categories": []
}
```

## Update a wishlist

```json
PATCH /api/wishlists/:id (requires authentication)
```

**NOTE**:
- A user can only update a wishlist if s/he is the owner `create_by` of it.

__Parameters__

   Column    |       Type        | Nullable | Optional | Description 
-------------|-------------------|----------|----------|--------------
 title       | `string`          | not null | Yes      | Title of the Wishlsit 
 is_public   | `boolean`         | not null | Yes      | Visibility of the wishlist

__Example__

```json
{
  "title": "Hollywood Movies"
}
```

__Response__

Status: 200 OK

```json
{
  "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
  "title": "Movies",
  "is_public": true, 
  "created_at": "2020-10-27T15:21:22.895341Z",
  "modified_at": "2020-10-27T15:21:22.895341Z",
  "created_by": {
    "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
    "first_name": "",
    "last_name": "",
    "photo": "http://example.com/media/users/01-0123/profile.png" 
  },
  "categories": [
    {
      "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
      "name": "thriller",
      "created_by": "123e9d28-c635-4ac3-8e3c-b79ad06000dff"
    },
    {
      "id": "12abcd28-c635-4ac3-8e3c-b79ad066abcd",
      "name": "comedy",
      "created_by": "123e9d28-c635-4ac3-8e3c-b79ad06000dff"
    }
  ]
}
```

## Delete a wishlist

```json
DELETE /api/wishlists/:id (requires authentication)
```

**NOTE**:
- A user can only delete a wishlist if s/he is the owner `created_by` of it.

Status: 204 No Content


# Category

## Create a new category

```json
POST /api/categories (requires authentication)
```

**NOTE**:
  - No need to provide "id" and "created_by" field as it will be auto assigned from the backend.

__Category Schema__

 Column     |       Type        | Nullable | Description 
------------|-------------------|----------|-------------
 id         | `uuid`            | not null | UUID for the `CategoryObject` 
 name       | `string`          | not null | Name of the Category 
 created_by | `uuid`            | not null | UUID for the `UserObject`

__Request__

```json
{
  "name": "thriller",
}
```

__Response__

Status: 201 Created

```json
{
  "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
  "name": "thriller",
  "created_by": "123e9d28-c635-4ac3-8e3c-b79ad06000dff"
}
```

## Delete a category

```json
DELETE /api/categories/:id (requires authentication)
```

**NOTE**:
- A user can only delete the categories the s/he created.

Status: 204 No Content

## Get all categories of a wishlist

```json
GET /api/wishlist/:id/categories
```

__Response__

Status: 200 OK

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
      "name": "thriller",
      "created_by": "123e9d28-c635-4ac3-8e3c-b79ad06000dff"
    },
    {
      "id": "12abcd28-c635-4ac3-8e3c-b79ad066abcd",
      "name": "comedy",
      "created_by": "123e9d28-c635-4ac3-8e3c-b79ad06000dff"
    }
  ]
}
```

## Remove a category from a wishlist

```json
DELETE /api/wishlists/:wishlist_id/categories/:category_id
```

Status: 204 No Content

## Filter wishlists using categories

```json
GET /api/wishlists?category="thriller"&category="comedy"
```

**NOTE**:
- A user can get wishlists if either they are public or the user is its owner

__Response__

Status: 200 OK

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "e5ee9d28-c635-4ac3-8e3c-b79ad06615bd",
      "title": "Books To Read",
      "is_public": true, 
      "created_at": "2020-10-27T15:21:22.895341Z",
      "modified_at": "2020-10-27T15:21:22.895341Z",
      "created_by": {
        "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
        "first_name": "",
        "last_name": "",
        "photo": "http://example.com/media/users/01-0123/profile.png" 
      },
      "categories": [
        {
          "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
          "name": "thriller",
          "created_by": "123e9d28-c635-4ac3-8e3c-b79ad06000dff"
        }
      ]
    },
    {
      "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
      "title": "Movies",
      "is_public": true, 
      "created_at": "2020-10-27T15:21:22.895341Z",
      "modified_at": "2020-10-27T15:21:22.895341Z",
      "created_by": {
        "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
        "first_name": "",
        "last_name": "",
        "photo": "http://example.com/media/users/01-0123/profile.png" 
      },
      "categories": [
        {
          "id": "12abcd28-c635-4ac3-8e3c-b79ad066abcd",
          "name": "comedy",
          "created_by": "123e9d28-c635-4ac3-8e3c-b79ad06000dff"
        }
      ]
    }
  ]
}
```

## Add a category to a wishlist

```json
POST /api/wishlists/:wishlist_id/categories
```

__Parameter__

  Column             |       Type        | Nullable | Description 
---------------------|-------------------|----------|-------------
 id                  | `uuid`            | not null | UUID of the `CategoryObject`


__Request__

```josn
{
  "id": "12abcd28-c635-4ac3-8e3c-b79ad066abcd"
}
```

__Response__

Status: 201 Created

```json
{
  "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
  "title": "Movies",
  "is_public": true, 
  "created_at": "2020-10-27T15:21:22.895341Z",
  "modified_at": "2020-10-27T15:21:22.895341Z",
  "created_by": {
    "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
    "first_name": "",
    "last_name": "",
    "photo": "http://example.com/media/users/01-0123/profile.png" 
  },
  "categories": [
    {
      "id": "12abcd28-c635-4ac3-8e3c-b79ad066abcd",
      "name": "comedy",
      "created_by": "123e9d28-c635-4ac3-8e3c-b79ad06000dff"
    }
  ]
}
```


# Card

## List cards of a wishlist

```
GET /api/wishlists/:id/cards (requires authentication)
```
**NOTE**:
- A user can only get cards that are created in his own or public wishlists.

__Card Schema__

  Column             |       Type        | Nullable | Description 
---------------------|-------------------|----------|-------------
 id                  | `uuid`            | not null | UUID for the `CardObject` 
 title               | `string`          | not null | Title of the Card 
 description         | `string`          |          | Description of the Card 
 link                | `string`          |          | Any hyper link 
 image               | `string`          |          | URL of the image uploaded for the Card 
 created_at          | `datetime`        | not null | Time at which the `CardObject` created 
 modified_at         | `datetime`        | not null | Time at which the `CardObject` modified 
 created_by          | `UserObject`      | not null | UUID for the `UserObject` created this Card 
 wishlist            | `uuid`            | not null | UUID for the `WishlistObject` under which this Card exists

__Response__

Status: 200 OK

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
      "title": "Terminator",
      "description": "A nice and short description",
      "link": "https://example.com/anything",
      "image": "http://example.com/media/users/01-0123/profile.png",
      "created_at": "2020-10-27T15:21:22.895341Z",
      "modified_at": "2020-10-27T15:21:22.895341Z",
      "created_by": {
        "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
        "first_name": "",
        "last_name": "",
        "photo": "http://example.com/media/users/01-0123/profile.png" 
      },
      "wishlist": "7c111111-c832-4639-9368-dd8633f8baa6",
    },
    {
      "id": "aaabbc28-c635-4ac3-8e3c-b79ad066abcd",
      "title": "Terminator",
      "description": "A nice and short description",
      "link": "https://example.com/anything",
      "image": "http://example.com/media/users/01-0123/profile.png",
      "created_at": "2020-10-27T15:21:22.895341Z",
      "modified_at": "2020-10-27T15:21:22.895341Z", 
      "created_by": {
        "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
        "first_name": "",
        "last_name": "",
        "photo": "http://example.com/media/users/01-0123/profile.png" 
      },
      "wishlist": "7c111111-c832-4639-9368-dd8633f8baa6",
    }
  ]
}
```

## Get details of a single card

```json
GET /api/cards/:id
```

**NOTE**:
- A user can only get cards that are created in his own or public wishlists.

__Response__

Status: 200 OK

```json
{
  "id": "aaabbc28-c635-4ac3-8e3c-b79ad066abcd",
  "title": "Terminator",
  "description": "A nice and short description",
  "link": "https://example.com/anything",
  "image": "http://example.com/media/users/01-0123/profile.png",
  "created_at": "2020-10-27T15:21:22.895341Z",
  "modified_at": "2020-10-27T15:21:22.895341Z",
  "created_by": {
    "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
    "first_name": "",
    "last_name": "",
    "photo": "http://example.com/media/users/01-0123/profile.png" 
  },
  "wishlist": "7c111111-c832-4639-9368-dd8633f8baa6"
}
```

## Create a card

```json
POST /api/cards (requires authentication)
```

__Parameters__

  Column             |       Type        | Nullable | Optional | Default |Description 
---------------------|-------------------|----------|----------|---------|---------------
 title               | `string`          | not null | No       |         | Title of the Card 
 description         | `string`          |          | Yes      | null    | Description of the Card 
 link                | `string`          |          | Yes      | null    | Any hyper link 
 image               | `string`          |          | Yes      | null    | URL of the image uploaded for the Card 
 wishlist            | `uuid`            | not null | No       |         | UUID for the `WishlistObject` under which this Card exists

__Request__

```json
{
 "title": "Terminator",
 "wishlist": "7c111111-c832-4639-9368-dd8633f8baa6"
}
```

__Response__

Status: 201 Created

```json
{
  "id": "aaabbc28-c635-4ac3-8e3c-b79ad066abcd",
  "title": "Terminator",
  "description": null,
  "link": null,
  "image": null,
  "created_at": "2020-10-27T15:21:22.895341Z",
  "modified_at": "2020-10-27T15:21:22.895341Z",
  "created_by": {
    "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
    "first_name": "",
    "last_name": "",
    "photo": "http://example.com/media/users/01-0123/profile.png" 
  },
  "wishlist": "7c111111-c832-4639-9368-dd8633f8baa6"
}
```

## Update a card

**NOTE**:
- A user can only update a card if s/he is the owner of it `created_by`.

```json
PATCH /api/cards/:id (requires authentication)
```

__Parameters__

  Column             |       Type        | Nullable | Optional |Description 
---------------------|-------------------|----------|----------|---------------
 title               | `string`          | not null | Yes      | Title of the Card 
 description         | `string`          |          | Yes      | Description of the Card 
 link                | `string`          |          | Yes      | Any hyper link 
 image               | `string`          |          | Yes      | URL of the image uploaded for the Card 
 wishlist            | `uuid`            | not null | Yes      | UUID for the `WishlistObject` under which this Card exists

__Request__

```json
{
 "title": "Terminator2",
 "wishlist": "7c888811-c832-4639-9368-dd8633f8baa6",
 "description": "Another short description",
}
```

__Response__

Status: 200 OK

```json
{
  "id": "aaabbc28-c635-4ac3-8e3c-b79ad066abcd",
  "title": "Terminator2",
  "description": "Another short description",
  "link": null,
  "image": null,
  "created_at": "2020-10-27T15:21:22.895341Z",
  "modified_at": "2020-10-27T15:21:22.895341Z", 
  "created_by": {
    "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
    "first_name": "",
    "last_name": "",
    "photo": "http://example.com/media/users/01-0123/profile.png" 
  },
  "wishlist": "7c888811-c832-4639-9368-dd8633f8baa6"
}
```

## Delete a card

```json
DELETE /api/cards/:id (requires authentication)
```

**NOTE**:
- A user can only delete a card that is been created by him/her.

Status: 204 No Content


# Review

## List reviews of a card

```
GET /api/cards/:id/reviews (requires authentication)
```
**NOTE**:
- A user can only get reviews that are created on his own cards or cards present in public wishlists.

__Review Schema__

  Column          |       Type        | Nullable | Description 
------------------|-------------------|----------|-------------
 id               | `uuid`            | not null | UUID for the `ReviewObject` 
 comment          | `string`          | not null | Review Comment 
 rating           | `integer`         |          | Rating between 0 and 10  
 will_recommend   | `boolean`         |          | Weather User would recommend the card or not 
 created_at       | `datetime`        | not null | Time at which the `ReviewObject` created 
 modified_at      | `datetime`        | not null | Time at which the `ReviewObject` modified 
 created_by       | `UserObject`      | not null | UUID for the `UserObject` who created the Review 
 card             | `uuid`            | not null | UUID for the `CardObject` for which this Review was created

__Response__

Status: 200 OK

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "fffe9d28-c635-4ac3-8e3c-b79ad066abcd",
      "comment": "Worth Reading",
      "rating": 5,
      "will_recommend": null,
      "created_at": "2020-10-27T15:21:22.895341Z",
      "modified_at": "2020-10-27T15:21:22.895341Z",
      "created_by": {
        "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
        "first_name": "",
        "last_name": "",
        "photo": "http://example.com/media/users/01-0123/profile.png" 
      },
      "card": "7c111111-c832-4639-9368-dd8633f8baa6",
    },
    {
      "id": "abcd9d28-c635-4ac3-8e3c-b79ad066abcd",
      "comment": "Excellant!!!",
      "rating": 9,
      "will_recommend": true,
      "created_at": "2020-10-27T15:21:22.895341Z",
      "modified_at": "2020-10-27T15:21:22.895341Z",
      "created_by": {
        "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
        "first_name": "",
        "last_name": "",
        "photo": "http://example.com/media/users/01-0123/profile.png" 
      },
      "card": "7c111111-c832-4639-9368-dd8633f8baa6",
    }
  ]
}
```

## Get details of a single review

```json
GET /api/reviews/:id
```

**NOTE**:
- A user can only get reviews that are created on his own cards or cards present in public wishlists.

__Response__

Status: 200 OK

```json
{
  "id": "abcd9d28-c635-4ac3-8e3c-b79ad066abcd",
  "comment": "Excellant!!!",
  "rating": 9,
  "will_recommend": true,
  "created_at": "2020-10-27T15:21:22.895341Z",
  "modified_at": "2020-10-27T15:21:22.895341Z",
  "created_by": {
    "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
    "first_name": "",
    "last_name": "",
    "photo": "http://example.com/media/users/01-0123/profile.png" 
  },
  "card": "7c111111-c832-4639-9368-dd8633f8baa6",
}
```

## Create a review

```json
POST /api/reviews (requires authentication)
```

__Parameters__

  Column          |       Type        | Nullable | Optional | Default |  Description 
------------------|-------------------|----------|----------|---------|------------------
 comment          | `string`          | not null | Yes      | ''      | Review Comment 
 rating           | `integer`         |          | Yes      | null    | Rating between 0 and 10  
 will_recommend   | `boolean`         |          | Yes      | null    | Weather User would recommend the card or not 
 card             | `uuid`            | not null | No       |         | UUID for the `CardObject` for which this Review was created

__Request__

```json
{
 "comment": "A short or long comment!",
 "rating": 3,
 "card": "7c111111-c832-4639-9368-dd8633f8baa6"
}
```

__Response__

Status: 201 Created

```json
{
  "id": "abcd9d28-c635-4ac3-8e3c-b79ad066abcd",
  "comment": "A short or long comment!",
  "rating": 3,
  "will_recommend": null,
  "created_at": "2020-10-27T15:21:22.895341Z",
  "modified_at": "2020-10-27T15:21:22.895341Z", 
  "created_by": {
    "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
    "first_name": "",
    "last_name": "",
    "photo": "http://example.com/media/users/01-0123/profile.png" 
  },
  "card": "7c111111-c832-4639-9368-dd8633f8baa6",
}
```

## Update a review

**NOTE**:
- A user can only update a review if s/he is the owner of it `created_by`.

```json
PATCH /api/reviews/:id (requires authentication)
```

__Parameters__

  Column          |       Type        | Nullable | Optional |  Description 
------------------|-------------------|----------|----------|------------------
 comment          | `string`          | not null | Yes      | Review Comment 
 rating           | `integer`         |          | Yes      | Rating between 0 and 10  
 will_recommend   | `boolean`         |          | Yes      | Weather User would recommend the card or not 
 card             | `uuid`            | not null | Yes      | UUID for the `CardObject` for which this Review was created

__Request__

```json
{
 "comment": "The modified comment",
 "rating": 5,
 "will_recommend": false
}
```

__Response__

Status: 200 OK

```json
{
  "id": "abcd9d28-c635-4ac3-8e3c-b79ad066abcd",
  "comment": "The modified comment",
  "rating": 5,
  "will_recommend": false,
  "created_at": "2020-10-27T15:21:22.895341Z",
  "modified_at": "2020-10-27T15:21:22.895341Z",
  "created_by": {
    "id": "7c030b31-c832-4639-9368-dd8633f8baa6",
    "first_name": "",
    "last_name": "",
    "photo": "http://example.com/media/users/01-0123/profile.png" 
  },
  "card": "7c111111-c832-4639-9368-dd8633f8baa6",
}
```

## Delete a review

```json
DELETE /api/reviews/:id (requires authentication)
```

**NOTE**:
- A user can only delete a review that is been created by him/her.

Status: 204 No Content
