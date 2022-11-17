import streamlit as st
with st.sidebar:
  st.title("¡Bienvenido a tu app de Salud Mental!")
  st.image("https://www.uam.es/uam/media/imgl/1606893115743/2022-03-07-cabello-img.jpg")
  st.write("La salud mental tiene un impacto directo en nuestra forma de pensar, sentir y actuar. Determina cómo respondemos ante el estrés, cómo nos relacionamos con otras personas y cómo tomamos decisiones. Es por esto tan importante cuidar de ella como cuidamos de nuestro cuerpo físico. 😃")

st.header ("*¡Infórmate más!*")
st.write("Haz click en cada una de las cajas que se muestran a continuación ")

Ansiedad = st.checkbox('Ansiedad')

if Ansiedad:
    st.write('La ansiedad puede ser normal en situaciones estresantes, cómo hablar en público o realizar una prueba. La ansiedad es solo un indicador de una enfermedad subyacente cuando los sentimientos se vuelven excesivos en todo momento e interfieren con la vida cotidiana.')
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnWzwMwIViwoH_SORLvxn_ISqQ2rgT3g7EQLTGujuUYQ&s")
    st.write("Desliza la barra según tus emociones (dónde cero representa lo mínimo y cinco lo máximo)")
    miedo=st.slider("¿Has sentido miedo ultimamente?", 0, 5)
    if miedo==(1):
      st.write("Bien sigue a si")
    if miedo==(2):
      st.write("Amigo algo esta raro")
    if miedo==(3):
      st.write("Checate porfavor")
    if miedo==(4):
      st.write("Pide ayuda porfa")
    if miedo==(5):
      st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
    angustia=st.slider("¿Has sentido angustia?", 0, 5)
    if angustia==(1):
      st.write("Bien sigue a si")
    if angustia==(2):
      st.write("Amigo algo esta raro")
    if angustia==(3):
      st.write("Checate porfavor")
    if angustia==(4):
      st.write("Pide ayuda porfa")
    if angustia==(5):
      st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
    concentracion=st.slider("¿Tienes problemas para concentrarte?", 0, 5)
    if concentracion==(1):
      st.write("Bien sigue a si")
    if concentracion==(2):
      st.write("Amigo algo esta raro")
    if concentracion==(3):
      st.write("Checate porfavor")
    if concentracion==(4):
      st.write("Pide ayuda porfa")
    if concentracion==(5):
      st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
    memoria=st.slider("Dificultad para recordar cosas", 0, 5)
    if memoria==(1):
      st.write("Bien sigue a si")
    if memoria==(2):
      st.write("Amigo algo esta raro")
    if memoria==(3):
      st.write("Checate porfavor")
    if memoria==(4):
      st.write("Pide ayuda porfa")
    if memoria==(5):
      st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
    pensamientos=st.slider("¿Has tenido pensamientos o imagenes catastróficas?", 0, 5)
    if pensamientos==(1):
      st.write("Bien sigue a si")
    if pensamientos==(2):
      st.write("Amigo algo esta raro")
    if pensamientos==(3):
      st.write("Checate porfavor")
    if pensamientos==(4):
      st.write("Pide ayuda porfa")
    if pensamientos==(5):
      st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
    st.write("*¡Si quieres saber más, haz click en el siguiente enlace!*")
    st.write("https://youtu.be/34ZVrmJxEUo")

Depresión=st.checkbox("Depresión")

if Depresión:
  st.write("La depresión es un trastorno mental caracterizado fundamentalmente por un bajo estado de ánimo y sentimientos de tristeza, asociados a alteraciones del comportamiento, del grado de actividad y del pensamiento.")
  st.write("Desliza la barra según tus emociones (dónde cero representa lo mínimo y diez lo máximo)")
  desanimado=st.slider("¿Te has sentido desanimado, deprimido ó sin esperanza?", 0, 5)
  if desanimado==(1):
      st.write("Bien sigue a si")
  if desanimado==(2):
      st.write("Amigo algo esta raro")
  if desanimado==(3):
      st.write("Checate porfavor")
  if desanimado==(4):
      st.write("Pide ayuda porfa")
  if desanimado==(5):
    st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
  placer=st.slider("¿Sientes poco interes o placer en hacer algunas cosas?", 0, 5)
  if placer==(1):
      st.write("Bien sigue a si")
  if placer==(2):
      st.write("Amigo algo esta raro")
  if placer==(3):
      st.write("Checate porfavor")
  if placer==(4):
      st.write("Pide ayuda porfa")
  if placer==(5):
    st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
  dormir=st.slider("¿Duermes demasiado, o incluso tienes problemas en dormirte?", 0, 5)
  if dormir==(1):
      st.write("Bien sigue a si")
  if dormir==(2):
      st.write("Amigo algo esta raro")
  if dormir==(3):
      st.write("Checate porfavor")
  if dormir==(4):
      st.write("Pide ayuda porfa")
  if dormir==(5):
    st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
  pensamientos=st.slider("¿Has pensado en la muerte?", 0, 5)
  if pensamientos==(1):
      st.write("Bien sigue a si")
  if pensamientos==(2):
      st.write("Amigo algo esta raro")
  if pensamientos==(3):
      st.write("Checate porfavor")
  if pensamientos==(4):
      st.write("Pide ayuda porfa")
  if pensamientos==(5):
    st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
  amor=st.slider("Falta de amor propio, aprecio hacia amigos o familiares", 0, 5)
  if amor==(1):
      st.write("Bien sigue a si")
  if amor==(2):
      st.write("Amigo algo esta raro")
  if amor==(3):
      st.write("Checate porfavor")
  if amor==(4):
      st.write("Pide ayuda porfa")
  if amor==(5):
    st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
  st.write("*¡Si quieres saber más, haz click en el siguiente enlace!*")
  st.write("https://youtu.be/vJHYZL-KADg")

