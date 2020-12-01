
class Messages:

    START_MSG = "Merhabalar {}.\n\nBen YouTube Çevirici Botuyum.Bana yetki verdikten sonra herhangi bir telegram videosunu youtube'a yüklemek için beni kullanabilirsiniz.Şunlardan daha fazla bilgi edinebilirsiniz:/help.\n\nTeşekkür Ederim."

    HELP_MSG = [
        ".",
        "Merhabalar.\n\nHer şey sırayla. YouTube'un yüklenen her videoyu işlediğinin farkında olmalısınız, ve AI'si, yüklenir yüklenmez telif hakkıyla korunan içerik bulursa videoyu telif hakları için işaretlemesi şaşırtıcı olur, ve videoyu yayınlayamayacaksınız.\n\nNasıl çalıştığımı öğrenmek için tüm sayfaları okuyun.",

        "**Nasıl çalıştığımı öğrenelim.**\n\n**Adım 1:** __Bana youtube kanalına yükleme yetkisi veriyorsun.Gelecek sayfalarda bunun hakkında daha fazla bilgi var.__\n\n**Adım 2:** __Bana herhangi bir Telegram videosunu iletiyorsun.__\n\n**Adım 3:** __Cevap ver __/upload __iletilen video dosyasına.Ayrıca upload komutunda bir başlık belirtebilirsiniz,ama isteğe bağlı olsa. __`/upload`.__Başlık verilmemişse, dosya adı başlık olarak kullanılacak.__\n\n**Adım 4:** __Dosyayı uzaktan indiriyorum ve Youtube kanalınıza yüklüyorum.__\n\n**Adım 5:** __Yükledikten sonra size Youtube bağlantısını gönderiyorum.__",

        "**Youtube kanalınızı oluşturun**\n\nYoutube Kanalınız yoksa beni kullanmanın bir anlamı yok.Bu yüzden bir tane oluşturmak için verilen adımları izleyin.\n\n**Adım 1:** __Bilgisayarda veya mobil cihaz kullanarak YouTube'da oturum açın.__\n\n**Adım 2:** __Kanal gerektiren herhangi bir işlemi deneyin, video yüklemek gibi, yorum gönderme veya oynatma listesi oluşturma gibi.__\n\n**Adım 3:** __Henüz bir kanalınız yoksa, kanal oluşturmak için bir istem görürsünüz.__\n\n**Adım 4:** __Ayrıntıları kontrol edin ve yeni kanalınızı oluşturmayı onaylayın.__",

        "**YouTube hesabınızı doğrulayın**\n\nYoutube spam ve kötüye kullanımı çok ciddiye alıyor. Bu yüzden Youtube hesabınızı doğrulamanız istenir. Hesabınızı doğruladıktan sonra, 15 dakikadan daha uzun videolar yükleyebileceksiniz. Hesabınızı doğrulamadıysanız, yüklenen 15 dakikadan uzun her video kaldırılacak.\n[Youtube hesabınızı buradan doğrulayın.](http://www.youtube.com/verify)",

        "**Şimdi izin verelim.**\n\nYoutube hesabınıza video yükleyebilmem için bana erişim vermeniz gerekiyor.Bunun için verilen bağlantıyı açın ve erişime izin verin ve kodu kopyalayın. Buraya gel ve yaz `/authorise kopyalanan kodu bana gönderin.\n\n**Korkma!**\nBen bir hacker değilim veya insanların mahremiyetine sızmak isteyen biri değilim.Gizliliğine saygı duyuyorum. Ben sadece yardım isteyen herkese yardım etmek için buradayım. Eğer bir hacker olsaydım burada oturmayacak olurdum, ama Telegram Botları yazıyorum."
    ]

    NOT_A_REPLY_MSG = "Lütfen bazı video dosyalarına yanıt verin."

    NOT_A_MEDIA_MSG = "Hiçbir medya dosyası bulunamadı. "+NOT_A_REPLY_MSG

    NOT_A_VALID_MEDIA_MSG = "Bu geçerli bir medya değil"

    PROCESSING = "İşleniyor....."

    NOT_AUTHENTICATED_MSG = "Herhangi bir hesaba video yüklemek için kimlik doğrulamamışsın. şu koda bak ve /help hesabını doğrula"

    NO_AUTH_CODE_MSG = "Kod yok. Lütfen bir kod girin"

    AUTH_SUCCESS_MSG = "tebrikler, Youtube'a yüklemek için beni doğruladın.\nMutlu yükleme!"

    AUTH_FAILED_MSG = "Kimlik doğrulama başarısız oldu\nayrıntılar:{}"
    
    AUTH_DATA_SAVE_SUCCESS = "Verilen kimlik doğrulama verileri başarıyla kaydedildi!"
    
