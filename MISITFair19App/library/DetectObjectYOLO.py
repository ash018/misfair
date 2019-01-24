import cv2
import argparse
import numpy as np

classes = None
COLORS = None
DetectedObjects = {}


def get_output_layers(net):
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers


def draw_prediction(classes, COLORS, img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    color = COLORS[class_id]
    cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 9)
    cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 4)
    DetectedObjects[label] = DetectedObjects[label]+1

def DetectFacesInImage(dir, input_image, image_file_name):
    print(input_image)
    image = cv2.imread(input_image)
    Width = image.shape[1]
    Height = image.shape[0]
    scale = 0.00392

    with open('PiImage\\HumanDetectConfig\\' + 'obj.names', 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    for item in classes:
        DetectedObjects[item] = 0

    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

    COLORS = [(51, 255, 255), (255, 0, 0), (0, 0, 102), (255, 191, 0), (255, 64, 0), (255, 0, 255)]

    net = cv2.dnn.readNet('PiImage\\HumanDetectConfig\\' + 'yolo-obj_14500.weights',
                          'PiImage\\HumanDetectConfig\\' + 'yolo-obj.cfg')

    blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)

    outs = net.forward(get_output_layers(net))

    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.25
    nms_threshold = 0.2

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    for i in indices:
        i = i[0]
        box = boxes[i]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]
        draw_prediction(classes, COLORS, image, class_ids[i], confidences[i], round(x), round(y), round(x + w),
                        round(y + h))

    # cv2.imshow("object detection", image)
    # cv2.waitKey()
    output_filename = 'PiImage\\\FairOutput\\' + image_file_name
    cv2.imwrite(output_filename, image)
    return "Output.jpg", DetectedObjects
    # cv2.destroyAllWindows()