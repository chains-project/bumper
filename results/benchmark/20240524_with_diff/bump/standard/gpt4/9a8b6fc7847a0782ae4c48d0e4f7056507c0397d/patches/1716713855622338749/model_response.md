```java
@java.lang.Override
protected it.geosolutions.geostore.core.security.password.PasswordEncoder createStringEncoder() {
    it.geosolutions.geostore.core.security.password.PasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PasswordEncoder();
    try {
        java.lang.reflect.Method method = encoder.getClass().getMethod("setPasswordEncryptor", org.jasypt.util.password.StrongPasswordEncryptor.class);
        method.invoke(encoder, new org.jasypt.util.password.StrongPasswordEncryptor());
    } catch (java.lang.NoSuchMethodException | java.lang.IllegalAccessException | java.lang.reflect.InvocationTargetException e) {
        e.printStackTrace();
    }
    return encoder;
}
```