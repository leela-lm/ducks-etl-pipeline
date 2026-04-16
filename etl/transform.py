def transform_chapters(data):
    records = []

    for feature in data.get("features", []):
        attr = feature.get("attributes", {})
        geom = feature.get("geometry", {})

        records.append({
            "chapter_id": attr.get("ChapterID"),
            "chapter_name": attr.get("University_Chapter"),
            "city": attr.get("City"),
            "state": attr.get("State"),
            "longitude": geom.get("x"),
            "latitude": geom.get("y"),
        })

    return records
