```java
	protected PasswordEncoder createStringEncoder() {
		PasswordEncoder encoder = new PasswordEncoder();
		StringDigester digester = new StringDigester();
		digester.setAlgorithm("SHA-1");
		digester.setIterations(1024);
		encoder.setStringDigester(digester);
		return encoder;
	}
```