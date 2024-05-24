Here's the proposed patch for the failing method:

```java
import org.bouncycastle.crypto.tls.AlertDescription;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
        throws IOException {

    KeyParameter macKey = initRecordMAC(decryptCipher);

    byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new org.bouncycastle.crypto.tls.TlsFatalAlert(new AlertDescription(20));
    }

    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

    return output;
}
```

The changes include:

* Importing the `AlertDescription` class from the updated library.
* Replacing the deprecated constructor for `TlsFatalAlert` with a new one that takes an `AlertDescription` object as a parameter.
* Creating a new `AlertDescription` object with the value of `20` (the value for `bad_record_mac`), and passing it to the `TlsFatalAlert` constructor.