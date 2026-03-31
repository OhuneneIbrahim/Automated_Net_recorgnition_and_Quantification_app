from detectron2.data.datasets import register_coco_instances
from detectron2.data import DatasetCatalog, MetadataCatalog

def register_datasets(train_json, train_img, val_json, val_img):
    for name in ["nets_train", "nets_val"]:
        if name in DatasetCatalog.list():
            DatasetCatalog.remove(name)
        if name in MetadataCatalog.list():
            MetadataCatalog.remove(name)

    register_coco_instances("nets_train", {}, train_json, train_img)
    register_coco_instances("nets_val", {}, val_json, val_img)

    return (
        MetadataCatalog.get("nets_train"),
        MetadataCatalog.get("nets_val"),
    )