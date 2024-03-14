As the error message indicates that the class `CertificationPermission` cannot be found in the package `eu.europa.esig.dss.pades`, it's likely that the class has been moved or removed in the new library version. Without the complete change log of the library, it's difficult to provide a precise solution.

However, in most cases, you should look for a similar class or a class that provides similar functionality in the new library version. If such class exists, replace the import statement with the new class.

For example, if the `CertificationPermission` class has been replaced by a class named `NewCertificationPermission` in the same package, the import statement should be changed as follows:

```java
import eu.europa.esig.dss.pades.NewCertificationPermission;
```

If the class has been moved to a different package, let's say `eu.europa.esig.dss.newpades`, the import statement should be:

```java
import eu.europa.esig.dss.newpades.CertificationPermission;
```

Please replace `NewCertificationPermission` and `eu.europa.esig.dss.newpades` with the actual class and package names from the new library version.