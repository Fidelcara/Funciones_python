import json
import plotly.graph_objs as go
import plotly.utils
import numpy as np
import re
import pandas as pd
import holidays
import requests
import os
import oracledb


def verificar_fecha(cadena):
    # patrones=["%Y-%m-%d","%Y/%m/%d","%d-%m-%Y"]
    patron = r"\d{2}/\d{2}/\d{4}"
    
    if re.match(patron, cadena):
        return cadena
    else:
        return ''

def tramos():
    horas=['']
    for i in range(0,24):
        if i<10:
            horas.append(f'0{i}:00')
            horas.append(f'0{i}:30')
        else:
            horas.append(f'{i}:00')
            horas.append(f'{i}:30')
    return horas

def segundos_a_hhmmss(segundos):
    horas, segundos = divmod(segundos, 3600)
    minutos, segundos = divmod(segundos, 60)
    return f'{horas:02}:{minutos:02}:{segundos:02}'

def tiempo(segundos):
    if segundos is None or segundos == 0:
        return ''
    else:
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        segundos = segundos % 60
        return f'{horas:02d}:{minutos:02d}:{segundos:02d}'

def transformacion_resultados(datos,tmp):
    nueva_lista=[]
    for lista in datos:
        row=[data for data in lista]
        for i in range(len(row)):
            if i in tmp:
                row[i]=tiempo(row[i])
            else:
                pass
        nueva_lista.append(row)
    return nueva_lista

