The error message indicates that the import statement is failing because the symbol `CertificationPermission` cannot be found in the `eu.europa.esig.dss.pades` package. This could be due to a number of reasons, such as the class not being present in the version of the library being used, or the library not being correctly included in the project.

Unfortunately, without more information about the library and its versions, it's impossible to provide a specific solution. However, a general approach to solve this issue would be to check the version of the library being used and ensure it contains the `CertificationPermission` class. If the class is not present in the library, you may need to downgrade or upgrade the library version.

If the library is correctly included and the class is present in the library, the issue could be with the project's build path. In this case, you would need to check the project's build configuration and ensure the library is correctly included.

In any case, without the ability to change the library or its version, we cannot provide a code patch to fix this issue. The solution lies in the project configuration, not in the code itself.