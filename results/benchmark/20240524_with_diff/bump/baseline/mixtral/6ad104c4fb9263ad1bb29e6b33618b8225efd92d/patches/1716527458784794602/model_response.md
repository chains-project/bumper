Here's the patched method that should fix the error:

```java
import org.bouncycastle.crypto.tls.AlertDescription;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
        throws IOException {

    KeyParameter macKey = initRecordMAC(decryptCipher);

    byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new org.bouncycastle.crypto.tls.TlsFatalAlert(new AlertDescription(7));
    }

    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

    return output;
}
```

The changes include:

* Importing the `AlertDescription` class from the `org.bouncycastle.crypto.tls` package.
* Replacing the `TlsFatalAlert` constructor that takes a short argument with the new constructor that takes an `AlertDescription` argument.
* Creating a new `AlertDescription` instance with the value 7, which corresponds to `bad_record_mac`.