def condicionales(tabla,fecha1='',fecha2='',ID='', SKILL= '',tramo1='',tramo2='',cursor=''):  
    
    posiciones={'avaya.skill_agente':{'resultados':[5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 17], 'estadisticas': [2, 3, 4, 5, 6, 7, 8]},
    'skill_tramo':{'resultados':[5, 7, 8, 10, 12], 'estadisticas': [2]},
    'skill_total':{'resultados':[4, 6, 7, 9, 11], 'estadisticas': [2]}}
    
    resultados=[]
    estadisticas=[]
    selector=''
    if tabla.lower()=='avaya.skill_agente':
        columnas="TO_CHAR(fecha), skill,perfil,login_id, llamadas_acd,tmp_prom_acd, tmp_prom_acw,llam_aban,tmp_prom_aban,tmp_acd,tmp_acw, tmp_llam_agente,otra_hora,tmp_aux,tmp_dispon, tmp_pers,llam_reten,tmp_prom_reten"
        
        total=f"SELECT SUM(llamadas_acd), SUM(llam_aban),SUM(tmp_acd), SUM(tmp_acw), SUM(tmp_llam_agente),SUM(otra_hora),SUM(tmp_aux), SUM(tmp_dispon), SUM(tmp_pers),SUM(llam_reten) FROM {tabla}"
    
        promedio=f"SELECT TO_CHAR(FECHA), login_id, TMP_PROM_ACD, TMP_PROM_ACW, TMP_PROM_ABAN, TMP_PROM_RETEN FROM {tabla}"
    
    if tabla.lower()=='skill_tramo':
        columnas="TO_CHAR(FECHA), HORA, SKILL, PERFIL, VEL_PROM_RESP, TMP_PROM_ABAN, LLAM_ACD, TMP_PROM_ACD, TMP_PROM_ACW, LLAM_ABAN, DEMORA_MAXIMA, LLAM_SALIDA_EXTN, TMP_PROM_SALIDA_EXTN, PORC_TIEMPO_ACD, PORC_LLAMADAS_RESP, PROM_POSIC_PERSONAL, LLAM_POSIC, PORC_NIVEL_SERVC"
        
        total=f"SELECT SUM(LLAM_ACD), SUM(llam_aban),SUM(DEMORA_MAXIMA), SUM(LLAM_SALIDA_EXTN) FROM {tabla}"
    
        promedio=f"SELECT TO_CHAR(FECHA), perfil, LPAD(HORA,5,'0'), VEL_PROM_RESP, TMP_PROM_ABAN, TMP_PROM_ACD, TMP_PROM_ACW, TMP_PROM_SALIDA_EXTN, PROM_POSIC_PERSONAL FROM {tabla}"
    
    if tabla.lower()=='skill_total':
        columnas="TO_CHAR(FECHA), SKILL, PERFIL, VEL_PROM_RESP, TMP_PROM_ABAN, LLAM_ACD, TMP_PROM_ACD, TMP_PROM_ACW, LLAM_ABAN, DEMORA_MAXIMA, LLAM_SALIDA_EXTN, TMP_PROM_SALIDA_EXTN, PORC_TIEMPO_ACD, PORC_LLAMADAS_RESP, PROM_POSIC_PERSONAL, LLAM_POSIC, PORC_NIVEL_SERVC"
        
        total=f"SELECT SUM(LLAM_ACD), SUM(LLAM_ABAN), SUM(DEMORA_MAXIMA), SUM(LLAM_SALIDA_EXTN) FROM {tabla}"
    
        promedio=f"SELECT TO_CHAR(FECHA), perfil, VEL_PROM_RESP, TMP_PROM_ABAN, TMP_PROM_ACD, TMP_PROM_ACW, TMP_PROM_SALIDA_EXTN, PROM_POSIC_PERSONAL  FROM {tabla}"
    
    consulta_base=f'SELECT {columnas} from {tabla}'
    orden_fecha= 'ORDER BY FECHA'
    
    if (fecha1 !='' or fecha2!='') and (ID=='' and SKILL=='' and tramo1 =='' and tramo2 ==''):
        print('1')
        if fecha1 !='' and fecha2!= '':
            selector = f"WHERE FECHA BETWEEN TO_DATE('{fecha1}') AND TO_DATE('{fecha2}')"
        elif fecha1!='' and fecha2=='':
            selector = f"WHERE FECHA = TO_DATE('{fecha1}')"
        elif fecha1=='' and fecha2!='':
            selector = f"WHERE FECHA = TO_DATE('{fecha2}')"
            
    #Agente
    if tabla.lower()=='avaya.skill_agente':
        
        if fecha1 =='' and fecha2=='' and ID!='':
            selector = f"WHERE LOGIN_ID=({ID})"
            
        elif fecha1 !='' and fecha2!='' and ID!='':
            selector = f"WHERE LOGIN_ID=({ID}) AND FECHA BETWEEN TO_DATE('{fecha1}') AND TO_DATE('{fecha2}')"
            
        elif (fecha1 !='' or fecha2!='') and ID!='':
            if fecha1!='':
                fecha =fecha1
            else:
                fecha=fecha2
            selector = f"WHERE LOGIN_ID=({ID}) AND FECHA = TO_DATE('{fecha}')"
            
        consulta=f"{consulta_base} {selector}"
        totalidad=f"{total} {selector}"


    #Tramo
    if tabla.lower()=='skill_tramo':
        
        #Tramos
        if (tramo1 !='' or tramo2!='') and (fecha1 =='' and fecha2==''):
            if tramo1 !='' and tramo2!= '':
                selector = f"WHERE LPAD(HORA,5, '0') BETWEEN ('{tramo1}') AND ('{tramo2}')"
            else:
                if tramo1!='':
                    tramo=tramo1
                    
                else:
                    tramo=tramo2
                    selector = f"WHERE LPAD(HORA,5, '0')=('{tramo}')"

        #Fechas y tramos
        elif (fecha1 !='' or fecha2!='') and (tramo1 !='' or tramo2!=''):

            if fecha1 !='' and fecha2!='' and tramo1 !='' and tramo2!= '':
                selector = f"WHERE LPAD(HORA,5, '0') BETWEEN '{tramo1}' and '{tramo2}' AND  FECHA BETWEEN TO_DATE('{fecha1}') AND TO_DATE('{fecha2}')"
                
            elif (fecha1 =='' and fecha2!='' and tramo1 !='' and tramo2!= '')or (fecha1 !='' and fecha2=='' and tramo1 !='' and tramo2!= ''):
                if fecha1!='':
                    fecha=fecha1
                else:
                    fecha=fecha2
                selector = f"WHERE LPAD(HORA,5, '0') BETWEEN ('{tramo1}') and ('{tramo2}') AND FECHA = TO_DATE('{fecha}')"
                
            elif (fecha1 !='' and fecha2!='' and tramo1 =='' and tramo2!= '')or (fecha1 !='' and fecha2!='' and tramo1 !='' and tramo2== ''):
                if tramo1!='':
                    tramo=tramo1
                else:
                    tramo=tramo2
                selector = f"WHERE LPAD(HORA,5, '0') =('{tramo}') AND FECHA BETWEEN TO_DATE('{fecha1}') AND TO_DATE('{fecha2}')"
                
            elif (fecha1 =='' and fecha2!='' and tramo1 =='' and tramo2!= '') or (fecha1 =='' and fecha2!='' and tramo1 !='' and tramo2== ''):
                if tramo1!='':
                    tramo=tramo1
                else:
                    tramo=tramo2
                selector = f"WHERE LPAD(HORA,5, '0') =('{tramo}') AND FECHA = TO_DATE('{fecha2}')"
                
            elif (fecha1 !='' and fecha2=='' and tramo1 =='' and tramo2!= '')or(fecha1 !='' and fecha2=='' and tramo1 !='' and tramo2== ''):
                if tramo1!='':
                    tramo=tramo1
                else:
                    tramo=tramo2
                selector = f"WHERE LPAD(HORA,5, '0') =('{tramo}') AND FECHA = TO_DATE('{fecha1}')"
                
        elif (fecha1!= '' or fecha2!='') and tramo1=='' and tramo2=='':
            if fecha1 !='' and fecha2!= '':
                selector = f"WHERE FECHA BETWEEN TO_DATE('{fecha1}') AND TO_DATE('{fecha2}')"
            elif fecha1!='' and fecha2=='':
                selector = f"WHERE FECHA = TO_DATE('{fecha1}')"
            elif fecha1=='' and fecha2!='':
                selector = f"WHERE FECHA = TO_DATE('{fecha2}')"
    
        hora= ", LPAD(HORA,5,'0')"
        
        
        selector_skill=f"AND SKILL=({SKILL})"
        consulta=f"{consulta_base} {selector} {selector_skill} {orden_fecha} {hora}"
        totalidad=f"{total} {selector} {selector_skill}"
            
        
    
    #Total
    if tabla.lower()=='skill_total':
        
        if fecha1 =='' and fecha2=='' and SKILL!='':
            selector= f"WHERE SKILL = ({SKILL})"
        
        elif fecha1 !='' and fecha2!='' and SKILL!='':
            selector= f"WHERE FECHA BETWEEN TO_DATE('{fecha1}') AND TO_DATE('{fecha2}') AND SKILL=({SKILL})"
        
        elif (fecha1 !='' or fecha2!='') and SKILL!='':
            if fecha1!='':
                fecha=fecha1
            else:
                fecha=fecha2
            selector= f"WHERE FECHA = TO_DATE('{fecha}') AND SKILL = ({SKILL})"

        consulta=f"{consulta_base} {selector} {orden_fecha}"
        totalidad=f"{total} {selector}"
    
    if tabla.lower()=='skill_tramo':
        consulta_promedio=f"{promedio} {selector} {selector_skill} {orden_fecha} {hora}"
    else:
        consulta_promedio=f"{promedio} {selector} {orden_fecha}"
        
    cursor.execute(consulta)
    resultados= cursor.fetchall()
    try:
        resultados=transformacion_resultados(resultados,posiciones[tabla]['resultados'])
    except:
        pass
    cursor.execute(totalidad)
    estadisticas=cursor.fetchall()
    try:
        estadisticas=transformacion_resultados(estadisticas,posiciones[tabla]['estadisticas'])
    except:
        pass
    cursor.execute(consulta_promedio)
    medias=cursor.fetchall()
    
    return estadisticas, resultados, medias

