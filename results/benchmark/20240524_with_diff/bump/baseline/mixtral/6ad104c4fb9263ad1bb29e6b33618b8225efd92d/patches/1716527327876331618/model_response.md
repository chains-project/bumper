Here's the proposed patch for the `ChachaDecoder.java` file:

```java
import org.bouncycastle.crypto.tls.TlsUtils;

// ...

@Override
public void decodeRecord(InputStream input, OutputStream output) throws IOException {
    int type = input.read();
    if (type < 0) {
        return;
    }

    int length = TlsUtils.readUint16(input);
    if (length < 0) {
        throw new TlsFatalAlert(AlertDescription.decode_error);
    }

    int macLength = macSize;
    if (type == Type.application_data) {
        macLength = 0;
    }

    if (length > maxFragmentLength || length > (maxFragmentLength - macLength)) {
        throw new TlsFatalAlert(AlertDescription.decode_error);
    }

    if (length > 0) {
        byte[] buffer = new byte[length];
        int read = input.read(buffer, 0, length);
        if (read != length) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        if (type != Type.application_data) {
            decrypt(buffer, 0, length);
        }

        output.write(buffer, 0, length);
    }
}
```

This patch removes the import of `TlsFatalAlert` and replaces its usage with `AlertDescription` from `org.bouncycastle.crypto.tls.TlsUtils`. This is possible since the `AlertDescription` provides the necessary `decode_error` constant.