Here's a fixed version of the `signPdf` method. I changed the import statement for `CertificationPermission` from `org.openpdfsign` to `eu.europa.esig.dss.pades`.

```java
import eu.europa.esig.dss.pades.CertificationPermission;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.common.PDRectangle;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.KeyStore;
import java.security.KeyStore.PasswordProtection;
import java.security.cert.Certificate;
import java.security.cert.CertificateChain;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;

public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    // ... (rest of the method is unchanged)
    signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
    // ... (rest of the method is unchanged)
}
```

This fix assumes that you add the following import statement at the beginning of your file:

```java
import eu.europa.esig.dss.pades.CertificationPermission;
```