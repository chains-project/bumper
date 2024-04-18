```java
@Override
protected PasswordEncoder createStringEncoder() {
	byte[] password = lookupPasswordFromKeyStore();
	char[] chars = toChars(password);
	try {
		stringEncrypter = new StandardPBEStringEncryptor();
		stringEncrypter.setPasswordCharArray(chars);

		if (getProviderName() != null && !getProviderName().isEmpty()) {
			stringEncrypter.setProviderName(getProviderName());
		}
		stringEncrypter.setAlgorithm(getAlgorithm());

		org.springframework.security.crypto.password.PasswordEncoder encoder = new org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder();
		return encoder;
	} finally {
		scramble(password);
		scramble(chars);
	}
}
```