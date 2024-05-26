Here'ed the updated `createStringEncoder` method with the necessary changes:
```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        StringEncryptor stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncryp9.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security3.PasswordEncoder encoder = new org.jasypt.spring.security3.PasswordEncoder();
        encoder.setStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```
The key changes are:

- `org.jasypt.spring.security.PBEPasswordEncoder` has been replaced with `org.jasypt.spring.security3.PasswordEncoder`
- `org.jasypt.spring.security.PBEPasswordEncoder.setPbeStringEncryptor` has been replaced with `org.jasypt.spring.security3.PasswordEncoder.setStringEncryptor`
- `org.jasypt.spring.security.PBEPasswordEncoder` has been removed, the new class is `org.jasypt.spring.security3.PasswordEncoder`