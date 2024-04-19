```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void testScope() {
    final java.lang.String line = "GET /resource.txt HTTP/1.1";
    final java.lang.String action = "foo:bar:baz";
    final java.util.concurrent.atomic.AtomicReference<java.lang.String> caction = new java.util.concurrent.atomic.AtomicReference<>();
    final java.util.concurrent.atomic.AtomicReference<java.lang.String> cline = new java.util.concurrent.atomic.AtomicReference<>();
    final java.util.function.Function<java.lang.String, java.lang.String> f = java.lang.String::trim;
    final java.lang.String[] split = line.split(" ");
    caction.set(split[1]);
    cline.set(split[2]);
}
```