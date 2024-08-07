# chromosome_karyotyping
Developed a system designed to assist in the meticulous task of identifying and categorizing chromosomes within the context of karyotyping, an essential process in the field of genetics and medical diagnosis. 

This system offers several significant advantages. First, it operates swiftly, significantly reducing the time required for chromosome analysis. Second, it excels in accuracy, minimizing errors that can occur during manual analysis.

Have trained the dataset on varying parameters, here's the reference:
runs/detect/train/train3/weights/best.pt for iou=0.7, imgsz=100, epochs=500 model=yolov8n.pt  
runs/detect/train/train5/weights/best.pt for iou=0.5, imgsz=100, epochs=500 model=yolov8n.pt  
runs/detect/train/train7/weights/best.pt for iou=0.5, imgsz=100, epochs=500 model=yolov8x.pt  
runs/detect/train/train9/weights/best.pt for iou=0.5, imgsz=100, epochs=100 model=yolov8x.pt 

<img height=640 width=400 align=left src="https://github.com/akshan-main/chromosome_karyotyping/blob/master/test/images/karyotype-11_bmp_jpg.rf.75f3e9e0274d17fbf5e3140cd64f7aaa.jpg"> 
<img height=640 width=400 align =right src="https://github.com/akshan-main/chromosome_karyotyping/blob/master/sample_output.jpeg">


