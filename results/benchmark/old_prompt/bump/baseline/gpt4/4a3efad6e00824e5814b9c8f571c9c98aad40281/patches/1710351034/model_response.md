This error message indicates that the CertificationPermission class cannot be found in the eu.europa.esig.dss.pades package. 

This could be due to several reasons:

1. The library (DSS) containing this class is not properly included in the project.
2. The version of the library does not contain this class.
3. The class has been moved to a different package in a newer version of the library.

Without knowing the exact details of the library version and its contents, I can't provide an exact fix. However, I can suggest some possible solutions:

1. If the library is not included, you should add it to your project dependencies.
2. If the library version is incorrect, you should update it to a version that contains the CertificationPermission class.
3. If the class has been moved to a different package, you should change the import statement to reflect this.

Please check these possibilities and adjust your code accordingly. If the class has been moved to a different package, your import statement might look something like this:

```java
import eu.europa.esig.someOtherPackage.CertificationPermission;
```

Replace "someOtherPackage" with the correct package name. If the class has been removed altogether, you will need to find an alternative way to achieve the functionality provided by the CertificationPermission class in the version of the library you are using.