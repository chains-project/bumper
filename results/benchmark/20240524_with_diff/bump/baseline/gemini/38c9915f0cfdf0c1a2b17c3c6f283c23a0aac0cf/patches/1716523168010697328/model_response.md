```java
import org.cactoos.text.JoinedText;

import java.util.ArrayList;
import java.util.List;

public class WalletsIn {

    public WalletsIn() {
    }

    public JoinedText walletsIn(String address, String... addresses) {
        List<String> allAddresses = new ArrayList<>();
        allAddresses.add(address);
        for (String addr : addresses) {
            allAddresses.add(addr);
        }
        return new JoinedText(",", allAddresses);
    }
}
```