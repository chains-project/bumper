```java
  @Override
	    protected PasswordEncoder createStringEncoder() {
	        PasswordEncoder encoder = new PasswordEncoder();
	        encoder.setStringDigester(new StrongPasswordEncryptor());
	        return encoder;
	    }
```