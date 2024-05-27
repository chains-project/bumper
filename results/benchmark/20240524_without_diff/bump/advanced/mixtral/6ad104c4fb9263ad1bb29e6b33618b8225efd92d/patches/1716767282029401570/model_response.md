Here's a proposed patch for the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// Add the following import statement
import org.bouncycastle.crypto.tls.TlsUtils;

public class ChachaDecoder {
    // Existing code

    private void decode(InputStream input, byte[] output) throws IOException {
        // Existing code

        int macLength = mac.length;
        if (macLength > 0) {
            // Existing code

            if (!TlsUtils.isValidLabel(label)) {
                throw new TlsFatalAlert(AlertDescription.internal_error,
                        "invalid label in MAC");
            }

            // Existing code
        }

        // Existing code
    }

    // Existing code
}
```
This patch adds the missing import statement for `TlsUtils` class, which is used in the `decode` method. The `TlsUtils` class is part of the Bouncy Castle library and is required to resolve the `TlsUtils.isValidLabel` method call. This should fix the "package org.bouncycastle.crypto.tls does not exist" error.