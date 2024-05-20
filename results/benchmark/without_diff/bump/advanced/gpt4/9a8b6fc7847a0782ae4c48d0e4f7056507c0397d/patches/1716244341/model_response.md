```java
@java.lang.Override
protected it.geosolutions.geostore.core.security.password.PasswordEncoder createStringEncoder() {
    it.geosolutions.geostore.core.security.password.PasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PasswordEncoder();
    encoder.setPasswordEncryptor(new org.jasypt.util.passwordconfig.StringDigester());
    return encoder;
}
```