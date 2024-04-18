It seems that the `CertificationPermission` class is not available in the `org.openpdfsign` package. This class is part of the Java Standard Library, and it's not clear why it would be missing from the `org.openpdfsign` package.


To fix this error, you could try adding the following import statement to the `Signer` class:
```
import java.security.cert.CertificationPermission;
```
Alternatively, you could try using the fully qualified name of the class, `java.security.cert.CertificationPermission`, instead of the variable name `CertificationPermission`.

It's also possible that there's a problem with the dependencies or the build process of the `org.openpdfsign` package, and the `CertificationPermission` class is not being included in the package. In that case, you may need to check the dependencies and build process of the package to ensure that it includes all necessary classes.