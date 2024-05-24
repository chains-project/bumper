```java
@Override
	    protected PasswordEncoder createStringEncoder() {
	        StrongPasswordEncryptor encryptor = new StrongPasswordEncryptor();
	        PasswordEncoder encoder = new PasswordEncoder();
	        encoder.setStringDigester(encryptor);
	        return encoder;
	    }
```