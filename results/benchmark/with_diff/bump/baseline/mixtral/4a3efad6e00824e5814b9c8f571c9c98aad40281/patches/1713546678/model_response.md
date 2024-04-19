Here's a proposed patch for the failing client code:

```java
import eu.europa.esig.dss.pades.PadesCertificationLevel;
import eu.europa.esig.dss.pades.PadesSigner;
import eu.europa.esig.dss.pades.PadesSigningCertificateSource;
import eu.europa.esig.dss.pades.PadesSigningCertificateValidator;
import eu.europa.esig.dss.pades.PadesSignerParameters;
import eu.europa.esig.dss.pades.PadesSignaturePolicies;
import eu.europa.esig.dss.pades.PadesSigningCertificate;
import eu.europa.esig.dss.pades.PadesSignatureService;

// ...

private void signPdf(InputStream inputStream, OutputStream outputStream) throws Exception {
    // ...

    // Replace CertificationPermission with PadesCertificationLevel
    PadesSignerParameters signerParameters = new PadesSignerParameters();
    signerParameters.setCertificationLevel(PadesCertificationLevel.CERTIFY_MINOR_CHANGES);

    // ...

    // Replace CertificationPermission with PadesSigningCertificate
    PadesSigningCertificate signingCertificate = new PadesSigningCertificate(signingCertificateToken,
            new PadesSigningCertificateSource(), new PadesSigningCertificateValidator());

    // Replace CertificationPermission with PadesSigner
    PadesSigner padesSigner = new PadesSigner(signingCertificate, signerParameters);

    // Replace CertificationPermission with PadesSignatureService
    PadesSignatureService signatureService = new PadesSignatureService(padesSigner);

    // ...
}
```

This patch replaces the `CertificationPermission` class with the appropriate classes from the new library version. I've added import statements for the new classes and updated the code to use them. The `PadesCertificationLevel` enum is used instead of `CertificationPermission`, and the `PadesSigningCertificate`, `PadesSigner`, and `PadesSignatureService` classes are used instead of `CertificationPermission`.