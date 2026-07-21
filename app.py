import streamlit as st
import openai

# 1. API Düyməsinin və Qlobal Tənzimləmələrin Qurulması
# Qeyd: Real sistemdə API açarını təhlükəsizlik üçün st.secrets daxilində saxlayacağıq.
openai.api_key = st.secrets.get("OPENAI_API_KEY", "bura_oz_real_api_acarinizi_yaza_bilərsiniz")

# 2. Qlobal Paket Limitlərinin Təyini ($19, $49 və $300-lük sistem üçün)
PLAN_LIMITS = {
    "Starter": 50000,       # $19-lıq paket üçün aylıq söz limiti
    "Growth": 200000,      # $49-luq paket üçün aylıq söz limiti
    "Enterprise": 9999999  # $300-lük qeyri-məhdud böyük paket
}

def count_words(text):
    """Mətndəki sözlərin sayını hesablamaq üçün daxili funksiya"""
    if not text:
        return 0
    return len(text.split())

# 3. İstifadəçinin Cari Sessiya Yaddaşının (State) Aktiv Edilməsi
if "used_words" not in st.session_state:
    st.session_state.used_words = 0

if "current_plan" not in st.session_state:
    st.session_state.current_plan = "Starter"  # Standart olaraq Starter ilə başlayırıq

# 4. Saytın Professional Vizual İnterfeysi (UI)
st.set_page_config(page_title="CopyAI Pro - SaaS", page_icon="🚀", layout="centered")
st.title("🚀 CopyAI Pro — Süni İntellektli Mətn Generatoru")
st.subheader("Frilanserlər və Agentliklər Üçün Qlobal SaaS Platforması")

# Sol paneldə istifadəçinin limit məlumatlarını göstəririk
st.sidebar.header("📊 İstifadəçi Paneli")
st.sidebar.write(f"Cari Paketiniz: {st.session_state.current_plan} Plan")
st.sidebar.progress(min(st.session_state.used_words / PLAN_LIMITS[st.session_state.current_plan], 1.0))
st.sidebar.write(f"📝 İstifadə olunan söz: {st.session_state.used_words} / {PLAN_LIMITS[st.session_state.current_plan]}")

# 5. Mətn Daxiletmə Xanaları
user_prompt = st.text_area(
    "Süni intellektin nə yazmasını istəyirsiniz? (Məsələn: 'Sosial media üçün post', 'Professional məqalə')",
    placeholder="Mətn mövzusunu bura daxil edin...",
    height=150
)

# 6. Əsas "Generate" (Mətn Yarat) Düyməsi və Limit Yoxlanışı
if st.button("Mətni Generasiya Et ✨", use_container_width=True):
    if not user_prompt.strip():
        st.warning("Zəhmət olmasa, ilk öncə mətn mövzusunu daxil edin.")
    
    # İSTİFADƏÇİNİN LİMİTİNİ YOXLAYIRIQ 🛡️
    elif st.session_state.used_words >= PLAN_LIMITS[st.session_state.current_plan]:
        st.error("⚠️ Aylıq söz limitiniz bitmişdir! Zəhmət olmasa paketinizi dollarla yeniləyin.")
        st.info("💡 Paket linkləriniz: Starter ($19) | Growth ($49) | Enterprise ($300)")
    
    else:
        with st.spinner("Süni intellekt mətni hazırlayır, zəhmət olmasa gözləyin..."):
            try:
                # OpenAI API-yə rəsmi sorğunun göndərilməsi
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Sən peşəkar bir mətn yazarı (copywriter) və marketoloqsan."},
                        {"role": "user", "content": user_prompt}
                    ],
                    max_tokens=1000
                )
                
                # Yaradılan mətni əldə edirik
                ai_generated_text = response.choices[0].message['content']
                
                # Sözlərin sayını hesablayırıq və limitə əlavə edirik 📈
                new_words_count = count_words(ai_generated_text)
                st.session_state.used_words += new_words_count
                
                # Ekranda nəticəni göstəririk
                st.success(f"Mətn uğurla yaradıldı! (Yaradılan söz sayı: {new_words_count})")
                st.write(ai_generated_text)
                
                # Səhifəni yeniləyirik ki, sol paneldəki limit sayğacı dərhal artsın
                st.rerun()
                
            except Exception as e:
                st.error(f"API xətası baş verdi: {str(e)}")