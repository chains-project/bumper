```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    final java.lang.String digest = original.digest();
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(false, java.lang.String.format("latest: digest: %s", digest)));
}
```