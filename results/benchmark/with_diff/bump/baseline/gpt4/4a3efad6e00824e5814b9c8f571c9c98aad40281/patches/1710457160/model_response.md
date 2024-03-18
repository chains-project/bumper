As the error message suggests, the class `CertificationPermission` is not found in the package `eu.europa.esig.dss.pades`. This might be due to a change in the library's structure in the new version. Without the exact changes in the library, it's hard to provide an accurate solution. However, assuming the `CertificationPermission` class has been moved to a different package, you can import it from its new location.

For example, if `CertificationPermission` has been moved to `eu.europa.esig.dss`, you can change the import statement like this:

```java
import eu.europa.esig.dss.CertificationPermission;
```

Again, the exact solution depends on the changes made in the new version of the library. You may need to consult the library's documentation or source code to find the new location of the `CertificationPermission` class.