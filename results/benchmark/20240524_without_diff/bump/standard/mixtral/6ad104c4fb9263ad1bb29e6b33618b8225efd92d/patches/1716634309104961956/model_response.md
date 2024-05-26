Here'`java.lang.Integer` is the fully qualified version of `Integer`.

```java
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws java.io.IOException {
    org.bouncycastle.crypto.params.KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = io.github.hapjava.server.impl.crypto.PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!org.bouncycastle.util.Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new org.bouncycastle.crypto.tls.TlsFatalAlert(new org.bouncycastle.crypto.tls.AlertDescription(10));
    }
    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(cipherte struct, 0, ciphertext.length, output, 0);
    return output;
}
```

In the above code, I have replaced the `org.bouncycastle.crypto.tls.AlertDescription.bad_record_TlsFatalAlert(AlertDescription.bad_record_mac)` with `new org.bouncycastle.crypto.tls.AlertDescription(10)` as the `AlertDescription` is not accessible directly.

Note: The `bad_record_mac` value is 10, so I have used it directly.