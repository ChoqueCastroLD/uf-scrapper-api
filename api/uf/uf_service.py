from pyquery import PyQuery as pq
from api.error_handling.errors import NotFoundError
import requests

def get_uf_value(date):
    url = f"https://www.sii.cl/valores_y_fechas/uf/uf{date.year}.htm"
    response = requests.get(url)
    doc = pq(response.content)
    table = doc(f"#mes_all table")
    row = table(f"tr:nth-child({date.day})")
    data = row(f"td:nth-child({date.month + 1})")
    uf_value_text = data.text().replace(".", "").replace(",", ".")
    if not uf_value_text:
        raise NotFoundError("Valor de la UF no encontrado para la fecha especificada")
    uf_value = float(uf_value_text)
    return uf_value

