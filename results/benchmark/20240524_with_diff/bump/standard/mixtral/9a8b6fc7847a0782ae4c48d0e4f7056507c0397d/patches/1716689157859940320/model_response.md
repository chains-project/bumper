Here'Fully Qualified Code’’’

@java.lang.Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
org.jasypt.util.text.TextEncryptor textEncryptor = new org.jasypt.util.text.StrongTextEncryptor();
encoder.setTextEncryptor(textEncryptor);
return encoder;
}

’’’