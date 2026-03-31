from detectron2.config import get_cfg
from detectron2 import model_zoo

def get_detectron_cfg(num_classes=2, output_dir="models"):
    cfg = get_cfg()
    cfg.merge_from_file(
        model_zoo.get_config_file(
            "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
        )
    )

    cfg.OUTPUT_DIR = output_dir

    cfg.DATASETS.TRAIN = ("nets_train",)
    cfg.DATASETS.TEST = ("nets_val",)

    cfg.DATALOADER.NUM_WORKERS = 2

    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(
        "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
    )

    cfg.SOLVER.IMS_PER_BATCH = 2
    cfg.SOLVER.BASE_LR = 0.00025
    cfg.SOLVER.MAX_ITER = 5000
    cfg.SOLVER.STEPS = []

    cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 256
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = num_classes

    cfg.TEST.EVAL_PERIOD = 500
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.3

    return cfg