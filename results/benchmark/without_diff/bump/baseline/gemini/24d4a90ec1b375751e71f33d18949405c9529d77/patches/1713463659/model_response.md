```java
import com.jcabi.aspects.Tv;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;

public class AwsOcketITCase {

    public static void main(String[] args) throws IOException {
        URL url = new URL("https://www.google.com/");
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.connect();

        int responseCode = connection.getResponseCode();
        System.out.println("Response Code: " + responseCode);

        connection.disconnect();
    }
}
```