{{ config(materialized='table') }}

SELECT
    chapter_id,
    chapter_name,
    city,
    state,
    latitude,
    longitude
FROM {{ ref('stg_chapters') }}
WHERE state IS NOT NULL