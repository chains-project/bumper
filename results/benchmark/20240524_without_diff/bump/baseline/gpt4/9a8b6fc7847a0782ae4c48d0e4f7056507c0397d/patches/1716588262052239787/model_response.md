```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new PasswordEncoder();
    try {
        Class<?> clazz = Class.forName("org.jasypt.util.password.StrongPasswordEncryptor");
        Object instance = clazz.getDeclaredConstructor().newInstance();
        encoder.setPasswordEncryptor((PasswordEncryptor) instance);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return encoder;
}
```