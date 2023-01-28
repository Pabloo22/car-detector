# car-detector
El objetivo de este proyecto es desarrollar una herramienta que permita contar el número de coches que 
pasan en una determinada autopista. Para ello, se necesita únicamente de un vídeo de esta en el que se
pueda apreciar el paso de los diferentes vehículos. Esto puede ser de utilidad tanto a las autoridades 
encargadas de regular el tráfico como a aplicaciones de navegación.

Para lograr este objetivo se hace uso de diferentes clases:

* La clase `Preprocessor` se encarga de combinar los distintos elementos de la aplicación. A esta clase 
se le proporciona un vídeo en bruto y devuelve un vídeo que incluye los coches detectados junto a un 
contador de estos.
* La clase `Tracker` lleva el recuento de los diferentes coches que han aparecido en el vídeo. Esta clase 
se encarga de determinar si un coche detectado en un frame es el mismo que el detectado en el siguiente.
* Además, se utilizan distintos detectores de coches. En concreto, se han implementado dos de ellos. 
El primero es un detector basado en el algoritmo YOLOv5. El segundo hace uso de métodos clásicos y es 
con el que curiosamente se han conseguido mejores resultados en el vídeo estudiado.
* Por último, se ha creado un módulo `data_structures` en el que se almacenan varias estructuras de 
datos que se servirán de las clases anteriormente mencionadas. En particular, se ha implementado una clase 
`Frame`, una clase `Video` y una clase `Rectangle`.

## ¿Cómo funciona?
La detección de coches se aplica únicamente en una "zona de acción" especificada previamente por el usuario.

Una vez cargado el vídeo, se envían los frames secuencialmente\* al detector de coches. Este detector 
devolverá una lista de rectángulos en los que ha detectado un coche por cada frame. Esta información 
se pasa a la clase `Tracker` para que determine si se tratan de coches nuevos o si estaban previamente en 
frames anteriores. En este último caso se devuelve cuál ha sido su traza para que pueda ser dibujada. 

Para evitar falsos positivos, se hace uso de un hiperparámetro de la clase `Tracker` que determina 
un mínimo número de frames en los que debe aparecer un coche para sumar el contador de coches que han pasado.

En el caso del detector clásico, se hace uso además de un tamaño mínimo de contorno que evita la detección 
de objetos que no tienen el tamaño suficiente como para ser un coche.

\*La implementación actual está pensada para ser utilizada mediante una CPU. Sin embargo, se ha hecho uso
de la librería `multiprocessing` para que la detección de coches se pueda realizar en paralelo si la detección
de coches no depende de la detección de coches en frames anteriores. En caso de disponer de una GPU se podría
reducir el tiempo de detección de coches del detector YOLOv5 modificando ligeramente el código.

## ¿Cómo se usa?
Para reproducir los resultados disponibles: `data/new_video_classic_detector.avi` y 
`data/new_video_yolo_detector.avi`, clone el repositorio y ejecute el archivo `demo.py`. 

Para instalar las dependencias del proyecto, ejecute el siguiente comando en la raíz del proyecto:
```bash
pip install -r requirements.txt
```
