```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    org.jasypt.encryption.pbe.StandardPBEStringEncryptor stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
    stringEncrypter.setPasswordCharArray(chars);
    if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
        stringEncrypter.setProviderName(getProviderName());
    }
    stringEncrypter.setAlgorithm(getAlgorithm());
    it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
    encoder.setPbeStringEncryptor(stringEncrypter);
    return encoder;
}
```