Estrés=st.checkbox("Estrés")

if Estrés:
  st.write("El estrés es la respuesta física o mental a una causa externa, como tener muchas tareas o padecer una enfermedad. Un estresor o factor estresante puede ser algo que ocurre una sola vez o a corto plazo, o puede suceder repetidamente durante mucho tiempo.")
  st.write("Desliza la barra según tus emociones (dónde cero representa lo mínimo y cinco lo máximo)")
  ahogo=st.slider("Sensación de ahogo", 0, 5)
  if ahogo==(1):
      st.write("Bien sigue a si")
  if ahogo==(2):
      st.write("Amigo algo esta raro")
  if ahogo==(3):
      st.write("Checate porfavor")
  if ahogo==(4):
      st.write("Pide ayuda porfa")
  if ahogo==(5):
    st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
  comer=st.slider("Mayor necesidad de comer", 0, 5)
  if comer==(1):
      st.write("Bien sigue a si")
  if comer==(2):
      st.write("Amigo algo esta raro")
  if comer==(3):
      st.write("Checate porfavor")
  if comer==(4):
      st.write("Pide ayuda porfa")
  if comer==(5):
    st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
  temblores=st.slider("Temblores o TICs", 0, 5)
  if temblores==(1):
      st.write("Bien sigue a si")
  if temblores==(2):
      st.write("Amigo algo esta raro")
  if temblores==(3):
      st.write("Checate porfavor")
  if temblores==(4):
      st.write("Pide ayuda porfa")
  if temblores==(5):
    st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
  calma=st.slider("Dificultad para mantener la calma", 0, 5)
  if calma==(1):
      st.write("Bien sigue a si")
  if calma==(2):
      st.write("Amigo algo esta raro")
  if calma==(3):
      st.write("Checate porfavor")
  if calma==(4):
      st.write("Pide ayuda porfa")
  if calma==(5):
    st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
  dolores=st.slider("Dolores de cabeza o abdominales constantes", 0, 5)
  if dolores==(1):
      st.write("Bien sigue a si")
  if dolores==(2):
      st.write("Amigo algo esta raro")
  if dolores==(3):
      st.write("Checate porfavor")
  if dolores==(4):
      st.write("Pide ayuda porfa")
  if dolores==(5):
    st.write("Urgue que tomes ayuda comunicate con los numeros proporcionados para la ayuda mental")
  st.write("*¡Si quieres saber más, haz click en el siguiente enlace!*")
  st.write("https://youtu.be/r0mQj2Y_sqI")


SaludMental=st.radio("¿Alguna vez has recibido algún tratamiento psicológico?", ["SI", "NO"])
if SaludMental== "SI":
  st.write("En las sesiones de terapia psicológica, se puede trabajar el desarrollo de habilidades y estrategias que nos ayuden a reducir o controlar los eventos estresantes o los cambios vitales. Además, la terapia resulta sumamente útil para identificar nuevos objetivos y desarrollar un plan para lograrlos. La Universidad Autónoma de Chihuahua a través del DAIE cuenta con un equipo profesional de psicólogos que brindan atención a las y los estudiantes universitarios de manera permanente y gratuita. Para agendar una cita puedes comunicarte al teléfono (614) 4391520 en la extensión 8011.")
if SaludMental== "NO":
  st.write("Si conoces a alguien que requiera ayuda con su salud mental comuncarse a (614) 4391520 en la extensión 8011")
col1,col2,col3=st.columns( [1,2,3] )

st.header ("*¿Sabías que condiciones mentales cómo la depresión incrementan el riesgo de padecer enfermedades físicas como diabetes?*")

