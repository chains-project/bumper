Here's a proposed patch that you can apply to the given code:
```java
protected Session session() throws IOException {
    final File file = File.createTempFile("jcabi-ssh", ".key");
