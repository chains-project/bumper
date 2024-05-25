```java
  @Override
	    protected PasswordEncoder createStringEncoder() {
	        PasswordEncoder encoder = new PasswordEncoder();
	        encoder.setPasswordEncryptor(new ConfigurablePasswordEncryptor());
	        return encoder;
	    }
```