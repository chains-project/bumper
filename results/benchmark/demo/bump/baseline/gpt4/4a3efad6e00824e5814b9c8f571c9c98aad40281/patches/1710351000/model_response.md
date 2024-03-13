The error message indicates that the symbol `CertificationPermission` can't be found. This could be due to a number of reasons, such as the package not being available or the class not being present in the package.

However, given the constraints provided, there's not much we can change in the import statement itself. It's possible that the package has been updated and the `CertificationPermission` class is no longer present, or its location has changed.

You should check the documentation of the `eu.europa.esig.dss.pades` package to see if the `CertificationPermission` class has been moved or renamed. If it has, you should change the import statement to reflect the new location or name.

Without specific details on the package update, it's impossible to provide a specific code fix. However, if for example, the class had been renamed to `CertificationPermissions`, the updated code would look like this:

```java
import eu.europa.esig.dss.pades.CertificationPermissions;
```

Remember to replace `CertificationPermissions` with the actual new location or name of the class.