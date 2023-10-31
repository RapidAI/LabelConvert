from label_convert.labelme_to_coco import LabelmeToCOCO

data_dir = "dataset/labelme_format"
out_dir = "output"
convert = LabelmeToCOCO(
    data_dir=data_dir, out_dir=out_dir, val_ratio=0.1, have_test=True, test_ratio=0.1
)

convert()
