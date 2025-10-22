from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import random

def create_pdf():
    # Данные для задания
    tasks = [
        ("Photos/IMG_20251020_175109_595.jpg", "Monster"),
        ("Photos/IMG_20251020_123050_219.jpg", "Spider"),
        ("Photos/IMG_20251020_122957_466.jpg", "Mummy"),
        ("Photos/IMG_20251019_161943_247.jpg", "Wizard"),
        ("Photos/IMG_20251019_161657_379.jpg", "Scarecrow"),
        ("Photos/IMG_20251019_161133_941.jpg", "Fireworks"),
        ("Photos/IMG_20251019_161047_687.jpg", "Bat"),
        ("Photos/IMG_20251019_160956_540.jpg", "Vampire"),
        ("Photos/IMG_20251019_160820_005.jpg", "Ghost"),
        ("Photos/IMG_20251019_160644_141.jpg", "Witch"),
        ("Photos/IMG_20251019_160545_015.jpg", "Jack-o'-lantern"),
        ("Photos/IMG_20251020_192659_254.jpg", "Pumpkin")
    ]
    
    # Перемешиваем слова
    words = [task[1] for task in tasks]
    random.shuffle(words)
    
    # Создаем PDF
    c = canvas.Canvas("Matching_Task.pdf", pagesize=A4)
    width, height = A4
    
    # Добавляем фон (если файл существует)
    try:
        bg = ImageReader("Photos/IMG_20251020_193039_262.jpg")
        c.drawImage(bg, 0, 0, width=width, height=height)
        print("Фон добавлен")
    except:
        print("Фон не найден, продолжаем без фона")
    
    # Настройки
    IMAGE_SIZE = 80
    x_left = 50
    x_right = 300
    y_start = 700
    y_step = 50
    
    # Заголовок
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Matching Task - Connect images with words")
    
    # Создаем задания
    for i, (img_path, word) in enumerate(tasks):
        y_pos = y_start - i * y_step
        
        # Левая колонка - изображения
        try:
            img = ImageReader(img_path)
            c.drawImage(img, x_left, y_pos-IMAGE_SIZE/2, 
                       width=IMAGE_SIZE, height=IMAGE_SIZE)
        except:
            c.setFont("Helvetica", 8)
            c.drawString(x_left, y_pos, f"[{word}]")
        
        # Правая колонка - перемешанные слова
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x_right, y_pos, words[i])
        
        # Линия для ответов
        c.line(x_left + IMAGE_SIZE + 10, y_pos, x_right - 10, y_pos)
    
    c.save()
    print("✅ PDF создан: Matching_Task.pdf")

if __name__ == "__main__":
    create_pdf()
