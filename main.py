from ultralytics import YOLO
import cv2

traducao_changana = {
    'person': 'munhu',
    'laptop': 'khomphyuta',
    'cell phone': 'telefone',
    'bed': 'mubedu',
    'car': 'movha',
    'dog': 'nguana',
    'cat': 'xingove',
    'book': 'buku',
    'chair': 'xitshamu',
    'table': 'meza',
    'pen': 'peni',
    'pencil': 'pensele',
    'paper': 'papila',
}

# Função para traduzir o nome do objeto manualmente
def traduzir_para_changana(nome_objeto):
    return traducao_changana.get(nome_objeto, "Desconhecido")

model = YOLO('YoloWeights/yolov8x.pt')

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Erro ao abrir a câmera.")
    exit()

print("Pressione 's' para capturar a imagem.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Falha ao capturar imagem.")
        break

    cv2.imshow('Camera - Pressione "s" para capturar', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("Imagem capturada!")
        cv2.imwrite("captured_image.jpg", frame)
        break

cap.release()
cv2.destroyAllWindows()

results = model(frame, show=False)

for result in results:
    boxes = result.boxes
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0].item()
        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        nome_changana = traduzir_para_changana(class_name)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        label = f"{nome_changana} {conf:.1f}"
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.imshow("Detecção de Objetos", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
