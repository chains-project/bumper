```java
import java.text.Normalizer;

import io.zold.api.Wallet;

public class WalletsIn {
    public void process() {
        String text = "some text";
        text = Normalizer.normalize(text, Normalizer.Form.NFKD);
    }
}
```