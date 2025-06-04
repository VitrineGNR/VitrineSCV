import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="VitrineSCV - Sistema de Vendas",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("VitrineSCV - Sistema Completo de Vendas")
st.markdown("**Interface moderna para gestão comercial**")

# Menu lateral
st.sidebar.title("Menu Principal")
st.sidebar.markdown("---")

opcao = st.sidebar.selectbox(
    "Navegação:",
    ["🏠 Dashboard", "📋 Propostas", "👥 Clientes", "📦 Produtos", "📊 Relatórios"]
)

# SEÇÃO: DASHBOARD
if opcao == "🏠 Dashboard":
    st.header("Dashboard de Vendas")
    
    # Métricas principais
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="💰 Vendas do Mês",
            value="R$ 124.500,00",
            delta="+12.5%"
        )
    
    with col2:
        st.metric(
            label="📝 Propostas Ativas", 
            value="23",
            delta="+5"
        )
    
    with col3:
        st.metric(
            label="📈 Taxa de Conversão",
            value="38%", 
            delta="+2.5%"
        )
    
    st.markdown("---")
    
    # Gráficos
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.subheader("📈 Evolução de Vendas")
        vendas_data = pd.DataFrame({
            "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
            "Valor": [45000, 55000, 75000, 65000, 95000, 124500]
        })
        
        fig = px.line(
            vendas_data, 
            x="Mês", 
            y="Valor",
            title="Vendas Mensais (R$)",
            markers=True
        )
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with chart_col2:
        st.subheader("🎯 Vendas por Produto")
        produtos_data = pd.DataFrame({
            "Produto": ["Produto A", "Produto B", "Produto C", "Produto D"],
            "Vendas": [45000, 25000, 35000, 20000]
        })
        
        fig = px.pie(
            produtos_data, 
            values="Vendas", 
            names="Produto",
            title="Distribuição de Vendas"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Últimas atividades
    st.subheader("📅 Últimas Atividades")
    atividades = pd.DataFrame({
        "Data": ["04/06/2025", "03/06/2025", "02/06/2025"],
        "Atividade": [
            "Proposta PROP-004 enviada para Cliente DEF",
            "Pedido PED-015 faturado",
            "Nova visita agendada com Empresa ABC"
        ],
        "Status": ["✅ Concluído", "✅ Concluído", "⏳ Pendente"]
    })
    st.dataframe(atividades, use_container_width=True)

# SEÇÃO: PROPOSTAS
elif opcao == "📋 Propostas":
    st.header("Gestão de Propostas")
    
    tab1, tab2, tab3 = st.tabs(["Propostas Ativas", "Nova Proposta", "Histórico"])
    
    with tab1:
        st.subheader("📝 Propostas em Andamento")
        
        # Dados das propostas
        propostas_df = pd.DataFrame({
            "ID": ["PROP-001", "PROP-002", "PROP-003"],
            "Cliente": ["Empresa ABC Ltda", "Loja XYZ Comércio", "Distribuidora 123"],
            "Data": ["01/06/2025", "28/05/2025", "15/05/2025"],
            "Valor": ["R$ 12.500,00", "R$ 8.750,00", "R$ 22.300,00"],
            "Status": ["📤 Enviada", "🔍 Em análise", "⏳ Aguardando resposta"]
        })
        
        st.dataframe(propostas_df, use_container_width=True)
        
        # Ações para propostas
        st.markdown("### 🔧 Ações")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            proposta_selecionada = st.selectbox(
                "Selecione uma proposta:", 
                propostas_df["ID"]
            )
        
        with col2:
            if st.button("📄 Visualizar PDF", use_container_width=True):
                st.success(f"📄 PDF da {proposta_selecionada} gerado com sucesso!")
                st.info("💡 Funcionalidade de PDF será implementada com reportlab/fpdf2")
        
        with col3:
            if st.button("✅ Converter em Pedido", use_container_width=True):
                pedido_id = f"PED-{proposta_selecionada.split('-')[1]}"
                st.success(f"🎉 {proposta_selecionada} convertida em {pedido_id}!")
                st.balloons()
    
    with tab2:
        st.subheader("➕ Criar Nova Proposta")
        
        with st.form("nova_proposta"):
            # Dados do cliente
            st.markdown("#### 👤 Dados do Cliente")
            col1, col2 = st.columns(2)
            
            with col1:
                cliente = st.selectbox(
                    "Cliente:", 
                    ["Empresa ABC Ltda", "Loja XYZ Comércio", "Distribuidora 123", "Novo Cliente..."]
                )
                email_cliente = st.text_input("E-mail:", "contato@empresaabc.com")
            
            with col2:
                telefone_cliente = st.text_input("Telefone:", "(11) 1234-5678")
                data_proposta = st.date_input("Data da Proposta:")
            
            # Produtos
            st.markdown("#### 📦 Produtos")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                produto = st.selectbox("Produto:", ["Produto A", "Produto B", "Produto C", "Produto D"])
            
            with col2:
                quantidade = st.number_input("Quantidade:", min_value=1, value=1)
            
            with col3:
                preco = st.number_input("Preço Unitário (R$):", min_value=0.01, value=2500.00, format="%.2f")
            
            # Condições comerciais
            st.markdown("#### 💳 Condições Comerciais")
            col1, col2 = st.columns(2)
            
            with col1:
                cond_pagamento = st.selectbox(
                    "Condição de Pagamento:", 
                    ["À Vista", "30 dias", "30/60 dias", "30/60/90 dias"]
                )
            
            with col2:
                prazo_entrega = st.text_input("Prazo de Entrega:", "15 dias úteis")
            
            # Observações
            observacoes = st.text_area(
                "📝 Observações:",
                "Proposta sujeita à disponibilidade de estoque. Frete não incluso."
            )
            
            # Botão de envio
            submit = st.form_submit_button("🚀 Gerar Proposta", use_container_width=True)
            
            if submit:
                novo_id = f"PROP-{len(propostas_df) + 1:03d}"
                total = quantidade * preco
                
                st.success(f"🎉 Proposta {novo_id} criada com sucesso!")
                st.info(f"💰 Valor total: R$ {total:,.2f}")
                st.balloons()
    
    with tab3:
        st.subheader("📚 Histórico de Propostas")
        st.info("📊 Implementação do histórico completo com filtros por período, cliente e status")

# SEÇÃO: CLIENTES
elif opcao == "👥 Clientes":
    st.header("Gestão de Clientes")
    
    tab1, tab2 = st.tabs(["Lista de Clientes", "Novo Cliente"])
    
    with tab1:
        st.subheader("👥 Clientes Cadastrados")
        
        clientes_df = pd.DataFrame({
            "Nome": ["Empresa ABC Ltda", "Loja XYZ Comércio", "Distribuidora 123"],
            "CNPJ": ["12.345.678/0001-90", "98.765.432/0001-10", "33.444.555/0001-66"],
            "Telefone": ["(11) 1234-5678", "(21) 9876-5432", "(31) 3333-4444"],
            "Cidade": ["São Paulo/SP", "Rio de Janeiro/RJ", "Belo Horizonte/MG"],
            "Vendas Total": ["R$ 45.000,00", "R$ 32.500,00", "R$ 67.800,00"]
        })
        
        st.dataframe(clientes_df, use_container_width=True)
    
    with tab2:
        st.subheader("➕ Cadastrar Novo Cliente")
        
        with st.form("novo_cliente"):
            col1, col2 = st.columns(2)
            
            with col1:
                nome = st.text_input("Nome/Razão Social:")
                cnpj = st.text_input("CNPJ:")
                telefone = st.text_input("Telefone:")
            
            with col2:
                email = st.text_input("E-mail:")
                cidade = st.text_input("Cidade/UF:")
                observacoes = st.text_area("Observações:")
            
            if st.form_submit_button("💾 Cadastrar Cliente"):
                st.success("✅ Cliente cadastrado com sucesso!")

# SEÇÃO: PRODUTOS
elif opcao == "📦 Produtos":
    st.header("Gestão de Produtos")
    
    tab1, tab2 = st.tabs(["Estoque", "Novo Produto"])
    
    with tab1:
        st.subheader("📦 Controle de Estoque")
        
        produtos_df = pd.DataFrame({
            "Código": ["PRD-001", "PRD-002", "PRD-003", "PRD-004"],
            "Produto": ["Produto A", "Produto B", "Produto C", "Produto D"],
            "Categoria": ["Categoria 1", "Categoria 2", "Categoria 1", "Categoria 3"],
            "Preço": ["R$ 2.500,00", "R$ 4.375,00", "R$ 1.850,00", "R$ 980,00"],
            "Estoque": [25, 8, 45, 12],
            "Mínimo": [10, 10, 15, 5],
            "Status": ["✅ Normal", "⚠️ Baixo", "✅ Normal", "✅ Normal"]
        })
        
        st.dataframe(produtos_df, use_container_width=True)
        
        # Alertas de estoque
        st.markdown("### 🚨 Alertas de Estoque")
        produtos_baixo = produtos_df[produtos_df["Status"] == "⚠️ Baixo"]
        
        if not produtos_baixo.empty:
            st.warning(f"⚠️ {len(produtos_baixo)} produto(s) com estoque baixo!")
            st.dataframe(produtos_baixo[["Produto", "Estoque", "Mínimo"]], use_container_width=True)
        else:
            st.success("✅ Todos os produtos com estoque adequado!")
    
    with tab2:
        st.subheader("➕ Cadastrar Novo Produto")
        st.info("🔧 Funcionalidade em desenvolvimento")

# SEÇÃO: RELATÓRIOS
elif opcao == "📊 Relatórios":
    st.header("Relatórios e Análises")
    
    tab1, tab2, tab3 = st.tabs(["Vendas", "Comissões", "Performance"])
    
    with tab1:
        st.subheader("📈 Relatório de Vendas")
        
        col1, col2 = st.columns(2)
        with col1:
            periodo = st.selectbox("Período:", ["Último mês", "Últimos 3 meses", "Ano atual"])
        with col2:
            representada = st.selectbox("Representada:", ["Todas", "Alpha", "Beta", "Gamma"])
        
        if st.button("📊 Gerar Relatório"):
            st.success("📊 Relatório gerado com sucesso!")
            
            # Dados de exemplo
            vendas_relatorio = pd.DataFrame({
                "Período": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
                "Vendas": ["R$ 45.000", "R$ 55.000", "R$ 75.000", "R$ 65.000", "R$ 95.000", "R$ 124.500"],
                "Meta": ["R$ 50.000", "R$ 50.000", "R$ 60.000", "R$ 60.000", "R$ 80.000", "R$ 100.000"],
                "Atingimento": ["90%", "110%", "125%", "108%", "119%", "125%"]
            })
            
            st.dataframe(vendas_relatorio, use_container_width=True)
    
    with tab2:
        st.subheader("💰 Relatório de Comissões")
        st.info("🔧 Funcionalidade será implementada com cálculos automáticos")
    
    with tab3:
        st.subheader("🎯 Performance da Equipe")
        st.info("🔧 Análise de performance por vendedor")

# Rodapé
st.sidebar.markdown("---")
st.sidebar.markdown("**VitrineSCV v1.0**")
st.sidebar.markdown("Sistema de Vendas Moderno")
st.sidebar.markdown("Desenvolvido com Streamlit")

# Informações de status
with st.sidebar.expander("ℹ️ Informações do Sistema"):
    st.write("✅ Sistema 100% online")
    st.write("✅ Otimizado para iPad")
    st.write("✅ Interface responsiva")
    st.write("✅ Deploy gratuito")
