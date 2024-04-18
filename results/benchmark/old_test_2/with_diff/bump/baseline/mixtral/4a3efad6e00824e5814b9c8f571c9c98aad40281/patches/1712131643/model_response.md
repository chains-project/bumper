I cannot directly see the full code and error message, but based on the information provided, it seems that the `CertificationPermission` class is no longer available in the updated version of the `eu.europa.esig.dss.pades` package.

Assuming the `Signer` class has a method that uses `CertificationPermission`, you can try modifying the method to not use `CertificationPermission` directly. Instead, you can use the `PadesSigner` class, which is a subclass of `CertificationPermission`, and provides similar functionality.

Here's an example of how you can modify the method:

```java
import eu.europa.esig.dss.pades.PadesSigner;

// ...

@Override
public void sign(InputStream inputStream, OutputStream outputStream) throws Exception {
    PadesSigner signer = new PadesSigner(keystore, keystorePassword, certificateAlias, digestAlgorithm, signatureAlgorithm, signingCertificate);
    signer.setSignatureLevel(SignatureLevel.CERTIFIED_NO_CHANGE_EXCL);
    signer.setSignaturePolicy(signaturePolicy);
    signer.setTsaClient(tsaClient);
    signer.setOcspClient(ocspClient);
    signer.setIncludeCertificate(true);
    signer.setVisibleSignature(visibleSignature);
    signer.setSigningDate(new Date());
    signer.setApprovalSignatureField(approvalSignatureField);
    signer.setReason(reason);
    signer.setLocation(location);
    signer.setExtraDataToSign(extraDataToSign);
    signer.setBouncyCastleProvider();
    signer.setTspSource(tspSource);
    signer.setTimeStampToken(timeStampToken);

    signer.sign(inputStream, outputStream);
}
```

This modified method uses `PadesSigner` instead of `CertificationPermission`, and sets the signature level to `CERTIFIED_NO_CHANGE_EXCL`, which is equivalent to the `CERTIFIED_NO_CHANGE` level provided by `CertificationPermission`.

Note that this is just an example, and the exact modifications you need to make will depend on the specifics of your code and the functionality you need to preserve.