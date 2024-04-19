Here's a proposed patch for the failing client code:

```java
import eu.europa.esig.dss.pades.PadesCertificationLevel;

// ...

public class Signer {
    // ...

    @Override
    protected CertificationLevel getCertificationLevel() {
        return PadesCertificationLevel.CERTIFY_DETACHED;
    }

    // ...
}
```

In this patch, I replaced the `CertificationPermission` import with `eu.europa.esig.dss.pades.PadesCertificationLevel`. Then, I changed the `getCertificationLevel` method to return a `PadesCertificationLevel` instance, which is an added library method in the new version. This should resolve the "cannot find symbol" error for `CertificationPermission`.