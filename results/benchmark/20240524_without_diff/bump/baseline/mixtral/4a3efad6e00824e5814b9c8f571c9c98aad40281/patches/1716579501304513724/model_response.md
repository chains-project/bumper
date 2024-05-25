Here's a potential patch for the failing client code:

```java
import eu.europa.esig.dss.pades.PadesCertificationLevel;

// ...

public class Signer {
    // ...

    @Override
    public byte[] sign(InputStream inputStream, String outputFilePath, String certificatePath, String pin) throws Exception {
        // ...

        // Replace CertificationPermission with PadesCertificationLevel
        PadesCertificationLevel certificationLevel = PadesCertificationLevel.CERTIFICATION_BASIC;

        // ...

        // Use certificationLevel instead of certificationPermission
        padesSigner.setCertificationLevel(certificationLevel);

        // ...
    }
}
```

This patch replaces the usage of `CertificationPermission` with `PadesCertificationLevel` and sets the certification level to `CERTIFICATION_BASIC`. This should resolve the error message about the missing symbol. Note that the exact replacement value may need to be adjusted depending on the intended behavior of the original `CertificationPermission` usage.