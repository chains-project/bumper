```java
@java.lang.Override
protected it.geosolutions.geostore.core.security.password.PasswordEncoder createStringEncoder() {
    it.geosolutions.geostore.core.security.password.PasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PasswordEncoder();
    // No method to set password encryptor in the new version
    return encoder;
}
```