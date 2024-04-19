```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void testScope() {
    final java.lang.String line = "GET /resource.txt HTTP/1.1";
    final java.lang.String action = "foo:bar:baz";
    final java.util.concurrent.atomic.AtomicReference<java.lang.String> caction = new java.util.concurrent.atomic.AtomicReference<>();
    final java.util.concurrent.atomic.AtomicReference<java.lang.String> cline = new java.util.concurrent.atomic.AtomicReference<>();
    final java.lang.String[] parts = line.split(" ");
    if (parts.length >= 3) {
        caction.set(parts[1]);
        cline.set(parts[2]);
    }
}
```