```java
import eu.europa.esig.dss.pades.CertificationPermission;

import java.io.IOException;
import java.security.cert.X509Certificate;

public class Signer {

    public static void main(String[] args) throws IOException {
        // Get the certificate from the command line arguments
        String certPath = args[0];
        X509Certificate certificate = CertificateUtils.loadCertificate(certPath);

        // Create a new CertificationPermission object
        CertificationPermission permission = new CertificationPermission(certificate);

        // Print the permission to the console
        System.out.println(permission);
    }
}
```