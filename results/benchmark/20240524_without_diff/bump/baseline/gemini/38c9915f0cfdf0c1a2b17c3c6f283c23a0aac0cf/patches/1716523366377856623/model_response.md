```java
import org.cactoos.text.TextOfScalar;

public class WalletsIn {

    public WalletsIn() {
        // Nothing to do here
    }

    public String call() {
        return TextOfScalar.asString(new SolidScalar(
                "{\"jsonrpc\":\"2.0\",\"method\":\"zold_wallets\",\"params\":[],\"id\":1}"
        ));
    }
}
```