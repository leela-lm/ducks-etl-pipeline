SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY chapter_id ORDER BY chapter_id) as rn
    FROM `ducks-etl-project.ducks_dataset.ducks_chapters_raw`
)
WHERE rn = 1