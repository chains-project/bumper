@java.lang.Override
protected org.springframework.security.crypto.password.PasswordEncoder createStringEncoder() {
    return new org.springframework.security.crypto.password.Pbkdf2PasswordEncoder();
}