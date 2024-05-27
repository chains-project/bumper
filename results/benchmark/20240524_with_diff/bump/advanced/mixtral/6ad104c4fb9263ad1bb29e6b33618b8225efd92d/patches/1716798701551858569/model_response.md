Here's the patched version of the failing method:
```java
import org.bouncycastle.crypto.tls.AlertDescription;

import java.io.IOException;

public void decodeRecord(ByteBuffer byteBuffer) throws IOException {
    short contentType = byteBuffer.getShort();
    if (contentType != 20) {
        throw new TlsFatalAlert(AlertDescription.decode(contentType));
    }
    // ...
}
```
The `TlsFatalAlert` constructor has been removed, so we need to replace it with a call to the `AlertDescription.decode()` method, which has been added. We also need to import `org.bouncycastle.crypto.tls.AlertDescription`.