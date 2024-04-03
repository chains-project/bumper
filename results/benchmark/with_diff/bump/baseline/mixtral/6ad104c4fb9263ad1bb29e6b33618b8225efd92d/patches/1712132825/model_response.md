Sure, here's a proposed patch for the failing client code:
```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

...

@Override
protected void decodeHandshakeMessage(InputStream input) throws IOException {
    int type = readUint8(input);
    if (type == HandshakeType.helloRetryRequest.getValue()) {
        decodeHelloRetryRequest(input);
    } else if (type == HandshakeType.newSessionTicket.getValue()) {
        decodeNewSessionTicket(input);
    } else if (type == HandshakeType.encryptedExtensions.getValue()) {
        decodeEncryptedExtensions(input);
    } else if (type == HandshakeType.certificate.getValue()) {
        decodeCertificate(input);
    } else if (type == HandshakeType.serverKeyExchange.getValue()) {
        decodeServerKeyExchange(input);
    } else if (type == HandshakeType.certificateVerify.getValue()) {
        decodeCertificateVerify(input);
    } else if (type == HandshakeType.finished.getValue()) {
        decodeFinished(input);
    } else if (type == HandshakeType.keyUpdate.getValue()) {
        decodeKeyUpdate(input);
    } else {
        throw new TlsFatalAlert(AlertDescription.decode(type));
    }
}
```
The only change I made is to import and use the new `TlsFatalAlert` class from the updated library version. I also changed the last line of the method to use the new `TlsFatalAlert` constructor that takes an `AlertDescription` argument.

Note that I did not need to create any new variables or remove the `@Override` decorator, since the method signature has not changed. Additionally, I did not use any removed library methods, but I did use the new `TlsFatalAlert` constructor that was added in the updated version.