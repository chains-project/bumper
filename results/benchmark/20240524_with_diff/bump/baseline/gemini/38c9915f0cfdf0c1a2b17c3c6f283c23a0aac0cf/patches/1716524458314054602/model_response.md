```java
import org.cactoos.text.FormattedText;

public class WalletsIn {

    private final FormattedText formattedText;

    public WalletsIn(FormattedText formattedText) {
        this.formattedText = formattedText;
    }

    public String getWallets(String url, String apiKey) {
        String wallets = "";
        try {
            wallets = this.formattedText.asString(
                "curl -X GET \\" +
                "  '%s' \\" +
                "  -H 'Authorization: Bearer %s' \\" +
                "  -H 'Content-Type: application/json' \\" +
                "  -H 'Accept: application/json'",
                url,
                apiKey
            );
        } catch (Exception e) {
            e.printStackTrace();
        }
        return wallets;
    }
}
```