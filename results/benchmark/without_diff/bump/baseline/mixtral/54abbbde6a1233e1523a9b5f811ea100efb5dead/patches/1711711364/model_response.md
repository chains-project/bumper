Here's a proposed patch to fix the issue:

```java
protected Session session() throws IOException {
    final File file = File.createTempFile("jcabi-ssh", ".key");
