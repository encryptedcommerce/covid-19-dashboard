from typing import Dict

from models.common import get_user_country


LOCALIZED_TEXT: Dict[str, Dict[str, str]] = {}  # versions of text snippets in various language

LOCALIZED_TEXT['en'] = {
    'summary-dashboard': 'Summary Dashboard',
    'confirmed': 'Confirmed Cases',
    'deaths': 'Deaths',
    'recovered': 'Recovered Cases',
    'y-axis': 'y-axis',
    'log-scale': 'log scale',
    'linear-scale': 'linear scale',
    'title': 'COVID-19 Interactive Dashboard',
    'summary-intro': 'This dashboard contains interactive visualization of COVID-19 data.',
    'summary-description': '''
You may select countries to include in the charts.
If detected, your country and others with similar statistics will be added by default,
in addition to several countries with the highest statistics.
    ''',
    'data-credit': 'Data is provided by',
    'data-update': ', updated daily around 00:05 UTC',
    'geoip-credit': 'Geographic IP data:',
    'chart': 'Chart',
    'table': 'Data Table',
}

LOCALIZED_TEXT['es'] = {
    'summary-dashboard': 'Panel de Resumen',
    'confirmed': 'Casos Confirmados',
    'deaths': 'Muertes',
    'recovered': 'Casos Recuperados',
    'y-axis': 'eje y',
    'log-scale': 'escala logarítmica',
    'linear-scale': 'escala lineal',
    'title': 'Panel interactivo de COVID-19',
    'summary-intro': 'Este panel contiene visualización interactiva de datos COVID-19.',
    'summary-description': '''
Puede seleccionar países para incluir en los cuadros.
Si se detecta, su país y otros con estadísticas similares se agregarán de forma predeterminada,
además de varios países con las estadísticas más altas.
    ''',
    'data-credit': 'Los datos son proporcionados por',
    'data-update': ', actualizado diariamente alrededor de las 00:05 UTC',
    'geoip-credit': 'Datos geográficos de IP:',
    'chart': 'Gráfico',
    'table': 'Tabla de Datos',
}

LOCALIZED_TEXT['fr'] = {
    'summary-dashboard': 'Tableau de Bord Récapitulatif',
    'confirmed': 'Cas Confirmés',
    'deaths': 'Des Morts',
    'recovered': 'Cas Récupérés',
    'y-axis': 'axe y',
    'log-scale': 'échelle logarithmique',
    'linear-scale': 'échelle linéaire',
    'title': 'Tableau de Bord Interactif COVID-19',
    'summary-intro': 'Ce tableau de bord contient une visualisation interactive des données COVID-19.',
    'summary-description': '''
Vous pouvez sélectionner les pays à inclure dans les graphiques.
S'il est détecté, votre pays et d'autres pays ayant des statistiques similaires seront ajoutés par défaut,
en plus de plusieurs pays avec les statistiques les plus élevées.
    ''',
    'data-credit': 'Les données sont fournies par',
    'data-update': ', mis à jour quotidiennement vers 00:05 UTC',
    'geoip-credit': 'Données IP géographiques:',
    'chart': 'Graphique',
    'table': 'Tableau de Données',
}

LOCALIZED_TEXT['it'] = {
    'summary-dashboard': 'Dashboard di Riepilogo',
    'confirmed': 'Casi Confermati',
    'deaths': 'Morti',
    'recovered': 'Casi Recuperati',
    'y-axis': 'asse y',
    'log-scale': 'Scala Logaritmica',
    'linear-scale': 'Scala Lineare',
    'title': 'Pannello interattivo COVID-19',
    'summary-intro': 'Questa dashboard contiene una visualizzazione interattiva dei dati COVID-19.',
    'summary-description': '''
È possibile selezionare i paesi da includere nei grafici.
Se rilevato, il tuo Paese e altri con statistiche simili verranno aggiunti per impostazione predefinita,
oltre a diversi paesi con le statistiche più alte.
    ''',
    'data-credit': 'I dati sono forniti da',
    'data-update': ', aggiornato quotidianamente intorno alle 00:05 UTC',
    'geoip-credit': 'Dati IP geografici:',
    'chart': 'Grafico',
    'table': 'Tabella Dati',
}

