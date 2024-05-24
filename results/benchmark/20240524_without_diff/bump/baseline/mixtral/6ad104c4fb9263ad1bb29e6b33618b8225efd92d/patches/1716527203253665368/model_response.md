Here's the fixed version of the failing method in `ChachaDecoder.java`:

```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    // ...

    @Override
    public void notifyError(int alert) {
        throw new TlsFatalAlert((short) alert);
    }

    // ...
}
```

The `TlsFatalAlert` constructor with a single `short` argument has been added in the new version of the library. So, we can replace the original code with this constructor.