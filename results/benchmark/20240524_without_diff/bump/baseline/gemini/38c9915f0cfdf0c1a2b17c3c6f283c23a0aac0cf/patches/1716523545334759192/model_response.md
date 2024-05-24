```java
import org.cactoos.scalar.IoChecked;

public class WalletsIn {

    public WalletsIn() {
        new IoChecked(this::getWallets);
    }

    private byte[] getWallets() {
        return new byte[0];
    }
}
```