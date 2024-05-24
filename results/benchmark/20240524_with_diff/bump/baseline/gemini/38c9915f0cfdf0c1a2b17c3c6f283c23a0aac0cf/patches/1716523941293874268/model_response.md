```java
import org.cactoos.text.TextOfScalar;

public class WalletsIn {

    public WalletsIn(String url, String password) {
        this.url = url;
        this.password = password;
    }

    private final String url;
    private final String password;

    public String getUrl() {
        return url;
    }

    public String getPassword() {
        return password;
    }

    public String toString() {
        return TextOfScalar.asString(this);
    }
}
```