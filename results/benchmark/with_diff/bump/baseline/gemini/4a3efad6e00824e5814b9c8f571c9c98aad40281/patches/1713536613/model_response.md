```java
import eu.europa.esig.dss.pades.Certification;

import java.util.List;

public class Signer {

    public void sign(byte[] data, String signatureAlgorithm, String digestAlgorithm, List<Certification> certifications) {
        // ...
    }

}
```