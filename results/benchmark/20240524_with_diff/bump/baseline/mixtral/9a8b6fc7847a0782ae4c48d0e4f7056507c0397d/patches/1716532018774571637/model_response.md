Here's the fixed version of the method:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new PasswordEncoder();
    encoder.setPasswordEncryptor(new org.jasypt.util.password.StandardStringDigester());
    return encoder;
}
```

In this version, I replaced the removed `StrongPasswordEncryptor` with the new `StandardStringDigester` class, which is an alternative for password encryption.