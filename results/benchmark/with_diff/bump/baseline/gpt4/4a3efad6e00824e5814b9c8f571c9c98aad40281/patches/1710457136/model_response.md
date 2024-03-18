Based on the error message, the class `CertificationPermission` is not found in the package `eu.europa.esig.dss.pades`. However, without knowing the changes in the new library version, it's impossible to provide a specific fix.

Assuming the `CertificationPermission` class was moved to a different package, the fix would be to import it from its new location. For example, if it was moved to `eu.europa.esig.dss.cert`, the import statement would change to:

```java
import eu.europa.esig.dss.cert.CertificationPermission;
```

If the `CertificationPermission` class was removed entirely, you'd need to replace its usage with an equivalent class or functionality from the updated library. Without knowing the specifics of the library update, it's impossible to provide a specific replacement.

Please provide the changes in the new library version to get a more accurate solution.