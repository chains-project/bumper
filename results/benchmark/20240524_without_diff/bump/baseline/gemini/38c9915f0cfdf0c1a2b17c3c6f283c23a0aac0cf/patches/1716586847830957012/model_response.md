```java
import org.cactoos.scalar.UncheckedScalar;
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

public class RtTransaction {

    // ...

    public static String getTransaction(String url) throws IOException {
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("User-Agent", "Mozilla/5.0");
        int responseCode = con.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) { // success
            Scanner scanner = new Scanner(con.getInputStream());
            String inline = scanner.nextLine();
            scanner.close();
            return inline;
        } else {
            throw new RuntimeException("GET request not worked");
        }
    }

    // ...

}
```