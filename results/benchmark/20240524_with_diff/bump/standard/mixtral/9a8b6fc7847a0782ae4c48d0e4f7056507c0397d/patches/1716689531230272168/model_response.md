Here's a possible patch for the given client code:
```java
@Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
        encoder.setPasswordEncryptor(stringEncrypter);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```
The changes I made are:

* Replace `it.geosolutions.geostore.core.security.password.PBEPasswordEncoder` with `org.jasypt.spring.security.PasswordEncoder`
* Replace `setPbeStringEncryptor` with `setPasswordEncryptor`

Note that the `PBEPasswordEncoder` class has been removed in the new library version, and replaced with the `PasswordEncoder` class. The `setPbeStringEncryptor` method has also been removed, and replaced with the `setPasswordEncryptor` method.