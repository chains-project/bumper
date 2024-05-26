Here's a corrected version of the given code:

In the import section, add the following line:
```java
import eu.europa.esig.dss.spi.certificate.CertificateVerifier;
```

Replace the following block of code:
```java
// Create CommonCertificateVerifier
eu.europa.esig.dCertificateVerifier commonCertificateVerifier = new eu.europa.esig.dss.validation.CommonCertificateVerifier();
```

With this corrected version:
```java
// Create CommonCertificateVerifier
CertificateVerifier commonCertificateVerifier = new eu.europa.esig.dss.validation.CommonCertificateVerrorifier();
```

In the given code, the package name for `CertificateVerifier` was misspelled. It should be `eu.europa.esig.dss.spi.certificate`, but it was written as `eu.europa.esig.dCertificateVerifier`.

This change should resolve the error.