def generate_plot(cursor='', tabla='', fecha1='', fecha2='', skill=''):
    
    consulta_base = f"SELECT llam_aban, fecha, perfil from {tabla}"
    
    if skill!='':
        selector=f"WHERE SKILL=({skill}) AND FECHA BETWEEN TO_DATE('{fecha1}') AND TO_DATE('{fecha2}')"
    else:
        selector=f"WHERE FECHA BETWEEN TO_DATE('{fecha1}') AND TO_DATE('{fecha2}')"
    
    orden="ORDER BY FECHA"
    
    consulta=f"{consulta_base} {selector} {orden}"
    cursor.execute(consulta)
    datos = cursor.fetchall()
    
    df = pd.DataFrame(datos, columns=['valor', 'fecha', 'perfil'])

    # Crea un rango de fechas completo desde la fecha mínima hasta la fecha máxima
    fecha_minima = df['fecha'].min()
    fecha_maxima = df['fecha'].max()
    rango_fechas_completo = pd.date_range(start=fecha_minima, end=fecha_maxima)

    # Crea una lista de todas las descripciones únicas
    perfiles_unicos = df['perfil'].unique()

    # Genera todas las combinaciones posibles de fechas y descripciones
    combinaciones = pd.MultiIndex.from_product([rango_fechas_completo, perfiles_unicos], names=['fecha', 'perfil'])
    df_completo = pd.DataFrame(index=combinaciones).reset_index()

    # Fusiona el DataFrame completo con tus datos originales
    df_completo = df_completo.merge(df, on=['fecha', 'perfil'], how='left')

    # Rellena los valores faltantes con 0
    df_completo['valor'].fillna(0, inplace=True)
    df_agrupado = df_completo.groupby(['perfil', 'fecha'])['valor'].sum().reset_index()
    
    contador=0
    traces={}
    for skill in perfiles_unicos:
        contador += 1
        x_axis=rango_fechas_completo
        y_axis= df_agrupado['valor'].loc[df_agrupado['perfil']==skill]
        trace_name = f'trace{contador}'
        trace = go.Scatter(x=x_axis, y=y_axis, name=skill, mode='lines+markers', hoverinfo='y')
        traces[trace_name]=trace
        
    data=[traces[trace] for trace in traces]
        

    layout = go.Layout(title='', xaxis=dict(title='<b>Fecha (aaaa/mm/dd)</b>',type='category'), yaxis=dict(title='<b>Llamadas abandonadas</b>', type='linear'))
    
    fig = go.Figure(data=data, layout=layout)
    
    # Convertir el gráfico a un JSON que entienda el HTML (necesario)
    plot_data = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return plot_data

