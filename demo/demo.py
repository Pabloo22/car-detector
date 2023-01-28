"""
DEMO DE LA LIBRERIA DE DETECCIÓN DE COCHES
Autores: Pablo Ariño y Jorge de la Rosa
Fecha: 28/01/2023


A  continuación  presentamos una libreria de detección de coches en un  video. Para ello, hemos  empleado
dos métodos: Un método clásico y un método con redes neuronales. Empezaremos explicando el método clásico.
En el video generado resaltamos los coches y con una linea roja denotamos su recorrido en el vídeo.
"""

from src import Processor, Tracker
from src.car_detectors import ClassicDetector, YoloDetector

# Ruta al video de prueba utilizado
RUTA_VIDEO = 'data/video.avi'
RUTA_NUEVO_VIDEO_CLASSIC = 'data/new_video_classic_detector.avi'
RUTA_NUEVO_VIDEO_YOLO = 'data/new_video_yolo_detector.avi'


def detector_clasico():
    """
    __MÉTODO CLÁSICO__
    Para el método  clásico  hemos hecho  lo siguiente. Primero,  hemos tomado dos frames del video, los pasamos a escala de
    grises y realizamos la diferencia entre estos fotogramas. De esta forma capturamos el movimiento de un frame a otro.
    Luego, con el resultado de esa diferencia  apreciamos los  coches en blanco, por lo que con un filtro de unos de dimensiones
    5x5 realizamos una dilatación a la imagen para obtener estructuras cuadradas en vez de coches, y  capturar de esta forma
    todos los pixeles separados y que queden unidos. A continuación, aplicamos un blur a la imagen para eliminar los pixeles
    diminutos que existan en la imagen y suavizar los bordes. Por último, detectamos  el contorno de las 'manchas blancas' y
    dibujamos un cuadrado alrededor.
    """
    # Importamos el detector clásico
    car_detector = ClassicDetector()

    # Creamos un objeto Processor
    app = Processor(car_detector, video_path=RUTA_VIDEO)

    # Generamos el video procesado
    new_video = app.process_video(n_jobs=1)

    # Guardamos el video
    # new_video.save(RUTA_NUEVO_VIDEO)

    # Visualizamos el video generado
    new_video.visualize()


def detector_yolo():
    """
    __MÉTODO REDES NEURONALES__
    Para el método con redes neuronales hemos aplicado el algoritmo de YOLOv5 para detección de coches. Hemos cargado
    directamente un repositorio de github donde está el modelo entrenado y lo hemos aplicado en el programa. Como se podrá
    ver, el algoritmo es relativamente más lento en ejecutar (3-10 min) en CPU, por lo que lo dejamos comentado por este motivo.
    En caso de querer comprobar su funcionamiento, descomente el código.
    """
    # Importamos el detector YOLOv5
    car_detector = YoloDetector()

    # Creamos un objeto Tracker para modificar los parametros por defecto
    tracker = Tracker(min_trace_length=12)
    
    # Creamos un objeto Processor
    app = Processor(car_detector, video_path=RUTA_VIDEO, tracker=tracker)

    # Generamos el video procesado
    new_video = app.process_video(n_jobs=-1)

    # Guardamos el video
    new_video.save(RUTA_NUEVO_VIDEO_YOLO)

    # Visualizamos el video generado
    new_video.visualize()


if __name__ == '__main__':
    detector_clasico()
    # detector_yolo()
