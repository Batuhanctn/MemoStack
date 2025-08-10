# MemoStack ve Kullanıcı Yönetimi Projesi

Bu proje, kullanıcıların kaydolup giriş yapabildiği, profil bilgilerini yönetebildiği ve kişisel notlar oluşturabildiği Python tabanlı bir web uygulamasıdır. Tüm veriler Google Firebase üzerinde gerçek zamanlı olarak saklanmaktadır.

## ✨ Detaylı Özellikler

-   **Kullanıcı Kimlik Doğrulama (Authentication):**
    -   Firebase Authentication servisi kullanılarak güvenli bir şekilde yeni kullanıcı kaydı oluşturulur.
    -   Kayıtlı kullanıcılar e-posta ve şifreleri ile sisteme giriş yapabilir.
-   **Profil Yönetimi:**
    -   Her kullanıcının Firebase Realtime Database üzerinde kendine ait bir profili bulunur.
    -   Kullanıcılar `Ad Soyad`, `Üniversite` ve `Bölüm` gibi kişisel bilgilerini güncelleyebilir.
-   **Not Yönetimi (CRUD Operasyonları):**
    -   Giriş yapmış kullanıcılar kendilerine özel notlar oluşturabilir (`Create`), okuyabilir (`Read`), güncelleyebilir (`Update`) ve silebilir (`Delete`).

## 🛠️ Kullanılan Teknolojiler

-   **Backend:** Python, Flask
-   **Veritabanı:** Google Firebase (Authentication & Realtime Database)
-   **Kütüphaneler:** `Flask`, `pyrebase4`, `firebase-admin`

## 🚀 Kurulum ve Çalıştırma

(Kurulum adımları önceki versiyon ile aynıdır ve geçerlidir.)

## 🌊 Veri Akış Mimarisi (Örnek: Kullanıcı Kaydı)

Bir kullanıcının kayıt olma sürecindeki veri akışı şu adımları izler:

1.  **Kullanıcı Arayüzü (`signup.html`):** Kullanıcı, kayıt formuna `username`, `mail` ve `password` bilgilerini girer ve formu gönderir.
2.  **Flask Rota (`app.py` -> `/signup`):** `POST` isteği bu rota tarafından yakalanır. Form verileri `request.form` ile alınır.
3.  **Kimlik Doğrulama (`db.py` -> `Firebase.register`):** `app.py`, alınan `mail` ve `password` ile `db.py` içerisindeki `register` fonksiyonunu çağırır. Bu fonksiyon, Firebase Authentication servisine yeni bir kullanıcı oluşturma isteği gönderir.
4.  **Veritabanı Kaydı (`user.py` -> `User.save`):** Kullanıcı Firebase'de oluşturulduktan sonra, `app.py` yeni kullanıcının ID'sini alır ve bu ID ile bir `User` nesnesi oluşturur. `user.save()` metodu çağrılarak Realtime Database'de bu kullanıcı için boş bir profil oluşturulur.
5.  **Profil Güncelleme (`user.py` -> `User.update`):** Son olarak, formdan gelen `username` bilgisi ile `user.update()` metodu çağrılır ve kullanıcının profili güncellenir.
6.  **Yönlendirme:** İşlem tamamlandığında kullanıcı, kendi profil sayfasına (`userpage.html`) yönlendirilir.

## 🔌 Detaylı API Rotaları (Endpoints)

-   `GET /`: Ana sayfayı render eder.
-   `POST /login`:
    -   **Açıklama:** Kullanıcı girişi yapar.
    -   **Form Verileri:** `mail`, `password`
-   `POST /signup`:
    -   **Açıklama:** Yeni kullanıcı kaydı oluşturur.
    -   **Form Verileri:** `mail`, `password`, `username`
-   `POST /information/<user_id>`:
    -   **Açıklama:** Kullanıcı profil bilgilerini günceller.
    -   **Form Verileri:** `fullname`, `university`, `department`
-   `GET /userpage/<user_id>`: Kullanıcının profil sayfasını render eder.

## 💡 Gelecekteki Geliştirmeler

-   **Not Arama:** Kullanıcıların notları içinde anahtar kelime ile arama yapabilmesi.
-   **Şifre Sıfırlama:** Kullanıcıların "şifremi unuttum" özelliği ile şifrelerini yenileyebilmesi.
-   **Not Kategorizasyonu:** Notlara etiket veya kategori ekleyerek filtreleme yapma imkanı.
-   **Dosya Yükleme:** Notlara resim veya doküman gibi dosyalar ekleyebilme.


