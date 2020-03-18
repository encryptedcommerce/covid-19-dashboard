from typing import Dict

from models.common import get_user_country


LOCALIZED_TEXT: Dict[str, Dict[str, str]] = {}  # versions of text snippets in various language

LOCALIZED_TEXT['en'] = {
    'summary-welcome': 'COVID-19 Interactive Dashboard',
    'summary-intro': 'This dashboard contains interactive visualization of COVID-19 data.',
    'summary-description': '''
        You may select countries to include in the charts.
        If detected, your country and others with similar statistics will be added by default,
        in addition to several countries with the highest statistics.
    ''',
    'data-credit': 'Data is provided by',
    'data-update': ', updated daily around 00:05 UTC',
    'geoip-credit': 'Geographic IP data:',
}

LOCALIZED_TEXT['es'] = {
    'summary-welcome': 'Panel interactivo de COVID-19',
    'summary-intro': 'Este panel contiene visualización interactiva de datos COVID-19.',
    'summary-description': '''
        Puede seleccionar países para incluir en los cuadros.
        Si se detecta, su país y otros con estadísticas similares se agregarán de forma predeterminada,
        además de varios países con las estadísticas más altas.
    ''',
    'data-credit': 'Los datos son proporcionados por',
    'data-update': ', actualizado diariamente alrededor de las 00:05 UTC',
    'geoip-credit': 'Datos geográficos de IP:',
}

LOCALIZED_TEXT['fr'] = {
    'summary-welcome': 'Tableau de bord interactif COVID-19',
    'summary-intro': 'Ce tableau de bord contient une visualisation interactive des données COVID-19.',
    'summary-description': '''
    Vous pouvez sélectionner les pays à inclure dans les graphiques.
         S'il est détecté, votre pays et d'autres pays ayant des statistiques similaires seront ajoutés par défaut,
         en plus de plusieurs pays avec les statistiques les plus élevées.
    ''',
    'data-credit': 'Les données sont fournies par',
    'data-update': ', mis à jour quotidiennement vers 00:05 UTC',
    'geoip-credit': 'Données IP géographiques:',
}

LOCALIZED_TEXT['it'] = {
    'summary-welcome': 'Pannello interattivo COVID-19',
    'summary-intro': 'Questa dashboard contiene una visualizzazione interattiva dei dati COVID-19.',
    'summary-description': '''
        È possibile selezionare i paesi da includere nei grafici.
        Se rilevato, il tuo Paese e altri con statistiche simili verranno aggiunti per impostazione predefinita,
        oltre a diversi paesi con le statistiche più alte.
    ''',
    'data-credit': 'I dati sono forniti da',
    'data-update': ', aggiornato quotidianamente intorno alle 00:05 UTC',
    'geoip-credit': 'Dati IP geografici:',
}

LOCALIZED_TEXT['de'] = {
    'summary-welcome': 'Interaktives COVID-19-Dashboard',
    'summary-intro': 'Dieses Dashboard enthält eine interaktive Visualisierung der COVID-19-Daten.',
    'summary-description': '''
        Sie können Länder auswählen, die in die Diagramme aufgenommen werden sollen.
        Wenn dies erkannt wird, werden Ihr Land und andere Länder mit ähnlichen Statistiken standardmäßig hinzugefügt.
        Neben mehreren Ländern mit den höchsten Statistiken.
    ''',
    'data-credit': 'Daten werden bereitgestellt von',
    'data-update': ', täglich aktualisiert um 00:05 UTC',
    'geoip-credit': 'Geografische IP-Daten:',
}

LOCALIZED_TEXT['pt'] = {
    'summary-welcome': 'Painel interativo COVID-19',
    'summary-intro': 'Este painel contém visualização interativa dos dados COVID-19.',
    'summary-description': '''
        Você pode selecionar países para incluir nos gráficos.
        Se detectado, seu país e outros com estatísticas semelhantes serão adicionados por padrão,
        além de vários países com as estatísticas mais altas.
    ''',
    'data-credit': 'Os dados são fornecidos por',
    'data-update': ', atualizado diariamente às 00:05 UTC',
    'geoip-credit': 'Dados IP geográficos:',
}

LOCALIZED_TEXT['ru'] = {
    'summary-welcome': 'COVID-19 Интерактивная панель инструментов',
    'summary-intro': 'Эта панель содержит интерактивную визуализацию данных COVID-19.',
    'summary-description': '''
        Вы можете выбрать страны для включения в диаграммы.
        В случае обнаружения ваша страна и другие страны с аналогичной статистикой будут добавлены по умолчанию,
        в дополнение к нескольким странам с самой высокой статистикой.
    ''',
    'data-credit': 'Данные предоставлены',
    'data-update': ', обновляется ежедневно около 00:05 UTC',
    'geoip-credit': 'Географические данные IP:',
}

