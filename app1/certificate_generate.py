from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from datetime import datetime

@login_required
def generate_certificate_nr20(request):
    last_name = request.user.last_name
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Certificação em Nr20.pdf"'
    
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d/%m/%Y")

    p = canvas.Canvas(response, pagesize=landscape(letter))
    
    p.setFillColorRGB(1, 1, 1)
    p.rect(0, 0, landscape(letter)[0], landscape(letter)[1], fill=True, stroke=False)

    image_path = './static/assets/capacete-fundobranco.png'
    image_width = 150
    image_height = 100
    p.drawImage(image_path, 20, landscape(letter)[1] - 120, width=image_width, height=image_height)

    image_path_rigth = './static/assets/qualidade.jpg'
    image_width_rigth = 150
    image_height_rigth = 100

    # Posição da imagem no canto superior direito
    image_x_rigth = landscape(letter)[0] - image_width_rigth - 20  # Subtrai a largura da imagem do limite direito da página
    image_y_rigth = landscape(letter)[1] - 120

    # Desenhe a imagem do image_path_rigth no canto superior direito
    p.drawImage(image_path_rigth, image_x_rigth, image_y_rigth, width=image_width_rigth, height=image_height_rigth)

    # Desenhe a faixa azul preenchendo toda a largura
    p.setFillColorRGB(0.15, 0.56, 1)
    p.rect(0, landscape(letter)[1] - 220, landscape(letter)[0], 50, fill=True, stroke=False)

    title_text = f"Certificação em NR20"
    title_text_width = p.stringWidth(title_text, "Helvetica-Bold", 30)
    title_text_x = (landscape(letter)[0] - title_text_width) / 2
    p.setFillColorRGB(0, 0, 0)
    p.setFont("Helvetica-Bold", 30)
    p.drawString(title_text_x, landscape(letter)[1] - 200, title_text)
    
    student_text = f"ESTE CERTIFICADO COMPROVA QUE"
    student_text_width = p.stringWidth(student_text, "Helvetica", 12)
    student_text_x = (landscape(letter)[0] - student_text_width) / 2
    p.setFont("Helvetica", 12)
    p.drawString(student_text_x, landscape(letter)[1] - 270, student_text)
    
    student_name = "Aluno(a): "

    # Calcule a largura total do título combinado
    student_name_width = p.stringWidth(student_name, "Helvetica", 12)

    # Calcule a posição x para centralizar o título combinado
    student_name_x = (landscape(letter)[0] - student_name_width) / 2

    # Desenhe o título combinado centralizado
    p.drawString(student_name_x, landscape(letter)[1] - 300, student_name)

    # Aumente o tamanho da fonte do sobrenome
    # Calcule a largura do sobrenome
    student_last_name_width = p.stringWidth(last_name, "Helvetica", 20)

    # Calcule a posição x para centralizar o sobrenome
    student_last_name_x = (landscape(letter)[0] - student_last_name_width) / 2

    # Desenhe o sobrenome centralizado
    p.setFont("Helvetica", 20)  # Defina o tamanho da fonte para o sobrenome
    p.drawString(student_last_name_x, landscape(letter)[1] - 330, last_name) 

    course_text = f"CONCLUIU COM ÊXITO O CURSO NR20 NA DATA: {formatted_datetime}, FORNECIDO PELA CURSOS-securitas" 
    course_text_width = p.stringWidth(course_text, "Helvetica", 12)
    course_text_x = (landscape(letter)[0] - course_text_width) / 2
    p.setFont("Helvetica", 12)  # Volte à fonte de tamanho 12 para o texto do curso
    p.drawString(course_text_x, landscape(letter)[1] - 360, course_text)

    course_text_2 = f"DURANTE SUA PARTICIPAÇÃO NO CURSO, DEMONSTROU UM NOTÁVEL COMPROMETIMENTO E DEDICAÇÃO, "
    course_text_2_width = p.stringWidth(course_text_2, "Helvetica", 12)
    course_text_2_x = (landscape(letter)[0] - course_text_2_width) / 2
    p.drawString(course_text_2_x, landscape(letter)[1] - 390, course_text_2)

    course_text_3 = f"DESTACANDO-SE PELO EMPENHO EXEMPLAR EM TODAS AS ATIVIDADES PROPOSTAS."
    course_text_3_width = p.stringWidth(course_text_3, "Helvetica", 12)
    course_text_3_x = (landscape(letter)[0] - course_text_3_width) / 2
    p.drawString(course_text_3_x, landscape(letter)[1] - 420, course_text_3)
    
    p.setLineWidth(1)
    p.setStrokeColorRGB(0, 0, 0)
    p.line(20, landscape(letter)[1] - 500, landscape(letter)[0] - 20, landscape(letter)[1] - 500)
    
    p.showPage()
    p.save()

    return response
