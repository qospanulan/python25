

SELECT * FROM blog_blog;

SELECT * FROM blog_post
WHERE created_at=updated_at;


SELECT * FROM blog_post
WHERE id IN (2, 3) OR content LIKE '%ц%';


SELECT blog_id, COUNT(*) FROM blog_post
GROUP BY blog_id;


SELECT "blog_post"."blog_id" AS "blog_id",
       MAX("blog_post"."id") AS "posts_count"
  FROM "blog_post"
 GROUP BY 1, 2
 LIMIT 21


