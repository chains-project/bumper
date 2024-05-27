Here is the patched code:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        org.jasypt.encryption.pbe.StandardPBEStringEncryptor stringEncryptor = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncryptor.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncryptor.setProviderName(getProviderName());
        }
        stringEncryptor.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security3.PasswordEncoder encoder = new org.jasypt.spring.security3.PasswordEncoder();
        encoder.setStringEncryptor(stringEncryptor);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```