def promedios(datos='',titulos='',tabla=''):

    datos = [list(tupla) for tupla in datos]
    
    if tabla=='skill_tramo':
        for i,lista in enumerate(datos):
            datos[i][0]= lista[0]+' - '+lista[2]
            del datos[i][2]
            
    
    for i,lista in enumerate(datos):
        for j in range(2,len(lista)):
            if lista[j] is None:
                datos[i][j]=0

    diccionario={}
    for dato in datos:
        
        if dato[1] in diccionario:
            if dato[0] in diccionario[dato[1]] and dato[3]<diccionario[dato[1]][dato[0]][1]:
                pass
            else:
                diccionario[dato[1]][dato[0]]=np.array(dato[2:])
        else:
            diccionario[dato[1]] = {dato[0]: np.array(dato[2:])}
    
    graficos= []
    for i in range(len(diccionario[datos[0][1]][datos[0][0]])):#para repetirlo por cada tipo de dato
            contador=0
            traces={}
            for skill in diccionario:
                
                x_axis= [fechas for fechas in diccionario[skill]]
                contador += 1
                trace_name = f'trace{contador}' 
                
                if 'tiempo' in titulos[i].lower():
                    y_axis=[diccionario[skill][fecha][i] for fecha in diccionario[skill]]
                    tiempos_etiquetas = [segundos_a_hhmmss(dato) for dato in y_axis]
                    trace=go.Bar(x=x_axis, y=y_axis,name=skill,text=tiempos_etiquetas,hoverinfo='none')
                    layout = go.Layout(title='', xaxis=dict(title='<b>Fecha (aaaa/mm/dd)</b>',type='category'), yaxis=dict(title='<b>Tiempo(segundos)<b>'))

                else:
                    trace = go.Scatter(x=x_axis, y=[diccionario[skill][fecha][i] for fecha in diccionario[skill]], mode='lines+markers', name=skill, hoverinfo='y')
                    layout = go.Layout(title='', xaxis=dict(title='<b>Fecha (aaaa/mm/dd)</b>',type='category'), yaxis=dict(title='', type='linear'))

                traces[trace_name]=trace
            data=[traces[trace] for trace in traces]

            fig = go.Figure(data=data, layout=layout)
            # Convertir el gráfico a un JSON que entienda el HTML (necesario)
            graficos.append(json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder))
        
    return graficos

def obtener_informacion_fechas(fechas):
    informacion = []
    
    for fecha in fechas:
        
        # Verifica si es festivo en Madrid
        if fecha in holidays.Spain(years=fecha.year, observed=True, prov='MD') or fecha.weekday()==6:
            es_festivo = 1
        else:
            es_festivo = 0
        
        informacion.append({
            'Fecha': fecha.strftime("%Y-%m-%d"),
            'Es festivo en Madrid': es_festivo
        })
    
    return informacion

