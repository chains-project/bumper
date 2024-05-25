```java
import eu.europa.esig.dss.pades.CertificationPermission;

import java.util.Arrays;
import java.util.List;

public class Signer {

    public static void main(String[] args) {
        List<String> permissions = Arrays.asList(
                CertificationPermission.SIGN_AND_ADD_REVOCATION_INFORMATION.toString(),
                CertificationPermission.SIGN_AND_ADD_TIMESTAMP.toString(),
                CertificationPermission.SIGN_AND_ADD_CERT_VALUES.toString(),
                CertificationPermission.SIGN_AND_ADD_OCSP.toString(),
                CertificationPermission.SIGN_AND_ADD_CRL.toString(),
                CertificationPermission.SIGN_AND_ADD_CERTS.toString(),
                CertificationPermission.SIGN.toString(),
                CertificationPermission.ADD_REVOCATION_INFORMATION.toString(),
                CertificationPermission.ADD_TIMESTAMP.toString(),
                CertificationPermission.ADD_CERT_VALUES.toString(),
                CertificationPermission.ADD_OCSP.toString(),
                CertificationPermission.ADD_CRL.toString(),
                CertificationPermission.ADD_CERTS.toString(),
                CertificationPermission.ADD_SIGNATURE_POLICY.toString(),
                CertificationPermission.ADD_SIGNATURE_POLICY_QUALIFIER.toString());

        for (String permission : permissions) {
            System.out.println(permission);
        }
    }
}
```