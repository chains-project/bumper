```java
@Bean
    public PasswordEncoder passwordEncoder() {
        StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();
        passwordEncryptor.setPasswordEncoder(new PBEStringEncryptor());
        return passwordEncryptor;
    }
```