```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new BCryptPasswordEncoder();
    return encoder;
}
```