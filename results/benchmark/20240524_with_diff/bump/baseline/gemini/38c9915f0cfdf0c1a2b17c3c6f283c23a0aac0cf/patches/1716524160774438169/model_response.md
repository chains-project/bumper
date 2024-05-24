```java
import org.cactoos.text.JoinedText;

public class WalletsIn {

    public String walletsIn(String url) throws Exception {
        String walletsIn = new JoinedText(
                "GET ",
                url,
                " HTTP/1.1\r\n",
                "Host: ",
                "127.0.0.1:8080\r\n",
                "Authorization: Basic ",
                "YWRtaW46cGFzc3dvcmQ=\r\n",
                "\r\n"
        ).asString();
        return walletsIn;
    }
}
```