```java
  protected PasswordEncoder createStringEncoder() {
		byte[] password = lookupPasswordFromKeyStore();
		char[] chars = toChars(password);
		PBEStringEncryptor stringEncrypter = new PBEStringEncryptor();
		stringEncrypter.setPasswordCharArray(chars);
		if (getProviderName() != null && !getProviderName().isEmpty()) {
			stringEncrypter.setProviderName(getProviderName());
		}
		stringEncrypter.setAlgorithm(getAlgorithm());
		PBEPasswordEncoder encoder = new PBEPasswordEncoder();
		encoder.setStringEncryptor(stringEncrypter);
		return encoder;
	}
```