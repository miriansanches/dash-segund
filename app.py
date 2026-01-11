import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# ============ CONFIGURAÇÃO DA PÁGINA ============
st.set_page_config(
    page_title="Dashboard Receitas - Vértiq",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============ CSS PERSONALIZADO ============
st.markdown("""
    <style>
        /* Cores Vértiq: Preto e Amarelo */
        :root {
            --primary-color: #FDB913;
            --dark-bg: #0F0F0F;
            --card-bg: #1A1A1A;
            --text-color: #FFFFFF;
        }
        
        body {
            background-color: #0F0F0F;
            color: #FFFFFF;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        
        .main {
            background-color: #0F0F0F;
        }
        
        .stMetric {
            background: linear-gradient(135deg, #1A1A1A 0%, #252525 100%);
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #FDB913;
        }
        
        h1, h2, h3 {
            color: #FDB913 !important;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            background-color: #0F0F0F;
            border-bottom: 2px solid #1A1A1A;
        }
        
        .stTabs [data-baseweb="tab-list"] button {
            color: #FFFFFF;
            background-color: transparent;
            border-bottom: 3px solid transparent;
        }
        
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
            color: #FDB913;
            border-bottom-color: #FDB913;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #1A1A1A 0%, #252525 100%);
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #FDB913;
        }
    </style>
""", unsafe_allow_html=True)

# ============ DADOS ============
# Valores já calculados com multiplicadores aplicados
receita_categorias = {
    'Categoria': [
        'Renda Fixa, Câmbio, Internacional, Fundos',
        'RV Corretagem',
        'COE, RV Estruturadas, Consórcios, Seguros'
    ],
    'Receita': [83358.79, 6755.00, 24985.24]
}

# Dados de assessores
assessores_dados = {
    'Assessor': ['Fernando Elias', 'Guilherme Rocha', 'W. Marques', 'Marisa Regina', 
                 'Fernando José', 'Paulo Minehira', 'Samuel Falcão', 'Cintia Campos'],
    'Janeiro': [60475.11, 36476.22, 23322.87, 15860.26, 6084.50, 3791.05, 2033.04, 1433.48],
    'Dezembro': [71665.51, 84975.18, 143193.27, 37090.03, 14099.06, 12901.42, 2033.04, 8110.66]
}

# Concentração de acessos Janeiro
concentracao_jan = {
    'Fernando Elias (Sr.)': 38.51,
    'Guilherme Rocha (Fundador)': 23.23,
    'W. Marques (Fundador)': 14.85,
    'Marisa Regina (Sr.)': 10.10,
    'Fernando José (Digital)': 3.87,
    'Enzo Rocha (Digital)': 2.35,
    'Paulo Minehira (Sr.)': 2.41,
    'Demais Assessores': 4.68
}

# Concentração de acessos Dezembro
concentracao_dez = {
    'W. Marques (Fundador)': 36.53,
    'Fernando Elias (Sr.)': 18.28,
    'Guilherme Rocha (Fundador)': 21.68,
    'Marisa Regina (Sr.)': 9.46,
    'Fernando José (Digital)': 3.60,
    'Enzo Rocha (Digital)': 1.53,
    'Paulo Minehira (Sr.)': 3.29,
    'Demais Assessores': 5.64
}

# Produtos
produtos_jan = {
    'Renda Fixa': 74907.50,
    'COE': 25559.24,
    'Consórcio': 39921.20,
    'RV Estruturados': 7145.62,
    'RV Corretagem': 6380.51,
    'Internacional': 1971.26,
    'Câmbio': 1013.21,
    'RV BTC': 121.05,
}

produtos_dez = {
    'Renda Fixa': 50768.50,
    'COE': 158527.94,
    'Consórcio': 43741.80,
    'RV Estruturados': 74312.72,
    'RV Corretagem': 26613.99,
    'Internacional': 13173.08,
    'Câmbio': 4973.25,
    'RV BTC': 7128.25,
}

# ============ HEADER ============
st.markdown("""
    <div style='background: linear-gradient(135deg, #1A1A1A 0%, #000000 100%); 
                padding: 30px 20px; 
                border-bottom: 3px solid #FDB913; 
                margin: -60px -30px 30px -30px;'>
        <h1 style='color: #FDB913; margin-bottom: 5px;'>📊 Dashboard Receitas</h1>
        <p style='color: #AAAAAA; margin: 0;'>Análise de Receitas - Vértiq Digital</p>
        <p style='color: #666666; font-size: 12px; margin: 10px 0 0 0;'>
            📅 Atualizado em: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}
        </p>
    </div>
""", unsafe_allow_html=True)

# ============ MÉTRICAS PRINCIPAIS ============
col1, col2, col3, col4 = st.columns(4)

total_jan = sum(produtos_jan.values())
total_dez = sum(produtos_dez.values())
variacao = total_jan - total_dez
variacao_pct = (variacao / total_dez) * 100

with col1:
    st.metric(
        label="Receita Total - Janeiro",
        value=f"R$ {total_jan:,.2f}",
        delta=f"{variacao_pct:.1f}% vs Dez",
        delta_color="inverse"
    )

with col2:
    st.metric(
        label="Receita Total - Dezembro",
        value=f"R$ {total_dez:,.2f}",
        delta=None
    )

with col3:
    st.metric(
        label="Variação Absoluta",
        value=f"R$ {variacao:,.2f}",
        delta="Redução na receita",
        delta_color="off"
    )

with col4:
    st.metric(
        label="Assessores Ativos",
        value="18",
        delta="No período"
    )

st.divider()

# ============ TABS ============
tab1, tab2, tab3 = st.tabs(["📈 Gráficos Principais", "👥 Assessores", "📊 Comparativos Detalhados"])

# ============ TAB 1: GRÁFICOS PRINCIPAIS ============
with tab1:
    st.subheader("Concentração de Receita por Produto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Janeiro 2026")
        
        fig_pie1 = go.Figure(data=[go.Pie(
            labels=list(produtos_jan.keys()),
            values=list(produtos_jan.values()),
            marker=dict(colors=['#FDB913', '#FFD60A', '#FFED4E', '#FFE135', '#FFF44F', '#FFD400', '#FFC600', '#FFB600'],
                       line=dict(color='#0F0F0F', width=2)),
            textposition='inside',
            textfont=dict(color='#000000', size=10, weight='bold'),
            hovertemplate='<b>%{label}</b><br>R$ %{value:,.0f}<extra></extra>'
        )])
        
        fig_pie1.update_layout(
            paper_bgcolor='#1A1A1A',
            plot_bgcolor='#1A1A1A',
            font=dict(color='#FFFFFF', size=11),
            height=400,
            showlegend=False,
            margin=dict(t=0, b=0, l=0, r=0)
        )
        
        st.plotly_chart(fig_pie1, use_container_width=True)
    
    with col2:
        st.markdown("#### Dezembro 2025")
        
        fig_pie2 = go.Figure(data=[go.Pie(
            labels=list(produtos_dez.keys()),
            values=list(produtos_dez.values()),
            marker=dict(colors=['#FFB600', '#FFC600', '#FFD400', '#FFF44F', '#FFE135', '#FFED4E', '#FFD60A', '#FDB913'],
                       line=dict(color='#0F0F0F', width=2)),
            textposition='inside',
            textfont=dict(color='#000000', size=10, weight='bold'),
            hovertemplate='<b>%{label}</b><br>R$ %{value:,.0f}<extra></extra>'
        )])
        
        fig_pie2.update_layout(
            paper_bgcolor='#1A1A1A',
            plot_bgcolor='#1A1A1A',
            font=dict(color='#FFFFFF', size=11),
            height=400,
            showlegend=False,
            margin=dict(t=0, b=0, l=0, r=0)
        )
        
        st.plotly_chart(fig_pie2, use_container_width=True)
    
    st.divider()
    
    st.subheader("Evolução Semanal de Receita")
    
    fig_line = go.Figure()
    
    fig_line.add_trace(go.Scatter(
        x=['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'],
        y=[39509.80, 35000, 36000, 46509.79],
        name='Janeiro 2026',
        mode='lines+markers',
        line=dict(color='#FDB913', width=3),
        marker=dict(size=10, symbol='circle'),
        fill='tozeroy',
        fillcolor='rgba(253, 185, 19, 0.2)',
        hovertemplate='<b>%{x}</b><br>R$ %{y:,.0f}<extra></extra>'
    ))
    
    fig_line.add_trace(go.Scatter(
        x=['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'],
        y=[98000, 95500, 99000, 99500],
        name='Dezembro 2025',
        mode='lines+markers',
        line=dict(color='#666666', width=3, dash='dash'),
        marker=dict(size=10, symbol='square'),
        hovertemplate='<b>%{x}</b><br>R$ %{y:,.0f}<extra></extra>'
    ))
    
    fig_line.update_layout(
        paper_bgcolor='#1A1A1A',
        plot_bgcolor='#1A1A1A',
        font=dict(color='#FFFFFF', size=12),
        hovermode='x unified',
        height=450,
        margin=dict(t=40, b=60, l=80, r=20),
        xaxis=dict(title='<b>Período</b>', showgrid=True, gridcolor='#333333'),
        yaxis=dict(title='<b>Receita (R$)</b>', showgrid=True, gridcolor='#333333')
    )
    
    st.plotly_chart(fig_line, use_container_width=True)
    
    st.divider()
    
    st.subheader("Top 8 Assessores - Comparativo")
    
    fig_bar = go.Figure(data=[
        go.Bar(
            x=assessores_dados['Assessor'],
            y=assessores_dados['Janeiro'],
            name='Janeiro 2026',
            marker_color='#FDB913',
            text=[f'R$ {v/1000:.1f}k' for v in assessores_dados['Janeiro']],
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>R$ %{y:,.0f}<extra></extra>'
        ),
        go.Bar(
            x=assessores_dados['Assessor'],
            y=assessores_dados['Dezembro'],
            name='Dezembro 2025',
            marker_color='#333333',
            text=[f'R$ {v/1000:.1f}k' for v in assessores_dados['Dezembro']],
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>R$ %{y:,.0f}<extra></extra>'
        )
    ])
    
    fig_bar.update_layout(
        barmode='group',
        paper_bgcolor='#1A1A1A',
        plot_bgcolor='#1A1A1A',
        font=dict(color='#FFFFFF', size=11),
        hovermode='x unified',
        height=500,
        margin=dict(t=40, b=120, l=80, r=20),
        xaxis=dict(tickangle=-45, showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#333333')
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)

# ============ TAB 2: ASSESSORES ============
with tab2:
    st.subheader("Ranking de Receita por Assessor - Janeiro 2026")
    
    # Ordenar assessores
    df_assessores = pd.DataFrame(assessores_dados)
    df_ordenado = df_assessores.sort_values('Janeiro', ascending=False)
    
    fig_ranking = go.Figure(data=[go.Bar(
        y=df_ordenado['Assessor'],
        x=df_ordenado['Janeiro'],
        orientation='h',
        marker=dict(color='#FDB913', line=dict(color='#FFD60A', width=2)),
        text=[f'R$ {v/1000:.1f}k' for v in df_ordenado['Janeiro']],
        textposition='outside',
        hovertemplate='<b>%{y}</b><br>R$ %{x:,.0f}<extra></extra>'
    )])
    
    fig_ranking.update_layout(
        paper_bgcolor='#1A1A1A',
        plot_bgcolor='#1A1A1A',
        font=dict(color='#FFFFFF', size=12),
        height=400,
        margin=dict(t=40, b=60, l=200, r=60),
        xaxis=dict(title='<b>Receita (R$)</b>', showgrid=True, gridcolor='#333333'),
        yaxis=dict(showgrid=False)
    )
    
    st.plotly_chart(fig_ranking, use_container_width=True)
    
    st.divider()
    
    st.markdown("#### Detalhamento por Assessor")
    
    df_display = df_assessores.copy()
    df_display['Variação %'] = ((df_display['Janeiro'] - df_display['Dezembro']) / df_display['Dezembro'] * 100).round(1)
    df_display['Janeiro'] = df_display['Janeiro'].apply(lambda x: f'R$ {x:,.2f}')
    df_display['Dezembro'] = df_display['Dezembro'].apply(lambda x: f'R$ {x:,.2f}')
    df_display['Variação %'] = df_display['Variação %'].apply(lambda x: f'{x:.1f}%')
    
    st.dataframe(df_display, use_container_width=True, hide_index=True)

# ============ TAB 3: COMPARATIVOS DETALHADOS ============
with tab3:
    st.subheader("Concentração de Acessos - Comparativo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Janeiro 2026")
        
        fig_conc_jan = go.Figure(data=[go.Pie(
            labels=list(concentracao_jan.keys()),
            values=list(concentracao_jan.values()),
            marker=dict(colors=['#FDB913', '#FFD60A', '#FFED4E', '#FFE135', '#FFF44F', '#FFD400', '#FFC600', '#FFB600'],
                       line=dict(color='#0F0F0F', width=2)),
            textposition='inside',
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>%{percent}<extra></extra>'
        )])
        
        fig_conc_jan.update_layout(
            paper_bgcolor='#1A1A1A',
            plot_bgcolor='#1A1A1A',
            font=dict(color='#FFFFFF', size=10),
            height=400,
            showlegend=False,
            margin=dict(t=0, b=0, l=0, r=0)
        )
        
        st.plotly_chart(fig_conc_jan, use_container_width=True)
    
    with col2:
        st.markdown("#### Dezembro 2025")
        
        fig_conc_dez = go.Figure(data=[go.Pie(
            labels=list(concentracao_dez.keys()),
            values=list(concentracao_dez.values()),
            marker=dict(colors=['#FFB600', '#FFC600', '#FFD400', '#FFF44F', '#FFE135', '#FFED4E', '#FFD60A', '#FDB913'],
                       line=dict(color='#0F0F0F', width=2)),
            textposition='inside',
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>%{percent}<extra></extra>'
        )])
        
        fig_conc_dez.update_layout(
            paper_bgcolor='#1A1A1A',
            plot_bgcolor='#1A1A1A',
            font=dict(color='#FFFFFF', size=10),
            height=400,
            showlegend=False,
            margin=dict(t=0, b=0, l=0, r=0)
        )
        
        st.plotly_chart(fig_conc_dez, use_container_width=True)
    
    st.divider()
    
    st.subheader("Receita por Categoria (Com Multiplicadores)")
    
    fig_cat = go.Figure(data=[go.Bar(
        x=receita_categorias['Categoria'],
        y=receita_categorias['Receita'],
        marker=dict(color=['#FDB913', '#FFD60A', '#FFED4E'], line=dict(color='#FDB913', width=2)),
        text=[f'R$ {v/1000:.1f}k' for v in receita_categorias['Receita']],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>R$ %{y:,.0f}<extra></extra>'
    )])
    
    fig_cat.update_layout(
        paper_bgcolor='#1A1A1A',
        plot_bgcolor='#1A1A1A',
        font=dict(color='#FFFFFF', size=12),
        height=450,
        margin=dict(t=40, b=100, l=80, r=20),
        xaxis=dict(tickangle=-30, showgrid=False),
        yaxis=dict(title='<b>Receita (R$)</b>', showgrid=True, gridcolor='#333333'),
        showlegend=False
    )
    
    st.plotly_chart(fig_cat, use_container_width=True)
    
    st.divider()
    
    st.markdown("#### Detalhe de Categorias")
    
    df_categorias = pd.DataFrame({
        'Categoria': receita_categorias['Categoria'],
        'Receita Final': [f'R$ {v:,.2f}' for v in receita_categorias['Receita']],
        'Status': ['✅ Calculado', '✅ Calculado', '✅ Calculado']
    })
    
    st.dataframe(df_categorias, use_container_width=True, hide_index=True)

# ============ RODAPÉ ============
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.caption(f"📅 {datetime.now().strftime('%d/%m/%Y às %H:%M')}")

with col2:
    st.caption("🎨 Dashboard Vértiq - Análise de Receitas")

with col3:
    st.caption("💼 Dados: Janeiro vs Dezembro 2025")