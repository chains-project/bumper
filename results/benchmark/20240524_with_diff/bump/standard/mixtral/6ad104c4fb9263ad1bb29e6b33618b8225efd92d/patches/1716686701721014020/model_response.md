Here'ed the updated code to fix the error:

```java
import org.bouncycastle.util.Arrays;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.AlertDescription;

// ...

public void decode(TlsUtilities util, InputStream in, int length) throws IOException {
    // ...
    if (this.tag == TlsConstants.TAG_APPLICATION_DATA) {
        // ...
        if (this.version == TlsUtilities.TLS12) {
            // ...
            if (this.type == TlsConstants.CONTENT_TYPE_HANDSHAKE) {
                // ...
                if (length > 0) {
                    // ...
                    if (length == 32) {
                        // ...
                        if (this.clientRandom.length != 32) {
                    // ...
                    }
                    // ...
                } else if (length > 0) {
                    // ...
                    if (length == 12) {
                        // ...
                        if (this.clientRandom.length != 12) {
                    // ...
                    }
                    // ...
                }
                // ...
            }
            // ...
        }
        // ...
    }
    // ...
    if (this.tag == TlsConstants.TAG_ALERT) {
        // ...
        if (length > 0) {
            // ...
            if (length == 2) {
                // ...
                short value = in.readByte();
                value = (short) (value << 8 | in.readByte());
                throw new TlsFatalAlert(new AlertDescription(value));
            }
            // ...
        }
        // ...
    }
    // ...
}
// ...
```

I added the following import statements:

```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.AlertDescription;
```

And changed the following line:

```java
throw new TlsFatalAlert(value);
```

To:

```java
throw new TlsFatalAlert(new AlertDescription(value));
```

This should fix the illegal start of type error caused by the removal of the `org.bouncycastle.crypto.tls.TlsFatalAlert(short)` constructor.