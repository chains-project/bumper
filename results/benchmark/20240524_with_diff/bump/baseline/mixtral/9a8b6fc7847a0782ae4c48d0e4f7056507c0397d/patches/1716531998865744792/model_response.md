Here's the fixed version of the method:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new PasswordEncoder();
    encoder.setPasswordEncryptor(new org.jasypt.util.password.StandardStringDigester());
    return encoder;
}
```

I replaced the `StrongPasswordEncryptor` with `StandardStringDigester` since the `StrongPasswordEncryptor` has been removed and `StandardStringDigester` is a similar alternative.