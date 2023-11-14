## AST-YT

Bu Python betiği, belirli kriterlere göre YouTube videolarını arar ve sonuçları döndürür. Kullanıcıların belirli tarihler arasında, belirli anahtar kelimelerle, belirli bir izlenme sayısı ve maksimum süre ile videoları aramasına olanak sağlar. Ayrıca, kullanıcı yaş kısıtlamalı videoları aramak isteyip istemediğini de seçebilir.

## Gereksinimler
- Google API Client Library for Python (`google-api-python-client`)
- Python `isodate` modülü (ISO 8601 süre biçimlerini ayrıştırmak için)
- YouTube Data API Anahtarı

## Kullanım

1. Bu repoyu klonlayın veya indirin.
2. `pip3 install --upgrade google-api-python-client isodate` komutunu kullanarak gerekli modülleri yükleyin.
3. Betiği çalıştırın ve gerekli bilgileri girin.
    - Başlangıç ve bitiş tarihleri (YYYY-MM-DD formatında)
    - Aranacak anahtar kelimeler (virgülle ayrılmış)
    - Gösterilecek maksimum video sayısı
    - Maksimum video süresi (dakika cinsinden)
    - Minimum video izlenme sayısı
    - Yaş kısıtlaması olup olmadığı (Eğer varsa 'E', yoksa 'H')
