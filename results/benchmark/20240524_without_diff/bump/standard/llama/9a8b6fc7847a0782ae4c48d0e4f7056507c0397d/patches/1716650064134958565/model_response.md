```java
@java.lang.Override
protected org.jasypt.spring.security.PBEPasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        org.jasypt.encryption.pbe.StandardPBEStringEncryptor stringEncryptor = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncryptor.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncryptor.setProviderName(getProviderName());
        }
        stringEncryptor.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security.PBEPasswordEncoder encoder = new org.jasypt.spring.security.PBEPasswordEncoder(stringEncryptor);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```