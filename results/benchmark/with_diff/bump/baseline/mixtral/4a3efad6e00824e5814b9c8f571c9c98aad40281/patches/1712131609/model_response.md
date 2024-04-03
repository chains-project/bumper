I've proposed a patch for the `Signer.java` class below. I fixed the error by replacing the `CertificationPermission` import with the correct one based on the new library version.

```java
import eu.europa.esig.dss.pades.PadesCertificationLevel;

//...

@Override
public void setCertificationLevel(CertificationLevel certificationLevel) {
    if (certificationLevel != null) {
        this.certificationLevel = PadesCertificationLevel.getCertificationLevel(certificationLevel.name());
    }
}
```

In the new library version, `CertificationPermission` is removed and replaced with `PadesCertificationLevel`. I replaced the `CertificationPermission` with `PadesCertificationLevel` and updated the `setCertificationLevel` method accordingly.