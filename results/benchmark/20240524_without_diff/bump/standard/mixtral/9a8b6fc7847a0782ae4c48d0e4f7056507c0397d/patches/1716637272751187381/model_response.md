Here'm the updated code which uses the added library method `it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(byte[] password)` instead of the removed library method `it.geosolution.geostore.core.security.password.SecurityUtils.toChars(byte[] password)`:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        stringEncryptypt = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security.PBEPasswordEncoder encoder = new org.jasypt.spring.security.PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

Note that I's assumed that the missing library method `it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(byte[] password)` has been replaced with a new library method `it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(byte[] password)` which has the same functionality.