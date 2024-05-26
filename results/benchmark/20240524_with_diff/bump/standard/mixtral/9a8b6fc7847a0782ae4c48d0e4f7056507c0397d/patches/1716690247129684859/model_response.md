Here is a possible patch for the failing method:
```java
@Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        org.jasypt.encryption.pbe.PBEStringEncryptor encryptor = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        encryptor.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            encryptor.setProviderName(getProviderName());
        }
        encryptor.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
        encoder.setPasswordEncryptor(encryptor);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```
The main changes in this patch are:

* Replace the deprecated `PBEPasswordEncoder` class with the new `PasswordEncoder` class from the `org.jasypt.spring.security` package.
* Replace the deprecated `setPbeStringEncryptor` method with the new `setPasswordEncryptor` method.
* Remove the `PBEPasswordEncoder` object, since it is no longer needed.
* Add the necessary import statements for the new classes and methods.

Note that this patch assumes that the new version of the library includes a compatible implementation of the `PasswordEncoder` interface. If that is not the case, additional changes may be needed.