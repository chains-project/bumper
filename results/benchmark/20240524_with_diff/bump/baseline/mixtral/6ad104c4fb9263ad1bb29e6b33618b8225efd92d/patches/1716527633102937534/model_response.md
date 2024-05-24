Here's a proposed patch for the failing client code:

```java
import org.bouncycastle.crypto.tls.AlertDescription;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
        throws IOException {

    KeyParameter macKey = initRecordMAC(decryptCipher);

    byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new org.bouncycastle.crypto.tls.TlsFatalAlert(new AlertDescription(40));
    }

    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

    return output;
}
```

The changes made are:

* Importing the `AlertDescription` class from the `org.bouncycastle.crypto.tls` package.
* Changing the exception instantiation to use the new constructor that takes an `AlertDescription` argument, and passing a new `AlertDescription` instance with the appropriate value (40, which corresponds to `bad_record_mac`).