```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void testScope() {
    final java.lang.String line = "GET /resource.txt HTTP/1.1";
    final java.lang.String action = "foo:bar:baz";
    final java.util.concurrent.atomic.AtomicReference<java.lang.String> caction = new java.util.concurrent.atomic.AtomicReference<>();
    final java.util.concurrent.atomic.AtomicReference<java.lang.String> cline = new java.util.concurrent.atomic.AtomicReference<>();
    final com.artipie.http.client.auth.AuthenticationScope scope = new com.artipie.http.client.auth.AuthenticationScope(line, action);
    caction.set(scope.action());
    cline.set(scope.line());
}
```