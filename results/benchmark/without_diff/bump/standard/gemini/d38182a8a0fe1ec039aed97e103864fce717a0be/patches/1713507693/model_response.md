```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void testScope() {
    final java.lang.String line = "GET /resource.txt HTTP/1.1";
    final java.lang.String action = "foo:bar:baz";
    final java.util.concurrent.atomic.AtomicReference<java.lang.String> caction = new java.util.concurrent.atomic.AtomicReference<>();
    final java.util.concurrent.atomic.AtomicReference<java.lang.String> cline = new java.util.concurrent.atomic.AtomicReference<>();
    final java.util.concurrent.atomic.AtomicReference<java.util.Optional<java.util.List<java.util.Optional<com.github.dockerjava.api.command.AuthConfig>>>> authConfigOpt = new java.util.concurrent.atomic.AtomicReference<>();
    authConfigOpt.set(java.util.Optional.empty());
    caction.set(action);
    cline.set(line);
    org.mockito.stubbing.Answer<java.util.List<java.util.Optional<com.github.dockerjava.api.command.AuthConfig>>> answer = invocation -> authConfigOpt.get().stream().collect(java.util.stream.Collectors.toList());
    org.mockito.Mockito.when(docker.authConfig(action, line)).thenAnswer(answer);
    new com.artipie.docker.http.AuthScopeSlice(docker, caction::set).accept(cline::set);
    org.junit.jupiter.api.Assertions.assertTrue(caction.get().equals("foo:bar:baz"));
}
```