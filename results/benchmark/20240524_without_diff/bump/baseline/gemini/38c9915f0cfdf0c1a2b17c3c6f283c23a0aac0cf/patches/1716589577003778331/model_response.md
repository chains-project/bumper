```java
import org.cactoos.text.UncheckedText;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;

public class RtTransaction {

    public String getTransaction(String url) throws IOException {
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        con.setRequestMethod("GET");
        int responseCode = con.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) { // success
            return new UncheckedText(con.getInputStream()).asString();
        } else {
            return null;
        }
    }
}
```