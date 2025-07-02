import os
import tempfile
from django.utils import timezone
from django.db import transaction
from imapclient import IMAPClient
import pyzmail
from lxml import etree
from gestionProveedores.models.factura import Factura
from gestionProveedores.models import Correo, ArchivoAdjunto
from django.conf import settings

EMAIL_HOST = 'imap.gmail.com'
EMAIL_USER = 'programador1@redmedicronips.com.co'
EMAIL_PASS = 'pdyx mklo dcli sduu'

def process_emails():
    with IMAPClient(EMAIL_HOST, ssl=True) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.select_folder('INBOX', readonly=True)

        messages = server.search(['ALL'])

        for uid in messages:
            # ✅ Verificar si ya lo guardamos
            exists = Correo.objects.filter(uid=uid).exists()
            if exists:
                print(f"Correo con UID {uid} ya existe. Saltando...")
                continue

            raw_message = server.fetch([uid], ['RFC822'])[uid][b'RFC822']
            message = pyzmail.PyzMessage.factory(raw_message)

            subject = message.get_subject()
            from_email = message.get_addresses('from')[0][1]

            body = ""
            if message.text_part:
                body = message.text_part.get_payload().decode(message.text_part.charset or 'utf-8')
            elif message.html_part:
                body = message.html_part.get_payload().decode(message.html_part.charset or 'utf-8')

            correo_obj = Correo.objects.create(
                subject=subject,
                from_email=from_email,
                date_received=timezone.now(),
                raw_message=body,
                uid=uid  # ✅ Guardamos UID
            )

            archivos_nombres = []

            for part in message.mailparts:
                filename = part.filename
                if filename:
                    archivos_nombres.append(filename)

                    payload = part.get_payload()

                    file_path = os.path.join(settings.MEDIA_ROOT, 'adjuntos', filename)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    with open(file_path, 'wb') as f:
                        f.write(payload)

                    ArchivoAdjunto.objects.create(
                        correo=correo_obj,
                        nombre_archivo=filename,
                        archivo=f'adjuntos/{filename}'
                    )

                    if filename.lower().endswith('.xml'):
                        with tempfile.NamedTemporaryFile(delete=False, suffix='.xml') as tmp_file:
                            tmp_file.write(payload)
                            tmp_file_path = tmp_file.name

                        factura_data = process_xml(tmp_file_path)
                        if factura_data:
                            save_factura(factura_data, subject, from_email)

                        os.unlink(tmp_file_path)

            correo_obj.archivos = ", ".join(archivos_nombres)
            correo_obj.save()

def process_xml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()

        if '<?' in xml_content and '<' in xml_content:
            start_idx = xml_content.find('<')
            xml_content = xml_content[start_idx:]

        xml_content = xml_content.replace('?>|', '?>')
        xml_content = xml_content.replace('</ ', '</')

        root = etree.fromstring(xml_content.encode('utf-8'))

        registro = root.find('.//RegistroFT006')
        if registro is None:
            return None

        data = {
            'factura_id_factura_electronica': registro.findtext('IdFacturaElectronica', ''),
            'factura_numero_autorizacion': registro.findtext('NumeroAutorizacion', ''),
            'factura_razon_social_proveedor': registro.findtext('RazonSocialProveedor', ''),
            'factura_razon_social_adquiriente': registro.findtext('RazonSocialAdquiriente', ''),
            'factura_valor': float(registro.findtext('ValorTotal', '0')),
            'factura_fecha': registro.findtext('FechaFactura', None),
        }
        return data

    except Exception as e:
        print(f"Error procesando XML: {e}")
        return None

@transaction.atomic
def save_factura(data, subject, from_email):
    factura = Factura.objects.create(
        factura_id_factura_electronica=data.get('factura_id_factura_electronica'),
        factura_numero_autorizacion=data.get('factura_numero_autorizacion'),
        factura_razon_social_proveedor=data.get('factura_razon_social_proveedor'),
        factura_razon_social_adquiriente=data.get('factura_razon_social_adquiriente'),
        factura_valor=data.get('factura_valor', 0),
        factura_fecha=data.get('factura_fecha') or timezone.now().date(),
        factura_concepto=f"Correo de {from_email} - Asunto: {subject}",
    )
    print(f"Factura guardada: {factura}")
