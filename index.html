<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Halloween Matching Task</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        body {
            font-family: 'Times New Roman', serif;
            background-color: #f5f5f5;
            padding: 20px;
            margin: 0;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #8B4513;
            font-size: 36px;
            margin-bottom: 30px;
        }
        .cards-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
        }
        .card {
            width: 200px;
            height: 250px;
            border: 2px solid #8B4513;
            border-radius: 10px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .card-image {
            height: 70%;
            background-color: #f0f0f0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            color: #666;
        }
        .card-label {
            height: 30%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
            color: #8B4513;
            background-color: #FFF8DC;
        }
        .button-container {
            text-align: center;
            margin-top: 20px;
        }
        button {
            background-color: #8B4513;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 18px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #A0522D;
        }
    </style>
</head>
<body>
    <div class="container" id="content">
        <h1>Halloween Matching Task</h1>
        <div class="cards-container" id="cardsContainer">
            <!-- Cards will be generated here -->
        </div>
    </div>
    <div class="button-container">
        <button id="downloadBtn">Download PDF</button>
    </div>

    <script>
        // Halloween items data
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

        // Shuffle the array to randomize order
        function shuffleArray(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
            return array;
        }

        // Generate cards
        function generateCards() {
            const container = document.getElementById('cardsContainer');
            const shuffledItems = shuffleArray([...halloweenItems]);
            
            shuffledItems.forEach(item => {
                const card = document.createElement('div');
                card.className = 'card';
                
                const imageDiv = document.createElement('div');
                imageDiv.className = 'card-image';
                // In a real implementation, you would use the actual image
                // imageDiv.style.backgroundImage = `url(${item.image})`;
                // imageDiv.style.backgroundSize = 'cover';
                // imageDiv.style.backgroundPosition = 'center';
                
                // For demonstration, we'll show the image path
                imageDiv.textContent = item.image.split('/').pop();
                
                const labelDiv = document.createElement('div');
                labelDiv.className = 'card-label';
                labelDiv.textContent = item.label;
                
                card.appendChild(imageDiv);
                card.appendChild(labelDiv);
                container.appendChild(card);
            });
        }

        // Download as PDF
        document.getElementById('downloadBtn').addEventListener('click', function() {
            const { jsPDF } = window.jspdf;
            const doc = new jsPDF('p', 'mm', 'a4');
            const element = document.getElementById('content');
            
            html2canvas(element, {
                scale: 2,
                useCORS: true
            }).then(canvas => {
                const imgData = canvas.toDataURL('image/png');
                const imgWidth = 210; // A4 width in mm
                const pageHeight = 295; // A4 height in mm
                const imgHeight = canvas.height * imgWidth / canvas.width;
                let heightLeft = imgHeight;
                
                let position = 0;
                
                doc.addImage(imgData, 'PNG', 0, position, imgWidth, imgHeight);
                heightLeft -= pageHeight;
                
                while (heightLeft >= 0) {
                    position = heightLeft - imgHeight;
                    doc.addPage();
                    doc.addImage(imgData, 'PNG', 0, position, imgWidth, imgHeight);
                    heightLeft -= pageHeight;
                }
                
                doc.save('halloween-matching-task.pdf');
            });
        });

        // Initialize the page
        window.onload = generateCards;
    </script>
</body>
</html>
