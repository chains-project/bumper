```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        org.jasypt.encryption.pbe.StandardPBEStringEncryptor stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.acegisecurity.providers.encoding.PasswordEncoder encoder = new org.acegisecurity.providers.encoding.PasswordEncoder() {
            @java.lang.Override
            public java.lang.String encodePassword(java.lang.String rawPass, java.lang.Object salt) {
                return stringEncrypter.encryptPassword(rawPass);
            }

            @java.lang.Override
            public bool isPasswordValid(java.lang.String encPass, java.lang.String rawPass, java.lang.Object salt) {
                return stringEncrypter.checkPassword(rawPass, encPass);
            }
        };
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```