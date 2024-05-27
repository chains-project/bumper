Here's the patched version of the failing method. I replaced the usage of `TlsFatalAlert` with a custom exception.

```java
import java.io.IOException;

public class ChachaDecoder {
    // ...

    private void decode(TlsContext context, InputStream in, ChannelHandlerContext handlerContext) throws IOException {
        // ...

        try {
            // ...
        } catch (Exception e) {
            throw new TlsFatalAlert(40, "Error decoding record.");
        }
    }

    // ...

    private static class TlsFatalAlert extends IOException {
        private final short alertDescription;

        public TlsFatalAlert(int alertDescription) {
            super("TlsFatalAlert: " + TlsUtilities.alertDescription(alertDescription));
            this.alertDescription = (short) alertDescription;
        }

        public short getAlertDescription() {
            return alertDescription;
        }
    }
}
```

This patch creates a custom `TlsFatalAlert` exception within the `ChachaDecoder` class. It has the same constructor and method as the removed `TlsFatalAlert` class. The `decode` method now throws the custom `TlsFatalAlert` exception.