def obtener_tiempo_aemet(fechas, api_key_aemet,proxy):

    resultados=[]
    fechaIniStr=fechas[0].strftime('%Y-%m-%dT%H:%M:%SUTC')
    fechaFinStr=fechas[-1].strftime('%Y-%m-%dT%H:%M:%SUTC')
    idema=3195
    
    endpoint = f"https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{fechaIniStr}/fechafin/{fechaFinStr}/estacion/{idema}/"

    # Construye la URL para obtener la predicción meteorológica diaria
    url = f"{endpoint}?api_key={api_key_aemet}"
    
    response = requests.get(url,proxies=proxy,verify=False)
    # Extrae la URL real de los datos (enlace JSON)
    data_url = response.json()['datos']
    # Realiza otra solicitud para obtener los datos reales
    response_data = requests.get(data_url,proxies=proxy,verify=False)

    # Extrae los datos del tiempo
    tiempo_data = response_data.json()
    
    #la clave racha no está en todos los días.
    claves_deseadas = ('fecha', 'tmed', 'prec')
    
    for dia in tiempo_data:
        valores=[]
        for clave in claves_deseadas:
            
            try:
                # Obtener los valores para cada diccionario en la lista
                x=dia.get(clave,None)
                if x=='Ip':
                    valores.append(None)
                else:
                    valores.append(float(x.replace(',', '.')))
            except:
                valores.append(dia.get(clave,None))
                
        resultados.append(valores)
    return resultados

def datos_prediccion():
    api_key_vcweather='WWYYX79NBWYJRUU5Z4B3QDXP3'
    proxy = {'http': "http://50341471Z:Perrito1999$@proxy.gslb.madrid.org:8080", 'https': "http://50341471Z:Perrito1999$@proxy.gslb.madrid.org:8080"}
    locations='Madrid'
    aggregateHours=24 #día completo
    unitGroup='metric' #unidades sistema internacional
    contentType='json' #o csv
    
    url=f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast?locations={locations}&aggregateHours={aggregateHours}&unitGroup={unitGroup}&shortColumnNames=false&contentType={contentType}&key={api_key_vcweather}"
    meteo = json.loads(requests.get(url, proxies=proxy,verify=False).text) #diccionario con el tiempo meteo

    claves_seleccionadas=['precip','temp']
    resultados = {}

    for i in range (len(meteo['locations']['Madrid']['values'])):
        
        fecha=meteo['locations']['Madrid']['values'][i]['datetimeStr']
        resultados[fecha]={}
        
        for k in claves_seleccionadas:
            resultados[fecha][k]=meteo['locations']['Madrid']['values'][i][k]
            
    df=pd.DataFrame(index=pd.to_datetime(list(resultados.keys()),utc=True))
    df["day"] = df.index.dayofweek 
    df["week"] = [x.week for x in df.index]
    df['month']=[x.month for x in df.index]
    df["dayofyear"] = [x.dayofyear for x in df.index]
    df['tmed']= [resultados[i]['temp'] for i in resultados]
    df['prec']= [resultados[i]['precip'] for i in resultados]
    festivo=obtener_informacion_fechas(df.index)
    df['Festivo']=[fiesta['Es festivo en Madrid'] for fiesta in festivo]
    orden_columnas = ['day','week','month','dayofyear','tmed','prec','Festivo']
    df = df[orden_columnas]
    
    return df

def borrar_archivos_antiguos(carpeta, fecha_actual):
    for archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_archivo):
            fecha_archivo, extension = os.path.splitext(archivo)
            if fecha_archivo != fecha_actual or extension not in ['.html', '.json']:
                os.remove(ruta_archivo)
                
def conexion_oracle(servicio, usuario='hernandezjf', contraseña='temporal01', path='C:/oracle/product/11.2.0/client_1/network/admin/'):
    oracledb.init_oracle_client()
    name = usuario
    key = contraseña
    service_name = servicio
    carpeta=path
    conexion = oracledb.connect(user=name,password=key,dsn=service_name,config_dir=carpeta)
    cursor = conexion.cursor()
    return cursor

def consulta(cursor,query):
    cursor.execute(query)
    datos=cursor.fetchall()
    return datos