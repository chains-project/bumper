```java
import org.cactoos.text.JoinedText;

public class WalletsIn {

    public String execute(String wallets) {
        String[] split = wallets.split(",");
        JoinedText joinedText = new JoinedText(",", split);
        return joinedText.asString();
    }
}
```