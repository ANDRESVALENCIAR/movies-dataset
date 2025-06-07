import streamlit as st

st.set_page_config(page_title="Registro Solicitudes Recibidas", page_icon="📝")
st.title("Registro Solicitudes Recibidas - Guardada Pendiente RCR")

with st.form("registro_form"):
    proviene = st.text_input("Proviene")
    no_tarea_pre = st.text_input("No. Tarea-Pre")
    crear_tarea_pre = st.checkbox("Crear una Tarea Pre")
    no_llamada = st.text_input("No. Llamada", "1987362")
    remitente = st.text_input("Recibió o Remitente", "AFV")
    fecha_llamada = st.text_input("Fecha llamada", "06/06/2025 21:45:40")
    asignado_a = st.text_input("Asignado a")
    email = st.text_input("E-mail", "3013209882@nocorreo.com")
    cotizar = st.checkbox("Cotizar")
    editar_contacto = st.checkbox("Editar Contacto")
    tipo_contacto = st.radio("Tipo de contacto", ["Cliente", "Otro"], index=0)
    nit = st.text_input("Nit")
    nombre_contacto = st.text_input("Nombre Contacto")
    nombre_empresa = st.text_input("Nombre Empresa", "IPCF SAS")
    celular = st.text_input("Celular", "3013209882")
    telefono = st.text_input("Teléfono")
    telefono2 = st.text_input("Teléfono 2")
    ciudad = st.text_input("Ciudad")
    pais = st.text_input("País", "Colombia")
    vendedor = st.text_input("Vendedor", "Manuela Trujillo")
    asunto = st.selectbox(
        "Asunto",
        ["Solicitud de Cotización", "Otra solicitud o Mensaje"],
        index=0,
    )
    link_bitrix = st.text_input("Link Bitrix Negociacion", "BitrixNegociacion")
    otro_link = st.text_input("Otro Link", "Otro Link")
    solicitud = st.text_area("Solicitud o Mensaje")
    observaciones = st.text_area("Observaciones")
    estado_llamada = st.selectbox(
        "Estado llamada",
        ["PENDIENTE", "ATENDIDA", "CERRADA"],
        index=0,
    )
    cotizacion1 = st.text_input("Cotizacion #1")
    cotizacion2 = st.text_input("Cotizacion #2")
    sfe = st.text_input("sfe #")
    prioridad = st.selectbox(
        "Prioridad",
        ["ALTA", "MEDIA", "BAJA"],
        index=1,
    )

    submitted = st.form_submit_button("Guardar")

if submitted:
    st.success("Solicitud guardada")
    st.write("### Resumen")
    st.write(
        {
            "Proviene": proviene,
            "No. Tarea-Pre": no_tarea_pre,
            "Crear Tarea Pre": crear_tarea_pre,
            "No. Llamada": no_llamada,
            "Recibió o Remitente": remitente,
            "Fecha llamada": fecha_llamada,
            "Asignado a": asignado_a,
            "E-mail": email,
            "Cotizar": cotizar,
            "Editar Contacto": editar_contacto,
            "Tipo contacto": tipo_contacto,
            "Nit": nit,
            "Nombre Contacto": nombre_contacto,
            "Nombre Empresa": nombre_empresa,
            "Celular": celular,
            "Teléfono": telefono,
            "Teléfono 2": telefono2,
            "Ciudad": ciudad,
            "País": pais,
            "Vendedor": vendedor,
            "Asunto": asunto,
            "Link Bitrix Negociacion": link_bitrix,
            "Otro Link": otro_link,
            "Solicitud o Mensaje": solicitud,
            "Observaciones": observaciones,
            "Estado llamada": estado_llamada,
            "Cotizacion #1": cotizacion1,
            "Cotizacion #2": cotizacion2,
            "sfe #": sfe,
            "Prioridad": prioridad,
        }
    )
