SELECT "blog_blog"."id",
       "blog_blog"."name",
       "blog_blog"."description",
       "blog_blog"."created_at",
       "blog_blog"."updated_at"
  FROM "blog_blog"
 LIMIT 21;


SELECT "blog_post"."id",
       "blog_post"."content",
       "blog_post"."blog_id"
  FROM "blog_post"
 LIMIT 21;


SELECT * FROM blog_post
WHERE id='2';

SELECT "blog_post"."id",
       "blog_post"."content",
       "blog_post"."blog_id"
  FROM "blog_post"
 WHERE "blog_post"."id" = 2
 LIMIT 21;




SELECT id, content::varchar, blog_id FROM blog_post
WHERE content::varchar LIKE '%ц%'; -- BETWEEN, < lt, > gt, =< lte, => gte
 


SELECT id, content, blog_id FROM blog_post
WHERE id IN (2, 3);









