```java
import com.google.common.base.Joiner;

import org.cactoos.text.JoinedText;

public class WalletsIn {
    // ...

    @Override
    public String getWallets(String address) {
        return new JoinedText(
                Joiner.on(","),
                walletsRepository.getWallets(address)
        ).asString();
    }

    // ...
}
```