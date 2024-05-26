```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
  // TODO: review this AI generated patch!
  final String path = "path";
  final String repository = "repository";
  final String tag = "tag";
  final String digest = "digest";
  final String auth = "auth";
  final String dockerPath = path + "/" + repository + "/" + tag;
  final String dockerDigestPath = dockerPath + "/" + digest;
  final String dockerAuthPath = dockerPath + "/" + auth;
  final String dockerDigestAuthPath = dockerPath + "/" + digest + "/" + auth;

  org.junit.jupiter.api.Assertions.assertThrows(
      com.artipie.docker.http.DockerException.class,
      () -> new com.artipie.docker.http.UploadEntityRequest(
          dockerPath,
          dockerDigestPath,
          dockerAuthPath,
          dockerDigestAuthPath,
          new com.artipie.http.Headers.From(new com.artipie.asto.Content.Empty())
      )
  );
}
```