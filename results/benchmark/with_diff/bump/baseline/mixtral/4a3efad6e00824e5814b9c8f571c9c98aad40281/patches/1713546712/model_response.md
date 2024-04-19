Here's a possible patch for the failing code:

```java
import eu.europa.esig.dss.pades.PadesCertificationLevel;

// ...

public void sign(InputStream inputStream, OutputStream outputStream,
                 String signatureFieldName, String certificationLevel) throws Exception {
    PadesSigner signer = new PadesSigner(certificationLevel);
    // ...
    signer.setSignatureFieldName(signatureFieldName);
    // ...
    signer.sign(inputStream, outputStream);
}

```

In this patch, I replaced the usage of `CertificationPermission` with `PadesCertificationLevel`, which is a new class added in the updated library. This should fix the "cannot find symbol" error.

Note that the `PadesCertificationLevel` accepts a string value that corresponds to the certification level, so you may need to update the `certificationLevel` parameter accordingly. For example, if you previously used `CertificationPermission.NO_CERTIFICATION`, you can replace it with `PadesCertificationLevel.NO_CERTIFICATION`.