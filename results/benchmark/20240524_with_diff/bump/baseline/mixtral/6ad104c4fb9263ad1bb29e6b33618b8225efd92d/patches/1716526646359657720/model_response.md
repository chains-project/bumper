Here's a possible patch for the failing method in the client code:

```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.AlertDescription;

// ...

@Override
public void decode(InputStream input, ByteQueue queue) throws IOException {
    int tag = input.read();
    if (tag != TAG_APPLICATION_DATA) {
        throw new TlsFatalAlert(AlertDescription.decode(input));
    }
    // ...
}
```

Note that I replaced the usage of `AlertDescription.getAlertDescription()` with `AlertDescription.decode(input)`, which is a new method added in the updated library version.