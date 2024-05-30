Here is the proposed patch for the failing client code:

```java
@java.lang.Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setTextEncryptor(new org.jasypt.util.text.StrongTextEncryptor());
    return encoder;
}
```

In this patch, we have replaced the deprecated `setPasswordEncryptor` method with the new `setTextEncryptor` method, and updated the constructor call accordingly. This should fix the error caused by the missing `setPasswordEncryptor` method.