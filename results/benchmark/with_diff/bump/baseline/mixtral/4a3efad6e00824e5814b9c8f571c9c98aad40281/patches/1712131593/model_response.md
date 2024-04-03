I cannot directly access your codebase, but I can propose a patch for the failing method. Here's the fixed `Signer.java` method with the updated import statement based on the provided information:

```java
import eu.europa.esig.dss.pades.PadesSigner;
import eu.europa.esig.dss.pades.PadesSignatureLevel;
import eu.europa.esig.dss.pades.PadesSigningCertificateSource;
import eu.europa.esig.dss.pades.PadesSigningCertificate;
import eu.europa.esig.dss.pades.PadesCertificationLevel;

// ...

@Override
public void signPdf(InputStream inputStream, OutputStream outputStream, String signatureFieldName,
                     String reason, String location, String certificateAlias, String password) throws Exception {
    // Your existing code here

    // Create a PadesSigner object
    PadesSigner padesSigner = new PadesSigner(signingCertificateSource, PadesSignatureLevel.B_BASIC);

    // Set the certification level
    padesSigner.setCertificationLevel(PadesCertificationLevel.CERTIFIED_NO_CHANGES_ALLOWED);

    // Set the permission
    padesSigner.setSigningCertificate(signingCertificate);
    padesSigner.setCertificationPermission(CertificationPermission.NO_CHANGES_ALLOWED);

    // Rest of your existing code here
}
```

Please note that I cannot guarantee this patch will work without any issues, as I don't have the complete codebase and context. Make sure to test the updated code thoroughly.