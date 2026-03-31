import json
def sanitize_coco_json(input_json_path, output_json_path):
    with open(input_json_path, "r") as f:
        coco = json.load(f)

    annotations = coco["annotations"]
    categories = coco["categories"]

    used_ids = sorted({ann["category_id"] for ann in annotations})
    used_categories = [cat for cat in categories if cat["id"] in used_ids]

    if not used_categories:
        raise ValueError("No used categories were found in the annotations.")

    old_to_new = {}
    new_categories = []
    for new_id, cat in enumerate(sorted(used_categories, key=lambda x: x["id"]), start=1):
        old_to_new[cat["id"]] = new_id
        new_cat = dict(cat)
        new_cat["id"] = new_id
        new_categories.append(new_cat)

    for ann in annotations:
        ann["category_id"] = old_to_new[ann["category_id"]]

    coco["categories"] = new_categories

    with open(output_json_path, "w") as f:
        json.dump(coco, f)

    print(f"Saved sanitized JSON to: {output_json_path}")
    print("Category mapping:", old_to_new)
    print("Final categories:", [(c["id"], c["name"]) for c in new_categories])