LOCALIZED_TEXT['de'] = {
    'summary-dashboard': 'Zusammenfassung Dashboard',
    'confirmed': 'Bestätigte Fälle',
    'deaths': 'Todesfälle',
    'recovered': 'Wiederhergestellte Fälle',
    'y-axis': 'y-Achse',
    'log-scale': 'Logarithmische Skalierung',
    'linear-scale': 'Lineare Skalierung',
    'title': 'Interaktives COVID-19-Dashboard',
    'summary-intro': 'Dieses Dashboard enthält eine interaktive Visualisierung der COVID-19-Daten.',
    'summary-description': '''
Sie können Länder auswählen, die in die Diagramme aufgenommen werden sollen.
Wenn dies erkannt wird, werden Ihr Land und andere Länder mit ähnlichen Statistiken standardmäßig hinzugefügt.
Neben mehreren Ländern mit den höchsten Statistiken.
    ''',
    'data-credit': 'Daten werden bereitgestellt von',
    'data-update': ', täglich aktualisiert um 00:05 UTC',
    'geoip-credit': 'Geografische IP-Daten:',
    'chart': 'Diagramm',
    'table': 'Datentabelle',
}

LOCALIZED_TEXT['pt'] = {
    'summary-dashboard': 'Painel Resumo',
    'confirmed': 'Casos Confirmados',
    'deaths': 'Mortes',
    'recovered': 'Casos Recuperados',
    'y-axis': 'eixo y',
    'log-scale': 'Escala Logarítmica',
    'linear-scale': 'Escala Linear',
    'title': 'Painel interativo COVID-19',
    'summary-intro': 'Este painel contém visualização interativa dos dados COVID-19.',
    'summary-description': '''
Você pode selecionar países para incluir nos gráficos.
Se detectado, seu país e outros com estatísticas semelhantes serão adicionados por padrão,
além de vários países com as estatísticas mais altas.
    ''',
    'data-credit': 'Os dados são fornecidos por',
    'data-update': ', atualizado diariamente às 00:05 UTC',
    'geoip-credit': 'Dados IP geográficos:',
    'chart': 'Gráfico',
    'table': 'Tabela de Dados',
}

LOCALIZED_TEXT['ru'] = {
    'summary-dashboard': 'Сводная панель',
    'confirmed': 'Подтвержденные дела',
    'deaths': 'Смертей',
    'recovered': 'Восстановленные Случаи',
    'y-axis': 'ось ординат',
    'log-scale': 'логарифмическая шкала',
    'linear-scale': 'линейная шкала',
    'title': 'COVID-19 Интерактивная панель инструментов',
    'summary-intro': 'Эта панель содержит интерактивную визуализацию данных COVID-19.',
    'summary-description': '''
Вы можете выбрать страны для включения в диаграммы.
В случае обнаружения ваша страна и другие страны с аналогичной статистикой будут добавлены по умолчанию,
в дополнение к нескольким странам с самой высокой статистикой.
    ''',
    'data-credit': 'Данные предоставлены',
    'data-update': ', обновляется ежедневно около 00:05 UTC',
    'geoip-credit': 'Географические данные IP:',
    'chart': 'Диаграмма',
    'table': 'Таблица данных',
}

LOCALIZED_TEXT['se'] = {
    'summary-dashboard': 'Sammanfattning Instrumentpanel',
    'confirmed': 'Bekräftade Fall',
    'deaths': 'Dödsfall',
    'recovered': 'Återställda Fall',
    'y-axis': 'y-axel',
    'log-scale': 'logaritmisk skala',
    'linear-scale': 'linjär skala',
    'title': 'COVID-19 Interaktiv Instrumentpanel',
    'summary-intro': 'Denna instrumentbräda innehåller interaktiv visualisering av COVID-19-data.',
    'summary-description': '''
Du kan välja länder som ska inkluderas i diagrammen.
Om det upptäcks kommer ditt land och andra med liknande statistik att läggas till som standard,
förutom flera länder med den högsta statistiken.
    ''',
    'data-credit': 'Data tillhandahålls av',
    'data-update': ', uppdateras dagligen runt 00:05 UTC',
    'geoip-credit': 'Geografiska IP-data:',
    'chart': 'Diagram',
    'table': 'Datatabell',
}

