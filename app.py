import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Моё приложение", page_icon="🚀")

def setup_ios_pwa(app_title: str, icon_url: str):
    js_code = f"""
    <script>
        const parentDoc = window.parent.document;
        
        // 1. Название приложения под иконкой на экране "Домой"
        let titleMeta = parentDoc.querySelector('meta[name="apple-mobile-web-app-title"]');
        if (!titleMeta) {{
            titleMeta = parentDoc.createElement('meta');
            titleMeta.name = 'apple-mobile-web-app-title';
            parentDoc.head.appendChild(titleMeta);
        }}
        titleMeta.content = "{app_title}";

        // 2. Полноэкранный режим (скрывает адресную строку Safari)
        let capableMeta = parentDoc.querySelector('meta[name="apple-mobile-web-app-capable"]');
        if (!capableMeta) {{
            capableMeta = parentDoc.createElement('meta');
            capableMeta.name = 'apple-mobile-web-app-capable';
            parentDoc.head.appendChild(capableMeta);
        }}
        capableMeta.content = "yes";

        // 3. Иконка для экрана "Домой" (180x180 PNG)
        let iconLink = parentDoc.querySelector('link[rel="apple-touch-icon"]');
        if (!iconLink) {{
            iconLink = parentDoc.createElement('link');
            iconLink.rel = 'apple-touch-icon';
            parentDoc.head.appendChild(iconLink);
        }}
        iconLink.href = "{icon_url}";
    </script>
    """
    components.html(js_code, height=0, width=0)

# Вызываем функцию, передавая название и прямую ссылку на PNG-иконку
setup_ios_pwa(
    app_title="БИО",
    icon_url="/app/static/"
)

st.write("Hi")
