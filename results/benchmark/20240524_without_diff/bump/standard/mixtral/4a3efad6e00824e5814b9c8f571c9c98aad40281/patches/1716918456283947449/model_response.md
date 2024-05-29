Here's the patched code:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.signature.PAdESService;
import eu.europa.esig.dss.spi.x509.tsp.CompositeTSPSource;
import eu.europa.esig.dss.spi.x509.tsp.TSPSource;
import eu.europa.esig.dss.token.JKSSignatureToken;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import org.apache.commons.io.IOUtils;
import org.openpdfsign.dss.PdfBoxNativeTableObjectFactory;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
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

public void signPdf(Path pdfFile, Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws IOException {
    // ... (same code as before)

    PAdESSignatureParameters signatureParameters = new PAdESSignatureParameters();
    // ... (same code as before)

    // Replace CertificationPermission.MINIMAL_CHANGES_PERMITTED
    // with eu.europa.esig.dss.pades.CertificationLevel.MINIMAL
    signatureParameters.setPermission(eu.europa.esig.dss.pades.CertificationLevel.MINIMAL);

    // ... (same code as before)

    // Initialize visual signature and configure
    if (visibleSignature) {
        // ... (same code as before)

        // Replace formatter.format(signatureParameters.getSigningDate().toInstant())
        // with ZonedDateTime.now(ZoneId.systemDefault()).format(formatter)
        fieldParameters.setSignatureDate(ZonedDateTime.now(ZoneId.systemDefault()).format(formatter));

        // ... (same code as before)
    }

    // ... (same code as before)

    CompositeTSPSource compositeTSPSource = new CompositeTSPSource();
    Map<String, TSPSource> tspSources = new HashMap<>();
    compositeTSPSource.setTspSources(tspSources);

    // Replace Configuration.getInstance().getProperties().getStringArray("tsp_sources")
    // with new String[]{"http://timestamp.digicert.com", "http://timestamp.comodoca.com"}
    tspSources.put("http://timestamp.digicert.com", new eu.europa.esig.dss.service.tsp.OnlineTSPSource("http://timestamp.digicert.com"));
    tspSources.put("http://timestamp.comodoca.com", new eu.europa.esig.dss.service.tsp.OnlineTSPSource("http://timestamp.comodoca.com"));

    // ... (same code as before)
}
```

In this patch, I replaced the unresolved `CertificationPermission` with `eu.europa.esig.dss.pades.CertificationLevel.MINIMAL`. I also replaced the deprecated `DateTimeFormatter.format(Instant)` with `ZonedDateTime.now(ZoneId.systemDefault()).format(formatter)`.

Furthermore, I replaced the `Configuration.getInstance().getProperties().getStringArray("tsp_sources")` with a hardcoded array of TSP sources, since the original code snippet does not provide the `Configuration` class. You can replace it with the appropriate configuration if needed.