LOCALIZED_TEXT['zh-Hans'] = {
    'summary-dashboard': '摘要仪表板',
    'confirmed': '确诊病例',
    'deaths': '死亡人数',
    'recovered': '追回案件',
    'y-axis': 'y轴',
    'log-scale': '对数刻度',
    'linear-scale': '线性刻度',
    'title': 'COVID-19互动式仪表板',
    'summary-intro': '此仪表板包含COVID-19数据的交互式可视化。',
    'summary-description': '''
您可以选择要包含在图表中的国家。
如果检测到，默认情况下将添加您所在的国家/地区和统计相似的其他国家/地区，
除了几个统计数字最高的国家。
    ''',
    'data-credit': '数据由',
    'data-update': '，每天在世界标准时间00:05左右更新',
    'geoip-credit': '地理IP数据：',
    'chart': '图表',
    'table': '数据表',
}

LOCALIZED_TEXT['jp'] = {
    'summary-dashboard': 'サマリーダッシュボード',
    'confirmed': '確認済みのケース',
    'deaths': '死',
    'recovered': '回収されたケース',
    'y-axis': 'y軸',
    'log-scale': '対数目盛',
    'linear-scale': 'リニアスケール',
    'title': 'COVID-19インタラクティブダッシュボード',
    'summary-intro': 'このダッシュボードには、COVID-19データのインタラクティブな視覚化が含まれています。',
    'summary-description': '''
チャートに含める国を選択できます。
検出された場合、あなたの国および同様の統計情報を持つ他の国がデフォルトで追加されます。
最高の統計を持ついくつかの国に加えて。
    ''',
    'data-credit': 'データはによって提供されます',
    'data-update': '、毎日00:05 UTCに更新',
    'geoip-credit': '地理的IPデータ：',
    'chart': 'チャート',
    'table': 'データ表',
}

LOCALIZED_TEXT['hi'] = {
    'summary-dashboard': 'सारांश डैशबोर्ड',
    'confirmed': 'पुष्टि किए गए मामले',
    'deaths': 'लोगों की मृत्यु',
    'recovered': 'बरामद मामले',
    'y-axis': 'y- अक्ष',
    'log-scale': 'लघुगणक मापक',
    'linear-scale': 'रैखिक पैमाने',
    'title': 'COVID-19 इंटरएक्टिव डैशबोर्ड',
    'summary-intro': 'इस डैशबोर्ड में COVID-19 डेटा का इंटरैक्टिव विज़ुअलाइज़ेशन है।',
    'summary-description': '''
आप चार्ट में शामिल करने के लिए देशों का चयन कर सकते हैं।
यदि पता लगाया जाता है, तो आपका देश और अन्य समान आँकड़े डिफ़ॉल्ट रूप से जोड़े जाएंगे,
उच्चतम आँकड़ों के साथ कई देशों के अलावा।
    ''',
    'data-credit': 'द्वारा डेटा प्रदान किया जाता है',
    'data-update': ', अद्यतन लगभग 00:05 यूटीसी',
    'geoip-credit': 'भौगोलिक IP डेटा:',
    'chart': 'चार्ट',
    'table': 'विवरण सारणी',
}

# mapping of country name to language code
LANG_MAP: Dict[str, str] = {}

automap = ['FR', 'IT', 'DE', 'RU', 'SE', 'CN', 'JP']
for country in automap:
    language = country.lower()
    LANG_MAP[country] = language

for country in ['AR', 'BO', 'CL', 'CO', 'CR', 'DO', 'EC', 'SV', 'GT', 'HN', 'MX', 'NI', 'PA', 'PY', 'PE', 'PR', 'UY', 'VE']:
    LANG_MAP[country] = 'es'

for country in ['UK', 'US', 'AU', 'CA']:
    LANG_MAP[country] = 'en'

for country in ['BE', 'CA', 'LU', 'FR']:
    LANG_MAP[country] = 'fr'

for country in ['AT', 'LI', 'LU', 'DE', 'CH']:
    LANG_MAP[country] = 'de'

for country in ['BR', 'PT']:
    LANG_MAP[country] = 'pt'

for country in ['CN']:
    LANG_MAP[country] = 'zh-Hans'

for country in ['IN']:
    LANG_MAP[country] = 'hi'


def localize(snippet_id: str) -> str:
    """Looks up user's country and returns identified text snippet translated to user's language.

    Arguments:
        snippet_id: id of text snippet from `LOCALIZED_TEXT` dict.
    """
    user_country = get_user_country(country_code=True)
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
