# Todify's Database Schema

## Diagram

![phase-1-database-relations](./img/phase-1-database-relations.png)

## Tables

### User

 Column       |  Type         | Nullable | Default | Description 
--------------|---------------|----------|---------|-------------
 password     | `string`(128) | not null |         | Password
 last_login   | 'datetime'    |          |         | Timestamp when user last login
 is_superuser | `boolean`     | not null |         | Designates wheather the user is superuser
 id           | `uuid`        | not null | `uuid4` | `PrimaryKey` UUID for the `UserObject`
 created_at   | 'datetime'    | not null |         | Timestamp at which the user is created
 modified_at  | 'datetime'    | not null |         | Timestamp at which the user last modified
 first_name   | `string`(120) | not null | ""      | First Name
 last_name    | `string`(120) | not null | ""      | Last Name
 email        | `string`      | not null |         | Email Address
 username     | `string`(32)  | not null |         | `Unique` Username
 avatar       | `string`(100) |          |         | URL of the image uploaded by the User
 avatar_poi   | `string`(20)  | not null |         | Avatar's Point of Interest
 is_active    | `boolean`     | not null |         | Designates wheather the user is active
 is_staff     | `boolean`     | not null |         | Designates wheather the user is staff

Indexes:
- "user_pkey" PRIMARY KEY, btree (id)
- "user_email_key" UNIQUE CONSTRAINT, btree (email)
- "user_username_key" UNIQUE CONSTRAINT, btree (username)
- "user_username_cf016618_like" btree (username varchar_pattern_ops)

Referenced by:
- TABLE "card" CONSTRAINT "card_created_by_id_a1f9a55e_fk_user_id" FOREIGN KEY (created_by_id) REFERENCES "user"(id) DEFERRABLE INITIALLY DEFERRED
- TABLE "category" CONSTRAINT "category_created_by_id_d315699e_fk_user_id" FOREIGN KEY (created_by_id) REFERENCES "user"(id) DEFERRABLE INITIALLY DEFERRED
- TABLE "django_admin_log" CONSTRAINT "django_admin_log_user_id_c564eba6_fk_user_id" FOREIGN KEY (user_id) REFERENCES "user"(id) DEFERRABLE INITIALLY DEFERRED
- TABLE "review" CONSTRAINT "review_created_by_id_f6b70669_fk_user_id" FOREIGN KEY (created_by_id) REFERENCES "user"(id) DEFERRABLE INITIALLY DEFERRED
- TABLE "user_groups" CONSTRAINT "user_groups_user_id_abaea130_fk_user_id" FOREIGN KEY (user_id) REFERENCES "user"(id) DEFERRABLE INITIALLY DEFERRED
- TABLE "user_user_permissions" CONSTRAINT "user_user_permissions_user_id_ed4a47ea_fk_user_id" FOREIGN KEY (user_id) REFERENCES "user"(id) DEFERRABLE INITIALLY DEFERRED
- TABLE "wishlist" CONSTRAINT "wishlist_created_by_id_b520df09_fk_user_id" FOREIGN KEY (created_by_id) REFERENCES "user"(id) DEFERRABLE INITIALLY DEFERRED

----------------------------------------------------------------------------------------------------------------------------------------

### Wishlist

 Column        | Type          | Nullable | Default | Description 
---------------|---------------|----------|---------|-------------
 id            | `uuid`        | not null | `uuid4` | `PrimaryKey` UUID for the `WishlistObject`
 created_at    | `datetime`    | not null |         | Timestamp at which the wishlist is created
 modified_at   | `datetime`    | not null |         | Timestamp at which the wishlist last modified
 title         | `string`(120) | not null |         | Title
 description   | `string`(512) | not null |         | Description
 is_public     | `boolean`     | not null | `true`  | Designates wheather the wishlist should be considered as public
 created_by    | `uuid`        | not null |         | UUID of `UserObject` that created the wishlist

Indexes:
- "wishlist_pkey" PRIMARY KEY, btree (id)
- "wishlist_created_by_id_b520df09" btree (created_by_id)

Foreign-key constraints:
- "wishlist_created_by_id_b520df09_fk_user_id" FOREIGN KEY (created_by_id) REFERENCES "user"(id) DEFERRABLE INITIALLY DEFERRED

Referenced by:
- TABLE "card" CONSTRAINT "card_wishlist_id_19c77387_fk_wishlist_id" FOREIGN KEY (wishlist_id) REFERENCES wishlist(id) DEFERRABLE INITIALLY DEFERRED
- TABLE "wishlist_category_mapping" CONSTRAINT "wishlist_category_mapping_wishlist_id_0cbdf4c5_fk_wishlist_id" FOREIGN KEY (wishlist_id) REFERENCES wishlist(id) DEFERRABLE INITIALLY DEFERRED

----------------------------------------------------------------------------------------------------------------------------------------

### Category

 Column        | Type          | Nullable | Default | Description 
---------------|---------------|----------|---------|-------------
 id            | `uuid`        | not null | `uuid4` | UUID for the `CategoryObject`
 name          | `string`(120) | not null |         | Category Name
 created_by    | `uuid`        | not null |         | UUID of `UserObject` that created the category

