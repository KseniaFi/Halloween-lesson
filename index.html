<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Halloween Matching Task</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <style>
        /* Сброс стилей и базовые настройки */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Times New Roman', serif;
            background-color: #f5f5f5;
            padding: 20px;
            color: #333;
            width: 100%;
        }
        
        /* Основной контейнер, который будет преобразован в PDF */
        #pdf-content {
            width: 794px; /* A4 width in pixels at 96dpi */
            min-height: 1123px; /* A4 height in pixels at 96dpi */
            margin: 0 auto;
            padding: 30px;
            background-color: white;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            position: relative;
            display: flex;
            flex-direction: column;
        }
        
        /* Заголовок */
        h1 {
            text-align: center;
            color: #8B4513;
            font-size: 32px;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid #8B4513;
        }
        
        /* Инструкции */
        .instructions {
            text-align: center;
            font-size: 16px;
            margin-bottom: 20px;
            color: #5a3921;
            line-height: 1.4;
        }
        
        /* Область для сопоставления */
        .matching-area {
            flex: 1;
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            gap: 20px;
        }
        
        /* Колонки */
        .column {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        
        .column-title {
            text-align: center;
            font-size: 20px;
            margin-bottom: 15px;
            color: #8B4513;
            font-weight: bold;
        }
        
        /* Карточки */
        .card {
            border: 2px solid #8B4513;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #fff8e1;
            break-inside: avoid;
            page-break-inside: avoid;
            flex: 1;
            margin-bottom: 10px;
        }
        
        .image-card {
            background-color: #f9f9f9;
            min-height: 0; /* Важно для flex-распределения */
        }
        
        .image-card img {
            max-width: 90%;
            max-height: 90%;
            display: block;
            object-fit: contain;
        }
        
        .word-card {
            font-size: 18px;
            font-weight: bold;
            color: #8B4513;
            text-align: center;
            padding: 5px;
            word-wrap: break-word;
            min-height: 0; /* Важно для flex-распределения */
        }
        
        /* Область для подписи */
        .signature-area {
            padding-top: 15px;
            border-top: 1px dashed #8B4513;
            display: flex;
            justify-content: space-between;
        }
        
        .signature-line {
            width: 180px;
            border-bottom: 1px solid #8B4513;
            text-align: center;
            padding-top: 20px;
            font-size: 14px;
            color: #666;
        }
        
        /* Кнопка загрузки */
        .button-container {
            text-align: center;
            margin-top: 20px;
        }
        
        button {
            background-color: #8B4513;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        button:hover {
            background-color: #a0522d;
        }
        
        /* Заглушка для изображений */
        .placeholder {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            width: 100%;
            color: #666;
            font-size: 14px;
            text-align: center;
            padding: 10px;
        }
        
        /* Стили для печати */
        @media print {
            body {
                padding: 0;
                background: white;
            }
            
            #pdf-content {
                box-shadow: none;
                margin: 0;
                padding: 25px;
                width: 100%;
                height: 100%;
            }
            
            .button-container {
                display: none;
            }
        }
    </style>
</head>
<body>
    <!-- Контейнер, который будет преобразован в PDF -->
    <div id="pdf-content">
        <h1>Halloween Matching Task</h1>
        <p class="instructions">Match the Halloween images on the left with the correct words on the right by drawing lines between them.</p>
        
        <div class="matching-area">
            <!-- Левая колонка с изображениями -->
            <div class="column">
                <div class="column-title">Images</div>
                <div id="images-column" class="column-content">
                    <!-- Карточки с изображениями будут сгенерированы здесь -->
                </div>
            </div>
            
            <!-- Правая колонка со словами -->
            <div class="column">
                <div class="column-title">Words</div>
                <div id="words-column" class="column-content">
                    <!-- Карточки со словами будут сгенерированы здесь -->
                </div>
            </div>
        </div>
        
        <div class="signature-area">
            <div class="signature-line">Name: ___________________</div>
            <div class="signature-line">Date: ___________________</div>
            <div class="signature-line">Score: ___________________</div>
        </div>
    </div>

    <div class="button-container">
        <button id="download-pdf">Download PDF</button>
    </div>

    <script>
        // Данные для карточек
        const halloweenItems = [
            { image: "Photos/IMG_20251020_175109_595.jpg", label: "Monster" },
            { image: "Photos/IMG_20251020_123050_219.jpg", label: "Spider" },
            { image: "Photos/IMG_20251020_122957_466.jpg", label: "Mummy" },
            { image: "Photos/IMG_20251019_161943_247.jpg", label: "Wizard" },
            { image: "Photos/IMG_20251019_161657_379.jpg", label: "Scarecrow" },
            { image: "Photos/IMG_20251019_161133_941.jpg", label: "Fireworks" },
            { image: "Photos/IMG_20251019_161047_687.jpg", label: "Bat" },
            { image: "Photos/IMG_20251019_160956_540.jpg", label: "Vampire" },
            { image: "Photos/IMG_20251019_160820_005.jpg", label: "Ghost" },
            { image: "Photos/IMG_20251019_160644_141.jpg", label: "Witch" },
            { image: "Photos/IMG_20251019_160545_015.jpg", label: "Jack-o'-lantern" },
            { image: "Photos/IMG_20251020_192659_254.jpg", label: "Pumpkin" }
        ];

        // Функция для перемешивания массива
        function shuffleArray(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
            return array;
        }

        // Генерация карточек
        function generateCards() {
            const imagesColumn = document.getElementById('images-column');
            const wordsColumn = document.getElementById('words-column');

            // Создаем карточки с изображениями (в исходном порядке)
            halloweenItems.forEach(item => {
                const card = document.createElement('div');
                card.className = 'card image-card';
                
                const img = document.createElement('img');
                img.src = item.image;
                img.alt = item.label;
                
                // Обработчик на случай, если изображение не загрузится
                img.onerror = function() {
                    this.style.display = 'none';
                    const placeholder = document.createElement('div');
                    placeholder.className = 'placeholder';
                    placeholder.textContent = item.label;
                    card.appendChild(placeholder);
                };
                
                card.appendChild(img);
                imagesColumn.appendChild(card);
            });

            // Создаем карточки со словами (в случайном порядке)
            const shuffledWords = shuffleArray([...halloweenItems.map(item => item.label)]);
            
            shuffledWords.forEach(word => {
                const card = document.createElement('div');
                card.className = 'card word-card';
                card.textContent = word;
                wordsColumn.appendChild(card);
            });
        }

        // Обработчик кнопки для генерации PDF
        document.getElementById('download-pdf').addEventListener('click', function() {
            const element = document.getElementById('pdf-content');
            
            // Конфигурация для html2pdf
            const options = {
                margin: [10, 10, 10, 10],
                filename: 'Halloween_Matching_Task.pdf',
                image: { 
                    type: 'jpeg', 
                    quality: 0.98 
                },
                html2canvas: { 
                    scale: 2,
                    useCORS: true,
                    logging: false,
                    width: 794, // Фиксированная ширина A4
                    height: 1123, // Фиксированная высота A4
                    windowWidth: 794
                },
                jsPDF: { 
                    unit: 'mm', 
                    format: 'a4', 
                    orientation: 'portrait'
                }
            };

            // Создание и сохранение PDF
            html2pdf().set(options).from(element).save();
        });

        // Инициализация при загрузке страницы
        window.onload = generateCards;
    </script>
</body>
</html>
