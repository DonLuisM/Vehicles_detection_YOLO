from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

#* Upload the model here
modelo_V8n = YOLO('best.pt')

clases_colores = {
        'Carro': (0, 255, 0),
        'Bus': (0, 0, 255),
        'Camion': (120, 100, 180),
        'Helicoptero': (0, 140, 200),
        'Bote': (150, 200, 0),
        'Fondo': (0, 0, 0)
    }

#* YOLO'S function
def detection_model_YOLO(frame, results, threshold = 0.6):
        for i, result in enumerate(results.boxes.data.tolist()):
            x1, y1, x2, y2, score, class_id = result
            print(score)
            
            if score > threshold:
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                print('Coordenadas de la BB: ',x1,y1,x2,y2)
                print('Confianza: ', score)
                print('Etiqueta: ', class_id)
                
                if class_id == 0:
                    class_id = "Bote"                
                elif class_id == 1:
                    class_id = "Bus"
                elif class_id == 2:
                    class_id = "Camion"
                elif class_id == 3:
                    class_id = "Carro"
                elif class_id == 4:
                    class_id = "Helicoptero"
                else:
                    class_id = 'Fondo'
                
                color_bb = clases_colores.get(class_id, (255, 0, 0))
                
                # Sobre las filas para que no quede por fuera el rectangulo
                cv2.rectangle(frame, (x1,y1),(x2,y2), color_bb, 2)
                cv2.putText(frame, (class_id), (x1,y1-5), cv2.FONT_HERSHEY_SIMPLEX, 1, color_bb, 3, cv2.LINE_AA)
                
        return frame

#* Real time function
def start_real_time_detect():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640,640))
        cv2.imshow('frame', frame)
        results = modelo_V8n.predict(frame)[0]
        frame = detection_model_YOLO(frame, results)
        cv2.imshow('frame', frame)
        
        # Press 'q' to close the capture
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    # Releases resources
    cap.release()
    cv2.destroyAllWindows()

#* Image's function
def detection_archives():
    archivo = filedialog.askopenfilename(
        title="Seleccione archivo de vídeo o foto",
        filetypes=[
            ("Archivos de imagen", "*.jpg"),
            ("Archivos de imagen", "*.jpeg"),
            ("Archivos de imagen", "*.png"),
            ("Archivos de video", "*.mp4")
        ]
    )

    # Verify
    if archivo:
        # Show the archive selection
        print(f"Archivo seleccionado: {archivo}")
        
        # Verify if the archive is an image or video file
        try:
            # opened the image file
            img = Image.open(archivo)
            img.thumbnail((1024, 1024)) 
            
            # Convert the image to a format that can be processed by OpenCV
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            results = modelo_V8n.predict(frame)[0]
            imagen = detection_model_YOLO(frame, results)
            cv2.imshow("Detección", imagen)
            cv2.waitKey(0)  # Wait until a key is pressed
            cv2.destroyAllWindows()  # Close OpenCV window

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")
    else:
        messagebox.showinfo("Cancelado", "No se seleccionó ningún archivo")