LOCALIZED_TEXT['se'] = {
    'summary-welcome': 'COVID-19 Interaktiv instrumentpanel',
    'summary-intro': 'Denna instrumentbräda innehåller interaktiv visualisering av COVID-19-data.',
    'summary-description': '''
        Du kan välja länder som ska inkluderas i diagrammen.
        Om det upptäcks kommer ditt land och andra med liknande statistik att läggas till som standard,
        förutom flera länder med den högsta statistiken.
    ''',
    'data-credit': 'Data tillhandahålls av',
    'data-update': ', uppdateras dagligen runt 00:05 UTC',
    'geoip-credit': 'Geografiska IP-data:',
}

LOCALIZED_TEXT['cn'] = {
    'summary-welcome': 'COVID-19互动式仪表板',
    'summary-intro': '此仪表板包含COVID-19数据的交互式可视化。',
    'summary-description': '''
        您可以选择要包含在图表中的国家。
        如果检测到，默认情况下将添加您所在的国家/地区和统计相似的其他国家/地区，
        除了几个统计数字最高的国家。
    ''',
    'data-credit': '数据由',
    'data-update': '，每天在世界标准时间00:05左右更新',
    'geoip-credit': '地理IP数据：',
}

LOCALIZED_TEXT['jp'] = {
    'summary-welcome': 'COVID-19インタラクティブダッシュボード',
    'summary-intro': 'このダッシュボードには、COVID-19データのインタラクティブな視覚化が含まれています。',
    'summary-description': '''
        チャートに含める国を選択できます。
        検出された場合、あなたの国および同様の統計情報を持つ他の国がデフォルトで追加されます。
        最高の統計を持ついくつかの国に加えて。
    ''',
    'data-credit': 'データはによって提供されます',
    'data-update': '、毎日00:05 UTCに更新',
    'geoip-credit': '地理的IPデータ：',
}

LOCALIZED_TEXT['in'] = {
    'summary-welcome': 'COVID-19 इंटरएक्टिव डैशबोर्ड',
    'summary-intro': 'इस डैशबोर्ड में COVID-19 डेटा का इंटरैक्टिव विज़ुअलाइज़ेशन है।',
    'summary-description': '''
        आप चार्ट में शामिल करने के लिए देशों का चयन कर सकते हैं।
        यदि पता लगाया जाता है, तो आपका देश और अन्य समान आँकड़े डिफ़ॉल्ट रूप से जोड़े जाएंगे,
        उच्चतम आँकड़ों के साथ कई देशों के अलावा।
    ''',
    'data-credit': 'द्वारा डेटा प्रदान किया जाता है',
    'data-update': ', अद्यतन लगभग 00:05 यूटीसी',
    'geoip-credit': 'भौगोलिक IP डेटा:',
}

# mapping of country name to language code
LANG_MAP: Dict[str, str] = {}

automap = ['fr', 'it', 'de', 'ru', 'se', 'cn', 'jp', 'in']
for country in automap:
    LANG_MAP[country] = country

for country in ['co', 'es', 've', 'pe', 'mx']:
    LANG_MAP[country] = 'es'

for country in ['uk', 'us', 'au', 'ca']:
    LANG_MAP[country] = 'es'

for country in ['fr']:
    LANG_MAP[country] = 'fr'

for country in ['de']:
    LANG_MAP[country] = 'de'

for country in ['br', 'pt']:
    LANG_MAP[country] = 'pt'


def localize(snippet_id: str) -> str:
    """Looks up user's country and returns identified text snippet translated to user's language.

    Arguments:
        snippet_id: id of text snippet from `LOCALIZED_TEXT` dict.
    """
    user_country = get_user_country(country_code=True)
    print(f'-- localize({snippet_id} got user_country: {user_country}')
    if user_country not in LANG_MAP.keys():
        # User country is not in language map; return English by default
        lang = 'en'
    else:
        lang = LANG_MAP[user_country]

    if lang not in LOCALIZED_TEXT.keys():
        # Language is not in the snippets; set language to English
        lang = 'en'

    if snippet_id not in LOCALIZED_TEXT[lang].keys():
        # Incorrect snippet ID specified
        print(f'* Error: unmapped snippet ID "{snippet_id}" specified for language: {lang}')
        return ''

    text = LOCALIZED_TEXT[lang][snippet_id]
    return text