Indexes:
- "category_pkey" PRIMARY KEY, btree (id)
- "category_created_by_id_d315699e" btree (created_by_id)

Foreign-key constraints:
- "category_created_by_id_d315699e_fk_user_id" FOREIGN KEY (created_by_id) REFERENCES "user"(id) DEFERRABLE INITIALLY DEFERRED

Referenced by:
- TABLE "wishlist_category_mapping" CONSTRAINT "wishlist_category_mapping_category_id_e7ab4718_fk_category_id" FOREIGN KEY (category_id) REFERENCES category(id) DEFERRABLE INITIALLY DEFERRED

----------------------------------------------------------------------------------------------------------------------------------------

### Wishlist_Category_Mapping

 Column      | Type       | Nullable | Default | Description 
-------------|------------|----------|---------|-------------
 id          | `uuid`     | not null | `uuid4` | UUID for the `WishlistCategoryObject` 
 created_at  | `datetime` | not null |         | Timestamp at which the mapping created
 modified_at | `datetime` | not null |         | Timestamp at which the mapping last modified
 category    | `uuid`     | not null |         | UUID for the `CategoryObject`
 wishlist    | `uuid`     | not null |         | UUID for the `WishlistObject`

Indexes:
- "wishlist_category_mapping_pkey" PRIMARY KEY, btree (id)
- "wishlist_category_mapping_wishlist_id_category_id_90c9dc0e_uniq" UNIQUE CONSTRAINT, btree (wishlist_id, category_id)
- "wishlist_category_mapping_category_id_e7ab4718" btree (category_id)
- "wishlist_category_mapping_wishlist_id_0cbdf4c5" btree (wishlist_id)

Foreign-key constraints:
- "wishlist_category_mapping_category_id_e7ab4718_fk_category_id" FOREIGN KEY (category_id) REFERENCES category(id) DEFERRABLE INITIALLY DEFERRED
- "wishlist_category_mapping_wishlist_id_0cbdf4c5_fk_wishlist_id" FOREIGN KEY (wishlist_id) REFERENCES wishlist(id) DEFERRABLE INITIALLY DEFERRED

----------------------------------------------------------------------------------------------------------------------------------------

### Card

 Column        | Type          | Nullable | Default  | Description 
---------------|---------------|----------|----------|-------------
 id            | `uuid`        | not null | `uuid4`  | UUID for the `CardObject`
 created_at    | `datetime`    | not null |          | Timestamp at which card is created
 modified_at   | `datetime`    | not null |          | Timestamp at which card is last modified
 title         | `string`(120) | not null |          | Card Title
 description   | `string`(512) | not null |          | Card Description
 link          | `string`(200) | not null |          | Any URL
 photo         | `string`(100) |          | null     | URL of the image uploaded
 photo_poi     | `string`(20)  | not null |          | Photo's point of interest
 created_by    | `uuid`        | not null |          | UUID of the `UserObject` that created the card
 wishlist      | `uuid`        | not null |          | UUID of the `WishlistObject` under which the card exists

Indexes:
- "card_pkey" PRIMARY KEY, btree (id)
- "card_created_by_id_a1f9a55e" btree (created_by_id)
- "card_wishlist_id_19c77387" btree (wishlist_id)

Foreign-key constraints:
- "card_created_by_id_a1f9a55e_fk_user_id" FOREIGN KEY (created_by_id) REFERENCES "user"(id) DEFERRABLE INITIALLY DEFERRED
- "card_wishlist_id_19c77387_fk_wishlist_id" FOREIGN KEY (wishlist_id) REFERENCES wishlist(id) DEFERRABLE INITIALLY DEFERRED

Referenced by:
- TABLE "review" CONSTRAINT "review_card_id_8a99c4c3_fk_card_id" FOREIGN KEY (card_id) REFERENCES card(id) DEFERRABLE INITIALLY DEFERRED

----------------------------------------------------------------------------------------------------------------------------------------

### Review

 Column         | Type          | Nullable | Default | Description 
----------------|---------------|----------|---------|-------------
 id             | `uuid`        | not null | `uuid4` | UUID for the `ReviewObject` 
 created_at     | `datetime`    | not null |         | Timestamp at which review is created
 modified_at    | `datetime`    | not null |         | Timestamp at which the review last modified
 title          | `string`(120) | not null |         | Review Title
 description    | `string`(512) | not null | ""      | Review Description
 rating         | `integer`     |          | null    | Review Rating 0 to 10
 will_recommend | `boolean`     |          | null    | Designates wheather the review recommends the card to other users
 card           | `uuid`        | not null |         | UUID for the `CardObject` for which the review is created
 created_by     | `uuid`        | not null |         | UUID of the `UserObject` that created the review

Indexes:
- "review_pkey" PRIMARY KEY, btree (id)
- "review_card_id_8a99c4c3" btree (card_id)
- "review_created_by_id_f6b70669" btree (created_by_id)

Foreign-key constraints:
- "review_card_id_8a99c4c3_fk_card_id" FOREIGN KEY (card_id) REFERENCES card(id) DEFERRABLE INITIALLY DEFERRED
- "review_created_by_id_f6b70669_fk_user_id" FOREIGN KEY (created_by_id) REFERENCES "user"(id) DEFERRABLE INITIALLY DEFERRED
