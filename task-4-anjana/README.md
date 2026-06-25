Project 4: Building the Machine's Optic Nerve

Project Objective
An AI implementation project focused on transitioning from structured datasets to unstructured visual data feeds. This pipeline ingests raw imagery, preprocesses it, and utilizes a pre-trained deep learning framework to execute real-world object recognition. The pipeline is versatile and designed to process raw unstructured assets using a combination of deep learning frameworks and structural processing engines.

Tech Stack and Libraries
- Language: Python 3.x
- Framework: OpenCV (Open Source Computer Vision)
- Model Architecture: MobileNet-SSD (Single Shot Detector) parsed via Caffe
- Visualizations and Assets: Matplotlib and Pillow

Core Parameters and Evaluation Metrics
- The IPO Model: Ingests three-dimensional input arrays and normalizes them into blob formats required by the deep neural network.
- Accuracy Benchmarking: Implements a strict confidence guardrail matching industry compliance rules with an 80% filter threshold. Detections falling below this mark are automatically discarded.
- Visual Confirmation: Programmatically maps precise bounding box coordinates and classification labels directly onto the final output image display workspace.

Execution Verification and Output
When running the object tracking configuration on unstructured imagery, the pipeline successfully isolates target profiles with high precision:

![Object Detection Output](assets/dog-puppy-on-garden-royalty-free-image-1586966191.avif)

- Detected Object Class: Dog
- Validated Model Confidence Score: 99.72%
