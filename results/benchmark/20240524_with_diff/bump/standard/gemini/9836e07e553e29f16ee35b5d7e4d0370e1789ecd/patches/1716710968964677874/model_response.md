```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
  // TODO: review this AI generated patch!
  assertThrows(
      org.junit.jupiter.api.Assertions::assertThrows,
      IllegalArgumentException.class,
      () -> new com.artipie.docker.http.UploadEntityRequest(
          new com.artipie.http.async.AsyncResponse(),
          "foo",
          new com.artipie.http.Headers.From(new java.util.HashMap<>()),
          () -> java.util.stream.Stream.empty(),
          java.nio.file.Paths.get("/tmp/foo/bar"),
          new com.artipie.docker.http.auth.Authentication.Simple("user", "password")));
}
```